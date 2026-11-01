"""Standalone numerical corroboration for the intrinsic diameter of a conical frustum.
Run: python3 frustum_diameter_checker.py
All distances below concern the lateral surface, including boundary circles, not end disks.
"""
import math
import random


def pair_distance(r, s, delta, inner):
    """Shortest distance for 0<=delta<=pi on annulus/conical universal cover."""
    if not (inner <= min(r, s) and 0 <= delta <= math.pi):
        raise ValueError('outside geometric domain')
    ar = math.acos(min(1., inner / r))
    ass = math.acos(min(1., inner / s))
    if delta <= ar + ass:
        return math.hypot(r - s * math.cos(delta), s * math.sin(delta))
    return (math.sqrt(max(0., r*r-inner*inner))
            + math.sqrt(max(0., s*s-inner*inner))
            + inner*(delta-ar-ass))


def diameter(outer, inner, half_cone_angle):
    """Theorem's exact diameter; cone half angle in (0,pi/2)."""
    phi = math.pi * math.sin(half_cone_angle)
    q = inner/outer
    if phi < math.pi/3 and q < 2*math.cos(phi)-1:
        return outer * math.sqrt(1+q*q-2*q*math.cos(phi)), 'mixed-rim'
    if q <= math.cos(phi/2):
        return 2*outer*math.sin(phi/2), 'outer-chord'
    return outer*(2*math.sqrt(1-q*q)+q*(phi-2*math.acos(q))), 'outer-tangent'


def run():
    rng = random.Random(7432026)
    cases=0; pairs=0; max_violation=0.; max_contact_err=0.
    for angle in [0.05,0.16,0.23,0.33,0.34,0.45,0.55,0.78,1.06,1.43]:
        phi=math.pi*math.sin(angle)
        qstar=2*math.cos(phi)-1
        thresholds = [0.0003, 0.07, 0.2, 0.5, 0.8, .95, .999,
                      math.cos(phi/2), max(0.0001, qstar)]
        for v in thresholds:
            for q in [v-0.00001,v,v+0.00001]:
                if not 0<q<1: continue
                B=1.
                predicted,stage=diameter(B,q,angle)
                d1=pair_distance(B,q,phi,q)
                d2=pair_distance(B,B,phi,q)
                err=abs(predicted-max(d1,d2))
                max_contact_err=max(max_contact_err,err)
                assert err < 2e-12, (q,phi,predicted,d1,d2,stage)
                for _ in range(3000):
                    rr=q+(1-q)*rng.random()
                    ss=q+(1-q)*rng.random()
                    delta=phi*rng.random()
                    d=pair_distance(rr,ss,delta,q)
                    viol=d-predicted
                    max_violation=max(max_violation, viol)
                    assert viol <= 5e-12, (phi,q,rr,ss,delta,d,predicted,stage)
                    pairs+=1
                cases+=1
    print(f'OK cases={cases}, sampled_pairs={pairs}, max_positive_violation={max_violation:.3g}, max_contact_error={max_contact_err:.3g}')
    # A one-dimensional radial grid verifies boundary-maximization prediction independently.
    checked=0
    for phi in [0.18, 0.7, 1.25, 2.4, 3.0]:
        for q in [0.1, 0.45, 0.81, 0.99]:
            worst=max(pair_distance(q+(1-q)*i/90,q+(1-q)*j/90,phi,q)
                      for i in range(91) for j in range(91))
            contact=max(pair_distance(B,C,phi,q) for B in [q,1.] for C in [q,1.])
            assert abs(worst-contact)<1e-10, (phi,q,worst,contact)
            checked+=1
    print(f'OK radial_grid_cases={checked}, radial_grid_points_per_case=8281')

if __name__=='__main__':
    run()
