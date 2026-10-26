#!/usr/bin/env python3
"""Independent finite verification of the two-marker conjugacy DFA law.

No external dependencies.  A bottom-up minimization of the full prefix trie
provides one implementation; enumerated right quotients provide another.
Neither algorithm uses the analytic collision calculation.
"""


def conjugates(a, b):
    w = '1' + '0' * a + '1' + '0' * b
    return {w[i:] + w[:i] for i in range(len(w))}


def minimal_dfa_states(a, b):
    words = conjugates(a, b)
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node['#'] = True
    intern = {}
    def visit(node):
        signature = (bool(node.get('#')), visit(node['0']) if '0' in node else 0,
                     visit(node['1']) if '1' in node else 0)
        if signature not in intern:
            intern[signature] = len(intern) + 1
        return intern[signature]
    visit(root)
    return len(intern) + 1 # additional dead state, class id 0


def quotient_count(a, b):
    words = conjugates(a, b)
    n = a+b+2
    result = 1 # empty right language, i.e., dead state
    for k in range(n+1):
        classes = {}
        for w in words:
            classes.setdefault(w[:k], set()).add(w[k:])
        result += len({frozenset(s) for s in classes.values()})
    return result


def closed_form(a, b):
    ell, h = sorted((a,b))
    d = h-ell
    return (2*ell+4)*h + 4 - ell*ell - min(d*d,(ell+1)**2)


def main():
    cases = 0
    for a in range(24):
        for b in range(a,24):
            expected = closed_form(a,b)
            got = minimal_dfa_states(a,b)
            assert got == expected, (a,b,expected,got)
            cases += 1
    small = 0
    for a in range(9):
        for b in range(a,9):
            q = quotient_count(a,b)
            f = closed_form(a,b)
            assert q == f == minimal_dfa_states(a,b), (a,b,q,f)
            small += 1
    # independently test symmetry under exchanging the two zero gaps
    for a in range(11):
        for b in range(11):
            assert minimal_dfa_states(a,b) == minimal_dfa_states(b,a)
    print(f'PASS: {cases} independently minimized tries, {small} direct quotient inventories, symmetry through 10')
    print('Selected checks:',{(a,b):minimal_dfa_states(a,b) for a,b in [(0,0),(1,1),(2,2),(2,5),(3,5),(5,10)]})


if __name__ == '__main__':
    main()
