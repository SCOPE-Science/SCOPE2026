"""Exact checks of a first-return generating function for an induced interval map.
No external packages required.
"""
from fractions import Fraction as Q
from math import comb, isclose, sqrt, pi

def transition(lam, i, j):
    if i <= 3:
        start=1
    elif i == 4:
        start=2
    else:
        start=i-1
    if j < start: return Q(0)
    return (1-lam)*lam**(j-start)

def first_return_via_states(lam, horizon):
    # Exact within horizon: states above horizon+2 cannot return in time.
    max_state=horizon+2
    b_mass=sum((1-lam)*lam**(i-1) for i in (1,2,3))
    weights={i:((1-lam)*lam**(i-1))/b_mass for i in (1,2,3)}
    out=[]
    for step in range(1,horizon+1):
        new={}
        hit=Q(0)
        for i,prob in weights.items():
            if prob==0: continue
            for j in range(1,max_state+1):
                transition_p=transition(lam,i,j)
                if not transition_p: continue
                m=prob*transition_p
                if j<=3: hit+=m
                else: new[j]=new.get(j,Q(0))+m
        out.append(hit)
        weights=new
    return out

def coeff_formula(lam,n):
    if n==1: return 1-lam**3
    total=sum((j+1)*comb(2*n-j-4,n-j-2)*lam**j for j in range(n-1))
    return (lam**(n+1)*(1-lam**2)*(1-lam)**(n-1)*total)/Q(n-1)

count=0
for lam in [Q(1,5), Q(1,3), Q(1,2), Q(3,5), Q(4,5)]:
    vals=first_return_via_states(lam, 24)
    for n,p in enumerate(vals,1):
        q=coeff_formula(lam,n)
        assert p==q, (lam,n,p,q)
        count+=1
    if lam<Q(1,2):
        paper_mass=(1+lam)*(1-2*lam)/(lam**3-2*lam**2-lam+1)
        mean=1+lam**3/((1+lam)*(1-2*lam))
        assert mean*paper_mass==1
    else:
        escape=lam**2*(2*lam-1)/(lam**2-lam+1) if lam>Q(1,2) else Q(0)
        assert escape>=0
# Independently derive transition probabilities from exact affine image ranges.
for lam in [Q(1,5), Q(1,3), Q(1,2), Q(3,5), Q(4,5)]:
    for i in range(1,18):
        left,right=lam**i,lam**(i-1)
        if i==1: shift,den=lam,1-lam
        elif i==2: shift,den=lam**2,lam*(1-lam)
        elif i==3: shift,den=lam**3,lam**2*(1-lam)
        elif i==4: shift,den=lam**4,lam**2*(1-lam)
        else: shift,den=lam**i,lam*(1-lam)
        assert (left-shift)/den == 0
        height=(right-shift)/den
        for j in range(1,29):
            bottom,top=lam**j,lam**(j-1)
            length=max(Q(0),min(height,top)-bottom)
            from_geometry=length/(height)*1 if height else Q(0)
            assert from_geometry==transition(lam,i,j),(lam,i,j)
print('PASS',count,'exact rational coefficient tests, 5*17*28 affine-image comparisons, and stationary return consistency')
for lam in [0.3,0.5,0.7]:
    R=4*lam*(1-lam)
    c=lam*(1+lam)/(4*sqrt(pi)*(2-lam)**2)
    n=100
    p=float(coeff_formula(Q(str(lam)),n))
    print('asymptotic ratio',lam,p/(c*R**n*n**(-1.5)))
