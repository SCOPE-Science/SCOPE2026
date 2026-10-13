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

The proof uses the exact continuum of necessary non-entangling constraints from arXiv:2511.08285v1, not a finite discretization. The key reduction is
\[
a^2x+2a(1-a)y+(1-a)^2z\le\frac12\quad\text{for all }a\in[0,1]
\]
if and only if
\[
0\le x,z\le\frac12,\qquad
y\le\frac12+\sqrt{\left(\frac12-x\right)\left(\frac12-z\right)}
\]
for the nonnegative variables relevant here. The subsequent two-variable quadratic maximization is exact.

The attached checker is run from `artifacts/verify.py`. It verifies the rational strict-extension example
\[
\lambda=\left(\frac{63}{100},\frac15,\frac3{20},\frac1{50}\right)
\]
in exact arithmetic, including the source's first-row hypothesis, failure of regions A, B, and C, the positive-discriminant branch, the envelope value \(121/640\), and the strict gap \(7/640\). A dense-grid comparison is only a numerical sanity check and does not certify the continuum theorem.

Unproved limits: the envelope is not shown sufficient for a non-entangling conversion, and the complete full-rank fixed-spectrum problem remains open outside the excluded region.
