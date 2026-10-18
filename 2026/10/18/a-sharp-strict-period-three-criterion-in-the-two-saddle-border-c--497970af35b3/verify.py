"""Exact-rational spot checks for period-three itineraries of the planar border-collision normal form."""
from fractions import Fraction as Q


def coefficients(a,d,b,e,word):
    if word == 'LLR':
        tr = a*a*b-a*d-a*e-b*d
        det = d*d*e
        nums = (a*b+a*e+b+d*e-d+1,
                a*b+a+b*d+d*e-e+1,
                a*a+a*d+a+d*d-d+1)
    elif word == 'LRR':
        tr = a*b*b-a*e-b*d-b*e
        det = d*e*e
        nums = (b*b+b*e+b+e*e-e+1,
                a*b+a+b*d+d*e-e+1,
                a*b+a*e+b+d*e-d+1)
    else:
        raise ValueError(word)
    return tr,det,1-tr+det,nums


def step(z,a,d,b,e):
    x,y = z
    t,k = (a,d) if x<0 else (b,e)
    return (t*x+y+1, -k*x)


def cycle_test(a,d,b,e,word):
    tr,det,den,nums=coefficients(a,d,b,e,word)
    if not den:
        return
    xs=[v/den for v in nums]
    # Before the initial L phase, the last phase is R in both cyclic words.
    z=(xs[0],-e*xs[-1])
    for j,letter in enumerate(word):
        if (z[0]<0) != (letter=='L') or z[0] != xs[j]:
            # Only test strict admissible symbol sequences.
            return
        z=step(z,a,d,b,e)
    assert z==(xs[0],-e*xs[-1])


witness=(Q(7,5), Q(1,3), Q(-16,5), Q(-4))
a,d,b,e=witness
tr,det,den,nums=coefficients(*witness,'LLR')
assert (tr,det,den)==(Q(-9,125),Q(-4,9),Q(706,1125))
xs=tuple(v/den for v in nums)
assert xs==(Q(-7845,353),Q(-270,353),Q(2590,353))
assert a>abs(1+d) and b < -abs(1+e)
assert xs[0]<0 and xs[1]<0 and xs[2]>0
assert 1-tr+det>0 and 1+tr+det>0 and abs(det)<1
z=(xs[0],-e*xs[2])
assert z==(Q(-7845,353),Q(10360,353))
assert step(z,*witness)==(Q(-270,353),Q(2615,353))
assert step(step(z,*witness),*witness)==(Q(2590,353),Q(90,353))
assert step(step(step(z,*witness),*witness),*witness)==z
for a in [Q(7,5),Q(3,2),Q(2),Q(5,2)]:
    for d in [Q(-1,2),Q(1,3),Q(2,3)]:
        for b in [Q(-3),Q(-4),Q(-5,2)]:
            for e in [Q(-4),Q(-1,2),Q(1,4)]:
                if a<=abs(1+d) or b>=-abs(1+e):
                    continue
                for word in ('LLR','LRR'):
                    cycle_test(a,d,b,e,word)
                q=b*(b+e+1)+(e*e-e+1)
                assert q>0
print('EXACT_PERIOD3_CYCLE_AND_SCHUR_CHECKS_OK')
