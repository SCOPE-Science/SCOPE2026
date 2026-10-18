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
# Reproducible verification

`verify_prelinearity.py` is standalone Python 3 standard-library source. Execute `python verify_prelinearity.py` beside this file.

Observed result:

`VERIFY_OK exact joint spectrum on all 511 compositions of 1..9 worlds; 14 large-parameter algebraic consistency tests`

The verifier constructs the partial order and principal cones separately from the counting formula, enumerates every upper set and ordered pair, tests Kripke implication failure at each world, and checks the complete three-way partition and boundary of universal prelinearity. The 511 frames are all ordered compositions of the integer totals \(1\) through \(9\), so this is exhaustive within that **finite** parameter range only. Fourteen symbolic checks of balanced larger levels test elementary normalization and nonnegativity, not an infinite enumeration. The general proof is in `RESULT.md`; no independent expert, theorem-prover, or external certification was performed.
