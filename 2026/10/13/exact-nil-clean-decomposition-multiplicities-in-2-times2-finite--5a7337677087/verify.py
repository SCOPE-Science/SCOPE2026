from itertools import product
from collections import Counter

class PrimeField:
    def __init__(self,p): self.q=p
    def add(self,a,b): return (a+b)%self.q
    def sub(self,a,b): return (a-b)%self.q
    def mul(self,a,b): return (a*b)%self.q
    def inv(self,a): return pow(a,-1,self.q)

class GF4:
    q=4
    # elements a+b*alpha encoded a+2b, with alpha^2=alpha+1
    def add(self,a,b): return a^b
    sub=add
    def mul(self,a,b):
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0|(c1<<1)
    def inv(self,a):
        if not a: raise ZeroDivisionError
        for b in range(1,4):
            if self.mul(a,b)==1: return b
        raise AssertionError

def madd(F,A,B): return tuple(F.add(x,y) for x,y in zip(A,B))
def msub(F,A,B): return tuple(F.sub(x,y) for x,y in zip(A,B))
def mmul(F,A,B):
    a,b,c,d=A; e,f,g,h=B
    return (F.add(F.mul(a,e),F.mul(b,g)),
            F.add(F.mul(a,f),F.mul(b,h)),
            F.add(F.mul(c,e),F.mul(d,g)),
            F.add(F.mul(c,f),F.mul(d,h)))
def tr(F,A): return F.add(A[0],A[3])
def det(F,A): return F.sub(F.mul(A[0],A[3]),F.mul(A[1],A[2]))
def is_idem(F,A): return mmul(F,A,A)==A
def is_nil(F,A): return tr(F,A)==0 and det(F,A)==0

def projective_reps(F):
    return [(1,t) for t in range(F.q)]+[(0,1)]

def invariant_lines(F,A):
    a,b,c,d=A
    n=0
    for x,y in projective_reps(F):
        u=(F.add(F.mul(a,x),F.mul(b,y)),F.add(F.mul(c,x),F.mul(d,y)))
        if F.sub(F.mul(x,u[1]),F.mul(y,u[0]))==0:
            n+=1
    return n

def direct_count(F,A,idems):
    return sum(1 for E in idems if is_nil(F,msub(F,A,E)))

def formula(F,A):
    I=(1,0,0,1)
    ans=int(is_nil(F,A))+int(is_nil(F,msub(F,A,I)))
    if tr(F,A)==1:
        ans += F.q+1-invariant_lines(F,A)+F.q*int(det(F,A)==0)
    return ans

def classify_trace_one(F,A):
    q=F.q
    if tr(F,A)!=1: return None
    e=invariant_lines(F,A); d=det(F,A)
    # scalar test
    scalar=(A[1]==0 and A[2]==0 and A[0]==A[3])
    if d==0: return 'det0'
    if scalar: return 'scalar'
    if e==2: return 'split'
    if e==1: return 'jordan'
    if e==0: return 'irreducible'
    raise AssertionError((A,e,d))

def expected_profile(q,even):
    out={
      'det0':(2*q-1,q*(q+1)),
      'split':(q-1, q*(q+1)*(q-2)//2 if even else q*(q+1)*(q-3)//2),
      'irreducible':(q+1, q*q*(q-1)//2 if even else q*(q-1)*(q-1)//2),
    }
    if not even:
        out['jordan']=(q,q*q-1)
        out['scalar']=(0,1)
    return out

def run(F, even):
    q=F.q
    mats=list(product(range(q), repeat=4))
    idems=[A for A in mats if is_idem(F,A)]
    assert len(idems)==q*(q+1)+2, (q,len(idems))
    counts=Counter()
    types=Counter()
    type_values={}
    for A in mats:
        got=direct_count(F,A,idems)
        want=formula(F,A)
        assert got==want,(q,A,got,want,tr(F,A),det(F,A),invariant_lines(F,A))
        counts[got]+=1
        typ=classify_trace_one(F,A)
        if typ:
            types[typ]+=1
            type_values.setdefault(typ,set()).add(got)
    nil_locus=sum(v for k,v in counts.items() if k>0)
    expected_locus=q**3+2*q**2-(0 if even else 1)
    assert nil_locus==expected_locus,(q,nil_locus,expected_locus)
    exp=expected_profile(q,even)
    for typ,(value,mult) in exp.items():
        assert types[typ]==mult,(q,typ,types[typ],mult)
        if mult:
            assert type_values[typ]=={value},(q,typ,type_values[typ],value)
    extra=set(types)-set(exp)
    assert not extra,(q,extra)
    assert sum(types.values())==q**3,(q,sum(types.values()),q**3)
    # nilpotent and I+nilpotent matrices must be exactly the multiplicity-one families
    n_nil=sum(1 for A in mats if is_nil(F,A))
    assert n_nil==q*q,(q,n_nil)
    assert counts[1]==2*q*q,(q,counts[1],2*q*q)
    print('FIELD_OK',q,'idempotents',len(idems),'nil_locus',nil_locus,'distribution',dict(sorted(counts.items())))

for p in (2,3,5,7):
    run(PrimeField(p), even=(p==2))
run(GF4(), even=True)
print('VERIFY_OK')
