---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Derive gamma=(u^T X^dagger u)^-1 by rank-one Schur-complement/PSD criterion; diagonalize X=diag(a,b). For C=1/a,D=1/b, I=E[(Ccos²+Dsin²)^-1]=1/sqrt(CD); U+V=I and CU+DV=1 yield U=a sqrt(b)/(sqrt a+sqrt b), V=b sqrt(a)/(sqrt a+sqrt b), continuous at a=b. Then E[gamma uu^T]=sqrt(ab)/(sqrt a+sqrt b) sqrt(X), and min generalized eigenvalue of (E[gamma uu^T],X) equals sqrt(a)/(sqrt a+sqrt b); Q projected on b eigendirection attains it. Independent deterministic quadratures for (1,1),(1,4),(1,100),(0.1,7),(3,19) corroborate; integral is analytic for all a,b>0.

## originality

PASS

The exact weighted random-removal *matrix* mean and sharp PSD comparison are not the same as Garber Lemma 5 unweighted Haar projector moment, though both use the same algorithmic update and a standard two-dimensional reciprocal-quadratic integral.

## value

PASS

Sharp expected spectral progress for the exact random PSD rank-two deflation primitive is a motivated structural lemma: it replaces a conditioning-loss a/(2b) by an optimally attained coefficient and avoids falsely asserting global algorithm improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
