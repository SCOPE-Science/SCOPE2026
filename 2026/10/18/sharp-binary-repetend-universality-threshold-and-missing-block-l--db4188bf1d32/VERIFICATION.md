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

Lifting exponent for 2^(2*3^t)-1 establishes ord_(3^k)(2)=2*3^(k-1), so long-division remainders traverse precisely all units mod Q=3^k. Each length-j word equals floor(2^j r/Q), r a unit. With M=2^floor(log2(2*3^(k-1))), bins for j<m have width >=3 and all nonempty with unit; for j>m there are more possible words than starts. At j=m bin width Q/M lies in [3/2,3); if Q>=2M every bin has a unit. If Q<2M, a missing bin contains one multiple r=3t, with residue u=Mr mod Q satisfying Q-M<u<M; multiplication by M permutes multiples of three mod Q, giving exact max(0, floor((M-1)/3)-floor((Q-M)/3)) missing words. The phase J_k=m for k>=2 iff Q>=2M follows from modulo-eight / bin-size endpoint argument; index densities follow from equidistribution of (k-1)log_2(3) modulo one, yielding log2(3/2) and log2(4/3). Independently generated true cyclic binary division periods for k=1..10, and counted all j<=m+1 word sets; discrepancies zero, including k=8 deficit 544 and k=10 deficit 2162.

## originality

PASS

No inspected primary theorem or relevant published finding implies the additional exact claim; the explicitly identified preexisting components are excluded from novelty. This is best-of-knowledge only, with detailed source-access and equivalence risks below.

## value

PASS

The question of exactly which contiguous binary patterns occur in the full period of reciprocals 1/3^k is a natural, previously studied digit-complexity invariant. This determines the moving information-scale critical length, not merely convergence at each fixed length, and yields an exact missing-pattern count and a nontrivial natural-density phase law. Such an exact boundary is independently useful for normality/complexity questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
