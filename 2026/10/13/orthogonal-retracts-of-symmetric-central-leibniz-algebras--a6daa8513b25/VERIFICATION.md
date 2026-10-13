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

Run `python3 verify.py` with Python 3. The self-contained program enumerates all idempotent Leibniz endomorphism matrices in two diagonal two-dimensional cases over the prime field of three elements. Independently, it enumerates all projection matrices satisfying the bilinear orthogonality equations for diagonal forms over the prime fields of three and five elements. It also enumerates totally isotropic one- and two-dimensional subspaces over the prime field of three elements in dimensions up to four, comparing the incidence recursion against direct subspace sets. The expected terminal output includes `VERIFY_OK`.

The general theorem has a handwritten algebraic proof based on the derived ideal, projection normal forms, complement counts, Witt decomposition, and an incidence count. Finite tests alone would not establish infinitely many dimensions or finite extension fields. No independent mathematical audit has been performed.
