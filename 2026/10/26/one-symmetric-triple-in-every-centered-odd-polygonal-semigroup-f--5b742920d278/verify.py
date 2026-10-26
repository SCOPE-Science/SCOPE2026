from math import gcd
from heapq import heappush, heappop

def centered(k,n):return 1 + k*n*(n-1)//2

def represent(z,x,y):
    if x<=0 or y<=0:return False
    return any((z-u*x)>=0 and (z-u*x)%y==0 for u in range(z//x+1))

def gluing(triple):
    a,b,c=triple
    for x,y,z in [(a,b,c),(a,c,b),(b,c,a)]:
        d=gcd(x,y)
        if gcd(d,z)==1 and represent(z,x//d,y//d):return True
    return False

def apery(gens):
    a=min(gens); dist=[10**80]*a;dist[0]=0;h=[(0,0)]
    while h:
        v,r=heappop(h)
        if v!=dist[r]:continue
        for z in gens:
            s=(r+z)%a;nv=v+z
            if nv<dist[s]:dist[s]=nv;heappush(h,(nv,s))
    assert all(d<10**80 for d in dist)
    F=max(dist)-a;g=sum(dist)//a-(a-1)//2
    return F,g

def frob(k):return (27*k**5+432*k**4+2058*k**3+3912*k**2+2779*k+328)//64

def check():
    scanned=0
    for k in range(3,102,2):
        good=(3*k+7)//2
        for n in range(k,k+151):
            tri=tuple(centered(k,n+j) for j in range(3))
            got=gluing(tri)
            assert got==(n==good),(k,n,tri,got,good)
            scanned+=1
    print('EXACT_GLUING_OK',scanned)
    for k in [3,5,7,9,11,13,15,17,19,21]:
        n=(3*k+7)//2
        a,b,c=(centered(k,n+j) for j in range(3))
        d=3*k+8
        assert gcd(a,c)==d and gcd(d,b)==1 and (n+1)*a+n*c==d*b
        assert b==(n+1)*(a//d)+n*(c//d)
        F,g=apery([a,b,c]); assert F==frob(k) and 2*g==F+1,(k,F,g,frob(k))
        print('APERy_OK',k,n,a,b,c,F,g)
    for k,n in [(3,3),(3,5),(5,5),(7,7),(9,12)]:
        gens=[centered(k,n+j) for j in range(3)]
        assert not gluing(gens)
        F,g=apery(gens);assert 2*g>F+1,(k,n,F,g)
    print('NON_SYMMETRIC_APERY_OK')
if __name__=='__main__':check()
