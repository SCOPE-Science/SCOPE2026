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

The finite-symbolic reduction in `RESULT.md` turns all column and length quantifiers into four explicit exponent blocks and four cyclic remainder lengths. Reconstructing these blocks gives exactly the table in the proof. For positive integer sequences with period at most four, the valuation comparisons in the proof derive the required divisibility at *every* prime, rather than at just the displayed sample bases.

`verify.py` independently computes column exponent blocks from the five-element starting word and checks all cyclic remainder sums. It also checks 780 small-period valuation words, 100 column residues, and 258300 finite direct generalized-binomial exponent cases. Reproduction: `python3 verify.py`; expected stdout is stored in `verification_output.txt`.

The numerical checks are supplementary, and do not establish the unrestricted theorem without the stated periodicity and valuation arguments. No external or independent audit has been performed.
