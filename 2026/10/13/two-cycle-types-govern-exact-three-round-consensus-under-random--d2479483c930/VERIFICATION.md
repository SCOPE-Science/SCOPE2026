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

From a directory containing the embedded `verify.py`, run `python verify.py`. The program uses only the Python standard library. It enumerates all \(105\) eight-vertex perfect matchings, explicitly forms three successive averaging steps using eight-by-eight integer path-count arrays, and tests equality with the all-ones array before division by \(8\). It enumerates the complete \(105^2\) conditional sample space for a fixed first matching, checks the class sizes \((45,12,48)\), checks the successful third-match counts \((0,288,192)\), and confirms \(480/105^2=32/735\). It independently repeats the total count with another first matching.

The computation is an exact finite-domain check, not a substitute for the structural proof. The proof itself establishes coverage of every matching via inclusion-exclusion, contraction to four supervertices, and exhaustive classification of loopless two-regular multigraphs on four vertices. No claims are made about general numbers of agents, nonuniform sampling, approximate convergence speed, or data-specific hitting times. Independent audit has not been performed.
