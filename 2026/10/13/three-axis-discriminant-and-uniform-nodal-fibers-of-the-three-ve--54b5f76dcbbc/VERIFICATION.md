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

# Verification record

The symbolic proof uses an explicit Jacobian annihilator \(VH=0\), its rank-one reduction, and an exact orthogonal-bundle normal form on every punctured critical-value axis. The matrix rank and singular-support claims are valid for every integer \(M\ge3\) over \(\mathbb C\). The all-fiber complete-intersection premise is Theorem 1.1 of arXiv:2610.02585v1.

To reproduce finite consistency checks, run `python check_discriminant.py` with Python 3.8 or later. This exhaustively evaluates the differential of the three scalar products over \(\mathbb F_3\) for all \(3^9\) frames and checks transverse Hessian ranks for \(3\le M\le8\). Expected output: `GRAM_DISCRIMINANT_EXACT_OK; frames= 19683`. Finite-field enumeration does not prove complex analytic normal forms or all-dimensional claims. No independent audit has been performed.
