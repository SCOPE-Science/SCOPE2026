---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Let y_i be center receipts from leaf i, x_i=q−y_i, C=∑y_i. Center-to-leaf EFX becomes C+min(y_i)≥q−1. Leaf-to-center EFX with some center bundle item of zero value forces y_i≤floor(q/2); only when other y_j all vanish does y_i≤(q+1)/2, with feasible extra orientations only at q=3, giving 3b. Each y_i has binomial(q,y_i) labeled realizations. For b≥q−1 all disallowed small sums ≤q−2 include a zero component, giving polynomial correction; binomial symmetry yields exact parity rates. Independently brute-forced complete all-goods EFX for eight small (b,q) against the finite formula.

## originality

PASS

General multigraph EFX orientation papers determine existence or computational complexity, not the exact labeled enumeration or its parity-sensitive random orientation rate for uniform unit multistars. Strongly related incidence-valuation fair-orientation definitions were compared explicitly, including all-goods versus positive-only variants.

## value

PASS

EFX orientation feasibility is known, but the number and fair-coin probability of all allowed orientations are natural finer combinatorial statistics. The uniform multistar is the first tractable parallel-edge test family, and the isolated q=3 exception and parity-dependent asymptotic rate are substantive boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
