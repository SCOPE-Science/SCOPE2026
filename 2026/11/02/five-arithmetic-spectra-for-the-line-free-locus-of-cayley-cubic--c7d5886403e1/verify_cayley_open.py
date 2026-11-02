#!/usr/bin/env python3
"""Exact finite-group and finite-field checks for open twisted Cayley cubics."""
from itertools import permutations, combinations, product
from collections import defaultdict,Counter
V=tuple(range(4))
E={frozenset(e) for e in combinations(V,2)}
M={frozenset((frozenset(p[:2]),frozenset(p[2:]))) for p in permutations(V)}
assert len(M)==3
inc={(e,v) for e in E for v in e}


def ctype(p):
    seen=set(); parts=[]
    for i in V:
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j);n+=1;j=p[j]
        parts.append(n)
    return tuple(sorted(parts,reverse=True))


def fcounts(p):
    onedge=lambda e:frozenset(p[i] for i in e)
    onmatching=lambda m:frozenset(onedge(e) for e in m)
    v=sum(p[i]==i for i in V)
    m=sum(onmatching(x)==x for x in M)
    e=sum(onedge(x)==x for x in E)
    b=sum(onedge(x)==x and p[i]==i for x,i in inc)
    return (v,m,e,b)


def point_coeffs(p):
    v,m,e,b=fcounts(p)
    # Complement of 4 coordinate and 3 matching lines in P^2:
    # geometric 6 triple and 3 double crossing points;
    # 18 triple branches and 6 double branches.
    return (1-v-m,1-v-2*m+b+m*(m-1))


def move(p,s):
    if isinstance(s,str):return s
    if isinstance(s,int):return p[s]
    if isinstance(s,tuple):return tuple(move(p,t) for t in s)
    if isinstance(s,frozenset):return frozenset(move(p,t) for t in s)
    raise TypeError(s)

# Independent inclusion-exclusion through orbit-fixed incidence sets.
arr_lines={('C',i) for i in V}|{('M',m) for m in M}
triple_points={('T',e) for e in E}
double_points={('D',m) for m in M}
branch3={('T',e,('C',i)) for e in E for i in e}
branch3|={('T',e,('M',next(m for m in M if e in m))) for e in E}
branch2={('D',m,('M',n)) for m in M for n in M if n!=m}
assert [len(s) for s in [arr_lines,triple_points,double_points,branch3,branch2]]==[7,6,3,18,6]

def from_branches(p):
    fix=lambda S:sum(move(p,x)==x for x in S)
    L=fix(arr_lines); P=fix(triple_points)+fix(double_points)
    B=fix(branch3)+fix(branch2)
    return (1-L,1-L+B-P) # P^2 - union: q^2 + (1-L)q + (1-L+B-P)

class_data={}
for p in permutations(V):
    c=ctype(p); f=point_coeffs(p)
    assert f==from_branches(p),(p,f,from_branches(p))
    if c in class_data:assert class_data[c]==f
    else:class_data[c]=f
assert len(class_data)==5
expected={
    (1,1,1,1):(-6,9),
    (2,1,1):(-2,-1),
    (2,2):(-2,1),
    (3,1):(0,0),
    (4,):(0,-1),
}
assert class_data==expected,(class_data,expected)

# Geometric split variety, with lines listed explicitly. By projective normalization,
# every F_p-rational projective point occurs once in the iterator.
def proj_points(p,n=4):
    for lead in range(n):
        for tail in product(range(p),repeat=n-lead-1):
            yield (0,)*lead+(1,)+tail


def surface(x,p):
    return sum(x[i]*x[j]*x[k] for i,j,k in combinations(V,3))%p==0


def on_line(x,p):
    # Edge line: support within 2 coordinates.
    if sum(bool(a) for a in x)<=2:return True
    # Matching line x_i+x_j=x_k+x_l=0.
    return any(all(sum(x[i] for i in e)%p==0 for e in m) for m in M)


def in_inverse_arr(y,p):
    if sum(y)%p!=0 or any(a==0 for a in y):return False
    return not any(any(sum(y[i] for i in e)%p==0 for e in m) for m in M)

for p in (3,5,7,11):
    all_surface=[x for x in proj_points(p) if surface(x,p)]
    off=[x for x in all_surface if not on_line(x,p)]
    hyp=[y for y in proj_points(p) if in_inverse_arr(y,p)]
    assert len(off)==(p-3)**2,(p,len(off))
    assert len(hyp)==len(off)
    inv=lambda x:tuple(pow(a,-1,p) for a in x)
    norm=lambda x:tuple(a*pow(next(t for t in x if t),-1,p)%p for a in x)
    assert {norm(inv(x)) for x in off}==set(hyp)
    print('SPLIT_FIELD',p,'surface',len(all_surface),'off_lines',len(off),'arrangement',len(hyp))

# Explicit character sums and rational zeta numerator/denominator can be read
# from a_n and b_n for powers of any representative.
for c in sorted(expected):
    p=next(p for p in permutations(V) if ctype(p)==c)
    cur=tuple(V);values=[]
    for n in range(1,13):
        cur=tuple(p[i] for i in cur)
        values.append(point_coeffs(cur))
    print('CLASS',c,'coefficients',expected[c],'extension_coefficients',values)

print('S4_ACTION_AND_SPLIT_REDUCTION_VERIFY_OK')

# Independent arithmetic test: construct all five quartic etale F_3-algebras,
# count trace-zero elements with nonvanishing coordinate and pair sums.
class Field:
    def __init__(self,deg,polytail):
        self.deg=deg;self.p=3;self.order=3**deg;self.poly=polytail
        self.coeffs=[tuple((x//3**i)%3 for i in range(deg)) for x in range(self.order)]
    def add(self,a,b):
        return sum(((self.coeffs[a][i]+self.coeffs[b][i])%3)*3**i for i in range(self.deg))
    def mul(self,a,b):
        d=self.deg; c=[0]*(2*d-1)
        for i,ai in enumerate(self.coeffs[a]):
            for j,bj in enumerate(self.coeffs[b]):c[i+j]=(c[i+j]+ai*bj)%3
        for k in range(2*d-2,d-1,-1):
            t=c[k]
            for j in range(d):c[k-d+j]=(c[k-d+j]-t*self.poly[j])%3
        return sum(c[i]*3**i for i in range(d))
    def pow(self,a,n):
        x=1
        while n:
            if n&1:x=self.mul(x,a)
            a=self.mul(a,a);n//=2
        return x

polys={1:(0,),2:(1,0),3:(1,0,2),4:(1,0,1,1)}
for part,expected_count in [((1,1,1,1),0),((2,1,1),2),((2,2),4),((3,1),9),((4,),8)]:
    d=max(part) # partitions here have only 1's or equal nontrivial degree
    K=Field(d,polys[d]);cnt=0; raw=0
    factors=list(product(*[range(3**r) for r in part]))
    for factor_values in factors:
        # x is 4 embeddings of the quartic etale algebra, as a tuple in F_{3^d}.
        xs=[]
        for factor_deg,a in zip(part,factor_values):
            for i in range(factor_deg):xs.append(K.pow(a,3**i))
        if any(x==0 for x in xs):continue
        tr=0
        for x in xs:tr=K.add(tr,x)
        if tr!=0:continue
        if any(K.add(xs[0],xs[j])==0 for j in (1,2,3)):continue
        raw+=1
    assert raw%2==0
    cnt=raw//2
    assert cnt==expected_count,(part,cnt,expected_count)
    print('TWIST_F3',part,'open_points',cnt)
print('ALL_FIVE_ARITHMETIC_TWISTS_VERIFY_OK')
