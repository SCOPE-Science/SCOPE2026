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

## Actual mathematical checks

The proof verifies the full quantifier range \(n\to\infty\), fixed \(r\ge2\), \(1\le a<r\), \(c>0\), \(m_n/2^{na/2}\to c\). The mixed factorial-moment argument accounts for all multi-marked collision graphs and proves the independent-Poisson limit for all size-\(a\) antecedents jointly. Markov's inequality handles all sets larger than the threshold, while pairwise independence of world-pair witness indicators gives a second-moment proof for all sets below it.

The accompanying `checker.py` was replayed as a standalone Python 3 program with no extra dependencies. It exhaustively enumerates world tables for nine small combinations of \(q,r,m,a\), checks direct supervenience semantics against the deterministic high-probability profile whenever its witness conditions hold, and checks finite exact first/cross-second collision moments. It reports `ALL_CHECKS_OK`. Enumeration is not an infinite proof and is not used to establish novelty or priority.

## Limits of verification

The available indexed transcription of the 1998 random-database precursor was incomplete: Theorems 1–2 and 4 and substantial surrounding sections were inspected, but an inaccessible remainder could contain a multivariate refinement. No independent audit was conducted. The theorem makes no claim for nonuniform or correlated predicate extensions or growing numbers of predicates.
