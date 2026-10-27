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

# Reproducibility and scope

Running `python verify.py` with SymPy verifies the polynomial identity \(A f_x+C f_z=0\) in \(\mathbb Z[t,x,y,z]\), as well as all adjacent and opposite pair-difference factorizations, corresponding incidence/nonincidence substitutions, and the opposite-pair resultants. Its observed output was `VERIFY_OK: polynomial syzygy, four A7 contacts, opposite pairs, no triples`.

The normal-form exhaustiveness follows from the polar-line and binary-quadratic argument in `RESULT.md`, not from code. Near freeness follows from the proven singularity inventory, the Dimca–Sernesi inequality, and the nearly-free numerical criterion. Both numerical inputs to these theorems are established in the proof. The program uses symbolic computation in an indeterminate parameter rather than only particular examples. These are mathematical and self-review; no independent audit has occurred.
