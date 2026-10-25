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

## Reproducible checks

The accompanying `verify.py` uses only Python's standard library. Running `python verify.py` independently enumerates every first radical element in five small prime-field cases and computes the number of commuting second elements from the rank of the induced commutator operator. The observed agreement pairs (direct count, closed formula) are \((1024,1024)\), \((41553,41553)\), \((30208,30208)\), \((30208,30208)\), and \((2375680,2375680)\) for parameters \((a,c,q)=(1,1,2),(1,1,3),(2,1,2),(1,2,2),(2,2,2)\), respectively.

## Logical checks and limits

The general proof is exact and does not depend on the finite checks: a complete split by vanishing/nonvanishing of the two middle-arrow coordinates and a rank-of-tensor-sum argument establishes the formula uniformly. The direct enumerator implements the path multiplication and computes \(\operatorname{rank}(\operatorname{ad}_X)\) from scratch; its enumerated finite fields are prime fields only, while the theorem permits all prime powers by elementary linear algebra. No finite enumeration is presented as a proof of a universal statement. Prior literature already covers polynomiality and general recursive evaluation; novelty is restricted to the explicit all-parameter formula. Independent audit: not performed.
