---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For k>=2, n>=4k, the marked cycle power has 2k-regular adjacency and reflection symmetry: every 1-WL class is a union of S_d={d,-d}. At the first refinement, S_1..S_k are separated from more distant shells, and at round 2 the counts into the near-root colour are 2k-d-1 (1<=d<=k) and 2k-d+1 (k<d<=2k), with the n=4k antipodal correction. The induction identifies each newly exposed tail shell by the minimum already individualized shell d-k among its neighbours; all shells beyond rk+k remain indistinguishable. This yields exact wavefront partitions and R=max(2,ceil((floor(n/2)-1)/k)) for n>=4k+1. At n=4k, S_(2k-1) and S_(2k) collide at round 2 and split at round 3 by adjacency to S_(k-1). Reflection acts transitively on every final S_d and refinement cannot split them; automorphism orbits therefore equal shells. Independent full 1-WL implementation checked all intermediate partitions and exact depths for 342 parameter pairs (k=2..10, n=4k..9k+7), including seam and odd n. This finite test corroborates rather than proves all k,n.

## originality

PASS

The general all-n rooted cycle-power intermediate partitions, exact stabilization depth and n=4k discontinuity are a sharper statement than existing prime-order marked-circulant orbit results or general 1-WL literature; best-of-knowledge PASS, not an absolute priority certificate.

## value

PASS

Counting-colour-refinement stabilization depth is a natural algorithmic complexity parameter for a canonical symmetric graph family. The complete phase transition from n=4k to n=4k+1 and all intermediate partitions provide useful exact benchmarks, beyond routine orbit-equality observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
