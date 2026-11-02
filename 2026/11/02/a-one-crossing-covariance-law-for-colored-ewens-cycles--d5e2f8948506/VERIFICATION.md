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

Run `python3 checker.py` with Python standard library. It enumerates all permutations on 6 and 8 labels, measures the exact Ewens-weighted joint moments of the two opposite mixed three-cycle types, and verifies their rational closed forms for four positive rational bias parameters. The program also probes strict monotonicity of the rational covariance ratio for a range of balanced population sizes and compares the first-order asymptotic coefficient at a large finite size.

Observed output from the package source: `PASS 622 assertions permutation_cases= 41040`. All displayed theorems for arbitrary sizes follow from the symbolic marked-cycle proof and monotone rational factorization, not from finite enumeration. The sharp root expansion coefficient was additionally checked by exact symbolic series; the standalone checker is an independent finite-data sanity check rather than a formal proof certificate.

Independent audit: not performed.
