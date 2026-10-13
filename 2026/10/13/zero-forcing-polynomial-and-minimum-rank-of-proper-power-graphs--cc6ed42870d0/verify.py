#!/usr/bin/env python3
from itertools import product, combinations
from collections import defaultdict

def params(p,q,d):
    assert p != q and p % 2 == 1 and q % 2 == 1 and d >= 2
    t=(p**d-1)//(p-1)
    a=p-1
    c=q-1
    h=(p-1)*(q-1)
    s=a+h
    n=p**d*q-1
    return t,a,c,h,s,n

def build_class_graph(p,q,d):
    t,a,c,h,s,n=params(p,q,d)
    V=[]
    classes={}
    classes["C"]=[("C",j) for j in range(c)]
    V += classes["C"]
    for i in range(t):
        classes[f"A{i}"]=[("A",i,j) for j in range(a)]
        classes[f"H{i}"]=[("H",i,j) for j in range(h)]
        V += classes[f"A{i}"]+classes[f"H{i}"]
    N={v:set() for v in V}
    def add_clique(L):
        for x,y in combinations(L,2):
            N[x].add(y); N[y].add(x)
    add_clique(classes["C"])
    for i in range(t):
        A=classes[f"A{i}"]; H=classes[f"H{i}"]
        add_clique(A); add_clique(H)
        for x in A:
            for y in H:
                N[x].add(y); N[y].add(x)
        for x in H:
            for y in classes["C"]:
                N[x].add(y); N[y].add(x)
    assert len(V)==n
    return V,N,classes

def zero_forces(blue,N):
    blue=set(blue)
    while len(blue)<len(N):
        move=None
        for v in N:
            if v in blue:
                W=N[v]-blue
                if len(W)==1:
                    move=next(iter(W))
                    break
        if move is None:
            return False
        blue.add(move)
    return True

def criterion(bits):
    # bits = (Cwhite, (Awhite,Hwhite), ...)
    cwhite=bits[0]
    r=sum(1 for aw,hw in bits[1:] if aw and hw)
    return r<=1

def representative_state(classes,bits):
    white=set()
    if bits[0]:
        white.add(classes["C"][0])
    for i,(aw,hw) in enumerate(bits[1:]):
        if aw: white.add(classes[f"A{i}"][0])
        if hw: white.add(classes[f"H{i}"][0])
    return white

def poly_formula(p,q,d):
    t,a,c,h,s,n=params(p,q,d)
    # C(u) * [B0(u)^t + t B2(u) B0(u)^(t-1)]
    def mul(P,Q):
        R=defaultdict(int)
        for i,x in P.items():
            for j,y in Q.items():
                R[i+j]+=x*y
        return dict(R)
    def ppow(P,k):
        R={0:1}
        for _ in range(k):
            R=mul(R,P)
        return R
    C={c:1,c-1:c}
    B0={s:1,s-1:s}
    B2={s-2:a*h}
    P=mul(C,ppow(B0,t))
    T=mul(C,mul({k:t*v for k,v in B2.items()},ppow(B0,t-1)))
    R=defaultdict(int)
    for k,v in P.items(): R[k]+=v
    for k,v in T.items(): R[k]+=v
    return dict(sorted(R.items()))

def weighted_pattern_poly(p,q,d):
    t,a,c,h,s,n=params(p,q,d)
    out=defaultdict(int)
    # Enumerate white/no-white choice at the class level.
    for Cw in (0,1):
        for branchbits in product([(0,0),(1,0),(0,1),(1,1)], repeat=t):
            bits=(Cw,)+branchbits
            if not criterion(bits):
                continue
            kwhite=Cw+sum(x+y for x,y in branchbits)
            blue=n-kwhite
            mult=(c if Cw else 1)
            for aw,hw in branchbits:
                if aw: mult*=a
                if hw: mult*=h
            out[blue]+=mult
    return dict(sorted(out.items()))

def direct_group_graph(p,q,d):
    # Additive C_p^d x C_q. Exclude identity.
    zero=(0,)*d+(0,)
    elements=[pv+(y,) for pv in product(range(p), repeat=d) for y in range(q)
              if pv+(y,)!=zero]
    def order(x):
        hasp=any(v%p for v in x[:d])
        hasq=(x[-1]%q)!=0
        return (p if hasp else 1)*(q if hasq else 1)
    def mult(k,x):
        return tuple((k*x[i])%p for i in range(d)) + ((k*x[-1])%q,)
    cyclic={}
    for x in elements:
        cyclic[x]={mult(k,x) for k in range(order(x))}
    N={x:set() for x in elements}
    for x,y in combinations(elements,2):
        if x in cyclic[y] or y in cyclic[x]:
            N[x].add(y); N[y].add(x)
    return elements,N

