from itertools import combinations
from collections import Counter
from math import comb

vertices=tuple(range(6))
left={0,1,2}
right={3,4,5}
edges={tuple(sorted((i,j))) for i in left for j in right}

# Stanley-Reisner graph data.
assert len(vertices)==6
assert len(edges)==9
assert all((u in left and v in right) or (u in right and v in left) for u,v in edges)

def induced(W):
    W=set(W)
    E=[e for e in edges if e[0] in W and e[1] in W]
    return W,E

def components(W,E):
    if not W:
        return 0
    adj={v:set() for v in W}
    for u,v in E:
        adj[u].add(v); adj[v].add(u)
    seen=set(); c=0
    for v in W:
        if v in seen:
            continue
        c+=1; stack=[v]; seen.add(v)
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
    return c

# Hochster formula for a one-dimensional simplicial complex.
betti=Counter({(0,0):1})
for j in range(1,7):
    for W0 in combinations(vertices,j):
        W,E=induced(W0)
        c=components(W,E)
        h0=c-1
        h1=len(E)-len(W)+c
        if h0:
            betti[(j-1,j)] += h0
        if h1:
            betti[(j-2,j)] += h1
expected={(0,0):1,(1,2):6,(2,3):4,(2,4):9,(3,5):12,(4,6):4}
assert dict(betti)==expected, (betti,expected)

# Polynomial helpers, low degree first.
def add(p,q):
    n=max(len(p),len(q)); out=[0]*n
    for i in range(n):
        out[i]=(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    while len(out)>1 and out[-1]==0: out.pop()
    return out

numer=[1]
for (i,j),b in expected.items():
    if i==0 and j==0: continue
    term=[0]*j+[((-1)**i)*b]
    numer=add(numer,term)
rhs=mul([1,4,4], [1,-4,6,-4,1])
assert numer==rhs
assert numer==[1,0,-6,4,9,-12,4]

# Standard monomial count. A monomial survives iff at most one left variable
# and at most one right variable has positive exponent.
def hilbert_by_support(n):
    if n==0: return 1
    # support only in one part: 3+3 choices, one monomial each for degree n.
    one_part=6
    # support on one left and one right variable: 9 choices and n-1 positive splits.
    two_part=9*max(0,n-1)
    return one_part+two_part

def hilbert_formula(n):
    # coefficient of (1+4t+4t^2)/(1-t)^2
    ans=n+1
    if n>=1: ans += 4*n
    if n>=2: ans += 4*(n-1)
    return ans
for n in range(13):
    assert hilbert_by_support(n)==hilbert_formula(n)
for n in range(2,13):
    assert hilbert_formula(n)==9*n-3

multiplicity=1+4+4
assert multiplicity==9
arith_genus=1-(-3)
assert arith_genus==4

# Singular-stratum combinatorics: each of six coordinate vertices lies on
# exactly three of the nine projective lines.
deg={v:0 for v in vertices}
for u,v in edges:
    deg[u]+=1; deg[v]+=1
assert set(deg.values())=={3}

print('hochster_betti='+','.join(f'beta_{i}_{j}={expected[(i,j)]}' for i,j in sorted(expected)))
print('hilbert_numerator=1-6t^2+4t^3+9t^4-12t^5+4t^6')
print('hilbert_series=(1+4t+4t^2)/(1-t)^2')
print('multiplicity=9')
print('projective_degree=9')
print('arithmetic_genus=4')
print('K3,3_vertices=6')
print('K3,3_edges=9')
print('triple_points=6')
print('VERIFY_OK')
