#!/usr/bin/env python3
"""Independent finite checks for local-block transfer formulas on Boolean Ockham algebras.
Scientific semantics: P([n]); twisted complement ~(S)={i: sigma(i) not in S}.
"""
from itertools import product, permutations
from math import prod
import random

def var(i): return ('v',i)
def meet(a,b): return ('&',a,b)
def join(a,b): return ('|',a,b)
def neg(a): return ('~',a)
ZERO=('0',); ONE=('1',)

def depth(t):
    if t[0]=='~':return 1+depth(t[1])
    if t[0] in ('&','|'):return max(depth(t[1]),depth(t[2]))
    return 0

def eval_local(t,block):
    def walk(node,offset):
        op=node[0]
        if op=='v':return block[offset][node[1]]
        if op=='0':return 0
        if op=='1':return 1
        if op=='~':return 1-walk(node[1],offset+1)
        if op=='&':return walk(node[1],offset)&walk(node[2],offset)
        if op=='|':return walk(node[1],offset)|walk(node[2],offset)
        raise ValueError(op)
    return walk(t,0)

def allowed(eq,k):
    d=max(depth(eq[0]),depth(eq[1]));q=2**k;D=d+1
    seq=list(product((0,1),repeat=k))
    good=set()
    for z in product(range(q),repeat=D):
        w=[seq[j] for j in z]
        if eval_local(eq[0],w)==eval_local(eq[1],w):good.add(z)
    return d,q,good

def transfer_count(eq,k,n):
    d,q,good=allowed(eq,k)
    count=0
    for z in product(range(q),repeat=n):
        if all(tuple(z[(i+j)%n] for j in range(d+1)) in good for i in range(n)):
            count+=1
    return count

def matrix_trace(eq,k,n):
    d,q,good=allowed(eq,k)
    if d==0:return len(good)**n
    # Actual integer transfer powers; avoid floating approximations.
    states=list(product(range(q),repeat=d)); ix={s:i for i,s in enumerate(states)}
    R=len(states); A=[[0]*R for _ in states]
    for word in good:
        A[ix[word[:d]]][ix[word[1:]]]+=1
    def mm(A,B):
        C=[[0]*R for _ in range(R)]
        for i in range(R):
            for h in range(R):
                if A[i][h]:
                    for j in range(R):
                        if B[h][j]:C[i][j]+=A[i][h]*B[h][j]
        return C
    B=[[int(i==j) for j in range(R)] for i in range(R)]
    for _ in range(n):B=mm(B,A)
    return sum(B[i][i] for i in range(R))

def direct_count(eq,k,n):
    # For cycle permutation 0->1->..->n-1.
    ans=0
    for words in product(range(1<<n),repeat=k):
        def ev(t):
            typ=t[0]
            if typ=='v':return words[t[1]]
            if typ=='0':return 0
            if typ=='1':return (1<<n)-1
            if typ=='&':return ev(t[1]) & ev(t[2])
            if typ=='|':return ev(t[1]) | ev(t[2])
            if typ=='~':
                v=ev(t[1]); shift=sum(((v>>((i+1)%n))&1)<<i for i in range(n))
                return ((1<<n)-1)^shift
            raise ValueError(typ)
        if ev(eq[0])==ev(eq[1]):ans+=1
    return ans

x=var(0);y=var(1)
equations={
    'double_negation':(neg(neg(x)),x,1),
    'excluded_middle':(join(x,neg(x)),ONE,1),
    'noncontradiction':(meet(x,neg(x)),ZERO,1),
    'de_morgan':(neg(meet(x,y)),join(neg(x),neg(y)),2),
    'triple_negation':(neg(neg(neg(x))),neg(x),1),
    'join_implication':(join(x,neg(y)),join(neg(y),x),2),
    'twisted_absorption':(meet(x,neg(neg(y))),x,2),
    'second_order':(neg(join(x,neg(y))),meet(neg(x),neg(neg(y))),2),
    'contradictory':(meet(x,neg(x)),ONE,1),
    'neg_fixed':(x,neg(x),1),
}
for label,(eq1,eq2,k) in equations.items():
    d=max(depth(eq1),depth(eq2));nmax=9 if k==1 else 5
    for n in range(1,nmax+1):
        m=matrix_trace((eq1,eq2),k,n)
        b=transfer_count((eq1,eq2),k,n)
        a=direct_count((eq1,eq2),k,n)
        assert a==b==m,(label,n,a,b,m)
        if label=='double_negation':
            from math import gcd
            assert a==2**gcd(n,2),(label,n,a)
        if label=='excluded_middle':assert a==2
print('VERIFY_OK equation_templates=%s independent_cycle_assignments=%s full_transfer_matrix=YES' % (len(equations),sum(sum((1<<(n*k)) for n in range(1,(9 if k==1 else 5)+1)) for (_,_,k) in equations.values())))

def cycle_lengths(p):
    visited=set();result=[]
    for u in range(len(p)):
        if u in visited:continue
        n=0;v=u
        while v not in visited:
            visited.add(v);n+=1;v=p[v]
        result.append(n)
    return result

def direct_perm_count(eq,k,p):
    n=len(p); ans=0
    for words in product(range(1<<n),repeat=k):
        def ev(t):
            typ=t[0]
            if typ=='v':return words[t[1]]
            if typ=='0':return 0
            if typ=='1':return (1<<n)-1
            if typ=='&':return ev(t[1]) & ev(t[2])
            if typ=='|':return ev(t[1]) | ev(t[2])
            if typ=='~':
                v=ev(t[1]); shift=sum(((v>>p[i])&1)<<i for i in range(n))
                return ((1<<n)-1)^shift
            raise ValueError(typ)
        if ev(eq[0])==ev(eq[1]):ans+=1
    return ans
samples=0
for label in ['double_negation','excluded_middle','de_morgan','triple_negation','twisted_absorption','neg_fixed']:
    e1,e2,k=equations[label]
    for n in range(1,6):
        for p in permutations(range(n)):
            predicted=prod(matrix_trace((e1,e2),k,L) for L in cycle_lengths(p))
            observed=direct_perm_count((e1,e2),k,p)
            assert predicted==observed,(label,n,p,predicted,observed)
            samples+=1
print('PERMUTATION_PRODUCT_OK models=%s size_at_most=5' % samples)

def prime_cost(n):
    bound=n  # p=2 gives 2**v2(n), at most n.
    for p in range(2,n+3):
        if any(p%d==0 for d in range(2,int(p**.5)+1)):continue
        v=1
        while n%(p*v)==0:v*=p
        bound=min(bound,v*(p-1))
    return bound
for a in range(2,81,2):
    delta=min(L-__import__('math').gcd(L,a) for L in range(1,a+100) if a%L)
    assert delta==prime_cost(a),(a,delta,prime_cost(a))
print('ARITHMETIC_SHARP_GAP_OK even_iterates=2..80')
