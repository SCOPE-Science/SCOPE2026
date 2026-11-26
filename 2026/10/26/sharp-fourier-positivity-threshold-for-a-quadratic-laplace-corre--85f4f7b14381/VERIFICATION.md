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

In the stated unnormalized convention, the two diagonal coordinates separate the base transform F_a=8a²/((a²+X)(a²+Y)), X=(ξ−η)² and Y=(ξ+η)². Exponential domination justifies two derivatives in a. Independently, with u=1/(1+X), v=1/(1+Y), the ratio of the correction transform to F_1 is E=−13/6+6(u+v−5/6)²+2(u−v)². Thus the transform is F_1(1+cE); the unique minimizing pair u=v=5/12 is attainable and gives exactly X=Y=7/5, hence the four stated zeros and immediate failure beyond the threshold. E is bounded on (0,1]², so integrability follows by comparison with the product form of F_1. By Bochner and Fourier inversion the signed density determines positive semidefiniteness, and in the allowed range it is positive almost everywhere. For distinct sites a nonzero finite exponential sum does not vanish identically (restrict to a line with distinct projected sites), giving a strictly positive Gram form. The radial derivative is e^(−r)[−1+c(2r−r²)], nonpositive for c≤1 and strictly negative except for the isolated stationary radius at c=1. This proves the contrast and all asserted boundary cases for c≥0.

## originality

PASS

The sharp square-norm boundary and four-point zero set survive comparison with general norm-radial characterizations and the same-day Euclidean covariance cone. The planar L¹/square change of variables and the base Laplace transform are known. The distinct content is the optimized correction and its critical frequencies, not a general radial characterization.

## value

PASS

The square kernel is a natural separable Laplace example after a diagonal change of coordinates. The sharp coefficient tells exactly when a positive decreasing profile stops defining a covariance kernel, and the isolated zeros distinguish the first loss of spectral positivity from loss of strict finite-site definiteness. These are useful concrete properties not furnished by an abstract admissibility criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
