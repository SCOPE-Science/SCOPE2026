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

The main claim is proved algebraically using smoothness, the exact integer Hessian determinant, Bézout completeness, local tangent contact orders, and an explicit cyclotomic Galois permutation computation. Finite-field checks below are corroborative, not proofs over all prime powers.

Run `python3 verify_c48_flex.py` from the directory containing this file; Python 3 and SymPy are required. The script independently reconstructs the Hessian from derivatives of \(X^4+Y^4+XZ^3\), checks the twelve affine coordinate conditions, exhaustively checks the eight cyclotomic automorphisms and the resulting orbit/fixed-point counts, enumerates flex-support intersections over twenty-three prime fields, and enumerates the quadratic extension fields \(\mathbb F_{25}\), \(\mathbb F_{49}\), and \(\mathbb F_{121}\). The script's observed exit status was zero and its final output was `C48_FULL_HESSIAN_GALOIS_ORBITS_PRIME_AND_QUADRATIC_EXTENSION_COUNTS_PASS`.

The theorem is limited to the fixed quartic equation over characteristic zero and good characteristics above three. Complete arithmetic splitting is proved for those fields via the action of units modulo twenty-four. No independent audit or external validation has been performed.
