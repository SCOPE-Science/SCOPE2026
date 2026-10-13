from math import isqrt

EXPECTED=[12,18,20,24,40,56,88,104,196,234,650]

def factor(n):
    x=n; f={}; p=2
    while p*p<=x:
        while x%p==0:
            f[p]=f.get(p,0)+1; x//=p
        p=3 if p==2 else p+2
    if x>1: f[x]=f.get(x,0)+1
    return f

def sigma_from_factor(f):
    s=1
    for p,a in f.items():
        s*= (p**(a+1)-1)//(p-1)
    return s

def near(n):
    f=factor(n); s=sigma_from_factor(f); d=s-2*n
    return d>0 and d<n and n%d==0, d

for n in EXPECTED:
    ok,d=near(n)
    assert ok,(n,d)

# The finite scan is regression evidence only, not the universal proof.
got=[]
for n in range(2,1_000_001):
    f=factor(n)
    if sum(f.values())<=4:
        ok,d=near(n)
        if ok: got.append(n)
assert got==EXPECTED,(got,EXPECTED)

# Exact algebraic branch checks appearing in the symbolic proof.
# Omega=3: 4p and 2p^2 candidates.
assert [(p,7-p) for p in (3,5) if (4*p)%(7-p)==0]==[(3,4),(5,2)]
assert (-3**2+3*3+3)==3 and (2*3**2)%3==0
# Omega=4, 8p branch.
assert [(p,15-p) for p in (3,5,7,11,13) if (8*p)%(15-p)==0]==[(3,12),(5,10),(7,8),(11,4),(13,2)]
# 4p^2 branch.
vals=[]
for p in (3,5,7):
    d=-p*p+7*p+7
    if d>0 and (4*p*p)%d==0: vals.append((p,d))
assert vals==[(7,7)]
# 2r^2 s branch with r<s: only (3,13) and (5,13).
sol=[]
for r in (3,5):
    if r==3:
        for s in (5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73):
            d=3*(s+13)
            if d>0 and (2*r*r*s)%d==0: sol.append((r,s,d))
    else:
        for s in (7,11,13):
            d=93-7*s
            if d>0 and (2*r*r*s)%d==0: sol.append((r,s,d))
assert sol==[(3,13,78),(5,13,2)],sol
print('VERIFY_OK expected=%d scan_limit=1000000 max=%d' % (len(EXPECTED), max(EXPECTED)))
