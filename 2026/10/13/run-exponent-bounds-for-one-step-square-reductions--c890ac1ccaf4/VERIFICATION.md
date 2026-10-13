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

Run `python3 verify.py`.

The checker enumerates all \(4094\) nonempty binary words of lengths at most \(11\) and all \(3279\) nonempty ternary words of lengths at most \(7\). For every word it computes one-step square-reduction outputs directly, independently constructs maximal match intervals for every root length, and checks equality of the two counts.

For every match interval it reconstructs the corresponding maximal periodic factor, computes its minimum period, verifies divisibility into the square-root length, and confirms that the factor is one of the word's standard runs. It then checks
\[
\deg^+(W)\le\sum_R\left\lfloor\frac{e(R)}{2}\right\rfloor.
\]
The checker also confirms that `00100` has two distinct square-reduction outputs but only one distinct square factor.

The finite census is not used to infer the theorem for arbitrary length. Universal validity comes from the proof in `RESULT.md` and the cited published run-exponent bounds. Independent audit has not been performed.
