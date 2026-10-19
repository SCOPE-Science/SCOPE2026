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

The standalone `verify_rs_first_repetition.py` requires only the Python standard library. Running `python3 verify_rs_first_repetition.py` yields `PHASE_OK`, `CODING_OK`, `COLLISIONS_OK`, and `VERIFY_OK`. The phase check enumerates all adjacent pairs in the four-state morphic word (eight pairs) and every length-eight factor arising from their two-block expansions. It confirms 24 phase-even factors, 32 phase-odd factors, and zero shared factors. Its exhaustive coverage follows from the substitution closure argument in RESULT.md.

The independent digit-arithmetic generator agrees with the four-state morphism for 131072 positions. Direct substring comparisons establish the exact first collision and its unique earlier occurrence for every length from 1 through 1024 and for lengths 1025, 1536, 2048, 2049, 3073, 4096, 4097, 6145, and 8192. The base cases are contained in this range. The infinite-length inference uses the explicit induction in RESULT.md, not finite extrapolation.

The checked theorem is limited to the standard binary Rudin–Shapiro word. No external independent audit has been conducted.
