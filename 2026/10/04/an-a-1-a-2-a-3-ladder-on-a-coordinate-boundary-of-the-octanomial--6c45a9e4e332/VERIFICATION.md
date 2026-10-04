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

The exact symbolic verifier is `verify.py`. It reconstructs the local affine polynomial at \([1:0:0:0]\), its gradient and Hessian, the corank-one kernel, the cubic restriction along that kernel, the adapted coordinate change, the transverse Hessian, and the reduced cubic and quartic coefficients.

Run:

`python3 verify.py`

Expected terminal line:

`VERIFY_OK`

The decisive identities are
\[
\det H=2c(ab-cf),\qquad F(-ct,bt,at)=ab(ah+bg-cd)t^3,
\]
and, on \(ab-cf=ah+bg-cd=0\),
\[
[t^4]F\bigl(u(t)-ct/a,\,v(t)+bt/a,\,t\bigr)=-\frac{b^2gh}{a^2c}\ne0.
\]
The verifier checks the symbolic identities only. The passage from a corank-one hypersurface germ with nondegenerate transverse quadratic part and reduced one-variable order \(3\) or \(4\) to type \(A_2\) or \(A_3\) uses the analytic splitting lemma over \(\mathbb C\). No global classification of singular points is asserted.
