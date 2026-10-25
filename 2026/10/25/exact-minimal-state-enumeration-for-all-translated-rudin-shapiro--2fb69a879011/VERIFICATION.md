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

# Verification record

The proof reduces every residual to a unique normalized arithmetic triple and distinguishes triples for all nonnegative suffix arguments. The cutoff at \(e=\operatorname{bitlength}(c)+3\) is symbolic; no finite experimental threshold is used to prove the infinite statement.

`checker.py` (Python 3 standard library) tests three separate implementations: breadth-first closure of the normalized triple transitions; an exact short-interval evaluator using the five-consecutive-integers property; and construction/minimization of a bit-by-bit addition-with-carry DFAO that independently tracks adjacent output-bit parity. It verifies agreement for 2,048 offsets, 15,000 direct outputs, and dyadic counts at 17 exponents. Execute with `python3 checker.py`. The accompanying `checker_output.txt` records the actual output of this execution.

No formalized theorem proving, outside mathematical expert certification, or independent audit has been conducted. Exhaustive testing of finite offsets is not asserted to establish claims for all offsets.
