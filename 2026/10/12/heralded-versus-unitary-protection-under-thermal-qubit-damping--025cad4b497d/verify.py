"""Exact rational verification of a generalized-amplitude-damping filter separation.

Only standard-library modules are needed.  For the unitary calculation,
polynomials are reduced modulo w*w = p*(1-u*u), where w=sqrt(p)*sin(theta).
"""
from fractions import Fraction as F
from itertools import combinations, permutations

p = F(7, 20)
gamma = F(4, 5)
k = F(3, 4)
t = (1-p)*(2*gamma-1)
A = gamma+(1-gamma)*p
B = (1-gamma)*(1-p)
C = gamma*(1-p)
D = 1-gamma+gamma*p
assert (A,B,C,D) == (F(87,100), F(13,100), F(13,25), F(12,25))
assert A+B == C+D == 1
assert p*p <= B*C*(A+D)**2
assert p*p > 4*A*B*C*D
q = k*k*A+D
choi_diag = ((k*k*A*A+B*C)/2, B*q/2, C*q/2, (k*k*B*C+D*D)/2)
assert choi_diag == (F(78937,320000), F(20163,320000), F(20163,80000), F(10737,80000))
coherence = k*p/2
assert coherence == F(21,160)
minor = choi_diag[1]*choi_diag[2]-coherence*coherence
assert minor == -F(34453431,25600000000) < 0
assert 0 < k <= 1

# Ring elements (a(u),b(u)) representing a(u)+w*b(u).
def cp(x=0):
    return ({0:F(x)} if x else {}, {})

def monos(c=1,deg=0,odd=False):
    return ({},{deg:F(c)}) if odd else ({deg:F(c)}, {})

def addp(a,b):
    out = dict(a)
    for n,x in b.items():
        out[n] = out.get(n,F(0)) + x
        if not out[n]: del out[n]
    return out

def negp(a): return {n:-x for n,x in a.items()}

def mulp(a,b):
    out={}
    for n,x in a.items():
        for m,y in b.items():out[n+m]=out.get(n+m,F(0))+x*y
    return {n:x for n,x in out.items() if x}

def add(a,b):return (addp(a[0],b[0]),addp(a[1],b[1]))

def neg(a):return (negp(a[0]),negp(a[1]))

def mul(a,b):
    # w^2 = p(1-u^2)
    ww={0:p,2:-p}
    return (addp(mulp(a[0],b[0]),mulp(mulp(a[1],b[1]),ww)),
            addp(mulp(a[0],b[1]),mulp(a[1],b[0])))

def mulscalar(a,x):return ({n:v*x for n,v in a[0].items()}, {n:v*x for n,v in a[1].items()})

one=cp(1); zero=cp();u=monos(deg=1);w=monos(odd=True)
I=[[1,0],[0,1]]
X=[[0,1],[1,0]]
Yreal=[[0,-1],[1,0]] # Y=i*Yreal, hence Y tensor Y = -Yreal tensor Yreal
Z=[[1,0],[0,-1]]

def tensor(a,b):
    return [[a[i//2][j//2]*b[i%2][j%2] for j in range(4)] for i in range(4)]

H=[[zero for j in range(4)] for i in range(4)]
terms=[(one,tensor(I,I)),
       (mulscalar(w,t),tensor(X,I)),
       (add(cp(t),mulscalar(u,t*p)),tensor(Z,I)),
       (mulscalar(u,p),tensor(X,X)),
       (mulscalar(w,p),tensor(X,Z)),
       (cp(-p),tensor(Yreal,Yreal)),
       (mulscalar(w,-p),tensor(Z,X)),
       (mulscalar(u,p*p),tensor(Z,Z))]
for coefficient,matrix in terms:
    for i in range(4):
        for j in range(4):
            H[i][j]=add(H[i][j],mulscalar(coefficient,F(matrix[i][j],4)))

def determinant(mat):
    n=len(mat);res=zero
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        prod=one
        for i,j in enumerate(perm): prod=mul(prod,mat[i][j])
        res=add(res,neg(prod) if inversions%2 else prod)
    return res

e=[]
for size in range(1,5):
    e_sum=zero
    for indices in combinations(range(4),size):
        sub=[[H[i][j] for j in indices] for i in indices]
        e_sum=add(e_sum,determinant(sub))
    e.append(e_sum)

expected=[cp(1),
 ({0:F(13*397910,16000000),1:-F(13*16380,16000000),2:-F(13*2639,16000000)},{}),
 ({0:F(1112805,32000000),1:-F(212940,32000000),2:-F(34307,32000000)},{}),
 ({0:F(139247037225,256000000000000),1:-F(109220120100,256000000000000),
   2:-F(16339726130,256000000000000),3:-F(18389285460,256000000000000),
   4:F(7457876881,256000000000000)}, {})]
assert e==expected,(e,expected)
# e_2 and e_3 decrease on [-1,1], and are positive at u=1.
assert expected[1][0][0]+expected[1][0][1]+expected[1][0][2] > 0
assert expected[2][0][0]+expected[2][0][1]+expected[2][0][2] > 0
# Integer numerator P(u) of e4. Bernstein coefficients of P(2y-1), n=4.
bern=(F(257974593536),F(177204577664),F(456454468448,3),
      F(86373743024),F(2755782416))
assert all(b>0 for b in bern)
from math import comb
poly_y={}
for j,b in enumerate(bern):
    for h in range(5-j):
        degree=j+h
        poly_y[degree]=poly_y.get(degree,F(0))+b*comb(4,j)*comb(4-j,h)*(-1)**h
expected_poly_y={0:F(257974593536),1:F(-323080063488),
                 2:F(334301566144),3:F(-385766343872),4:F(119326030096)}
assert poly_y==expected_poly_y
# Re-expand P(2y-1) directly from the polynomial numerator in u.
numerator={0:139247037225,1:-109220120100,2:-16339726130,
           3:-18389285460,4:7457876881}
reexpanded={n:F(0) for n in range(5)}
for n,coef in numerator.items():
    for h in range(n+1):
        reexpanded[h]+=F(coef)*comb(n,h)*(2**h)*((-1)**(n-h))
assert reexpanded==poly_y
# Positive elementary symmetric functions imply positive spectrum for
# a Hermitian matrix: det(z I + H) has positive coefficients and no z>0 root.
print('VERIFY_OK rational_choi=passed unitary_all_angles=passed bernstein=passed')
