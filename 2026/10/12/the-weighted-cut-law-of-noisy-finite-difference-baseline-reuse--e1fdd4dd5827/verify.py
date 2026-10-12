"""Exact-arithmetic checks for covariance-cut design in noisy finite differences.

Run: python verify.py. Python 3 standard library only.
The mathematical proof, including asymptotic complexity, is in RESULT.md;
finite tests validate the formulas but do not replace the general proof.
"""
from fractions import Fraction as F
from itertools import product, combinations

checks = 0

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def quad(H,x):
    return dot(x,[dot(row,x) for row in H])/2

def direct_mean(H,labels,x,h,eta):
    n=len(H)
    r=max(labels)+1
    total=F(0)
    for bits in product((-1,1),repeat=n+r):
        perturb=bits[:n]
        base=bits[n:]
        der=[dot(row,x)+h*H[i][i]/2+F(perturb[i]-base[labels[i]],1)/h
             for i,row in enumerate(H)]
        xn=[x[i]-eta*der[i] for i in range(n)]
        fx=quad(H,xn)
        total+=fx
    return total/(2**(n+r))

def direct_gradient_mse(H,labels,h):
    n=len(H)
    r=max(labels)+1
    total=F(0)
    for bits in product((-1,1),repeat=n+r):
        errors=[h*H[i][i]/2+F(bits[i]-bits[n+labels[i]],1)/h
                for i in range(n)]
        total+=dot(errors,errors)
    return total/(2**(n+r))

def formula(H,labels,x,h,eta):
    n=len(H)
    mu=[dot(row,x)+h*H[i][i]/2 for i,row in enumerate(H)]
    y=[x[i]-eta*mu[i] for i in range(n)]
    v=F(0)
    for i in range(n):
        v+=H[i][i]
        for j in range(n):
            if labels[i]==labels[j]:
                v+=H[i][j]
    return quad(H,y)+eta**2/(2*h*h)*v

def cut(H,labels):
    n=len(H)
    return sum((H[i][j] for i in range(n) for j in range(i+1,n)
                if labels[i]!=labels[j]),F(0))

H2=[[F(1),-F(3,5)],[-F(3,5),F(1)]]
H3=[[F(2), F(1,3), -F(1,4)],
    [F(1,3), F(3), F(1,5)],
    [-F(1,4), F(1,5), F(2)]]
for H in [H2,H3]:
    n=len(H)
    x=[F(i+1,7) for i in range(n)]
    for h in (F(1,2),F(2,3)):
        for eta in (F(1,3),F(3,4)):
            for labels in product(range(2),repeat=n):
                if not set(labels)=={0,1} and any(labels):
                    continue
                labels=tuple(labels)
                f=direct_mean(H,labels,x,h,eta)
                g=formula(H,labels,x,h,eta)
                assert f==g,(H,labels,h,eta,f,g)
                checks+=1
                all_label=(0,)*n
                if labels==all_label:
                    continue
                diff=g-formula(H,all_label,x,h,eta)
                assert diff==-eta**2/h**2*cut(H,labels)
                checks+=1

# Contrary to naive intuition, an extra independent baseline call can
# strictly worsen expected objective when the Hessian cross term is negative.
h=F(1,2);eta=F(1,3);x=[F(0),F(0)]
delta=formula(H2,(0,1),x,h,eta)-formula(H2,(0,0),x,h,eta)
assert delta==eta**2/h**2*F(3,5)>0
checks+=1

# Concrete exact witness: one baseline has lower quadratic risk than two.
# However the Euclidean gradient MSE is identical because only the
# variances (not the cross-covariances) enter its trace.
assert formula(H2,(0,0),[F(0),F(0)],F(1),F(1))==F(3,2)
checks+=1
assert formula(H2,(0,1),[F(0),F(0)],F(1),F(1))==F(21,10)
checks+=1
for lab in ((0,0),(0,1)):
    # Squared bias = 1/2; trace covariance = 4. Direct enumeration
    # of the gradient error checks the claimed grouping invariance.
    mse=direct_gradient_mse(H2,lab,F(1))
    assert mse==F(9,2)
    checks+=1

# All simple graphs of size <=5: exact partition optimum equals MAXCUT.
# A diagonal-dominant graph Hessian stays positive definite.
for n in range(2,6):
    pairs=list(combinations(range(n),2))
    for bitset in range(1<<len(pairs)):
        eps=F(1,10*n)
        E={pairs[t] for t in range(len(pairs)) if bitset & (1<<t)}
        H=[[F(int(i==j)) + (eps if (min(i,j),max(i,j)) in E else 0)
            for j in range(n)] for i in range(n)]
        best=-1
        min_within=None
        for labs in product((0,1),repeat=n):
            if labs[0]: continue # quotient out the complement symmetry
            ncut=sum(int(labs[i]!=labs[j]) for i,j in E)
            within=sum(int(labs[i]==labs[j]) for i,j in E)
            best=max(best,ncut)
            value=within
            if min_within is None or value<min_within: min_within=value
            assert cut(H,labs)==eps*ncut
            checks+=1
        assert len(E)-best==min_within
        checks+=1
print('PASS',checks,'exact rational checks')
