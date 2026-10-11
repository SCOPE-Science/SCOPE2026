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
# Verification

The package includes two standalone Python 3 programs with no nonstandard library dependencies.

`python3 check_plane_neighborhood.py` builds projective coordinates modulo three, checks the 13-line incidence design, creates all 3,861 nonempty faces, checks the 1,910-pair discrete Morse matching against every Hasse incidence via a full directed topological sort, and computes all 39 signed integral boundary coefficients via a terminating gradient-path recursion. It verifies that the Morse degree vector is zero.

`python3 independent_plane_check.py` independently lists projective points, constructs the nonincidence neighborhoods directly and computes reduced simplicial boundary ranks over the two-element field from first principles. It finds the same face vector and reduced ranks 39 and 1 in dimensions four and five, zero elsewhere.

The mod-two computation alone would not prove the integral homotopy type. The integer attaching-map calculation and Hurewicz theorem supply the required stronger step. The certificate is exhaustive only for this finite 26-vertex graph; no statement for larger projective planes or independent external review is included.
