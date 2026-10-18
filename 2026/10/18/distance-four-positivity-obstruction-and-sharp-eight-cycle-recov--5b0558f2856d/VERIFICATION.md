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

# Exact reproducibility

Run `python -m pip install -r artifacts/requirements.txt` in a suitable Python environment and then `python artifacts/verify_pade02_cycles.py` at this package root. The script requires SymPy and no external research corpus or private network access.

The program reconstructs each unweighted cyclic Laplacian, its quadratic rational denominator matrix, and its symbolic inverse independently; checks matrix inversion and conservation; checks all required circulant and reversal symmetries; proves strict positivity of rational numerators and denominators for cycles of lengths three through seven via exact nonnegative polynomial coefficients; checks the full eight-cycle fourth-distance numerator and its one-positive-root property; and checks a path-graph distance-four coefficient. A run with Python 3.13 and SymPy 1.14 completed 259 exact symbolic assertions and reported success.

The result for all graphs of diameter at least four comes from an analytic Taylor-coefficient and graph-distance proof, not from sampled graphs. Large-step strict positivity uses the finite connected Laplacian spectral projector. The displayed eight-cycle root's decimal representation is a numerical approximation only; its uniqueness and the exact sign threshold are algebraic. These checks do not constitute independent assessment of novelty, correctness of every external source, or publication certification.
