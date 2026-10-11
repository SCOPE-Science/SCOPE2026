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
The proof establishes the exact scale profile
\[
d_8(\lambda)=\max\left\{1,\sqrt2-1+\frac{\lambda}{\sqrt2},\lambda-(\sqrt2-1)\right\}.
\]
The fixed pair
\[
x=(-(\sqrt2-1),1),
\qquad
y=(1,0)
\]
is unit, Birkhoff--James orthogonal, and attains this value for every \(\lambda\ge0\).

The lower bound is checked analytically in the only support types, up to dihedral symmetry: a facet endpoint and an interior normal cone exposing a vertex. In the interior case, the three lower bounds are Birkhoff monotonicity, a coordinate estimate from \(u\ge1/\sqrt2\), and a norming-functional estimate giving \(\lambda-(\sqrt2-1)\).

For the generalized rectangular quotient, the three denominator intervals have no interior maximum: the middle logarithmic derivative has the sign of
\[
(2-\sqrt2)\lambda^{p-1}-1,
\]
so it can only change from negative to positive, while the final interval derivative is strictly negative. Therefore only the two switch scales contribute to the maximum.

`verify.py` reconstructs the octagonal norm, checks the equality pair and sampled support families against the denominator profile, verifies the switch scales, and compares the closed formula with a dense one-variable scan for representative exponents. These computations are supplementary only.

No independent audit or independent validation has been performed.
