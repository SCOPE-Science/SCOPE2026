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

# Reproducibility and limitations

The theorem is proved by recovering the translation subgroup from left multiplication operators, constructing Fourier projectors and matrix units after splitting the group characters, and descending split blocks via Frobenius. The finite-field descent uses Wedderburn–Artin and finiteness of division rings, not a modular Maschke theorem.

Run `python3 verify_left_alexander.py` from the package directory. The script constructs the affine permutation matrices, computes their span rank by modular Gaussian elimination, and compares it with independently enumerated character orbits and Frobenius block dimensions. It checks nineteen cyclic configurations (two repeat calls used for specific field-descent assertions) and five rank-two abelian configurations, including coefficient characteristics dividing the order of the affine permutation group. These finite tests are consistency checks and are not substitutes for the general proof.

The coefficient characteristic dividing the order of the underlying abelian group is excluded, as are non-Latin Alexander quandles. The comparison with earlier work acknowledges previously established complex multiplicity-free results. No independent mathematical audit or universal machine certification has been performed.
