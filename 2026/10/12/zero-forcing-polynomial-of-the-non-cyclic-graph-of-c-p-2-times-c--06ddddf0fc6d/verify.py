#!/usr/bin/env python3
from itertools import combinations, product
from math import comb


def add(x,y,p):
    return ((x[0]+y[0])%(p*p),(x[1]+y[1])%p)

def smul(k,x,p):
    return ((k*x[0])%(p*p),(k*x[1])%p)

def order(x,p):
    if x==(0,0): return 1
    y=(0,0)
    for k in range(1,p*p+1):
        y=add(y,x,p)
        if y==(0,0): return k
    raise RuntimeError

def cyclic_subgroup(x,p):
    return {smul(k,x,p) for k in range(order(x,p))}

def direct_graph(p):
    V=[x for x in product(range(p*p),range(p)) if x!=(0,0)]
    H={x:cyclic_subgroup(x,p) for x in V}
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            cyc=(x in H[y]) or (y in H[x])
            if not cyc:
                N[i].add(j);N[j].add(i)
    return V,N

def class_of(x,p):
    a,b=x
    if a%p==0:
        aa=(a//p)%p
        if b==0:
            return ('P',0)
        # order-p line in F_p^2 different from P: normalize b to 1
        inv=pow(b,-1,p)
        slope=(aa*inv)%p
        return ('B',slope)
    # order p^2; normalize first coordinate modulo p to 1.
    u=a%p
    inv=pow(u,-1,p)
    j=(b*inv)%p
    return ('A',j)

def class_sizes(p):
    V,_=direct_graph(p)
    d={}
    for x in V:d.setdefault(class_of(x,p),[]).append(x)
    return d

def predicted_edge(c,d):
    kc,ic=c; kd,id=d
    if c==d:return False
    if kc=='P': return kd=='B'
    if kd=='P': return kc=='B'
    if kc=='A' and kd=='A': return ic!=id
    if kc=='B' and kd=='B': return ic!=id
    return {kc,kd}=={'A','B'}

def zero_forces(blue,N):
    blue=set(blue)
    while True:
        move=None
        for v in sorted(blue):
            white=N[v]-blue
            if len(white)==1:
                move=next(iter(white)); break
        if move is None:return len(blue)==len(N)
        blue.add(move)

def false_twin_classes(V,N,p):
    d={}
    for i,x in enumerate(V):d.setdefault(class_of(x,p),[]).append(i)
    for C in d.values():
        for i in C:
            for j in C:
                if i!=j:
                    assert j not in N[i]
                    assert N[i]==N[j]
    return d

def weighted_polynomial(p):
    V,N=direct_graph(p)
    d=false_twin_classes(V,N,p)
    labels=sorted(d, key=lambda z:(z[0],z[1]))
    reps={c:d[c][0] for c in labels}
    n=len(V)
    coeff={}
    # A forcing set cannot omit two false twins. Enumerate all admissible white class sets.
    for r in range(len(labels)+1):
        for Wcls in combinations(labels,r):
            W={reps[c] for c in Wcls}
            blue=set(range(n))-W
            if zero_forces(blue,N):
                weight=1
                for c in Wcls: weight*=len(d[c])
                coeff[n-r]=coeff.get(n-r,0)+weight
    return V,N,d,coeff

def formula(p):
    if p==2:
        return {4:20,5:18,6:7,7:1}
    N=p**3-1
    c4=p**4*(p-1)**5//2
    c3=p**3*(p-1)**3*(p*p+1)//2
    c2=p*(p-1)**2*(p**3+p*p+3*p+1)//2
    return {N-4:c4,N-3:c3,N-2:c2,N-1:N,N:1}

for p in (2,3,5):
    V,N,d,coeff=weighted_polynomial(p)
    assert coeff==formula(p),(p,coeff,formula(p))
    # Verify exact class sizes and the complete quotient adjacency table.
    s=p-1; a=p*(p-1)
    assert len(d[('P',0)])==s
    for i in range(p):
        assert len(d[('A',i)])==a
        assert len(d[('B',i)])==s
    for c,C in d.items():
        for e,E in d.items():
            if c==e: continue
            expected=predicted_edge(c,e)
            for x in C[:min(2,len(C))]:
                for y in E[:min(2,len(E))]:
                    assert ((y in N[x])==expected)
    print(f"p={p}: N={len(V)}, class_sizes=P:{s}, A:{a}x{p}, B:{s}x{p}, polynomial={coeff}")

# Independently brute-force every subset for the seven-vertex boundary.
V,N=direct_graph(2)
brute={}
for k in range(len(V)+1):
    c=sum(zero_forces(C,N) for C in combinations(range(len(V)),k))
    if c:brute[k]=c
assert brute==formula(2)
print(f"p=2 exhaustive_all_subsets={brute}")

# Verify the closed coefficients and class-peeling criterion for several odd primes without expanding vertices.
for p in (3,5,7,11):
    s=p-1; a=p*s; N=p**3-1
    # peelable white profiles (epsilon,r,t): P indicator, number A classes, number B classes.
    good=[]
    for eps in (0,1):
        for r in range(p+1):
            for t in range(p+1):
                k=eps+r+t
                peel=((t<=1 and r<=2) or (eps==0 and r==0 and t==2))
                if peel: good.append((eps,r,t))
    assert max(sum(x) for x in good)==4
    # Weighted coefficients by profile.
    coeff={}
    for eps,r,t in good:
        k=eps+r+t
        wt=(s**eps)*comb(p,r)*(a**r)*comb(p,t)*(s**t)
        coeff[N-k]=coeff.get(N-k,0)+wt
    assert coeff==formula(p),(p,coeff,formula(p))
    print(f"p={p}: profile_formula_OK min_omitted=4 min_sets={formula(p)[N-4]}")

print('VERIFY_OK')
