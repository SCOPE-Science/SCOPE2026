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

# Verification of the quartic defect and sharpness

The independent audit channel is unperformed. The documented self-review consists of direct proof reconstruction, exact coefficient matching, pointwise cone geometry and the finite checks below.

Run `python verify.py` with SymPy. The script checks that the difference between both sides of the scalar identity is identically zero, verifies positivity by an exact factorization and reproduces finite-parameter sharpness witnesses. Its finite samples are illustrative only; the proof in `RESULT.md` establishes the result for every positive parameter, every permitted measure space and all unit pairs.

The exact coefficient identities are \(E-3\tau^2=2A^2/B\) and \(12\tau^2=2B-4A^2/B\), with \(E^2=\tau^2(1+2\tau^2)(2+\tau^2)\). The cone bound uses an orthogonal eigenbasis of the quadratic form, so no approximate numerical diagonalization is needed in the analytical argument. The constant is demonstrated optimal on every allowed space by placing two rotated eigenvector coordinates on disjoint norm-one functions.

The near-equality statement controls distance to pointwise null lines, not distance to the globally mass-balanced minimizer subset. The published numerical infimum is prior work and not the claim of novelty. Potential unindexed equivalent weighted quartic remainders remain a priority risk.
