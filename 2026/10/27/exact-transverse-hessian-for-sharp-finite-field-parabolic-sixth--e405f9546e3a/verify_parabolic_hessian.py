#!/usr/bin/env python3
"""Exact finite-field checks of convolution counts for a parabolic sixth-moment Hessian.

All arithmetic is exact; no third-party packages or network access needed.
The finite enumerations corroborate, rather than prove, the all-field theorem.
"""

def check_field(p, nonsquare=None):
    if nonsquare is None:
        q=p
        def add(x,y):return (x+y)%p
        def mul(x,y):return (x*y)%p
    else:
        q=p*p
        def add(x,y):return (x%p+y%p)%p+p*((x//p+y//p)%p)
        def mul(x,y):
            a,b=x%p,x//p
            c,d=y%p,y//p
            return ((a*c+nonsquare*b*d)%p)+p*((a*d+b*c)%p)
    square=[mul(x,x) for x in range(q)]
    N=[[0]*q for _ in range(q)]
    L=[[0]*q for _ in range(q)]
    Q=[[0]*q for _ in range(q)]
    h=[0]*q;h[0]=1;h[1]=-1
    for x in range(q):
        for y in range(q):
            xy=add(x,y);xx=add(square[x],square[y]);v=h[x]+h[y];w=h[x]*h[y]
            for z in range(q):
                s=add(xy,z);t=add(xx,square[z]);N[s][t]+=1
                L[s][t]+=v+h[z]
                Q[s][t]+=w+v*h[z]
    a=sum(n*n for row in N for n in row)
    b=sum(z*z for row in L for z in row)
    c=sum(N[s][t]*Q[s][t] for s in range(q) for t in range(q))
    assert a==q*q*(q*q+q-1),(q,'normalization',a)
    assert b==18*q*(q-1),(q,'linear',b)
    assert c==-6*q,(q,'quadratic',c)
    normterm=6*a//q
    real=b+2*c-normterm
    imag=b-2*c-normterm
    assert real==-6*q*(q*q-2*q+4)
    assert imag==-6*q*q*(q-2)
    print('PASS',q,'S0=',a,'sum_L2=',b,'sum_NQ=',c)

if __name__=='__main__':
    for prime in (5,7,11,13):check_field(prime)
    # In F25=F5[alpha]/(alpha^2-2), 2 is nonsquare in F5.
    check_field(5,nonsquare=2)
    print('ALL_FINITE_CHECKS_PASS')
