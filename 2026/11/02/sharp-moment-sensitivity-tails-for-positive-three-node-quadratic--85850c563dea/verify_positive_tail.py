"""Reproduce exact identities and numerical diagnostics for the quadratic positive-rule tail.

Python 3 standard library. The analytic limit proof is in RESULT.md;
finite checks below are corroboration rather than a substitute for that proof.
"""
from fractions import Fraction as Q
import math, random

def inverse_rows(a,b,c):
    xs=(a,b,c)
    ans=[]
    for i,x in enumerate(xs):
        y,z=(xs[j] for j in range(3) if j!=i)
        den=(x-y)*(x-z)
        ans.append((y*z/den,-(y+z)/den,1/den))
    return ans

def moments_weights(a,b,c):
    return tuple(row[0]+row[2]/3 for row in inverse_rows(a,b,c))

def frobenius_sq(a,b,c):
    return sum(float(v*v) for row in inverse_rows(a,b,c) for v in row)

def exact_identity_checks():
    xs=[Q(-1),Q(-4,5),Q(-2,3),Q(-1,2),Q(-1,5),Q(0),Q(1,5),Q(1,2),Q(2,3),Q(4,5),Q(1)]
    total=0
    positives=0
    for i,a in enumerate(xs):
        for j in range(i+1,len(xs)):
            for c in xs[j+1:]:
                b=xs[j]
                rows=inverse_rows(a,b,c)
                for p,row in enumerate(rows):
                    for k,x in enumerate((a,b,c)):
                        got=sum(x**h*row[h] for h in range(3))
                        assert got==(1 if k==p else 0)
                weights=moments_weights(a,b,c)
                for p,goal in enumerate((Q(1),Q(0),Q(1,3))):
                    assert sum(weights[k]*(a,b,c)[k]**p for k in range(3))==goal
                criterion=(a*c<Q(-1,3) and b>Q(-1,3)/c and b<Q(-1,3)/a)
                assert (min(weights)>0)==criterion
                total+=1
                if criterion: positives+=1
    return total, positives

def c_squared(s):
    return 2*(9*s**4+4*s*s+1)/(3*s*s+1)**2

def k_density(s):
    left=c_squared(s)/(4*s*s)
    right=1/(2*s*s)-1/(3*s*s+1)**2
    assert abs(left-right) <= 1e-11
    return left

def tail_integral_numeric(n=150000):
    step=(1-1/3)/n
    return step*sum(k_density(1/3+(i+.5)*step) for i in range(n))

def near_collision_tests():
    errs=[]
    for s in (Q(2,5),Q(1,2),Q(2,3),Q(4,5)):
        for h in (Q(1,100),Q(1,500),Q(1,2500)):
            a=-s; b=a+h
            c=1/(3*s)+h/(6*s*s)
            assert min(moments_weights(a,b,c))>0
            limit=float(h*h)*frobenius_sq(a,b,c)
            errs.append((float(s),float(h),abs(limit-float(c_squared(s)))))
    return errs

def strip_estimate(t, n=180000):
    """Importance-integrate left collision strip, multiply by reflection symmetry."""
    rng=random.Random(99)
    emax=6/t
    accum=0.0
    for _ in range(n):
        s=1/3+(2/3)*rng.random()
        e=emax*rng.random()
        if e>=s:continue
        a=-s; b=a+e
        lo=1/(3*s); hi=min(1.,1/(3*(s-e)))
        width=max(0,hi-lo)
        if not width:continue
        c=lo+width*rng.random()
        if frobenius_sq(a,b,c)>t*t:
            accum+=width
    # 3/4 ordered density, times 2 symmetric strips, uniform s,e sampling width (2/3)*emax
    return t*t*(3/4)*2*(2/3)*emax*accum/n

if __name__=='__main__':
    cnt,pos=exact_identity_checks()
    assert cnt>=150 and pos>0
    p_pos=math.log(3)/2-1/3
    k=1-math.pi*math.sqrt(3)/36
    k_numeric=tail_integral_numeric(25000)
    assert abs(k-k_numeric)<1e-8,(k,k_numeric)
    errs=near_collision_tests()
    assert max(error for s,h,error in errs if h==.0004)<.007
    print('exact-rational triples checked',cnt,'positive',pos)
    print('positive-event probability',f'{p_pos:.12f}')
    print('unconditional tail coefficient',f'{k:.12f}','numeric integral',f'{k_numeric:.12f}')
    print('conditional tail coefficient',f'{k/p_pos:.12f}')
    print('coalescence error largest at smallest h',max(error for s,h,error in errs if h==.0004))
    for t in (100,200,400):
        est=strip_estimate(t)
        print('importance-integrated t^2 probability at threshold',t,'=',f'{est:.8f}', 'analytic K=',f'{k:.8f}')
        assert abs(est-k)<.055
    print('CHECK_OK')
