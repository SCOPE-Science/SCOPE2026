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

The theorem is proved symbolically in `RESULT.md`. The standalone exact-arithmetic replay in `verify.py` checks the identities and inequalities used to diagnose the width substitution:

* \(W_g(p)=(p+1)^{2g}-(p-1)^{2g}\) equals the odd-term binomial expansion;
* for every checked \(g\ge2\), the correction \(W_g(p)-4gp^{2g-1}\) is positive;
* in dimension \(2\), the exact identity is \(W_2(p)=8p^3+8p\);
* the ratio \(W_g(p)/(p-1)^{2g}\) has the asserted fixed-dimension \(p^{-1}\) scale.

The finite replay is a regression check, not a substitute for the general proof. No claim of optimality is made. The verifier output is stored in `verification_output.txt`.
