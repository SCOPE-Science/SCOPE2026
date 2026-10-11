---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The unclipped state matrix has characteristic polynomial \(z^2-(1+\beta-q)z+\beta\), so Jury gives local asymptotic stability exactly for \(0<q<2(1+\beta)\). On any nonzero two-cycle, periodicity forces opposite velocities and hence clipped gradients of equal and opposite magnitude \(G=(1+\beta)(a-b)/\alpha\). Scalar clipping leaves only two exhaustive branches: \(G<C\), where both positions are unsaturated and the equations force the critical equality; or \(G=C\), where both are saturated and the gap is \(\alpha C/(1+\beta)\), giving precisely the supercritical center band. In the strictly saturated alternating region the forcing is locally constant, so the velocity perturbation obeys \(e_t=\beta e_{t-1}\) and the center converges along the neutral cycle manifold. Fresh exact rational checks reproduced both critical and supercritical branches; the frozen verifier was independently read.

## originality

PASS

Optimization papers on clipping study descent/convergence or differently normalized momentum. Older saturated-control literature is substantially closer and was inspected: it constructs periodic behavior for saturated discrete-time double integrators and neutrally stable planar systems, but its model saturates an entire linear feedback input in a different state-space recurrence and its explicit orbit is period four. It does not state or imply the clip-current-gradient heavy-ball threshold, critical continuum, full supercritical period-two center band, or exact normal contraction factor. Resultary and targeted searches found no matching theorem.

## value

PASS

The theorem separates bounded oscillation from convergence in a widely used clipped-momentum mechanism and gives a complete, sharp period-two bifurcation with an exact neutral manifold and transverse rate. The result is materially stronger than merely observing one oscillatory example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
