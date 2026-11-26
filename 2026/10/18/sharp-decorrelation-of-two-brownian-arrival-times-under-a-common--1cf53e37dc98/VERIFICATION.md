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

The first shared exponential gap R gives the regenerative pair T_i=min(H_i,R)+1_{H_i>R}T′_i; future times have the fresh joint law. The marginal second moments are finite (also seen from the analytic renewal transform at zero), and differentiating that transform gives the stated variance. Conditional on R the two truncated hit times have mean K(R), while integration by parts gives E[K(R)Q(R)]=rA/2. The probability both need the fresh cycle is 1−2p+J. Substituting the marginal mean yields A/[p(2p−J)]. Conditional independence given the clock gives a covariance equal to the variance of the conditional mean. The latter is strictly positive because K(s)+Q(s)m, conditional on the first gap s, is continuous and unbounded as s→∞. For an independent prefactor check, use J=∫exp(−τ)erfc(z/(2√τ))²dτ and scale τ=zu. The phase u+1/(2u) has its minimum √2 at u=1/√2 and second derivative 2√2 there; the local amplitude is 4u/(πz) after scaling. The global erfc upper bound and phase gap off the saddle control tails and give J∼2^(5/4)exp(−√2 z)/√(π z). The A error after scaling is bounded by twice E[(rR)²1_{H<R}]=2p(z²/4+5z/4+2), negligible against J/p. Hence the Pearson correlation is asymptotic to J/(2p). Independent quadrature used Cov=E[(K(R)−m(1−Q(R)))²]/(2p−J) from the conditional-mean renewal, in normalized units; it agrees with the stated covariance, and the exact/asymptotic correlation ratios at z=20 and 60 were 0.935416908 and 0.976388691. Replay: python3 branches/independent_checks.py 4 (mpmath).

## originality

PASS

The shared-clock model, labeled-arrival correlations in qualitative terms and the renewal framework are known. The inspected strongest matches do not supply the exact equal-distance pair mixed moment together with its strong-reset Pearson exponent and prefactor. In particular, the same-date same-model fixed-time survival result is genuine overlap in conditional-clock technique and positivity, but it does not do the mixed-time moment evaluation or the rare joint-hit asymptotic. The pass is for the quantitative result and not for the single-walker transform or the general idea that common resetting induces dependence.

## value

PASS

The equal-distance two-searcher case is the minimal common-clock model in which labeling and irreversible arrivals make dependence scientifically relevant. The exact covariance characterizes the modeling error of treating shared and independent clocks alike. The sharp normalized rate identifies the mechanism: atypical simultaneous hits in a single excursion set the decay, even though the dependence has a strictly positive sign for every finite rate. A qualitative sign or a bound without the saddle prefactor would not quantify that effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
