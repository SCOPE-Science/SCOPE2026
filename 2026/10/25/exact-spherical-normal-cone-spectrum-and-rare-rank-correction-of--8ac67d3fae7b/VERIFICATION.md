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

# Checks and limitations

`check_angles.py` compares the analytical Gaussian integrals against independently enumerated optimization over every vertex of each two-row matching polytope for all dimensions two through eight. Simulations use fixed seeds and predefined sample counts. Each observed rank-frequency vector must lie within a six-standard-error envelope plus numeric tolerance of the exact integral prediction; angular mass normalization is asserted to numerical precision. At dimensions ten, fifty, one hundred, and one thousand, the script also evaluates the scaled relative rank-one correction; its approach to one corroborates the limit constant.

The proof in `RESULT.md` is the evidence for all-dimensional validity. Computational checks are finite, simulation-dependent, and do not certify infinite statements or bibliographic originality. No independent mathematical audit has been performed.
