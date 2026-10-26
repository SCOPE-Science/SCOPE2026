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

# Reproducibility
Run `python verify.py` with Python 3 and NumPy. Recorded output: `VERIFY_OK cases=54 n_range=2..10 ranks=1..n exact_margins_commutators_trace plus_numeric_Gram_eigenvalues`.

For each rank the script independently enumerates all multisets, removes each entry to construct the integer weighting, checks dimensions and balanced margins, tests the integer adjacent-degree commutator, checks trace, verifies full row rank, and compares all Gram eigenvalues including multiplicities against the claimed formula. Finite checks do not prove the formula at arbitrarily large size; that is established by the stated algebraic proof. The numerical eigenvalue comparison has documented tolerances in the code.
