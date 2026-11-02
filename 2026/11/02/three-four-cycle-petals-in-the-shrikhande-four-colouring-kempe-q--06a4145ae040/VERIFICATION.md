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

# Reproducible finite verification

Run `python3 verify_cayley.py` and `python3 verify_latin.py` from the directory containing these files; both require Python 3 standard library only.

The Cayley-model checker verifies exactly 16 independent four-sets, 10 exact covers, 240 named proper colourings, 1008 Kempe adjacency edges, degree counts 216 of degree eight and 24 of degree twelve, all 240 eccentricities, all 28,680 unordered pair distances and the quotient structure. The Latin-model checker independently constructs a 48-edge graph from the cyclic order-four Latin square, classifies all independent four-sets into rows, columns, symbols and parity blocks, produces exact covers with a different recursion, identifies Kempe adjacency by 28,680 pairwise comparisons, and recomputes distances and quotient. It checks an explicit 16-vertex isomorphism between the two graph models using all 120 unordered vertex pairs. Both programs terminate with a printed `PASS` only after their assertions succeed.

Execution produced `CAYLEY_KEMPE_PASS` and `LATIN_PAIRWISE_KEMPE_PASS`, together with identical intermediate summaries. All calculations use exact finite integer and set operations. The claim concerns exactly this finite graph; no infinite-family extrapolation and no independent scholarly audit are implied.
