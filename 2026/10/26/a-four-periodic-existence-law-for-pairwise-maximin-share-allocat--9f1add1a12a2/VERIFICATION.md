---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For valuations (81 all)x3, (100,100,94,94)x5, (94,94,100,100)x5, and (101 all)xp, each agent has total deficit 100 from baseline 101 per item, forcing any PMMS allocation’s bundle sizes to differ by <=1: a pair with difference >=2 can be repartitioned into bundles each worth strictly more than the smaller original bundle. For equal cardinalities k, two-bundle maximin reduces exactly to minimizing maximum deficit across all rare-item triples t; for k and k+1 the short agent compares its deficit to the minimum attainable deficit of the k-side, while long agents automatically pass. Every labeled assignment of the 3 A, 5 B and 5 C rare goods is determined by count compositions; there are C(6,3) C(8,3)^2=62720 profiles. Independent exhaustive exact-integer enumeration over all 62720 profiles at each k=4..13 returned feasible equal-size counts 28,24,8,0,0,0,0,0,0,0. For k>=13 every rare subset fits and comparisons stabilize, proving no equal-size PMMS beyond k=13. The inspected verifier also specifies 15 small-p witnesses and templates for all n=4k+r, r=1,2,3; explicit deficit feasibility and monotonic split-set argument extend each template for all k>=7. Finite enumeration is exhaustive for the bounded certificate only; the infinite periodic statement uses cardinality and k>=13 stabilization. Thus PMMS iff p<15 or (13+p)%4 !=0; first failure p=15, 28 goods, then p=19,23,..., within this particular positive-valued family.

## originality

PASS

Qualified best-of-knowledge: Haris Aziz 2026 introduces the specific valuation seed at p=39 (52 items), proving only that seed lacks PMMS. The supplied theorem characterizes every p>=0, including first family failure p=15 and recurrent restoration after a single common good. Earlier unrestricted small-market counterexamples by Gölz and Bei et al. dominate global minimum sizes, not the precise padding-family phase diagram. Aziz original full text unavailable in this run, so a stronger appendix covering all p cannot be excluded; an exact match under alternative language remains a residual risk, not an automatic fail.

## value

PASS

Adding an equally positively valued resource to a fixed four-agent fair-division instance is a natural market perturbation. The complete infinite four-periodic existence/nonexistence law shows nonmonotonicity of fair allocation under added resources and an exact first family-specific obstruction; it does not claim a new universal minimum or simply re-evaluate p=39.

The dated certificate retains the supplied scientific assessment, sources and limitations.
