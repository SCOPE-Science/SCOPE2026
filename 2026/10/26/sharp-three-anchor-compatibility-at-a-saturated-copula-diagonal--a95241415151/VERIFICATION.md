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

# Analytical and computational verification

The universal theorem rests on the displayed conditional-second-moment identity, the saturation/zero-variance argument, Jensen's inequality, the quadratic inequality on \([\alpha,1]\), and explicitly nonnegative checkerboard row constructions. The finite checkerboard conversion ensures both uniform margins; no numerical approximations are needed for the proof. For every \(0<a<b<c<1\), the interval width is the positive exact fraction \((c-b)(1-c)/(1-a)\).

Run `python3 verify.py` with Python standard library only. The reproduced output is `PASS: 1904 exact-rational construction, moment, interval and incompatibility checks`. The program checks 400 randomly sampled rational triples with exact Fraction arithmetic (two endpoints and one mixture each), the explicit rational pairwise witnesses, 200 general two-anchor witnesses at the threshold, and supplemental conditional-moment stress tests. A seeded pseudo-random sequence makes the checks reproducible. The constructed copulas are rigorously defined by the latent rows and response-bin construction in RESULT.md; the code verifies their row-level moments and probabilities. These finite checks are not exhaustive over continuum parameter ranges.

No independent audit has been performed. The complete arbitrary three-anchor feasible set is not claimed.
