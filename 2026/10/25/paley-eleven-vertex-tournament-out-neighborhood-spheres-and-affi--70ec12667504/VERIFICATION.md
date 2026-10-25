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

# Verification of the finite Paley tournament claim

Run `python PALEY11_VERIFY.py` with Python 3.10 or later, standard library only. The source constructs the actual out-neighborhood family \(x+\{1,3,4,5,9\}\) over \(\mathbb F_{11}\). It asserts the face vector \((11,55,110,55,11)\), all 242 nonempty faces and 715 Hasse covers, a complete disjoint matching with 110 pairs and critical counts (one vertex; 21 triangles), and acyclicity by a full directed-Hasse topological sort. These steps are necessary for the integral homotopy assertion: face counts or mod-two ranks alone would not suffice.

The same program independently enumerates the 55 affine symmetries of the complex and their exact signed fixed-face traces. It asserts class counts 1, 10 and 44, with respective traces 21, -1 and 1, and confirms the invariant dimension by exact integer arithmetic. Expected successful marker: `PALEY11_CERTIFICATE_PASSED`.

Limits: this certificate treats one finite tournament and its specified affine group, not all tournaments or all field orders. Algebraic identification of the representation uses rational character theory; this does not identify its integral lattice. Independent audit remains unperformed.
