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

Integrating the top-hat difference on each Fourier mode gives the positive product symbol p_beta(t) with limits 1/3 and 2 beta. To justify the uniform ratio rather than ratios on unrelated grids, approximate each of an arbitrary pair of finite positive frequencies on the same grid of spacing h=2 pi delta/L, then let h tend to zero. Finite frequencies approach both limiting spectral endpoints. For beta>0 the symbol has positive infimum by compactness and the endpoint limits. The inequality p_beta≥1/3 at all frequencies is exactly beta≥sup H. Sine's upper Taylor bound and the negative sine on [pi,2 pi] give H≤1/6 through 2 pi, whereas H(5 pi/2)>1/6 and the limits of H are 1/20 and 1/6. The envelope t/[6(t−1)]−t^-2 bounds H above on the tail and is strictly below 9/50 there (the difference has numerator 2t³−27t²+150t−150 after multiplication by 150 t²(t−1)). At beta_star the symbol's maximum is attained below 2 pi: its value at pi exceeds 8/15, but the tail is at most 1309/2700 and the zero-frequency limit is 1/3. The attained threshold minimum is above 2 pi. Fixing the resulting maximizing and minimizing frequencies u<t, their ratio strictly decreases with beta, excluding every smaller beta. Every larger beta raises the value at u while the infimum cannot exceed 1/3. For beta=1/6 the lower tail estimate reduces to t³−10t²+60t−60≥0 for t≥6; the upper estimate uses the alternating Taylor bound through t^6 for sinc up to 19/5 and the decreasing envelope (1+1/t)(1+6/t²) thereafter. This gives p in [3/10,3/5]. At beta=1/2 the sine Taylor upper bound through degree 13 gives p(4)>4/3. All needed Taylor remainders have the asserted signs by decrease of the terms in the withheld tails over the stated ranges. Independent rational checks and local stationary-point diagnostics (python /workspace/review_checks.py, check 4) reproduce about 0.1747779923813 and 1.700200564562; these diagnostics do not certify global maximizing frequencies, nor are they needed for the theorem.

## originality

PASS

The checked sources supply the preconditioner family and robustness results, or exact spread at one fixed coefficient, but do not imply the unique uniform minimizer over coefficients. Distinct supported contribution: the all-beta minimax characterization and uniqueness, with the quantitative comparison to the kernel-mass prescription. This is a best-of-knowledge statement, not exhaustive priority certification.

## value

PASS

The mass coefficient is prescribed by a substantive existing construction, so optimizing it for the canonical top-hat symbol is not an arbitrary parameter search. Separation of the active frequencies turns two pointwise comparisons into a unique robust optimum, and the certified greater-than-two improvement is material for the ideal spectral model. It is a useful benchmark, not a PCG iteration or finite-element tuning guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
