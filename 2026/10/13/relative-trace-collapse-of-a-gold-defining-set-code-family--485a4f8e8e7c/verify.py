# Exact finite-field check for the Gold defining-set equivalence theorem at m=6.
M=6
MOD=(1<<6)|(1<<1)|1  # x^6+x+1
MASK=(1<<6)-1

def deg(x): return x.bit_length()-1

def mul(a,b):
    r=0
    aa=a
    bb=b
    while bb:
        if bb&1: r ^= aa
        bb >>= 1
        aa <<= 1
        if aa & (1<<M): aa ^= MOD
    return r & MASK

def powf(a,n):
    r=1
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a); n//=2
    return r

def inv(a):
    assert a
    return powf(a,(1<<M)-2)

def trF(a):
    s=0; x=a
    for _ in range(M):
        s ^= x; x=mul(x,x)
    assert s in (0,1)
    return s
Q=1<<(M//2)
E=M//2

def frobQ(a): return powf(a,Q)
def reltr(a): return a ^ frobQ(a)
def norm(a): return mul(a,frobQ(a))
def inK(a): return frobQ(a)==a

def trK(k):
    assert inK(k)
    s=0; x=k
    for _ in range(E):
        s ^= x; x=mul(x,x)
    assert s in (0,1)
    return s

def D(a1,a2):
    return {x for x in range(1,1<<M) if trF(mul(a1,norm(x)))==0 and trF(mul(a2,norm(x)))==0}

def Dc(c):
    assert c and inK(c)
    return {x for x in range(1,1<<M) if trK(mul(c,norm(x)))==0}

def weight_enum(S):
    out={}
    for b in range(1<<M):
        w=sum(trF(mul(b,x)) for x in S)
        out[w]=out.get(w,0)+1
    return out
# sanity field inverses
for a in range(1,1<<M): assert mul(a,inv(a))==1
# relative trace identity for every a,x
for a in range(1<<M):
  for x in range(1<<M):
    y=norm(x)
    assert inK(y)
    assert trF(mul(a,y))==trK(mul(reltr(a),y))
# norm surjectivity and unit-circle size
Kstar=[k for k in range(1,1<<M) if inK(k)]
for k in Kstar:
    assert any(norm(t)==k for t in range(1,1<<M))
U=[u for u in range(1,1<<M) if norm(u)==1]
assert len(U)==Q+1==9
# all Theorem 3.5 parameter pairs; normalize and check permutation map
pairs=0
all_sets=[]
for a1 in range(2,1<<M): # GF(2)={0,1}; paper excludes both
  if a1==1: continue
  for a2 in range(2,1<<M):
    if a2==a1: continue
    c1,c2=reltr(a1),reltr(a2)
    rank1 = (c1==0) ^ (c2==0) or (c1!=0 and c1==c2)
    paper35 = ((inK(a1) and not inK(a2)) or (not inK(a1) and inK(a2)) or (not inK(a1) and not inK(a2) and inK(a1^a2)))
    assert rank1==paper35
    if not paper35: continue
    pairs+=1
    c=c1 or c2
    S=D(a1,a2)
    assert S==Dc(c)
    assert len(S)==27
    # normalize to any fixed c0=1 by t with N(t)=c, since D_c -> D_1 under x->t x (1*N(t)=c)
    t=next(t for t in range(1,1<<M) if norm(t)==c)
    image={mul(t,x) for x in S}
    assert image==Dc(1)
    # norm-one torus acts coordinatewise on S
    for u in U:
        assert {mul(u,x) for x in S}==S
    all_sets.append(S)
# canonical weight distribution matches source Table 2 for m=6
canon=Dc(1)
assert weight_enum(canon)=={0:1,12:36,16:27}
assert pairs>0
print('THEOREM35_PAIRS',pairs)
print('CANONICAL_LENGTH',len(canon))
print('UNIT_CIRCLE_ORDER',len(U))
print('WEIGHT_ENUM',weight_enum(canon))
print('VERIFY_OK')
