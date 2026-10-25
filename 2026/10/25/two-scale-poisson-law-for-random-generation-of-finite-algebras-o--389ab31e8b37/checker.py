from itertools import product
from math import prod

def op(a,b,t):
    out=[]
    for x,y in zip(a,b):
        if t=='and': out.append((0 if x==0 else y if x==2 else 1))
        else: out.append((2 if x==2 else y if x==0 else 1))
    return tuple(out)
def neg(a):return tuple(2-x for x in a)
def down(a):return tuple(2 if x==2 else 0 for x in a)
def closure(g,rs):
    d=len(rs); zero=(0,)*d; one=(2,)*d
    S={zero,one,*g}
    while True:
        L=list(S); T=set(S)
        for x in L:
            T.add(neg(x));T.add(down(x))
            for y in L:
                T.add(op(x,y,'and'));T.add(op(x,y,'or'))
        if T==S: return S
        S=T

def fall(a,b):
    return prod(range(a-b+1,a+1)) if b<=a else 0

def expected(r,s,k):return fall(2**k,r)*fall(3**k-2**k,s)
for r,s,k in [(1,0,0),(1,0,1),(2,0,1),(3,0,2),(0,1,1),(0,2,1),(0,2,2),(1,1,1),(1,1,2),(2,1,2),(1,2,2),(0,3,2)]:
    rs=(2,)*r+(3,)*s
    A=list(product(*[(0,2) if t==2 else (0,1,2) for t in rs]))
    count=0
    for g in product(A,repeat=k):
        if len(closure(g,rs))==len(A): count+=1
    print('case',r,s,k,'count',count,'expected',expected(r,s,k))
    assert count==expected(r,s,k)
print('ALL_CHECKS_OK')
