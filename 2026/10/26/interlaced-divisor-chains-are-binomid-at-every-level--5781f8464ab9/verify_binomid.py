"""Exact finite integer-exponent checks for the interlaced divisor-chain theorem."""
from random import Random


def columns(e):
    N=len(e)
    prefix=[0]
    for x in e: prefix.append(prefix[-1]+x)
    for k in range(1,N+1):
        c=[prefix[n+k-1]-prefix[n-1]-prefix[k] for n in range(1,N-k+2)]
        yield k,c


def check_binomid(e):
    p=[0]
    for x in e: p.append(p[-1]+x)
    for n in range(1,len(e)+1):
        for k in range(1,n+1):
            if p[n]-p[n-k]<p[k]:
                return False,(n,k,p[n]-p[n-k]-p[k])
    return True,None


def run():
    r=Random(23022023)
    examples=0
    for _ in range(400):
        n=r.randrange(10,85)
        a=[r.randrange(0,4),0]
        a[1]=a[0]+r.randrange(0,4)
        for j in range(2,n): a.append(a[j-2]+r.randrange(0,3))
        assert check_binomid(a)[0]
        for k,c in columns(a):
            assert check_binomid(c)[0],(a,k,c)
            examples+=1
    for q in range(2,55):
        for prime in (2,3,5):
            e=[int(n%2==0 or n>=2*q+1) for n in range(1,120)]
            assert all(e[i]<=e[i+2] for i in range(len(e)-2))
            assert e[0]<=e[1]
            for k,c in columns(e):
                assert check_binomid(c)[0],(q,prime,k,c)
                examples+=1
    bad=(0,1,1)*25
    assert check_binomid(bad)[0]
    c=dict(columns(bad))[2]
    assert c[:5]==[0,1,0,0,1],c[:5]
    assert not check_binomid(c)[0]
    print(f'PASS: {examples} finite second-level column tests, plus sharp 3-step counterexample')

if __name__=='__main__':run()
