#!/usr/bin/env python3
"""Exact finite-graph certificate for elementary CA first-offender growth.

No numerical fitting is used to decide the growth classes. Run as
python verify.py in the directory containing classification.csv.
"""
import csv
from collections import Counter, defaultdict, deque
from pathlib import Path


def transitions(rule):
    # Four de Bruijn vertices (left,center), coded 0..3.
    # 0 is the empty subset; 15 is the full four-vertex subset.
    out = [[0, 0] for _ in range(16)]
    for subset in range(16):
        for leftcenter in range(4):
            if subset & (1 << leftcenter):
                for right in (0, 1):
                    input_triple = 2 * leftcenter + right
                    output = (rule >> input_triple) & 1
                    dest = 2 * (leftcenter & 1) + right
                    out[subset][output] |= 1 << dest
    return out


def graph(rule, first):
    d = transitions(rule)
    start = (d[15][first], 15)
    if not start[0]:
        return None
    reachable = {start}
    todo = deque([start])
    edge = {}
    back = defaultdict(set)
    while todo:
        u = todo.popleft()
        vlist = []
        for symbol in (0, 1):
            q = d[u[0]][symbol]
            if q:
                v = (q, d[u[1]][symbol])
                vlist.append(v)  # retained with multiplicity by distinct labels
                back[v].add(u)
                if v not in reachable:
                    reachable.add(v)
                    todo.append(v)
        edge[u] = vlist
    targets = {u for u in reachable if any(
        d[u[0]][last] == 0 and d[u[1]][last] != 0
        for last in (0, 1))}
    useful = set(targets)
    todo = deque(targets)
    while todo:
        for v in back[todo.popleft()]:
            if v not in useful:
                useful.add(v)
                todo.append(v)
    if start not in useful:
        return None
    return start, targets, {u: [v for v in edge[u] if v in useful]
                            for u in useful}


