---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

For extreme points, after whole-vector sign changes,
\[
x=(a,b),\qquad y=(c,d),
\qquad
a^p+b^p=c^p+d^p=1,
\]
with nonnegative coordinates.

If the coordinate differences have the same sign, equal unit norms force \(x=y\), so the sum of the two James chords is only \(2\).

In the crossing case, assume
\[
a\ge c,\qquad b\le d,
\]
and put
\[
s=a-c+d-b.
\]
If \(s\le2^{1/p}\), Minkowski gives
\[
H(x,y)\le2+s\le2+2^{1/p}.
\]
Equality would force equality in Minkowski, hence \(x=y\) for \(p>1\), contradicting \(s=2^{1/p}\).

If \(s\ge2^{1/p}\), the exact source estimate gives
\[
H(x,y)
\le
\bigl(a^p+d^p\bigr)^{1/p}+a+d
\le
2^{1/p}+2.
\]
Equality forces \(a=d=1\), then \(b=c=0\).

Every nonextreme sphere point is interior to one opposite-sign \(\ell_1\)-edge. Convex equality would make both axis endpoints of that edge maximize with a common extreme partner, impossible by the extreme classification.

Finally,
\[
H(\varepsilon e_1,\delta e_2)=2+2^{1/p}
\]
for all \(\varepsilon,\delta\in\{-1,1\}\).

The proof is exact. Numerical sampling over the full radial sphere for several \(p\)-values was used only as a counterexample stress test and is not proof.
