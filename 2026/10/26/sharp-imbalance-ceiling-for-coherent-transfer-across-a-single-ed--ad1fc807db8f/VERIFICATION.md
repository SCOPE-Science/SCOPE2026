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

# Verification and reproducibility

The standalone program `barbell_verification.py` requires Python 3 and NumPy. Run `python barbell_verification.py` from the directory containing the script.

The program separately assembles the full normalized-adjacency matrix and the symmetry-reduced quotient. It tests three observables at 36 small-graph/time combinations (108 checks): coherent right-clique amplitude, total right-clique probability and the exact local-vertex dark-state identity. It checks the first macroscopic peak, right-side aggregate peak and upper spectral splitting for eight larger graph sizes (24 checks), and tests both types of collective probability against the limiting sinusoid for 20 more size/time combinations (40 checks). **172 finite diagnostics passed**, with the assertions in the script establishing their numerical tolerances.

The analytic proof is independent of these finite tests and applies to arbitrarily large clique sizes with positive finite limiting size ratio. Numerical eigenvectors cannot establish the global-in-time supremum or the infinite-family limit; those follow from the four-mode decomposition and uniform spectral projection estimate in `RESULT.md`. No independent audit or experiment outside this manuscript is claimed.
