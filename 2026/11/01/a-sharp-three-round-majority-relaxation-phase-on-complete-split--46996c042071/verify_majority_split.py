"""Reproducible finite checks of majority dynamics on complete split graphs.

The checks enumerate all binary assignments for small orders and one
representative of every within-part population for larger orders.
No finite check is used as a substitute for the all-parameter proof.
"""
from math import comb


def bit_step(x,a,b):
    n=a+b
    c=(x&((1<<a)-1)).bit_count()
    p=(x>>a).bit_count()
    y=0
    for i in range(n):
        own=(x>>i)&1
        ones=c+p-own if i<a else c
        degree=n-1 if i<a else a
        v=1 if 2*ones>degree else (0 if 2*ones<degree else own)
        y|=v<<i
    return y


def signature_step(left,right,a,b):
    c=sum(left); p=sum(right); s=c+p; n=a+b
    if n%2:
        nl=[int(2*s>n)]*a
    elif 2*s<n:
        nl=[0]*a
    elif 2*s>n:
        nl=[1]*a
    else:
        nl=[1-v for v in left]
    if 2*c<a:
        nr=[0]*b
    elif 2*c>a:
        nr=[1]*b
    else:
        nr=list(right)
    return nl,nr


def predicted(a,b,c,p):
    n=a+b
    return int(n%2==0 and a>b and c+p==n//2 and
               (a-b)/2<c<n/2 and c!=a/2)


def exact_count(a,b):
    if a<=b or (a+b)%2:
        return 0
    r=(a+b)//2
    return (comb(a+b,r)-2*comb(a,r)
            -(comb(a,a//2)*comb(b,b//2) if a%2==0 else 0))


def recurrent_count(a,b):
    n=a+b
    tie=comb(a,a//2)*comb(b,b//2) if a%2==0 and b%2==0 else 0
    return 2+2*int(a<=b)+(2*comb(a,n//2) if a>b and n%2==0 else 0)+tie


def test_all(a,b):
    n=a+b;N=1<<n
    maps=[bit_step(x,a,b) for x in range(N)]
    t=[0]*N
    for x in range(N):
        y=x
        for step in range(4):
            if maps[maps[y]]==y:
                t[x]=step
                break
            y=maps[y]
        else:
            raise AssertionError(('not periodic after three rounds',a,b,x))
        c=(x&((1<<a)-1)).bit_count();p=(x>>a).bit_count()
        assert (t[x]==3)==bool(predicted(a,b,c,p)),(a,b,x,t[x],c,p)
    assert sum(v==0 for v in t)==recurrent_count(a,b),(a,b,sum(v==0 for v in t),recurrent_count(a,b))
    assert sum(maps[x]==x for x in range(N))==2,(a,b,'fixed states')
    t3=sum(v==3 for v in t)
    assert t3==exact_count(a,b), (a,b,t3,exact_count(a,b))
    return t3,N


def test_signatures(a,b):
    tally=0
    for c in range(a+1):
        for p in range(b+1):
            left=[1]*c+[0]*(a-c)
            right=[1]*p+[0]*(b-p)
            initial=(left,right);y=initial
            for step in range(4):
                if signature_step(*signature_step(*y,a,b),a,b)==y:
                    break
                y=signature_step(*y,a,b)
            else:
                raise AssertionError(('signature escape',a,b,c,p))
            assert (step==3)==bool(predicted(a,b,c,p)),(a,b,c,p,step)
            if step==3: tally+=comb(a,c)*comb(b,p)
    assert tally==exact_count(a,b), (a,b,tally,exact_count(a,b))
    return (a+1)*(b+1)


def main():
    total=0;cases=0;t3_total=0
    for n in range(2,17):
        for a in range(1,n):
            b=n-a
            k,N=test_all(a,b)
            total+=N; t3_total+=k; cases+=1
    print('EXHAUSTIVE_PAIRS',cases,'EXHAUSTIVE_STATES',total,'T3_STATES',t3_total)
    signatures=0; large_pairs=0
    for a in range(1,33):
        for b in range(1,33):
            signatures+=test_signatures(a,b);large_pairs+=1
    print('SIGNATURE_PAIRS',large_pairs,'SIGNATURE_CONFIGURATIONS',signatures)
    print('EXAMPLE a=5 b=3 EXACT_T3',exact_count(5,3))
    print('EXAMPLE a=6 b=4 EXACT_T3',exact_count(6,4))
    print('EXAMPLE a=7 b=5 EXACT_T3',exact_count(7,5))
    print('MAJORITY_SPLIT_ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
