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

# Verification and limits

The core claim is the exact all-radius identity in `RESULT.md`, obtained by the analytic identities \(u_z=\overline\omega\omega'/(1-|\omega|^2)\) and \(\Delta u=4|\omega'|^2/(1-|\omega|^2)^2\), angular Fourier-mode cancellation for holomorphic \(h''/h'\), and the disk divergence theorem. Each argument holds on any compact disk \(0<r<1\) without boundary regularity.

For the explicit sharp family \(h(z)=z\), \(g(z)=az^2/2\), the exact energy integral is \(\pi |a|^2r^2/(1-|a|^2r^2)\) and the circlewise order magnitude is \(r+|a|^2r(1-r^2)/(2(1-|a|^2r^2))\). These are equal for every \(0\le|a|<1\) and \(0<r<1\). The included standard-library checker `checks/model_examples.py` passed on three exact rational cases, including a constant-dilatation boundary example. Those finite checks are illustrative only and cannot establish the general theorem.

For the Schwarzian application, the 2026 inequality enforces \(|A_f|\le|\omega^*|/4\le1/4\) wherever \(\omega'\ne0\); continuity and the radius-\(1/2\) lower bound rule out nonconstant dilatation. Constant dilatation reduces the criterion to \(S_h=0\), hence the Möbius family. The latter rigidity result alone also follows from prior global order estimates, as acknowledged in the main paper and scientific review.

There is no independent audit or external validation. There is no assertion about uniqueness of all extremizers, finite energy as \(r\) approaches the disk boundary, or the separate harmonic inner-radius conjecture.
