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

# Reproduction

Run `python3 verify.py` (Python 3, standard library only). Expected final line: `VERIFY_OK`. The verifier calculates the polynomial contribution of each of the 63 nonempty directed cut families symbolically, checks the six cardinality-grouped coefficients, and verifies the resulting polynomial factorization. It exhaustively enumerates all normalized diagonal-one three-by-three overlap matrices over the fields of orders 2, 3, 4, 5, and 7, using the irreducible polynomial \(t^2+t+1\) for the field of order four. It additionally checks the two-generator dimension-two condition over four fields and directly spans words in all 64 binary normalized three-by-three projector triples. Finally it enumerates all 28 binary rank-one idempotents and independently checks algebra generation of all 21,952 ordered triples, finding exactly 1,512 generating triples.

# Logical limits

The symbolic proof, not enumeration, establishes the theorem uniformly for all finite fields and matrix sizes. The source comparison concerns checked sections of the identified prior works; a plausible older paper's full text was inaccessible. No external independent audit has been performed.
