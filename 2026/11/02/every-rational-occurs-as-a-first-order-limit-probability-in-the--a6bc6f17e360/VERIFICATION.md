---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Av(231,312,321) consists exactly of direct sums of decreasing layers of size one/two, i.e. Fibonacci compositions. For each denominator b≥2 the b words W_j=112(22)^(j−1)12(22)^(b−j)22 have identical weight, exactly three 1s and 2b+2 2s, and are pairwise cross-bifix-free. Replacing the earliest occurrence by another W_j preserves total permutation size and cannot create an earlier match, yielding exact equinumerosity of all b earliest-hit types at every finite n. The inversion relation plus layer representative and successor predicates express each fixed word and its earliest occurrence in FO with position/value orders. Fixed prefix composition measures tend to iid weights φ^(−1), φ^(−2); independent disjoint windows imply any designated word eventually occurs with probability→1. Therefore every rational a/b∈[0,1] is an FO limit probability. Independent cross-bifix/weight check for b=2..15 corroborates; the infinite argument is structural.

## originality

PASS

Best-of-knowledge originality of the final exact statement, with actual published-result comparisons rather than title matching; no inspected source mathematically implies the full stated result. Inaccessible closely related texts are explicitly retained as priority risks; failed search is not novelty proof.

## value

PASS

A natural first-order limit-probability spectrum of a canonical Fibonacci permutation class; strengthens previously established dense-spectrum and convergence theorems to exact containment of all rationals, using reusable first-hit equal-weight coding with finite-size symmetry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
