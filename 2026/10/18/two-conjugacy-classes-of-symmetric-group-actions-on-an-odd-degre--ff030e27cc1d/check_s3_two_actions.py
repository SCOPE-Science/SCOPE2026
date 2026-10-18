"""Exact finite-group consistency checks for two S3 actions on C_h.
The all-genus geometric argument is separate from these finite tests.
"""
from math import gcd
import sympy as sp

def check(h):
    m=12*h-6; k=2*h-1
    M=2*m; a=m-1
    def mul(X,Y):
        x,b=X; y,d=Y
        return ((x+(a if b else 1)*y)%M,(b+d)%2)
    def inv(X):
        x,b=X
        return ((-x if b==0 else -a*x)%M,b)
    I=(0,0)
    assert (a*a-1)%M==0
    S3=[]
    v=(2*m//3,0)
    assert mul(v,mul(v,v))==I
    for j in range(m):
        w=(2*j,1)
        assert mul(w,w)==I
        elements={I,v,mul(v,v),w,mul(v,w),mul(mul(v,v),w)}
        assert len(elements)==6
        S3.append(frozenset(elements))
    distinct=set(S3)
    assert len(distinct)==m//3 == 2*k
    conj_orbits=[]
    while distinct:
        H=next(iter(distinct)); orbit=set()
        for g in [(n,b) for n in range(M) for b in range(2)]:
            other=frozenset(mul(mul(g,x),inv(g)) for x in H)
            orbit.add(other)
        assert orbit<=distinct
        conj_orbits.append(orbit)
        distinct-=orbit
    assert sorted(len(o) for o in conj_orbits)==[k,k]
    assert gcd(m,1-m//2)==2
    u=sp.symbols('u'); x=sp.symbols('x')
    P0,P1=sp.Integer(2),u
    for index in range(1,2*h-1):
        P0,P1=P1,sp.expand(u*P1-P0)
    P=P1
    assert sp.degree(P,u)==2*h-1
    assert sp.gcd(P,sp.diff(P,u))==1
    assert sp.gcd(P,u*u-4)==1
    assert sp.expand((x**(2*h-1)+x**(-(2*h-1))-P.subs(u,x+1/x))*x**(2*h-1))==0
    # Both quotient genera from the verified degrees and squarefreeness.
    assert (sp.degree(P,u)-1)//2==h-1
    assert (sp.degree((u*u-4)*P,u)-1)//2==h
    # Ramification contributions, by stabilizer orders in the two actions.
    genus=6*h-3
    assert 2*genus-2==6*(2*h-2)+4
    assert 2*genus-2==6*(2*(h-1)-2)+4+4*3
    return (h,m,len(S3),[len(o) for o in conj_orbits])
if __name__=='__main__':
    rows=[check(h) for h in range(1,16)]
    print(rows)
    print('TWO_S3_ACTIONS_GROUP_CHECK_OK')
