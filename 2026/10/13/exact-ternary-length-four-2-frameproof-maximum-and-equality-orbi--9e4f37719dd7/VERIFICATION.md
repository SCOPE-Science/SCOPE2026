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

# Verification

The standalone `artifacts/verify.py` reconstructs all \(81\) ternary length-four words and tests the \(2\)-frameproof condition directly on each triple. Because independent symbol relabelings can send any chosen codeword to \(0000\), exclusion of a \(13\)-word code reduces without loss to an exhaustive search over codes containing \(0000\). The recursion explores increasing subsets and intersects the exact set of legal later words after every selected pair; it therefore prunes only branches that already contain a forbidden triple or cannot reach the requested cardinality.

The program finds no normalized size-
\(13\) code and exactly \(832\) normalized size-
\(12\) maxima. Coordinatewise translations reconstruct \(5{,}616\) labeled maxima, checked again by the incidence identity \(832\cdot81=5{,}616\cdot12\). It then generates the full natural group using adjacent coordinate swaps and adjacent symbol transpositions and obtains exactly two orbits, with sizes \(432\) and \(5{,}184\); their stabilizer orders are \(72\) and \(6\). Every enumerated maximum is independently rechecked from the direct triple predicate.

The final census digest is `b064067a522954ba8b0f3150ebc11b264dc601831ded0e41b0baa614e7bdc293`.

Limits: this verifies only the stated finite ternary length-four claim and its natural-equivalence classification. It does not prove a general alphabet-size bound.
