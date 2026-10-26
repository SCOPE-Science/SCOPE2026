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

# Reproducibility and limits

Use Python 3 with `sympy` installed and run `python scripts/census.py` followed by `python scripts/independent_check.py`. Both reconstruct the full binary-field census and verify `certificates/orbits.json` from scratch, with the expected outputs recorded separately under `certificates/`. The first program uses SymPy for polynomial ideals and an affine parameter enumeration; the second uses a complete scan of all coefficient masks, a binary polynomial gcd for line factorization, all invertible projective matrices, and its own polynomial Buchberger routine. The two agree on all orbit representatives' geometric smoothness and line factorization statistics. The work establishes only the stated finite classification and has not undergone independent external audit.
