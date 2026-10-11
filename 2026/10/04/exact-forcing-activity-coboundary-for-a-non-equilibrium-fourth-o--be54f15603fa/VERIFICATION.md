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

Direct differentiation of \(\Phi\) along the printed vector field cancels \(-aw\) with \(a\dot z\), the \(exy\) term with the derivative of \(-(e/2)x^2\), and \(fxz\) with the matching component of \(-f\,d(xy)/dt\), leaving exactly \(bx^2-(c+f)y^2+g\). A bounded forward state makes \(\Phi(T)-\Phi(0)\) uniformly bounded, so division by \(T\) gives the time-average law. Invariance of a compactly supported probability measure gives the stationary law by integrating the time-integrated identity. The sign cases follow immediately, and the source decimal parameters reduce exactly to coefficients \(35/99\) and \(115/198\). The inspected symbolic verifier independently checks the polynomial identity and rational specialization.

## originality

PASS

The Jahanshahi et al. source studies the same printed four-dimensional non-equilibrium flow through equilibria, bifurcations, entropy, hidden attractors, and control. Semantic search found the audited coboundary theorem as the direct same-system result and only analogous moment identities for other vector fields. No inspected primary or published result states this exact forcing-activity coboundary or its invariant-measure consequences.

## value

PASS

The identity converts a numerically studied chaotic model into a rigorous long-time activity law and gives a parameter region where bounded dynamics are impossible. Exact stationary constraints of this form are useful for validating simulations and separating global recurrence facts from local bifurcation or Lyapunov diagnostics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
