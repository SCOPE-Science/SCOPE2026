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

Run:

`python verify.py`

Expected output begins with `VERIFY_OK`.

The verifier uses exact rational Gaussian elimination for the linear systems extracted from the proof. For every odd \(n\in\{5,7,\ldots,31\}\) and every nonzero shift \(r\), it checks that
\[
d_0=d_{-r}=0,
\qquad
\sum_m d_m-d_\ell-d_{\ell-r}=0\quad(\ell\ne0)
\]
has only the zero solution. It separately checks the zero-shift system. It also verifies the symbolic magnitude identities behind the explicit counterexamples for every even \(n\) from \(4\) through \(30\), together with the small failures at \(2\) and \(3\).

These are bounded consistency checks. They do not substitute for the universal proof, whose decisive step is the odd-cycle recurrence and the identity \(T=T(n-1)/2\). No numerical determinant threshold, random search, or exhaustive claim beyond the stated finite replay is used.
