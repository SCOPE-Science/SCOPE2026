"""Complete LIS census over 231-avoiding perms, dual-certified patience vs RS."""
import bisect, itertools, json, sys
from functools import lru_cache

def catalan(n):
    from math import comb
    return comb(2*n, n)//(n+1)

def gen231(n):
    """Recursive Catalan decomposition: pi = L n R, values(L)<values(R)."""
    if n == 0:
        yield ()
        return
    for k in range(1, n+1):
        for L in gen231(k-1):
            for R in gen231(n-k):
                # L on values 1..k-1 (as-is), R standardized on k..n-1
                Rshift = tuple(x + (k-1) for x in R)
                yield L + (n,) + Rshift

def avoids231(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a,b,c = p[i],p[j],p[k]
                # order type
                s = sorted([a,b,c])
                rank = {v:i+1 for i,v in enumerate(s)}
                if (rank[a],rank[b],rank[c])==(2,3,1):
                    return False
    return True

def lis_patience(p):
    piles=[]
    for x in p:
        i=bisect.bisect_left(piles,x)
        if i==len(piles): piles.append(x)
        else: piles[i]=x
    return len(piles)

def rs_firstrow(p):
    """Robinson-Schensted row insertion; return first-row length + full tableau rows."""
    T=[]
    for x in p:
        r=0; v=x
        while True:
            if r==len(T):
                T.append([v]); break
            row=T[r]
            i=bisect.bisect_right(row,v)  # row insertion: bump first element > v
            if i==len(row):
                row.append(v); break
            else:
                row[i],v=v,row[i]
                r+=1
    return (len(T[0]) if T else 0), T

def rs_log(p):
    T=[]; lines=[]
    for step,x in enumerate(p):
        r=0; v=x; bumped=[]
        while True:
            if r==len(T):
                T.append([v]); lines.append(f"step {step+1}: insert {x}: new row {r+1} <- {v}; tableau={ [list(rr) for rr in T] }"); break
            row=T[r]
            i=bisect.bisect_right(row,v)
            if i==len(row):
                row.append(v); lines.append(f"step {step+1}: insert {x} (carried {v}): append to row {r+1}; tableau={ [list(rr) for rr in T] }"); break
            else:
                old=row[i]; row[i]=v; bumped.append((r+1,old))
                lines.append(f"step {step+1}: insert {x} (carried {v}): row {r+1} bumps {old} at col {i+1}")
                v=old; r+=1
    return T, lines

def descents(p):
    return sum(1 for i in range(len(p)-1) if p[i]>p[i+1])

def census(n):
    from collections import Counter
    dist=Counter(); maxlis=-1; maxwit=None; mindes=None; mindeswit=None
    total=0; wit_first_rows={}
    for p in gen231(n):
        total+=1
        assert avoids231(p), f"soundness fail {p}"
        a=lis_patience(p)
        b,_=rs_firstrow(p)
        assert a==b, f"dual disagree {p}: {a} vs {b}"
        dist[a]+=1
        d=descents(p)
        if a>maxlis: maxlis=a; maxwit=p
        if mindes is None or d<mindes: mindes=d; mindeswit=p
    assert total==catalan(n), f"completeness {total} vs C{n}={catalan(n)}"
    return dist,total,maxlis,maxwit,mindes,mindeswit

results={}
for n in (9,10):
    dist,total,ml,mw,md,mdw=census(n)
    results[n]={"dist":dict(sorted(dist.items())),"total":total,"maxlis":ml,"maxwit":list(mw),"mindes":md,"mindeswit":list(mdw)}
    print(f"n={n} total={total} C={catalan(n)} dist={dict(sorted(dist.items()))}")
    print(f"  maxLIS={ml} wit={list(mw)} mindes={md} wit={list(mdw)}")

with open("output/artifacts/distribution.json","w") as f:
    json.dump({str(k):v for k,v in results.items()},f,indent=1)
print("wrote distribution.json")
