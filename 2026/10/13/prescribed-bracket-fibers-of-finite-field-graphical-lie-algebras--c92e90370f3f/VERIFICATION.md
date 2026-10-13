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

# Reproduction checks and limits

The embedded `verify_forest_fibers.py` contains the entire checker and requires only Python's standard library. It directly computes each prescribed edge-determinant target from all vertex pairs and independently evaluates the formula from induced supports. Its finite-field multiplication includes a separate representation of \(\mathbb F_4\) as \(\mathbb F_2[t]/(t^2+t+1)\), rather than pretending that arithmetic modulo four is a field.

Executed checks: exactly 277 target-by-target exhaustive comparisons across seven forests of up to four vertices and fields of orders two, three and four; complete summation of target fibers to \(q^{2|V|}\) for all these forests at field orders two, three, four, five and seven; verification of path and star examples for \(q=2\). Run `python3 verify_forest_fibers.py`; `VERIFY_OK` indicates those tests passed.

The general theorem for all forests and prime powers relies on the root-and-child proof in `RESULT.md`, not on finite testing. Novelty remains subject to comparison with any as-yet-uninspected equivalent historical formula. Independent audit has not been performed.
