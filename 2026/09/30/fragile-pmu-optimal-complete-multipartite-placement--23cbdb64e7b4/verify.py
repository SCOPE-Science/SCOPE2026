from fractions import Fraction
from itertools import product
from math import comb

QS = [Fraction(1,5), Fraction(1,2), Fraction(4,5)]


def partitions(n):
    out=[]
    def rec(rem,last,cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for x in range(last, rem+1):
            rec(rem-x,x,cur+[x])
    rec(n,1,[])
    return out


def build_graph(parts):
    part=[]
    for i,r in enumerate(parts):
        part.extend([i]*r)
    n=len(part)
    adj=[set() for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if part[u] != part[v]:
                adj[u].add(v); adj[v].add(u)
    return adj,part


def power_dominates(adj,S):
    if not S:
        return False
    observed=set(S)
    for v in S:
        observed.update(adj[v])
    while True:
        add=set()
        for v in observed:
            un=[u for u in adj[v] if u not in observed]
            if len(un)==1:
                add.add(un[0])
        if not add-observed:
            break
        observed.update(add)
    return len(observed)==len(adj)


def structural(parts,part_of,S):
    if not S:
        return False
    counts={}
    for v in S:
        counts[part_of[v]]=counts.get(part_of[v],0)+1
    if len(counts)>=2:
        return True
    i,t=next(iter(counts.items()))
    return t >= parts[i]-1


def H(r,s,x):
    top=min(s,max(r-2,0))
    return sum((Fraction(comb(s,t))*x**t for t in range(1,top+1)), Fraction(0))


def delta(r,j,x):
    top=min(j,max(r-2,0))
    return sum((Fraction(comb(j-1,t-1))*x**t for t in range(1,top+1)), Fraction(0))


def formula(parts,occ,q):
    ell=sum(occ)
    if ell==0:
        return Fraction(0)
    x=(1-q)/q
    return 1-q**ell*(1+sum(H(r,s,x) for r,s in zip(parts,occ)))


def direct(parts,occ,q):
    adj,part_of=build_graph(parts)
    sensors=[]
    base=0
    for r,s in zip(parts,occ):
        sensors.extend(range(base,base+s))
        base += r
    p=1-q
    ans=Fraction(0)
    m=len(sensors)
    for mask in range(1<<m):
        surviving=[sensors[j] for j in range(m) if (mask>>j)&1]
        if power_dominates(adj,surviving):
            ans += p**len(surviving)*q**(m-len(surviving))
    return ans


def greedy(parts,ell,q):
    x=(1-q)/q
    occ=[0]*len(parts)
    for _ in range(ell):
        choices=[]
        for i,r in enumerate(parts):
            if occ[i] < r:
                choices.append((delta(r,occ[i]+1,x),i))
        _,i=min(choices)
        occ[i]+=1
    return tuple(occ)


def all_occ(parts,ell):
    for occ in product(*[range(r+1) for r in parts]):
        if sum(occ)==ell:
            yield occ

structural_checks=0
formula_checks=0
optimizer_checks=0
marginal_checks=0
corollary_checks=0
multipartite_types=0

for n in range(2,9):
    for parts in partitions(n):
        multipartite_types += 1
        adj,part_of=build_graph(parts)
        for mask in range(1<<n):
            S=[v for v in range(n) if (mask>>v)&1]
            assert power_dominates(adj,S) == structural(parts,part_of,S)
            structural_checks += 1
        for occ in product(*[range(r+1) for r in parts]):
            if sum(occ)==0:
                continue
            for q in QS:
                assert direct(parts,occ,q) == formula(parts,occ,q)
                formula_checks += 1
        for q in QS:
            x=(1-q)/q
            for r in parts:
                ds=[delta(r,j,x) for j in range(1,r+1)]
                assert all(ds[j] <= ds[j+1] for j in range(len(ds)-1))
                marginal_checks += max(0,len(ds)-1)
        for ell in range(1,n+1):
            for q in QS:
                x=(1-q)/q
                go=greedy(parts,ell,q)
                gc=sum(H(r,s,x) for r,s in zip(parts,go))
                best=min(sum(H(r,s,x) for r,s in zip(parts,o)) for o in all_occ(parts,ell))
                assert gc == best
                optimizer_checks += 1
                b0=sum(r for r in parts if r<=2)
                b1=3*sum(1 for r in parts if r==3) + sum(1 for r in parts if r>=4)
                if ell <= b0:
                    target=1-q**ell
                    assert formula(parts,go,q)==target
                    corollary_checks += 1
                elif ell <= b0+b1:
                    target=1-q**ell*(1+(ell-b0)*x)
                    assert formula(parts,go,q)==target
                    corollary_checks += 1

print(f"multipartite_types={multipartite_types}")
print(f"structural_checks={structural_checks}")
print(f"formula_checks={formula_checks}")
print(f"marginal_monotonicity_checks={marginal_checks}")
print(f"optimizer_checks={optimizer_checks}")
print(f"closed_form_corollary_checks={corollary_checks}")
print("VERIFY_OK")
