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

The accompanying `verify.py` is directly executable with Python 3, NumPy and SymPy. It checks 842 asserted identities and finite matrices, including exact spectra in the four- and six-vertex cases, independent-edge feasible weight perturbations, the dual polygon edge lengths, and both planar eigenvector equations. It does not substitute numerical testing for the all-size proof in `RESULT.md`.

The critical universal inequalities follow from the centered polygon's two coordinate columns, the Rayleigh minimum, and their explicit chord-square costs. Equality for the supplied weights is verified using the exact alternating-cycle Bloch spectrum. The proof of labelled-edge uniqueness is an elementary noncollinearity argument at each circle vertex; it does not assume uniqueness from mere symmetry reduction.

All real positive price ratios and budgets and all integers \(m\ge2\) are addressed analytically. The finite sample cannot exclude an equivalent result in unavailable literature; no independent audit has been performed.
