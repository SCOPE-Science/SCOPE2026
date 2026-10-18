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

# Reproducibility

With Python, NumPy, SciPy and SymPy installed, execute `python verify.py` from this extracted package. The script independently checks the explicit compression and discriminant using symbolic arithmetic, evaluates the exact probability integral at selected finite sketch sizes using incomplete-beta quadrature, and tests the direct Gaussian sketch formula for five sketch dimensions. Its output is recorded in `verification_output.txt`.

The verifier executes 971 deterministic assertions and returns exit code zero; analytic density normalization and the asymptotic argument are proved in RESULT.md rather than inferred from sampling. Numeric integration does not certify an infinite family of cases. A finite-run random-number stream serves only as deterministic implementation regression, not as a probabilistic error guarantee.
