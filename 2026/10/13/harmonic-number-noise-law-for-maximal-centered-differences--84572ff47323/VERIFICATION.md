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

The proof is analytic and valid for every integer \(m\ge1\). The key exact identity is
\[
2\sum_{j=1}^{m}\frac{(m!)^2}{j(m-j)!(m+j)!}=H_m.
\]
It is proved in `RESULT.md` by a beta-integral transformation, not by numerical enumeration.

`verify.py` is a supplementary exact-rational replay. For each \(1\le m\le20\), it constructs the closed-form stencil coefficients, verifies polynomial moments through degree \(2m\), and checks that the complete absolute coefficient sum equals \(H_m\) exactly. A successful run prints `VERIFY_OK`.

Limits: this replay does not certify floating-point implementations, stochastic-noise statistics, nonuniform or one-sided grids, or derivative orders other than one.
