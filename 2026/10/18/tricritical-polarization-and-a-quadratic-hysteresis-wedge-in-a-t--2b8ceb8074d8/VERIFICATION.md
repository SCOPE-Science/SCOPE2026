---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the normalized two-zealot rule, direct cancellation gives F=sinh(2 gamma x)/(cosh(2 gamma x)+A exp(-gamma x^2))-x, with A=exp(gamma(delta-1)). Setting the linear coefficient to zero gives A=2 gamma-1. Expanding the cross-multiplied numerator and then dividing by the positive denominator gives the critical cubic (4 gamma^2-3)/6 and the printed general critical quintic. The unique positive cubic zero lies inside delta>=0 and has quintic -3/10. The inward fifth-order drift gives d(x^-4)/dt=6/5+o(1) along any sufficiently small nonzero forward solution. With y=x^2, F=xG, the positive root on the critical-gamma slice follows from the simple root after rescaling y=sqrt(mu)z, and is attracting by 2y G_y<0. The fold equations G=G_y=0 after y=nu z and mu=nu^2 s have nonsingular Jacobian, giving the two stated coefficients. For the full wedge, G_yy<0, G_mu>0 near the origin (G(0,mu,nu)=mu), and G at the fold's positive y is therefore positive when mu exceeds the fold value. With both boundary values negative, there are exactly two positive roots in the fixed neighborhood. The slope signs yield the two repellers and the three attractors including zero. This is a local classification, not a count of distant equilibria.

## originality

PASS

The same model and its linear stability boundary are prior work; qualitative nonlinear plots and a distinct fixed-gamma exact classification also overlap. The inspected results do not cover the unique cubic degeneracy, critical quintic, or the near-degeneracy fourth-root and quadratic-fold laws.

## value

PASS

The degeneracy is selected by the model's known stability boundary, not by an arbitrary parameter slice. The calculation separates continuous from hysteretic onset and quantifies the local interval of tristability, the anomalous fourth-root polarization scale and the critical relaxation rate, none of which can be read off a linear stability diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
