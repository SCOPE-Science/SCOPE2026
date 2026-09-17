#!/usr/bin/env python3
"""Brute-force finite check of the theorem in RESULT.md (pure Python)."""
import argparse


def parts(n, hi=None):
    if n == 0:
        yield ()
        return
    hi = min(n, hi or n)
    for a in range(hi, 0, -1):
        for r in parts(n-a, a):
            yield (a,) + r


def catalog(N):
    return [(n,t) for n in range(1,N+1) for t in (('P','C') if n>=3 else ('P',))]


def multisets(total, cat, lo=0):
    if total == 0:
        yield ()
        return
    for i in range(lo, len(cat)):
        n,t = cat[i]
        if n <= total:
            for r in multisets(total-n, cat, i):
                yield ((n,t),) + r


def graph(comps):
    A=[]; off=0; alpha=0; odd=0
    for n,t in comps:
        A += [set() for _ in range(n)]
        for j in range(n-1):
            A[off+j].add(off+j+1); A[off+j+1].add(off+j)
        if t=='C':
            A[off].add(off+n-1); A[off+n-1].add(off)
            alpha += n//2; odd += n%2
        else:
            alpha += (n+1)//2
        off += n
    return A,alpha,odd


def feasible(A, lam):
    n=len(A); k=len(lam); order=sorted(range(n), key=lambda v:-len(A[v]))
    col=[-1]*n; rem=list(lam)
    def dfs(p):
        if p==n: return True
        v=order[p]
        forbidden={col[u] for u in A[v] if col[u]>=0}
        for c in range(k):
            if rem[c] and c not in forbidden:
                rem[c]-=1; col[v]=c
                if dfs(p+1): return True
                col[v]=-1; rem[c]+=1
        return False
    return dfs(0)


def predicted(n, alpha, odd, lam):
    return lam[0] <= alpha and (len(lam)<2 or lam[0]+lam[1] <= n-odd)


def main(N):
    cat=catalog(N); gcount=cases=0
    for n in range(1,N+1):
        for comps in multisets(n,cat):
            A,alpha,odd=graph(comps); gcount+=1
            for lam in parts(n):
                cases+=1
                if feasible(A,lam) != predicted(n,alpha,odd,lam):
                    raise SystemExit(f'MISMATCH n={n} comps={comps} lambda={lam}')
    print(f'PASS max_n={N} graph_types={gcount} graph_partition_cases={cases}')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--max-n',type=int,default=11)
    main(ap.parse_args().max_n)
