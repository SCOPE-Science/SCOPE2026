"""Finite independent checks for a conditional balance-modality law.
Run with Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def conditional_probs(n, k, edge_p=Fraction(1, 2)):
    """P(outgoing non-p minus p count equals 0 or -1)."""
    y = n-k
    p = edge_p
    def binprob(t, j):
        return Fraction(0) if not 0 <= j <= t else comb(t,j)*p**j*(1-p)**(t-j)
    q0 = sum((binprob(k,x)*binprob(y,x) for x in range(n+1)),Fraction(0))
    qm = sum((binprob(k,x)*binprob(y,x-1) for x in range(n+1)),Fraction(0))
    return q0, qm


def pred(n, col, arcs, v):
    d = sum((1-2*col[w])*arcs[v*n+w] for w in range(n))
    return (int(d == 0),int(d == -1))


def tri_law(n,k):
    q0,qm=conditional_probs(n,k)
    step={1:Fraction(1,2)*q0, -1:Fraction(1,2)*qm, 0:1-Fraction(1,2)*(q0+qm)}
    result={0:Fraction(1)}
    for _ in range(n-1):
        new={}
        for a,pa in result.items():
            for b,pb in step.items():
                new[a+b]=new.get(a+b,Fraction(0))+pa*pb
        result=new
    return result


def check_enumeration(n):
    nmodels=2**(n+n*n)
    by_k=Counter()
    by_k_d=Counter()
    witnesses=0
    for cbits in range(2**n):
        col=tuple((cbits>>w)&1 for w in range(n))
        k=sum(col)
        for abits in range(2**(n*n)):
            arcs=tuple((abits>>i)&1 for i in range(n*n))
            outcomes=[pred(n,col,arcs,v) for v in range(n)]
            diff=sum(arcs[v]*(outcomes[v][0]-outcomes[v][1]) for v in range(1,n))
            full=diff + arcs[0]*(outcomes[0][0]-outcomes[0][1])
            if full!=diff:
                assert arcs[0] and (outcomes[0][0] or outcomes[0][1])
                witnesses+=1
            by_k[k]+=1
            by_k_d[(k,diff)]+=1
            assert (full>=0)==(sum(arcs[v]*outcomes[v][0] for v in range(n)) >= sum(arcs[v]*outcomes[v][1] for v in range(n)))
    for k in range(n+1):
        law=tri_law(n,k)
        for d in range(-n,n+1):
            assert Fraction(by_k_d[(k,d)],by_k[k])==law.get(d,0), (n,k,d,Fraction(by_k_d[(k,d)],by_k[k]),law.get(d,0))
    print('n=',n,'models=',nmodels,'self_effect_cases=',witnesses,'conditioned_laws=OK')


def check_binomial_convolution():
    # Independently enumerate per-row outgoing arcs against each possible colour count.
    for n in range(1,12):
        for k in range(n+1):
            col=(1,)*k+(0,)*(n-k)
            counts=Counter(sum((1-2*col[w])*edge[w] for w in range(n)) for edge in product((0,1),repeat=n))
            q0,qm=conditional_probs(n,k)
            assert q0==Fraction(counts[0],2**n)
            assert qm==Fraction(counts[-1],2**n)
    print('row_convolution_exact=OK')


def main():
    check_binomial_convolution()
    for n in (1,2,3,4):
        check_enumeration(n)
    print('NEAR_COMPLETE_MODAL_BALANCE_EXACT_CHECKS_OK')

if __name__=='__main__':
    main()
