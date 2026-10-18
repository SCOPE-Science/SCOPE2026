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

Run `python verify.py` using Python 3. No third-party packages or external files are required.

The verifier works exactly in \(\mathbf F_7[\lambda]\), not by floating-point arithmetic or sampling a finite list of curve parameters. It forms the defining octic, expands its sixth power, extracts all \(21^2\) Cartier-relevant coefficients, and partitions the resulting matrix into four scalar, four two-dimensional, and three three-dimensional blocks. It checks each determinant symbolically against \(\lambda\) or \(-\lambda^d(\lambda^2-2)\). Ranks of each block at the two exceptional roots are checked by exact modular elimination, establishing that each nontrivial block has corank one. The script separately recomputes the genus-three quotient matrix from \((\xi^7-2\lambda\xi^4+\xi)^3\).

The smoothness theorem and the Deuring–Shafarevich formula are cited mathematical inputs, not purportedly certified by executing the code. The proof explains why those inputs apply. The script does not compute full Newton polygons, classify abstract curve isomorphisms, or constitute an independent audit.
