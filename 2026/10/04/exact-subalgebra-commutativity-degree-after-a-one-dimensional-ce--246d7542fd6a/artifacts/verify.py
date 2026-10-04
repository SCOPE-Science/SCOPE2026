from itertools import combinations, product
from fractions import Fraction

def rref_subspaces(n,p):
    out=[]
    for k in range(n+1):
        for piv in combinations(range(n),k):
            free=[j for j in range(n) if j not in piv]
            slots=[]
            for i,pc in enumerate(piv):
                for j in free:
                    if j>pc:
                        slots.append((i,j))
            for vals in product(range(p), repeat=len(slots)):
                rows=[[0]*n for _ in range(k)]
                for i,pc in enumerate(piv): rows[i][pc]=1
                for (ij,val) in zip(slots,vals):
                    i,j=ij; rows[i][j]=val
                out.append(tuple(tuple(r) for r in rows))
    return out

def rank(rows,p):
    a=[list(r) for r in rows if any(x%p for x in r)]
    if not a: return 0
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if a[i][c]%p),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][c],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]%p:
                f=a[i][c]%p
                a[i]=[(a[i][j]-f*a[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def contains(rows,v,p):
    return rank(rows,p)==rank(list(rows)+[v],p)

def bracket(a,b,p):
    # basis order x,y,z,c; only [x,y]=z
    t=(a[0]*b[1]-a[1]*b[0])%p
    return (0,0,t,0)

def is_subalg(rows,p):
    for a in rows:
        for b in rows:
            if not contains(rows, bracket(a,b,p),p): return False
    return True

def permutes(A,B,p):
    rows=list(A)+list(B)
    for a in A:
        for b in B:
            if not contains(rows, bracket(a,b,p),p): return False
    return True

def formula(q):
    S=2*q**3+4*q**2+3*q+5
    bad=q**4*(q+1)*(3*q+1)
    good=S*S-bad
    return S,bad,good,Fraction(good,S*S)

for p in (2,3):
    subs=[U for U in rref_subspaces(4,p) if is_subalg(U,p)]
    S,bad,good,sd=formula(p)
    assert len(subs)==S,(p,len(subs),S)
    brute_bad=sum(1 for A in subs for B in subs if not permutes(A,B,p))
    assert brute_bad==bad,(p,brute_bad,bad)
    print(f"q={p} subalgebras={S} nonpermutable_ordered_pairs={bad} sd={sd}")
for q in (5,7,11):
    S,bad,good,sd=formula(q)
    assert good==q**6+12*q**5+27*q**4+44*q**3+49*q**2+30*q+25
    print(f"q={q} formula_subalgebras={S} formula_nonpermutable={bad} sd={sd}")
print("CHECK_OK")
