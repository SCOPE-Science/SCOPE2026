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

# Reproducibility and verification

Run `python verify.py` with Python 3, NumPy and SciPy. This is a supplementary numerical consistency check; no external data files are needed. It was run successfully and printed `PASS`.

The program checks 125 independent Gaussian Hessian determinant and completed-square identities in five dimensions; 20 comparisons of the exact normalized \(p\)-moment over four Gaussian contraction widths; three small-width quadratic constants; and four entropy values computed via two-sided moment differentiation rather than the closed entropy integral. The tolerances are explicit in the program.

The unlimited dimension and continuous exponent conclusions are proved using exact finite-dimensional matrix identities and integrals in the main proof, the known global Lieb bound, and nonattainment of sharp Heisenberg Young inequality at interior exponents. Numerically sampled Gaussian matrices and moment values do not establish those universal conclusions. The independent scientific audit has not been performed.
