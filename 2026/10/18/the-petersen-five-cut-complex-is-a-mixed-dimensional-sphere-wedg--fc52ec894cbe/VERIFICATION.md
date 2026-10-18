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

The accompanying `check_integral.py`, `check_finite_fields.py` and `morse_certificate.json` are complete stand-alone scientific artifacts. Python 3 standard library is the only dependency. Place the three files in the same directory, then run `python3 check_integral.py` and `python3 check_finite_fields.py`.

`check_integral.py` enumerates all \(252\) five-vertex cuts of the Petersen graph and verifies the face-vector counts, complete acyclic matching, signed integral cancellation sequence, matrix certificate, seven-dimensional rational rank and determinant-one seven-by-seven minor. It checks all \(1850\) arrows in the \(495\)-node directed Hasse diagram for acyclicity rather than inferring this from unmatched-cell counts. The exact matrix checks imply torsion-free homology, and the CW cell dimensions imply the claimed homotopy type.

`check_finite_fields.py` separately enumerates facets and full simplicial chains, using no Morse pairs or certificate. It finds boundary ranks \((9,36,84,115)\) over \(\mathbb F_p\) for \(p=2,3,5,7,11\) and reduced Betti ranks \((0,0,0,1,5)\). These are independent computational cross-checks but do not, by themselves, prove absence of integral torsion.

The conclusion is specific to the ordinary five-cut complex of the ten-vertex Petersen graph. The computations are exhaustive finite checks; no generalization to infinitely many graph orders is claimed. Independently written mathematical review has not been performed.
