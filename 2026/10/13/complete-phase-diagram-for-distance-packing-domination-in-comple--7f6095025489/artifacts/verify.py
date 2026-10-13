from itertools import product
from math import comb

def profiles(total):
    out=[]
    def rec(rem,last,cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for x in range(last,rem+1):
            cur.append(x); rec(rem-x,x,cur); cur.pop()
    rec(total,1,[])
    return out

def graph(profile):
    parts=[]
    for i,n in enumerate(profile):
        parts += [i]*n
    N=len(parts)
    dist=[[0]*N for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if u==v: dist[u][v]=0
            elif parts[u]!=parts[v]: dist[u][v]=1
            else: dist[u][v]=2
    return parts,dist

def direct(profile,d,p,mask):
    parts,dist=graph(profile)
    N=len(parts)
    S=[i for i in range(N) if (mask>>i)&1]
    if not S: return False
    for u in range(N):
        if u not in S and min(dist[u][x] for x in S)>d:
            return False
    for a in range(len(S)):
        for b in range(a+1,len(S)):
            if dist[S[a]][S[b]]<p+1:
                return False
    return True

def formula_coeff(profile,d,p):
    N=sum(profile); r=len(profile)
    q=sum(1 for n in profile if n==1)
    c=[0]*(N+1)
    if d==0:
        if p==0: c[N]=1
        return c
    if d==1:
        if p==0:
            # all subsets meeting >=2 parts, plus whole parts
            for s in range(N+1): c[s]+=comb(N,s)
            for n in profile:
                for s in range(n+1): c[s]-=comb(n,s)
            c[0]+=r-1
            for n in profile: c[n]+=1
            return c
        if p==1:
            for n in profile: c[n]+=1
            return c
        c[1]=q
        return c
    # d>=2
    if p==0:
        for s in range(1,N+1): c[s]=comb(N,s)
        return c
    if p==1:
        for n in profile:
            for s in range(1,n+1): c[s]+=comb(n,s)
        return c
    c[1]=N
    return c

def gamma_from_coeff(c):
    for i,x in enumerate(c):
        if x: return i
    return None

profiles_checked=0
parameter_cases=0
subset_checks=0
for N in range(2,9):
    for profile in profiles(N):
        profiles_checked+=1
        for d in range(0,5):
            for p in range(0,5):
                parameter_cases+=1
                brute=[0]*(N+1)
                for mask in range(1<<N):
                    subset_checks+=1
                    if direct(profile,d,p,mask):
                        brute[mask.bit_count()]+=1
                form=formula_coeff(profile,d,p)
                if brute!=form:
                    raise AssertionError(("coeff",profile,d,p,brute,form))
                # check gamma table implicitly from first nonzero
                gb=gamma_from_coeff(brute); gf=gamma_from_coeff(form)
                if gb!=gf:
                    raise AssertionError(("gamma",profile,d,p,gb,gf))
print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles_checked}; "
    f"parameter_cases={parameter_cases}; "
    f"subset_checks={subset_checks}; "
    "orders=2..8; d,p=0..4"
)
