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

# Computational checks

Execute `python verify.py` with Python 3 and SymPy installed. The script evaluates the neutral theorem's formulas with exact fractions and independently builds all \(2^n\)-state transition matrices of the original stochastic birth–death model for \(n=3,4,5\). It then solves rational absorbing-state linear systems for the fixation probabilities, not merely the reduced expectation chain.

Successful completed check counts: 48 exact rational stationary-vector comparisons, 48 strict ordering and difference identities, 31 independently calculated full-state fixation probabilities, 15 numerical checks of the scaling limit, and 98 exact shortest-block simplifications. The exact full-state tests include \(\tau=1,2,3\) except \(n=5,\tau=3\).

The finite tests are not an exhaustive proof for unbounded network size or duration. The analytic derivation in `RESULT.md` establishes those claims. Numeric asymptotic samples are supplementary and use a declared tolerance; no claim of exact numerical certification or external validation is made.
