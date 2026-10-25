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

For m,n>=1 and target alpha>=m, let k=alpha+1,d=n+1. Two letter permutations on B=[k]xZ_d are a=(sigma,1), b=(tau,0) with sigma k-cycle and tau transposition. The first-coordinate permutation of ab is a (k−1)-cycle fixing one vertex, so a^k and (ab)^(k−1) yield pure counter shifts k and k−1; gcd 1 generates all Z_d for arbitrary d and hence full S_k x Z_d. Reachability and pairwise state-distinguishability show inputs have exactly m,n finals in their minimal DFAs; accepted B suffix projections equal Stab(k), whose preimage union of F_A is [k−1], yielding quotient asc=alpha and minimality. Low alpha<m follows published unary positive range [1,mn] using duplicate binary letter; empty cases are zero and nonemptiness excludes zero for m,n>0. Independent group closures for (k,d)=(2,2),(3,3),(4,3),(5,2) reproduced k!d and stabilizer sizes. Infinite claim follows coprime shifts, not enumeration.

## originality

PASS

Best-of-knowledge originality after comparing exact mathematical implications, not titles. The fixed-binary theorem implies the previously established unbounded unrestricted spectrum but not conversely. The novelty is replacing separate counter generator c by coupling it to a k-cycle and extracting pure increments k and k−1. Unary existence supplies only low values and the optimality obstruction, not new binary high-range witnesses.

## value

PASS

Determines the exact minimum alphabet size at which every positive quotient accepting-state target can occur, sharpening the previously established unrestricted 3-letter high-range realization. An explicit two-generator group embedding is a meaningful state-complexity construction, not mere parameter relabeling; unary upper bound proves sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
