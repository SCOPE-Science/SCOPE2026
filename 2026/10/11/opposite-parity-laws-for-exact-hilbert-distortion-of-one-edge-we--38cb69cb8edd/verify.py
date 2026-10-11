"""Exact rational checks for optimal Euclidean distortion of one-short-edge cycles."""
from fractions import Fraction as Q
from itertools import product


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q(0))


def cycle_values(p, lam):
    lam=Q(lam)
    assert p>=2 and 0<lam<=1
    w=[Q(1)]*p+[lam]
    normw=dot(w,w)
    c0=Q(p*(p-1),1)/(Q(p*p)-lam*lam)
    A=Q(p-1,p)
    k=lam*lam/Q(p*p)
    D=(Q(p-1)*(1+lam*lam/Q(p)) if p%2 else Q(p)-2*lam+lam*lam*Q(p-1,p))
    predicted=1+c0*D
    def q(x):
        s=sum(x[:p],Q(0))/p
        return sum(((xi-s)**2 for xi in x[:p]),Q(0)) + c0*(p+lam*lam)**2/(lam*lam)*s*s
    def qdual(u):
        s=sum(u[:p],Q(0))/p
        return sum(((ui-s)**2 for ui in u[:p]),Q(0)) + u[p]*u[p]/c0
    # Graph-edge molecules are images of unit coordinate vectors under the quotient projection.
    projected=[[Q(i==j)-w[i]*w[j]/normw for i in range(p+1)] for j in range(p+1)]
    Qmax=max(q(v) for v in projected)
    assert Qmax==c0, (p,lam,Qmax,c0)
    # Enumerate cube-section vertices by leaving one free coordinate.
    vertices=set()
    for free in range(p+1):
        others=[j for j in range(p+1) if j!=free]
        for signs in product((-1,1),repeat=p):
            u=[Q(0)]*(p+1)
            for j,sgn in zip(others, signs):
                u[j]=Q(sgn)
            u[free]=-dot(w,u)/w[free]
            if -1<=u[free]<=1:
                assert dot(w,u)==0
                vertices.add(tuple(u))
    Hmax=max(qdual(u) for u in vertices)
    expected_h=(D+1/c0)
    assert Hmax==expected_h,(p,lam,Hmax,expected_h)
    assert Qmax*Hmax==predicted,(p,lam,Qmax*Hmax,predicted)
    # Direct primal/dual domination on the full vertex sets.
    assert all(q(v)<=c0 for v in projected)
    assert all(qdual(v)<=Hmax for v in vertices)
    return len(vertices),predicted

if __name__=='__main__':
    count=0
    for p in range(2,10):
        for lam in (Q(1),Q(1,2),Q(1,3),Q(2,3),Q(3,4),Q(1,7),Q(7,8)):
            k,dist=cycle_values(p,lam)
            count+=1
            if p<=4:
                print('n=',p+1,'lambda=',lam,'vertices=',k,'distance^2=',dist)
    print('Exact rational instances checked:',count,'ALL_PASS')
