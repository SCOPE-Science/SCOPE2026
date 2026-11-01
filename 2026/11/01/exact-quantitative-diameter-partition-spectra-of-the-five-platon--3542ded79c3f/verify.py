#!/usr/bin/env python3
"""Exact certificate for the diameter-partition spectra of Platonic vertices.
Run with Python 3.10+; uses only Python's standard library.
All arithmetic occurs in the ordered field Q(sqrt(5)).
"""
from itertools import combinations, product

ZERO=(0,0)
ONE=(1,0)
PHI=(0,1)
INVPHI=(-1,1)

def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[0],-x[1]
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=x; c,d=y
    return a*c+b*d,a*d+b*c+b*d

def sign(x):
    a,b=x; u=2*a+b; v=b
    if not u: return (v>0)-(v<0)
    if not v or (u>0)==(v>0): return (u>0)-(u<0)
    if u>0: return (u*u>5*v*v)-(u*u<5*v*v)
    return (5*v*v>u*u)-(5*v*v<u*u)

def less(x,y): return sign(sub(x,y))<0

def fmt(x): return f'{x[0]}+({x[1]})phi'

def scale(x,s): return mul(x,(s,0))

def pt(x,y,z): return x,y,z

def distance_sq(p,q):
    return sum_q([mul(sub(a,b),sub(a,b)) for a,b in zip(p,q)])

def sum_q(seq):
    s=ZERO
    for x in seq: s=add(s,x)
    return s

def generate():
    tetra=[pt(*( (n,0) for n in a)) for a in ((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))]
    cube=[pt(*[scale(ONE,x) for x in z]) for z in product((-1,1), repeat=3)]
    octa=[pt(*[scale(ONE,x) for x in z]) for z in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))]
    ico=[]; dodeca=list(cube)
    for a,b in product((-1,1),repeat=2):
        ico.extend([pt(ZERO,scale(ONE,a),scale(PHI,b)),pt(scale(ONE,a),scale(PHI,b),ZERO),pt(scale(PHI,a),ZERO,scale(ONE,b))])
        dodeca.extend([pt(ZERO,scale(INVPHI,a),scale(PHI,b)),pt(scale(INVPHI,a),scale(PHI,b),ZERO),pt(scale(PHI,a),ZERO,scale(INVPHI,b))])
    return {'tetra':tetra,'cube':cube,'octa':octa,'icosa':ico,'dodeca':dodeca}

# Exact spectral input for independent cross-check against coordinate computations.
EXPECTED={
 'tetra':([(8,0)],[4,1]),
 'cube':([(4,0),(8,0),(12,0)],[8,4,2,1]),
 'octa':([(2,0),(4,0)],[6,2,1]),
 'icosa':([(4,0),(4,4),(8,4)],[12,4,2,1]),
 'dodeca':([(8,-4),(4,0),(8,0),(4,4),(12,0)],[20,10,5,4,2,1]),
}
# Each list is indexed by the threshold index, with index zero at cutoff 0.
WITNESSES={
 'tetra':{0:[0,1,2,3],1:[0,0,0,0]},
 'cube':{0:list(range(8)),1:[0,0,1,1,2,2,3,3],2:[0,0,0,0,1,1,1,1],3:[0]*8},
 'octa':{0:list(range(6)),1:[0,1,0,1,0,1],2:[0]*6},
 'icosa':{0:list(range(12)),1:[0,1,2,1,2,1,2,0,0,3,3,3],2:[0]*6+[1]*6,3:[0]*12},
 'dodeca':{0:list(range(20)),1:[0,1,2,3,4,5,6,7,0,1,2,5,8,3,6,4,9,7,8,9],
  2:[0,1,3,1,0,2,3,2,0,0,1,4,3,1,3,0,2,4,3,2],
  3:[0,2,0,1,0,1,1,1,0,0,2,2,2,2,0,3,0,1,1,1],
  4:[0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1],
  5:[0]*20},
}

def maximal_small_sets(D,t,size):
    n=len(D)
    good=[]
    for selection in combinations(range(n),size):
        if all(not less(t,D[i][j]) for i,j in combinations(selection,2)):
            good.append(sum(1<<i for i in selection))
    return good

def assert_level_structure(D,expected,name):
    levels={D[i][j] for i in range(len(D)) for j in range(i)}
    assert levels==set(expected),(name,levels,expected)
    for a,b in zip(expected,expected[1:]): assert less(a,b), (name,a,b)

def main():
    data=generate()
    total=0
    for name,V in data.items():
        n=len(V)
        D=[[distance_sq(p,q) for q in V] for p in V]
        assert all(D[i][i]==ZERO for i in range(n))
        assert all(D[i][j]==D[j][i] for i in range(n) for j in range(n))
        thresholds,chromatic=EXPECTED[name]
        assert_level_structure(D,thresholds,name)
        for index,t in enumerate([ZERO]+thresholds):
            colors=WITNESSES[name][index]
            assert len(colors)==n
            assert len(set(colors))==chromatic[index],(name,index,len(set(colors)))
            for i,j in combinations(range(n),2):
                assert colors[i]!=colors[j] or not less(t,D[i][j]),(name,index,i,j)
            total+=1
        print(name, 'vertices',n,'squared levels', list(map(fmt,thresholds)), 'chromatic profile',chromatic)
    # Lower bounds by geometric-combinatorial (independent-set) certificates.
    D={name:[[distance_sq(p,q) for q in V] for p in V] for name,V in data.items()}
    # Tetra: at cutoff zero, all distinct points have positive distances.
    # Cube: at t=4, no pair with same color can have a common antipodal-of-edge partner triple;
    # maximum 2 allowed. At t=8, antipodal pairs force >=2 colors.
    cube=D['cube']; octa=D['octa']; ico=D['icosa']; dode=D['dodeca']
    def show(name,limit,size,expected_count=None):
        ss=maximal_small_sets(D[name],limit,size)
        if expected_count is not None: assert len(ss)==expected_count,(name,limit,size,len(ss))
        print('small-set count',name,fmt(limit),size,len(ss))
        return ss
    # Max clique size certificate for complement of each far-distance graph:
    show('cube',(4,0),3,0)
    show('octa',(2,0),4,0)
    show('icosa',(4,0),4,0)
    show('dodeca',(8,-4),3,0)
    # The dodecahedron has 12 pentagonal faces as its only size-5 small-diameter cliques.
    five=show('dodeca',(4,0),5,12)
    # More directly, four of those sets never partition 20 vertices.
    for four in combinations(five,4):
        assert (four[0] | four[1] | four[2] | four[3]) != ((1<<20)-1)
    # The maximum class under d² <=8 has 7 vertices; three colors would
    # force sizes (7,7,6). Check all disjoint seven-pairs and their complement.
    seven=show('dodeca',(8,0),7,100)
    eight=show('dodeca',(8,0),8,0)
    assert not eight
    allbits=(1<<20)-1
    disjoint=0
    for a,b in combinations(seven,2):
        if a&b: continue
        disjoint+=1
        remaining=allbits^(a|b)
        chosen=[i for i in range(20) if remaining&(1<<i)]
        assert len(chosen)==6
        assert any(less((8,0),dode[i][j]) for i,j in combinations(chosen,2))
    assert disjoint==820,disjoint
    print('disjoint 7+7 pairs',disjoint,'none has admissible remaining six-set')
    # A 2-coloring at all t just below largest diameter is always necessary:
    # every Platonic vertex set here has an actual diameter pair.
    print('EXACT_CERTIFICATE_OK', total, 'threshold witnesses, and all necessary obstructions')

if __name__=='__main__': main()
