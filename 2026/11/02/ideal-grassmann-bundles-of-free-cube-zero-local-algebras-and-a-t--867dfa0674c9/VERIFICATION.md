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

# Reproducibility
Run `python3 verify.py` with the Python standard library. The exact output from the run is stored in `verify_output.txt`.

The checker enumerates all reduced-row-echelon subspaces of the radical for five prime-field configurations. For every subspace, it applies left and right multiplication by each original degree-one generator, tests membership by row reduction, and counts genuine two-sided ideals. It adds the unique full-algebra ideal and compares all counts by dimension against the stated formula. In the two-generator configurations it separately enumerates the four-dimensional ideal set, checks the three twisted-cubic Plücker quadrics and the fixed linear Plücker subspace, and checks the direct projective parameterization for surjectivity. It uses neither the predicted ideal list nor the cone equations to select candidate ideals.

Expected final output marker: `FREE_CUBE_ZERO_IDEAL_CENSUS_OK 5 EXHAUSTIVE_CASES`.

Observed counts for the seven-dimensional two-generator algebra: over \(\mathbb F_2\), \((1,15,35,15,7,3,1,1)\), total \(78\); over \(\mathbb F_3\), \((1,40,130,40,13,4,1,1)\), total \(230\). The entries index ideal dimensions from zero to seven.

These finite checks are not an exhaustive search over all finite fields, all generator ranks, or arbitrary infinite fields. The general assertions rely on the written structural proof and on the Plücker-coordinate argument.
