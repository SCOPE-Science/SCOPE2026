---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At each p^j level, choosing a subset of 1,2,...,2^a is equivalent to an integer x_j in [0,S], S=2^(a+1)-1. Setting y_j=2x_j-S turns equal partition sums into sum y_j p^j=0 with every y_j odd and |y_j|<=S. Since p>2^a, S<2p and S+1<2p. Modulo p, y_0 must be a nonzero odd multiple of p of magnitude below 2p, so y_0=-epsilon_0 p. After division by p, p divides y_1-epsilon_0; that difference is even and has magnitude below 2p, hence it vanishes and y_1=epsilon_0. Repeating gives y_{2k}=-epsilon_k p and y_{2k+1}=epsilon_k independently for each pair. Thus there are 2^((b+1)/2) oriented partitions, and global sign reversal is exactly block swap with no fixed point, leaving 2^((b-1)/2) unordered partitions. The verifier independently enumerates bounded signed-coefficient solutions for representative upper-strip cases and a below-strip counterexample.

## originality

PASS

Rao--Peng and Mahanta--Saikia--Yaqubi supply existence theory for Zumkeller numbers and the two-prime family, while a published Resultary finding gives the exact partition count only for the exponent-one family 2^a p. In the upper strip that special case equals one. No inspected source gives the all-odd-exponent multiplicity 2^((b-1)/2) or the rigid adjacent-pair sign classification. The submitted carry argument therefore extends the known b=1 count and refines the existence theorem throughout the natural upper strip.

## value

PASS

Partition multiplicity is the natural refinement of Zumkeller existence. The theorem classifies every equal-sum divisor bipartition across an infinite, structurally distinguished upper strip and extends the known exact b=1 count to all odd exponents by a rigid signed-carry mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
