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

Use Python with NumPy and SymPy installed, in the directory containing `verify.py`, and execute `python verify.py`.

The script verifies exact symbolic coefficient matching for the scalar-optimal cubic, the scale-normalized family polynomial, the derivative determining the modal optimizer, and the sharp rational optimizers. It isolates the real algebraic parameter \(t=1-2^{-1/3}\) with rational cubic inequalities, then verifies every published strict sufficient-parameter inequality by conservative rational interval bounds. It samples 8,008 modal companions and performs 100 seeded direct proximal matrix updates, including an exact identification of the two modal contraction factors. On execution it prints a final `VERIFIED` line plus the example's numerical rates. Numeric spectral grids are merely supplementary: analytic arguments in RESULT.md prove all infinite-range assertions.

No external service, previous package, confidential research ledger, or unreproduced computational artifact is required. The verification is same-model only. Independent scientific audit has not been performed.
