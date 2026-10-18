---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Independently differentiated the exact displayed P and Q with rational symbolic algebra: P(x,1)=0, Q(x,1)=(x-1)(x-2)(2x-3). The Jacobian at (3/2,1) is [[0,-19/16],[-1/2,13/6]], determinant -19/32 and eigenvalues (26±sqrt(1018))/24 of opposite signs. Direct evaluation at the other two roots yields [[0,-1],[1,0]]. The polynomial on y=1 has exactly three roots; no off-line exhaustion or global phase portrait is inferred. The source-tree verification script was read; this independent calculation does not rely on its output.

## originality

PASS

The dated original source describes two positive equilibria, while the model equation forces a third saddle. This is not a reformulation of the source’s local focus computations. The result is elementary but a substantive correction to the stated phase-space geometry; no pre-existing correction of this exact equation was found in compared sources.

## value

PASS

A source-specific persistent additional positive saddle changes the equilibrium skeleton of a quartic ecological model used to discuss Hopf cycles, despite not invalidating local calculations about the two focal points. It motivates an eventual separatrix/global basin study; the bounded correction is useful without claiming full classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
