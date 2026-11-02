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

Reproducible command: `python verify.py`, requiring Python 3, SymPy and NumPy. Execution passed `VERIFY_OK assertions=2827 direct_RK_cases=420`. The script checks the Butcher stability function, exact extremizer and irrational sign certificate, exact lower-bound identities, all-dimension witness inequalities up to 100 leaves as a diagnostic, direct RK stage matrices versus spectral formulas in 420 randomized cases, stochastic row sums, off-diagonal signs, and balanced all-step numerics for small stars.

The mathematical proof is in `RESULT.md` and does not depend on any finite sweep or floating-point tolerance. In particular, symbolic calculus establishes the global scalar minimum; monotonicity of \(F\) and the exact radical sign prove the claims for every admissible dimension and rate. The numerical checks cannot establish historical originality or independent validation. An independent audit has not been performed.
