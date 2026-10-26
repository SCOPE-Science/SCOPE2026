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

Use the Python standard library to run `python3 verify.py` beside this document. The script checks four Green-kernel orbits with exact fractions, vanishing row sums, phase boundaries, and sharp absolute-row sums on parameter grids. For seven small graphs it independently forms the full unnormalized Laplacian, exactly inverts its nonsingular rank-one shift \(L+J/(mn)\), subtracts \(J/(mn)\), and compares every inverse entry with the explicit tensor Green formula. Further checks cover threshold neighborhoods and the universal bound over many integer dimensions.

The theorem for arbitrary dimensions, the exact finite cutoff, and the asymptotic statements depend on the symbolic proof in RESULT.md. Finite checks neither establish novelty nor replace that proof. No independent validation or external mathematical audit has been performed.
