#!/usr/bin/env python3
"""Exact, standalone arithmetic and independent profile checks for ternary cyclic bigram uniqueness."""
from math import factorial, gcd
from functools import lru_cache
from collections import Counter

@lru_cache(None)
def fact(k): return factorial(k)

def degree(k,i): return sum(k[3*i:3*i+3])

def word_count(k):
    n=sum(k)
    active=[i for i in range(3) if degree(k,i)]
    if len(active)==0: return 0
    if len(active)==1:
        return 1 if k[3*active[0]+active[0]]==n else 0
    seen={active[0]}
    pending=[active[0]]
    while pending:
        v=pending.pop()
        for w in active:
            if w not in seen and (k[3*v+w] or k[3*w+v]):
                seen.add(w);pending.append(w)
    if len(seen)!=len(active):return 0
    if len(active)==2:
        a,b=active
        tau=k[3*a+b]
    else:
        a,b,c=active
        # directed matrix-tree determinant rooted at a; self-loops omitted.
        tau=(k[3*b+a]+k[3*b+c])*(k[3*c+a]+k[3*c+b])-k[3*b+c]*k[3*c+b]
    num=n*tau
    for i in active:num*=fact(degree(k,i)-1)
    den=1
    for entry in k:den*=fact(entry)
    assert num%den==0,(k,num,den)
    return num//den

def phi(k):return sum(gcd(i,k)==1 for i in range(1,k+1))

def necklaces(k):
    n=sum(k);g=0
    for v in k:g=gcd(g,v)
    result=sum(phi(d)*word_count(tuple(v//d for v in k)) for d in range(1,g+1) if g%d==0)
    assert result%n==0,(k,result)
    return result//n

def predicted(n):
    if n<=5:return [0,3,6,11,24,45][n]
    return n*n+9*n-26+[0,7,4,3,4,7][n%6]

def generate(n):
    for t in range(-(n//3),n//3+1):
        for a in range((n-3*abs(t))//2+1):
            for b in range((n-3*abs(t)-2*a)//2+1):
                for c in range((n-3*abs(t)-2*a-2*b)//2+1):
                    rem=n-3*abs(t)-2*(a+b+c)
                    p=max(0,t);m=max(0,-t)
                    k=[0]*9
                    k[1]=a+p;k[3]=a+m
                    k[5]=b+p;k[7]=b+m
                    k[6]=c+p;k[2]=c+m
                    for l0 in range(rem+1):
                        for l1 in range(rem-l0+1):
                            k[0]=l0;k[4]=l1;k[8]=rem-l0-l1
                            yield tuple(k)

def criterion(k):
    n=sum(k)
    active=[i for i in range(3) if degree(k,i)]
    if len(active)==1:return True
    if len(active)==2:
        u,v=active
        r=k[3*u+v]
        if not r or r!=k[3*v+u]:return False
        lu,lv=k[3*u+u],k[3*v+v]
        return r==1 or lu+lv==0 or (lu+lv==1)
    if len(active)!=3:return False
    t=k[1]-k[3]
    if t<0:
        # Swap labels 1 and 2: reverse triangle orientation.
        perm=(0,2,1)
        k=tuple(k[3*perm[i]+perm[j]] for i in range(3) for j in range(3))
        t=-t
    a=k[3];b=k[7];c=k[2]  # 01 reverse, 12 reverse, 20 reverse for positive triangle
    loops=[k[0],k[4],k[8]]
    if t>0:
        pairs=[i for i,v in enumerate((a,b,c)) if v>0]
        if not pairs:
            return t==1 or sum(loops)==0 or (sum(loops)==1)
        if len(pairs)>1:return False
        v=(a,b,c)[pairs[0]]
        if t>1 and v>1:return False
        if t>1:return not any(loops)
        # t=1: the one unvisited vertex of the reciprocal pair can receive arbitrary loops.
        excluded_vertex=[2,0,1][pairs[0]]
        return all(loops[i]==0 for i in range(3) if i!=excluded_vertex)
    pairs=[i for i,v in enumerate((a,b,c)) if v>0]
    if len(pairs)!=2:return False
    # path with two reciprocal edge families and one common middle vertex
    missing=({0,1,2}-set(pairs)).pop()
    middle=[2,0,1][missing]
    # for a: 0-1; b: 1-2; c: 0-2
    endpoints=[0,1,2]
    endpoints.remove(middle)
    # map each reciprocal pair to its leaf
    pair_leaves={0:(0,1),1:(1,2),2:(0,2)}
    r=[]
    for j in pairs:
        leaf=next(x for x in pair_leaves[j] if x!=middle)
        r.append((leaf,(a,b,c)[j]))
    if min(w for _,w in r)>1:return False
    if loops[middle]:return False
    for leaf,w in r:
        if w>1 and loops[leaf]:return False
    return True

# A fixed polynomial certificate that adding one reciprocal pair cannot reduce
# the normalized BEST expression in the relevant support regimes.
def polynomial_certificate():
    from collections import defaultdict
    V=('a','b','c','u')
    one={(0,0,0,0):1};zero={}
    def c(v):return {(0,0,0,0):v} if v else {}
    def var(v):return {tuple(int(x==v) for x in V):1}
    def add(*args):
        out=defaultdict(int)
        for x in args:
            for k,v in x.items():out[k]+=v
        return {k:v for k,v in out.items() if v}
    def neg(x):return {k:-v for k,v in x.items()}
    def mul(x,y):
        out=defaultdict(int)
        for k,v in x.items():
            for j,w in y.items():out[tuple(a+b for a,b in zip(k,j))]+=v*w
        return {k:v for k,v in out.items() if v}
    A=var('a');C=var('c');U=var('u')
    for T,B in ((add(one,U),var('b')),(zero,add(one,U))):
        # tau=ab+ac+at+bc+bt+ct+t^2
        tau=add(mul(A,B),mul(A,C),mul(A,T),mul(B,C),mul(B,T),mul(C,T),mul(T,T))
        d=add(B,C,T)
        s0=add(A,C,T);s1=add(A,B,T)
        lhs=mul(add(tau,d),mul(s0,s1))
        rhs=mul(tau,mul(add(A,T,one),add(A,one)))
        difference=add(lhs,neg(rhs))
        assert all(v>=0 for v in difference.values()),difference
        assert difference

if __name__=='__main__':
    polynomial_certificate()
    for n in range(1,26):
        count=0
        for k in generate(n):
            direct=(necklaces(k)==1)
            predicted_unique=criterion(k)
            assert direct==predicted_unique,(n,k,direct,predicted_unique)
            count+=direct
        assert count==predicted(n),(n,count,predicted(n))
    print('VERIFY_OK: exact BEST/Burnside counts, all matrix classifications to n=25, independent polynomial certificate')
