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

`verify_strip3.py` is standalone Python 3 code with no nonstandard dependencies. Its `run()` routine compares the six formulas for the three edge-orbit columns with 80-term-each-side Green-kernel sums to error below \(2\times10^{-13}\). It independently constructs finite strip incidence Laplacians, grounds a vertex, solves six exact-rational linear systems (all three orbit types for finite lengths eleven and fifteen), and compares their central-edge projection currents with the derived infinite formulas to tolerance \(0.02\). It checks the strict ordering of the orbit norms. The checker prints `VERIFY_OK` upon success.

The finite-graph checks confirm asymptotic convergence but do not certify infinite estimates; the latter are proved by the spectral Green-function series identities in `RESULT.md`. No code assesses external independence or literature completeness. The numerical threshold is used only to test diagnostics, not as an algebraic proof.
