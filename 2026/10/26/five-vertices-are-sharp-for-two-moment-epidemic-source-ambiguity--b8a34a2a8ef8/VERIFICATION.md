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

Run `python verify.py` with Python 3 and SymPy 1.14; compare its canonical JSON standard output with `certificate.json`. The verifier enumerates all bond states for paths of orders 2–9 at the rational probabilities 1/4, 1/2 and 3/4; checks both population moments against the arm-tail formulas; verifies the n=3 and n=4 polynomial identities, the n=5 resultant and exact rational root bracket; and checks several symbolic expansion cases plus integer slope inequalities. The analytical proof in RESULT.md establishes the universal quantifier over all n at least five without relying on finite computation. These checks are self-review only; there is no independent validation.

## Model limits

Unknown transmissibility is constant over replicated outbreaks and edge successes are independent. This is not a validation of general SIR dynamics, noisy finite-sample estimators, or full-law indistinguishability. The published-literature originality comparison is bounded by the primary texts inspected and the available search results; potentially equivalent formulations may exist.
