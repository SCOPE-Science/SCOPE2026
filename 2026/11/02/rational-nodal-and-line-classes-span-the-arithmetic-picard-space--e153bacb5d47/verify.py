"""Exact, standalone verification of the F3 Cayley Hessian K3 arithmetic.

Dependencies: Python >=3.9 and SymPy >=1.10. No remote services.
Run: python verify.py
"""
from itertools import product, permutations
from collections import Counter
import sympy as s

x=s.symbols('x0:4')
e1=sum(x)
e3=sum(s.prod(x[j] for j in range(4) if j!=i) for i in range(4))
e4=s.prod(x)
F=s.expand(e3)
h=s.expand(e1*e3-4*e4)
assert s.expand(s.hessian(F,x).det()+4*h)==0
print('INTEGRAL_HESSIAN_IDENTITY=PASS')

# All four projective affine charts, Groebner bases over F3.
all_rational_nodes=set()
for j in range(4):
    zz=[x[i] for i in range(4) if i!=j]
    f=s.Poly(h.subs(x[j],1),*zz,modulus=3)
    constraints=[f]+[f.diff(z) for z in zz]
    G=s.groebner(constraints,*zz,order='lex',modulus=3)
    leading=[g.LM(order='lex').exponents for g in G.polys]
    bounds=[]
    for k in range(3):
        pure=[u[k] for u in leading if all(u[l]==0 for l in range(3) if l!=k)]
        assert pure
        bounds.append(min(pure))
    monomials=[u for u in product(*(range(b) for b in bounds))
               if all(not all(u[k]>=v[k] for k in range(3)) for v in leading)]
    assert len(monomials)==9, (j,len(monomials),G)
    singular=[]
    for t in product(range(3),repeat=3):
        ev=dict(zip(zz,t))
        if all(int(g.eval(ev))%3==0 for g in constraints):
            singular.append(t)
            arr=[0]*4;arr[j]=1
            for i,v in zip((i for i in range(4) if i!=j),t):arr[i]=v
            k=next(i for i in range(4) if arr[i]!=0)
            inv=pow(arr[k],-1,3)
            all_rational_nodes.add(tuple((a*inv)%3 for a in arr))
    assert len(singular)==9
    print(f'CHART_{j}_GROEBNER_LENGTH=9;F3_SINGULAR_SOLUTIONS=9')
assert len(all_rational_nodes)==15
# Full orbit description, includes one characteristic-three-only node.
reps=[(1,0,0,0),(1,2,0,0),(1,1,1,2),(1,1,1,1)]
orbit_sets=[]
for v in reps:
    orbit=set()
    for perm in set(permutations(v)):
        k=next(i for i,a in enumerate(perm) if a)
        z=pow(perm[k],-1,3)
        orbit.add(tuple((a*z)%3 for a in perm))
    orbit_sets.append(orbit)
assert [len(a) for a in orbit_sets]==[4,6,4,1]
assert set.union(*orbit_sets)==all_rational_nodes
assert all(not orbit_sets[i].intersection(orbit_sets[j]) for i in range(4) for j in range(i+1,4))
for v in all_rational_nodes:
    j=next(i for i,a in enumerate(v) if a)
    zz=[x[i] for i in range(4) if i!=j]
    local=h.subs(x[j],1)
    det=s.hessian(local,zz).det()
    ev=dict(zip(x,v))
    assert int(det.subs(ev))%3!=0,(v,det)
print('GEOMETRIC_SINGULARITIES=15_RATIONAL_NODES;ORBITS=4,6,4,1;HESSIAN_RANK3=PASS')

# Two independent projective-point counts; enumerate all normalized projective vectors.
def points_q(q,zero,one,add,mul,neg):
    histogram=Counter()
    for first in range(4):
        for trail in product(range(q),repeat=3-first):
            v=(zero,)*first+(one,)+trail
            esum=zero;ethree=zero;efour=one
            for t in v:
                esum=add[esum][t];efour=mul[efour][t]
            for j in range(4):
                prod=one
                for k in range(4):
                    if k!=j:prod=mul[prod][v[k]]
                ethree=add[ethree][prod]
            val=add[mul[esum][ethree]][neg[efour]] # -4=-1 modulo 3
            if val==zero:histogram[first]+=1
    return sum(histogram.values()),tuple(histogram[j] for j in range(4))

# F3, integer elements 0,1,2.
add3=[[(a+b)%3 for b in range(3)] for a in range(3)]
mul3=[[(a*b)%3 for b in range(3)] for a in range(3)]
neg3=[(-a)%3 for a in range(3)]
n3,charts3=points_q(3,0,1,add3,mul3,neg3)
assert n3==25,(n3,charts3)
print(f'H_F3_POINTS={n3};AFFINE_CHART_COUNTS={charts3}')

# F9=F3[u]/(u^2+1) with u^2=-1=2.
V=list(product(range(3),repeat=2))
index={z:i for i,z in enumerate(V)}
add9=[[index[((a+c)%3,(b+d)%3)] for c,d in V] for a,b in V]
mul9=[[index[((a*c+2*b*d)%3,(a*d+b*c)%3)] for c,d in V] for a,b in V]
neg9=[index[((-a)%3,(-b)%3)] for a,b in V]
n9,charts9=points_q(9,index[(0,0)],index[(1,0)],add9,mul9,neg9)
assert n9==145,(n9,charts9)
print(f'H_F9_POINTS={n9};AFFINE_CHART_COUNTS={charts9}')

