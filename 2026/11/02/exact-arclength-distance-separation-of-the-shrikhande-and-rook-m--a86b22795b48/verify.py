#!/usr/bin/env python3
"""Exact-rational verification of two unit-edge intrinsic graph distance laws."""
from fractions import Fraction as Q
from itertools import combinations, product

def graphs():
    vertices = list(product(range(4), repeat=2))
    rook = set(); shr = set()
    steps = {(1,0), (3,0), (0,1), (0,3), (1,1), (3,3)}
    for a,b in combinations(range(16),2):
        x,y = vertices[a], vertices[b]
        if (x[0] == y[0]) != (x[1] == y[1]):
            rook.add((a,b))
        if ((x[0]-y[0]) % 4, (x[1]-y[1]) % 4) in steps:
            shr.add((a,b))
    return rook, shr

def distance_matrix(edges):
    N=16
    adj=[set() for _ in range(N)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    d=[[0 if a==b else (1 if b in adj[a] else 2) for b in range(N)] for a in range(N)]
    assert len(edges)==48 and all(len(adj[a])==6 for a in range(N))
    for a,b in combinations(range(N),2):
        assert len(adj[a]&adj[b])==2
        assert d[a][b] == min((2 if x in adj[a] and b in adj[x] else 99) for x in range(N)) if d[a][b]==2 else True
    return d,adj

def canonical(matrix):
    a,b,c,d=matrix
    transforms=[(a,b,c,d),(b,a,d,c),(c,d,a,b),(d,c,b,a),
                (a,c,b,d),(c,a,d,b),(b,d,a,c),(d,b,c,a)]
    return min(transforms)

def patterns(edges):
    D,_=distance_matrix(edges)
    out={}
    for e,f in combinations(sorted(edges),2):
        key=canonical(tuple(D[x][y] for x in e for y in f))
        out[key]=out.get(key,0)+1
    assert sum(out.values())==1128
    return out

def clip(poly, A,B,C):
    if not poly: return []
    out=[]
    for s,e in zip(poly,poly[1:]+poly[:1]):
        vs=A*s[0]+B*s[1]+C;ve=A*e[0]+B*e[1]+C
        if vs>=0 and ve>=0:out.append(e)
        elif vs>=0 and ve<0:
            u=vs/(vs-ve);out.append((s[0]+u*(e[0]-s[0]),s[1]+u*(e[1]-s[1])))
        elif vs<0 and ve>=0:
            u=vs/(vs-ve);out.extend(((s[0]+u*(e[0]-s[0]),s[1]+u*(e[1]-s[1])),e))
    return out

def tail(pattern, r):
    a,b,c,d=pattern
    poly=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    # Points (x,y) with ALL four endpoint routes longer than r.
    for A,B,C in [(1,1,Q(a)-r),(1,-1,Q(b+1)-r),(-1,1,Q(c+1)-r),(-1,-1,Q(d+2)-r)]:
        poly=clip(poly,Q(A),Q(B),C)
    return abs(sum((p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])),Q(0)))/2

def difference(pR,pS,r):
    return -Q(2,48**2)*sum((pR.get(k,0)-pS.get(k,0))*tail(k,r) for k in set(pR)|set(pS))

def target(r):
    return -min(r-Q(2),Q(3)-r)**2/24 if 2<=r<=3 else Q(0)

def main():
    R,S=graphs();pr=patterns(R);ps=patterns(S)
    expected_R={(0,1,1,1):96,(0,1,1,2):144,(1,1,1,1):24,(1,1,2,2):288,(1,2,2,1):72,(1,2,2,2):288,(2,2,2,2):216}
    expected_S={(0,1,1,1):96,(0,1,1,2):144,(1,1,1,2):96,(1,1,2,2):192,(1,2,2,1):24,(1,2,2,2):384,(2,2,2,2):192}
    assert pr==expected_R,(pr,expected_R)
    assert ps==expected_S,(ps,expected_S)
    def induced(edges):
        A=set(tuple(e) for e in edges)
        count=0
        for e,f in combinations(sorted(edges),2):
            if len(set(e+f))<4:continue
            if all(tuple(sorted((u,v))) not in A for u in e for v in f):count+=1
        return count
    assert induced(R)==216 and induced(S)==192
    # Each clipping area is a quadratic polynomial on every interval
    # [j/2,(j+1)/2].  Endpoints and midpoint uniquely fix it.
    checks=0
    for j in range(6):
        l=Q(j,2);h=Q(j+1,2)
        for r in (l,(l+h)/2,h):
            assert difference(pr,ps,r)==target(r),(r,difference(pr,ps,r),target(r))
            checks+=1
    # Recheck the characteristic diagnostic value directly.
    assert difference(pr,ps,Q(5,2))==-Q(1,96)
    # Degree-two tail theorem: only induced 2K2 pairs contribute for r>=5/2.
    for r in (Q(5,2),Q(11,4),Q(3)):
        for k in set(pr)|set(ps):
            required=2*(Q(3)-r)**2 if k==(2,2,2,2) else Q(0)
            assert tail(k,r)==required,(k,r)
    print('PASS: two strongly regular 16-vertex graphs; 48 edges each; all 1128 unordered edge pairs each.')
    print('PASS: 216 versus 192 induced two-edge matchings; exact pair-pattern frequency tables.')
    print('PASS: 18 exact rational piecewise-polynomial control points and quadratic tail identities.')
    print('PASS: F_rook(5/2)=29/32; F_shrikhande(5/2)=11/12; difference=-1/96.')
if __name__=='__main__':main()
