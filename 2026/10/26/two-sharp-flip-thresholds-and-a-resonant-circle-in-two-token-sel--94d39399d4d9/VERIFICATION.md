---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At collinear tokens, tangent derivatives of all dot products and hence of the full softmax weights vanish. Dividing the resulting two-by-two tangent matrices by the nonzero unnormalized-vector norms yields the exact fixed-point eigenvalues and squared two-cycle multipliers, including sharp eta and qM threshold conditions. At resonance I+eta V=A diag(1,-1) and the split synchronized/antisynchronized return derivative gives multipliers 1 and cos^2(2theta)/A^2<1. Direct independent full-softmax finite-difference tests of both cycles and multiple resonant angles passed; this corroborates rather than proves all-parameter limits.

## originality

PASS

Qualified best-of-knowledge assessment: The exact orbit statements here are for full self-including softmax with mixed-sign V; isotropic negative V, masked kernels, and normalized optimization sign cycles do not give the two distinct q-dependent stability inequalities. General signed- or isotropic-attention dynamics can cover the existence of a flip, credited as prior. The simultaneous mixed-sign, self-including antipodal threshold and exactly normally attracting resonant circle require additional explicit transverse spectral calculation; no direct implication located. Prior general normalized-map definitions and spectral selection explain parts of the mechanism; they do not mechanically specify both strict sink boundaries or the resonance normal multiplier for this model. Residual priority and source-access risks are explicitly retained.

## value

PASS

The distinct transverse thresholds and a whole resonant normally attracting two-cycle continuum give a sharply resolved bifurcation structure in a natural minimal normalized-attention example, beyond a general statement that negative directions can flip.

The dated certificate retains the supplied scientific assessment, sources and limitations.
