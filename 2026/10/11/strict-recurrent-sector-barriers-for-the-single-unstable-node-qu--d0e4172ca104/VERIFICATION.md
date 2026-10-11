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
# Analytical and executable verification

The packaged `verify.py` verifies the polynomial energy derivative, the scalar height equation, the characteristic polynomial at the equilibrium, and the algebraic obstruction on a hypothetical constant-height oscillator interval. Execute `python verify.py` with SymPy installed (for instance from `requirements.txt`). That check has been run successfully for the packaged source code.

For arbitrary real \(a\) and strictly positive \(b\), the proof in `RESULT.md` then uses the bounded-solution integrating factor, the nonempty compact invariant \(\omega\)-limit set, and an invariant-set contradiction. Those passages are analytic; no finite numerical run is claimed as an infinite-time certificate. The proof does not establish bounded dynamics when \(a>0\), nor blowup or escape rates when no bounded trajectory exists.
