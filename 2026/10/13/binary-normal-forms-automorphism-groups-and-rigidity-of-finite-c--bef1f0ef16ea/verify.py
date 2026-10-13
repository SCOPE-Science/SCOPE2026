#!/usr/bin/env python3
"""Exact finite-chain support and symmetry checks for Bochvar normal forms."""
from itertools import permutations
from math import factorial

checks=0

def supports(k):
    """All strict descending chains of subsets, beginning at full support."""
    full=(1<<k)-1
    def extend(chain):
        yield tuple(chain)
        final=chain[-1]
        for nxt in range(final):
            if nxt & ~final == 0:
                yield from extend(chain+[nxt])
    return extend([full])


def stabilizer_formula(chain,k):
    sizes=[mask.bit_count() for mask in chain]
    blocks=[sizes[i]-sizes[i+1] for i in range(len(sizes)-1)]+[sizes[-1]]
    ans=1
    for x in blocks:
        ans *= factorial(x)
    return ans


def act(mask,p):
    return sum(1<<p[i] for i in range(len(p)) if mask>>i&1)

for k in range(0,8):
    by_n={}
    count=0
    for chain in supports(k):
        count+=1
        N=sum(1<<mask.bit_count() for mask in chain)
        by_n.setdefault(N,set()).add(tuple(mask.bit_count() for mask in chain))
        assert len(set(chain))==len(chain)
        assert all(chain[i+1] & ~chain[i] == 0 for i in range(len(chain)-1))
        assert N.bit_count()==len(chain)
        rigid_expected=any(N==(1<<t)-1 for t in range(1,k+3)) or any(N==(1<<t)-2 for t in range(2,k+3))
        assert (stabilizer_formula(chain,k)==1)==rigid_expected
        checks+=4
        # Every restriction P(S_i) -> P(S_j), (U -> U intersect S_j),
        # is surjective; and is iso on the interval [0,S_j] of the base.
        for j,S in enumerate(chain):
            for i in range(j):
                for u in range(1<<k):
                    if u & ~S == 0:
                        assert (u & chain[i]) & S == u
                        checks+=1
    assert set(by_n)==set(range(1<<k,1<<(k+1)))
    assert all(len(v)==1 for v in by_n.values())
    checks+=len(by_n)+1
    if k<=5:
        P=list(permutations(range(k)))
        for chain in supports(k):
            aut=sum(1 for p in P if all(act(S,p)==S for S in chain))
            assert aut==stabilizer_formula(chain,k)
            checks+=1
    print(f"k={k}: {count} labeled strict-support chains; {len(by_n)} distinct consecutive sizes; automorphism verified={k<=5}")
print(f"VERIFY_OK {checks} exact assertions; binary uniqueness through k=7; stabilizer symmetries through k=5")

# Independently build the complete Bochvar operation tables of every
# normal-form chain at bottom rank <=3; verify source Definition 3.1.
axiom_checks=0
for k in range(4):
    allmask=(1<<k)-1
    for chain in supports(k):
        carriers=[(i,t) for i,S in enumerate(chain) for t in range(1<<k) if t & ~S == 0]
        bot=(0,0); top=(0,allmask)
        def op(a,b,join):
            h=max(a[0],b[0]);S=chain[h]
            return (h, ((a[1] | b[1]) if join else (a[1] & b[1])) & S)
        def meet(a,b):return op(a,b,False)
        def join(a,b):return op(a,b,True)
        def neg(a):return (a[0],chain[a[0]]^a[1])
        def J(j,a):
            if j==2:return (0,a[1])
            if j==0:return (0,chain[a[0]]^a[1])
            return (0,allmask^chain[a[0]])
        assert len(carriers)==sum(1<<S.bit_count() for S in chain)
        axiom_checks+=1
        for a in carriers:
            assert join(a,a)==a and neg(neg(a))==a and join(bot,a)==a
            assert neg(top)==bot
            for j in range(3):
                assert join(J(j,a),neg(J(j,a)))==top
                assert J(2,J(j,a))==J(j,a)
                assert J(0,J(j,a))==neg(J(j,a))
                assert J(1,J(j,a))==bot
                assert J(j,neg(a))==J(2-j,a)
                for l in range(3):
                    assert meet(join(J(j,a),J(l,a)),J(j,a))==J(j,a)
            for (j,l,m) in permutations(range(3)):
                assert J(j,a)==neg(join(J(l,a),J(m,a)))
            for j in (1,2):
                assert join(a,J(j,a))==a
            axiom_checks+=36
            for b in carriers:
                assert join(a,b)==join(b,a)
                assert meet(a,b)==neg(join(neg(a),neg(b)))
                assert neg(join(a,b))==meet(neg(a),neg(b))
                assert J(0,join(a,b))==meet(J(0,a),J(0,b))
                assert J(2,join(a,b))==join(join(meet(J(2,a),J(2,b)),meet(J(2,a),J(2,neg(b)))),meet(J(2,neg(a)),J(2,b)))
                assert (J(0,a),J(1,a),J(2,a))!=(J(0,b),J(1,b),J(2,b)) or a==b
                axiom_checks+=6
                for c in carriers:
                    assert join(join(a,b),c)==join(a,join(b,c))
                    assert meet(a,join(b,c))==join(meet(a,b),meet(a,c))
                    axiom_checks+=2
print(f"VERIFY_AXIOMS_OK {axiom_checks} exact checks of all 19 Bochvar axioms/quasi-axiom over all canonical forms with k<=3")
