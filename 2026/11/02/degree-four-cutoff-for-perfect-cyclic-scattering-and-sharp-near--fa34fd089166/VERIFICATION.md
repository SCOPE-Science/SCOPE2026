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

A unitary circulant deterministic scatterer is a phased R^m. Conjugate nonconstant Fourier modes force the phase to be ±1; the constant mode cannot be -1 at positive k and finite alpha, so the phase is +1 and t=1 or alpha=0. At n=2 the fixed eigenvalue -1 in the other mode gives the same restriction and only the swap is possible. At t=0 all nonconstant modes equal -1, incompatible with R^m for n>=3. For t>0 the first h=floor((n-1)/2) mode eigenvalues lie in the upper semicircle, so m must be 1: m>=2 below n/2 would violate the sign at j=ceil(n/(2m))<=h. Matching R then requires k=tan(v_j)/tan(t v_j). Differentiating its logarithm and using the decrease of sinc gives incompatible conditions for two distinct v_j at 0<t<1, while h=1 gives exactly the n=3,4 curves. At t=1 all conditions reduce to k=1. For the optimized loss the conjugate phases make the target amplitude real, and its quadratic loss is 2/n times the sum of squares (2v_j delta - sin(2a_j)(k-1))^2. Projection along the momentum direction gives the two coefficients, with strict positivity by strict monotonicity of v/sin(2v). The Hessian in k is nonzero at the perfect point; the analytic critical branch is unique locally. At fixed n and alpha=0, compactifying k admits continuous endpoint extensions uniformly near t=1: the target probabilities tend to 4/n^2 at zero and to zero (odd n) or 4/n^2 (even n) at infinity. Since P=1 at t=1 only at k=1, a compactness gap away from that point forces every global maximum onto the local branch for t sufficiently near one.

## originality

PASS

The interpolation, exact scattering formula, low-degree entries and pure preferred-orientation router are prior. The distinct claims supported here are the exhaustive finite-momentum interior cutoff against every phased permutation and the positive, sharp leakage after global momentum optimization near t=1. The closest indexed same-family result is about reflectionlessness in the opposite scaling regime, not deterministic routing or this optimizer.

## value

PASS

The result identifies exactly when an established interpolation permits probability-one circulation, not merely low reflection. The degree cutoff isolates a coupling-family obstruction; the positive optimized loss distinguishes that obstruction from a poor momentum choice, and gives a quantitative design tolerance near the pure orientation endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
