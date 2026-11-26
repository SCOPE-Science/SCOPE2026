---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On an even path an even-index first bond strands odd components, while an odd-index first bond splits two even paths with the original boundary rate. Its probability is alpha/(m-1+alpha); Poisson memorylessness makes the two remaining components independent. On a simple even cycle the first accepted bond leaves an even path of its own type, producing the two stated weighted coefficients. The recurrence gives zP'=beta(P-1)+alpha zP²; P=-u'/(alpha u) gives the entire 0F1 denominator and the quotient. All nonconstant coefficients of u are strictly negative, so on the positive axis its single zero is simple, and the triangle equality with consecutive nonzero powers precludes any other zero on or inside that modulus. The quotient residue is -1/alpha; Cauchy's estimate after subtracting the pole gives the unit-amplitude contribution R^{-n} per branch. For alpha2>alpha1 the m≥2 recurrence-factor ratio is at least c=alpha2(1+alpha1)/(alpha1(1+alpha2))>1. Induction gives a coefficient ratio ≥c^{(m-1)/2}, proving the strict radius decrease, not merely monotonic coefficients. This quantitative bound and the simple analytic root also give -R'(1/2)/R0≥2/3 (consistent with the direct derivative proof). A fixed circle separating the symmetric simple zero from the remaining zeros continues to separate it for nearby rates, making the Cauchy estimate uniform. Expanding log R at alpha=1/2±t/n yields the two factors exp(±kappa t) and the stated cosh. Independent accepted-order weights checked the exact branch coefficients for both perfect matchings in 50 cycle/rate cases, n=2 through 11, including the smallest simple cycle. A separate series calculation gave R0=1.43922883989064515077598 and kappa=1.09364675458441884588785.

## originality

PASS

Pass is for the genuinely alternating-rate law, the strict ordering of its two poles, and the 1/n crossover, not the homogeneous specialization or first-event method. Krapivsky's exact homogeneous path extremal-count distribution already gives the symmetric path recurrence, generating function and pole. Via the line-graph correspondence and one cycle cut it gives the exact symmetric cycle probability and its leading asymptotic as well. The closest catalog finite-cycle crossover uses a different acceptance rule and studies coverage time, while the closest catalog result with the same deposition rule gives an infinite-chain marginal. Neither supplies the alternating finite-cycle probability of zero vacancies or the symmetry crossover of that probability.

## value

PASS

Perfect jamming coverage is a well-defined rare event not recoverable from mean occupancy. Resolving its exact inhomogeneous finite-size law, proving which weighted matching controls the exponential rate, and identifying a nontrivial scaling window are useful information beyond the known symmetric law. The asymptotic result is supported by both exact pole residues and a quantitative monotonicity proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
