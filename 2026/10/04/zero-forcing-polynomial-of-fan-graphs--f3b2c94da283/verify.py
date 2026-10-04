from itertools import product

def fan(m):
    # vertices 0=center, 1..m are path vertices
    n = m + 1
    adj = [set() for _ in range(n)]
    for v in range(1, m+1):
        adj[0].add(v)
        adj[v].add(0)
    for v in range(1, m):
        adj[v].add(v+1)
        adj[v+1].add(v)
    return adj

def is_zero_forcing(adj, mask):
    n = len(adj)
    blue = mask
    full = (1 << n) - 1
    while True:
        changed = False
        for u in range(n):
            if not ((blue >> u) & 1):
                continue
            white = [v for v in adj[u] if not ((blue >> v) & 1)]
            if len(white) == 1:
                blue |= 1 << white[0]
                changed = True
                break
        if not changed:
            break
    return blue == full

def path_zero_forcing_condition(m, mask_on_path):
    # A set of P_m is zero forcing iff it contains an endpoint or
    # a pair of consecutive path vertices.
    if mask_on_path & 1:
        return True
    if mask_on_path & (1 << (m-1)):
        return True
    return any(((mask_on_path >> i) & 3) == 3 for i in range(m-1))

def fan_structural_condition(m, mask):
    center = mask & 1
    pathmask = mask >> 1
    if center:
        return path_zero_forcing_condition(m, pathmask)

    # With the center white, no path vertex can force another path
    # vertex initially. The first force must be the center. This
    # occurs exactly from an endpoint whose path-neighbor is blue,
    # or an internal path vertex whose two path-neighbors are blue.
    if m >= 2:
        if (pathmask & 3) == 3:
            return True
        if ((pathmask >> (m-2)) & 3) == 3:
            return True
    for i in range(m-2):
        if ((pathmask >> i) & 7) == 7:
            return True
    return False

def add(a,b):
    n=max(len(a),len(b))
    c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def shift(a,k):
    return [0]*k + a[:]

def binomial_poly(n):
    from math import comb
    return [comb(n,i) for i in range(n+1)]

def independent_path_poly(t):
    # I(P_t;x), with P_0 empty
    if t == 0:
        return [1]
    if t == 1:
        return [1,1]
    a=[1]
    b=[1,1]
    for _ in range(2,t+1):
        a,b=b,add(b,shift(a,1))
    return b

def boundary_tribonacci_poly(m):
    # binary strings of length m with no 111 and neither endpoint
    # pair equal to 11
    if m == 0:
        return [1]
    if m == 1:
        return [1,1]
    if m == 2:
        return [1,2]
    if m == 3:
        return [1,3,1]
    if m == 4:
        return [1,4,4]
    b2,b3,b4=[1,2],[1,3,1],[1,4,4]
    for r in range(5,m+1):
        br=add(add(b4,shift(b3,1)),shift(b2,2))
        b2,b3,b4=b3,b4,br
    return b4

def sub(a,b):
    n=max(len(a),len(b))
    c=[0]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]-=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c


def no111_poly(m):
    if m == 0: return [1]
    if m == 1: return [1,1]
    if m == 2: return [1,2,1]
    q0,q1,q2=[1],[1,1],[1,2,1]
    for r in range(3,m+1):
        qr=add(add(q2,shift(q1,1)),shift(q0,2))
        q0,q1,q2=q1,q2,qr
    return q2

def boundary_inclusion_poly(m):
    q=no111_poly(m)
    if m < 6:
        return boundary_tribonacci_poly(m)
    return add(sub(q, [0,0]+[2*x for x in no111_poly(m-3)]), [0,0,0,0]+no111_poly(m-6))

def predicted_poly(m):
    # Z(F_m;x) = (1+x)^(m+1) - x I(P_{m-2};x) - B_m(x)
    out=binomial_poly(m+1)
    out=sub(out,shift(independent_path_poly(m-2),1))
    out=sub(out,boundary_tribonacci_poly(m))
    return out

graphs=subsets=forcing_sets=0
for m in range(2,18):
    adj=fan(m)
    n=m+1
    coeff=[0]*(n+1)
    for mask in range(1<<n):
        subsets += 1
        actual=is_zero_forcing(adj,mask)
        structural=fan_structural_condition(m,mask)
        assert actual == structural, (m,mask,actual,structural)
        if actual:
            forcing_sets += 1
            coeff[mask.bit_count()] += 1
    while len(coeff)>1 and coeff[-1]==0:
        coeff.pop()
    assert boundary_tribonacci_poly(m) == boundary_inclusion_poly(m), (m,boundary_tribonacci_poly(m),boundary_inclusion_poly(m))
    pred=predicted_poly(m)
    assert coeff == pred, (m,coeff,pred)

    minimum=next(i for i,c in enumerate(coeff) if c)
    assert minimum == 2, (m,minimum)
    if m == 2:
        assert coeff[2] == 3
    else:
        assert coeff[2] == 4, (m,coeff[2])
    graphs += 1

print("VERIFY_OK")
print("fan_graphs_checked =", graphs)
print("vertex_subsets_checked =", subsets)
print("zero_forcing_sets_checked =", forcing_sets)
print("path_sizes m = 2..17")
print("all direct zero-forcing tests matched the structural classification")
print("all polynomial coefficients matched the recurrence and inclusion-exclusion formulas")
print("all zero-forcing numbers equal 2")
print("minimum-set counts are 3 for m=2 and 4 for every m>=3")
