"""Reproduce the dyadic one-gap two-binomial Thue--Morse theorem.
Python 3, standard library only. No external data.
"""
from fractions import Fraction as F
from itertools import product

class P:
    """Exact rational polynomial in h, degree at most two."""
    def __init__(self, x=0):
        if isinstance(x, P): self.v=x.v
        elif isinstance(x,tuple): self.v=tuple(F(a) for a in x)
        else: self.v=(F(x),F(0),F(0))
    def __add__(self, other):
        q=P(other); return P(tuple(a+b for a,b in zip(self.v,q.v)))
    __radd__=__add__
    def __neg__(self):return P(tuple(-x for x in self.v))
    def __sub__(self,other):return self+-P(other)
    def __rsub__(self,other):return P(other)+-self
    def __mul__(self,other):
        q=P(other); z=[F(0)]*3
        for i,a in enumerate(self.v):
            for j,b in enumerate(q.v):
                if i+j<3:z[i+j]+=a*b
                elif a*b:raise AssertionError('non-quadratic polynomial')
        return P(tuple(z))
    __rmul__=__mul__
    def __truediv__(self,other):
        q=P(other)
        assert q.v[1:]==(0,0) and q.v[0]
        return P(tuple(x/q.v[0] for x in self.v))
    def at(self,t):return self.v[0]+self.v[1]*t+self.v[2]*t*t
    def __hash__(self):return hash(self.v)
    def __eq__(self,other):return self.v==P(other).v
    def __repr__(self):return repr(self.v)

H=P((0,1,0))
def unit(a,b):
    q=[P(0) for _ in range(4)];q[2*a+b]=P(1);return q

def Ebase(e):
    if e==0:return ((H-2)/3,(2*H-1)/3,(2*H-1)/3,(H+1)/3)
    return ((H-1)/3,(2*H+1)/3,(2*H-2)/3,(H-1)/3)

def symbolic(e):
    """All possible profiles, deduplicated as exact polynomials in h."""
    S={}
    def emit(c,dI,dE,label):
        E=[a+b for a,b in zip(Ebase(e),dE)]
        z=2*H-c;I=H*H/2+dI
        p=(c,z*(z-1)/2-E[0],I-E[1],c*z-I-E[2],c*(c-1)/2-E[3])
        S.setdefault(p,[]).append(label)
        t=(2*H-c,p[4],p[3],p[2],p[1]);S.setdefault(t,[]).append('complement '+label)
    emit(H,0,[0]*4,'equal at zero shift')
    for u,v in product((0,1),repeat=2):
        emit(H,0,[a-b for a,b in zip(unit(e,0),unit(1-u,v))],f'equal even {u}{v}')
    for u in (0,1):
        emit(H,-H*(1-2*u),[a-b for a,b in zip(unit(e,0),unit(u,1-u))],f'equal odd {u}')
    for u in (0,1):
        q=(u,-u,u,-u)
        emit(H+1-2*u,u-1,[a-b+c for a,b,c in zip(unit(e,1),unit(u,1-u),q)],f'mixed odd s even {u}')
        emit(H+1-2*u,-u,[a-b+c for a,b,c in zip(unit(e,1),unit(u,1-u),q)],f'mixed odd s odd {u}')
    for u,v in product((0,1),repeat=2):
        q=(u,u-1,1-u,-u)
        emit(H,0,[a-b+c for a,b,c in zip(unit(e,1),unit(1-u,v),q)],f'mixed even s even {u}{v}')
    for u in (0,1):
        v=1-u;q=(u,u-1,1-u,-u)
        emit(H,2*u-1,[a-b+c for a,b,c in zip(unit(e,1),unit(1-u,v),q)],f'mixed even s odd {u}')
    return S

def no_zero_for_h_ge_four(q):
    """A sufficient exact sign certificate after substituting h=4+t, t>=0."""
    a,b,c=q.v[2],q.v[1],q.v[0]
    coeffs=(16*a+4*b+c,8*a+b,a)
    return (coeffs[0]>0 and all(x>=0 for x in coeffs[1:])) or (coeffs[0]<0 and all(x<=0 for x in coeffs[1:]))

def tm(m):
    w='0'
    for _ in range(m):w=''.join('01' if b=='0' else '10' for b in w)
    return w

def actual_gap_profile(w):
    n=len(w);c=w.count('1');p=[0,0,0,0]
    for i in range(n):
        for j in range(i+2,n):
            p[2*int(w[i])+int(w[j])]+=1
    return (c,*p)

def observed(m):
    T=tm(m);B=T.translate(str.maketrans('01','10')); n=len(T)
    return {actual_gap_profile(a[r:]+b[:r]) for a,b in product((T,B),repeat=2) for r in range(n)}

def main():
    for parity in (0,1):
        rows=symbolic(parity)
        assert len(rows)==12,(parity,len(rows))
        # Certify noncollision for every REAL h>=4 by an exact polynomial sign witness.
        items=list(rows)
        for k,p in enumerate(items):
            for q in items[k+1:]:
                assert any(no_zero_for_h_ge_four(a-b) for a,b in zip(p,q)),(parity,p,q)
        print('SYMBOLIC PASS parity',parity,'12 polynomial profiles pairwise separated for all h>=4')
    for m in range(3,8):
        h=2**(m-1)
        predicted={tuple(int(p.at(h)) for p in row) for row in symbolic(m%2)}
        empirical=observed(m)
        assert len(predicted)==12
        assert predicted==empirical,(m,len(predicted),len(empirical),predicted^empirical)
        print('FINITE PASS',m,2**m,12)
    # Direct independent factor extraction from the Thue--Morse fixed point.
    for m in range(3,7):
        n=2**m;long=tm(m+4)
        factor={actual_gap_profile(long[i:i+n]) for i in range(len(long)-n+1)}
        assert factor==observed(m),(m,'factor mismatch')
        print('DIRECT FACTORS PASS',m,len(factor))
    print('ALL PASS')
if __name__=='__main__':main()
