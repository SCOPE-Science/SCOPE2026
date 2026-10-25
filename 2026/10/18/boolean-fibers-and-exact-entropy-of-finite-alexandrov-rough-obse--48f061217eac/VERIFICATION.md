---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For finite T0 posets, upper neighborhood successor tests show x is free exactly when its strict upper set contains both a selected and an unselected element; all other memberships are fixed by the observed interior/closure. Each mixed successor witnesses a chain to fixed selected and fixed unselected points, making arbitrary free-bit replacement preserve observation. Non-T0 equivalent points give singletons in same fiber but empty intersection outside fiber. Independence on each cube gives conditional entropy h2(p)E|F|, with E|F|=sum_x[1−p^{d_x}−(1−p)^{d_x}] for d_x>=1; subtraction from |P|h2(p) proves stated exact entropy. Independently enumerated every topologically ordered poset n<=5, verifying the Boolean intervals and conditional statistics; not an infinite proof.

## originality

PASS

Järvinen, Radeleczki and Veres 2009 study the lattice of *distinct* quasiorder rough approximation pairs and their Alexandrov description, while later three-valued-pair work characterizes realizable pairs. Neither materially inspected text establishes the full *inverse-fiber* Boolean-interval iff-T0 criterion or the Bernoulli entropy collapse; no matching Resultary semantic finding returned. Best-of-knowledge with possible unindexed aliases.

## value

PASS

The theorem precisely measures information loss for a natural observation channel on all finite T0 posets and separates output entropy from total number of observations, a nontrivial structural/information-theoretic exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
