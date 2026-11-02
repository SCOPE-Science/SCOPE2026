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

# Reproducibility checks

Execute `python3 verify_choice.py` with Python 3. The program needs only the standard library, and rederives its occupancy states, its offered-pair probabilities, its greedy-constrained Bellman decisions and its alternative policy expectations.

The exact assertions establish the two rational differences in `RESULT.md` and strict positivity of the root advantage. Its float pass is exploratory policy selection only: every proposed greedy decision is subsequently assessed via exact `fractions.Fraction` arithmetic, and the final root values are exact rational solutions. Finite enumeration here is exhaustive for this fixed nine-vertex graph by the part-symmetry reduction; it is not an exhaustive classification of other graph families.

The companion analytic argument proves greedy optimality on every complete bipartite graph; the program does not serve as a substitute for that infinite-family coupling proof.
