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

# Reproducibility and limits

Run `python verify.py` with Python 3 and only its standard library. The program operates on exact integers reduced modulo three. It checks idempotence, commutativity, bijective/involutive right translations on the 81-point canonical example, all 531,441 ordered triples for right self-distributivity, an explicit nonzero medial defect, and generation by four marked elements. It enumerates all 531,441 ordered quadruples of projected ternary vectors, finds exactly 303,264 affinely independent quadruples, and confirms the lifted generating count by multiplication by 81. It samples 60,000 deterministic pseudorandom polynomial quadruple tests across dimensions three through five and verifies 60 further generated-subquandle closures with exact finite operations.

The expected final line begins `VERIFY_OK:`. The checker output observed for the supplied exact code was:

`VERIFY_OK: 81-point quandle; 531441 distributivity tests; 531441 projected quadruples; cubic cocycle and defect; generating tuples`

These finite experiments are not an exhaustive proof in unbounded dimension. The proof instead uses a field-characteristic-three algebraic identity, the nonzero alternating-three-form defect and a vector-space rank count. The reader should evaluate those proof steps independently. No external independent audit was requested or performed.
