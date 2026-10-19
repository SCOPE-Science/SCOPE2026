# Scientific review: cycle counts and outdegree statistics

## Correctness — PASS

Conditioning on one vertex's \(d\) outgoing arcs leaves all other arcs independently fair. Counting cycles anchored at the conditioned vertex proves the exact conditional mean (5), including the Hamilton-cycle endpoint. The total-covariance identity gives the master formula for arbitrary \(f\). Binomial coefficient and convolution identities independently yield the exact histogram and exceedance formulas, with positive finite prefactors establishing all sign and rank claims. Full exhaustive labeled-tournament enumeration at 3–6 vertices and 89,996 further parameter/sign checks passed; the analytic argument is required for the infinite family.

## Originality — PASS with specified residual risks

The exact finite random-tournament **cross-covariance** for every cycle length and every additive degree statistic, with universal rank-one proportionality and complete bin/threshold signs, was not found in examined directly relevant sources. Linial–Morgenstern's analysis of three- and four-cycle densities is extremal rather than a random-score covariance result. Komarov–Mackey's exact five-cycle formula uses an edge-score sequence that is strictly richer than the vertex-degree histogram; their theorem does not state the current family of expectations/covariances. Kuo–Liu–Ribas–Zhou (2019) give a sieve upper bound for random-tournament cycle-count multiplicities, not a joint outdegree result. Known deterministic three-cycle degree identities provide a plausible partial precursor, not the all-length conditional mean.

An implicit derivation from earlier edge-score identities or general motif-projection theory is a genuine priority risk. The complete Butts (2006) directed cycle-census text was not accessible for direct comparison, and its abstract does not resolve possible implication. Review does not establish independently certified novelty.

## Mathematical value — PASS

The outdegree histogram is the natural score-profile diagnostic for a fair random tournament, whereas directed-cycle counts measure recurrent orientation motifs. An exact **rank-one dependence structure** across all cycle lengths is a substantive structural simplification: it permits every linear outdegree adjustment to be transferred from triangles to all longer cycles. The degree-bin zero/sign transitions (including square-order exact zeros) and sharp exceedance sign threshold provide complete natural finite-dimensional classifications, not an arbitrary parameter slice.

## Limits and closest literature

The result covers independent unbiased orientations, not fixed-degree tournaments or biased edge laws. Orthogonality is not independence; rank one applies only to the cross-covariance operator. Closest papers: Linial–Morgenstern (arXiv:1405.1576), Komarov–Mackey (arXiv:1410.6828), Kuo et al. (2019); accessible abstract only: Butts (2006). Potential priority implications from general second-order motif methods remain.

Self-review: passed. Independent audit: not yet performed.
