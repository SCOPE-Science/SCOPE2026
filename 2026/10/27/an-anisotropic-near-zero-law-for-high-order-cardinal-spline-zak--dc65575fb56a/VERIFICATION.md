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

The positive Zak exponent leads to Fourier aliases n+omega with phases exp(2 pi i(n+omega)x), by taking Fourier coefficients of exp(-2 pi i omega x)Z. The sinc power and first derivatives are summable uniformly on compact coordinate ranges for m>=3; the parenthetical uniformity in proof step 1 should be read on bounded ranges such as the fundamental square, not as uniform convergence of fixed-index partial sums on R^2. The finding only needs the bounded ranges. On omega=1/2+s/m the n=0,-1 amplitudes are [cos(pi s/m)/(1±2s/m)]^m; their logarithms and s derivatives converge uniformly on bounded s. The remaining aliases are bounded by summable inverse odd-frequency powers, also after x or scaled-frequency differentiation. For r in [0,1/2] the tail is at most 2 a sum_{j>=1}(2j+1)^(-m), the second-to-first amplitude ratio is at most e^(-4u), and a/h_m>=e^(cu) because log(sin(pi r)/(2r))/(1/2-r) has a positive continuous extension. This gives strict exclusion outside a bounded scaled strip for fixed tau. The limit's level boundary has zero area by vertical sections; their sublevel lengths produce A(tau). Substitution t=cos(pi x) in that integral reduces the small-tau leading term to the semicircle integral on [-tau/2,tau/2] divided by pi; the relative Taylor error is O(tau^2). At the central zero, paired half-integer aliases give a negative real x derivative and negative imaginary omega derivative, with the sums in RESULT.md:81–82. Odd m gives positive-term sums and even m positive alternating sums, hence the determinant is strictly positive for every m>=3 with the stated sharp error. The known zero uniqueness also matches the centered convention. Inspected CHECKER.py, CHECKER_OUTPUT.txt and VERIFICATION.md; the reported finite diagnostics are not a proof of confinement or convergence and were not rerun.

## originality

PASS

The distinct quantitative finding is the unit-scale, increasing-order C^1 profile, global fixed-threshold area limit, and sharp transverse determinant. The zero location and uniqueness are established prior results, with the parity-dependent uncentered locations becoming identical after shifting by m/2. Related indexed statements concern other scales, one fixed order, or a half-density frame symbol rather than the present unit-scale small-modulus distribution.

## value

PASS

Full-cell sublevel area measures how much of the Zak symbol is poorly conditioned, which a zero set alone cannot do. The exact order-scale profile and explicit area separate exponential amplitude decay from the 1/m frequency width, with an independent sharp local determinant normalization. These address a meaningful aspect of the critical Zak symbol without claiming a noncritical Gabor frame bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
