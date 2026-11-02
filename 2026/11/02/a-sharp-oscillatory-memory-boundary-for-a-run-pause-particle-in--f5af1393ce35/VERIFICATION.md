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

# Verification details

The exact proof in `RESULT.md` derives four-state generator balance, solves a two-dimensional odd-moment system and a three-dimensional lag covariance system, and checks every spectral boundary, including the nonoscillatory direction-randomization case and the collision of the trap pole with the real parts of the complex pair.

Execute the standalone Python standard-library checker with `python verify.py` in this directory. The recorded replay passed 2,970 assertions. Exact-rational tests check all off-diagonal transition rates, uniform chain stationarity, generator action, moment balances and positive variance across 24 parameter pairs, with 10 choices of stiffness and speed per pair. Independently of the closed spectral formula, a third-order matrix ODE is propagated by a convergent Taylor scheme and compared on a finite grid of times, covering reversal, no reversal, persistent orientation and critical stiffness. Additional finite assertions check the coefficient of the slow real pole and explicitly positive/negative sign witnesses. No external data or random seed is used.

Finite tests cannot prove sign changes at infinitely many times, uniqueness in a continuum of parameter values, global publication priority, or bounds for models with thermal noise. Those mathematical quantifiers are established only through the analytic proof, with literature novelty qualified as best-knowledge. No independent mathematical or publication-priority audit has been performed.
