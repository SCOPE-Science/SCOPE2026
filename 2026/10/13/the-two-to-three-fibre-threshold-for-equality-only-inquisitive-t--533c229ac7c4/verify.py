#!/usr/bin/env python3
"""Standalone reproducibility checks for an equality-only inquisitive team formula.
Only Python's standard library is required. Finite tests supplement, not replace,
the quantified mathematical proof in RESULT.md.
"""
from itertools import combinations, product
from random import Random


def subsets(rows):
    rows = tuple(rows)
    for mask in range(1 << len(rows)):
        yield tuple(rows[j] for j in range(len(rows)) if (mask >> j) & 1)


def value_question(team, coordinate, domain):
    # Fully expand mu(t) = forall v( (v=t) inquisitive_or not(v=t) ).
    # Negation of equality is classical: no assignment may satisfy equality.
    return all(
        all(row[coordinate] == d for row in team)
        or all(row[coordinate] != d for row in team)
        for d in domain
    )


def dependence_via_implication(team, domain):
    # (mu(x) -> mu(y)): all subteams evaluated at both operands.
    return all(
        not value_question(y, 1, domain) or value_question(y, 2, domain)
        for y in subsets(team)
    )


def exists_missing_z(team, domain):
    # Inquisitive existential: one constant w works for the whole team.
    return any(all(row[0] != d for row in team) for d in domain)


def phi_by_team_semantics(team, domain):
    # ((mu(x)->mu(y)) -> inquisitive-exists w (w != z)).
    return all(
        not dependence_via_implication(y, domain)
        or exists_missing_z(y, domain)
        for y in subsets(team)
    )


def fd(team):
    seen = {}
    for z, x, y in team:
        if x in seen and seen[x] != y:
            return False
        seen[x] = y
    return True


def phi_by_witness_search(team, domain):
    return not any(fd(y) and {row[0] for row in y} == set(domain)
                   for y in subsets(team))


def two_sat_satisfiable(number_of_variables, clauses):
    """Clauses of 0..2 signed literals (index, positive_bool)."""
    k = number_of_variables
    graph = [[] for _ in range(2*k)]
    reverse = [[] for _ in range(2*k)]

    def node(lit):
        i, positive = lit
        return 2*i + (1 if positive else 0)

    def add_edge(a, b):
        graph[a].append(b)
        reverse[b].append(a)

    for clause in clauses:
        if not clause:
            return False
        if len(clause) == 1:
            u = node(clause[0]); add_edge(u ^ 1, u)
        else:
            assert len(clause) == 2
            u, v = map(node, clause)
            add_edge(u ^ 1, v)
            add_edge(v ^ 1, u)

    visited = [False] * (2*k)
    ordering = []
    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs(w)
        ordering.append(v)
    for v in range(2*k):
        if not visited[v]:
            dfs(v)
    component = [-1]*(2*k)
    def rdfs(v, c):
        component[v] = c
        for w in reverse[v]:
            if component[w] < 0:
                rdfs(w, c)
    c = 0
    for v in reversed(ordering):
        if component[v] < 0:
            rdfs(v, c)
            c += 1
    return all(component[2*i] != component[2*i+1] for i in range(k))


def polytime_witness_exists_fiber_at_most_two(team, domain):
    team = tuple(sorted(set(team)))
    pairs = sorted({(x,y) for z,x,y in team})
    idx = {pair:i for i,pair in enumerate(pairs)}
    clauses = []
    for d in domain:
        fiber = [row for row in team if row[0] == d]
        assert len(fiber) <= 2
        clauses.append([(idx[(x,y)], True) for z,x,y in fiber])
    for a,b in combinations(pairs, 2):
        if a[0] == b[0] and a[1] != b[1]:
            clauses.append([(idx[a],False), (idx[b],False)])
    return two_sat_satisfiable(len(pairs), clauses)


def reduce_exact_three_sat(clauses, p):
    """clauses use distinct variables and signed literal (variable, desired bit)."""
    assert p >= 2
    assert all(len(c) == 3 and len({v for v, b in c}) == 3 for c in clauses)
    m = len(clauses)
    n = max(m, p, 2)
    padded = list(clauses)
    # Three distinct rows per padding clause: (p0,1),(p0,0),(p1,1).
    while len(padded) < n:
        padded.append(((0,1), (0,0), (1,1)))
    team = frozenset((i, v, b)
                     for i, c in enumerate(padded) for v, b in c)
    assert all(sum(z == i for z,x,y in team) == 3 for i in range(n))
    assert all(b in (0, 1) for z,x,b in team)
    return range(n), team


