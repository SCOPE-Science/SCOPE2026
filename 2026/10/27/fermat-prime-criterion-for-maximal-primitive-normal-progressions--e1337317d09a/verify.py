"""Direct finite enumerator for maximal primitive progressions (plain Python)."""
from math import gcd

def factors(n):
    ans=[]; d=2
    while d*d<=n:
        if n%d==0:
            ans.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:ans.append(n)
    return ans

def check(p,d):
    assert pow(d,(p-1)//2,p)==p-1
    nn=p*p-1
    fs=factors(nn)
    def mul(v,w):
        a,b=v; c,e=w
        return ((a*c + d*b*e)%p,(a*e+b*c)%p)
    def power(x,k):
        r=(1,0)
        while k:
            if k&1:r=mul(r,x)
            x=mul(x,x);k//=2
        return r
    F=[(a,b) for a in range(p) for b in range(p)]
    prim={x for x in F if x!=(0,0) and all(power(x,nn//ell)!=(1,0) for ell in fs)}
    count=0; others=0
    for a in F:
        for b in F:
            if b==(0,0):continue
            if all(((a[0]+i*b[0])%p,(a[1]+i*b[1])%p) in prim for i in range(p-1)):
                count+=1
                if a!=b:others+=1
    tot=sum(gcd(i,nn)==1 for i in range(1,nn+1))
    assert len(prim)==tot
    expected=tot if (p-1)&(p-2)==0 else 0
    assert count==expected and others==0,(p,count,expected,others)
    print(f'EXACT p={p} q={p*p} primitive={len(prim)} length={p-1} valid_ordered_pairs={count} distinct_start_step_exceptions={others} cert=OK')
for p,d in [(5,2),(7,3),(11,2),(17,3)]:check(p,d)
