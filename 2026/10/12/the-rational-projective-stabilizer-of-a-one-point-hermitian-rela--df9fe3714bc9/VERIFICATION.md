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

The finite-field checker `verify_stabilizer.py` uses explicit quadratic extension fields and exhaustive normalized-matrix coefficient equations for the parameters \(s=2\) and \(s=3\). It enumerates \(24\) and \(108\) matrices, matches the independent norm/trace parametrization exactly, and checks the unipotent group law. For \(s=2\), the element-order distribution verifies the quaternion group. The command is `python verify_stabilizer.py`; expected final output is `HERMITIAN_STABILIZER_EXACT_OK`.

The proof for all prime powers rests instead on: (1) smoothness and a unique rational point, (2) the consequent fixed tangent and triangular matrix normal form, (3) comparison of all six homogeneous coefficients, and (4) finite-field norm and trace counts. The checker does not inspect geometric projectivities over extension fields, nor does it certify novelty. The available conference article was examined against the exact stabilizer statement; an inaccessible specialized projective-equivalence chapter remains a bibliographic risk.
