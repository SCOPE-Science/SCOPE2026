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

The scalar amplification identity is derived algebraically by solving both triangular implicit stages. The derivative, endpoint values, zero locus, order-moment equivalence, extremal sampling inequality, binomial sign law and limiting exponential waiting-time law are proved in `RESULT.md`.

The standalone `verify.py` requires only Python 3 and the standard library. Run `python3 verify.py` in the extracted directory. The executed verifier passed 4,270 exact stage and contraction checks; 1,056 derivative-sign tests; 20,100 exact sign-region checks; 126 exact two-atom moment-constrained comparisons; 30 exact finite-horizon parity-distribution checks; and 12 high-precision threshold and edge checks.

Finite checks do not certify universal quantifiers. Their role is to detect algebraic implementation mistakes and corroborate selected cases. No third-party verification, computational-exhaustiveness claim, or independent audit is implied.
