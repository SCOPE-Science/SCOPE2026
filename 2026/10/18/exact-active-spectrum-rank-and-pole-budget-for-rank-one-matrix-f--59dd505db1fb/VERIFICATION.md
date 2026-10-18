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
# Reproducibility and verification

The exact algebraic identity was checked symbolically for both a positive rank-one update and an admissible negative update, multiple choices of rational poles and a nontrivial repeated eigenvalue. The deterministic script `verify_rank.py` reports 27 exact rational/symbolic checks. High-precision eigendecomposition tests for fractional exponents strictly inside \((-1,0)\cup(0,1)\), for both update signs, report 54 checks of the active rank, null vector and definiteness signs.

Reproduce with `python verify_rank.py` using Python, SymPy and mpmath. The script uses 70-digit arithmetic for representative matrix powers. The proof, not the finite checks or numerical tolerance, establishes exact algebraic rank for all dimensions and admissible inputs.

Proof dependencies: Sherman–Morrison rank-one inverse update; nonvanishing Cauchy minors and their version with an adjoining constant column; standard Stieltjes integral representations of fractional powers; uniqueness of partial fractions. The theorem does not certify approximation ranks at floating-point precision, arbitrary signed-residue rational functions, or nonnormal matrices.
