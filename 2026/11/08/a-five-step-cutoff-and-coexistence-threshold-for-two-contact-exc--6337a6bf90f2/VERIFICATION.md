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

# Reproducibility and limits

Run `python3 verify_symbolic.py` to enumerate every one of the 729 truncated occupancy profiles. It checks the exact 12 recurrent abstract states, all 12 nonempty time/period abstract classes, universal first entry by time five, and the sharp cutoff matrix for shore sizes one through six. The mathematical proof establishes that these six-size feasibility checks cover every larger shore size.

Run `python3 verify_direct.py` for an independent vertex-level evolution and multinomial-profile weight check. It exhausts all configurations on all 25 pairs of shores of sizes one through five and on the size-six by size-six pair: 663,210 labelled configurations in total. The program verifies first-entry times, least periods, recurrence populations, and the exact generating-function coefficient construction at every tested size. The logs `verify_symbolic.out` and `verify_direct.out` record actual successful executions of the included programs.

The first program is a complete finite proof certificate for the abstract transition graph; direct labelled tests are supporting checks, not proofs by extrapolation. The unrestricted claim also needs the explicit quotient and recurrence-lifting arguments in `RESULT.md`. This package has no machine-checked formal proof and no independent audit.
