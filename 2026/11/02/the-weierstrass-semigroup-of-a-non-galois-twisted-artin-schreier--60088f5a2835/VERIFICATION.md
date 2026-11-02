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

# Reproduction and limits

Execute `python3 verify_semigroup_twisted.py` with any Python 3 standard-library environment. The script checks \(324\) admissible parameter pairs, with \(p\in\{3,5,7,11,13,17,19\}\) and \(2\le d\le54\). It directly constructs the finite portion of each numerical semigroup, enumerates its gaps, verifies the claimed Apéry set, checks all generators for indecomposability, computes pseudo-Frobenius elements, and checks genus and pole identities from tame Riemann–Hurwitz.

Observed output:

`VERIFY_OK: 324 pairs; Apéry, gaps, pseudo-Frobenius, genus, tame Riemann-Hurwitz and pole-order identities`

The verifier is exact-integer arithmetic, not computer algebra over a finite field. It verifies numerical implications of the abstract curve proof; it does **not** independently prove that the given quotient curve has the asserted function field or pole orders. Those statements are proved in `RESULT.md` using the explicit group action and valuations. No infinite parameter range is certified solely by the finite tests. No independent mathematical validation has been performed.
