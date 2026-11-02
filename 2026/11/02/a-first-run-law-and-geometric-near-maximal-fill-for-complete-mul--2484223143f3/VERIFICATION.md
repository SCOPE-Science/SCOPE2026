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

Run the standard-library-only program \(\texttt{python3 verify.py}\). It exhaustively compares the exact predicted probability mass function with random-order graphical elimination for every part-size vector having 2–5 parts, each part of size 1–4, total size at most 7. It checks 1,584 exact-rational Schur-complement/graphical-fill pairs on four explicit graphs, plus rational normalization, extrema and balanced-parameter formulas for several larger cases. The observed result was `VERIFICATION_OK 2231 grouped exact assertions`.

The code deliberately checks finite instances, not every possible graph size; the symbolic proof in `RESULT.md` establishes all quantified claims. No external proof certification or independent scientific audit has occurred. The uninspected 1993 minimum-fill technical paper leaves a publication-priority risk, but does not affect the displayed finite computations.