def tarjan(edges):
    next_id = 0
    numbers, lowlink, stack, active, components = {}, {}, [], set(), []
    def visit(v):
        nonlocal next_id
        numbers[v] = lowlink[v] = next_id
        next_id += 1
        stack.append(v)
        active.add(v)
        for w in edges[v]:
            if w not in numbers:
                visit(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in active:
                lowlink[v] = min(lowlink[v], numbers[w])
        if lowlink[v] == numbers[v]:
            members = []
            while True:
                w = stack.pop()
                active.remove(w)
                members.append(w)
                if w == v:
                    break
            components.append(members)
    for u in sorted(edges):
        if u not in numbers:
            visit(u)
    return components


def analyze_graph(G):
    if G is None:
        return 'finite', 0, 0
    start, targets, edges = G
    components = tarjan(edges)
    owner = {u: i for i, c in enumerate(components) for u in c}
    dag = [set() for _ in components]
    cyclic = [False] * len(components)
    branching = [False] * len(components)
    for i, comp in enumerate(components):
        cyclic[i] = len(comp) > 1 or comp[0] in edges[comp[0]]
        for u in comp:
            internal = 0
            for v in edges[u]:
                if owner[v] == i:
                    internal += 1
                else:
                    dag[i].add(owner[v])
            if cyclic[i] and internal > 1:
                branching[i] = True
    chain = {}
    def count_cycles(i):
        if i not in chain:
            chain[i] = int(cyclic[i]) + max(
                [count_cycles(j) for j in dag[i]] or [0])
        return chain[i]
    max_chain = count_cycles(owner[start])
    if any(branching):
        return 'exponential', max_chain, -1
    if max_chain > 1:
        return 'polynomial', max_chain, -1
    if max_chain == 1:
        return 'bounded', max_chain, -1
    # Productive graph is acyclic. The largest accepted v length is exact.
    distances = {}
    def length(u):
        if u not in distances:
            distances[u] = max(
                ([0] if u in targets else []) + [1 + length(v)
                                                  for v in edges[u]])
        return distances[u]
    return 'finite', 0, 2 + length(start)


def classify(rule):
    results = [analyze_graph(graph(rule, bit)) for bit in (0, 1)]
    order = ['finite', 'bounded', 'polynomial', 'exponential']
    kind = max((z[0] for z in results), key=order.index)
    longest = max(z[2] for z in results)
    d = transitions(rule)
    absent_one = any(not d[15][bit] for bit in (0, 1))
    longest = max(longest, int(absent_one))
    if kind != 'finite':
        longest = -1
    return kind, longest


def exact_first_offender_counts(rule, count):
    # Distinct first-letter/start choices and middle words label separate paths.
    d = transitions(rule)
    ans = [sum(d[15][bit] == 0 for bit in (0, 1))]
    dp = Counter((d[15][bit], 15) for bit in (0, 1) if d[15][bit])
    for n in range(2, count+1):
        ans.append(sum(quantity for (q, r), quantity in dp.items()
                       for last in (0, 1) if d[q][last] == 0
                       and d[r][last] != 0))
        after = Counter()
        for (q, r), quantity in dp.items():
            for letter in (0, 1):
                q2 = d[q][letter]
                if q2:
                    after[q2, d[r][letter]] += quantity
        dp = after
    return ans


def direct_counts(rule, maxlen):
    # Independent enumerator: ALL length-(n+2) inputs, not subset transitions.
    previous_allowed = {''}
    counts = []
    for n in range(1, maxlen+1):
        words = set()
        for code in range(1 << (n+2)):
            bits = [(code >> i) & 1 for i in range(n+2)]
            out = []
            for i in range(n):
                triple = 4*bits[i] + 2*bits[i+1] + bits[i+2]
                out.append(str((rule >> triple) & 1))
            words.add(''.join(out))
        missing = 0
        for code in range(1 << n):
            s = format(code, '0%db' % n)
            if s not in words and s[:-1] in previous_allowed and s[1:] in previous_allowed:
                missing += 1
        counts.append(missing)
        previous_allowed = words
    return counts



def bounded_certificate(rule):
    """For bounded graphs, prove eventual periodicity by repeated exact vectors."""
    from math import lcm
    d = transitions(rule)
    pieces = []
    for first in (0, 1):
        G = graph(rule, first)
        if G is None:
            pieces.append(([0], 0, 1))
            continue
        start, targets, edges = G
        vertices = tuple(sorted(edges))
        index = {v: i for i, v in enumerate(vertices)}
        vector = [int(v == start) for v in vertices]
        seen = {}
        series = []
        while tuple(vector) not in seen:
            assert len(series) < 1000  # a generous finite-graph sanity limit, not a proof assumption
            seen[tuple(vector)] = len(series)
            series.append(sum(vector[index[v]] * sum(
                d[v[0]][last] == 0 and d[v[1]][last] != 0
                for last in (0, 1)) for v in vertices))
            following = [0] * len(vertices)
            for v in vertices:
                for w in edges[v]:
                    following[index[w]] += vector[index[v]]
            vector = following
        mu = seen[tuple(vector)]
        period = len(series) - mu
        assert period > 0
        pieces.append((series, mu, period))
    window = max(part[1] for part in pieces) + lcm(*(part[2] for part in pieces)) + 3
    def coeff(part, m):
        series, mu, period = part
        return series[m if m < len(series) else mu + (m-mu) % period]
    # n=1 also allows impossible one-symbol outputs.
    one_letter = sum(d[15][i] == 0 for i in (0, 1))
    outputs = [one_letter] + [sum(coeff(part, n-2) for part in pieces)
                             for n in range(2, window+1)]
    assert max(outputs) <= 2
    assert any(outputs[2:])
    # The exact recurrence state has already repeated, so comparing through
    # this window proves the following formula for every length, not just a
    # sampled prefix.
    A = {27, 39, 53, 83, 172, 202, 216, 228}
    B = {38, 44, 52, 100, 155, 203, 211, 217}
    C = {46, 116, 139, 209}
    D = {58, 78, 92, 114, 141, 163, 177, 197}
    if rule in A:
        predicted = lambda n: int(n == 4 or n >= 7)
    elif rule in B:
        predicted = lambda n: int(n >= 4 and n % 2 == 0)
    elif rule in C:
        predicted = lambda n: int(n >= 3 and n % 2 == 1)
    else:
        assert rule in D
        predicted = lambda n: 1 if n == 4 else 2 if n >= 7 else 0
    assert outputs == [predicted(n) for n in range(1, window+1)], rule
    return tuple(outputs)

def run():
    csvfile = Path(__file__).resolve().with_name('classification.csv')
    rows = list(csv.DictReader(csvfile.open(encoding='utf-8', newline='')))
    assert len(rows) == 256 and [int(r['rule']) for r in rows] == list(range(256))
    hist = Counter()
    finite_lengths = Counter()
    bounded_types = set()
    for rule in range(256):
        kind, maximum = classify(rule)
        row = rows[rule]
        assert (row['growth_class'], int(row['max_min_forbidden_length'])) == (kind, maximum), rule
        hist[kind] += 1
        if kind == 'finite':
            finite_lengths[maximum] += 1
        if kind == 'bounded':
            bounded_types.add(tuple(exact_first_offender_counts(rule, 24)))
            assert max(bounded_certificate(rule)) <= 2
        # Independent comparison with raw neighborhood enumeration.
        observed = direct_counts(rule, 9)
        predicted = exact_first_offender_counts(rule, 9)
        assert observed == predicted, (rule, observed, predicted)
    assert hist == {'finite':176, 'bounded':28, 'exponential':52}
    assert hist['polynomial'] == 0
    assert max(finite_lengths) == 10
    assert [r for r in range(256) if rows[r]['growth_class']=='finite'
            and int(rows[r]['max_min_forbidden_length'])==10] == [57,99,156,198]
    assert len(bounded_types) == 4
    print('VERIFY_OK: 256 exhaustive first-offender graphs; 176 finite / 28 bounded / 52 exponential;')
    print('no polynomial-growth class; finite maximum length 10 at rules 57, 99, 156, 198;')
    print('four bounded signatures with exact ultimate-periodicity certificates; 2304 direct image tests')

if __name__ == '__main__':
    run()
