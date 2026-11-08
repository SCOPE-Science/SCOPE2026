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

`CHECK.py` is a standalone, standard-library Python program. Execute `python3 CHECK.py` after extracting the embedded file. It verifies exact rational finite-tree moments and the dyadic-hub witness inequalities; its deterministic assertion count is printed on success.

Analytical checks: (i) the parent-choice generating function yields the insertion-depth Bernoulli law; (ii) an exact orthogonal martingale expansion yields the total-path-length variance identity; (iii) sublinear hub masses make the martingale square-summable and permit deterministic centering; (iv) two earlier hubs at each critical/supercritical spike give a positive lower bound on the conditional variance and force logarithmic growth in the normalized total variance.

The finite program does not certify the all-order proof, independently assess historical priority, or establish a distributional limit in the critical regime. Independent audit: not yet performed.
