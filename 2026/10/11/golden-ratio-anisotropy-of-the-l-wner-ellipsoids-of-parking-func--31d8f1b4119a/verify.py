#!/usr/bin/env python3
"""Pure-stdlib exact checks for the classical parking-function ellipsoid limit.
Tests polynomial identities and finite orbit covariance formulas; this does not
certify a limiting statement by finite enumeration.
"""
from fractions import Fraction as F
from itertools import permutations

class Q5:
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    def __add__(self, other):
        if not isinstance(other, Q5): other=Q5(other)
        return Q5(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self, other): return self + (-other if isinstance(other,Q5) else -Q5(other))
    def __rsub__(self, other): return other + (-self)
    def __mul__(self, other):
        if not isinstance(other,Q5): other=Q5(other)
        return Q5(self.a*other.a+5*self.b*other.b, self.a*other.b+self.b*other.a)
    __rmul__=__mul__
    def __truediv__(self, other):
        if isinstance(other,Q5):
            den=other.a*other.a-5*other.b*other.b
            return self*Q5(other.a/den,-other.b/den)
        return Q5(self.a/F(other),self.b/F(other))
    def __eq__(self, other):
        if not isinstance(other,Q5):other=Q5(other)
        return self.a==other.a and self.b==other.b
    def __repr__(self): return '(%s + %s sqrt(5))'%(self.a,self.b)

def add(a,b):
    out=[Q5() for _ in range(max(len(a),len(b)))]
    for i,c in enumerate(a):out[i]=out[i]+c
    for i,c in enumerate(b):out[i]=out[i]+c
    return out

def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    out=[Q5() for _ in range(len(a)+len(b)-1)]
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]=out[i+j]+c*d
    return out

def scale(a,c):return [c*x for x in a]

def formula(n,k):
    S=F(k*(2*n-k-1),2)
    T=F((n-1)*n*(2*n-1)-(n-k-1)*(n-k)*(2*(n-k)-1),6)
    V=T-S*S/n
    return S,T,V

def main():
    r5=Q5(0,1)
    u=(Q5(3)-r5)/2
    h=lambda z:sub([Q5()]+z[1:] if False else z, [Q5()])
    H=[Q5(), Q5(1), Q5(F(-1,2))]
    V=[Q5(),Q5(1),Q5(-2),Q5(F(4,3)),Q5(F(-1,4))]
    hu=(r5-Q5(1))/4
    vu=Q5(F(5,8),F(-5,24))
    L=sub(sub([vu],V),scale(mul(sub(H,[hu]),sub(H,[hu])),Q5(F(5,3))))
    R=scale(mul(mul([Q5(),Q5(1)],mul([-u,Q5(1)],[-u,Q5(1)])),[r5-Q5(1),Q5(-1)]),Q5(F(1,6)))
    assert L==R, (L,R)
    assert hu*hu==Q5(F(3,8),F(-1,8))
    assert vu==hu*hu*Q5(F(5,3))
    print('Q(sqrt(5)) polynomial gap identity: EXACT PASS')
    orbit_checks=0
    for n in range(2,8):
        for k in range(n):
            base=(0,)*(n-k)+tuple(range(n-k,n))
            orbit=set(permutations(base))
            S,T,V=formula(n,k)
            assert all(sum(z)==S and sum(t*t for t in z)==T for z in orbit)
            mu=F(S,n)
            cov=sum((F(z[0])-mu)**2 for z in orbit)/len(orbit)
            diag=F((T/n)-(S*S/(n*n)))
            assert cov==diag
            pair=sum((F(z[0])-mu)*(F(z[1])-mu) for z in orbit)/len(orbit)
            assert cov-pair==V/F(n-1)
            orbit_checks+=1
    print('finite permutation-orbit means and covariance:',orbit_checks,'EXACT PASS')
    examples={2:[F(1,3),F(2,3)],3:[F(2,9),F(1,3),F(4,9)],
              4:[F(1,5),F(0),F(4,5),F(0)]}
    for n,w in examples.items():
        S=[];V=[]
        for k in range(n):
            x,y,z=formula(n,k);S.append(x);V.append(z)
        mu=sum(w[k]*S[k] for k in range(n))
        a=sum(w[k]*V[k] for k in range(n))/F(n-1)
        b=(sum(w[k]*S[k]**2 for k in range(n))-mu*mu)/n
        assert a>0 and b>0
        for k in range(n):
            lev=V[k]/a+(S[k]-mu)**2/(n*b)
            assert lev<=n and (w[k]==0 or lev==n),(n,k,lev)
    print('n=2,3,4 exact finite Löwner covariance contact certificates: PASS')
    for n in (40,80,160,320,640,1280):
        scores=[]
        for k in range(n):
            S,T,W=formula(n,k)
            scores.append((W/F(n*n*(n-1)),k,S/F(n*n)))
        M,k,hk=max(scores)
        alpha=F(n,n+1)*M
        beta=F(n*n,(n+1)*(n+1))*hk*hk
        # finite two-orbit distribution is a feasible dual *design*, not
        # necessarily the final optimal primal enclosing ellipsoid.
        af=float(alpha)
        bf=float(beta)
        print('dual benchmark n=%d k=%d alpha=%.10f beta=%.10f'%(n,k,af,bf))
        assert abs(af-(5*(3-5**.5)/24))<2.0/n
        assert abs(bf-((3-5**.5)/8))<2.0/n
    print('finite two-orbit lower-design asymptotic checks: PASS')
if __name__=='__main__':main()
