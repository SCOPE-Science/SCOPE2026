---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The original quadrature tail has weights 23/12, 7/12 then 1 with three left-end corrections. Subtracting q times the preceding recurrence, q=e^{-theta}, cancels the starting convolution forcing and produces the displayed quartic with K=mu beta theta. At v=beta theta q(23-16q+5q²)/(12(1-q)), P(1)=6mu(1-q)(1-v); v>1 forces a real root>1. For v<1, the Cayley transform maps Schur to Hurwitz and seven necessary/sufficient Routh–Hurwitz expressions have explicit strictly positive polynomial numerators after q=X/(1+X),v=Y/(1+Y); independent rational SymPy reconstruction verified all coefficients nonnegative and exact term counts 3,14,16,16,16,63,117, plus all five v=1 boundary positivity checks. A separate expansion of theta W(e^{-theta}) proves <1 for theta>0, and the continuous augmented 2x2 memory ODE has a positive eigenvalue whenever beta>1. The verifier checks algebraic positivity for all positive parameters, not mere sampling.

## originality

PASS

Best-of-knowledge novelty of the precise final theorem survives comparison with relevant antecedents and currently indexed mathematical literature, but not exhaustive historical priority. Different numerical stability notions and quadrature weights prevent direct equivalence, despite the shared BDF family.

## value

PASS

This is an exact stability/false-stability phase boundary for a published high-order memory scheme. It demonstrates an operationally important spectral discrepancy between continuous Volterra growth and discrete numerical decay, including a rigorously nonempty interval for every timestep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
