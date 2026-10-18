"""Exact finite-dimensional checks for minimax multiplex attention formulas.

Requires Python 3.10 or later, standard library only. The computational
checks illustrate identities, not the arbitrary-size proofs.
"""
from fractions import Fraction as F
from itertools import product, combinations


def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), F(0))


def exact_risk(pi, costs, alpha):
    """Original strategic-consensus game: worst equilibrium shift over the cube."""
    n=len(pi); L=len(alpha)
    K=[sum((alpha[l]**2*pi[i]**2/costs[i][l] for l in range(L)),F(0)) for i in range(n)]
    total=sum(K,F(0))
    deviations=[K[i]-pi[i]*total for i in range(n)]
    worst=max((abs(dot(deviations,profile)) for profile in product((F(0),F(1)),repeat=n)))
    value=worst/(1+total)
    assert value==sum((abs(v) for v in deviations),F(0))/(2*(1+total))
    for opinion in product((F(0),F(1)),repeat=n):
        ystar=(dot(pi,opinion)+dot(K,opinion))/(1+total)
        reports=[[opinion[i]+alpha[l]*pi[i]/costs[i][l]*(opinion[i]-ystar)
                  for l in range(L)] for i in range(n)]
        aggregate=sum((alpha[l]*pi[i]*reports[i][l]
                       for i in range(n) for l in range(L)),F(0))
        assert aggregate==ystar
        for i in range(n):
            for l in range(L):
                assert alpha[l]*pi[i]*(ystar-opinion[i])+costs[i][l]*(reports[i][l]-opinion[i])==0
    return value


def transformed_risk(pi,costs,alpha):
    n=len(pi); L=len(alpha)
    h=[[pi[i]**2/costs[i][l] for l in range(L)] for i in range(n)]
    S=[sum((h[i][l] for i in range(n)),F(0)) for l in range(L)]
    A=[[h[i][l]-pi[i]*S[l] for l in range(L)] for i in range(n)]
    tsum=sum((a*a for a in alpha),F(0))
    z=[a*a/tsum for a in alpha]
    numerator=sum((abs(dot(row,z)) for row in A),F(0))
    sqrt_z_sum_squared=F(1,tsum)  # because sum(alpha)=1
    denominator=sqrt_z_sum_squared+dot(S,z)
    return numerator/(2*denominator)


def check_soc_witness(pi, costs, alpha):
    # Construct cone-feasibility witness at the exact risk threshold.
    n=len(pi); L=len(alpha)
    h=[[pi[i]**2/costs[i][l] for l in range(L)] for i in range(n)]
    S=[sum((h[i][l] for i in range(n)),F(0)) for l in range(L)]
    A=[[h[i][l]-pi[i]*S[l] for l in range(L)] for i in range(n)]
    denom=sum((a*a for a in alpha),F(0))
    z=[a*a/denom for a in alpha]
    r=[abs(dot(row,z)) for row in A]
    u={(l,j):alpha[l]*alpha[j]/denom for l in range(L) for j in range(l+1,L)}
    for (l,j), q in u.items():
        assert 4*q*q+(z[l]-z[j])**2==(z[l]+z[j])**2
    rhs=dot([1+s for s in S],z)+2*sum(u.values(),F(0))
    threshold=transformed_risk(pi,costs,alpha)
    assert sum(r,F(0))==2*threshold*rhs


def sharp_layer_risk(n,m,delta):
    # Exactly m active equally attended channels in n-agent n-layer example.
    pi=[F(1,n)]*n
    costs=[[F(1,n*n)/(1+delta*(i==l)) for l in range(n)] for i in range(n)]
    active=range(m)
    alpha=[F(1,m) if l in active else F(0) for l in range(n)]
    exact=exact_risk(pi,costs,alpha)
    formula=delta*F(n-m,n)/F(n+delta+m)
    assert exact==formula
    assert transformed_risk(pi,costs,alpha)==exact
    check_soc_witness(pi,costs,alpha)
    return exact


def tests():
    # Arbitrary stationary vector and heterogeneous channel costs.
    cases=[
      ([F(1,2),F(1,3),F(1,6)],
       [[F(1,4),F(1,6),F(1,2)], [F(1,5),F(2,3),F(3,7)], [F(2,5),F(3,5),F(1,8)]],
       [F(1,6),F(1,3),F(1,2)]),
      ([F(1,5),F(2,5),F(2,5)],
       [[F(1,2),F(2,3)], [F(3,4),F(1,8)], [F(1,3),F(1,6)]],
       [F(3,7),F(4,7)]),
    ]
    for pi,c,alpha in cases:
        a=exact_risk(pi,c,alpha)
        b=transformed_risk(pi,c,alpha)
        assert a==b,(a,b)
        check_soc_witness(pi,c,alpha)
    count=0
    for n in range(2,8):
        for delta in (F(1,3),F(1),F(2)):
            for m in range(1,n+1):
                sharp_layer_risk(n,m,delta)
                count+=1
    # Exact grid comparison for representative m-active perturbations of
    # the equal-attention optimizer.
    grid=0
    for n in range(2,6):
        delta=F(2,3)
        pi=[F(1,n)]*n
        costs=[[F(1,n*n)/(1+delta*(i==l)) for l in range(n)] for i in range(n)]
        for m in range(1,n+1):
            bound=delta*F(n-m,n)/F(n+delta+m)
            for t in product((1,2,3),repeat=m):
                s=sum(t)
                alpha=[F(t[l],s) if l<m else F(0) for l in range(n)]
                v=transformed_risk(pi,costs,alpha)
                assert v>=bound,(n,m,t,v,bound)
                grid+=1
    # Uniform n-layer calibration exactly cancels all theta.
    for n in range(2,8):
        assert sharp_layer_risk(n,n,F(1))==0
        for m in range(1,n):
            assert sharp_layer_risk(n,m,F(1))>0
    print('PASS: Nash first-order equations and cube extremal risk agree exactly.')
    print('PASS: quadratic attention transform agrees exactly for heterogeneous costs.')
    print(f'PASS: {count} exact layer-count identities and {grid} rational grid inequalities.')
    print('PASS: exact rotated-cone witnesses for all representative attention vectors.')
    print('PASS: all-layer cancellation and strict proper-subset obstruction.')

if __name__=='__main__':
    tests()
