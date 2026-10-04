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

The verifier implements the channel directly on strings and, separately, the closed zero-gap formula. For every \(2\le n\le10\), it constructs all binary length-\(n\) source words, permits exactly one deletion of \(0\) and zero or one unequal adjacent transposition in either order, collects all received words, and compares each inverse-ball size with the formula. It also checks the exact worst-case value and the full extremizer classification.

A second arithmetic check optimizes the support-form expression over every feasible \((m,p,e)\) pattern through \(n=200\) and compares it with \(\lfloor n^2/2\rfloor-n+2\). These finite checks are corroborative. The universal theorem rests on the combinatorial proof in RESULT.md.

No claim is made about multiple deletions, multiple adjacent transpositions, or nonbinary alphabets.
