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

# Verification scope

The independently runnable `verify.py` checks the exact scalar identities and rational matrix formulas displayed in `RESULT.md`. It uses SymPy and performs exact rather than floating-point calculations. From the directory containing both files, install `requirements.txt` and execute `python verify.py`. A successful run prints `VERIFY_OK` and the number of graph cases and checked entries.

The scalar derivative identities are symbolic certificates of monotonicity after positive denominators are established. The finite matrix checks independently form numerator and denominator polynomials in the graph Laplacian and invert the latter exactly. The proof of the full infinite-family claim depends on the orthogonal projector decomposition, the explicit strictly negative derivatives and the spectral-measure ordering argument; finite tests alone do not establish those general steps.

The computed tests do not establish numerical solution accuracy, internal-stage positivity, or properties of nonsymmetric, weighted, or arbitrary graphs. No separate external validation or independent review is claimed.
