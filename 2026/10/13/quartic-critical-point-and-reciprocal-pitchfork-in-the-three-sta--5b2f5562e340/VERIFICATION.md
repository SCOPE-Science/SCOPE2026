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

`verify.py` reconstructs the Taylor coefficients from the exact hyperbolic representation of the source's function. It verifies symbolically:

- the closed formula for \(c_2(t)\);
- the exact polynomial reduction that evaluates \(c_4\) at the critical root;
- \(Q_k(18/7)=-120/49\);
- \(R_k(18/7)=3(43k^2+5k-2)\);
- \(\partial_sR_k=7(k-2)(k+1)(2k-1)\);
- the formulas for the positive slope \(A_k\) and branch constant \(C_k\).

It additionally evaluates the signs for integer \(2\le k\le40\) as a finite consistency check. Those finite evaluations are not used as an all-order proof.

Expected successful output:

`VERIFY_OK symbolic=1 k_range=2..40`

Limits: this verification establishes the local Taylor and bifurcation algebra only. It does not search for distant critical points of \(K_1\) and does not certify global maximality or the complete Gibbs-measure phase diagram.
