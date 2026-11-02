"""Standalone finite consistency checks for the stated odd-parameter Lucas-companion theorem.
These modular tests are not a substitute for the infinite matrix proof.
"""

def matmul(a,b,mod):
    return ((a[0]*b[0]+a[1]*b[2])%mod,(a[0]*b[1]+a[1]*b[3])%mod,
            (a[2]*b[0]+a[3]*b[2])%mod,(a[2]*b[1]+a[3]*b[3])%mod)

def matpow(a,n,mod):
    res=(1,0,0,1)
    while n:
        if n&1:res=matmul(res,a,mod)
        a=matmul(a,a,mod)
        n//=2
    return res

def check():
    pairs=0
    rows=0
    for p in range(-15,16,2):
        A=(p,1,1,0)
        assert matpow(A,6,8)==(5,0,0,5)
        for k in range(2,13):
            q=2**(k+1)
            target=(1+2**k)%q
            assert matpow(A,3*2**(k-1),q)==(target,0,0,target)
        for k in range(1,12):
            q=2**k
            x,y=2%q,p%q
            seen=set()
            states=set()
            while (x,y) not in states:
                states.add((x,y))
                seen.add(x)
                x,y=y,(p*y+x)%q
            assert all(t in seen for t in range(1,q,2)), (p,k)
            rows+=1
        x,y=2,p
        for n in range(1,511):
            x,y=y,p*y+x
            t=0
            a=abs(x)
            assert a>0
            while a%2==0:
                a//=2;t+=1
            expected=0 if n%3 else (1 if n%2==0 else 2)
            assert t==expected,(p,n,t,expected)
            pairs+=1
    print(f'VERIFY_OK: {rows} finite modular unit-coverage cases; {pairs} valuation checks; matrix lifts through k=12 for all 16 odd parameters.')
if __name__=='__main__':check()
