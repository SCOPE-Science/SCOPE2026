---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the corrected claim, the radial L2 norm squared is at most 4 pi/3 by s=tanh r. The half-line cosine transform of sech is (pi/2) sech(pi s/2), obtained independently from the beta integral after v=e^(2r). Integration by parts against the derivative of sech and product-to-sum give the stated transform and exponential decay. Writing F(s)=s sech(c s) for c=pi/2, the transform is pi^2 times [F(omega+lambda)-F(omega-lambda)]/lambda. It is even and the continuous zero value is 2 pi^2 F'(omega), whose sign is that of 1-c omega tanh(c omega). For lambda>0, combining the translated cosh denominators leaves the sign of lambda coth(c lambda)-omega tanh(c omega). The first function increases strictly from 1/c to infinity because sinh(x) cosh(x)>x for x>0; the second increases from zero to infinity. This gives the inclusive cutoff, unique positive zero beyond it, and full repaired sign including lambda=0. The continuous L2 radial profile and integrable transform meet the L2-Godement hypotheses; the supercritical interval has positive Plancherel measure. An independently written decimal bisection using the exponential form of tanh and Machin's pi formula corroborated omega*=0.76373914287512802042949…; this calculation was not needed to certify the analytic sign.

## originality

PASS

The supported distinct claim is the nonzero-modulation cutoff and complete sign for the squared-sech envelope on curvature -1 H^3, not the transform framework, Fourier sech identity, unmodulated kernel, or general idea of a geodesic modulation cutoff. The closest indexed cutoff uses a different envelope and does not imply this one.

## value

PASS

This is an exact admissibility boundary for a natural modulated version of an established radial H^3 kernel. It decides whether a distance profile works on every configuration and, on failure, specifies the entire forbidden spectral band, including its single positive boundary. A Euclidean computation or the unmodulated theorem cannot substitute; strict monotonicity after combining two shifted terms yields both directions and the inclusive threshold. The corrected zero-frequency sign completes the classification without enlarging the scientific claim beyond this profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
