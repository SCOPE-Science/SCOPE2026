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

# Reproducibility and checks

The standalone `check.py` uses Python 3, NumPy, SciPy, and SymPy. Run from its containing directory with `python check.py`; the script returns a nonzero status if an assertion fails. The exact dimensionless objective, a separate killed-resolvent renewal expression, the positive speed floor, symbolic asymptotic expansion coefficients, and multiple independently selected parameters are tested. During preparation the script printed `PASS: 476 symbolic, independent-resolvent, optimization, and bound checks`.

The uniqueness certificate is analytic: the exponential-polynomial derivative has negative low-order coefficients and strictly positive coefficients past a single index. The coefficient-difference formula proves this for all integers in the required range, not just for sampled terms. The strong-drift limit is justified by a coercive global inequality, a matching trial parameter, and an analytic perturbation near its unique minimizer.

All calculations use the diffusion generator \(D\partial_{xx}-U\partial_x\) and local killing rate \(k\delta_0\). No full stochastic simulation or independent audit is asserted. Finite checks are diagnostic, not substitutes for the proof; the asymptotic remainder constants may depend on fixed \(D,L,k\). The article's finite-parameter mean-time equation is prior work.
