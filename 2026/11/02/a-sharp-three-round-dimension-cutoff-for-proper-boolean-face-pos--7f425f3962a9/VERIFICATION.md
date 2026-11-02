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

# Reproducible finite checks

Run `python3 verify_orbit_spectra.py` and `python3 verify_independent_types.py` with Python 3 standard library. Both are complete finite calculations, not statistical tests.

`verify_orbit_spectra.py` enumerates all possible four-cell pair Venn parameters and all feasible third-subset splits, with no sampling or memoized guesses; it computes exact nested third-move extension sets for dimensions 2–16. It checks seven distinct classes for dimensions 2–8 and stable exact types at 9–16.

`verify_independent_types.py` independently uses literal bit-mask subsets (not the orbit splitting formulas) and calculates exact recursively nested extension types for dimensions 2–9. It establishes seven pairwise different types for 2–8 and equality between 8 and 9.

The recorded outputs are `evidence/orbit.stdout.txt` and `evidence/independent.stdout.txt`, respectively. Successful verification is that both commands exit zero and reproduce the records. The mathematically complete extension to every dimension at least eight is the Venn-cell game strategy in RESULT.md. Finite computation alone is not a proof of that unbounded assertion.
