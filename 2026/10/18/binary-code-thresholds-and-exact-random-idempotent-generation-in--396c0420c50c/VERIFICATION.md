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

The general claim was reconstructed from the explicit multiplication law, the idempotent-coordinate equation, the diagonal interpolation criterion, and the commutator block-surjectivity calculation. Distinct-label conditions and the zero-loop boundary were checked algebraically. The count for each off-diagonal block uses a surjective linear map on the hyperplane of available idempotent coordinates; the free complementary column accounts for the factor of \(q^{m_{ij}}\).

Execute `python3 check_idempotent_generation.py` in the package directory. A direct finite-field span-closure implementation checks 14 small parameter cases, including the fields with two, three, and four elements; parallel arrows; opposing arrows; loops; and oriented paths/cycles. Expected final line: `ALL_IDEMPOTENT_GENERATOR_CASES_PASSED 14`.

Finite exhaustive tests do not prove the formula outside those cases. The full proof is in RESULT.md. Mathematical priority relative to every older presentation of conditional idempotent generation has not been independently settled. No independent audit has been performed.
