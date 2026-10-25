# Review of the edge-pair covariance sign classification

## Correctness
**PASS.** The exact deranged-matching recurrence follows from an inclusion–exclusion generating function. Conditioning on one allowed edge separates the other disjoint edges into precisely three orbits; symmetry, a forced-pair count, and the number of remaining edges give exact joint probabilities. The sign of the two-pair covariance follows from an explicit recurrence identity, with separate verification at the three small boundary sizes. All inequalities and asymptotic constants are proved for their stated ranges. The standalone exact checker counted and tested **19,267 assertions**, including enumeration of all deranged perfect matchings for two through seven original pairs. Finite testing supports but does not replace the unrestricted proof.

## Originality
**PASS, with priority risk.** Johnston–Kayll–Palmer (2022) gives deranged-matching enumeration, and Spiro–Surya (2022) develops asymptotic overlap counts. Granet–Joos (2023) and Deng (2025) provide asymptotic Poisson approximation results; these do not resolve the exact two-edge sign, including the exceptional four-pair reversal. The known count formula is not claimed as new. Searches for equivalent two-edge correlations, negative dependence, conditional matching indicators, and the complete multipartite \(K_{2,\ldots,2}\) model found no directly covering result. The sharp covariance classification may follow from an overlooked older special-function or switching identity, so historical priority is not certified.

## Value
**PASS.** Correlation sign is a structural dependence property of perfect matchings conditioned to avoid the forbidden pairs. Despite the usual positive covariance of disjoint-edge indicators in unrestricted complete-graph matchings, this natural exclusion model has both positive and negative disjoint-edge covariances. The theorem identifies precisely the local configuration producing repulsion, proves all parameter boundaries including the isolated four-pair anomaly, and quantifies distinct decay scales. The result is a complete infinite-family classification rather than an arbitrary numerical slice.

## Closest prior sources and limits
The earlier deranged-matching problem supplies the known enumeration and limit, and the 2022–2025 literature establishes coarse and multivariate Poisson overlap behavior. None of the inspected material yielded the exact finite two-edge covariance signs. No claim concerns weighted matching measures or stronger negative association; historical priority remains uncertain.

Self-review: passed. Independent audit: not yet performed.
