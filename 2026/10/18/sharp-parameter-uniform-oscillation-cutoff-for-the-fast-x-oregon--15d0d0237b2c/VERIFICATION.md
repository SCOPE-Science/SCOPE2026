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

Exact symbolic checks in `verify.py` independently reconstruct the inverse nullcline and derivative identities, verify the algebraic critical-point condition, compute the polynomial resultant, and evaluate the unique root. Running this checker provides finite algebraic verification, not independent validation of the dynamical theorem.

For the global part, the proof uses exact bounds on \(X_q\), explicit inward-pointing rectangle inequalities, positive equilibrium determinant, strict negative divergence, and Poincaré--Bendixson. For sharpness, the exact construction produces a hyperbolic source inside a positively invariant rectangle; an outward local ellipse and inward outer boundary enclose a compact invariant annulus, which guarantees a periodic orbit. No finite numerical sweep or truncated orbit simulation is used as a substitute for these arguments.

The results are confined to the quasi-steady planar fast-\(x\) model, positive parameters, and nonnegative initial conditions. The theorem does not prove any analogous bound for the full Oregonator or for alternative variable elimination. Historical coverage by sources without readable full text remains uncertain. Independent audit has not been performed.
