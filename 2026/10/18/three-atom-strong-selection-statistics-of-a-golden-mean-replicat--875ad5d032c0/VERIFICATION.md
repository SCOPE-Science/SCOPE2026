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

The supplied `verify.py` uses bracketed scalar roots to reconstruct the branch intervals for representative parameter values, obtains selected periodic words through inverse dynamics, and checks their physical mean, variance and derivative averages. It also checks the exact cyclic transition-count identities for all admissible binary cyclic words of lengths one through twelve.

The script completed **899 finite diagnostics**, with largest observed finite-parameter variance approximation error approximately \(0.00373901\), Lyapunov two-term approximation error approximately \(0.08134564\), and absolute mean error below \(10^{-12}\). The bounds in the theorem are asymptotic; finite-parameter discrepancy need not vanish for any one sample.

Run with `python verify.py` in a Python 3 environment with SciPy. The theorem's infinite quantifiers follow from the explicit interval, derivative, symbolic-frequency and entropy arguments in `RESULT.md`. These finite diagnostics do not certify the source's entire dynamics, numerical completeness of unrelated periodic cycles, or bibliographic novelty. Independent mathematical validation has not been performed.
