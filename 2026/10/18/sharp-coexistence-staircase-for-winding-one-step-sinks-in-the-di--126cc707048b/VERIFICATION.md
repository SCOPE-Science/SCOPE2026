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
# Verification of the coexistence staircase

The standalone `verify.py` uses exact rational arithmetic for the finite-window classification, tests square-threshold equalities on both sides, and independently recomputes the Jacobian and Schur factors from the original map. Executing it returns `VERIFY_OK`.

The complete infinite proof in `RESULT.md` establishes the criterion for all integer winding modes and proves the maximum for every \(0<b<1\), \(K>0\). Finite enumerations only check the implementation, not the quantified theorem. The exact mode existence boundary has a \(+1\) multiplier, and the upper stability boundary has a \(-1\) multiplier; neither is counted as a hyperbolic sink.

The literature comparison read the full 1978 original (three pages), the full published transport statement for the same model, and the relevant kicked-rotor sections of the 2015 supplemental text. Original 1991 and 2011 articles could not be read in full; this leaves a concrete bibliographic risk. No independent mathematical audit or external certificate is claimed.
