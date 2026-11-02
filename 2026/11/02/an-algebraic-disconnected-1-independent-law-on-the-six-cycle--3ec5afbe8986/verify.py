"""Exact rational-algebraic verification of a 1-independent C6 model.
Requires only Python standard library; a proof on a fixed six-edge configuration space.
"""
from fractions import Fraction as Q
P=(1,0,-24,74,-72,12,1) # coefficients ascending
LOW=Q(597345,10**6)
HIGH=Q(597346,10**6)


def trim(a):
    a=list(map(Q,a))
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b)))])

def neg(a): return [-x for x in a]

def sub(a,b):return add(a,neg(b))

def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    while len(c)>6:
        v=c.pop()
        for k,t in enumerate(P[:-1]):c[len(c)-6+k]-=v*t
    return trim(c)

def scale(a,k):return trim([Q(k)*x for x in a])

def poly_eval(a,x):
    s=Q(0)
    for t in a[::-1]: s=s*x+t
    return s

def lipschitz(a):return sum(k*abs(t) for k,t in enumerate(a) if k>0)

def positive_at_root(a):return poly_eval(a,LOW)> lipschitz(a)*(HIGH-LOW)

# six D6-orbit *total* probabilities for representative presence masks.
# All other orbits carry zero probability.
weights={
    0b001001: [6,-36,82,-72,12,1],
    0b001011: [-10,72,-170,146,-24,-2],
    0b001111: [4,-30,79,-74,12,1],
    0b010101: [2,-6,6,-2],
    0b010111: [-2,6,-6,6,-4,0],
    0b011011: [-1,6,-7,2],
}
# Rewrite two easily factored polynomials above precisely:
# w_010111 = 2 (2p-1)(p^2-p+1) = -2+6p-6p^2+4p^3
weights[0b010111]=[-2,6,-6,4]
# w_011011 = -(2p-1)(p^2-4p+1) = 1-6p+9p^2-2p^3
weights[0b011011]=[1,-6,9,-2]


def cycle_image(mask,sgn,shift):
    return sum(1<<((sgn*i+shift)%6) for i in range(6) if mask>>i&1)

def orbit(mask): return frozenset(cycle_image(mask,sgn,shift) for sgn in (-1,1) for shift in range(6))

def check():
    assert poly_eval(P,LOW)>0 and poly_eval(P,HIGH)<0
    assert LOW*LOW>Q(1,3)
    der=[i*P[i] for i in range(1,len(P))]
    assert poly_eval(der,LOW)+lipschitz(der)*(HIGH-LOW)<0
    assert len(weights)==6
    allorbits=[orbit(mask) for mask in weights]
    assert len(set(allorbits))==6
    assert len(set.union(*map(set,allorbits)))==32
    assert all(all(mask.bit_count()<=4 for mask in oo) for oo in allorbits)
    assert all(positive_at_root(coeff) for coeff in weights.values())
    mass={}
    for mask,coeff in weights.items():
        for state in orbit(mask):
            assert state not in mass
            mass[state]=scale(coeff,Q(1,len(orbit(mask))))
    def moment(mask):
        acc=[Q(0)]
        for s,pr in mass.items():
            if s&mask==mask:acc=add(acc,pr)
        return acc
    assert sub(moment(0),[1])==[Q(0)]
    for i in range(6):assert sub(moment(1<<i),[0,1])==[Q(0)]
    edgeverts=[{i,(i+1)%6} for i in range(6)]
    pairs=[]
    for A in range(1,1<<6):
        Va=set().union(*(edgeverts[i] for i in range(6) if A>>i&1))
        for B in range(A+1,1<<6):
            Vb=set().union(*(edgeverts[i] for i in range(6) if B>>i&1))
            if not Va&Vb:
                assert sub(moment(A|B),mul(moment(A),moment(B)))==[Q(0)],(A,B)
                pairs.append((A,B))
    assert len(pairs)==36
    print('PASS: real algebraic root bracket, positive orbit weights, exact mass normalization, 6 equal edge marginals and',len(pairs),'vertex-disjoint moment identities; 32 configurations all disconnected')
    print('orbit masses:')
    for mask,v in weights.items():print(f'{mask:06b}',len(orbit(mask)),float(poly_eval(v,Q(597345547414504,10**15))))

if __name__=='__main__':check()
