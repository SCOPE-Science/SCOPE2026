"""Finite checks for neighborhood-complex translation characters of odd folded cubes.

Uses independent vertex-subset enumeration; all arithmetic is exact.
"""
from itertools import combinations
from collections import Counter
from math import comb


def parity(x):
    return x.bit_count() & 1

def vset(n):
    return range(1 << (n-1))

def modv(z, n):
    mask = (1 << n)-1
    return min(z, z ^ mask)

def neighbors(x,n):
    return frozenset(modv(x ^ (1<<i),n) for i in range(n))

def faces(n):
    s=set()
    for x in vset(n):
        nn=sorted(neighbors(x,n))
        for k in range(1,n+1):
            for c in combinations(nn,k):
                s.add(tuple(c))
    return s

def fcounts(fs):
    z=Counter(len(f) for f in fs)
    return tuple(z[k] for k in range(1,max(z)+1))

def translated(face,t,n):
    return tuple(sorted(modv(x ^ t,n) for x in face))

def sign_invariant(face,t,n):
    new = [modv(x^t,n) for x in face]
    idx={v:i for i,v in enumerate(face)}
    p=[idx[x] for x in new]
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return (-1)**inv

def reduced_lefschetz(fs,t,n):
    return sum((-1)**(len(f)-1)*sign_invariant(f,t,n)
               for f in fs if translated(f,t,n)==f)-1

def rank_mod2(cols):
    piv={}
    for c in cols:
        while c:
            j=c.bit_length()-1
            if j in piv: c ^= piv[j]
            else:
                piv[j]=c;break
    return len(piv)

def boundary_ranks(fs):
    buckets={k:sorted(f for f in fs if len(f)==k) for k in range(1,max(map(len,fs))+1)}
    ranks=[]
    for k in range(2,len(buckets)+1):
        ix={f:i for i,f in enumerate(buckets[k-1])}
        cols=[sum(1<<ix[f[:j]+f[j+1:]] for j in range(k)) for f in buckets[k]]
        ranks.append(rank_mod2(cols))
    out=[len(buckets[1])-1-ranks[0]]
    for k in range(2,len(buckets)):
        out.append(len(buckets[k])-ranks[k-2]-ranks[k-1])
    out.append(len(buckets[len(buckets)])-ranks[-1])
    return ranks,out

def K2(n,j):
    return comb(n-j,2)+comb(j,2)-j*(n-j)

def all_checks():
    for n in (3,5,7):
        fs=faces(n)
        v=1<<(n-1)
        f=fcounts(fs)
        expected=(v,v*comb(n,2)//2)+tuple(v*comb(n,k) for k in range(3,n+1))
        assert f==expected,(n,f,expected)
        beta=(1<<(n-3))*(n*n-5*n+8)-1
        assert sum((-1)**i*x for i,x in enumerate(f))-1==beta
        trace={}
        doubles={modv((1<<i)^(1<<j),n) for i in range(n) for j in range(i+1,n)}
        assert len(doubles)==comb(n,2)
        for t in vset(n):
            trace[t]=reduced_lefschetz(fs,t,n)
            e=beta if t==0 else (v//2-1 if t in doubles else -1)
            assert trace[t]==e,('trace',n,t,trace[t],e)
        mult={}
        for y in range(1<<n):
            if y.bit_count()%2: continue
            # The sign character is well-defined on folded vertices for even-weight y.
            mult[y]=sum(trace[t]*(1-2*parity(y&t)) for t in vset(n))//v
            j=y.bit_count()
            target=(n-1)*(n-2)//2 if j==0 else ((n-2*j)**2+n*n-6*n+8)//4
            assert mult[y]==target,(n,j,y,mult[y],target)
        assert sum(mult.values())==beta
        if n in (3,5,7):
            ranks,betti=boundary_ranks(fs)
            assert betti==[0,0,beta]+[0]*(n-3),(n,ranks,betti)
            print('n',n,'facets',v,'fvector',f,'ranks',ranks,'betti_reduced',betti,'characters',dict(Counter((y.bit_count(),m) for y,m in mult.items())))
        else:
            print('n',n,'facets',v,'fvector',f,'beta2',beta,'characters',dict(Counter((y.bit_count(),m) for y,m in mult.items())))
    for n in (9,11,13,15):
        beta=(1<<(n-3))*(n*n-5*n+8)-1
        m0=(n-1)*(n-2)//2
        total=m0+sum(comb(n,j)*(((n-2*j)**2+n*n-6*n+8)//4) for j in range(2,n,2))
        assert total==beta,(n,total,beta)
        print('symbolic multiplicity sum',n,'=',beta)
if __name__=='__main__': all_checks()
