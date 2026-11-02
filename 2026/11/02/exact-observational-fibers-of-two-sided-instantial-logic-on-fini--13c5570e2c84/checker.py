"""Direct finite semantic checks for two-sided positive instantial neighborhoods on chains.
All masks encode upward-closed subsets of the chain."""
from itertools import product
from collections import Counter


def box(N, As, B):
    return any((U & ~B) == 0 and all(U & A for A in As) for U in N)


def diamond(N, As, B):
    return all(any((U & ~A) == 0 for A in As) or bool(U & B) for U in N)


def sig(N, op, upsets, arity):
    return tuple(op(N, args, B) for k in range(arity + 1)
                 for args in product(upsets, repeat=k) for B in upsets)


def classification(N, op, n):
    has_empty = int(0 in N)
    sizes = [x.bit_count() for x in N if x]
    return (has_empty, min(sizes) if op == 'box' else max(sizes)) if sizes else (has_empty, 0)


def main():
    for n in range(1, 7):
        masks = [sum(1 << i for i in range(n-j, n)) for j in range(n+1)]
        fams = [tuple(masks[i] for i in range(n+1) if f & (1 << i))
                for f in range(1 << (n+1))]
        for name, op in [('box', box), ('diamond', diamond)]:
            fibers = {}
            labels = {}
            for N in fams:
                s1 = sig(N, op, masks, 1)
                label = classification(N, name, n)
                if s1 in labels:
                    assert labels[s1] == label, (n,name, N, label)
                labels[s1] = label
                fibers.setdefault(label, set()).add(s1)
                assert sig(N, op, masks, 0) == s1[:n+1]
                if n <= 4:
                    # Independent direct check that all binary-instance tests
                    # are determined by the one-instance signature.
                    for A, C, B in product(masks, repeat=3):
                        reduced = (A & C) if name == 'box' else (A | C)
                        assert op(N, (A,C), B) == op(N, (reduced,), B)
            assert len(labels) == 2*n+2, (n,name,len(labels))
            assert all(len(v)==1 for v in fibers.values())
            group = Counter(classification(N, name, n) for N in fams)
            assert group[(0,0)] == 1 and group[(1,0)] == 1
            for j in range(1,n+1):
                expect = 2**(n-j) if name=='box' else 2**(j-1)
                assert group[(0,j)] == expect and group[(1,j)] == expect
            assert sum(group.values()) == 2**(n+1)
            assert max(group.values()) == 2**(n-1)
            print(f'n={n} {name}: {len(labels)} signatures; largest fiber {max(group.values())}; direct verified')
        assert (2*n+2)**2 <= 2**(2*n+2)
    print('ALL_CHECKS_OK')


if __name__=='__main__': main()
