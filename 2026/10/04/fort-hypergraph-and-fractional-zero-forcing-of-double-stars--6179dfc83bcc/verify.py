from itertools import combinations
from math import floor
from scipy.optimize import linprog

def double_star(a,b):
    # centers 0,1; A leaves 2..a+1; B leaves a+2..a+b+1
    n=a+b+2
    adj=[set() for _ in range(n)]
    u,v=0,1
    adj[u].add(v); adj[v].add(u)
    A=list(range(2,2+a))
    B=list(range(2+a,n))
    for x in A:
        adj[u].add(x); adj[x].add(u)
    for y in B:
        adj[v].add(y); adj[y].add(v)
    return adj,u,v,A,B

def is_fort(adj, mask):
    if mask == 0:
        return False
    n=len(adj)
    for v in range(n):
        if (mask>>v)&1:
            continue
        c=sum((mask>>w)&1 for w in adj[v])
        if c == 1:
            return False
    return True

def minimal_forts(adj):
    n=len(adj)
    forts=[m for m in range(1,1<<n) if is_fort(adj,m)]
    forts.sort(key=int.bit_count)
    mins=[]
    for m in forts:
        if not any((q & m) == q for q in mins):
            mins.append(m)
    return mins

def is_zero_forcing(adj, mask):
    n=len(adj)
    blue=mask
    full=(1<<n)-1
    while True:
        changed=False
        for u in range(n):
            if not ((blue>>u)&1):
                continue
            white=[v for v in adj[u] if not ((blue>>v)&1)]
            if len(white)==1:
                blue |= 1<<white[0]
                changed=True
                break
        if not changed:
            return blue==full

def solve_fractional(n, mins):
    A=[]; b=[]
    for m in mins:
        row=[0.0]*n
        for v in range(n):
            if (m>>v)&1:
                row[v]=-1.0
        A.append(row); b.append(-1.0)
    res=linprog([1.0]*n,A_ub=A,b_ub=b,bounds=[(0.0,1.0)]*n,method="highs")
    assert res.success
    return res.fun

def coord_range(n, mins, opt, idx):
    A=[]; b=[]
    for m in mins:
        row=[0.0]*n
        for v in range(n):
            if (m>>v)&1:
                row[v]=-1.0
        A.append(row); b.append(-1.0)
    Aeq=[[1.0]*n]; beq=[opt]
    c=[0.0]*n; c[idx]=1.0
    lo=linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=[(0.0,1.0)]*n,method="highs")
    c[idx]=-1.0
    hi=linprog(c,A_ub=A,b_ub=b,A_eq=Aeq,b_eq=beq,bounds=[(0.0,1.0)]*n,method="highs")
    assert lo.success and hi.success
    return lo.fun,-hi.fun

graphs=subsets=minimal_forts_checked=coord_lps=0
for a in range(2,7):
    for b in range(2,7):
        adj,u,v,A,B=double_star(a,b)
        n=len(adj)
        mins=minimal_forts(adj)
        expected=[]
        for x,y in combinations(A,2):
            expected.append((1<<x)|(1<<y))
        for x,y in combinations(B,2):
            expected.append((1<<x)|(1<<y))
        assert set(mins)==set(expected),(a,b,len(mins),len(expected))
        minimal_forts_checked += len(mins)

        opt=solve_fractional(n,mins)
        assert abs(opt-(a+b)/2.0)<1e-9,(a,b,opt)

        for idx in range(n):
            lo,hi=coord_range(n,mins,opt,idx)
            coord_lps += 2
            if idx in (u,v):
                assert abs(lo)<1e-9 and abs(hi)<1e-9,(a,b,idx,lo,hi)
            elif idx in A:
                if a==2:
                    assert abs(lo)<1e-9 and abs(hi-1.0)<1e-9,(a,b,idx,lo,hi)
                else:
                    assert abs(lo-0.5)<1e-9 and abs(hi-0.5)<1e-9,(a,b,idx,lo,hi)
            else:
                if b==2:
                    assert abs(lo)<1e-9 and abs(hi-1.0)<1e-9,(a,b,idx,lo,hi)
                else:
                    assert abs(lo-0.5)<1e-9 and abs(hi-0.5)<1e-9,(a,b,idx,lo,hi)

        # direct zero-forcing minimum
        z=n+1
        for mask in range(1<<n):
            subsets += 1
            if is_zero_forcing(adj,mask):
                z=min(z,mask.bit_count())
        assert z==a+b-2,(a,b,z)

        assert floor(a/2)+floor(b/2) <= z
        graphs += 1

print("VERIFY_OK")
print("double_star_parameter_pairs_checked =",graphs)
print("vertex_subsets_checked_for_zero_forcing =",subsets)
print("minimal_forts_checked =",minimal_forts_checked)
print("coordinate_optimization_LPs =",coord_lps)
print("parameters a,b = 2..6")
print("all minimal forts are same-side leaf pairs")
print("all fractional optima equal (a+b)/2")
print("all optimal-coordinate ranges match the stated optimizer classification")
print("all zero-forcing numbers equal a+b-2")
