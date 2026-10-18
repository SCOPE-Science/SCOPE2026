---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let p_i denote three oriented branch-to-branch path sums of lengths a<=b<=c. A chain extension on cycles forces q_i=z+x,z+y,z in rank-two homology. For fixed cointegral basis B, distributing each q_i equally along the path is optimal and turns ||s|| into inf_z max(||z+x||/a,||z+y||/b,||z||/c). The dimension-two isometry (u,v)->(u+v,u-v) maps l1 balls to l_infty boxes, where triple intersection is equivalent to pairwise intersection, giving max(||x-y||/(a+b),||x||/(a+c),||y||/(b+c)). Cointegral bases correspond to independent integral coordinate columns u,v. All ||u||1,||v||1,||u-v||1>=1, at least one >=2, and unimodular witnesses put 2 on the largest denominator b+c. Therefore exactly max(1/(a+b),2/(b+c)); rational witness/centers suffice for every subfield F⊂R. Independently tested 120 sorted length triples through length 8 and rational optimization. The infinite statement follows from the integer lower bound, not finite cases.

## originality

PASS

Hofmann–Löh first define algebraic gnarledness and compute one circle (Example 7.13), but their full arXiv text has no three-path theta classification. A published cactus-graph reciprocal-girth formula assumes edge-disjoint cycles; theta graphs share paths and are not cactus. This formula has a genuine second b+c scale and equilateral theta G=2/g rather than 1/g. General graph cycle-space projection constants use nonidentical invariant definitions; no stronger covering relation identified.

## value

PASS

Theta is the smallest natural rank-two graph with overlapping simple cycles, supplying a sharp boundary and phase transition beyond the cactus reciprocal-girth rule. The exact formula answers a motivated new chain-extension norm question for a standard graph family and can guide later series-parallel classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