def cnf_satisfiable(clauses, p):
    return any(all(any(bits[v] == b for v,b in clause) for clause in clauses)
               for bits in product((0,1), repeat=p))


def fd_cover_via_assignment(team, domain):
    # Independent of enumerating subteams; enumerate only choices for x-values.
    xvalues = sorted({x for z,x,y in team})
    return any(all(any(z == d and bits[xvalues.index(x)] == y
                       for z,x,y in team)
                   for d in domain)
               for bits in product((0,1), repeat=len(xvalues)))


def main():
    n_small = 0
    # Full direct semantics expanded from every operator: all teams on D of size two.
    for size in (1, 2):
        dom = tuple(range(size))
        universe = list(product(dom, repeat=3))
        for team in subsets(universe):
            for subteam in subsets(team):
                assert dependence_via_implication(subteam, dom) == fd(subteam)
            direct = phi_by_team_semantics(team, dom)
            witness = phi_by_witness_search(team, dom)
            assert direct == witness, ('formula', size, team)
            if max((sum(r[0] == z for r in team) for z in dom), default=0) <= 2:
                assert polytime_witness_exists_fiber_at_most_two(team, dom) == (not witness)
            n_small += 1
    rng = Random(269835)
    n_sparse = 0
    # Sparse three-valued teams: compare full semantic recursion with certificate.
    dom = tuple(range(3))
    allrows = list(product(dom, repeat=3))
    for _ in range(180):
        team = tuple(sorted(rng.sample(allrows, rng.randrange(0, 10))))
        assert phi_by_team_semantics(team, dom) == phi_by_witness_search(team, dom)
        if max((sum(r[0] == z for r in team) for z in dom), default=0) <= 2:
            assert polytime_witness_exists_fiber_at_most_two(team, dom) == (not phi_by_witness_search(team,dom))
        n_sparse += 1
    # Many-valued test of the 2-SAT lemma, including conflicts on >2 y-values.
    n_two_sat = 0
    dom4 = tuple(range(4))
    rows = list(product(dom4, repeat=3))
    for _ in range(1400):
        fibers = []
        for z in dom4:
            options = [row for row in rows if row[0] == z]
            fibers.extend(rng.sample(options, rng.randrange(3)))
        team = tuple(sorted(fibers))
        assert polytime_witness_exists_fiber_at_most_two(team, dom4) == (
            not phi_by_witness_search(team, dom4))
        n_two_sat += 1
    # Exhaust every three-valued team with at most two rows at each z.
    # This is (C(9,0)+C(9,1)+C(9,2))^3 = 46^3 = 97,336 teams.
    options3 = [()] + [(row,) for row in product(dom, repeat=2)]
    options3 += list(combinations(tuple(product(dom, repeat=2)), 2))
    n_exhaustive_two = 0
    for fibers in product(options3, repeat=3):
        team = tuple((z,x,y) for z, subset in enumerate(fibers) for x,y in subset)
        possible = False
        for bits in product(dom, repeat=3):
            if all(any(z == d and bits[x] == y for z,x,y in team) for d in dom):
                possible = True
                break
        assert possible == polytime_witness_exists_fiber_at_most_two(team, dom)
        n_exhaustive_two += 1
    # All 8 signed three-literal clauses on three distinct variables,
    # and every sequence of 1..4 such clauses (8 + 64 + 512 + 4096).
    options = [tuple((v, signs[v]) for v in range(3))
               for signs in product((0, 1), repeat=3)]
    n_reductions = 0
    for m in range(1,5):
        for clauses in product(options, repeat=m):
            dom, team = reduce_exact_three_sat(clauses, 3)
            source_sat = cnf_satisfiable(clauses, 3)
            target_fails = fd_cover_via_assignment(team, dom)
            assert source_sat == target_fails, ('3SAT',clauses)
            n_reductions += 1
    # Four propositional variables, random clauses with distinct positions.
    for _ in range(500):
        m = rng.randrange(1,7)
        clauses = []
        for j in range(m):
            vars_ = rng.sample(range(4),3)
            clauses.append(tuple((v,rng.randrange(2)) for v in vars_))
        dom, team = reduce_exact_three_sat(clauses,4)
        assert cnf_satisfiable(clauses,4) == fd_cover_via_assignment(team,dom)
        n_reductions += 1
    print('VERIFY_OK direct_teams=', n_small, 'sparse_teams=',n_sparse,
          'two_fiber_multi_value_cases=',n_two_sat,
          'three_value_exhaustive_two_fiber=',n_exhaustive_two,
          'sat_bridge_cases=',n_reductions)

if __name__ == '__main__':
    main()
