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

The published one-variable Alexander-polynomial formulas were transcribed term-for-term from Kegel--Schmalian Theorem 2.13.

For \(K_m\), the source's exponent-order argument applies for every \(|m|\ge3\), so all thirteen displayed terms remain distinct and the coefficient \(-7\) survives. Direct exact collection for \(m=-2,-1,1,2\) gives maximum coefficient magnitudes
\[
7,\ 13,\ 9,\ 7.
\]

For \(J_n\), the same source argument applies for every \(n\ge4\) and every \(n\le-5\), again preserving the coefficient \(-7\). Direct exact collection for \(n=-4,-3,-2,-1,1,2,3\) gives
\[
7,\ 7,\ 5,\ 13,\ 9,\ 7,\ 7.
\]

The standard L-space-knot Alexander-polynomial theorem requires every nonzero coefficient to have absolute value \(1\). Therefore each nonzero parameter value is excluded.

The bundled regression script prints:

`VERIFY_OK K_exceptional=4 J_exceptional=7 sampled_K=996 sampled_J=993 all_have_coefficient_abs_gt_1=true`

It exactly checks the finite exceptional set and samples the symbolic non-collision ranges. The infinite proof rests on the published exponent ordering, not on finite sampling.

The independent-audit channel has not been performed.
