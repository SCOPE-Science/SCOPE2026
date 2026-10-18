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

# Reproduction and limitations

Execute `python3 verify_monge.py` with Python 3 in this directory; the checker uses only the standard library. It enumerates exact ordering regions, simulates matrices from the claimed distribution and checks their Monge inequalities, verifies the mean of the extreme contrast against an exact rational formula, checks beta moments, tests the two explicit mass profiles at 40,000 columns, and compares an empirical joint edge CDF with its limiting Gumbel product. The script's deterministic seed makes the experiment reproducible.

A successful numerical run corroborates finite identities and limiting trends. The almost-sure uniform shape theorem and joint independent Gumbel law are instead proved analytically in RESULT.md. Sample-based tests do not establish infinite quantifiers. The proof assumes intrinsic-uniform measure on nonnegative, normalized, two-row Monge cost matrices; it is not a result about vertex-uniform or noise-perturbed sampling. Independent external review has not been performed.
