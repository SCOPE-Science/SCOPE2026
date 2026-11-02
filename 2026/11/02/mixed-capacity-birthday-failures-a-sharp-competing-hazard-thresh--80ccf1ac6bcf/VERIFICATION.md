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

The finite coefficient identities were tested against an independently formulated exact rational-state recursion and direct enumeration of ordered throws. The accompanying `check.py` was executed using Python 3 and completed 2,183 assertions, including all capacity mixes through eight bins for selected arrival times, direct word enumeration through four bins, probability conservation, and numerical checks of the critical formulas.

The infinite-size conclusions are proved analytically in `RESULT.md` by an exact independent-Gamma-clock embedding, Taylor expansion with uniform remainders on compact scales, and de-Poissonization using a martingale maximal inequality. Computation is not used as a substitute for these arguments. The reported approximate balance parameter is based on numerical quadrature and is not an interval certificate. Historical priority has not been independently audited.
