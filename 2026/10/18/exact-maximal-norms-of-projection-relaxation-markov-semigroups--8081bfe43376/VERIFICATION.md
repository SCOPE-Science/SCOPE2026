---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The modulus of a real or complex line segment is bounded by the larger endpoint modulus, and the orbit includes or approaches both endpoints. This gives max(|f|,|Pf|) also for the discrete powers exactly in the stated range 0≤rho<1. Pasting Pf on an arbitrary E and f off E is an exact linearization, because the measurable comparison event realizes the pointwise maximum for each f. With b=P1_E and a=1-b, conditional Cauchy–Schwarz gives the matrix with rows (1,0) and (sqrt(ab),b) on the two conditional energy square roots. The Gram matrix has trace 1+b and determinant b², yielding Lambda(b). The vector from a function with value 1 off E and r_b=ab/(Lambda(b)-b²) on E lies in the top eigendirection on 0<b<1, and both conditional Cauchy–Schwarz inequalities are then equalities. The multiplier is measurable and bounded (Lambda≥1 gives r_b≤b/(1+b)). Localizing on a positive-measure set in the conditioning sigma-algebra near the essential supremum gives the lower bound without a disintegration assumption; when that supremum is 1, constants give equality. Strict concavity gives the unique maximizing mass 2/3 and the stated essential-range criterion for norm equality. For trivial conditioning, compactness of the mass set follows from summable atomic subsums plus a full interval of nonatomic masses, and r_(2/3)=1/4. On the uniform grid, only the two neighbors of 2/3 can maximize; in the deficit identity the denominator strictly decreases between 8/3 and 2/3, so offsets of magnitudes 1/(3n) and 2/(3n) are ordered by deficit despite the asymmetry. Taylor expansion gives the coefficient 1/9. The arbitrary-space result is analytic, not a finite extrapolation; frozen finite replay path verify.py was inspected, not run, and is not needed for the proof.

## originality

PASS

The supported distinct claim is the exact norm for each fixed conditional expectation, as determined by the conditional event-mass profile, including its equality criterion and the sharp constant-projection and uniform-grid consequences. The bounded comparisons found broader martingale/semigroup inequalities and a different operator with the same sharp numerical constant, but no equivalent fixed-projection formula or stronger result implying it. Endpoint convexity, use of the complex modulus and the power extension are not treated as separate originality contributions. This is a best-of-knowledge decision, not a priority certificate.

## value

PASS

The relaxation model isolates a natural maximal-norm question where generic bounds conceal the role of the underlying probability space. The exact conditional profile distinguishes universal sharpness from sharpness for a given projection and works without measurable-fiber hypotheses. Its finite uniform specialization resolves the asymmetric grid choice, determines exactly when universal equality holds and quantifies the deficit. This is a useful structural and quantitative result, not only the computation of a universal constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
