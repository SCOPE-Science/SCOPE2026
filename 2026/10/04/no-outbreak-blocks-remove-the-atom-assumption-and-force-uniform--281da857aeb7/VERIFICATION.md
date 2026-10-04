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

The proof uses the published state update directly. Since every susceptibility multiplier lies in \([0,1]\), a season with \(\tau<1\) has \(R_e<1\) and hence no outbreak. Repeating the no-outbreak population shift \(r-1\) times sends every probability vector to the all-nonimmune class. Repeating the immunity recursion shows that the final immunity vector uses only within-block drift marks, so two chains driven by the same low-transmissibility block coalesce exactly.

The packaged `verify.py` uses exact rational arithmetic to replay those updates for multiple memory lengths and distinct initial states, and checks the closed product expression for the terminal immunity vector. It returns `VERIFY_OK` when all checks pass. These finite checks guard implementation and indexing errors; the theorem for arbitrary \(r\) is proved algebraically in `RESULT.md`.

The total-variation rate follows from the global minorization with mass \(\beta^{r-1}\). No claim of rate optimality is made, and serial dependence between seasons is outside the proved scope.
