"""Symbolically certify the local Taylor identities used in the proof."""
import sympy as s
A,B,C,D=s.symbols('A B C D', integer=True)
r=s.symbols('r', integer=True, even=True)
X=(A,B,C,D)
perms=[]
import itertools
for perm in itertools.permutations(range(4)):
    parity=(-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    perms.append((perm,parity))

def coefficient(signs,k):
    rows=(0,1,2,r)
    terms=[]
    for pm,sgn in perms:
        vec=[(s.Integer(signs[pm[i]])**rows[i], X[pm[i]], rows[i]) for i in range(4)]
        for ks in itertools.product(range(k+1), repeat=4):
            if sum(ks)!=k: continue
            factor=sgn
            for i,(sign,x,pow) in enumerate(vec):
                factor*=sign*s.binomial(pow,ks[i])*x**ks[i]
            terms.append(factor)
    return s.factor(s.expand(sum(terms)))

def verify():
    e3=coefficient((1,1,1,-1),3)
    assert s.simplify(e3-2*r*(r-2)*(A-B)*(A-C)*(B-C))==0,e3
    e3b=coefficient((1,1,-1,-1),3)
    assert s.simplify(e3b+2*r*(r-2)*(A-B)*(C-D)*(A+B-C-D))==0,e3b
    e4=coefficient((1,1,-1,-1),4)
    subs=s.factor(e4.subs(D,A+B-C))
    goal=s.Rational(2,3)*r*(r-2)*(r-4)*(A-B)*(C-D)*(A-C)*(B-C)
    assert s.simplify(subs-goal.subs(D,A+B-C))==0,(subs,goal)
    for signs in ((1,1,1,-1),(1,1,-1,-1)):
        for k in (0,1,2): assert coefficient(signs,k)==0,(signs,k)
    print('PASS: exact symbolic t^0,t^1,t^2 vanish; t^3,t^4 identities confirmed')
if __name__=='__main__':verify()
