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

The bundled program `minimax_pearson_check.py` uses exact fractions and Python's standard library. Execute `python minimax_pearson_check.py`. It was executed on the included file and reported 3,651 exact-rational truth instances, passing the direct divergence, oracle, sharp ratio, additive regret, endpoint balancing, and sampled competitor checks.

The script is an independent numerical-algebraic cross-check, not a proof for all real-valued parameters. Universal claims are established in the four mathematical steps of `RESULT.md`, including the sharpness witness \(s=5/6\) as \(m\uparrow2/3\). Full-support boundary suprema may be approached but not attained. No independent audit has been performed.
