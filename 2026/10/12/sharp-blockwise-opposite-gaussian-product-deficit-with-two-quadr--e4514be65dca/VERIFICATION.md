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

The deterministic checker evaluates the conditional fourth-order Gaussian polynomial
\[
v_2v_3+2r^2+(a^2v_3+b^2v_2+4abr)x^2+a^2b^2x^4,
\]
where \(v_2=1-a^2\), \(v_3=1-b^2\), and \(r=c-ab\). It uses the exact normalized negative Gaussian moments
\[
\mathbb E|Z|^{2-s}/M_s=1-s,
\qquad
\mathbb E|Z|^{4-s}/M_s=(1-s)(3-s)
\]
to replay the identity
\[
\Delta_s=-s\bigl[a^2+b^2+4abc-(2+s)a^2b^2\bigr].
\]
The checker uses rational arithmetic for several exact singular extremizers. In particular for \(s=1/2\), \(a^2=b^2=2/11\), and \(c=-7/11\), it verifies determinant zero, the minimum polynomial value \(-2/11\), and the sharp positive excess \(1/11\). It additionally runs deterministic positive-definite sampled cases to check the exact polynomial and the sharp bound numerically.

Run `python3 verify.py` with Python 3 and no third-party dependencies. A successful run prints a line beginning `VERIFY_OK exact_extremizers=3`. Numerical sampling provides no proof of an infinite statement: the global inequality and equality cases are established by the analytic correlation constraint and the completed-square bound in `RESULT.md`.
