from itertools import product
from math import log

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
        self.p=2 if q in (2,4) else 3
        self.f=2 if q==4 else 1
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0|(c1<<1)

def addv(F,a,b): return tuple(F.add(x,y) for x,y in zip(a,b))
def smul(F,c,a): return tuple(F.mul(c,x) for x in a)

def span_prime(F,gens):
    z=(0,)*len(gens[0]) if gens else ()
    S={z}
    for g in gens:
        S={addv(F,u,smul(F,c,g)) for u in S for c in range(F.p)}
    return frozenset(S)

def all_prime_subspaces(F,dim):
    zero=(0,)*dim
    vectors=list(product(range(F.q),repeat=dim))
    # For q=4, additive vectors are still F2^4 when dim=2; scalar entries encode two F2 bits.
    spaces={frozenset([zero])}
    frontier=[frozenset([zero])]
    while frontier:
        U=frontier.pop()
        for v in vectors:
            if v in U: continue
            W=frozenset(addv(F,u,smul(F,c,v)) for u in U for c in range(F.p))
            if W not in spaces:
                spaces.add(W); frontier.append(W)
    return spaces

def field_span(F,U,dim):
    S={(0,)*dim}
    for v in U:
        S |= {smul(F,c,v) for c in range(F.q)}
    changed=True
    while changed:
        changed=False
        old=list(S)
        for a in old:
            for b in old:
                c=addv(F,a,b)
                if c not in S: S.add(c); changed=True
    return frozenset(S)

def symp(F,v,w,n):
    s=0
    for i in range(n):
        s=F.add(s,F.mul(v[i],w[n+i]))
        # subtraction: same as add in char 2, otherwise add negative
        t=F.mul(w[i],v[n+i])
        if F.p==2: s=F.add(s,t)
        else: s=F.add(s,(-t)%F.p)
    return s

def ilog(size,base):
    d=0; x=1
    while x<size: x*=base; d+=1
    assert x==size
    return d

def check(n,q):
    F=Field(q); dim=2*n
    vectors=list(product(range(q),repeat=dim))
    spaces=all_prime_subspaces(F,dim)
    maxm=q**(2*n+2)
    maximal=0
    for U in spaces:
        S=field_span(F,U,dim)
        s=ilog(len(U),F.p)
        d=ilog(len(S),q)
        perp={v for v in vectors if all(symp(F,v,w,n)==0 for w in U)}
        assert len(perp)==q**(2*n-d)
        m=(q*len(U))*(q*len(perp))
        assert m==maxm*(F.p**(s-F.f*d))
        field_linear=(len(U)==len(S))
        assert (m==maxm)==field_linear
        if field_linear: maximal+=1
    # number of F_q-subspaces = sum Gaussian binomials; here compare by direct classification
    qspaces={field_span(F,U,dim) for U in spaces}
    assert maximal==len(qspaces)
    if F.f==1:
        assert maximal==len(spaces)
    else:
        assert maximal<len(spaces)
        # Explicit monotonicity obstruction U=F_p*v.
        v=next(v for v in vectors if any(v))
        U=frozenset(smul(F,c,v) for c in range(F.p))
        S=field_span(F,U,dim)
        assert len(U)<len(S)
        m=(q*len(U))*(q*q**(2*n-1))
        assert m==maxm*(F.p**(1-F.f))
        assert m<maxm
    print({"n":n,"q":q,"additive_subspaces":len(spaces),
           "field_subspaces":len(qspaces),"max_measure":maxm})

for case in [(2,2),(2,3),(1,4)]:
    check(*case)
print("VERIFY_OK")
