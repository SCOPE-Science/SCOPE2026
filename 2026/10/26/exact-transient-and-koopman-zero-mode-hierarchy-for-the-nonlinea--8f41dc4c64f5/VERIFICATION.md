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

# Verification of finite examples and universal proof boundaries

Run the included standalone standard-library script with `python3 verify.py`. In the current analysis, it returned exactly:

```
VERIFY_OK states_examined_even= 87376 ring_sizes=3..16 offdiagonal_pair_vertices= 12 cyclic_pair_components= 2
```

The checker enumerates all configurations for ring lengths \(3\) through \(16\), tests bijectivity for odd sizes, compares complete finite-state functional-graph entrance times with the formulas for even sizes, checks iterate-image ranks, verifies multiplicities obtained from Koopman image-rank differences, and recomputes the off-diagonal pair graph. All tests passed.

**Universal proof checks.** The collision graph has exactly twelve admissible off-diagonal vertices; every recurrent strongly connected component is bipartite and enforces one-parity support. The exact identity \(z^m-1=(z^u-1)^q\), with \(m=qu\), \(u\) odd, and \(q\) a power of two, gives rank \(m-\min(t,q)\) to the cyclic binary difference operator. This proves image ranks for all even sizes without relying on finite extrapolation. The Koopman rank formula \(\operatorname{rank}K^t=|F^t(X)|\) and second rank differences prove nilpotent block counts universally.

**Unverified limits.** No independent auditor has checked this package. The finite checker does not certify priority, arbitrary other local rules, or the nonzero Koopman eigenvalue multiplicities.
