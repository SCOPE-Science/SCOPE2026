from fractions import Fraction
from itertools import combinations, product
from collections import Counter, defaultdict

# Example 1.2 valuations from Cueto--Markwig, arXiv:2004.10891.
VAL = {
(0,0):0,(1,0):10,(0,1):8,(2,0):29,(1,1):15,(0,2):28,
(3,0):50,(2,1):29,(1,2):28,(0,3):50,(4,0):77,(3,1):51,
(2,2):32,(1,3):51,(0,4):74,
}
PTS=sorted(VAL)

def det2(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def lower_triangulation():
    facets=[]
    for tri in combinations(PTS,3):
        if det2(*tri)==0: continue
        (x1,y1),(x2,y2),(x3,y3)=tri
        z1,z2,z3=[VAL[p] for p in tri]
        D=Fraction(det2(*tri))
        # Solve z = a*x+b*y+c by Cramer's rule via differences.
        a=Fraction((z2-z1)*(y3-y1)-(z3-z1)*(y2-y1), det2(tri[0],tri[1],tri[2]))
        b=Fraction((x2-x1)*(z3-z1)-(x3-x1)*(z2-z1), det2(tri[0],tri[1],tri[2]))
        c=Fraction(z1)-a*x1-b*y1
        cop=[]
        good=True
        for p in PTS:
            gap=Fraction(VAL[p])-a*p[0]-b*p[1]-c
            if gap<0:
                good=False; break
            if gap==0: cop.append(p)
        if good and len(cop)==3:
            facets.append(tuple(sorted(tri)))
    facets=sorted(set(facets))
    assert len(facets)==16, len(facets)
    # Unimodular and correct area 8 (= area of Delta_4).
    twice_areas=[abs(det2(*t)) for t in facets]
    assert set(twice_areas)=={1}
    assert sum(twice_areas)==16
    return facets
TRIS=lower_triangulation()

class UF:
    def __init__(self): self.p={}
    def add(self,x):
        if x not in self.p:self.p[x]=x
    def find(self,x):
        p=self.p[x]
        if p!=x:self.p[x]=self.find(p)
        return self.p[x]
    def union(self,a,b):
        self.add(a);self.add(b)
        a,b=self.find(a),self.find(b)
        if a!=b:self.p[b]=a

def reflected_sign(signs,p,ex,ey):
    i,j=p
    return signs[p]*(ex if i%2 else 1)*(ey if j%2 else 1)

def mid(a,b):
    return (Fraction(a[0]+b[0],2), Fraction(a[1]+b[1],2))

def components(signs):
    uf=UF(); graph_nodes=set()
    # Four reflected charts in the diamond |x|+|y|<=4.
    for ex,ey in product((1,-1), repeat=2):
        for tri in TRIS:
            vv=[(ex*p[0],ey*p[1]) for p in tri]
            ss=[reflected_sign(signs,p,ex,ey) for p in tri]
            changing=[]
            for a,b in ((0,1),(1,2),(2,0)):
                if ss[a]!=ss[b]: changing.append(mid(vv[a],vv[b]))
            if changing:
                assert len(changing)==2
                u,v=changing
                graph_nodes.update((u,v)); uf.union(u,v)
    # Projective compactification: opposite points on the boundary diamond are identified.
    for u in list(graph_nodes):
        if abs(u[0])+abs(u[1])==4:
            v=(-u[0],-u[1])
            assert v in graph_nodes
            uf.union(u,v)
    return len({uf.find(u) for u in graph_nodes})

def characters(s):
    A=s[(0,0)]*s[(2,2)]>0
    B=s[(2,1)]*s[(3,1)]*s[(3,0)]*s[(2,2)]<0
    C=s[(1,2)]*s[(1,3)]*s[(2,2)]*s[(0,3)]<0
    return A,B,C

def real_classes(s):
    A,B,C=characters(s)
    return 1 + A+B+C + A*B+A*C+B*C

def enumerate_orthants():
    others=[p for p in PTS if p!=(0,0)]
    joint=Counter(); pats=Counter()
    for bits in product((1,-1), repeat=len(others)):
        s={(0,0):1}; s.update(dict(zip(others,bits)))
        abc=characters(s); k=sum(abc)
        comp=components(s); rb=4*real_classes(s)
        assert comp==k+1
        assert rb == (4,8,16,28)[k]
        joint[(comp,rb)]+=1; pats[abc]+=1
    assert set(pats.values())=={2048} and len(pats)==8
    assert joint==Counter({(1,4):2048,(2,8):6144,(3,16):6144,(4,28):2048}), joint
    return joint,pats

def source_samples():
    # Table 2 uses all-positive signs, then flips the listed coefficients.
    base={p:1 for p in PTS}
    expected=[((),2,8),(((3,1),),3,16),(((1,3),(3,1)),4,28),(((1,3),(3,1),(2,2)),1,4)]
    for flips,cc,rb in expected:
        s=base.copy()
        for p in flips:s[p]*=-1
        assert components(s)==cc, (flips,components(s),cc)
        assert 4*real_classes(s)==rb

source_samples()
joint,pats=enumerate_orthants()
print('VERIFY_OK triangles=16 projective_sign_orthants=16384 patterns=8x2048 census=1oval:2048,2nonnested:6144,3ovals:6144,4ovals:2048 real_bitangents=4,8,16,28')
