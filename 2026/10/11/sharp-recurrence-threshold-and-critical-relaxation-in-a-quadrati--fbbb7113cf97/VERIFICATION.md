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

# Verification of the mathematical argument

Run `python verify.py` from the directory containing the complete files, using Python and SymPy. Assertions check the exact derivative of \(Q=z-cy\), the completed square, the critical equilibrium and characteristic polynomial, and the quadratic center-manifold invariance residuals. They do not constitute a numerical proof of an infinite-time statement.

The global threshold and equality-case convergence are instead proved analytically using monotonicity, compact omega limit sets and LaSalle's invariance principle. Invariant-measure rigidity follows from integration of the exact polynomial identity. The sharp relaxation depends on the classical smooth center-manifold plus local strong-stable foliation theorem, followed by a scalar differential asymptotic. The result requires \(a<0\), \(d<0\), \(c\ne0\); no assertion is made for \(c=0\) or all unbounded initial data. Literature searches may miss unindexed equivalent results. Independent audit has not been performed.
