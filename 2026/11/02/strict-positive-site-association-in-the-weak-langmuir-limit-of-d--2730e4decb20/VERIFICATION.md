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

# Reproduction and scope

With Python 3 and NumPy installed, run `python verify.py` in a directory containing the supplied standalone verifier. It checks the normalized canonical and weak-exchange distributions on 240 independent nonconstant positive-weight instances with two through seven sites, the Boolean-square cross-product conditions, pair covariance signs for every pair and nontrivial canonical number, plus the exact two-site formula. It also builds and solves the full 64-state Markov generator on a two-by-three driven multi-lane strip and verifies stationarity, exact binomial particle-number marginals at four finite exchange rates, convergence to the proposed limiting law, and all-pairs positive covariance at the smallest tested rate.

Proof of the all-size, all-parameter result is analytical: binomial birth–death projection, finite-state singular perturbation, strict Newton inequalities, FKG/MTP2, and exact weighted exclusion-generator stationarity. Numerical checks cannot certify the infinite parameter ranges and are not used as their proof. All computations are finite and reproducible; no independent scientific audit or third-party verification is claimed.
