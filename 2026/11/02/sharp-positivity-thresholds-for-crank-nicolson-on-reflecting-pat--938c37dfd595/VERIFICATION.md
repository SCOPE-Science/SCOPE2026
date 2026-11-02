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

# Reproducibility and mathematical verification

Run `python3 verify.py` with an ordinary Python 3 interpreter and no third-party packages. The file checks exact rational inverses for the symmetric path matrices, central resolvent minima, positivity decisions, and transition-matrix row sums, at 105 \((n,z)\) settings with \(2\le n\le16\). It also checks the exact height-three (three-vertex) threshold, twenty finite threshold roots, monotonicity, and the two leading asymptotic constants.

The infinite claims are independently deduced from the Green-kernel formula, strict spectral monotonicity, exact inequalities and polynomial expansions in the proof; computations cannot replace those arguments. At the exact transition only central diagonal entries can vanish, while off-diagonal entries remain positive. Numerical root comparisons use floating-point precision and are supplementary, not certificates for all lengths.

The relevant Neumann compact-scheme source was inspected at publisher abstract/reference level only, and an originality assessment cannot exclude an equivalent formula in uninspected specialist literature. Independent mathematical validation has not been performed.
