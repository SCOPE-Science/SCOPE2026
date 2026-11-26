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

For an exact nonempty spoke set, each inter-spoke arc must omit a rim edge; this condition also makes every rim component a path with at most one hub edge. Summing gives a_d=x((1+x)^d-x^d), also for one spoke with its single length-n arc. Independent positive compositions between forced spokes give U=A/(1-A) and u_d=x(λ_+^d-λ_-^d)/Δ. Marked compositions supply n/k for k spokes in the partition function; the isolated-hub sector contributes (1+x)^n-x^n. Factoring 1-A then gives exactly the subtraction 2x^n, and forest enumeration ensures the denominator is positive. As the wrap gap diverges, eliminating the preceding row from successive rows of the exponential kernel reduces the determinant to the product of 1-q^d factors. Its Fourier symbol is positive with maximum x/(1+3x-2sqrt(x(1+x)))<1; inclusion-exclusion yields finite-dimensional convergence. A(1/λ_+)=1 gives the normalized gap law; differentiating there gives mean Δ/x, and its renewal mass u_d/λ_+^d gives the very same joint inclusions and hence the same Palm law. For the finite covariance inequality, putting u=q^r,v=q^{n-r}, the difference (1-uv)^2-(1+uv)(1-u)(1-v) is at least 2sqrt(uv)(1-sqrt(uv))^2>0. The finite denominator is even smaller than 1+uv. Distance ordering follows from the strict decrease of q^r+q^{n-r} up to the shorter-distance midpoint; the local limit yields -ρ²q^r. Independent replay: python3 /workspace/branches/review_checks.py 1, all spoke inclusions and pair claims on n=3–7 at x=1/3,1,3/2 by exact rim-first enumeration. The frozen script was inspected, not run.

## originality

PASS

Credit the known unit-fugacity partition function and strict correlation; weighted enumeration is potentially encoded in Bado's stronger multivariate generating polynomial. The pass is for the supported distinct process-level result: the explicit local determinantal and stationary renewal identifications for every fixed common fugacity, with the gap product providing its derivation. Priority for the finite inclusion identity in isolation is not certified.

## value

PASS

Identifying a complete local law of an unrooted spanning-forest model, simultaneously through an explicit determinantal operator and an explicit Palm renewal law, specifies all spoke correlations and gap statistics, unlike the known pair sign. The finite exact gap and wrap correction enable the fixed-fugacity limit on a natural graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
