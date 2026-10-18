"""Verify finite Gödel-chain order-type violation polynomials.
Standard library only. Run: python verify.py
"""
from itertools import product
from math import comb, factorial
import random

Z=('z',); O=('o',)
def V(i): return ('v',i)
def And(a,b): return ('and',a,b)
def Or(a,b): return ('or',a,b)
def Imp(a,b): return ('imp',a,b)
def Neg(a): return Imp(a,Z)

def evaluate(t, vals, n):
    op=t[0]
    if op=='z': return 0
    if op=='o': return n-1
    if op=='v': return vals[t[1]]
    a=evaluate(t[1],vals,n); b=evaluate(t[2],vals,n)
    if op=='and': return min(a,b)
    if op=='or': return max(a,b)
    if op=='imp': return (n-1 if a<=b else b)
    raise ValueError(op)

def pattern(vals, n):
    interior=sorted(set(v for v in vals if 0<v<n-1))
    rank={v:i+1 for i,v in enumerate(interior)}
    return (len(interior),tuple(0 if v==0 else -1 if v==n-1 else rank[v] for v in vals))

def coefficients(t,s,k):
    # Canonical chain C_(k+2) realizes every order type.
    n=k+2
    discovered={}
    for vals in product(range(n), repeat=k):
        d,p=pattern(vals,n)
        violation=evaluate(t,vals,n)!=evaluate(s,vals,n)
        if (d,p) in discovered:
            assert discovered[d,p]==violation
        discovered[d,p]=violation
    cs=[0]*(k+1)
    for (d,_),bad in discovered.items(): cs[d]+=int(bad)
    return cs,len(discovered)

def independent_brute(t,s,k,n):
    # Counts assignments directly without order-type aggregation.
    return sum(evaluate(t,vals,n)!=evaluate(s,vals,n)
               for vals in product(range(n),repeat=k))

def predict(cs,n): return sum(c*comb(n-2,d) for d,c in enumerate(cs) if d<=n-2)

def rngterm(rng,k,dep):
    if dep==0 or rng.randrange(6)==0:
        return rng.choice([Z,O]+[V(i) for i in range(k)])
    a=rngterm(rng,k,dep-1)
    b=rngterm(rng,k,dep-1)
    return rng.choice((And,Or,Imp))(a,b)

def main():
    tests=[('double-negation-top',Neg(Neg(V(0))),O,1,[1,0]),
           ('double-negation-elimination',Neg(Neg(V(0))),V(0),1,[0,1]),
           ('material-implication',Imp(V(0),V(1)),Or(Neg(V(0)),V(1)),2,None),
           ('reflexivity',Imp(V(0),V(0)),O,1,[0,0]),
           ('excluded-middle',Or(V(0),Neg(V(0))),O,1,None),
           ('comparison',Imp(V(0),V(1)),Imp(V(1),V(0)),2,None)]
    random.Random(72026)
    rng=random.Random(1022026)
    for k in (1,2,3):
        for i in range(65):
            tests.append((f'generated-k{k}-{i}',rngterm(rng,k,3),rngterm(rng,k,3),k,None))
    total=0; patterns=0
    examples={}
    for name,t,s,k,want in tests:
        cs,p=coefficients(t,s,k)
        if want is not None: assert cs==want,(name,cs,want)
        examples[name]=cs
        patterns+=p
        for n in range(2,10):
            brute=independent_brute(t,s,k,n)
            assert brute==predict(cs,n),(name,k,n,cs,brute,predict(cs,n))
            total+=n**k
        assert cs[k] <=factorial(k)
        if cs[k]==0 and sum(cs)>0:
            assert predict(cs,1000000)<1000000**k
    # Independent product test: explicit enumeration of pairs of components.
    x=V(0); y=V(1)
    t=Imp(x,y); s=Or(Neg(x),y)
    for a,b in product(range(2,6),repeat=2):
        brute=sum((evaluate(t,(i1,j1),a),evaluate(t,(i2,j2),b)) !=
                  (evaluate(s,(i1,j1),a),evaluate(s,(i2,j2),b))
                  for i1,j1,i2,j2 in product(range(a),range(a),range(b),range(b)))
        ca,_=coefficients(t,s,2)
        va=predict(ca,a); vb=predict(ca,b)
        expect=(a*b)**2-(a*a-va)*(b*b-vb)
        assert brute==expect,(a,b,brute,expect)
    print('VERIFY_OK equations=%d tuple_assignments=%d canonical_patterns=%d product_pairs=16'%(len(tests),total,patterns))
    for key in ('double-negation-top','double-negation-elimination','material-implication','reflexivity','excluded-middle','comparison'):
        print(key,examples[key])

if __name__=='__main__': main()
