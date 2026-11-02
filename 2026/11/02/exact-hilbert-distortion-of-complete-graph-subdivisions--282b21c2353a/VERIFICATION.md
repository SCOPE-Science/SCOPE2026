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

# Reproducible checks and their limits

Execute `python3 verify_distortion.py` from the directory containing this report and the script. No third-party dependencies are needed. The observed output was:

```
CHECK_OK orders=3..11 pairwise_exact_inequalities= 12006 bfs_orders=3..10 algebraic_n4=Q(sqrt(19))
```

The script uses exact rational arithmetic and represents \(\mathbb Q(\sqrt{19})\) as pairs of fractions with exact algebraic sign comparisons. It enumerates all pairs of singleton and doubleton vertices for \(3\le n\le11\), checks both sides of the claimed sharp squared-distance ratio bounds, and compares breadth-first-search graph distances to Hamming distances for \(3\le n\le10\). It verifies the exceptional defining polynomial exactly.

The lower-bound claims for every integer \(n\ge5\), the universal symmetrization step, the representation-theoretic Gram decomposition, and the \(n=4\) minimax inequality are proved analytically in `RESULT.md`; the script is not an exhaustive proof for all dimensions. No independent or external validation has been conducted.
