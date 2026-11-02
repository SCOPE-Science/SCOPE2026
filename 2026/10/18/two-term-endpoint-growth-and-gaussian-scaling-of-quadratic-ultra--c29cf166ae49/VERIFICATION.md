---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The Beta moments E Y²=1/(2a+1), E Y⁴=3/((2a+1)(2a+3)) yield variance 4a/((2a+1)^2(2a+3)) and exactly reproduce 1,y,y² with the normalized symmetric kernel. Rescaling z=sqrt(2a+1)y gives K=1+sqrt(2a+1)xz+((2a+3)/(4a))((2a+1)x²-1)(z²-1). Uniform finite moments imply Lambda_a(x)/a -> 4phi(1)x²; the uniform differentiated sign limit on [delta,1] and a strict gap on |x|<=1/2 show only +/-1 maximize for sufficiently large real a. The central x=z/sqrt(2a+1) Hermite limit is locally uniform. At x=1 the exact kernel is a(z²-1)+sqrt(2a+1)z+(3z²-1)/2, and weighted standardized-beta expansion phi(z)(1-H4(z)/(8a))+o(a^-1) plus moving-simple-root expansion at +/-1 gives Gaussian parts (6phi(1)+4Q-1)+2phi(1)-phi(1)=7phi(1)+4Q-1. Independent exact-rational beta reproduction and 55-digit numerical integration confirm component identities and limiting errors at seven a values; finite checks do not prove any infinite statement.

## originality

PASS

Best-of-knowledge originality for the fixed-degree-two, continuously weighted ultraspherical projector: an exact order-one correction and eventual unique maximizing endpoints accompany the uniform spatial limit and the central Hermite profile. Classical beta moments, Hermite limits, absolute normal first moment and general projection kernels are not independently novel. Published discrete Johnson analogues and inspected continuous-operator literature do not state or imply the full claim. Two closely titled 1999 papers remain uninspected beyond abstracts and are recorded as priority risks, not classified as wholly noncovering.

## value

PASS

The quadratic continuous Jacobi/Gegenbauer orthogonal projector is a canonical approximation operator. The exact first two coefficients of its large-weight sharp L1/Linfinity norm measure endpoint amplification and norm instability in high concentration, while its central Gaussian scaled profile stays bounded. The uniform spatial law and eventual uniqueness of the two endpoint worst evaluations supply a meaningful structural location result. These exact invariants are not a mere known-table restatement or trivial normalization of a polynomial moment; researchers investigating endpoint least-squares stability, Jacobi parameters and Hermite crossover can use both coefficients and location behavior. The familiar Gaussian limit alone would not meet this claim of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
