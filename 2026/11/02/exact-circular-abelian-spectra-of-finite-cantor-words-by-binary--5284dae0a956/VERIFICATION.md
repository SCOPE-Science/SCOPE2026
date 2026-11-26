---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Writing the one positions as B(j), ordinary gaps are 1+3^ν₂(j) and the wrap gap is 1. The telescoping sum of divisibility indicators would give 3^(n−1) at residue zero in the adjusted gap h=g−1; subtracting it gives h_0=0. Equal-length residue blocks differ by at most one in the count of multiples at each scale, and the total possible excess 3^(n−1)−1 is less than this wrap correction. Therefore every minimum block of fewer than 2^n gaps uses the wrap gap. The resulting span is 2+min_{a+b=m−2}(B(a)+B(b)); for one one it is 1. Weighting the binary digit equations by 2·3^j shows that each carry into bit j subtracts 2·3^(j−1) from B(m−2). No carry is possible before the first zero or above the leading one; if the first zero is below the leading one, the pattern initiating there, propagating through all intermediate bits and stopping at the leading one is feasible and dominates all others. This gives the claimed R including s=0 and all-ones s. Sliding windows have unit steps and complements give the minimum including length 3^n. In the sum over lengths each threshold contributes (N−d+1)+(N−d). Grouping the carry gains by leading bit and first zero gives 6^h−2·3^h+2^h at leading bit h, unchanged by omitting the all-ones endpoint. The totals follow. Frozen VERIFICATION.md and checker.py were inspected, not executed. Independent ternary-position and direct window-count sets through rank six reproduced the thresholds and totals (python -I /workspace/branches/independent_checks.py 4); this does not prove arbitrary rank.

## originality

PASS

The distinct supported content is the exact finite-circle minimum span law, with its sharp wrap criterion and solved digit convolution, yielding the complete spectrum and length-tagged total. Prior linear prefix maximality and finite-circle range/transport methods account for individual ingredients, not the carry optimum for these circles. None of the strongest inspected matches gives an equivalent or mechanically covering formula. This is a scoped best-of-knowledge decision, not an inference from the absence of hits.

## value

PASS

A complete spectrum of a canonical finite substitution family is a motivated finite-word invariant, distinct from infinite factor complexity. The exact threshold, stable across ranks and not requiring word construction or scanning over splits, together with the strict localization of minimizing arcs, gives usable extremal information. The closed total quantifies how the number of classes grows over all lengths. Sliding-window range alone would not be such a contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
