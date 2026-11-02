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

The theoretical claims are proved in RESULT.md. The independent-of-proof finite checker, `verify.py`, is a standalone Python 3 script requiring only the standard library. From the directory containing these two files run `python3 verify.py`. The exact-rational output is:

`VERIFY_OK exact_homogeneous_profiles=10236 exact_deviation_comparisons=197226 cycle_equilibria=99 three_voter_phases=15`

The program exhausts the \(n^n\) directed delegation functions for each integer population size \(n=2,3,4,5\) and three exact-rational casting probabilities, with equally spaced opinions and tolerance strictly above the stated bound. It separately checks the strict-below, equal-to, and strict-above parameter regions in the three-voter phase diagram for five exact-rational casting probabilities. It recomputes expected utilities from the finite orbit definition and enumerates every unilateral change; no external data or solver is required.

The program does **not** certify the theorem for all population sizes or all real parameters. Completeness of the general proof rests on the symbolic uniform penalty bound and explicit cycle/in-tree rerouting cases, not on enumeration. All source-derived distinctions and the claim of novelty are subject to independently reproduced literature checks.
