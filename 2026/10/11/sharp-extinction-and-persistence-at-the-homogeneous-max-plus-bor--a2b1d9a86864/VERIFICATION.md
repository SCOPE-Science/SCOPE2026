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

## Exact tests performed
`python3 check_exact.py` was run against the packaged standalone script, producing `EXACT_RATIONAL_REGRESSION_OK`. It uses `fractions.Fraction` rather than floating-point simulations for the tested trajectories. Under-damped parameter cases include \((T,D)=(0,1),(1,1),(1,2),(2,2),(2,3),(3,4),(3,3)\), with exhaustive small rational integer grids of initial coordinates and an explicit witness attaining the claimed least uniform index. Repeated-root checks use \(\lambda=1/2,1,2,3\). Distinct-root checks use rational pairs \((\lambda_+,\lambda_-)=(2,1),(3,2),(5,2),(8,2)\), and parameter distances chosen to make threshold crossings exact. The nonpositive initial half-plane was also checked on rational examples.

## Proof checks not delegated to computation
The exact two-step reset lemma, the sine-phase bound \(\lceil\pi/\theta\rceil\) for arbitrary real parameters, the all-initial-condition minimality argument, the sign of the repeated-root bracket, and the strictly monotone ratio in the distinct-root formula are proved analytically in `RESULT.md`. Finite computation does not certify universality, publication priority, or robustness under perturbations.

## Reproduction
Run `python3 check_exact.py` in the same directory as the file. Python 3 standard library suffices. There is no external download, random input, or nonstandard dependency. The self-contained script prints `EXACT_RATIONAL_REGRESSION_OK` if all specified assertions pass.
