"""Exact enumerator for the two-rainbow pushability of a regular octagon.

The arithmetic field is Q(sqrt(2)); all signs and comparisons use integer arithmetic.
Run with Python >=3.9; no external packages are needed.
"""
from fractions import Fraction as F
from itertools import combinations
from dataclasses import dataclass

@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a))
        object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def make(z): return z if isinstance(z,Q) else Q(F(z))
    def __add__(self,y):
        y=Q.make(y);return Q(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,y):return self+-Q.make(y)
    def __rsub__(self,y):return Q.make(y)+-self
    def __mul__(self,y):
        y=Q.make(y);return Q(self.a*y.a+2*self.b*y.b,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __truediv__(self,y):
        y=Q.make(y);den=y.a*y.a-2*y.b*y.b
        assert den!=0
        return Q((self.a*y.a-2*self.b*y.b)/den,(self.b*y.a-self.a*y.b)/den)
    def __rtruediv__(self,y):return Q.make(y)/self
    def sign(self):
        a,b=self.a,self.b
        if a==0:return (b>0)-(b<0)
        if b==0:return (a>0)-(a<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        d=a*a-2*b*b
        assert d!=0
        return (1 if a>0 else -1)*(1 if d>0 else -1)
    def __lt__(self,y):return (self-Q.make(y)).sign()<0
    def __le__(self,y):return (self-Q.make(y)).sign()<=0
    def __gt__(self,y):return (self-Q.make(y)).sign()>0
    def __ge__(self,y):return (self-Q.make(y)).sign()>=0
    def __float__(self):return float(self.a)+2**.5*float(self.b)
    def __repr__(self):return str(self.a) if not self.b else f'({self.a} + ({self.b})*sqrt(2))'

Z=Q(); ONE=Q(F(1)); H=Q(F(0),F(1,2))
V=[(ONE,Z),(H,H),(Z,ONE),(-H,H),(-ONE,Z),(-H,-H),(Z,-ONE),(H,-H)]
M=lambda i,j:int((i-j)%8 in (0,1,7))
SUBS=[u for k in [1,2,3] for u in combinations(range(8),k)]
def canonical(I):return min(tuple(sorted((s*x+t)%8 for x in I)) for s in [1,-1] for t in range(8))
IS=sorted(set(map(canonical,SUBS)))

def solve_support(I,J):
    """Return affine solution x=x0+B*t with exact arbitrary free variables."""
    N=len(I)+len(J)
    A=[[Z for _ in range(N+1)] for _ in range(4)]
    for k,i in enumerate(I):
        A[0][k]=ONE; A[2][k]=V[i][0]; A[3][k]=V[i][1]
    for l,j in enumerate(J):
        k=len(I)+l;A[1][k]=ONE;A[2][k]=V[j][0];A[3][k]=V[j][1]
    A[0][N]=A[1][N]=ONE
    pivots=[];r=0
    for col in range(N):
        pivot=next((rr for rr in range(r,4) if A[rr][col]!=Z),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        z=A[r][col]; A[r]=[val/z for val in A[r]]
        for k in range(4):
            if k!=r and A[k][col]!=Z:
                z=A[k][col];A[k]=[v-z*w for v,w in zip(A[k],A[r])]
        pivots.append(col);r+=1
        if r==4:break
    if any(all(A[k][col]==Z for col in range(N)) and A[k][N]!=Z for k in range(r,4)):
        return None
    free=[col for col in range(N) if col not in pivots]
    d=len(free)
    x0=[Z for _ in range(N)];B=[[Z for _ in range(d)] for _ in range(N)]
    for k,col in enumerate(pivots):
        x0[col]=A[k][N]
        for t,fc in enumerate(free): B[col][t]=-A[k][fc]
    for t,col in enumerate(free):B[col][t]=ONE
    return x0,B

def stationary(I,J,sol):
    x,B=sol; N=len(x); K=len(I);d=len(B[0]);
    if d>2:raise ValueError(f'Unexpected affine dimension {d}: {I},{J}')
    g=[Z for _ in range(d)];Hess=[[Z for _ in range(d)] for __ in range(d)]
    for i,ii in enumerate(I):
        for j,jj in enumerate(J):
            if not M(ii,jj):continue
            u=K+j
            for t in range(d):
                g[t]+=B[i][t]*x[u]+x[i]*B[u][t]
                for s in range(d):Hess[t][s]+=B[i][t]*B[u][s]+B[i][s]*B[u][t]
    if d==0:t=[]
    elif d==1:
        if not Hess[0][0]<Z:return None
        t=[-g[0]/Hess[0][0]]
    else:
        a,b=Hess[0]
        c,d2=Hess[1]
        det=a*d2-b*c
        if not a<Z or not det>Z:return None
        t=[(-d2*g[0]+b*g[1])/det,(c*g[0]-a*g[1])/det]
    w=[x[i]+sum((B[i][k]*t[k] for k in range(len(t))),Z) for i in range(N)]
    if any(z<=Z for z in w):return None
    f=sum((w[i]*w[K+j] for i,ii in enumerate(I) for j,jj in enumerate(J) if M(ii,jj)),Z)
    return f,w

def individually_balanced_extremes():
    """Enumerate vertices of the zero-mean distribution polytope."""
    out=[]
    for I in SUBS:
        n=len(I)
        A=[[ONE for _ in I]+[ONE],
           [V[i][0] for i in I]+[Z],
           [V[i][1] for i in I]+[Z]]
        rank=0;piv=[]
        for col in range(n):
            row=next((r for r in range(rank,3) if A[r][col]!=Z),None)
            if row is None:continue
            A[rank],A[row]=A[row],A[rank]
            inv=A[rank][col]
            A[rank]=[x/inv for x in A[rank]]
            for r in range(3):
                if r!=rank and A[r][col]!=Z:
                    z=A[r][col]
                    A[r]=[x-z*y for x,y in zip(A[r],A[rank])]
            piv.append(col)
            rank+=1
            if rank==3:break
        if rank<n:continue  # not a vertex: affinely dependent positive support
        if any(all(A[r][col]==Z for col in range(n)) and A[r][n]!=Z
               for r in range(rank,3)):
            continue
        weights=[Z]*n
        for r,col in enumerate(piv):weights[col]=A[r][n]
        if all(x>0 for x in weights):out.append((I,weights))
    return out

def explicit_witness():
    c=H
    b=(ONE+3*c)/(4*(ONE+c))
    p0=((ONE-c)+(ONE+c)*b)/2
    P={0:p0,4:ONE-p0}
    Qd={1:(ONE-b)/2,4:b,7:(ONE-b)/2}
    assert sum(P.values(),Z)==ONE
    assert sum(Qd.values(),Z)==ONE
    assert all(w>0 for w in list(P.values())+list(Qd.values()))
    assert all(sum(((P.get(i,Z)+Qd.get(i,Z))*V[i][k] for i in range(8)),Z)==Z for k in [0,1])
    probability=sum((P.get(i,Z)*Qd.get(j,Z) for i in P for j in Qd if M(i,j)),Z)
    return probability,P,Qd

def main():
    best=None
    nsupports=nstation=0
    per_orbit={}
    for I in IS:
        vals=[]
        for J in SUBS:
            nsupports+=1
            sol=solve_support(I,J)
            if sol is None:continue
            r=stationary(I,J,sol)
            if r is None:continue
            val,w=r
            assert all(x>0 for x in w)
            assert sum(w[:len(I)],Z)==ONE and sum(w[len(I):],Z)==ONE
            assert all(sum((w[k]*V[i][coord] for k,i in enumerate(I)),Z)
                       +sum((w[len(I)+k]*V[j][coord] for k,j in enumerate(J)),Z)==Z
                       for coord in (0,1))
            nstation+=1
            vals.append(val)
            if best is None or val>best[0]:best=(val,I,J,w)
        per_orbit[I]=(len(vals),max(vals) if vals else None)
    print('NUM_P_SUPPORT_ORBITS',len(IS),'NUM_SUPPORT_PAIRS',nsupports)
    print('NUM_INTERIOR_STRICT_CONCAVE_CRITICAL_POINTS',nstation)
    print('MAX',best)
    for I,(count,value) in per_orbit.items():print('ORBIT',I,'COUNT',count,'MAX',value)
    target=Q(F(13,16),F(-7,32))
    assert len(IS)==10 and nsupports==920 and nstation==126
    assert best[0]==target
    probability,P,Qd=explicit_witness()
    assert probability==target
    print('EXPLICIT_WITNESS',P,Qd,'VALUE',probability)
    ext=individually_balanced_extremes()
    assert len(ext)==12
    indivmax=Z
    for I,p in ext:
      for J,q in ext:
        val=sum((p[k]*q[l] for k,i in enumerate(I) for l,j in enumerate(J) if M(i,j)),Z)
        if val>indivmax:indivmax=val
    assert indivmax==Q(F(1,2))
    print('INDIVIDUALLY_BALANCED_EXTREME_MEASURES',len(ext),'PAIR_TESTS',len(ext)**2)
    print('INDIVIDUALLY_BALANCED_MAX',indivmax)
    print('PASS: all exact arithmetic over Q(sqrt(2))')

if __name__=='__main__':main()
