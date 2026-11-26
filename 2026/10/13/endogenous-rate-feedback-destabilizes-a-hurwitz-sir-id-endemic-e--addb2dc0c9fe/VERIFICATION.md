---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The proposed values satisfy the rational equilibrium equations, including the two rate-source balances and P=mu N+aI. Both rate values lie strictly inside admissible clipping intervals, so the auxiliary states and clipped rates agree locally. Independent symbolic differentiation and exact polynomial calculation reproduce both Jacobians and characteristic polynomials. The cubic has positive coefficients and strict Hurwitz margin 1753317/180500000. The full quintic has nonzero Routh pivots with signs (+,+,+,-,+,+), giving exactly two open right-half-plane roots with multiplicity. Since all quintic coefficients are positive, these are a conjugate nonreal pair. Positive real parts establish local instability of the five-state equilibrium, not a Hopf bifurcation.

## originality

PASS

The primary source specifies the very feedback laws, but its endemic-equilibrium proof in Theorem 7 analyzes only the three-population Jacobian; it neither gives this equilibrium and full spectrum nor implies the instability. Inspected nearby catalogue results concern other models. The distinction is a five-dimensional versus frozen-rate stability certificate, not a rescaling or change of notation.

## value

PASS

An admissible exact counterexample answers whether stable population dynamics at fixed rates can justify endemic stability after including the published feedback. It identifies where a three-dimensional calculation ceases to settle the actual model and provides a reproducible finite certificate of oscillatory linear instability, without overstating it as a cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
