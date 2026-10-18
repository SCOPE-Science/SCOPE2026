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

Independently expanded the Möbius factors to confirm I-B_A(z)B_A(w)^*=(1-zar w)(I-zA)^(-1)(I-A²)(I-ar w A)^(-1) for positive self-adjoint A: numerator cancellation is (1-zar w)(I-A²). Thus the source sub-Bergman kernel is transported by invertible L_A(z)=(I-A²)^(1/2)(I-zA)^(-1), giving ||f||_sub=||L_A^(-1) f|| on weighted Bergman. For alpha>0 weighted-area integration bounds analytic operator multipliers above by H∞ norm, and normalized reproducing kernels give equality; at alpha=0 use Hardy kernels. Spectral calculus over sigma(A) subset [0,a] with a in spectrum shows sup multipliers L_A and L_A^(-1) both equal sqrt((1+a)/(1-a)), attained as boundary z->1 and z->-1 respectively (spectral limit if a not an eigenvalue). Checked scalar endpoint expressions at a=0,.2,.75,.99 and sqrt7 at a=.75. The focal source kernel is an explicit algebraic identity; full focal text unavailability is a provenance risk, not an unchecked mathematical hypothesis.

## originality

PASS

The focal Luo–Shen preprint concerns equality as sets in a vector-valued Möbius construction; accessible abstract identifies that structural problem but its complete primary text was blocked, so the possibility that exact constants occur inside is a concrete significant residual risk. Cheng Chu already has the same sqrt((1+|b(0)|)/(1-|b(0)|)) scalar factor in a related one-sided comparison, but an upper bound in a scalar RKHS is not an exact simultaneous two-sided identity distortion for arbitrary positive operator A. Earlier vector-valued sub-Bergman work emphasizes structural properties. Best-of-knowledge originality passes only for the sharp two-sided operator-valued norm invariant, not the square-root function per se.

## value

PASS

Source-level set equivalence for a nonrigid vector-valued model naturally raises the precise norm-geometry question. The optimal two-direction constants form a useful quantitative condition-number invariant for arbitrary positive A and all alpha>=0, and turn a concrete nonrigidity example into exact sqrt7 rather than an unspecified equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
