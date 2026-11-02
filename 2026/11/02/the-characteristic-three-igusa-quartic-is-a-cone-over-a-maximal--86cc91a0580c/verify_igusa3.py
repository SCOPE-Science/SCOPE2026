"""Exact verification of the characteristic-three Igusa cone and its K3 base.

Requires SymPy. Everything is computed over GF(3) or GF(9); no floating-point
arithmetic, database tables or pre-computed singular-locus ideals are used.
"""
import itertools
import sympy as sp

u=sp.symbols('a b c d')
y=list(u)+[-sum(u)]
F=sp.Poly(sp.expand(sum(t*t for t in y)**2-4*sum(t**4 for t in y)),*u,modulus=3).as_expr()

def rank_mod3(matrix):
    a=[[int(t)%3 for t in row] for row in matrix]
    i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i]
        c=pow(a[i][j],-1,3)
        a[i]=[(c*v)%3 for v in a[i]]
        for h in range(len(a)):
            if h!=i:
                t=a[h][j]
                a[h]=[(v-t*w)%3 for v,w in zip(a[h],a[i])]
        i+=1
        if i==len(a):break
    return i

def normalize(v,p):
    lead=next((x for x in v if x),None)
    return None if lead is None else tuple((x*pow(lead,-1,p))%p for x in v)

# Full homogeneous projective Jacobian scheme; a chart has three variables.
points=set()
for idx,coordinate in enumerate(u):
    rem=[v for v in u if v!=coordinate]
    ff=sp.Poly(F.subs(coordinate,1),*rem,modulus=3).as_expr()
    jac=[ff]+[sp.diff(ff,t) for t in rem]
    g=sp.groebner(jac,*rem,order='grevlex',modulus=3)
    assert g.is_zero_dimensional
    # Count standard monomials in GF(3)[rem]/Jac, via leading monomials.
    leading=[m.LM(order='grevlex').exponents for m in g.polys]
    standards=[exp for exp in itertools.product(range(7),repeat=3)
        if all(not all(x>=y for x,y in zip(exp,l)) for l in leading)]
    assert len(standards)==12,(idx,len(standards))
    for r in itertools.product(range(3),repeat=3):
        v=list(r);v.insert(idx,1)
        if all(int(t.eval(dict(zip(rem,r))))%3==0 for t in g.polys):
            points.add(normalize(v,3))
    # Each chart contains exactly twelve reduced rational singular points.
    on_chart=sum(p[idx]!=0 for p in points)
    assert on_chart==12,(idx,on_chart)
assert len(points)==15

# Confirm the syntheme (three pair) parametrization gives all singular points.
def perfect_matchings(xs):
    if not xs:
        yield []
        return
    i=xs[0]
    for j in xs[1:]:
        for rest in perfect_matchings([t for t in xs if t not in (i,j)]):
            yield [(i,j)]+rest
assert_synthemes=set()
for pairs in perfect_matchings(list(range(6))):
    x=[0]*6
    for val,pair in enumerate(pairs):
        for index in pair:x[index]=val
    shift=x[5];z=[(xi-shift)%3 for xi in x]
    assert (sum(z)%3==0 and z[5]==0)
    assert_synthemes.add(normalize(z[:4],3))
assert assert_synthemes==points

# Nondegenerate quadratic term in the local equation: ordinary double points.
for P in points:
    idx=next(i for i,x in enumerate(P) if x)
    rem=[v for i,v in enumerate(u) if i!=idx]
    ff=sp.Poly(F.subs(u[idx],1),*rem,modulus=3).as_expr()
    center={v:P[j] for j,v in enumerate(u) if j!=idx}
    hess=sp.hessian(ff,rem)
    H=[[int(hess[i,j].subs(center))%3 for j in range(3)] for i in range(3)]
    assert rank_mod3(H)==3,(P,H)

# GF(9) arithmetic: elements a+b*i, i^2=-1, encoded as 3*a+b.
def gf9_add(x,y):
    a,b=divmod(x,3);c,d=divmod(y,3)
    return 3*((a+c)%3)+(b+d)%3

def gf9_mul(x,y):
    a,b=divmod(x,3);c,d=divmod(y,3)
    return 3*((a*c-b*d)%3)+(a*d+b*c)%3

def field_count(q):
    if q==3:
        add=lambda x,y:(x+y)%3
        mul=lambda x,y:(x*y)%3
        neg=lambda x:(-x)%3
        one=1
    else:
        assert q==9
        add=gf9_add;mul=gf9_mul
        neg=lambda x:gf9_mul(6,x)
        one=3
    total=0
    for first_nonzero in range(4):
        for trailing in itertools.product(range(q),repeat=3-first_nonzero):
            v=[0]*first_nonzero+[one]+list(trailing)
            s=0
            for x in v:s=add(s,x)
            v.append(neg(s))
            p2=p4=0
            for x in v:
                x2=mul(x,x)
                p2=add(p2,x2)
                p4=add(p4,mul(x2,x2))
            if add(mul(p2,p2),neg(p4))==0:total+=1
    return total

n3,n9=field_count(3),field_count(9)
assert (n3,n9)==(25,145)
res3,res9=n3+15*3,n9+15*9
assert (res3,res9)==(70,280)
assert res9==1+9*9+22*9
plus=(22+(res3-1-3*3)//3)//2
minus=22-plus
assert (plus,minus)==(21,1)
for m in (1,2):
    q=3**m
    qpoint={1:n3,2:n9}[m]
    assert qpoint==1+q*q+(6+(-1)**m)*q
print('SINGULAR_POINTS=15_F3_RATIONAL_ORDINARY_NODES')
print('SINGULAR_IDEAL_CHART_LENGTHS=12,12,12,12_ALL_REDUCED')
print('SYNTHEME_BIJECTION=15_PARTITIONS')
print(f'QUARTIC_POINTS_F3={n3};_F9={n9}')
print(f'K3_RESOLUTION_POINTS_F3={res3};_F9={res9}')
print('WEIL_MAX_F9=280;FROBENIUS_EIGENVALUES_PLUS3_21_MINUS3_1')
print('VERIFY_OK')
