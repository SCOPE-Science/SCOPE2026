"""Independent finite checks for cycle-count dependence in fair random tournaments.
Run: python3 verify.py. Uses only Python standard library and integer arithmetic.
"""
from itertools import permutations, combinations
from fractions import Fraction
from math import factorial, comb

assertions = 0

def check(test, msg):
    global assertions
    assert test, msg
    assertions += 1

def falling(n, k):
    ans = 1
    for j in range(k):
        ans *= n-j
    return ans

def cycle_masks(n,k,edge_index):
    out=[]
    # A directed k-cycle is represented by an ordered cyclic word with its
    # smallest element first; no other orientation identification is imposed.
    for vertices in combinations(range(n),k):
        a,*rest=vertices
        for seq in permutations(rest):
            seq=(a,)+seq
            pos=neg=0
            for u,v in zip(seq,seq[1:]+seq[:1]):
                b=1<<edge_index[(min(u,v),max(u,v))]
                if u<v: pos|=b
                else: neg|=b
            out.append((pos,neg))
    return out

def counts_for_n(n):
    edges=list(combinations(range(n),2))
    loc={e:i for i,e in enumerate(edges)}
    masks={k:cycle_masks(n,k,loc) for k in range(3,n+1)}
    all_counts={k:[] for k in masks}
    for sample in range(1<<len(edges)):
        for k,patterns in masks.items():
            cnt=sum((sample&pos)==pos and (sample&neg)==0 for pos,neg in patterns)
            all_counts[k].append(cnt)
        degrees=[0]*n
        for (u,v),bit in loc.items():
            if sample & (1<<bit):degrees[u]+=1
            else:degrees[v]+=1
        score_based=comb(n,3)-sum(d*(d-1)//2 for d in degrees)
        check(all_counts[3][-1]==score_based,f'score identity n={n} sample={sample}')
    return edges,all_counts

def fwht(vec):
    z=list(vec); step=1; size=len(z)
    while step<size:
        for b in range(0,size,2*step):
            for i in range(b,b+step):
                a,c=z[i],z[i+step]
                z[i]=a+c; z[i+step]=a-c
        step*=2
    return z

for n in range(3,7):
    edges,counts=counts_for_n(n)
    N=1<<len(edges)
    t=counts[3]
    Et=Fraction(sum(t),N)
    vt=Fraction(sum(x*x for x in t),N)-Et*Et
    check(Et==Fraction(falling(n,3),24), f'ET n={n}')
    check(vt==Fraction(falling(n,3),32), f'VarT n={n}')
    FT=fwht(t) if n>=4 else None
    for k,ck in counts.items():
        Ec=Fraction(sum(ck),N)
        cov=Fraction(sum(a*b for a,b in zip(t,ck)),N)-Et*Ec
        theory=Fraction(falling(n,k),2**(k+2))
        check(Ec==Fraction(falling(n,k),k*2**k),f'EC n={n} k={k}')
        check(cov==theory,f'Cov n={n} k={k}; {cov} != {theory}')
        alpha=Fraction(falling(n-3,k-3),2**(k-3))
        check(cov==alpha*vt,f'projection constant n={n} k={k}')
        residual=[Fraction(c)-Ec-alpha*(Fraction(a)-Et) for a,c in zip(t,ck)]
        check(sum(residual)==0,f'residual centered n={n} k={k}')
        check(sum((Fraction(a)-Et)*r for a,r in zip(t,residual))==0,f'orthogonality n={n} k={k}')
        if n>=4:
            FC=fwht(ck)
            for idx,(u,v) in enumerate(edges):
                check(FC[1<<idx]==0,f'linear Fourier coefficient n={n} k={k}')
            for i,j in combinations(range(len(edges)),2):
                idx=(1<<i)|(1<<j)
                if set(edges[i]).isdisjoint(edges[j]):
                    check(FC[idx]==0,f'disjoint-pair Fourier n={n} k={k}')
                else:
                    check(Fraction(FC[idx])==alpha*FT[idx],f'wedge Fourier n={n} k={k}')
            for subset in range(1,1<<len(edges)):
                if subset.bit_count()%2:
                    check(FC[subset]==0,f'odd Fourier degree n={n} k={k}')
    print(f'n={n}: {N} tournaments, k=3..{n}, exact means/covariance/projection/Walsh checks passed')
print('PASS:',assertions,'exact integer/fraction assertions')
