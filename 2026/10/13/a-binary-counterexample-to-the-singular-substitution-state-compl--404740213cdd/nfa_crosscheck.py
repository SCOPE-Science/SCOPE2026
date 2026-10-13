"""Independent finite-language NFA/epsilon-substitution and DFA-minimization check.

This check constructs the finite languages explicitly for the short base
inputs, and does not use the maximal-generator derivative certificate.
"""


def all_scattered_subwords(w):
    S = {''}
    for c in w:
        S.update(x+c for x in tuple(S))
    return S


def finite_dfa(words):
    # A partial-prefix trie quotient construction; states are actual sets
    # of complete suffixes, including the empty rejection residual.
    prefixes = {''}
    for word in words:
        prefixes.update(word[:j] for j in range(len(word)+1))
    row_sets = {frozenset()}
    row_sets.update(frozenset(w[len(p):] for w in words if w.startswith(p)) for p in prefixes)
    states = list(row_sets)
    idx = {s:i for i,s in enumerate(states)}
    tr = [[idx[frozenset(w[1:] for w in s if w.startswith(c))] for c in 'ab'] for s in states]
    final = ['' in s for s in states]
    return tr, final, idx[frozenset(words)]


def substitute_and_minimize(base, repl):
    T,F,origin = base
    U,G,rep_origin = repl
    n,m = len(T),len(U)
    total = n*(m+1)
    eps = [[] for _ in range(total)]
    arc = [[[] for _ in range(2)] for _ in range(total)]

    # Idle states 0..n-1 correspond to the original DFA. The remaining
    # active states (q,r) track a word from K and the post-a state q.
    for q in range(n):
        arc[q][1].append(T[q][1])
        eps[q].append(n+T[q][0]*m+rep_origin)
        for r in range(m):
            p = n+q*m+r
            for j in range(2):
                arc[p][j].append(n+q*m+U[r][j])
            if G[r]:
                eps[p].append(q)

    def closure(seed):
        found = set(seed)
        stack = list(found)
        while stack:
            i = stack.pop()
            for j in eps[i]:
                if j not in found:
                    found.add(j)
                    stack.append(j)
        return frozenset(found)

    subsets = [closure([origin])]
    ids = {subsets[0]:0}
    edges = []
    accept = []
    for subset in subsets:
        accept.append(any(q<n and F[q] for q in subset))
        out=[]
        for j in range(2):
            follow=closure(t for q in subset for t in arc[q][j])
            if follow not in ids:
                ids[follow] = len(subsets)
                subsets.append(follow)
            out.append(ids[follow])
        edges.append(out)

    # Moore refinement of accessible deterministic subset automaton.
    colors=[int(v) for v in accept]
    while True:
        sigs=[(accept[i],colors[edges[i][0]],colors[edges[i][1]]) for i in range(len(edges))]
        new_ids={sig:j for j,sig in enumerate(sorted(set(sigs)))}
        next_colors=[new_ids[sig] for sig in sigs]
        if next_colors==colors:
            break
        colors=next_colors
    return len(set(colors)),len(subsets)


def main():
    L = ['aaaaaaa','baaaaaba']
    K = ['aababa']
    B=finite_dfa(set().union(*(all_scattered_subwords(w) for w in L)))
    R=finite_dfa(set().union(*(all_scattered_subwords(w) for w in K)))
    nfa_min, reachable_subsets=substitute_and_minimize(B,R)
    assert len(B[0])==15 and len(R[0])==8
    assert nfa_min==127 and reachable_subsets==337, (nfa_min,reachable_subsets)
    print('VERIFY_OK independent_epsilon_NFA=337 deterministic_subsets minimum=127 originals=15,8')

if __name__=='__main__':
    main()
