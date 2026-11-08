---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The function 2u/sin(u) increases strictly from 2 to pi, so each 2<kappa<pi yields unique u. Directly substituting opposite two-block phases gives a literal least-period-two orbit; both Jacobians are the same symmetric block matrix because cos is even. Its eigenvalues on common rotation, inter-block, and intra-block zero-sum subspaces are respectively 1, 1-kappa*cos(u), 1-kappa*(p+q*cos(u)) (m-1 times) and 1-kappa*(q+p*cos(u)) (N-m-1 times). Floquet eigenvalues are their squares, and the singleton missing-mode cases do not undermine the criterion. Transverse attraction iff max(p,q)<p*=(sin(u)-u*cos(u))/(u*(1-cos(u))); > gives unstable eigenvalue, equality neutral +1 only. Integral p*=integral(s*sin(us))/integral(sin(us)), covariance of s and s*cot(us) strictly negative, gives 2/3 down to 2/pi; n=3 uniquely obstructed. Independently evaluated 21 original map/Jacobian cases.

## originality

PASS

Sine-circle period doubling and clustered discrete Kuramoto behavior are known; finite block-size-dependent exact Floquet spectrum and monotone sharp fraction 2/3 to 2/pi do not follow from the inspected continuum incoherent-state theory or the earlier numerical cluster studies. Full recent 2026 motivating preprint inaccessible; priority qualified.

## value

PASS

Gives a complete exact local stability classification of an explicit natural family of finite-network periodic states and a striking finite-size threshold: N=3 always unstable while balanced 2 and >=4 attract. It predicts block-imbalance thresholds across every strong-coupling parameter, not just isolated simulation examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
