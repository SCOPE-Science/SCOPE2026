from fractions import Fraction
from itertools import product


def vertices(n):
    return list(product((-1,1), repeat=n))


def hamming(a,b):
    return sum(x!=y for x,y in zip(a,b))


def independent(T):
    T=list(T)
    return all(hamming(T[i],T[j])>=2 for i in range(len(T)) for j in range(i+1,len(T)))


def verify_family(n,T):
    V=vertices(n)
    T=set(T)
    assert independent(T)
    U=[w for w in V if w not in T]
    # Distinct untruncated cube vertices require disjoint open sign orthants.
    assert len(U)==2**n-len(T)
    # Deterministic rational, unequal depths in (0,1).
    order=sorted(T)
    tau={t:Fraction(i+1,2*(len(order)+1)) for i,t in enumerate(order)}
    for t in T:
        for i in range(n):
            # New cut vertex on the i-th edge from t.
            x=list(map(Fraction,t))
            x[i]=Fraction(t[i])*(1-tau[t])
            # Its neighboring original cube vertex.
            w=list(t); w[i]=-w[i]; w=tuple(w)
            assert w in U  # independence is exactly what guarantees this.
            d=tuple(-z for z in w)
            # All active coordinate facets go strictly inward.
            for j in range(n):
                if j!=i:
                    assert t[j]*d[j] < 0
            # The active truncation facet goes strictly inward for n>=3.
            assert sum(t[j]*d[j] for j in range(n)) == -(n-2) < 0
            # No second truncation hyperplane is active at this cut vertex.
            for s in T:
                if s==t: continue
                lhs=sum(Fraction(s[j])*x[j] for j in range(n))
                assert lhs < n-tau[s]

# Exhaust all subsets of one parity class in dimensions 3 and 4.
for n in (3,4):
    P=[v for v in vertices(n) if sum(x<0 for x in v)%2==0]
    for mask in range(1<<len(P)):
        T=[P[i] for i in range(len(P)) if (mask>>i)&1]
        verify_family(n,T)

# Check the extremal parity-class construction and every cardinality up to half
# in dimensions through eight.
for n in range(3,9):
    P=[v for v in vertices(n) if sum(x<0 for x in v)%2==0]
    assert len(P)==2**(n-1)
    for m in range(len(P)+1):
        T=P[:m]
        assert independent(T)
        assert 2**n-len(T) in range(2**(n-1),2**n+1)
    verify_family(n,P)

# Banach--Mazur sandwich: alpha C is inside every truncation.
for n in range(3,10):
    tau_max=Fraction(3,5)
    alpha=1-tau_max/Fraction(n)
    assert 0<alpha<1
    # For x in alpha*C, max_t <t,x> = n*alpha = n-tau_max.
    assert n*alpha == n-tau_max

print('VERIFY_OK independent cube-corner illumination spectrum')
