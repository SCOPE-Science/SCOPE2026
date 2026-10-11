---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For the quadratic FBE, direct substitution gives the feedback \(\ell_x(p)=a(1-s)(p^2-2p/s)/2\), hence the online update is the projected affine map \(p_{k+1}=\Pi_{[1,2/s-1]}(1/s+(1-\theta)(p_k-1/s))\). Every candidate in the interval contracts the primal step, so the null-step safeguard never fires. For \(0<\theta<2\), projection is inactive and the closed forms for \(p_k\) and \(x_k\) follow; \(\theta=1\) reaches the optimum on the second primal step. For \(\theta\ge2\), the projected map sends endpoints to opposite endpoints, producing the exact 2-cycle and linear absolute contraction. The repository exact-rational verifier checks representative regimes and the feedback identity; the symbolic projected-map analysis proves the complete range.

## originality

PASS

The OSOP source introduces online-scaled operator splitting and its feedback framework but the accessible primary material does not state this scalar closed-form bifurcation. The earlier full HDM paper proves instability and local superlinear convergence for strongly convex quadratics and discusses null steps, yet does not give the exact projected scalar threshold \(\theta=2\) or endpoint 2-cycle. Resultary searches found no equivalent theorem.

## value

PASS

The theorem gives an exact stability/bifurcation boundary for a new adaptive splitting mechanism and exhibits a concrete regime in which the descent safeguard is blind to a preconditioner 2-cycle. The stable side also has an exact superlinear law, making this a motivated algorithmic boundary rather than an arbitrary scalar exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
