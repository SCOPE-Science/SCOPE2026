from collections import Counter
from functools import lru_cache
from math import comb
from fractions import Fraction

def profiles_of(total):
    out=[]
    def rec(rem,last,cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for x in range(last,rem+1):
            cur.append(x)
            rec(rem-x,x,cur)
            cur.pop()
    rec(total,1,[])
    return out

@lru_cache(None)
def perfect(a):
    a=tuple(a)
    s=sum(a)
    if s==0:
        return 1
    if s%2:
        return 0
    if max(a)>s//2:
        return 0
    i=next(i for i,x in enumerate(a) if x)
    ans=0
    for j,x in enumerate(a):
        if j!=i and x:
            b=list(a)
            b[i]-=1
            b[j]-=1
            ans += x*perfect(tuple(b))
    return ans

def formula_distribution(profile):
    n=tuple(profile)
    N=sum(n)
    ans=Counter()
    if N%2==0:
        ans[N//2] += perfect(n)
    for i,ni in enumerate(n):
        for u in range(1,ni+1):
            if (N-u)%2:
                continue
            b=list(n)
            b[i]-=u
            q=perfect(tuple(b))
            if q:
                ans[(N-u)//2] += comb(ni,u)*q
    return ans

def direct_distribution(profile):
    part_of=[]
    for i,n in enumerate(profile):
        part_of += [i]*n
    N=len(part_of)
    edges=[(u,v) for u in range(N) for v in range(u+1,N)
           if part_of[u]!=part_of[v]]
    counts=Counter()
    examined=0

    def rec(remaining,chosen):
        nonlocal examined
        if not remaining:
            examined += 1
            used=set()
            for u,v in chosen:
                used.add(u)
                used.add(v)
            if all(u in used or v in used for u,v in edges):
                counts[len(chosen)] += 1
            return
        v=min(remaining)
        rest=set(remaining)
        rest.remove(v)

        rec(rest,chosen)

        for w in list(rest):
            if part_of[w]!=part_of[v]:
                newrest=set(rest)
                newrest.remove(w)
                chosen.append((v,w))
                rec(newrest,chosen)
                chosen.pop()

    rec(set(range(N)),[])
    return counts,examined

def spectrum_criterion(profile,m):
    N=sum(profile)
    if 2*m==N:
        return max(profile)<=m
    u=N-2*m
    if u<1:
        return False
    for i,ni in enumerate(profile):
        if u<=ni:
            residual_i=ni-u
            other=max((profile[j] for j in range(len(profile)) if j!=i),
                      default=0)
            if max(residual_i,other)<=m:
                return True
    return False

profiles=0
examined=0
maximal=0

for N in range(2,9):
    for profile in profiles_of(N):
        profiles += 1
        direct,nexam=direct_distribution(profile)
        formula=formula_distribution(profile)
        examined += nexam
        maximal += sum(direct.values())

        if direct != formula:
            raise AssertionError(("distribution",profile,direct,formula))

        for m in range(0,N//2+1):
            if ((direct.get(m,0)>0) != spectrum_criterion(profile,m)):
                raise AssertionError(("spectrum",profile,m,direct))

        if direct:
            avg_direct=Fraction(sum(m*c for m,c in direct.items()),
                                sum(direct.values()))
            avg_formula=Fraction(sum(m*c for m,c in formula.items()),
                                 sum(formula.values()))
            if avg_direct != avg_formula:
                raise AssertionError(("average",profile,avg_direct,avg_formula))

print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles}; "
    f"matchings_examined={examined}; "
    f"maximal_matchings={maximal}; "
    "orders=2..8"
)
