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

# Verification and reproducibility

The exact proof is in `RESULT.md`. The critical finite-dimensional identities are the simultaneous Gram relation \(AA^{\mathsf T}=A^{\mathsf T}A=(n-1)I+J\), the inverse \(A^{-\mathsf T}=(A-q^{-1}J)/(n-1)\), pair counts, and the determinant ratios \(q:q:1\). The external Barba equality and Brouwer--Whiteman existence theorems are sourced explicitly in `RESULT.md`.

To independently reproduce the **example-only** calculations, run `python3 verify_five_dim.py` from the extracted files. It uses the Python standard library and checks the explicit dimension-five sign matrix, rational inverse columns, the exact norm on selected rational pairs, and the parametric coefficient/determinant identities for several odd integer values of \(q\).

This executable check is not an exhaustive classification of cube maximizers, a general-dimensional matrix existence oracle, or a substitute for the quantified proof. Independent scientific and bibliographic review has not been performed.
