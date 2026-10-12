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

The proof in `RESULT.md` is symbolic and applies to every finite nonempty pair of sides. It uses only the following consequences of laminarity:

1. Relative to one fibre \(S\), every other fibre contains \(S\), lies properly inside \(S\), or is disjoint from \(S\).
2. Fibres of size greater than \(2|A|/3\) cannot be disjoint, hence form a chain.
3. Distinct maximal fibres of size less than \(|A|/3\) are pairwise disjoint.
4. From disjoint sets each smaller than \(|A|/3\), if their union has size at least \(|A|/3\), greedy accumulation produces a union of size in \([|A|/3,2|A|/3)\).

These four facts give the complete lower-bound argument. The sharpness construction uses three equal left blocks and three equal right fibre types \(A,A_1,A_2\); any right set larger than one third necessarily mixes two types, and then every homogeneous left set has size at most one third.

`verify.py` exhaustively checks every binary relation for \(1\le |A|,|B|\le4\). It identifies laminar relations directly from their restricted fibres and searches all candidate subsets for a homogeneous rectangle meeting the ceiling of the one-third thresholds. It also checks the explicit sharpness family for several block sizes. The expected output is `VERIFY_OK`.

The exhaustive computation is a finite consistency check only. It is not used to extrapolate the theorem to untested sizes.

## Limits

No claim is made for \((k,1)\)-semi-equations with \(k\ge3\), for Boolean combinations, or for stronger notions requiring additional structure of the homogeneous rectangle.
