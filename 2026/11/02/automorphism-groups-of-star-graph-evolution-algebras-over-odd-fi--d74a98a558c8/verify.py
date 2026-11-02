"""Independent small-field enumeration for automorphisms of star evolution algebras.

Use: python verify.py. No third-party dependencies. Field F9 = F3[z]/(z^2+1).
"""
from itertools import product

def field(q):
    if q == 9:
        def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def neg(a):return ((-a%3)%3)+3*((-(a//3))%3)
        def mul(a,b):return ((a%3*b%3+2*(a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
    else:
        def add(a,b):return (a+b)%q
        def neg(a):return (-a)%q
        def mul(a,b):return a*b%q
    def sub(a,b):return add(a,neg(b))
    return add,sub,mul

def enumerate_automorphisms(q,m):
    add,sub,mul=field(q)
    def dot(a,b):
        out=0
        for x,y in zip(a,b):out=add(out,mul(x,y))
        return out
    def vec_add(a,b):return tuple(add(x,y) for x,y in zip(a,b))
    def vec_sub(a,b):return tuple(sub(x,y) for x,y in zip(a,b))
    zero=(0,)*m
    vectors=list(product(range(q),repeat=m))
    counts={}; examples={}; all_good=[]
    for u in range(1,q):
        usq=mul(u,u)
        target=(usq,)*m
        good=[v for v in vectors if dot(v,v)==u]
        match=[]
        def descend(cols,acc):
            if len(cols)==m-1:
                v=vec_sub(target,acc)
                if dot(v,v)==u and all(dot(v,w)==0 for w in cols):
                    G=cols+[v]
                    # The original basis is a,b_i with a^2=sum b_i and b_i^2=a.
                    # T(a)=u a; T(b_i)=i-th column G. Check all products.
                    assert all(dot(G[i],G[j])==(u if i==j else 0) for i in range(m) for j in range(m))
                    sums=zero
                    for col in G:sums=vec_add(sums,col)
                    assert sums==target
                    match.append(tuple(G))
                return
            for v in good:
                if all(dot(v,w)==0 for w in cols):
                    descend(cols+[v],vec_add(acc,v))
        descend([],zero)
        counts[u]=len(match)
        all_good+=match
        if match:examples[u]=match[0]
    return counts, len(all_good),examples

def orth_order(q,d,eps=None):
    if d%2:
        r=(d-1)//2
        return 2*q**(r*r)*prod(q**(2*i)-1 for i in range(1,r+1))
    r=d//2
    assert eps in (-1,1)
    return 2*q**(r*(r-1))*(q**r-eps)*prod(q**(2*i)-1 for i in range(1,r))

def prod(xs):
    out=1
    for x in xs:out*=x
    return out

def legendre(q,a):
    # Only tested on prime fields; the F9 example uses odd-dimensional orthogonal order.
    b=a%q
    return 1 if pow(b,(q-1)//2,q)==1 else -1

def expected(q,m):
    p=3 if q==9 else q
    d=m-1 if m%p else m-2
    if m%p:
        z=sum(1 for u in range(1,q) if (pow(u,3,q)==1 if q!=9 else field(q)[2](field(q)[2](u,u),u)==1))
        eps=legendre(q,(-1)**((d//2))*m) if d%2==0 else None
        return z*orth_order(q,d,eps)
    # Orthogonal space W0 / <1> is the complement of a hyperbolic plane.
    eps=legendre(q,(-1)**(d//2+1)) if d%2==0 else None
    t=(q-1) if d%2==0 else (q-1)//2
    return q**d*t*orth_order(q,d,eps)

if __name__=='__main__':
    checks=[(3,3),(5,3),(7,3),(9,3),(3,4)]
    total=0
    for q,m in checks:
        counts,count,_=enumerate_automorphisms(q,m)
        predicted=expected(q,m)
        print('F_%s K_(1,%s): exact count %s; multipliers %r'%(q,m,count,counts))
        assert count==predicted,(q,m,count,predicted)
        total+=count
    assert total==6+12+36+72+48
    print('STAR_EVOLUTION_AUTOMORPHISMS_OK',len(checks),total)
