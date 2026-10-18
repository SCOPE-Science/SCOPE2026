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

# Reproducibility and verification

Execute `python verify.py` in the directory containing the six companion scientific files; Python 3 and SymPy are required. The program verifies the factorization of the exact stationary risk about \(1/9\), the \(p\)-resultant of the sign polynomial and its derivative, the sharp quintic and Bernstein identities, the risk at two rational probability/stepsize examples, and the endpoint limits. It also compares the stationary first and second moment formulas with 350 iterations of the exact rational moment recursion on 25 parameter pairs. The verifier was executed successfully and its bytes were checked after extraction from the final package.

The infinite statements rely on explicit analytic steps in RESULT.md: contraction coupling, Descartes' sign rule, compactness at the positive-risk boundary, a polynomial resultant, Bernstein negativity and quintic monotonicity. Numeric roots are descriptive only, not certifications of absence of other roots. No independent audit or machine-proof certification is claimed.
