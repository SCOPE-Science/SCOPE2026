from fractions import Fraction
from collections import Counter
from math import factorial, isqrt

DIMS = 8

def P(S,d):
    return (768*S**4-3981*S**3+5808*S**2-5856*S-480
            +(2000*S**2+5184*S-3648)*d**2-3840*d**4)

def Q(S,d):
    return d*(1152*S**3-4902*S**2+2976*S+4416+11520*d**2)

def ahat(n,m):
    S=n+m; d=m-n
    den=P(S,d)+Q(S,d)
    assert den != 0
    return Fraction(P(S,d)-Q(S,d),den)

def norm2(r):
    return sum(v*v for v in r)

def reps(n):
    out=[]
    def rec(rem,maxv,a):
        if rem==0:
            out.append(tuple(a+[0]*(DIMS-len(a))))
            return
        if len(a)==DIMS: return
        for v in range(min(maxv,isqrt(rem)),0,-1):
            rec(rem-v*v,v,a+[v])
    rec(n,isqrt(n),[])
    return out

def neighbors(r):
    c=Counter()
    for j,v in enumerate(r):
        for s in (-1,1):
            a=list(r); a[j]=v+s
            y=tuple(sorted((abs(t) for t in a), reverse=True))
            if norm2(y): c[y]+=1
    return c

def orbit_size(r):
    c=Counter(r); den=1
    for k in c.values(): den*=factorial(k)
    return factorial(DIMS)//den * 2**sum(v!=0 for v in r)

def key(vals):
    return tuple(sorted(vals,reverse=True)+[0]*(DIMS-len(vals)))

# Alpay's 26 positive local values (Table 4), reproduced as integers.
h={}
for k,v in [(1,2019151),(2,976301),(3,548569),(4,355162),(5,253086),(6,192219),(7,152422),(8,124707)]: h[key([1]*k)]=v
for k,v in [(0,465840),(1,303163),(2,216956),(3,166127),(4,132937),(5,109828),(6,92546),(7,79454)]: h[key([2]+[1]*k)]=v
for k,v in [(0,145309),(1,117200),(2,97618),(3,83209),(4,72239)]: h[key([2,2]+[1]*k)]=v
h[key([2,2,2])]=76395
for k,v in [(0,141855),(1,113990),(2,95291),(3,82045)]: h[key([3]+[1]*k)]=v
assert len(h)==26

def vertex_weight_local(r,R,hmap):
    n=norm2(r); hx=hmap[r]; s=Fraction(0)
    for y,mul in neighbors(r).items():
        m=norm2(y)
        s += mul*(Fraction(hmap[y],hx) if m<=R else ahat(n,m))
    return Fraction(16)-s

# Finite verification of the published R=12 correction.
assert set(h)=={r for n in range(1,13) for r in reps(n)}
mins=[]
for n in range(1,13):
    for r in reps(n):
        V=vertex_weight_local(r,12,h)
        margin=V-Fraction(9,n)
        assert margin>0
        mins.append((margin,n,r))
assert min(mins)[0] == Fraction(3,2019151)

# R<=10 obstruction: x=(3,1,1,0,...,0) is outside and the unmodified field fails.
x=key([3,1,1]); n=norm2(x); assert n==11
s=Fraction(0)
for y,mul in neighbors(x).items(): s += mul*ahat(n,norm2(y))
V11=Fraction(16)-s
deficit=Fraction(9,11)-V11
assert deficit>0

# R=11 obstruction. After signed-permutation averaging, a hypothetical positive
# gluing potential is constant on these 23 orbits.  The local inequalities are
# D_x h_x - sum_y m_xy h_y > 0.
R=11
rr=[r for n in range(1,R+1) for r in reps(n)]
idx={r:i for i,r in enumerate(rr)}

def D(r):
    n=norm2(r); cross=Fraction(0)
    for y,mul in neighbors(r).items():
        if norm2(y)>R:
            aa=ahat(n,norm2(y)); assert aa>0
            cross += mul*aa
    return Fraction(16)-Fraction(9,n)-cross

# L is the orbit-symmetrized matrix: L_xx=o_x D_x and
# L_xy=-o_x m_xy. Detailed balance makes it symmetric.
N=len(rr); assert N==23
os=[orbit_size(r) for r in rr]
L=[[Fraction(0) for _ in range(N)] for _ in range(N)]
for x in rr:
    i=idx[x]; L[i][i]=os[i]*D(x)
    for y,mul in neighbors(x).items():
        if norm2(y)<=R:
            j=idx[y]; L[i][j]-=os[i]*mul
for i in range(N):
    for j in range(N): assert L[i][j]==L[j][i]

# Exact rational negative quadratic-form certificate.
z=[591,286,161,137,104,89,74,64,56,49,44,43,39,36,43,34,32,35,29,27,29,25,23]
quad=Fraction(0)
for i in range(N):
    for j in range(N): quad += z[i]*L[i][j]*z[j]
assert quad<0

# If positive h had Lh>0, putting z_i=h_i w_i gives
# z^T L z = sum_{i<j} c_ij h_i h_j(w_i-w_j)^2
#           + sum_i h_i(Lh)_i w_i^2 > 0 for every nonzero z.
# Therefore this negative certificate rules out R=11.

print('R12_min_local_margin=', min(mins)[0])
print('R_le_10_witness_V11=', V11)
print('R_le_10_deficit=', deficit)
print('R11_quadratic_certificate=', quad)
print('R11_orbit_order=')
for i,r in enumerate(rr): print(i, norm2(r), r, z[i])
print('OK')
