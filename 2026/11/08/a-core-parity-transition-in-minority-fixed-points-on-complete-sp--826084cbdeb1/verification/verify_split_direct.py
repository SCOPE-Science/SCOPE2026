"""Direct bitwise verification of stable minority states on complete split graphs."""
from math import comb

def step(a,b,x):
    N=a+b
    out=0
    for v in range(N):
        nbr=[u for u in range(N) if u!=v and (v<a or u<a)]
        ones=sum((x>>u)&1 for u in nbr)
        if 2*ones<len(nbr) or (2*ones==len(nbr) and ((x>>v)&1)):
            out|=1<<v
    return out

def expected(a,b):
    if a%2: return 2
    B=(comb(b,b//2) if b%2==0 else 2*comb(b,b//2))
    return 2+comb(a,a//2)*B

if __name__=='__main__':
    total=0
    for a in range(1,9):
        for b in range(a, min(12,17-a)+1):
            f=sum(step(a,b,x)==x for x in range(1<<(a+b)))
            e=expected(a,b)
            assert f==e,(a,b,f,e)
            total+=1<<(a+b)
            print('%d %d %d' %(a,b,f))
    print('PASS split direct; configurations examined:',total)
