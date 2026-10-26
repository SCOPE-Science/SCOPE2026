from collections import defaultdict
from math import comb

def composition_count(L,r,s):
    if not(0 <= s <= r): return 0
    if s==r: return 1 if L==r else 0
    q=r-s
    if L< s+2*q:return 0
    return comb(r,s)*comb(L-r-1,q-1)

def hist_formula(n):
    counts=defaultdict(int)
    counts[(0,0)]=1
    counts[(n,n)]=1
    for h in range(1,n):
        for r in range(1,min(h,n-h)+1):
            for s in range(r+1):
                a=composition_count(h,r,s)
                if not a:continue
                for t in range(r+1):
                    b=composition_count(n-h,r,t)
                    if not b:continue
                    z=n*a*b
                    assert z%r==0,(n,h,r,s,t,z)
                    counts[(h,h-s+t)]+=z//r
    return counts

def hist_brute(n):
    counts=defaultdict(int)
    for m in range(1<<n):
        h=m.bit_count()
        p=0
        for i in range(n):
            p+=(((m>>((i-1)%n))&1)+((m>>i)&1)+((m>>((i+1)%n))&1)>=2)
        counts[(h,p)]+=1
    return counts

if __name__=='__main__':
    for n in range(3,19):
        f=hist_formula(n); b=hist_brute(n)
        assert dict(f)==dict(b),(n, sorted(set(f.items())^set(b.items()))[:4])
        assert sum(f.values())==2**n
        if n%2:
            q=(n+1)//2
            h=min(h for (h,p),cnt in f.items() if p>=q and cnt)
            threshold=(n+5)//3 # ceil((n+3)/3)
            assert h==threshold,(n,h,threshold)
            crit=sum(c for (x,p),c in f.items() if x==h and p>=q)
            print('odd',n,'q',q,'hcrit',h,'critical winning profiles',crit,'all winning minority',sum(c for (x,p),c in f.items() if x<q and p>=q))
    for n in range(3,102,2):
        f=hist_formula(n)
        q=(n+1)//2
        h=(n+5)//3
        total=sum(v for (hh,pp),v in f.items() if hh==h and pp>=q)
        if n in (3,5,7): expected=comb(n,q)
        elif n%6==3: expected=n
        elif n%6==5: expected=n*(2*((n-5)//6)+3)
        else:
            k=(n-1)//6
            expected=n*(7*k*k+3*k+4)//2
        assert total==expected,(n,total,expected)
    print('PASS: independent exact histograms for n=3..18; closed critical formula on odd n through 101')
