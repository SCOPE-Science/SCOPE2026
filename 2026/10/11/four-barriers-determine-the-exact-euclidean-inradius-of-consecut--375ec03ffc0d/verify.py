#!/usr/bin/env python3
import math

cases=0
for d in range(2,101):
    sd=math.sqrt(d)
    for a in range(0,d):
        for b in range(a+1,d+1):
            vals=[
                0.5,
                b/(d+sd),
                (d-a)/(d+sd),
                (b-a)/(2*sd),
            ]
            r=min(vals)

            assert d*r <= d*(1-r) + 1e-12
            assert d*r <= b-r*sd + 1e-12
            assert a+r*sd <= d*(1-r) + 1e-12
            assert a+r*sd <= b-r*sd + 1e-12

            lo=max(d*r,a+r*sd)
            hi=min(d*(1-r),b-r*sd)
            assert lo <= hi + 1e-12
            s=(lo+hi)/2
            t=s/d

            assert t >= r-1e-12
            assert 1-t >= r-1e-12
            assert d*t-a >= r*sd-1e-12
            assert b-d*t >= r*sd-1e-12

            unique = any(abs(r-vals[i]) <= 1e-12 for i in range(3))
            strict_gap = vals[3] < min(vals[:3]) - 1e-12
            assert unique == (not strict_gap)

            if strict_gap:
                mid=(a+b)/2
                assert abs((a+r*sd)-mid) <= 1e-10
                assert abs((b-r*sd)-mid) <= 1e-10
                assert d*r < mid-1e-10
                assert mid < d*(1-r)-1e-10
                assert r < 0.5-1e-10

            cases += 1

print(f"VERIFY_OK consecutive-layer-S-hypersimplex-inradius cases={cases} d=2..100")
