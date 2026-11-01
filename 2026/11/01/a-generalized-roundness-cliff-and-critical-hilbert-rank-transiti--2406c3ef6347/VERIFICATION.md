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

# Reproducibility of the folded-cube spectral and embedding-rank calculations

Execute `python3 verification/check.py` using only the Python 3 standard library. The program independently builds every folded graph, executes all-pairs breadth-first searches, checks the closed shortest-path formula, and recovers each powered-distance eigenvalue coefficient both from a full signed Walsh character sum and from the exact binomial Krawtchouk formula. It checks all character-weight groups, the full critical nullities and the corresponding affine Euclidean ranks. It also checks rational fourth-power bounds and an exact rational stationary value used in the analytic proof.

Observed output on the checked package:

```
EXACT_OK F_6 vertices=32 classes=5 endpoint_nullity=15 rank=16
EXACT_OK F_7 vertices=64 classes=6 endpoint_nullity=35 rank=28
EXACT_OK F_8 vertices=128 classes=7 endpoint_nullity=1 rank=126
NUMERIC_DIAGNOSTIC F_6 threshold=0.482147185182
NUMERIC_DIAGNOSTIC F_7 threshold=0.516584374301
NUMERIC_DIAGNOSTIC F_8 threshold=0.135372723557
CERTIFICATE_OK integer_spectral_rows=18 full_graph_distances=21504 exact_inequalities=passed
```

The spectral table, combinatorial multiplicities, rational root-location bounds, monotonicity arguments, and global sign comparisons constitute the mathematical proof in RESULT.md. The numerical bisections are diagnostic and are **not** treated as rigorous interval certificates. The program does not verify the general analytic inequalities for all real exponents by enumeration. It does not assess any graph size outside the stated set, and no independent audit was conducted.
