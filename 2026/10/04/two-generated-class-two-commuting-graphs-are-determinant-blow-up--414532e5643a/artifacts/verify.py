from collections import Counter
from math import gcd

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def j2(n):
    if n == 1:
        return 1
    ans = n*n
    x = n
    p = 2
    while p*p <= x:
        if x % p == 0:
            ans = ans // (p*p) * (p*p-1)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        ans = ans // (x*x) * (x*x-1)
    return ans

class GABC:
    def __init__(self,A,B,c):
        assert c >= 2 and A % c == 0 and B % c == 0
        self.A=A; self.B=B; self.c=c
        self.one=(0,0,0)
        self.elts=[(u,v,w) for u in range(A) for v in range(B) for w in range(c)]

    def mul(self,x,y):
        u,v,w=x
        U,V,W=y
        return ((u+U)%self.A,(v+V)%self.B,(w+W-v*U)%self.c)

    def inv(self,x):
        u,v,w=x
        U=(-u)%self.A
        V=(-v)%self.B
        W=(-w+v*U)%self.c
        y=(U,V,W)
        assert self.mul(x,y)==self.one
        assert self.mul(y,x)==self.one
        return y

    def commute(self,x,y):
        return self.mul(x,y)==self.mul(y,x)

    def comm(self,x,y):
        return self.mul(self.mul(self.mul(self.inv(x),self.inv(y)),x),y)

    def detzero(self,x,y):
        u,v,_=x
        U,V,_=y
        return (u*V-v*U)%self.c==0

def predicted_hist(A,B,c):
    s=A*B//c
    return {
        s*c*d-1: s*j2(c//d)
        for d in divisors(c)
    }

def check(A,B,c):
    G=GABC(A,B,c)
    E=G.elts

    # Associativity: exhaustive in the smallest cases, deterministic broad sample otherwise.
    if len(E) <= 32:
        sample=E
    else:
        step=max(1,len(E)//23)
        sample=E[::step][:24]
    for x in sample:
        for y in sample:
            for z in sample:
                assert G.mul(G.mul(x,y),z)==G.mul(x,G.mul(y,z))

    for x in E:
        G.inv(x)

    center=[]
    degrees=[]
    for x in E:
        count=0
        universal=True
        for y in E:
            a=G.commute(x,y)
            assert a==G.detzero(x,y)
            count += a
            universal &= a
        if universal:
            center.append(x)
        degrees.append(count-1)

    s=A*B//c
    assert len(center)==s

    comms={G.comm(x,y) for x in E for y in E}
    assert comms=={(0,0,w) for w in range(c)}

    hist=dict(Counter(degrees))
    pred=predicted_hist(A,B,c)
    assert hist==pred,(A,B,c,hist,pred)
    assert len(E)==s*c*c

    print({
        "A":A,"B":B,"c":c,
        "order":len(E),
        "center":s,
        "degree_hist":dict(sorted(hist.items()))
    })
    return c,s,hist

cases=[(2,2,2),(3,3,3),(4,4,2),(8,2,2),(8,4,4),(12,6,6)]
data={case:check(*case) for case in cases}

assert data[(8,2,2)][0:2]==data[(4,4,2)][0:2]==(2,8)
assert data[(8,2,2)][2]==data[(4,4,2)][2]
assert tuple(sorted((8,2))) != tuple(sorted((4,4)))

print("VERIFY_OK")
