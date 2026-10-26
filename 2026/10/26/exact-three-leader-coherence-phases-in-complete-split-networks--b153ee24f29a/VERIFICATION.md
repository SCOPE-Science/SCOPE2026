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

Run `python verify.py` after installing `requirements.txt`.

The checker asserts 24 exact symbolic identities: rational pairwise cost formulas for the low-periphery cases, the two positive-coefficient shifted numerator certificates, and the infinite-range comparison. It evaluates 45,746 integer parameter pairs using Python's exact `Fraction` arithmetic and reconstructs 140 grounded Laplacians independently from graph adjacency before taking exact matrix inverses with SymPy.

Recorded result from the included program:

`VERIFY_OK symbolic_identities=24 parameter_pairs=45746 independent_laplacian_inverses=140`

All results above were executed on this exact standalone script. The finite numerical/algorithmic checks do not certify the infinite theorem; correctness for all allowed integers comes from the algebraic proof in `RESULT.md`. No external proof assistant or independent auditor has verified the theorem. No random trials or approximate eigenvalue cutoffs are used.
