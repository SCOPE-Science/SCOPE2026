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

The algebraic criterion follows from the vector part of the Nijenhuis identity on one symplectic vector and the central generator, then from the central part on two symplectic vectors. Those steps apply over arbitrary fields, including characteristic two. The isotropic-frame count and full-row-rank surjection count establish the finite-field formulas without dependence on a numerical experiment.

Run `python3 checker.py` from the extracted package. The checker independently evaluates Nijenhuis torsion on basis pairs and verifies the derived isotropic-image criterion. All \(2^9\) endomorphisms over \(\mathbb F_2\) and \(3^9\) over \(\mathbb F_3\) are checked in dimension three. All \(2^{16}\) possible image matrices in dimension four are checked for isotropy/rank over \(\mathbb F_2\), and additional seeded randomized torsion/criterion cross-checks cover dimension five in characteristics two, three and five.

The reference output concludes `HEISENBERG_NIJENHUIS_OK`. Finite tests do not establish the general theorem and do not provide an independent human or external audit.
