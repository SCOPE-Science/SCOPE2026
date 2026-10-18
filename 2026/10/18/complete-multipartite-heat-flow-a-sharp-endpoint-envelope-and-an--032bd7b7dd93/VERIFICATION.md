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

# Reproducibility and boundaries

The result uses the counting-measure unnormalized Laplacian of a finite complete multipartite graph. Its spectral projector decomposition and all row entry signs are proved in `RESULT.md`; those analytical arguments establish the statements for every admissible part-size list and every positive time. The numerical checker `check.py` provides finite supplementary verification by an independently constructed matrix exponential and by solving sample pairwise row-crossing equations.

Run `python check.py` in an environment with NumPy and SciPy installed. It prints the number of passed consistency assertions. A finite collection of tests does not establish exact all-graph claims, global time-uniform extrema, or mathematical priority.

An independent mathematical or bibliographic audit has not been performed.
