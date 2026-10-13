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

# Reproducible exact checks

The standalone `verify.py` needs only Python 3's `fractions` and `itertools` modules. Running `python3 verify.py` checks the four exact update matrices against the stated scalar proximal recurrence for 324 choices of starting state and selected subset. It reconstructs the rational Lyapunov matrix, verifies the identity slack at exclusive serial sampling, computes the joint-probability \(1/100\) slack and its four positive leading principal minors, verifies a cubic matrix annihilation identity for repeated full batches, and checks the path formula and its lower bound across 30 steps. All arithmetic is rational and exact.

The mathematical argument for all finite horizons and for the asymptotic conclusions is in `RESULT.md`. Checking 30 powers does not prove the closed form: the Cayley--Hamilton polynomial and initial conditions do. Checking a finite collection of initial states does not prove universal stability: the rational matrix inequality and positive-definite cone interpolation do.

The method is defined under exact arithmetic and fixed quadratic assumptions only. No independent audit has been performed.
