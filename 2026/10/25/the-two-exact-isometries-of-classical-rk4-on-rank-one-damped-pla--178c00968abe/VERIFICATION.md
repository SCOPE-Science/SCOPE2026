---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the entire Cayley-Hamilton reduction A^2+xA+YI=0: R4(A)=U I+V A, with U=1+Y(Y-x^2+4x-12)/24, V=-(x^3-4x^2-2xY+12x+4Y-24)/24. The off-diagonal Gram term is x sqrt(Y) V^2, so x,Y>0 force V=0 and U=+/-1. The +1 polynomial z(z^3+4z^2+12z+24) has one nonzero left conjugate pair characterized by rho in (2,3); the -1 polynomial factors, after t=z+1, into a left conjugate quadratic and a right conjugate quadratic characterized by v in (5,6). The roots have negative trace and positive determinant on exactly one admissible pair in each case. Differentiating Gram at V=0 yields Q_Y=2s diag(U_Y-xV_Y,U_Y); the two diagonal signs are both positive at +I and opposite at -I. Strict continuous-time contraction follows from norm derivative -2a*u1^2 and omega>0. Independently verified polynomial matrix and Gram identities symbolically, both cubic roots numerically, and derivative signs. No finite numerical check substitutes for global root count or continuous-time strictness.

## originality

PASS

Best-of-knowledge comparison of the complete asserted mathematical implication against actual primary material read and documented searches. Prior strong-stability work leaves the isolated exact matrix isometries and signs unclassified in read sections.

## value

PASS

The canonical rank-one damped planar oscillator has strictly dissipating continuous evolution yet can be exactly frozen or sign-flipped by classical RK4. Giving the exhaustive two-point resonance classification and distinct first-order frequency responses exposes a sharp structural numerical-analysis pathology, not an arbitrary small test or a mere stability-region plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
