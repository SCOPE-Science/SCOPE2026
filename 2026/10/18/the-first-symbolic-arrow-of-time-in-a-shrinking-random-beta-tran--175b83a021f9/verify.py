"""Exact finite-state and universal linear-constraint checks for a renewal-coded beta map.
Only uses Python's standard library; infinite limits are established in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from decimal import Decimal, getcontext


def renewal_model(weights):
    assert set(weights) == set(range(2, max(weights) + 1))
    assert sum(weights.values()) == 1
    mu = sum(k * v for k, v in weights.items())
    states = [(b, k, j) for b in (0, 1) for k in weights for j in range(k)]
    idx = {s: i for i, s in enumerate(states)}
    dist = [weights[k] / (2*mu) for b,k,j in states]
    output = [b if j == 0 else 1-b for b,k,j in states]
    transitions = []
    for b,k,j in states:
        if j < k-1:
            transitions.append([(idx[b,k,j+1], Q(1))])
        else:
            transitions.append([(idx[c,t,0],weights[t]/2) for c in (0,1) for t in weights])
    def prob(word):
        v = dist[:]
        for c in word:
            nv = [Q(0)] * len(states)
            for i,a in enumerate(v):
                if a and output[i] == c:
                    for h,p in transitions[i]: nv[h] += a*p
            v = nv
        return sum(v)
    return prob,mu


def pivot_basis(rows, columns):
    basis={}
    for original in rows:
        r={j:Q(v) for j,v in enumerate(original) if v}
        while r:
            j=min(r)
            if j in basis:
                a=r[j]
                for k,v in basis[j].items():
                    b=r.get(k,0)-a*v
                    if b: r[k]=b
                    else: r.pop(k,None)
            else:
                a=r[j]
                basis[j]={k:v/a for k,v in r.items()}
                break
    return basis


def in_span(row, basis):
    r={j:Q(v) for j,v in enumerate(row) if v}
    while r:
        j=min(r)
        if j not in basis: return False
        a=r[j]
        for k,v in basis[j].items():
            b=r.get(k,0)-a*v
            if b: r[k]=b
            else: r.pop(k,None)
    return True


def binary_word_check(length, base_pair=None):
    words=list(product((0,1),repeat=length)); pos={w:j for j,w in enumerate(words)}; d=len(words)
    rows=[]
    for w in product((0,1), repeat=length-1):
        r=[0]*d
        for c in (0,1): r[pos[(c,)+w]]+=1; r[pos[w+(c,)]]-=1
        rows.append(r)
    for w in words:
        r=[0]*d; r[pos[w]]+=1; r[pos[tuple(1-z for z in w)]]-=1
        rows.append(r)
    basis=pivot_basis(rows,d)
    first=None; signs={}
    for w in words:
        v=w[::-1]
        if w>=v: continue
        r=[0]*d; r[pos[w]]=1; r[pos[v]]=-1
        if in_span(r,basis): signs[''.join(map(str,w))]=0; continue
        if first is None: first=r; signs[''.join(map(str,w))]=1; continue
        if in_span([r[i]-first[i] for i in range(d)],basis):sgn=1
        elif in_span([r[i]+first[i] for i in range(d)],basis):sgn=-1
        else:raise AssertionError('Two independent time-asymmetries!')
        signs[''.join(map(str,w))]=sgn
    return len(basis),first,signs

for length in range(1,5):
    rank,first,signs=binary_word_check(length)
    assert first is None, (length,signs)
rank,first,signs=binary_word_check(5)
expected={'00010':1,'00011':-1,'00110':-1,'00111':1,'01001':1,'01101':-1,'10011':1,'10111':-1}
assert {w:s for w,s in signs.items() if s} == expected,signs

checks=0
for n in range(3,10):
    weights={k:Q(k+1,(n*(n+1)//2-1)+ (n-1)) for k in range(2,n+1)}
    den=sum(range(3,n+2))
    weights={k:Q(k+1,den) for k in range(2,n+1)}
    p,mu=renewal_model(weights)
    d=(weights[2]-weights[2]**2-weights[3])/(8*mu)
    assert p((0,0,0,1,0))-p((0,1,0,0,0))==d
    for L in range(1,6):
        for w in product((0,1),repeat=L):
            sign=0 if L<5 else signs.get(''.join(map(str,w)),0)
            if L==5 and w>w[::-1]:sign=-signs.get(''.join(map(str,w[::-1])),0)
            assert p(w)-p(w[::-1]) == sign*d,(n,w,sign,d)
            checks+=1
    tv=Q(1,2)*sum(abs(p(w)-p(w[::-1])) for w in product((0,1),repeat=5))
    assert tv==8*abs(d)

getcontext().prec=65
for n in range(3,13):
    lo,hi=Decimal(1),Decimal(2)
    for _ in range(240):
        z=(lo+hi)/2
        if sum(2*z**(-k) for k in range(2,n+1))>1: lo=z
        else:hi=z
    lam=(lo+hi)/2
    q={k:2*lam**(-k) for k in range(2,n+1)}
    mu=sum(k*x for k,x in q.items())
    d=(q[2]-q[2]**2-q[3])/(8*mu)
    exact=-lam**(-(n+3))/(2*mu)
    assert abs(d-exact)<Decimal('1e-48'),(n,d,exact)

print('VERIFY_OK',checks,'rational word comparisons; reversal-constraint rank',rank,'; 10 high-precision parameter identities')
