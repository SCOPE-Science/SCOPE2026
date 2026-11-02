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

Constructed independently the 32-state nondeterministic bitwise addition machine (carry, last bits of each summand, and two adjacent-11 parities) and its subset determinization. Compared its acceptance for (0,0),(0,1),(1,1) against a separately saturated base-2 value automaton for the explicit exceptions. Exhaustive BFS reached precisely 88 product states, testing both binary transitions and the complement predicate on every reached state for each pair. The transition invariant inductively identifies paths with all possible two-summand representations; 88-state exhaustive reachability therefore proves every nonnegative target, not merely a finite range. Acceptance at zero and repeated summands is correctly handled.

## originality

PASS

Best-of-knowledge originality concerns the exact restricted result, not known underlying theory. General automatic decidability shows these exception sets can be computed, not that the specific finite complements follow as published results. The 2025 signed prefix-sum inequalities are not representations n=a+b. Same-summand pure sign-class and mixed Thue-Morse/Rudin–Shapiro cases are distinct predicates. Comparison with DOI:10.1007/s00224-025-10214-1, DOI:10.1007/s00224-019-09929-9, arXiv:2112.13627 and published semantic research searches found no established equivalent in material actually read; inaccessible full texts are not treated as proof of noncoverage.

## value

PASS

This yields a complete additive-basis classification for the classical Rudin–Shapiro automatic parity partition: exactly all missing targets for each of three natural pairwise sumsets. Exact finite complement certificates are substantially more informative than asymptotic density or decidability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
