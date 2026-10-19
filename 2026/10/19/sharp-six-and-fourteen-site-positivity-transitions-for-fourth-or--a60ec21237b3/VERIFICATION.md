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

Run `python artifacts/verify_cycle_pade.py` after installing `sympy` as specified in `artifacts/requirements.txt`. The script symbolically recomputes the Padé expansion through degree seven, exact rational transition entries of cycles with three through six vertices, the six-cycle sign quartic, cycle distance-walk coefficients on thirty vertices, and the pseudoinverse difference equations through thirty-nine vertices. It also compares independently constructed rational matrix inverses at selected steps. On the assembled scientific files it prints `VERIFY_OK` and a total of 438 exact assertions.

# Scope of verification

The infinite-size small-step cutoff follows analytically from the first nonzero Padé coefficients and simple-path counting. The large-step cutoff and the limiting fraction follow analytically from the cycle pseudoinverse formula and its quadratic sign inequality. Finite symbolic tests are corroboration; none constitutes an exhaustive enumeration of all dimensions or all steps. The six-cycle complete step interval uses Descartes' rule plus exact positive expressions for the other two distances. Verification addresses the end-step transition operator, not internal stages, floating-point arithmetic, or independent mathematical certification.
