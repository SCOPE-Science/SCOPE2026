---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The cooling process propagates from all cooled vertices then selects a new source. A first source of eccentricity e forces finishing by e+1; for b=1 the diameter is 3 and for b>=2 it is 4. For T_{2,1}, distance-three survivor counting forbids a fourth round; b=2 leaves at most one remote outer leaf before selecting the fourth source, prohibiting five rounds. For b=3,a=1, two remote outer leaves force the second source to be the sole short leaf, after which no third source satisfies distance/survival constraints. Explicit legal source tuples (x_A,u,y_B) and (x_A,y_B,u,x_C), or (x_A,u,v,x_B), and named survivor leaves certify all matching lower bounds. Deleting arms proves the two minimal mixed witnesses. Independent exhaustive memoized cooled-set process enumeration reproduced the formula on all 35 parameter pairs with 1<=a,b<=6 and a+b>=3; this is ancillary to the all-parameter distance argument.

## originality

PASS

Bonato et al., How to cool a graph, Theorem 4, treats even numbers of equal-length spider legs and supplies a known b>=4 diameter-attaining specialization. That portion is explicitly prior-covered and is not separately claimed as a new principle. The mixed short/long threshold including b=3,a>=2 and the exceptional b=3,a=1 configuration is not stated or obtained by same-length hypotheses. Cooling graph products (2026) primarily treats graph products and disconnected constructions; its abstract does not provide this mixed spider classification, while its full text remained inaccessible with Oxford vpn_disconnected. No indexed Resultary record supplied the present cooling invariant for these spiders.

## value

PASS

The entire one-/two-edge mixed spider family is a natural first unequal-arm extension of the foundational cooling theorem. The exact sharp exceptional cases and the nine-vertex T_{2,3} minimal five-round witness isolate how extra short arms change the diameter attainment threshold. The b>=4 branch is not independently new, but the complete mixed classification is a motivated structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
