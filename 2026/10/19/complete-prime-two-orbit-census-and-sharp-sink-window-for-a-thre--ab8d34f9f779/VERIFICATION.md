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

# Verification evidence and limits

The proof derives a bijection between all two-periodic points of the three-dimensional polynomial map and two-periodic points of the explicitly stated scalar cubic; it then solves the two-point equations without a numerical search. The sample verifier `verify.py` uses SymPy and was executed on the packaged code in Python. It checks the sum/difference factorization, both Floquet characteristic polynomials under their defining algebraic relations, the Schur-factor identity, and each coordinate of five independently instantiated exact-rational parameter families.

The checker does **not** prove that an arbitrary nonlinear neutral orbit is attracting or repelling, does not test higher periods or infinity, and does not establish historical priority. The complete proof and the explicit parameter hypotheses are in `RESULT.md`. No independent external audit has been performed.
