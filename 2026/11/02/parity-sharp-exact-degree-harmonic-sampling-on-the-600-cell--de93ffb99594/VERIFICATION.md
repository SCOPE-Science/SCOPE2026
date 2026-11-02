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

# Verification of the mathematical claim

The source `CHECK.py` carries out an exact integer recurrence on the labelled affine \(E_8\) graph through degree 200; verifies the representation-dimension relation; checks the twelve parity-specific saturation witnesses and both sharp final obstructions; and checks coordinatewise 12-step multiplicity inclusion and the 60-step multiplicity shift in the computed finite range. It separately constructs all 120 distinct unit vertices of the 600-cell, computes the Chebyshev Gram matrices and numerically diagonalizes them at degrees 0 through 14, comparing the resulting 120 eigenvalues (with multiplicity) against their prescribed exact rational values; it also directly checks the matrix identities at the pairs of degrees 0/60 and 1/61.

**Actual replay:** `python CHECK.py` printed `PASS 241 assertion groups; ranks at degrees 27,29,58,60: [56, 60, 59, 60]`. Execution used Python 3 with NumPy. All numerical eigenvalue discrepancies and 60-step kernel-identity errors were below \(10^{-8}\). Each tested vertex has unit norm and antipodal partner, and the 120 generated vertices were distinct.

**What is proved beyond these finite tests:** The exact spectrum for every degree follows from the \(SU(2)\) character formula and finite-group orthogonality; the recurrence is exact from Clebsch–Gordan; multiplying by a nonzero invariant degree-12 form is an injection between all pairs of symmetric-power spaces twelve degrees apart. The element-order types 4, 6 and 10 force the necessary and sufficient congruence for perfectly tight sampling. Exact recurrence entries in six consecutive parity-appropriate residue classes imply *all* later rank-60 statements, and the two earlier failed degrees certify that the eventual thresholds cannot be lowered.

**What is not independently certified:** The checker is not a proof assistant and is not an independent mathematical audit. It does not settle historical priority or provide the leading constants for the asymptotic nonzero-eigenvalue conditioning bound. Complete texts of some historical symmetry-harmonic treatments were inaccessible and remain a literature-overlap risk.
