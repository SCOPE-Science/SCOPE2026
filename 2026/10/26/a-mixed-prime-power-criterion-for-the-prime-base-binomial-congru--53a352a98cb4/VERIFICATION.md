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

## Exact checks

Execute `python3 verify.py` using Python 3 and only the standard library. It independently constructs the binomial coefficient in full at each finite input, tests the original modulus, and compares it with the criterion. The test includes 106 exact parameter combinations under the documented bound, three larger examples, and a fourth-layer counterexample to omitting the Davis--Webb correction. Each tested parameter is covered by the theorem, but exhaustive finite testing is not a proof over all exponents.

## Mathematical verification

The proof explicitly relies on the established Davis--Webb reduction for p>=5, Lucas's mod-p theorem, Legendre's factorial valuation formula, uniqueness of Teichmüller roots modulo p-powers, and CRT. Their hypotheses and edge cases are spelled out in RESULT.md. No independently produced machine proof or expert audit is asserted.

## Limits

The complete full text of arXiv:1301.0252 was unavailable; its exact theorem statement was checked from the arXiv abstract and independently indexed abstracts. Previous research file summaries establish related findings but cannot prove no hidden stronger covering result exists. Independently audited status remains not performed.
