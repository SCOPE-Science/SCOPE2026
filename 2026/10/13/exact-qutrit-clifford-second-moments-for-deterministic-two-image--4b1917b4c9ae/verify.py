from fractions import Fraction as Q
from collections import deque, Counter
import itertools
import sympy as sp

# Exact Q(omega), omega^2+omega+1=0, represented by a+b*omega.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
def conj(x):
    a,b=x
    return (a-b,-b)
def scale(x,q): return (x[0]*q,x[1]*q)
ZERO=(Q(0),Q(0)); ONE=(Q(1),Q(0)); W=(Q(0),Q(1)); W2=(Q(-1),Q(-1))
WP=[ONE,W,W2]

labels=[(a,b) for a in range(3) for b in range(3) if (a,b)!=(0,0)]
idx={v:i for i,v in enumerate(labels)}

def gen_action(name):
    p=[]; e=[]
    for a,b in labels:
        if name=='X': u=(a,b); ph=(-b)%3
        elif name=='Z': u=(a,b); ph=a%3
        elif name=='P': u=(a,(b+a)%3); ph=(a*(a-1)//2)%3
        elif name=='F': u=((-b)%3,a); ph=(-a*b)%3
        else: raise ValueError(name)
        p.append(idx[u]); e.append(ph)
    return tuple(p),tuple(e)

def compose(h,g):
    # h after g: columns map e_j -> w^eg[j] e_pg[j] -> ...
    pg,eg=g; ph,eh=h
    return (tuple(ph[pg[j]] for j in range(8)),
            tuple((eg[j]+eh[pg[j]])%3 for j in range(8)))

ID=(tuple(range(8)),(0,)*8)
gens=[gen_action(x) for x in ('F','P','X','Z')]
seen={ID}; dq=deque([ID])
while dq:
    g=dq.popleft()
    for h in gens:
        k=compose(h,g)
        if k not in seen:
            seen.add(k); dq.append(k)
assert len(seen)==216
GROUP=list(seen)

def phi_for(Fun):
    # phi in nonidentity Weyl basis D_(a,b)=X^a Z^b.
    M=[[ZERO for _ in range(8)] for __ in range(8)]
    for b in (1,2):
        j=idx[(0,b)]
        for c in (1,2):
            i=idx[(0,c)]
            s=ZERO
            for x in range(3):
                s=add(s,WP[(b*x-c*Fun[x])%3])
            M[i][j]=scale(s,Q(1,3))
    return M

def twirl(Fun):
    phi=phi_for(Fun)
    S=[[ZERO for _ in range(64)] for __ in range(64)]
    for p,e in GROUP:
        # M = g^* phi g, sparse dense representation
        M=[[ZERO for _ in range(8)] for __ in range(8)]
        for j in range(8):
            zj=WP[e[j]]
            for k in range(8):
                v=phi[p[j]][p[k]]
                if v!=ZERO:
                    M[j][k]=mul(mul(conj(zj),WP[e[k]]),v)
        nz=[(j,k,M[j][k]) for j in range(8) for k in range(8) if M[j][k]!=ZERO]
        for j,k,v in nz:
            for l,m,w in nz:
                row=8*j+l; col=8*k+m
                S[row][col]=add(S[row][col],mul(v,w))
    # divide and prove rationality
    R=[]
    for row in S:
        rr=[]
        for a,b in row:
            a/=216; b/=216
            assert b==0
            rr.append(sp.Rational(a.numerator,a.denominator))
        R.append(rr)
    return sp.Matrix(R)

def fixed(Fun): return sum(i==Fun[i] for i in range(3))

def first_decay(Fun):
    # Tr full superoperator = # fixed basis projectors, top-left scalar=1.
    return sp.Rational(fixed(Fun)-1,8)

I=sp.eye(64)
counts=Counter()
for Fun in itertools.product(range(3),repeat=3):
    if len(set(Fun))!=2: continue
    r=fixed(Fun)
    A=twirl(Fun)
    assert A.rank()==12
    if r==1:
        assert A*(A-sp.Rational(1,6)*I)*(A+sp.Rational(1,12)*I)==sp.zeros(64)
        assert sp.trace(A)==0
        spec={sp.Rational(1,6):4,sp.Rational(-1,12):8,sp.Rational(0):52}
    else:
        assert A*(A-sp.Rational(1,6)*I)*(A-sp.Rational(1,24)*I)==sp.zeros(64)
        assert sp.trace(A)==1
        spec={sp.Rational(1,6):4,sp.Rational(1,24):8,sp.Rational(0):52}
    # Full second-moment matrix is block lower triangular with diag 1, fI_8,fI_8,A.
    f=first_decay(Fun)
    full=Counter({sp.Rational(1):1})
    for ev,m in spec.items(): full[ev]+=m
    full[f]+=16
    if full[sp.Rational(0)]==0: del full[sp.Rational(0)]
    # merge zero multiplicities if f=0 was added
    expected = {
      0: Counter({sp.Rational(1):1,sp.Rational(1,6):4,sp.Rational(1,24):8,sp.Rational(-1,8):16,sp.Rational(0):52}),
      1: Counter({sp.Rational(1):1,sp.Rational(1,6):4,sp.Rational(-1,12):8,sp.Rational(0):68}),
      2: Counter({sp.Rational(1):1,sp.Rational(1,6):4,sp.Rational(1,24):8,sp.Rational(1,8):16,sp.Rational(0):52}),
    }[r]
    assert full==expected, (Fun,r,full,expected)
    counts[r]+=1

assert counts==Counter({0:6,1:6,2:6})
print('VERIFY_OK')
print('projective_qutrit_clifford_size=216')
print('image_two_maps=18')
print('fixed_point_counts='+repr(dict(sorted(counts.items()))))
print('spectrum_r0=1^1,(1/6)^4,(1/24)^8,(-1/8)^16,0^52')
print('spectrum_r1=1^1,(1/6)^4,(-1/12)^8,0^68')
print('spectrum_r2=1^1,(1/6)^4,(1/24)^8,(1/8)^16,0^52')
