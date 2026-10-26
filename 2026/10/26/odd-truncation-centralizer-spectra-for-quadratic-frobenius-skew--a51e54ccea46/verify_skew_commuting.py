"""Independent finite-field checks of quadratic-Galois skew-truncation commuting laws.
No network access or external packages are required.
Run: python verify_skew_commuting.py
"""
from collections import Counter
from itertools import product
from fractions import Fraction

class FiniteField:
    def __init__(self, p, polynomial):
        self.p=p; self.d=len(polynomial)-1; self.mod=polynomial;self.q=p**self.d
        def digits(x):
            return [(x//(p**i))%p for i in range(self.d)]
        rep=[digits(i) for i in range(self.q)]
        self.add=[[sum(((rep[i][j]+rep[k][j])%p)*p**j for j in range(self.d)) for k in range(self.q)] for i in range(self.q)]
        self.neg=[sum(((-rep[i][j])%p)*p**j for j in range(self.d)) for i in range(self.q)]
        self.mul=[]
        for i in range(self.q):
            row=[]
            for k in range(self.q):
                c=[0]*(2*self.d-1)
                for j in range(self.d):
                    for h in range(self.d): c[j+h]=(c[j+h]+rep[i][j]*rep[k][h])%p
                for e in range(2*self.d-2,self.d-1,-1):
                    v=c[e]
                    if v:
                        for h in range(self.d): c[e-self.d+h]=(c[e-self.d+h]-v*self.mod[h])%p
                row.append(sum(c[j]*p**j for j in range(self.d)))
            self.mul.append(row)
    def pow(self,a,k):
        z=1
        while k:
            if k&1:z=self.mul[z][a]
            a=self.mul[a][a];k//=2
        return z

def ring_commutes(a,b,F,s):
    n=len(a); add=F.add; mul=F.mul; neg=F.neg
    sa=[a, [F.pow(x,s) for x in a]]
    sb=[b, [F.pow(x,s) for x in b]]
    for d in range(1,n):
        z=0
        for i in range(d+1):
            j=d-i
            z=add[z][mul[a[i]][sb[i%2][j]]]
            z=add[z][neg[mul[b[i]][sa[i%2][j]]]]
        if z:return False
    return True

def predicted(s,a):
    m=2*a+1
    ring_size=s**(2*m)
    Z=s**(a+2)
    counts=Counter({ring_size:Z})
    for t in range(a):
        centralizer=s**(2*a+2+2*t)
        counts[centralizer]+=Z*(s**(3*(a-t))-s**(3*(a-t-1)))
    assert sum(counts.values())==ring_size
    prob=Fraction(s**(-0),1) if False else (Fraction(s**(-2*a),1) if False else
        Fraction(s*s+s+1,s**(2*a+2))-Fraction(s+1,s**(3*a+2)))
    assert prob == Fraction(sum(size*number for size,number in counts.items()),ring_size**2)
    return counts,prob

def exhaustive(F,s,n):
    elements=list(product(range(F.q),repeat=n))
    sizes=Counter()
    for a in elements:
        sizes[sum(ring_commutes(a,b,F,s) for b in elements)]+=1
    target,prob=predicted(s,(n-1)//2)
    assert sizes==target,(s,n,sizes,target)
    pairs=sum(m*c for m,c in sizes.items())
    assert Fraction(pairs,len(elements)**2)==prob
    print(f'EXHAUSTIVE s={s} n={n} elements={len(elements)} classes={sorted(sizes.items())} commuting_pairs={pairs} probability={prob}')

if __name__=='__main__':
    f4=FiniteField(2,[1,1,1]);f9=FiniteField(3,[1,0,1]);f16=FiniteField(2,[1,1,0,0,1])
    for f,s,n in ((f4,2,3),(f4,2,5),(f9,3,3)):
        exhaustive(f,s,n)
    # The extension-field fixed subfield of F16 has order four. Test the
    # complete centralizers of a deterministic 12-element sample in R_3,
    # including central and noncentral elements, against the theorem.
    f=f16;s=4;n=3
    center_samples=[];outer_samples=[]
    for a in product(range(f.q),repeat=n):
        # Directly test whether this element commutes with generators theta and x.
        t=(2,0,0);x=(0,1,0)
        is_center=ring_commutes(a,t,f,s) and ring_commutes(a,x,f,s)
        if is_center and len(center_samples)<6:center_samples.append(a)
        if not is_center and len(outer_samples)<6:outer_samples.append(a)
        if len(center_samples)==6 and len(outer_samples)==6:break
    assert len(center_samples)==len(outer_samples)==6
    all_b=list(product(range(f.q),repeat=n))
    target,_=predicted(s,1)
    for a in center_samples+outer_samples:
        c=sum(ring_commutes(a,b,f,s) for b in all_b)
        assert c==(f.q**n if a in center_samples else s**4),(a,c)
    print('F16 CENTRALIZER SAMPLES PASSED 12; expected histogram:',sorted(target.items()))
    print('ALL_SKEW_TRUNCATION_CHECKS_PASSED')
