"""Exact finite-field checks for the symmetric Burkhardt quartic (public mathematics only)."""
from itertools import combinations, product
from math import comb

# F_4 = F_2[t]/(t^2+t+1), encoded as 0,1,t,1+t.
def mul(a,b):
    z=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1): z ^= 1<<(i+j)
    if z&8:z^=0b1100 # not needed for degree <=2 inputs
    if z&4:z^=0b111  # t^2 = t+1
    return z

def prod(seq):
    r=1
    for x in seq:r=mul(r,x)
    return r

def e(seq,k):
    r=0
    for ix in combinations(range(len(seq)),k):r ^= prod(seq[i] for i in ix)
    return r

def canonical(x):
    a=next(t for t in x if t)
    ai=mul(a,a)   # inverse a^2 over F4*
    return tuple(mul(t,ai) for t in x)

def six_from_five(y):
    x=list(y)
    r=0
    for v in x:r^=v
    x.append(r)
    return tuple(x)

def singular(x):
    # The Jacobian in x_0,...,x_4 after eliminating x_5.
    g5=e(x[:5],3)
    return all((e(x[:i]+x[i+1:],3)^g5)==0 for i in range(5))

def points(field):
    found=set()
    for y in product(field,repeat=5):
        if all(v==0 for v in y):continue
        x=canonical(six_from_five(y))
        if e(x,4)==0:found.add(x)
    return found

f2=points([0,1]);f4=points(range(4))
assert len(f2)==15, len(f2)
assert all(singular(p) for p in f2)
assert all(sum(bool(a) for a in x)==2 for x in f2)
assert len({x for x in f4 if singular(x)})==45
assert set(f2).issubset(f4)
assert len(f4)>45
q_zeros=[v for v in product([0,1],repeat=4) if sum((v[i]&v[j]) for i in range(4) for j in range(i+1,4))%2==0]
assert len(q_zeros)==6
assert len(q_zeros)-1==5
fixed=len(f2)
assert (45-fixed)%2==0
assert fixed==15 and (45-fixed)//2==15
print('F2_points=',len(f2),'all_singular=',all(singular(p) for p in f2))
print('F4_points=',len(f4),'F4_singular=',sum(singular(p) for p in f4),'F4_smooth=',sum(not singular(p) for p in f4))
print('F2 exceptional tangent quadric rational points=',len(q_zeros)-1)
print('F2 blowup rational points=',len(f2)*(len(q_zeros)-1))
print('Geometric node Frobenius profile=1^15 2^15 (45 nodes classified by the accompanying proof)')
print('VERIFY_OK')

def quadratic_expansion(x):
    # Chart x0=1, local t1,...,t4 and x5=x0+x1+...+x4.
    # Truncate the polynomial e4 to total degree <=2.
    zero=(0,0,0,0)
    constpoly=lambda v: {zero:v} if v else {}
    add=lambda A,B: {m:A.get(m,0)^B.get(m,0) for m in set(A)|set(B) if A.get(m,0)^B.get(m,0)}
    def times(A,B):
        C={}
        for a,c in A.items():
            for b,d in B.items():
                ex=tuple(a[i]+b[i] for i in range(4))
                if sum(ex)>2:continue
                C[ex]=C.get(ex,0)^mul(c,d)
        return {k:v for k,v in C.items() if v}
    slots=[]
    slots.append(constpoly(x[0]))
    for j in range(4):
        m=tuple(int(k==j) for k in range(4))
        slots.append(add(constpoly(x[j+1]),{m:1}))
    q=constpoly(x[5])
    for j in range(4):
        m=tuple(int(k==j) for k in range(4))
        q=add(q,{m:1})
    slots.append(q)
    F={}
    for idx in combinations(range(6),4):
        P=constpoly(1)
        for i in idx:P=times(P,slots[i])
        F=add(F,P)
    assert all(not c or sum(m)>=2 for m,c in F.items())
    Q={m:c for m,c in F.items() if sum(m)==2}
    B=[[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i+1,4):
            m=tuple(int(k in (i,j)) for k in range(4))
            B[i][j]=B[j][i]=Q.get(m,0)
    return Q,B

def rank4(B):
    M=[r.copy() for r in B]
    rank=0
    for j in range(4):
        pivot=next((r for r in range(rank,4) if M[r][j]),None)
        if pivot is None:continue
        M[rank],M[pivot]=M[pivot],M[rank]
        inv=mul(M[rank][j],M[rank][j])
        M[rank]=[mul(inv,a) for a in M[rank]]
        for r in range(4):
            if r!=rank and M[r][j]:
                a=M[r][j]
                M[r]=[M[r][i]^mul(a,M[rank][i]) for i in range(4)]
        rank+=1
    return rank

n15=(1,1,0,0,0,0)
n30=(1,1,2,2,3,3)
for P in [n15,n30]:
    assert e(P,1)==0 and e(P,4)==0 and singular(P)
    Q,B=quadratic_expansion(P)
    assert rank4(B)==4
    print('local-node-type',P,'polar_rank',rank4(B),'quadratic_terms',Q)
print('NODE_QUADRATICS_OK')
def quad_count(Q,field):
    roots=set()
    for v in product(field,repeat=4):
        if all(z==0 for z in v):continue
        z=0
        for exp,a in Q.items():
            term=a
            for k,power in enumerate(exp):
                for _ in range(power):term=mul(term,v[k])
            z^=term
        if z==0:roots.add(canonical(v))
    return len(roots)
q15,_=quadratic_expansion(n15)
q30,_=quadratic_expansion(n30)
print('F2 quadric Q_15 points:',quad_count(q15,[0,1]))
print('F4 quadric Q_15 points:',quad_count(q15,range(4)))
print('F4 quadric Q_30 points:',quad_count(q30,range(4)))
assert quad_count(q15,[0,1])==5
assert quad_count(q15,range(4))==25
assert quad_count(q30,range(4))==25
print('QUADRIC_FIELD_COUNTS_OK')
