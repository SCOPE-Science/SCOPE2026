from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        if q in (3,5): self.q=q; self.p=q; self.d=1
        elif q==9: self.q=9; self.p=3; self.d=2
        else: raise ValueError(q)
    def add(self,a,b):
        if self.d==1: return (a+b)%self.p
        return ((a%3+b%3)%3) + 3*((a//3+b//3)%3)
    def neg(self,a):
        if self.d==1: return (-a)%self.p
        return ((-a%3)%3) + 3*((-(a//3))%3)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.d==1: return (a*b)%self.p
        a0,a1=a%3,a//3; b0,b1=b%3,b//3
        # z^2+1=0, so z^2=2 over F_3.
        c0=(a0*b0+2*a1*b1)%3
        c1=(a0*b1+a1*b0)%3
        return c0+3*c1
    def pow(self,a,n):
        r=1
        while n:
            if n&1: r=self.mul(r,a)
            a=self.mul(a,a); n//=2
        return r
    def inv(self,a):
        assert a!=0
        return self.pow(a,self.q-2)
    def div(self,a,b): return self.mul(a,self.inv(b))


def trim(a,F):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)

def deg(a,F): return len(trim(a,F))-1

def monic(a,F):
    a=trim(a,F)
    if a==(0,): return a
    z=F.inv(a[-1])
    return tuple(F.mul(x,z) for x in a)

def divmod_poly(a,b,F):
    a=list(trim(a,F)); b=trim(b,F)
    assert b!=(0,)
    out=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        k=len(a)-len(b); c=F.div(a[-1],b[-1]); out[k]=c
        for j,x in enumerate(b): a[k+j]=F.sub(a[k+j],F.mul(c,x))
        while len(a)>1 and a[-1]==0: a.pop()
    return trim(out,F),trim(a,F)

def gcd_poly(a,b,F):
    a=trim(a,F); b=trim(b,F)
    while b!=(0,):
        _,r=divmod_poly(a,b,F); a,b=b,r
    return monic(a,F)

def rank(A,F):
    A=[row[:] for row in A]
    if not A: return 0
    nr,nc=len(A),len(A[0]); r=0
    for c in range(nc):
        piv=next((i for i in range(r,nr) if A[i][c]!=0),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=F.inv(A[r][c]); A[r]=[F.mul(x,z) for x in A[r]]
        for i in range(nr):
            if i!=r and A[i][c]!=0:
                z=A[i][c]
                A[i]=[F.sub(A[i][j],F.mul(z,A[r][j])) for j in range(nc)]
        r+=1
        if r==nr: break
    return r

def matrix_for(f,m,n,F):
    f=trim(f,F); out=[]
    for r in range(m):
        row=[0]*n
        for i,c in enumerate(f): row[r+i]=c
        out.append(row)
    return out

def monic_reps(s,F):
    out=[(1,)]
    for d in range(1,s+1):
        for coeff in product(range(F.q),repeat=d): out.append(tuple(coeff)+(1,))
    return out

def predicted_t_count(q,s,t):
    return (q+1)*q**(2*t-1)*(q**(s-t+1)-1)//(q-1)

def check(q,m,n):
    F=Field(q); s=n-m; reps=monic_reps(s,F)
    L=(q**(s+1)-1)//(q-1)
    assert len(reps)==L
    mats=[matrix_for(f,m,n,F) for f in reps]
    assert all(rank(M,F)==m for M in mats)
    hist_t=Counter(); hist_d=Counter()
    for i,f in enumerate(reps):
        for j,g in enumerate(reps):
            if i==j: continue
            d=gcd_poly(f,g,F)
            t=max(deg(f,F),deg(g,F))-deg(d,F)
            stacked=mats[i]+mats[j]
            inter=2*m-rank(stacked,F)
            ds=2*(m-inter)
            assert inter==max(0,m-t), (q,m,n,f,g,inter,t)
            assert ds==2*min(m,t)
            hist_t[t]+=1; hist_d[ds]+=1
    pred={t:predicted_t_count(q,s,t) for t in range(1,s+1)}
    assert dict(sorted(hist_t.items()))==pred
    assert sum(pred.values())==L*(L-1)
    return {"q":q,"m":m,"n":n,"size":L,"t_histogram":pred,"distance_histogram":dict(sorted(hist_d.items()))}

cases=[check(3,2,4),check(3,3,5),check(5,3,6),check(9,2,4)]
for c in cases: print(c)
print('VERIFY_OK')