def classify_element(x,p,q):
    pv=x[:-1]; y=x[-1]
    if all(v==0 for v in pv):
        return ("C",None)
    # normalize projective p-line by first nonzero coordinate
    i=next(j for j,v in enumerate(pv) if v)
    inv=pow(pv[i],-1,p)
    line=tuple((v*inv)%p for v in pv)
    return (("A" if y==0 else "H"),line)

def compare_direct(p,q,d):
    elements,N=direct_group_graph(p,q,d)
    # Check abstract adjacency rule using normalized line labels.
    for x,y in combinations(elements,2):
        tx,lx=classify_element(x,p,q)
        ty,ly=classify_element(y,p,q)
        pred=False
        if tx=="C" and ty=="C": pred=True
        elif tx=="C" and ty=="H" or ty=="C" and tx=="H": pred=True
        elif lx is not None and lx==ly and tx in ("A","H") and ty in ("A","H"):
            pred=True
        assert (y in N[x])==pred,(p,q,d,x,y,tx,lx,ty,ly)
    return len(elements)

def check_rank_witness(p,q,d):
    # Verify the symbolic dot-product table of the t+2 dimensional witness.
    t,a,c,h,s,n=params(p,q,d)
    # coordinates e_0,...,e_{t-1}, f, g; metric diag(1,...,1,1,-1)
    dim=t+2
    def dot(x,y):
        return sum(x[i]*y[i] for i in range(t+1))-x[t+1]*y[t+1]
    e=[]
    for i in range(t):
        v=[0]*dim; v[i]=1; e.append(tuple(v))
    f=[0]*dim; f[t]=1; f=tuple(f)
    g=[0]*dim; g[t+1]=1; g=tuple(g)
    w=tuple(f[i]+g[i] for i in range(dim))
    Avec=e
    Hvec=[tuple(e[i][j]+w[j] for j in range(dim)) for i in range(t)]
    assert dot(w,w)==0 and dot(f,w)==1
    for i in range(t):
        assert dot(Avec[i],Avec[i])!=0
        assert dot(Hvec[i],Hvec[i])!=0
        assert dot(Avec[i],Hvec[i])!=0
        assert dot(Hvec[i],f)!=0
        assert dot(Avec[i],f)==0
        for j in range(t):
            if i!=j:
                assert dot(Avec[i],Avec[j])==0
                assert dot(Avec[i],Hvec[j])==0
                assert dot(Hvec[i],Hvec[j])==0
    assert dot(f,f)!=0
    # e_i, f, and w span dim dimensions; g=w-f.
    return dim

for p,q,d in [(3,5,2),(5,3,2)]:
    V,N,classes=build_class_graph(p,q,d)
    t,a,c,h,s,n=params(p,q,d)
    # Exhaust all representative white profiles with at most one white per true-twin class.
    total=0
    for Cw in (0,1):
        for bb in product([(0,0),(1,0),(0,1),(1,1)],repeat=t):
            bits=(Cw,)+bb
            W=representative_state(classes,bits)
            ok=zero_forces(set(V)-W,N)
            assert ok==criterion(bits),(p,q,d,bits,ok)
            total+=1
    assert weighted_pattern_poly(p,q,d)==poly_formula(p,q,d)
    P=poly_formula(p,q,d)
    z=min(P)
    assert z==p**d*q-t-3
    assert P[z]==t*(p-1)**2*(q-1)**2*(q*(p-1))**(t-1)
    dim=check_rank_witness(p,q,d)
    assert dim==t+2
    direct_n=compare_direct(p,q,d)
    assert direct_n==n
    print(f"p={p}, q={q}, d={d}: profiles={total}, vertices={n}, Z={z}, min_sets={P[z]}, rank_witness={dim}, direct_group_graph=OK")

# One d=3 symbolic polynomial/minimum check without large graph construction.
p,q,d=3,5,3
t,a,c,h,s,n=params(p,q,d)
P=poly_formula(p,q,d)
assert min(P)==p**d*q-t-3
assert P[min(P)]==t*(p-1)**2*(q-1)**2*(q*(p-1))**(t-1)
assert check_rank_witness(p,q,d)==t+2
print(f"p={p}, q={q}, d={d}: symbolic polynomial and rank witness OK; t={t}, Z={min(P)}")
print("VERIFY_OK")
