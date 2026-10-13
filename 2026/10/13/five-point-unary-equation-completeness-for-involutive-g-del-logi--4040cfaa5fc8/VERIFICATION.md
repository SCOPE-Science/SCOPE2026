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

The checker `verify.py` uses only Python's standard library. From the directory containing this document, execute `python3 verify.py`.

It exhaustively closes unary functions over the finite algebras of sizes \(2\) through \(17\) under involution, Gödel conjunction, and Gödel implication, then checks equality against independently built piecewise normal-form sets and their expected cardinalities. It also evaluates the midpoint and strict-left characteristic terms on the relevant small chains.

An output ending with `VERIFICATION_OK` is a reproducible finite check, **not** a verification of the continuum argument or an independent audit. The proof in `RESULT.md` is the evidence for all unbounded statements; no external formal certification has been performed.
