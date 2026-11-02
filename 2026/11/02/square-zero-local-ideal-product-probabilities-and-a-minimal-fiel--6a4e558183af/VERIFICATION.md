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

## Exact replay

Run `python3 verify.py` beside `verification_output.txt`. A complete direct enumeration of ideals is performed in two eight-element rings with different characteristics; no precomputed ideal classification is fed into the enumerator. The program checks ring commutativity and associativity, all additive subgroups for ideal closure, the counts of ideal tuples with zero product for lengths two through five, and Gaussian-binomial examples. It prints `VERIFY_OK`, and the recorded expected output is `verification_output.txt`. The independent `verify_small.py` enumerates ideals of `Z/4`, `F2[t]/t^2`, `F2xF2` and `Z/6`; its output is `verification_small_output.txt` and also ends with `VERIFY_OK`.

## Scope of verification

The all-parameter statements and the exact equality/inequality classification are mathematical consequences of the proof in `RESULT.md`; finite enumeration is an independent consistency check, not a proof for all finite fields or for infinitely many product lengths. The minimal-cardinality argument uses the elementary classification of unital commutative rings of order four and six, not a computational enumeration of all ring multiplication tables.
