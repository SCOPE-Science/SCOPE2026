# Independent audit — 2026-10-01

## Final claim

For stationary two-state alternating-renewal processes, the complete stationary two-time law identifies the total cycle mean and the sum of the two renewal transforms but generally not the two sojourn laws; for every two-state continuous-time Markov chain, the stated Erlang-2/hyperexponential non-Markov process has exactly the same two-time law at every lag.

## Correctness — PASS

The algebraic inverse statement reconstructs cleanly. For the alternative Erlang-2 state-1 law, the renewal transform is \(a/s-a/(s+4a)\); for the proposed state-0 phase-type law it is \(b/s+a/(s+4a)\), so the sum is exactly \((a+b)/s\). Substitution in the classical equilibrium covariance transform gives the same Laplace transform and hence the same exponential covariance as the two-state Markov chain. The denominator roots bracket \(a+b\), giving a genuine two-exponential mixture with the required mean. The large-\(s\) limit identifies \(M\), after which the covariance identifies only \(r_0+r_1\). A separate symbolic replay reproduced all cancellations and representative positive-parameter mixtures.

Checked sources:
- Akimoto, Physical Review E 108, 054113 (2023), arXiv:2306.00359; equilibrium alternating-renewal correlation formula.
- Lowen and Teich, Physical Review E 47 (1993); renewal-noise correlation context.
- Dewanji and Kalbfleisch, Biometrika 74 (1987); richer path-window identification of semi-Markov sojourn distributions.
- Resultary semantic query for alternating-renewal Markov pair-law aliasing; the assigned record was the only exact hit.

Residual risks:
- The finite numeric cases only corroborate the phase-type validity; the exact symbolic identities establish the all-parameter construction.

## Originality — PASS

Best-of-knowledge originality passes for the inverse equivalence-class statement and the all-rate phase-type Markov-mimicking construction. The forward equilibrium transform is classical and is not credited as new. No searched Resultary record or inspected primary statement supplied the exact decomposition non-identifiability or the universal Erlang/hyperexponential alias.

### Equivalent formulations

Searches:
- Resultary query: stationary alternating renewal process Markov same two-time law covariance identifiability renewal transform phase-type aliasing
- Akimoto 2023, arXiv:2306.00359

Evidence:
- The Resultary search returned the assigned finding as the sole exact-topic hit.
- Akimoto studies the forward correlation function for alternating renewal processes.

Reasoning: Equivalent formulations include non-identifiability from all binary two-time marginals, from the autocovariance, or from the Lorentzian spectrum; each reduces to the same renewal-transform sum.

### Broader coverage

Searches:
- Akimoto 2023 equilibrium-correlation analysis
- Dewanji--Kalbfleisch 1987 equilibrium semi-Markov estimation

Evidence:
- The former supplies the forward transform; the latter uses richer windowed path observations.

Reasoning: Neither source, as inspected, gives a stronger theorem saying that all two-time laws identify only the transform sum or constructs an all-rate Markov alias.

### Exact database or table

Searches:
- Resultary exact-topic semantic search
- Targeted comparison with classical alternating-renewal correlation sources

Evidence:
- No exact prior table or parametric family matching the construction was located.

Reasoning: There is no finite database table that could imply the analytic all-parameter construction; the relevant comparison is an explicit formula/construction search.

### Claim versus prior implication

Searches:
- Classical forward transform versus equations defining the alternative pair

Evidence:
- The forward transform becomes identical whenever the renewal-transform sums agree, but producing two admissible laws with prescribed means is an additional inverse construction.

Reasoning: The final inverse theorem is not the forward formula alone; admissibility and exact mean matching must be proved.

### Source inspections

- **Statistics of the number of renewals, occupation times, and correlation in ordinary, equilibrium, and aging alternating renewal processes** (https://arxiv.org/abs/2306.00359): trigger — Same alternating-renewal equilibrium correlation object; material read — Abstract plus the forward transform as quoted and algebraically checked against the inspected package; method — Primary-source comparison; no whole-document noncoverage inference; assessment — Covers the classical forward correlation calculation, not established coverage of the inverse aliasing theorem.; evidence — The article studies correlation functions for specified alternating-renewal laws; the audited novelty is explicitly limited to inverse equivalence and the phase-type construction.

Checked sources:
- Akimoto, Physical Review E 108, 054113 (2023), arXiv:2306.00359; equilibrium alternating-renewal correlation formula.
- Lowen and Teich, Physical Review E 47 (1993); renewal-noise correlation context.
- Dewanji and Kalbfleisch, Biometrika 74 (1987); richer path-window identification of semi-Markov sojourn distributions.
- Resultary semantic query for alternating-renewal Markov pair-law aliasing; the assigned record was the only exact hit.

Residual risks:
- Older reliability, random-telegraph, ion-channel, or semi-Markov literature may contain the inverse aliasing observation under different terminology.
- Akimoto full article text was not re-read end-to-end in this run; its abstract and the exact forward formula cited in the inspected record were compared, so no whole-document noncoverage claim is made.

## Scientific value — PASS

The theorem identifies exactly what complete second-order observation can and cannot recover in a natural semi-Markov model and gives a smooth finite-dimensional counterexample to a common Markov diagnostic. That is a motivated identifiability boundary with direct statistical interpretation, not a routine reformulation of the covariance formula.

Checked sources:
- Akimoto, Physical Review E 108, 054113 (2023), arXiv:2306.00359; equilibrium alternating-renewal correlation formula.
- Lowen and Teich, Physical Review E 47 (1993); renewal-noise correlation context.
- Dewanji and Kalbfleisch, Biometrika 74 (1987); richer path-window identification of semi-Markov sojourn distributions.
- Resultary semantic query for alternating-renewal Markov pair-law aliasing; the assigned record was the only exact hit.

Residual risks:
- Older reliability, random-telegraph, ion-channel, or semi-Markov literature may contain the inverse aliasing observation under different terminology.
- Akimoto full article text was not re-read end-to-end in this run; its abstract and the exact forward formula cited in the inspected record were compared, so no whole-document noncoverage claim is made.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
