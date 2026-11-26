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

The cosine integral against the real signed empirical-minus-uniform measure is the squared modulus of its complex Fourier coefficient; each selected frequency has zero Lebesgue coefficient. Time-off-diagonal terms integrate to zero since m(q^t−q^s) is a nonzero integer, so the normalized expected squared discrepancy is exactly the sum of weights. For a primitive frequency the conditional expectation given X_{t+1} averages the q equally likely preimages and is zero. Reversing a row of T increments gives a bounded martingale-difference array. Each real linear combination of the primitive modes has conditional second moment equal to its transfer-averaged square. The stationary ergodic average tends almost surely to its Lebesgue square integral, which is one-half the squared Euclidean norm of the real coefficients; boundedness gives Lindeberg. Cramér–Wold thus gives independent circular Gaussians with mean-one squared moduli. The finite endpoint shift has error at most 2j before normalization, so orbit weights combine; iid orthogonality instead gives one Gaussian per selected frequency. Positivity of weights makes the variance comparison strict if any orbit is repeated. If interpreted as convergence of actual variances as well as comparison of the limiting laws, normalized real and imaginary sums of each fixed mode have bounded sixth moments by the bounded-difference martingale tail bound on their shifted primitive windows. Thus the squares of the weighted discrepancies are uniformly integrable. For the single-orbit exact formula, the only equal two-term sums of q-powers are permutations, including when q=2: two unequal exponents have two 1-bits while equal exponents give one after a carry. The labeled direct and swapped matchings contribute T² and h² with h common choices, respectively. Subtracting T² leaves h(h−1), including disjoint windows and T=1. The two-frequency example means consecutive shifts within that orbit, not consecutive integer frequencies in general.

## originality

PASS

Credit is for the exact finite-sample calibration calculation, principally the single-orbit variance for arbitrary shifts, including dyadic and composite bases. The weighted-exponential limit and iid criterion follow from an existing lacunary CLT after resolving the primitive modes and using the endpoint-shift identity, so the asymptotic mechanism is not separately credited as a new limit theorem. The exact mean is a direct orthogonality calculation. The strongest algebraic precursor examined supplies signed lacunary uniqueness under a stronger separation restriction; it does not supply the full all-base positive-power overlapping-window identity. The closest local records give finite or asymptotic variance for different pair-correlation statistics, or optimize a different additive-energy polynomial. On inspected evidence the finite-sample result is distinct, with the limits below.

## value

PASS

For a fixed Fourier-feature goodness-of-fit statistic this is an exact benchmark for mean matching despite dependence, and for how a single multiplicative orbit changes variance at every sample size. The finite formula identifies the role of window overlap even when two high frequencies share an asymptotic Gaussian mode but have disjoint time windows at the sample size used. This is usable finite calibration information beyond the known Gaussian limit; no full null quantile calibration or characteristic-kernel result is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
