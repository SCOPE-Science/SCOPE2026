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

Execute `python verification/check_skewness.py` (NumPy and SciPy) and `python verification/symbolic_check.py` (SymPy). The numerical script compares a direct generator resolvent against the closed third-cumulant polynomial for 60 fixed-seed parameter triples, repeats these with nonzero additive diffusion, and checks nine unique roots and their two neighboring signs. The symbolic script checks the polynomial rational identity exactly by symbolic cancellation. Both programs were executed from the packaged file contents and passed.

The algebraic proof is the stationary generator recurrence followed by the fact that one decreasing function crosses one increasing function on the interval of interest. Neither a finite parameter grid nor symbolic-software output is substituted for that proof. Independent experimental or peer review has not been performed.