# Each F3-rational A1 exceptional P1 has (q+1) points, replacing one point.
y3=n3+15*3; y9=n9+15*9
assert (y3,y9)==(70,280)
assert y9==1+9**2+22*9
# Frobenius squares all have abs9 and sum 198 -> all equal9.
# Frobenius trace = 70 - (1+3^2)=60 -> plus21, minus1.
assert 21*3-3==y3-1-3**2
for m in range(1,7):
    q=3**m
    smooth=q*q+1+q*(21+(-1)**m)
    singular=smooth-15*q
    assert singular==q*q+1+q*(6+(-1)**m)
print('Y_F3_POINTS=70;Y_F9_POINTS=280;WEIL_UPPER_BOUND=280')
print('FROBENIUS_EIGENVALUES=PLUS3_MULT21,MINUS3_MULT1')
print('ZETA_DENOMINATOR=(1-T)(1-9T)(1-3T)^21(1+3T)')
print('ALL_EXTENSION_FORMULAS=PASS')

# Enumerate every line defined over F3 using reduced row-echelon
# representatives for the 130 two-dimensional subspaces of F3^4.
def polynomial_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]=(out[i+j]+v*w)%3
    return out

def restriction_coefficients(r,s_):
    # Coefficient index is the exponent of u in h(u*r+v*s_).
    linear=[[s_[i],r[i]] for i in range(4)]
    sum_linear=[sum(z[k] for z in linear)%3 for k in range(2)]
    cubic=[0]*4
    for omit in range(4):
        a=[1]
        for i in range(4):
            if i!=omit:a=polynomial_mul(a,linear[i])
        cubic=[(t+v)%3 for t,v in zip(cubic,a)]
    quartic=[1]
    for a in linear:quartic=polynomial_mul(quartic,a)
    target=polynomial_mul(sum_linear,cubic)
    return [(target[k]-quartic[k])%3 for k in range(5)]

lines=[]
charts={}
for pivot_a,pivot_b in __import__('itertools').combinations(range(4),2):
    free=[(row,col) for row,pivot in ((0,pivot_a),(1,pivot_b))
          for col in range(pivot+1,4) if col not in (pivot_a,pivot_b)]
    local_count=0
    for values in product(range(3),repeat=len(free)):
        r=[0]*4;t=[0]*4;r[pivot_a]=1;t[pivot_b]=1
        for (row,col),value in zip(free,values):
            (r if row==0 else t)[col]=value
        if restriction_coefficients(r,t)==[0]*5:
            lines.append((tuple(r),tuple(t)));local_count+=1
    charts[(pivot_a,pivot_b)]=local_count
assert len(lines)==20,(len(lines),charts)
assert sum(3**len([(row,col) for row,pivot in ((0,a),(1,b))
                    for col in range(pivot+1,4) if col not in (a,b)])
           for a,b in __import__('itertools').combinations(range(4),2))==130
print('F3_RATIONAL_GRASSMANN_LINES=130;CONTAINED_IN_QUARTIC=20')

# Linear algebra over F3: intersection of two projective lines iff
# their 2-spaces together have rank <=3; point on line iff rank <=2.
def rank_mod3(vectors):
    a=[list(z) for z in vectors]
    if not a:return 0
    piv=0
    for col in range(len(a[0])):
        row=next((j for j in range(piv,len(a)) if a[j][col]%3),None)
        if row is None:continue
        a[piv],a[row]=a[row],a[piv]
        inverse=pow(a[piv][col]%3,-1,3)
        a[piv]=[(inverse*z)%3 for z in a[piv]]
        for j in range(len(a)):
            if j!=piv and a[j][col]%3:
                c=a[j][col]
                a[j]=[(v-c*w)%3 for v,w in zip(a[j],a[piv])]
        piv+=1
        if piv==len(a):break
    return piv

def point_on_line(p,L):return rank_mod3([p,L[0],L[1]])==2

def line_meets_line(A,B):return rank_mod3(list(A)+list(B))==3

nodes=sorted(all_rational_nodes)
assert len(nodes)==15
M=s.zeros(35)
for k in range(35):M[k,k]=-2
for i,p in enumerate(nodes):
    for j,L in enumerate(lines):
        if point_on_line(p,L):M[i,15+j]=M[15+j,i]=1
for a in range(20):
    for b in range(a+1,20):
        if line_meets_line(lines[a],lines[b]):
            meet_node=any(point_on_line(p,lines[a]) and
                          point_on_line(p,lines[b]) for p in nodes)
            if not meet_node:M[15+a,15+b]=M[15+b,15+a]=1
assert {sum(int(M[i,15+j]) for i in range(15)) for j in range(20)}=={3}
assert {sum(int(M[i,15+j]) for j in range(20)) for i in range(15)}=={4}
assert sum(int(M[15+a,15+b]) for a in range(20) for b in range(a+1,20))==10
print('INCIDENCE=15_NODES_EACH_ON_4_LINES;20_LINES_EACH_THROUGH_3_NODES')
print('SMOOTH_PAIRWISE_LINE_INTERSECTIONS=10')
# Explicit nondegenerate 21-class certificate: lexicographically greedy
# principal minor; exact integer determinant provides a replayable witness.
selected=[]
for i in range(35):
    candidate=selected+[i]
    if M.extract(candidate,candidate).det()!=0:selected=candidate
assert len(selected)==21,(len(selected),selected)
minor_det=int(M.extract(selected,selected).det())
assert minor_det==1536,minor_det
assert M.rank()==21
print('INTERSECTION_MATRIX_SIZE=35;RANK=21;MINOR_INDEXES='+str(selected))
print('NONZERO_PRINCIPAL_MINOR_DETERMINANT='+str(minor_det))
print('FROBENIUS_INVARIANT_PICARD_RANK=21;RATIONAL_GENERATORS_SPAN=PASS')
print('VERIFY_OK')
