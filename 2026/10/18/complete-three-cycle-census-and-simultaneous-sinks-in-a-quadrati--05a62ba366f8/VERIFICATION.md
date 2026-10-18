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

# Reproduction and verification

Run `python3 CHECK.py` with Python 3.9 or later from the directory containing the extracted files. It requires only the standard-library `fractions` and `itertools` modules. The script terminates with a success message after exact integer/rational assertions; any assertion failure instead raises an exception and prevents the success message.

The script verifies the rational witness coordinates and parameters, all six orderings of the scalar recurrence, both orientation-specific three-step matrices, their exact trace/determinant, six strict Schur stability inequalities, the canonical cycle equations and unit multipliers at the two critical rational parameters, the doubly zero return multiplier at a separate canonical parameter, and exact signs around the two phase transitions. These are finite reproducible calculations, not exhaustive searches over the continuum of parameters.

The infinite mathematical assertions are established in `RESULT.md`: the equality-pattern partition exhausts all real period-three triples; cyclic subtraction and Viète's theorem yield the only possible all-distinct cubic; its discriminant gives an exact existence criterion; conversely every real simple-root ordering solves the original equations; and a simple real cubic level-set analysis yields the two-equal orbit count. The 3D Jacobian has one additional zero multiplier relative to the planar recurrence, with no assumption of pointwise nilpotence for the nonlinearly conjugate normal form.

No independent audit or validation has been conducted. The lawful arXiv original was inspected in detail; the subsequent journal version's full text and some potentially unindexed equivalent historical results were unavailable or not exhaustively checked. Hyperbolicity is proved explicitly at the rational example and hence on an unspecified open neighborhood only; the result does not provide a full attracting-region classification in the five-cycle phase.
