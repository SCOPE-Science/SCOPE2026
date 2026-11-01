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

`CHECK.py` uses only Python's standard library. Execute `python3 CHECK.py` in a directory containing that file. The successful exact-enumeration run printed `CHECK_OK lengths=8..19 normalized_masks=2240 ambiguity_classes_at_19=1` after enumerating every admissible normalized reversal class at lengths eight through nineteen.

The verifier uses two separate parametrizations (four breakpoints and direct five-part integer compositions), checks their full signature-fiber dictionaries for equality, and evaluates each integer autocorrelation by both bit counts and dot products. It asserts all per-length counts, the sole two-element fiber, and the complete nineteen-term correlation vector. No external data, randomness, or numerical tolerance is used.

A separate exact polynomial identity in `RESULT.md` checks that the two witness masks have the same continuous Fourier magnitude. The abstract Fourier-reduction argument and the finite exhaustive search are both required for the full first-ambiguity theorem. Completeness holds only within the explicitly defined finite parameter universe; no extrapolation to arbitrary lengths or wider signal classes is made. Independent auditing has not been performed.
