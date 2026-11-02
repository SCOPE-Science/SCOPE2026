"""Exact GF(4) certificate for the plane-scheme orbit/incidence theorem.

Run with Python 3 (standard library only).  The finite completeness argument
uses the unique reduced-row-echelon representative of every three-subspace
of the six-dimensional vector space over GF(4).
"""
from collections import Counter, deque
from itertools import combinations, product

# GF(4)=GF(2)[t]/(t^2+t+1); integers 0,1,2,3 denote 0,1,t,t+1.
MUL=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
SQUARE=(0,1,3,2)
INV=(0,1,3,2)

def rref(rows):
    a=[list(r) for r in rows];k=0
    for j in range(6):
        i=next((i for i in range(k,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[k]=a[k],a[i]
        a[k]=[MUL[INV[a[k][j]]][z] for z in a[k]]
        for i in range(len(a)):
            if i==k:continue
            u=a[i][j]
            if u:a[i]=[z^MUL[u][w] for z,w in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return tuple(map(tuple,a))

def isotropic(a):
    # Coefficient of t_i^3 equals the parity of nonzero entries in row i.
    # Coefficient of t_i^2*t_j is sum_a (row_i,a)^2 * row_j,a.
    for i in range(3):
        if sum(z!=0 for z in a[i])%2:return False
        for j in range(i):
            s=0
            for u,v in zip(a[i],a[j]):s^=MUL[SQUARE[u]][v]
            if s:return False
    return True

def enumerate_planes():
    out=[];total=0
    for piv in combinations(range(6),3):
        free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,6) if j not in piv]
        for tup in product(range(4),repeat=len(free)):
            total+=1
            rows=[[0]*6 for _ in range(3)]
            for i,p in enumerate(piv):rows[i][p]=1
            for (i,j),u in zip(free,tup):rows[i][j]=u
            if isotropic(rows):out.append(tuple(map(tuple,rows)))
    assert total==376805, total
    assert len(out)==891, len(out)
    assert len(set(out))==len(out)
    return out

def points(a):
    pts=set()
    for s,t,u in product(range(4),repeat=3):
        if not (s or t or u):continue
        v=tuple(MUL[s][a[0][j]]^MUL[t][a[1][j]]^MUL[u][a[2][j]] for j in range(6))
        scalar=INV[next(x for x in v if x)]
        pts.add(tuple(MUL[scalar][x] for x in v))
    assert len(pts)==21
    return pts

def weights(a):return tuple(sorted(Counter(sum(x!=0 for x in p) for p in points(a)).items()))

def permute(a,i):
    rows=[]
    for r in a:
        z=list(r);z[i],z[i+1]=z[i+1],z[i];rows.append(z)
    return rref(rows)

def scale(a):
    return rref([[MUL[2][r[0]],*r[1:]] for r in a])

def orbit(rep,universe):
    seen={rep};Q=deque([rep])
    while Q:
        a=Q.popleft()
        for b in [scale(a),*(permute(a,i) for i in range(5))]:
            assert b in universe
            if b not in seen:seen.add(b);Q.append(b)
    return seen

def rank(rows):
    a=[list(r) for r in rows];k=0
    for j in range(6):
        i=next((i for i in range(k,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[k]=a[k],a[i]
        a[k]=[MUL[INV[a[k][j]]][v] for v in a[k]]
        for i in range(k+1,len(a)):
            u=a[i][j]
            if u:a[i]=[x^MUL[u][y] for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

def intersection_counts(a,others):
    return dict(sorted(Counter(6-rank(a+b) for b in others).items()))

def run():
    all_planes=enumerate_planes(); universe=set(all_planes)
    print('RREF_SUBSPACES=376805; FERMAT_PLANES=891')
    oldrep=((1,0,0,0,0,1),(0,1,0,0,1,0),(0,0,1,1,0,0))
    newrep=((1,0,0,1,1,1),(0,1,0,1,2,3),(0,0,1,1,3,2))
    assert oldrep in universe and newrep in universe
    old=orbit(oldrep,universe);new=orbit(newrep,universe)
    assert len(old)==405 and len(new)==486 and old.isdisjoint(new) and old|new==universe
    print('MONOMIAL_ORBITS=(405,486); STABILIZER_ORDERS=(432,360)')
    expected_old=((2,3),(4,9),(6,9)); expected_new=((4,15),(6,6))
    assert all(weights(a)==expected_old for a in old)
    assert all(weights(a)==expected_new for a in new)
    print('PLANE_WEIGHT_PROFILES=',expected_old,expected_new)
    fixed={a for a in universe if all(z in (0,1) for r in a for z in r)}
    assert len(fixed)==15 and fixed<=old
    print('FROBENIUS_ORBITS=15 fixed and 438 pairs, all fixed in the 405 orbit')
    print('ORBIT_REPRESENTATIVE_INCIDENCE=dimension of vector intersection (0,1,2,3)')
    expected=[{0:224,1:156,2:24,3:1},{0:288,1:180,2:18},
              {0:240,1:150,2:15},{0:272,1:186,2:27,3:1}]
    actual=[intersection_counts(oldrep,old),intersection_counts(oldrep,new),
            intersection_counts(newrep,old),intersection_counts(newrep,new)]
    assert actual==expected,(actual,expected)
    for label,v in zip(('old/old','old/new','new/old','new/new'),actual):print(label, v)
    print('VERIFY_OK')

if __name__=='__main__':run()
