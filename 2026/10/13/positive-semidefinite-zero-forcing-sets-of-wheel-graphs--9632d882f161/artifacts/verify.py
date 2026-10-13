from itertools import combinations


def wheel_adj(n):
    # vertices 0..m-1 are rim, h=m
    m=n-1; h=m
    adj=[set() for _ in range(n)]
    for i in range(m):
        j=(i+1)%m
        adj[i].add(j); adj[j].add(i)
        adj[i].add(h); adj[h].add(i)
    return adj


def comps_white(adj, blue):
    n=len(adj); W=[v for v in range(n) if v not in blue]
    seen=set(); comps=[]
    for s in W:
        if s in seen: continue
        stack=[s]; seen.add(s); comp=set()
        while stack:
            u=stack.pop(); comp.add(u)
            for v in adj[u]:
                if v not in blue and v not in seen:
                    seen.add(v); stack.append(v)
        comps.append(comp)
    return comps


def psd_forcing(adj, S):
    blue=set(S); n=len(adj)
    while len(blue)<n:
        changed=False
        for C in comps_white(adj, blue):
            # any blue u may force if exactly one neighbor in this white component
            for u in list(blue):
                N=adj[u] & C
                if len(N)==1:
                    blue.add(next(iter(N)))
                    changed=True
                    break
            if changed: break
        if not changed: return False
    return True


def criterion(n,S):
    m=n-1; h=m; R=set(range(m)); S=set(S)
    rim=S & R
    if h in S:
        return len(rim)>=2
    # three consecutive rim vertices cyclically
    if len(rim)<3: return False
    return any(i in rim and (i+1)%m in rim and (i+2)%m in rim for i in range(m))


def cyclic_no111_counts(m):
    cnt=[0]*(m+1)
    for mask in range(1<<m):
        bits=[(mask>>i)&1 for i in range(m)]
        if any(bits[i] and bits[(i+1)%m] and bits[(i+2)%m] for i in range(m)):
            continue
        cnt[sum(bits)] += 1
    return cnt


def poly_add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def mat_mul(A,B):
    d=len(A)
    C=[[[0] for _ in range(d)] for __ in range(d)]
    for i in range(d):
        for k in range(d):
            if A[i][k]==[0]: continue
            for j in range(d):
                if B[k][j]==[0]: continue
                C[i][j]=poly_add(C[i][j],poly_mul(A[i][k],B[k][j]))
    return C

def mat_pow(A,e):
    d=len(A)
    I=[[[1] if i==j else [0] for j in range(d)] for i in range(d)]
    R=I
    while e:
        if e&1: R=mat_mul(R,A)
        A=mat_mul(A,A); e//=2
    return R

def trace_poly(A):
    t=[0]
    for i in range(len(A)): t=poly_add(t,A[i][i])
    return t

# states 00,01,10,11; append 0 weight 1 or append 1 weight x
T=[
    [[1],[0,1],[0],[0]],
    [[0],[0],[1],[0,1]],
    [[1],[0,1],[0],[0]],
    [[0],[0],[1],[0]],
]

subset_checks=0; criterion_checks=0; coefficient_checks=0; basis_checks=0
for n in range(5,15):
    m=n-1; adj=wheel_adj(n)
    sim=[0]*(n+1); crit=[0]*(n+1)
    for mask in range(1<<n):
        S={v for v in range(n) if mask>>v & 1}
        a=psd_forcing(adj,S); b=criterion(n,S)
        subset_checks += 1; criterion_checks += 1
        if a: sim[len(S)] += 1
        if b: crit[len(S)] += 1
        if a!=b:
            raise AssertionError((n,S,a,b))
    if sim!=crit: raise AssertionError((n,sim,crit))
    # polynomial formula via direct cyclic-avoidance count
    no111=cyclic_no111_counts(m)
    formula=[0]*(n+1)
    # no-hub sets containing 111: (1+x)^m - Q_m
    from math import comb
    for k in range(m+1): formula[k] += comb(m,k)-no111[k]
    # hub + >=2 rim: x((1+x)^m - 1 - mx)
    for r in range(2,m+1): formula[r+1] += comb(m,r)
    coefficient_checks += n+1
    if formula!=sim: raise AssertionError((n,formula,sim))
    # transfer-matrix Q_m check
    tp=trace_poly(mat_pow(T,m))
    tp += [0]*(m+1-len(tp))
    if tp[:m+1]!=no111:
        raise AssertionError((n,tp,no111))
    coefficient_checks += m+1
    # basis count C(n,2)
    z=min(i for i,c in enumerate(sim) if c)
    if z!=3 or sim[3] != n*(n-1)//2:
        raise AssertionError((n,z,sim[3]))
    basis_checks += 2
print(f'VERIFY_OK n_range=5..14 subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} basis_checks={basis_checks} max_order=14')
