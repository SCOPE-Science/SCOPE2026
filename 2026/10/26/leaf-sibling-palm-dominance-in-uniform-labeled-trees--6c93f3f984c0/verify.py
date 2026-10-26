#!/usr/bin/env python3
"""Self-contained exact-arithmetic checks of leaf-sibling Palm identities.

All proofs for unrestricted sizes are contained in RESULT.md; exhaustive
finite checks here only detect mistakes in the derivation or transcription.
"""
from fractions import Fraction
from itertools import product
from collections import Counter
from math import comb, factorial


def evaluate_prufer(code, n):
    """Decode a labelled tree and count leaves and unordered sibling-leaf pairs."""
    deg = [1] * n
    for x in code:
        deg[x] += 1
    adj = [[] for _ in range(n)]
    work = deg[:]
    for x in code:
        leaf = next(i for i in range(n) if work[i] == 1)
        adj[leaf].append(x)
        adj[x].append(leaf)
        work[leaf] -= 1
        work[x] -= 1
    u,v = (i for i in range(n) if work[i] == 1)
    adj[u].append(v)
    adj[v].append(u)
    leaves = [len(a) == 1 for a in adj]
    C = sum(comb(sum(leaves[u] for u in a), 2) for a in adj)
    return sum(leaves), C


def numerator_palm_count(n, ell):
    # Conditional on an arbitrary fixed cherry, the contracted tree is
    # uniform on N=n-2 labels, its code length being N-2.
    N=n-2
    return sum((-1)**(j-k)*comb(j,k)*comb(N-1,j)*(N-j)**(N-2)
               for j in range(k,N)) if (k:=ell-2)>=0 else 0


def test():
    trials=0
    for n in range(4,9):
        joint=Counter()
        for code in product(range(n), repeat=n-2):
            L,C=evaluate_prufer(code,n)
            joint[L,C] += 1
            trials+=1
        total = n**(n-2)
        meanL = sum(L*v for (L,C),v in joint.items())
        meanC = sum(C*v for (L,C),v in joint.items())
        mix = sum(L*C*v for (L,C),v in joint.items())
        # Moment checks are exact fractions and do not evaluate floats.
        pC=Fraction((n-1)*(n-2)**(n-3),2*n**(n-3))
        pL=Fraction(n*(n-1)**(n-2),n**(n-2))
        pLp=Fraction(2,1)+Fraction((n-3)**(n-3),(n-2)**(n-4))
        assert Fraction(meanL,total)==pL,(n,'EL')
        assert Fraction(meanC,total)==pC,(n,'EC')
        assert Fraction(mix,meanC)==pLp,(n,'ELp')
        # Full Palm leaf law with coefficients from occupancy inclusion-exclusion.
        for ell in range(2,n+1):
            obs=Fraction(sum(C*v for (L,C),v in joint.items() if L==ell),meanC)
            rhs=Fraction(numerator_palm_count(n,ell),(n-2)**(n-4))
            assert obs==rhs,(n,ell,obs,rhs)
        # In each finite size, the Palm leaf law stochastically dominates.
        for threshold in range(n+1):
            a=Fraction(sum(C*v for (L,C),v in joint.items() if L>=threshold),meanC)
            b=Fraction(sum(v for (L,C),v in joint.items() if L>=threshold),total)
            assert a>=b,(n,threshold)
        assert Fraction(mix,total)-Fraction(meanL*meanC,total**2)==pC*(pLp-pL)
        print('n',n,'trees',total,'meanC',str(pC),'cov',str(pC*(pLp-pL)))
    # The analytical coupling uses these elementary transition inequalities.
    for n in range(4,501):
        for k in range(0,n-2):
            if k<=n-3:
                pnew=Fraction(n-1-k,n)
                pold=Fraction(n-3-k,n-2)
                assert pnew>pold
    print('PASS: enumerated',trials,'labeled trees, full Palm laws, moments, stochastic tails, and transitions.')

if __name__=='__main__':
    test()
