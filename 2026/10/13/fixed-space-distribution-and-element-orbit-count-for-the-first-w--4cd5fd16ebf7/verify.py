from collections import Counter
from itertools import product

def rank_mod(M,p):
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        iv=pow(A[r][c]%p,p-2,p)
        A[r]=[(z*iv)%p for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(n)]
        r+=1
    return r

def q5_data():
    p=5; dist=Counter(); autos=[]
    for a in range(1,p):
      for b in range(p):
       for c in range(p):
        for d in range(p):
         M=[[a,0,0,0],[b,a*a%p,0,0],[c,2*a*b%p,a**3%p,0],[d,(b*b+2*a*c)%p,3*a*a*b%p,a**4%p]]
         N=[[(M[i][j]-(1 if i==j else 0))%p for j in range(4)] for i in range(4)]
         dist[1+4-rank_mod(N,p)]+=1
         autos.append((a,b,c,d))
    assert dist==Counter({2:450,3:45,4:4,5:1})
    def phi(x,A):
        a,b,c,d=A; e0,e1,e2,e3,e4=x
        vals=[[0,a,b,c,d],[0,0,a*a%p,2*a*b%p,(b*b+2*a*c)%p],[0,0,0,a**3%p,3*a*a*b%p],[0,0,0,0,a**4%p]]
        out=[e0,0,0,0,0]
        for ek,v in zip((e1,e2,e3,e4),vals):
            for i in range(5): out[i]=(out[i]+ek*v[i])%p
        return tuple(out)
    unseen=set(product(range(5),repeat=5)); orbits=[]
    while unseen:
        x=next(iter(unseen)); orb={phi(x,A) for A in autos}
        orbits.append(orb); unseen-=orb
    assert len(orbits)==45
    burn=sum(dist[j]*(5**j) for j in dist)//500
    assert burn==45
    return dist,len(orbits)

class F25:
    @staticmethod
    def add(x,y): return ((x%5+y%5)%5)+5*((x//5+y//5)%5)
    @staticmethod
    def neg(x): return ((-x)%5)+5*((-(x//5))%5)
    @staticmethod
    def sub(x,y): return F25.add(x,F25.neg(y))
    @staticmethod
    def mul(x,y):
        a,b=x%5,x//5; c,d=y%5,y//5
        return ((a*c+2*b*d)%5)+5*((a*d+b*c)%5)
    @staticmethod
    def pow(x,n):
        r=1
        while n:
            if n&1: r=F25.mul(r,x)
            x=F25.mul(x,x); n//=2
        return r
    @staticmethod
    def inv(x):
        assert x
        return F25.pow(x,23)

def rank25(M):
    A=[row[:] for row in M]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]!=0),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        iv=F25.inv(A[r][c]); A[r]=[F25.mul(z,iv) for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[F25.sub(A[i][j],F25.mul(f,A[r][j])) for j in range(n)]
        r+=1
    return r

def q25_data():
    dist=Counter()
    for a in range(1,25):
      for b in range(25):
       for c in range(25):
        for d in range(25):
         a2=F25.mul(a,a); a3=F25.mul(a2,a); a4=F25.mul(a3,a)
         M=[[a,0,0,0],[b,a2,0,0],[c,F25.mul(2,F25.mul(a,b)),a3,0],[d,F25.add(F25.mul(b,b),F25.mul(2,F25.mul(a,c))),F25.mul(3,F25.mul(a2,b)),a4]]
         N=[[F25.sub(M[i][j],1 if i==j else 0) for j in range(4)] for i in range(4)]
         dist[1+4-rank25(N)]+=1
    expected=Counter({1:281250,2:92500,3:1225,4:24,5:1})
    assert dist==expected
    burn=sum(dist[j]*(25**j) for j in dist)//(24*25**3)
    assert burn==275
    return dist,burn

if __name__=='__main__':
    d5,o5=q5_data(); d25,o25=q25_data()
    print('VERIFY_OK', 'q5='+repr(dict(sorted(d5.items()))), 'orbits5='+str(o5), 'q25='+repr(dict(sorted(d25.items()))), 'orbits25='+str(o25))
