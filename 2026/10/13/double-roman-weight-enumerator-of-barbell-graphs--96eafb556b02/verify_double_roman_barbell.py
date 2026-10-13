from itertools import product
from collections import Counter
from math import comb


def poly_add(a,b):
    c=Counter(a); c.update(b); return Counter({k:v for k,v in c.items() if v})

def poly_mul(a,b):
    c=Counter()
    for i,ai in a.items():
        for j,bj in b.items(): c[i+j]+=ai*bj
    return Counter(c)

def poly_pow(a,n):
    r=Counter({0:1}); b=Counter(a)
    while n:
        if n&1:r=poly_mul(r,b)
        b=poly_mul(b,b); n//=2
    return r

def poly_scale(a,s): return Counter({k:s*v for k,v in a.items() if s*v})

def poly_sub(a,b): return poly_add(a,poly_scale(b,-1))

def mono(k,c=1): return Counter({k:c})

def shift(a,k): return Counter({i+k:v for i,v in a.items()})

def formula(n):
    m=n-1
    S=Counter({0:1,1:1,2:1,3:1})
    P01=Counter({0:1,1:1})
    Sm=poly_pow(S,m)
    p01m=poly_pow(P01,m)
    term=poly_scale(shift(poly_pow(P01,m-1),2),m)
    G=poly_add(poly_sub(poly_sub(Sm,p01m),term),mono(m+1,m))
    H=poly_sub(poly_sub(Sm,p01m),term)
    J=poly_add(poly_sub(Sm,p01m),mono(m,1))
    A=H; B=G; C=shift(G,1); D=shift(J,2); E=shift(Sm,3)
    # A^2+C^2+D^2+E^2+2(AC+BD+BE+CD+CE+DE)
    W=Counter()
    for p in (A,C,D,E): W=poly_add(W,poly_mul(p,p))
    for p,q in ((A,C),(B,D),(B,E),(C,D),(C,E),(D,E)):
        W=poly_add(W,poly_scale(poly_mul(p,q),2))
    return W

def graph(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for base in (0,n):
        for i in range(base,base+n):
            for j in range(i+1,base+n):
                adj[i].add(j); adj[j].add(i)
    adj[0].add(n); adj[n].add(0)
    return adj

def valid(vals,adj):
    for v,a in enumerate(vals):
        if a==0:
            ns=[vals[u] for u in adj[v]]
            if 3 not in ns and sum(x==2 for x in ns)<2:return False
        elif a==1:
            if not any(vals[u]>=2 for u in adj[v]):return False
    return True

checks=0; valid_count=0
for n in range(2,6):
    adj=graph(n); brute=Counter()
    for vals in product(range(4), repeat=2*n):
        checks+=1
        if valid(vals,adj):
            brute[sum(vals)]+=1; valid_count+=1
    got=formula(n)
    assert brute==got,(n,brute,got)
    mn=min(brute)
    if n==2: assert (mn,brute[mn])==(5,4)
    elif n==3: assert (mn,brute[mn])==(6,13)
    else: assert (mn,brute[mn])==(6,n*n)
# symbolic finite coefficient sanity for more n from formula
for n in range(6,13):
    got=formula(n); mn=min(k for k,v in got.items() if v)
    assert mn==6 and got[mn]==n*n
print(f'VERIFY_OK n_bruteforce=2..5 labelings={checks} valid_functions={valid_count} formula_n=2..12 coefficient_checks={sum(len(formula(n)) for n in range(2,13))} max_order=24')
