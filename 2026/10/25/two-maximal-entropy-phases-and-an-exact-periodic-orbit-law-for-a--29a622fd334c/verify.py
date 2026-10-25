#!/usr/bin/env python3
"""Exact finite-state checks for the antisquare-good shift theorem."""
from itertools import product

FORBIDDEN = ('0011','1100','0110','1001','010101','101010','001011','110100')
K = 5
V = [''.join(a) for a in product('01', repeat=K)
     if all(f not in ''.join(a) for f in FORBIDDEN)]
assert len(V) == 20
E = {v: [v[1:]+b for b in '01'
         if all(f not in v+b for f in FORBIDDEN)] for v in V}
assert all(w in V for vs in E.values() for w in vs)


def reach(v):
    seen={v}; stack=[v]
    while stack:
        for w in E[stack.pop()]:
            if w not in seen:
                seen.add(w);stack.append(w)
    return seen
R={v:reach(v) for v in V}
components=[];remaining=set(V)
while remaining:
    v=min(remaining)
    c={w for w in V if w in R[v] and v in R[w]}
    components.append(sorted(c));remaining-=c
assert len(components)==2 and all(len(c)==10 for c in components)
C0=next(c for c in components if '00000' in c)
C1=next(c for c in components if '11111' in c)
assert set(C1)==set(''.join('1' if t=='0' else '0' for t in w) for w in C0)
assert all(set(E[v]).issubset(c) for c in components for v in c)
assert all(sum(len(E[v]) for v in c)==14 for c in components)
assert '00000' in E['00000'] and '11111' in E['11111']


def multiply(a,b):
    n=len(a);m=len(b[0]);d=len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(d)) for j in range(m)] for i in range(n)]

def charpoly(a):
    """Faddeev-LeVerrier: monic characteristic polynomial, integer exact."""
    n=len(a); B=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    for k in range(1,n+1):
        T=multiply(a,B);tr=sum(T[i][i] for i in range(n))
        assert tr%k==0
        c=-tr//k
        coeff.append(c)
        B=[[T[i][j]+c*(i==j) for j in range(n)] for i in range(n)]
    return coeff

def poly_mul(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans

# Coefficients descending in x.
for C in components:
    A=[[int(v in E[u]) for v in C] for u in C]
    expected=poly_mul(poly_mul([1,0,0,0,0],[1,0,0,1]),[1,-1,0,-1])
    assert charpoly(A)==expected, (C, charpoly(A))

# Exact polynomial identity in the variable y: degree at most ten.
# Test at eleven integers, determining the characteristic polynomial identically.
for y in range(11):
    A=[[int(v in E[u])*(y if v[-1]=='1' else 1) for v in C0] for u in C0]
    expected=poly_mul(poly_mul([1,0,0,0,0],[1,0,0,y]),[1,-1,0,-y])
    assert charpoly(A)==expected, y

# Traces of powers are exact counts of cyclic points in the edge presentation.
A=[[int(v in E[u]) for v in V] for u in V]
P=[[int(i==j) for j in range(len(V))] for i in range(len(V))]
def avoids_cyclic_F(w):
    t=w*((6//len(w))+2)
    return all(f not in t[i:i+len(f)] for f in FORBIDDEN for i in range(len(w)))
def good_cyclic(w):
    # In a period-n word, an antisquare of any order >=n forces one
    # of order in [n,2n-1] by reducing its shift modulo n.
    n=len(w); t=w*(6+2*n//n)
    return not any(all(t[i+j]!=t[i+j+k] for j in range(k))
                   for k in range(2,2*n) for i in range(n))
counts=[]
for n in range(1,15):
    P=multiply(P,A)
    count=sum(P[i][i] for i in range(len(V)))
    brute_F=brute_good=0
    for a in product('01',repeat=n):
        w=''.join(a)
        f=avoids_cyclic_F(w);g=good_cyclic(w)
        assert f==g,(n,w)
        brute_F+=f;brute_good+=g
    assert count==brute_F==brute_good,(n,count,brute_F,brute_good)
    counts.append(count)
# Newton sums for lambda^3-lambda^2-1 with roots r_i,
# plus the root sum of x^3+1.
s=[3,1,1]
for n in range(3,15):s.append(s[n-1]+s[n-3])
assert counts==[2*(s[n]+(3*(-1)**(n//3) if n%3==0 else 0)) for n in range(1,15)]
print('ANTISQUARE_GOOD_ZETA_PASS', 'states=20', 'components=10+10', 'edges=28',
      'weighted_interpolation=11', 'periods=1..14', 'counts='+','.join(map(str,counts)))
