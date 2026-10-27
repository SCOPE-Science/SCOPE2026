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

The provided `verify_exact.py` independently expands the rational Schur representation and inverse coefficients, verifies the published deterministic polynomial specialized to unimodular Schur parameter, checks the exact phase factorization, and reconstructs every entry of the two strictly positive Bernstein matrices using exact rational arithmetic. The program runs under Python 3 with SymPy installed; `requirements.txt` gives the necessary package.

The infinite-class upper bound comes from the cited published inequality and its displayed Bernstein positivity proof. The exact symbolic verification checks the novel finite algebraic certificate and does not by itself prove an infinite-dimensional statement without the functional-analytic reduction. No independent audit or external proof certification was performed.
