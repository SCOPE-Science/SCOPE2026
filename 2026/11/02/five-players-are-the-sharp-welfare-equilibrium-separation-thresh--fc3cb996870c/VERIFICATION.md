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

# Reproduction
Run `python verify.py` with the Python standard library. It exhaustively enumerates every 2-action profile for every labeled connected simple graph on 2–4 vertices and each preference vector in the grid \(\{1/4,1/2,3/4\}^{|V|}\), and checks strict Nash behavior at all social optima. The expected printout reports `3195` graph–parameter instances and `3674` maximizing profiles. These discrete tests are corroboration only; the infinite continuum is proved algebraically in `RESULT.md`.

For the five-vertex witness it enumerates all \(32\) profiles with exact fractions, determines the unique welfare maximum, verifies the profitable deviation, checks the three Nash configurations and highest Nash welfare, and independently recomputes the optimal value by path dynamic programming. The expected printout reports `23/5`, `9/2` and `3` equilibria. No external mathematical or audit certification is claimed.
