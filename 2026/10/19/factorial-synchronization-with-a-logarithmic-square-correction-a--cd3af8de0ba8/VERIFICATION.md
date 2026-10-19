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
# Reproducibility and limits

The analytic argument is contained in `RESULT.md`. To replay the stand-alone checks, run `python verify.py` with Python 3 and SymPy installed; the successful check prints `VERIFY_OK`.

The checker exactly verifies the center/difference identities for symbolic coupling and the linear multipliers at the extinction equilibrium. It computes rational sample trajectories at couplings \(0\), \(1/10\), \(9/20\) and \(1/2\), and separately updates reciprocal means and logarithmic signed-error magnitudes for long trajectories, avoiding underflow. It compares the fixed-coupling normalized log amplitudes through 500,000 steps in each parameter regime.

Computational evidence tests implementation and finite instances only. It does not establish infinite-time convergence, characterize every initial state by enumeration, prove publication priority, or amount to an independent audit. The proof's key infinite steps are geometric error summability, the summable reciprocal-increment expansion, and convergence of the resulting logarithmic product remainders.
