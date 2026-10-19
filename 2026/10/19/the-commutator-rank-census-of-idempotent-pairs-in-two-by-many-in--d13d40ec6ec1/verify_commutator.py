"""Brute-force commutator-rank checks for pairs of incidence-algebra idempotents.

This checker independently enumerates idempotent matrices over small prime fields,
then computes commutator ranks without using the color-weight proof.
"""
from itertools import product


def idempotents(q,m):
    n=2+m
    eds=[(i,2+j) for i in range(2) for j in range(m)]
    for diag in product((0,1),repeat=n):
        active=[ij for ij in eds if diag[ij[0]]!=diag[ij[1]]]
        for vals in product(range(q),repeat=len(active)):
            weights = dict(zip(active,vals))
            yield tuple(diag), tuple(weights.get(ij,0) for ij in eds)


def matrix_rank_2xm(flat,q,m):
    a=flat[:m]; b=flat[m:]
    p=next((i for i,x in enumerate(a) if x%q),None)
    if p is None:return int(any(x%q for x in b))
    inv=pow(a[p],-1,q)
    c=b[p]*inv%q
    return 1 if all((b[j]-c*a[j])%q==0 for j in range(m)) else 2


def count_bruteforce(q,m):
    elems=list(idempotents(q,m))
    ans=[0,0,0]
    for u,x in elems:
        for v,y in elems:
            co=tuple(((u[i]-u[2+j])*y[i*m+j]-(v[i]-v[2+j])*x[i*m+j])%q
                     for i in range(2) for j in range(m))
            ans[matrix_rank_2xm(co,q,m)]+=1
    return ans,len(elems)


def formula(q,m):
    a=1+3*q*q
    b=2*q*(q+1)
    h=1+2*q*q+q**3
    c=q**3+q*q+2*q
    d=3*q*q+q
    s=4*a**m+12*b**m
    t=4*(q*q+1)**(2*m)+8*(2*q*(1+q*q))**m+4*(4*q*q)**m
    r1=4*(q+1)*(h**m-a**m)+16*(c**m-b**m)+8*(d**m-b**m)
    return [s,r1,t-s-r1]


def main():
    for q,m in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
        observed,elements=count_bruteforce(q,m)
        expect=formula(q,m)
        print('q,m=',q,m,'idempotents=',elements,'rank counts=',observed,'formula=',expect)
        assert observed==expect
    for q in (2,3,4,5):
        assert formula(q,1)[2]==0
        for m in (2,3,4): assert all(v>0 for v in formula(q,m))
    print('VERIFY_COMMUTATOR_OK')
if __name__=='__main__':main()
