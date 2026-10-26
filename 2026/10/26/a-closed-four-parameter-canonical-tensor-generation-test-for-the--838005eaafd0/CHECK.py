"""Exact finite sanity checks for a four-parameter toric criterion.

This program checks symbolic wall relations after numerical parameter substitution,
and finite representative tests. The proof for all integers is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations, product

TRI = [tuple(int(x) - 1 for x in s) for s in (
    '124', '234', '345', '456', '146', '167', '127', '237', '358', '568', '378', '678')]

def rays(a,b,c,d):
    return [(1,1,b),(1,0,0),(0,-1,0),(0,0,-1),
            (-1,a,d),(0,1,0),(0,0,1),(-1,c,d+1)]

def E(u,v,w,z):
    return (v+abs(u)>0 and z+abs(w)>0
            and (u*w>=0 or v*abs(w)+z*abs(u)>0))

def four_ray_checks(a,b,c,d):
    return (E(d,a+2,d+1,c+2), E(a,d+2,a+1,b+d+2),
            E(b+d,1-a,b+d+1,1-c), E(c,1-d,c+1,1-b-d))

def degree_table(a,b,c,d):
    return {'12':2,'14':1-b,'16':2,'17':b+1,
            '23':2,'24':b+1,'27':1-b,'34':a+d+2,
            '35':c-a+1,'37':c-d+1,'38':a-c+1,
            '45':2,'46':b+d-a+1,'56':a-c+1,
            '58':2,'67':-b-c-d,'68':c-a+1,'78':2}

def exact_wall_degrees(a,b,c,d):
    v=rays(a,b,c,d)
    edges=sorted(set(tuple(sorted(e)) for t in TRI for e in combinations(t,2)))
    assert len(edges)==18
    actual={}
    for i,j in edges:
        opp=[next(iter(set(t)-{i,j})) for t in TRI if i in t and j in t]
        assert len(opp)==2 and len(set(opp))==2
        rhs=tuple(v[opp[0]][k]+v[opp[1]][k] for k in range(3))
        solved=None
        for r,s in combinations(range(3),2):
            det=v[i][r]*v[j][s]-v[i][s]*v[j][r]
            if not det:continue
            alpha=Fraction(rhs[r]*v[j][s]-rhs[s]*v[j][r],det)
            beta=Fraction(v[i][r]*rhs[s]-v[i][s]*rhs[r],det)
            if all(alpha*v[i][k]+beta*v[j][k]==rhs[k] for k in range(3)):
                solved=2-alpha-beta
                break
        assert solved is not None
        actual[f'{i+1}{j+1}']=solved
    return actual

def is_in_convex_hull(point, neigh):
    # Caratheodory: in affine 3-space, at most four vertices needed.
    # Deterministically solve feasible affine systems by rational elimination.
    for k in range(1,min(4,len(neigh))+1):
        for support in combinations(neigh,k):
            matrix=[[Fraction(v[h]) for v in support]+[Fraction(point[h])] for h in range(3)]
            matrix.append([Fraction(1)]*k+[Fraction(1)])
            rank=0; pivots=[]
            for col in range(k):
                pivot=next((row for row in range(rank,4) if matrix[row][col]),None)
                if pivot is None:continue
                matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
                den=matrix[rank][col]
                matrix[rank]=[x/den for x in matrix[rank]]
                for row in range(4):
                    if row!=rank:
                        factor=matrix[row][col]
                        matrix[row]=[x-factor*y for x,y in zip(matrix[row],matrix[rank])]
                pivots.append(col);rank+=1
            if any(all(matrix[r][col]==0 for col in range(k)) and matrix[r][-1] for r in range(4)):
                continue
            if rank==k:
                coeff=[Fraction(0)]*k
                for row,col in enumerate(pivots):coeff[col]=matrix[row][-1]
                if all(x>=0 for x in coeff):return True
    return False

def exact_vertex_checks(a,b,c,d):
    vv=rays(a,b,c,d)
    ans=[]
    for i in range(8):
        ne=sorted({j for t in TRI if i in t for j in t if j!=i})
        ans.append(not is_in_convex_hull(vv[i],[vv[j] for j in ne]))
    return tuple(ans)

assert set(degree_table(0,0,0,0))==set(exact_wall_degrees(0,0,0,0))
for a,b,c,d in product(range(-2,3),repeat=4):
    assert exact_wall_degrees(a,b,c,d)==degree_table(a,b,c,d)
    predicate=four_ray_checks(a,b,c,d)
    vertices=exact_vertex_checks(a,b,c,d)
    assert vertices[:2]==(True,True) and vertices[4]==vertices[7]==True
    assert tuple(vertices[i] for i in (2,3,5,6))==predicate,(a,b,c,d,vertices,predicate)
for m in range(2,25):
    a,b,c,d=0,m,m,0
    assert all(four_ray_checks(a,b,c,d))
    vals=degree_table(a,b,c,d).values()
    assert all(vals) and max(abs(x) for x in vals)==2*m
print('VERIFY_OK: 625 exact four-parameter ray/edge tests; 23 family cases')
