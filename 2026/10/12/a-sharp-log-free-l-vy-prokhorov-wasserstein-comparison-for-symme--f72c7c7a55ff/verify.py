#!/usr/bin/env python3
import math

def mass(r,k):
    if r == 0.0:
        return 1.0 if k == 0 else 0.0
    return (1.0-r)/(1.0+r) * (r ** abs(k))

def eabs(r):
    return 2.0*r/(1.0-r*r)

def cutoff(B):
    return B/(math.sqrt(1.0+B*B)+1.0)

def dlp_formula(r,s):
    return 2.0*(s-r)/((1.0+r)*(1.0+s))

def w1_formula(r,s):
    return 2.0*(s/(1.0-s*s)-r/(1.0-r*r))

def ratio_formula(r,s):
    return (1.0+r*s)/((1.0-r)*(1.0-s))

def sharp_constant(B):
    return 1.0+B*B+B*math.sqrt(1.0+B*B)

def cdf(r,k):
    if k >= 0:
        return 1.0 - (r ** (k+1))/(1.0+r)
    j = -k
    return (r ** j)/(1.0+r)

maxerr = 0.0
for B in (0.1,0.25,0.5,0.75,1.0):
    R = cutoff(B)
    assert abs(eabs(R)-B) < 5e-15
    assert R <= math.sqrt(2.0)-1.0 + 1e-15
    pairs = [
        (0.0, 0.25*R),
        (0.1*R, 0.6*R),
        (0.4*R, 0.9*R),
        (0.99*R, R),
    ]
    for r,s in pairs:
        assert 0 <= r < s <= R + 1e-15
        # Single crossing: center decreases, every tested noncentral mass increases.
        assert mass(r,0) > mass(s,0)
        for k in range(1,80):
            assert mass(r,k) < mass(s,k) + 1e-18
        # Direct total-variation mismatch and CDF-sum W1, with negligible tails.
        K = 300
        dlp_direct = 0.5*sum(abs(mass(r,k)-mass(s,k)) for k in range(-K,K+1))
        w1_direct = sum(abs(cdf(r,k)-cdf(s,k)) for k in range(-K,K+1))
        de = abs(dlp_direct-dlp_formula(r,s))
        we = abs(w1_direct-w1_formula(r,s))
        re = abs(w1_formula(r,s)/dlp_formula(r,s)-ratio_formula(r,s))
        maxerr = max(maxerr,de,we,re)
        assert de < 1e-12 and we < 1e-12 and re < 1e-12
        assert ratio_formula(r,s) <= sharp_constant(B) + 1e-12

# Sharpness at B=1 through a coalescing pair at the boundary.
B=1.0
R=cutoff(B)
vals=[]
for n in (10,100,1000,10000):
    r=R*(1.0-1.0/n)
    vals.append(ratio_formula(r,R))
assert vals == sorted(vals)
assert sharp_constant(1.0) == 2.0+math.sqrt(2.0)
assert abs(vals[-1]-sharp_constant(1.0)) < 4e-4
print(f"VERIFY_OK B1_constant={sharp_constant(1.0):.15f} max_formula_error<1e-12")
