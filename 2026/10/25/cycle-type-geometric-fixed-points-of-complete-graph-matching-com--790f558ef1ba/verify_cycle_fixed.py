#!/usr/bin/env python3
"""Exact finite tests for a cycle-type geometric fixed-point theorem.
Only the matching-complex mathematics is computed here.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import factorial

def permutation(lengths):
    p=[]; starts=[]; n=0
    for d in lengths:
        starts.append(tuple(range(n,n+d)))
        for i in range(d): p.append(n+(i+1)%d)
        n+=d
    return p,starts

def fixed_edge_orbits(p):
    n=len(p); unseen={tuple(x) for x in combinations(range(n),2)}
    valid=[]
    while unseen:
        start=min(unseen); orb=[]; v=start
        while v not in orb:
            orb.append(v)
            unseen.remove(v)
            v=tuple(sorted((p[v[0]],p[v[1]])))
        assert v==start
        endpoints=[j for e in orb for j in e]
        if len(set(endpoints))==len(endpoints): valid.append(tuple(sorted(orb)))
    return valid

def predicted_support_orbit_counts(cycles):
    m=Counter(map(len,cycles)); out=Counter()
    for d,count in m.items():
        for i in range(count):
            if d%2==0:out[(d,i)]+=1
            for j in range(i+1,count):out[(d,i,j)]+=d
    return out

def orbit_supports(orbits,cycles):
    which={v:(len(c),k) for d in sorted(set(map(len,cycles))) for k,c in enumerate([c for c in cycles if len(c)==d]) for v in c}
    output=[]
    for orbit in orbits:
        support=tuple(sorted(set(which[v] for edge in orbit for v in edge)))
        assert len(set(d for d,_ in support))==1
        d=support[0][0]
        sig=(d,)+tuple(i for _,i in support)
        output.append((sig, frozenset(support)))
    return output

def face_coefficients(supports):
    coeff=Counter({0:1})
    def recurse(i,used,k):
        if i==len(supports):return
        for j in range(i,len(supports)):
            sup=supports[j]
            if not used.intersection(sup):
                coeff[k+1]+=1
                recurse(j+1,used|sup,k+1)
    recurse(0,frozenset(),0)
    return coeff

def formula_coefficients(cycles):
    grouped=Counter(map(len,cycles)); poly=[1]
    for d,m in sorted(grouped.items()):
        one=Counter()
        for p in range(m//2+1):
            c=factorial(m)//(2**p*factorial(p)*factorial(m-2*p)) * d**p
            if d%2==0:
                from math import comb
                for h in range(m-2*p+1):one[p+h]+=c*comb(m-2*p,h)
            else:one[p]+=c
        new=[0]*(len(poly)+max(one))
        for a,x in enumerate(poly):
            for b,y in one.items():new[a+b]+=x*y
        poly=new
    return Counter({i:v for i,v in enumerate(poly) if v})

def component_faces(d,m):
    supports=[]
    if d%2==0:
        supports.extend([(i,) for i in range(m)])
    for i,j in combinations(range(m),2):
        supports.extend([(i,j)]*d)
    faces={():1}
    def walk(prefix,last,used):
        for j in range(last,len(supports)):
            s=supports[j]
            if all(v not in used for v in s):
                f=prefix+(j,)
                faces[f]=1
                walk(f,j+1,used|set(s))
    walk((),0,set())
    return [sorted([f for f in faces if len(f)==i]) for i in range(max(map(len,faces))+1)]

def gf2rank(columns):
    pivots={};rk=0
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k in pivots:x^=pivots[k]
            else:pivots[k]=x;rk+=1;break
    return rk

def reduced_bettis(faces):
    f=[len(x) for x in faces]; r=[0]*len(f)
    for t in range(1,len(f)):
        prev={x:i for i,x in enumerate(faces[t-1])}
        cols=[]
        for z in faces[t]:
            col=0
            for i in range(t):col^=1<<prev[z[:i]+z[i+1:]]
            cols.append(col)
        r[t]=gf2rank(cols)
    return [f[t]-r[t]- (r[t+1] if t+1<len(r) else 0) for t in range(1,len(f))]

def verify_morse_acyclic(d,m):
    # Hasse arrows: downward for unmatched covers, upward for matched covers.
    supports=[]
    if d%2==0: supports.extend([(i,) for i in range(m)])
    for i,j in combinations(range(m),2):supports.extend([(i,j)]*d)
    flat=[tuple(x) for level in component_faces(d,m) for x in level]
    face_set=set(flat); matching={}; critical=[]
    loop_count=m if d%2==0 else 0
    for f in flat:
        used=set(v for j in f if j>=loop_count for v in supports[j])
        free=[i for i in range(m) if i not in used]
        if not free:
            critical.append(f);continue
        pivot=free[0]
        if pivot in f:
            lower=tuple(j for j in f if j!=pivot);upper=f
        else:
            lower=f;upper=tuple(sorted(f+(pivot,)))
        assert lower in face_set and upper in face_set
        matching[lower]=upper
    matched={(lo,hi) for lo,hi in matching.items()}
    edges={f:[] for f in flat}; indeg={f:0 for f in flat}
    for hi in flat:
        for j in range(len(hi)):
            lo=hi[:j]+hi[j+1:]
            x,y=(lo,hi) if (lo,hi) in matched else (hi,lo)
            edges[x].append(y); indeg[y]+=1
    q=[f for f in flat if indeg[f]==0];n=0
    while q:
        f=q.pop();n+=1
        for g in edges[f]:
            indeg[g]-=1
            if indeg[g]==0:q.append(g)
    assert n==len(flat),(d,m,n,len(flat))
    exp=0 if m%2 else d**(m//2)*factorial(m)//(2**(m//2)*factorial(m//2))
    assert len(critical)==exp,(d,m,len(critical),exp)
    assert all(len(f)==m//2 for f in critical)
    return len(flat)

def main():
    patterns=[(1,1,1,1),(2,),(2,1,1),(2,2),(2,2,1,1),(3,),(3,3),(3,3,3),(4,),(4,4),(6,6),(2,4,4),(2,2,3,3),(3,3,4,4),(4,6),(3,3,3,3),(5,5),(2,2,4,4),(1,1,1,2,2)]
    ccount=0
    for lengths in patterns:
        p,cycles=permutation(lengths)
        orbits=fixed_edge_orbits(p)
        direct=Counter(sig for sig,_ in orbit_supports(orbits,cycles))
        pred=predicted_support_orbit_counts(cycles)
        assert direct==pred,(lengths,direct,pred)
        supports=[support for _,support in orbit_supports(orbits,cycles)]
        co=face_coefficients(supports)
        ex=formula_coefficients(cycles)
        assert co==ex,(lengths,co,ex)
        ccount+=1
    hcount=0
    for d in (2,4,6):
        for m in (1,2,3,4,5):
            fs=component_faces(d,m)
            got=reduced_bettis(fs)
            if m%2:want=[0]*len(got)
            else:
                want=[0]*len(got)
                q=(d**(m//2))*factorial(m)//(2**(m//2)*factorial(m//2))
                want[m//2-1]=q
            assert got==want,(d,m,got,want)
            hcount+=1
    morse_faces=sum(verify_morse_acyclic(d,m) for d in (2,4,6) for m in range(1,6))
    print('CYCLE_ORBIT_FIXED_SPACE_CHECKS_OK',ccount,'cycle_types',hcount,'even_component_mod2_cases',morse_faces,'acyclic_matched_faces')
if __name__=='__main__':main()
