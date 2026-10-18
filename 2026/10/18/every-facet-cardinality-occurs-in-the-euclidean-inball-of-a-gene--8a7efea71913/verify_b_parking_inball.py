"""Reproducible high-precision and integer checks for generalized parking polytopes.

The analytic proof, not these finite computations, establishes the all-dimensional theorem.
Run: python verify_b_parking_inball.py (Python 3 standard library only).
"""
from decimal import Decimal, localcontext
from itertools import combinations, product, permutations
from math import comb


def data(b):
    n=len(b)
    S=[]; running=0
    for bi in b:
        running+=bi
        S.append(running)
    U=[0]+[sum(S[-k:]) for k in range(1,n+1)]
    with localcontext() as ctx:
        ctx.prec=60
        rad=[(Decimal(U[k]-k)/(Decimal(k)+Decimal(k).sqrt())) for k in range(1,n+1)]
        r=min(rad)
        active=[k for k in range(1,n+1) if abs(rad[k-1]-r)<Decimal('1e-42')]
        t=Decimal(1)+r
        for k in range(1,n+1):
            slack=Decimal(U[k])-Decimal(k)*t-r*Decimal(k).sqrt()
            assert slack>=Decimal('-1e-48'),(b,k,slack)
            assert (abs(slack)<Decimal('1e-42')) == (k in active),(b,k,slack,active)
        assert abs((t-1)-r)<Decimal('1e-48')
    return S,U,active


def check_vertex_support(b):
    n=len(b)
    S,U,active=data(b)
    reps=[tuple([1]*k+S[k:]) for k in range(n+1)]
    vertices={z for v in reps for z in permutations(v)}
    evaluations=0
    for k in range(1,n+1):
        for subset in combinations(range(n),k):
            vals=[sum(v[i] for i in subset) for v in vertices]
            assert min(vals)==k and max(vals)==U[k],(b,subset)
            evaluations+=len(vals)
    return len(vertices),evaluations


def phase_example(n,k):
    with localcontext() as ctx:
        ctx.prec=60
        t={j: (Decimal(j*(j+1)).sqrt()/
               (Decimal(1)+Decimal(j).sqrt()+Decimal(j+1).sqrt()))
           for j in range(1,n)}
        if k==1:theta=t[1]/2
        elif k==n:theta=t[n-1]+Decimal(1)
        else:theta=(t[k-1]+t[k])/2
        u=10**7
        B=int((theta*Decimal(u)).to_integral_value())
        b=(1+u,)+tuple(1 for _ in range(n-2))+(B,)
    _,_,active=data(b)
    assert active==[k],(n,k,b,active)
    return b


def main():
    params=checks=vertices=evaluations=0
    for n in range(2,6):
        for b in product(range(1,4),repeat=n):
            _,_,act=data(b)
            params+=1
            if n<=4 or b in ((1,1,1,1,1),(3,2,1,3,2),(2,3,1,1,2)):
                v,e=check_vertex_support(b)
                checks+=1;vertices+=v;evaluations+=e
    phase_cases=0
    for n in range(2,13):
        for k in range(1,n+1):
            phase_example(n,k)
            phase_cases+=1
    print('PASS containment_parameter_sets=',params)
    print('PASS vertex_support_cases=',checks,'vertices_total=',vertices,'subset_support_evaluations=',evaluations)
    print('PASS realized_unique_contact_sizes=',phase_cases,'dimensions=2..12')
    print('PASS n=3 interior_contact_example=',data((100,3,50))[2])


if __name__=='__main__':
    main()
