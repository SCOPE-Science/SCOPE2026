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
The proof was reconstructed from the definitions and checked in three layers.

1. Counting: every length-three word has at most three distinct one-deletion descendants, giving \(D(q,3,1)\ge\lceil q^2/3\rceil\).
2. Structural translation: two reverse orderings of a distinct-symbol triple cover both directed versions of all three underlying edges; a word \((a,b,a)\) covers \((a,a)\), \((a,b)\), and \((b,a)\).
3. Finite replay: `verify_odd_q.py` verifies explicit triangle decompositions and full ordered-pair coverage for \(q\in\{3,5,7,9,11,13\}\), and checks the residue-class arithmetic over many odd values.

The finite replay does not certify the published all-order quadratic-leave theorem. That theorem is the external mathematical ingredient supporting the infinite-family existence step. Even \(q\) is not covered by the claim.
