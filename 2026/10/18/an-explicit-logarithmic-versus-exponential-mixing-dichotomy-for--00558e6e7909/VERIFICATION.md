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

# Verification

Run `python3 verify.py` in a directory containing the two files. This checks finite transition matrices, uniform derivative-based coupling inequalities, stochasticity, the admissible high-conformity parameters, and tail bounds for multiple finite population sizes.

The quantified logarithmic upper bound uses the analytic inequality \(\sigma'(u)\le1/4\), while the exponential lower bound uses the binomial Chernoff–Cramér inequality and a union bound. Neither is inferred from numerical sampling. The integer threshold \(1/4\) is the ordinary total-variation mixing-time convention.

The theorem does not supply a sharp transition line or independent external certification.
