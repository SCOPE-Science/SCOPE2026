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
# Verification record

The file `verify.py` uses only Python 3 standard-library modules; run with `python3 verify.py`. It independently enumerates monomial Hilbert coefficients for the three-variable Jacobian complete intersection and its six-variable tensor square; checks the negative block-swap residue trace and all five primitive invariant dimensions; checks Hodge symmetry and rational Poincaré duality for both quotient and resolution; derives Euler characteristic of the smooth sextic from Chern classes, separately computes the fixed-locus Euler characteristic, and verifies the finite quotient Euler and blowup Euler formulas. It verifies the exact discrepancy arithmetic \(\frac12\) from the ramification and codimension-three blowup formulas. Expected marker: `VERIFY_OK`.

Proof obligations not discharged by the script are explicitly resolved in `RESULT.md`: smoothness for every smooth ternary sextic, exhaustive fixed-locus classification, linearized analytic quotient germ, smooth blowup and its exceptional geometry, and rational cohomology transfer. The computations do not verify absolute publication priority, integral torsion, the full ring structure, or an independent audit. All asserted numerical data are rational-cohomological except the explicitly stated fundamental groups and local singularity indices.
