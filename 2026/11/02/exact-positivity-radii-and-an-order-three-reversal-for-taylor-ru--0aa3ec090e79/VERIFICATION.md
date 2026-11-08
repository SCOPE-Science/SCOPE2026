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

For unweighted connected complete multipartite K_{n1,...,nk}, the orthogonal projector decomposition of L has eigenvalues 0,N,N-ni, yielding exact cross-part X=(1-r_p(Nh))/N and within-part Y. For p=2, r2 is strictly positive and Y=q h²/2; only cross-part entries turn negative beyond 2/N. For p=4, r4 is everywhere positive, Y has a strictly positive quadratic factor (negative discriminant), and the strictly increasing cubic z³-4z²+12z-24 controls the unique cross-part cutoff rho4/N. For p=3, X>0 for h>0, the within-part entries vanish at 3/(2N-ni), and singleton diagonals vanish at eta_N/N, with r3 strictly decreasing. These inequalities prove the entire interval and order reversal, including N=2,3,4 and N=5 exception and balanced-part extrema. The independently written Fraction-based matrix expansion verified 522 multipartition/time-step matrices and 23,634 entries; this is finite corroboration only.

## originality

PASS

A targeted semantic mathematical-record search and primary-literature comparison found universal method SSP/absolute-monotonicity theorems, alternative rational integrators and positive ODE schemes, but none implies the joint exact endpoint nonnegativity intervals for the specific linear complete-multipartite Laplacians, the order-three reversal at N≥5 or optimal partition profiles. Horváth 1998 universal RK4 zero positivity radius does not contradict the positive restricted-family final-update radius. Classical RK polynomials and spectral decomposition are prior methods; no uniqueness-of-discovery claim is made.

## value

PASS

Exact nonnegative final-update timesteps are consequential for discretizations of diffusion/Markov generators. The same graph class exhibits a sharp method-order reversal and all-size optimal partition rules; the result settles natural infinite families and is neither a generic textbook SSP deduction nor an isolated numeric matrix example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
