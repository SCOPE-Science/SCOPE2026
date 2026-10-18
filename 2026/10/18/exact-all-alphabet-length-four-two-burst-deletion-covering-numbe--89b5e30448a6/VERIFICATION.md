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

# Reproducibility

Run `python3 verify.py` from the extracted package. The program uses only Python 3 standard-library modules. It regenerates all seven integer-indexed local templates, every constructed alphabet size from 2 through 100, and checks exact covering/cardinality/multiplicity claims.

Expected output begins with `VERIFY_OK templates=7 q=2..100`. The construction and proof, not finite enumeration, establish all integer alphabet sizes.

The proof's assumptions must be kept exact: one codeword consists of four ordered symbols, and deletion removes one pair of consecutive coordinates, leaving the ordered outputs `(c,d)`, `(a,d)`, `(a,b)`. The lower bound counts at most three **distinct** outputs per source. The verifier checks the matching upper constructions; it does not certify unrelated channels, independent review, or literature novelty.
