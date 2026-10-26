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

The `check.py` program requires Python 3, NumPy and SciPy. Run `python check.py`. It reconstructs the stationary conditional Fourier equations and source characteristic function independently from their displayed analytic forms; compares numerical Lévy–Khintchine integrals to the predicted transform over several switching rates; checks that the OU driving density is negative near zero only below the threshold; verifies its integrated rate is \(\alpha\) in the admissible range; checks the independent compound-Poisson rate \(\log2\); and compares cumulants and an independent finite Monte Carlo gamma-variance-mixture simulation.

The analytic proof, not the computer experiments, establishes infinite divisibility, the strict self-decomposability boundary, and the OU construction for all real \(\alpha>0\). No statement here certifies novelty or provides external independent audit.
