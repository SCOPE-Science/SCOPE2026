---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Uniform posterior on the set of 90 labeled deck words consistent with yes/no history. The unnormalized Bellman recursion F(B,t)=max_g (|H_g|+F(H_g,t+1)+F(N_g,t+1)) is exact. Componentwise lower/upper score-polynomial recursions take min/max over Bellman-optimal actions and independently optimal continuations. Equality of every component at root proves all deterministic optimal policies have the same polynomial; mixtures preserve it. Independently implemented a tuple-of-word-index recursion (not the source bit-mask representation), visited 11867 states, returned F=271 and identical coefficient vectors (0,0,33,30,21,5,1). Mean 271/90 and variance 7469/8100 follow; finite exhaustive enumeration is complete for the specified deck, not all compositions.

## originality

PASS

Qualified PASS: Diaconis-Graham-Spiro 2020/2021 Table 2 gives optimal expectation 3.0111 for the two-copy/three-type case, covering the mean (271/90). Their complete primary paper focuses on expected values and heuristics and does not state the coefficientwise policy-invariant score law in inspected contents. The underlying Bellman recursion is classical; same-deck optimal-law invariance remains distinctive, with risk from older implementations/technical reports.

## value

PASS

A natural small repeated-label feedback game has a nontrivial universal risk distribution across every expectation-optimal policy; separating optimal expected score from invariant higher moments is an exact mathematically useful first repeated three-label case despite small finite size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
