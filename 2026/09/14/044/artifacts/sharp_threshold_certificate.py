"""Exact (rational) certificate for the sharp 1/12 threshold family.

Family F(t): A+ = (1/3,1/3,1/3), A-(t) = (-t,-t,1+2t).
Checks with Fraction: traces, Weyl tracelessness, Berger-frame validity
(Bianchi sum b = 0 and |bj-bi| <= aj-ai), sec_min = (1/3-t)/2,
3-sum = 1/3-2t. Headline: t=1/5 gives sec_min=1/15>0, 3-sum=-1/15<0.
Boundary: t=1/6 gives sec_min=1/12, 3-sum=0 (sharpness of Wu's constant).
"""
from fractions import Fraction as Q

def check(t):
    a_plus = (Q(1,3), Q(1,3), Q(1,3))
    a_minus = (-t, -t, 1+2*t)
    assert sum(a_plus) == 1 and sum(a_minus) == 1, "trace must be 1"
    assert sum(x - Q(1,3) for x in a_plus) == 0
    assert sum(x - Q(1,3) for x in a_minus) == 0, "Weyl traceless"
    sec_min = (min(a_plus) + min(a_minus)) / 2
    vals = sorted(a_plus + a_minus)
    s3 = vals[0] + vals[1] + vals[2]
    # Berger frame pairing: alpha_i=1/3 with beta_i; a_i=(al+be)/2, b_i=(al-be)/2
    avals = tuple((Q(1,3)+b)/2 for b in a_minus)
    bvals = tuple((Q(1,3)-b)/2 for b in a_minus)
    assert sum(avals) == 1 and sum(bvals) == 0, "Berger trace/Bianchi"
    # order Berger so a sorted ascending, carry b along
    pairs = sorted(zip(avals, bvals))
    a = [p[0] for p in pairs]; b = [p[1] for p in pairs]
    assert a[0]+a[1]+a[2] == 1
    ok = (abs(b[1]-b[0]) <= a[1]-a[0] and abs(b[2]-b[0]) <= a[2]-a[0]
          and abs(b[2]-b[1]) <= a[2]-a[1])
    return sec_min, vals, s3, a, b, ok

for t in [Q(1,5), Q(1,6)]:
    sec_min, vals, s3, a, b, ok = check(t)
    print(f"t={t}: sec_min={sec_min} (= {(1/3-t)/2}), sorted={vals}, "
          f"3-sum={s3} (= {Q(1,3)-2*t}), Berger a={a} b={b}, constraints ok={ok}")
    assert ok

sec, vals, s3, a, b, ok = check(Q(1,5))
assert sec == Q(1,15) and sec > 0 and s3 == Q(-1,15) and s3 < 0
sec6, vals6, s36, a6, b6, ok6 = check(Q(1,6))
assert sec6 == Q(1,12) and s36 == 0
print("EXACT CERTIFICATE PASSED: t=1/5 strictly sec>0 with 3-sum<0; t=1/6 boundary sharp.")
