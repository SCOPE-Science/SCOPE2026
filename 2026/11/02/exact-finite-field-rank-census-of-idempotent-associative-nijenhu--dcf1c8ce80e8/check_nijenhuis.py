"""Independent finite-field tests for idempotent associative Nijenhuis maps on 2x2 matrices.
No external libraries are required. Run: python check_nijenhuis.py
"""
import itertools
from collections import Counter

class Field:
    def __init__(self, q):
        self.q = q
        if q in (2, 4, 8):
            poly = {2:3,4:7,8:11}[q]
            self.add = lambda a,b: a ^ b
            def times(a,b):
                out=0
                while b:
                    if b&1:out ^= a
                    b >>= 1
                    a <<= 1
                    if a&q:a ^= poly
                return out
            self.mul=times
        elif q in (3,5,7):
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
        else:
            raise ValueError(q)
        self.zero=0
        self.one=1
        self.neg=lambda a:next(x for x in range(q) if self.add(a,x)==0)
        self.inv=lambda a:next(x for x in range(1,q) if self.mul(a,x)==1)
        self.E=list(range(q))
    def sum(self,seq):
        v=0
        for x in seq:v=self.add(v,x)
        return v

def madd(a,b,F):return tuple(F.add(x,y) for x,y in zip(a,b))
def scale(t,v,F):return tuple(F.mul(t,x) for x in v)
def mul(a,b,F):
    s=F.sum; f=F.mul
    return (s((f(a[0],b[0]),f(a[1],b[2]))),s((f(a[0],b[1]),f(a[1],b[3]))),
            s((f(a[2],b[0]),f(a[3],b[2]))),s((f(a[2],b[1]),f(a[3],b[3]))))

def subspace_basis_rref(k,F):
    for piv in itertools.combinations(range(4),k):
        allowed=[(i,j) for i in range(k) for j in range(piv[i]+1,4) if j not in piv]
        for c in itertools.product(F.E,repeat=len(allowed)):
            rows=[[0]*4 for _ in range(k)]
            for i,p in enumerate(piv):rows[i][p]=1
            for (i,j),x in zip(allowed,c):rows[i][j]=x
            yield tuple(map(tuple,rows))

def elements(basis,F):
    out=[]
    for coeffs in itertools.product(F.E,repeat=len(basis)):
        acc=(0,0,0,0)
        for a,v in zip(coeffs,basis):acc=madd(acc,scale(a,v,F),F)
        out.append(acc)
    return frozenset(out)

def subalgebras(k,F):
    out=[]
    for basis in subspace_basis_rref(k,F):
        S=elements(basis,F)
        if all(mul(u,v,F) in S for u in basis for v in basis):
            out.append((basis,S))
    return out

def det(a,F):return F.add(F.mul(a[0],a[3]),F.neg(F.mul(a[1],a[2])))

def typology(S,F):
    one=(1,0,0,1)
    if one in S:
        rank_one_lines=sum(1 for a in S if a!=(0,0,0,0) and det(a,F)==0)//(F.q-1)
        return {0:'field',1:'dual',2:'split'}[rank_one_lines]
    return 'nonunital'

def run(q):
    F=Field(q)
    ranks={k:subalgebras(k,F) for k in (0,1,2,3,4)}
    n_subalgebras={k:len(v) for k,v in ranks.items()}
    types=Counter(typology(S,F) for basis,S in ranks[2]); assert types==Counter({'field':q*(q-1)//2,'split':q*(q+1)//2,'dual':q+1,'nonunital':2*(q+1)}),types
    observed=Counter()
    types2=Counter()
    for k in (0,1,2,3,4):
        complementary = 0
        for b,S in ranks[k]:
            for c,T in ranks[4-k]:
                if len(S.intersection(T))==1:
                    complementary+=1
                    if k==2:types2[(typology(S,F),typology(T,F))]+=1
        observed[k]=complementary
    predicted={0:1,1:q*q*(q+1),2:2*q*(q+1)*(2*q+1),3:q*q*(q+1),4:1}
    assert dict(observed)==predicted,(q,observed,predicted)
    assert sum(observed.values())==2+2*q*(q+1)*(3*q+1)
    left_right=2*q*(q+1)
    expected_middle={('field','nonunital'):q*(q*q-1),('split','nonunital'):q*(q*q-1),('dual','nonunital'):2*q*(q+1),('nonunital','field'):q*(q*q-1),('nonunital','split'):q*(q*q-1),('nonunital','dual'):2*q*(q+1),('nonunital','nonunital'):left_right}
    assert types2==Counter(expected_middle),(q,types2,expected_middle)
    print('FIELD',q,'ALGEBRA_COUNTS',n_subalgebras,'DIM_2_TYPES',dict(types),'PROJECTION_RANKS',dict(sorted(observed.items())),'TOTAL',sum(observed.values()))
    if q==2:
        e=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
        basis_products=[[mul(a,b,F) for b in e] for a in e]
        def apply(P,v):
            out=(0,0,0,0)
            for t,c in zip(v,P):
                if t: out=madd(out,c,F)
            return out
        hist=Counter()
        for flat in itertools.product(F.E,repeat=16):
            P=tuple(tuple(flat[4*i+j] for j in range(4)) for i in range(4))
            if any(apply(P,P[i])!=P[i] for i in range(4)):continue
            okay=True
            for i in range(4):
                for j in range(4):
                    px=P[i]; py=P[j]
                    lhs=mul(px,py,F)
                    intermediate=madd(madd(mul(px,e[j],F),mul(e[i],py,F),F),apply(P,basis_products[i][j]),F)
                    # in characteristic two the minus sign equals the plus sign
                    if lhs!=apply(P,intermediate):okay=False;break
                if not okay:break
            if okay:
                # rank equals dimension of image, computed from all linear combinations
                hist[len({apply(P,v) for v in itertools.product(F.E,repeat=4)}).bit_length()-1]+=1
        assert hist==Counter(predicted),(hist,predicted)
        print('AMBIENT_2_16_LINEAR_MAPS_CHECKED',2**16,'NIJENHUIS_RANK_HISTOGRAM',dict(sorted(hist.items())))

if __name__=='__main__':
    for q in [2,3,4,5,8]:run(q)
    print('M2_ASSOCIATIVE_NIJENHUIS_ALL_CHECKS_OK')
