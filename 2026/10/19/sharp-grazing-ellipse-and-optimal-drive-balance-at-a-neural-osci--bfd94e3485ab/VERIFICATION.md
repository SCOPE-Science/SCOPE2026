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

# Reproducible analytical and symbolic verification

The scientific statement is proved for positive real parameters on the stated critical coupling surface, with **all times** quantified. The critical steps are the exact affine-center reduction, the bound on the maximum of a harmonic combination, the stable-spectrum obstruction to any extra active-cell periodic orbit, and the area and optimization algebra in `RESULT.md`.

Run `python verify.py` with Python 3 and SymPy installed. The script checks the full vector-field plane identity, the equilibrium equations, the harmonic frequency and amplitude relation, the optimal input-balance algebra, the optimal-drive and nonoptimal-drive exact-rational cases, their grazing-boundary conditions, the optimal projected and intrinsic areas, and the substitution of its sinusoidal orbit into all four ODEs. Expected final marker: `SYMBOLIC_CENTER_AND_ELLIPSE_OK`.

These finite symbolic examples are auxiliary checks. They cannot replace the proof of all-parameter uniqueness and all-time activity. No simulation can independently establish the claimed absence of other periodic solutions: that follows from the strictly stable complementary subspace in the exact affine linearization. Bibliographic completeness, independent publication priority and independent mathematical validation remain unestablished.
