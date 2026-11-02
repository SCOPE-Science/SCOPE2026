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

# Verification and reproducibility

The implementation `nottingham_checker.py` defines finite fields of orders \(2\), \(4\), and \(8\) by explicit polynomial-basis multiplication and tests field-table invertibility. For every coefficient tuple it computes the composition \(f\circ f\) directly from the full polynomial substitution rule. It checks equality modulo \(t^N\), derives the leading depth from the actual coefficients, and independently checks the proposed liftability congruence modulo \(t^{N+d}\). It compares each histogram against the theorem's depth formulas and reports an assertion failure if any case disagrees.

The exhaustive configurations use \(N=3,\ldots,13\) over \(\mathbb F_2\), \(N=3,\ldots,8\) over \(\mathbb F_4\), and \(N=3,\ldots,6\) over \(\mathbb F_8\), for 21 complete finite instances. All passed. The transcript is `nottingham_verification.txt`, ending in `NOTTINGHAM_JET_INVOLUTION_DEPTH_AND_LIFTABILITY_OK`.

The experimental lifting test validates a polynomial congruence and does not itself enumerate all infinite extensions. Its equivalence to full liftability depends on the recursion proved in `RESULT.md`. Likewise, finite experiments are not proofs of the arbitrary-truncation formulas. Independent review has not been carried out.
