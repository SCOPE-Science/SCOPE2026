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

The artifact `checker.py` uses the Python standard library, NumPy, and SciPy. Run `python3 checker.py`. The completed test replay returned `PASS: 1993 supplementary finite spectral and asymptotic assertions` and displayed the limiting coefficient \(0.7120369597144336\).

The code builds each bouquet as a graph, derives shortest-path distances by breadth-first search, forms its full anchored powered-distance matrix, and compares its full spectrum to the predicted block spectra for multiple exponents and petal counts. It also checks endpoint multiplicity, sides of the transition, sampled strict parameter monotonicity, and asymptotic proximity. Those checks are finite and supplementary; the proof in `RESULT.md` is analytical, with the integral positive-definiteness and strictness/interval theorem supplying the infinite-parameter steps. No independent audit or external mathematical certification was performed.
