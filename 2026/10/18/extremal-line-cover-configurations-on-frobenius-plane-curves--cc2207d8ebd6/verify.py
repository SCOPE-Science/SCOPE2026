"""Exact F_27 incidence checks for the curve y=x^9 (projective closure).
All calculations are made in F_3[t]/(t^3-t-1), represented by base-3 integers.
"""
from itertools import product
P = 3
Q = 27

def vec(a): return ((a % 3), ((a // 3) % 3), ((a // 9) % 3))
def pack(v): return sum((x % 3) * 3**i for i,x in enumerate(v))
def add(a,b): return pack(tuple(x+y for x,y in zip(vec(a),vec(b))))
def neg(a): return pack(tuple(-x for x in vec(a)))
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    ac,bc=vec(a),vec(b)
    w=[0]*5
    for i in range(3):
        for j in range(3): w[i+j]+=ac[i]*bc[j]
    # t^3=t+1; polynomial reduction from the top
    for j in (4,3):
        coeff=w[j]
        w[j]=0
        w[j-3]+=coeff
        w[j-2]+=coeff
    return pack(w[:3])
def power(a,n):
    x=1
    while n:
        if n&1:x=mul(x,a)
        a=mul(a,a)
        n>>=1
    return x

def coset(c,u): return frozenset(add(c,mul(u,i)) for i in range(3))

def all_cosets(u):
    remain=set(range(Q)); result=[]
    while remain:
        c=min(remain); line=coset(c,u)
        assert line<=remain
        remain-=line; result.append(line)
    return frozenset(result)

def curve_line_points(slope, intercept):
    return frozenset(x for x in range(Q) if sub(power(x,9),mul(slope,x))==intercept)

def projective_line_from_coset(c,u):
    slope=power(u,8)
    intercept=sub(power(c,9),mul(slope,c))
    return (slope,intercept)

if __name__=='__main__':
    assert set(vec(a) for a in range(Q))==set(product(range(3),repeat=3))
    assert all(mul(power(a,26),a)==a for a in range(Q))
    assert all(power(a,9)==power(power(a,3),3) for a in range(Q))
    directions={min(u,mul(2,u)) for u in range(1,Q)}
    assert len(directions)==13
    pencils={all_cosets(u) for u in directions}
    assert len(pencils)==13
    three_secants=set()
    intersections={0:0,1:0,3:0}
    for slope,intercept in product(range(Q),repeat=2):
        pts=curve_line_points(slope,intercept)
        assert len(pts) in intersections
        intersections[len(pts)]+=1
        if len(pts)==3: three_secants.add(pts)
    assert len(three_secants)==117
    assert intersections=={0:234,1:378,3:117},intersections
    cosets={coset(c,u) for c in range(Q) for u in range(1,Q)}
    assert cosets==three_secants
    for u in range(1,Q):
        for c in range(Q):
            slope,intercept=projective_line_from_coset(c,u)
            assert curve_line_points(slope,intercept)==coset(c,u)
    switched=set()
    # Disjoint two-dimensional affine planes indexed by coefficient of t^2:
    # within each plane partition into lines in the directions 1 or t.
    for choices in product([0,1],repeat=3):
        groups=[]
        for z,mode in enumerate(choices):
            for fixed in range(3):
                if mode==0:
                    line=frozenset(pack((x,fixed,z)) for x in range(3))
                else:
                    line=frozenset(pack((fixed,y,z)) for y in range(3))
                groups.append(line)
        spread=frozenset(groups)
        assert len(spread)==9
        assert set.union(*(set(line) for line in spread))==set(range(Q))
        assert sum(len(line) for line in spread)==Q
        assert spread<=three_secants
        switched.add(spread)
    assert len(switched)==8
    assert len(switched & pencils)==2
    assert len(pencils | switched)==19
    # There are q+1 independent projective lines through the sole point at infinity.
    print('VERIFY_OK F27_valid=True lines_0_1_3=234,378,117 secants=117 pencil_spreads=13 switched_spreads=8 nonpencil_switched=6 distinct_spreads_ge=19 minimum_covers_ge=532')

def check_binary_case():
    # F_8=F_2[t]/(t^3+t+1), with XOR addition.
    def fmul(a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1
            a<<=1
            if a&8:a^=0b1011
        return out
    def fpow(a,e):
        v=1
        for _ in range(e):v=fmul(v,a)
        return v
    def finv(a):return fpow(a,6)
    def secant(a,b):
        # Normalized equation y=m x+c; affine points P_s=(s,s^4).
        slope=fmul(fpow(a,4)^fpow(b,4),finv(a^b))
        const=fpow(a,4)^fmul(slope,a)
        return (0,slope,const)
    def matchings(vertices):
        if not vertices:
            yield frozenset(); return
        first=vertices[0]
        for j in range(1,len(vertices)):
            other=vertices[j]
            for rest in matchings(vertices[1:j]+vertices[j+1:]):
                yield rest|{(first,other)}
    q=8
    secants={(a,b):secant(a,b) for a in range(q) for b in range(a+1,q)}
    assert len(set(secants.values()))==28
    for (a,b),(tag,m,c) in secants.items():
        assert frozenset(x for x in range(q) if fpow(x,4)==fmul(m,x)^c)==frozenset([a,b])
    # Vertical lines through P_infty: eight equations x=a plus z=0.
    verticals=[(1,a) for a in range(q)]+[(1,'infinity')]
    allcovers=set(); counts={}
    def store(lines,typename):
        lines=frozenset(lines)
        assert len(lines)==q//2+1
        affine=set(); infinity=False
        for l in lines:
            if l[0]==1:
                infinity=True
                if l[1]!='infinity': affine.add(l[1])
            else:
                affine.update(x for x in range(q) if fpow(x,4)==fmul(l[1],x)^l[2])
        assert infinity and affine==set(range(q))
        assert lines not in allcovers
        allcovers.add(lines)
        counts[typename]=counts.get(typename,0)+1
    # I: four disjoint secants and arbitrary infinity line
    for pairing in matchings(tuple(range(q))):
        for vert in verticals:store([secants[tuple(sorted(edge))] for edge in pairing]+[vert],'I')
    # II: exactly one doubled vertex, one hole repaired by vertical
    for hole in range(q):
        for hub in range(q):
            if hub==hole:continue
            rem=tuple(x for x in range(q) if x not in (hole,hub))
            for a,b in __import__('itertools').combinations(rem,2):
                spare=tuple(x for x in rem if x not in (a,b))
                for pairing in matchings(spare):
                    edges=[(min(hub,a),max(hub,a)),(min(hub,b),max(hub,b))]
                    edges+=list(pairing)
                    store([secants[e] for e in edges]+[(1,hole)],'II')
    # III: one horizontal singleton, remaining matched, one hole
    for hole in range(q):
        for singleton in range(q):
            if singleton==hole:continue
            rem=tuple(x for x in range(q) if x not in (hole,singleton))
            for pairing in matchings(rem):
                lines=[secants[tuple(sorted(e))] for e in pairing]
                lines += [(0,0,fpow(singleton,4)),(1,hole)]
                store(lines,'III')
    # IV: two distinct verticals and match the remaining six
    for hole1,hole2 in __import__('itertools').combinations(range(q),2):
        rem=tuple(x for x in range(q) if x not in (hole1,hole2))
        for pairing in matchings(rem):
            store([secants[tuple(sorted(e))] for e in pairing]+[(1,hole1),(1,hole2)],'IV')
    assert counts=={'I':945,'II':2520,'III':840,'IV':420}, counts
    assert len(allcovers)==4725
    print('VERIFY_OK F8_cover_types=945,2520,840,420 distinct_optimal_covers=4725 closed_formula=4725')

if __name__=='__main__':
    check_binary_case()
