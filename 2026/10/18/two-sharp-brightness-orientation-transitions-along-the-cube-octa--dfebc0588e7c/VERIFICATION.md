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

The proof is entirely analytic and all dimension, normalization and parameter restrictions are written in RESULT.md. Execute `python3 verify.py` from the directory containing `verify.py`. This Python 3 checker requires only the standard library. It calculates projected polygon areas from signed-permutation vertices using a direct two-dimensional convex-hull algorithm and compares them with the exact Cauchy profile for 5,460 direction–parameter combinations, including the two transition parameters and both degenerate endpoints. It also cross-checks numerical root identities and the candidates for the extrema. Its expected final line is `ALL_BRIGHTNESS_CHECKS_OK`.

These checks do not certify uniqueness or priority, are not exhaustive over real viewing directions, and do not replace the analytic chamber and equality proofs. Independent mathematical audit has not been performed.
