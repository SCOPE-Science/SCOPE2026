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
# Reproducible verification
Execute `python3 verify.py` with Python 3 (standard library only). The checker enumerates the connected triples and all admissible four-faces of the Alexander dual for \(d=3,4,5\), independently enumerates all coordinate squares, confirms each connected triple has exactly one square parent and each Hamming-distance-two diagonal exactly one square, computes the retained square-triangulation counts, and independently reduces mod-two boundary matrices. It prints the checked dual face counts and \((H_1,H_2)\), and terminates with `HYPERCUBE_ORDINARY_THREE_CUT_DUAL_FINITE_CHECKS_OK`.

The all-dimensional and integral conclusions are mathematical deductions from the explicit elementary collapses and combinatorial Alexander duality stated in `RESULT.md`; finite mod-two checks alone cannot certify those general conclusions or rule out torsion. Independent audit: not performed.
