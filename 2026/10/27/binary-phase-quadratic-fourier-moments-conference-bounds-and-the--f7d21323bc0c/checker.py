#!/usr/bin/env python3
"""Independent finite checks for binary-phase quadratic torus moment theorem."""
from itertools import combinations
from math import comb

def score_signs(n, edge):
    b=0
    for a,c,d,e in combinations(range(n),4):
        x=edge(a,c)*edge(d,e)
        y=edge(a,d)*edge(c,e)
        z=edge(a,e)*edge(c,d)
        b+=(x==y==z)
    return b

def normalized_enumerate(n):
    edges=list(combinations(range(1,n),2))
    d={ij:k for k,ij in enumerate(edges)}
    eq=[]
    for a,b,c,e in combinations(range(n),4):
        def cycle(u,v,w,x):
            mask=0
            for i,j in ((u,v),(v,w),(w,x),(x,u)):
                if i and j:
                    mask ^= (1 << d[tuple(sorted((i,j)))])
            return mask
        eq.append((cycle(a,b,c,e), cycle(a,c,b,e)))
    best=comb(n,4)+1
    count=0
    for v in range(1 << len(edges)):
        s=sum((v&a).bit_count()%2 == 0 and (v&b).bit_count()%2 == 0 for a,b in eq)
        if s<best:
            best,count=s,1
        elif s==best: count+=1
    return best,count

def field(q):
    if q==5:
        values=list(range(5))
        def sub(a,b):return (a-b)%5
        def mul(a,b):return a*b%5
    elif q==9:
        values=[(a,b) for a in range(3) for b in range(3)]
        def sub(a,b):return ((a[0]-b[0])%3,(a[1]-b[1])%3)
        def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
    else:raise ValueError
    zero=values[0]
    sq={mul(x,x) for x in values if x!=zero}
    assert len(sq)==(q-1)//2
    def chi(v):return 0 if v==zero else (1 if v in sq else -1)
    elements=[None]+values
    C=[[0]*(q+1) for _ in range(q+1)]
    for i in range(q+1):
        for j in range(i+1,q+1):
            v=1 if i==0 else chi(sub(elements[i],elements[j]))
            C[i][j]=C[j][i]=v
    assert all(sum(C[i][k]*C[k][j] for k in range(q+1)) == (q if i==j else 0)
               for i in range(q+1) for j in range(q+1))
    return C

def run():
    minima={}
    for n in range(4,8):
        minima[n]=normalized_enumerate(n)
        print(f'exhaustive switching-gauge search n={n}: min={minima[n][0]}, minimizers={minima[n][1]}')
    assert [minima[n] for n in range(4,8)] == [(0,6),(0,12),(0,12),(5,3024)]
    for q in (5,9):
        C=field(q)
        for n in range(4 if q==5 else 7,q+2):
            vals=set()
            for V in combinations(range(q+1),n):
                S=lambda a,b:C[V[a]][V[b]]
                vals.add(score_signs(n,S))
            expected=0 if n<=6 else comb(n,4)//7
            assert vals=={expected},(q,n,vals,expected)
            print(f'Paley q={q}, n={n}, all induced scores={vals}')
    n_to_min={4:0,5:0,6:0,7:5,8:10,9:18,10:30}
    for n,b in n_to_min.items():
        E=comb(n,2)+12*comb(n,3)+4*comb(n,4)+32*b
        exp={4:58,5:150,6:315,7:741,8:1300,9:2124,10:3285}[n]
        assert E==exp
        print(f'moment n={n}, minimum E={E}')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':run()
