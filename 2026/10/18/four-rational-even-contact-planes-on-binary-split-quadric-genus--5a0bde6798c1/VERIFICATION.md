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

# Reproduction

Execute `python code/verify_even_contact.py` and `python code/contact_profiles.py` using Python with SymPy installed. The first script checks all 65,535 masks and displays the exact masks' contact counts, field-of-definition singularity filters, four-chart geometric smoothness tests on 60 candidates, and three 72-group automorphism orbits. The second independently checks contact multiplicity partitions on the three representatives. Their exact outputs are included under `data/`.

The finite-field singularity filter only disproves smoothness when a singular point is found; it is not used to certify the survivors. Geometric smoothness of each survivor is instead established by the algebraic unit ideal of its local Jacobian ideal on each of four projective affine charts, so no finite-extension cutoff is misused. All matrix actions use invertible binary two-by-two matrices, and the order-72 symmetry group includes interchange of the two rulings.

No formal assistant-independent proof or external certification has been performed.
