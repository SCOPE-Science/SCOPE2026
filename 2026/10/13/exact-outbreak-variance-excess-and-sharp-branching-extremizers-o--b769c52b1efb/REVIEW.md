# Self-review

## Correctness — PASS

The scope fixes one infected root, one forward edge trial per tree edge, iid vertex-specific conditional transmissibilities, independent trials given those variables, and \(0<q<1\). A root-to-vertex path uses distinct latent variables, giving its infection probability \(q^{d(u)}\). For incomparable endpoints, their paths share exactly two edges with a common parent—their lowest common ancestor—so the pair-infection excess is exactly \(v q^{d(u)+d(w)-d(\ell(u,w))-2}\). Expanding the total-count variance yields the factor of two without wrongly assuming infection indicators independent. Every branching tree contains a sibling pair, and its depth and weight imply the sharp minimum; root-versus-nonroot comparability implies the sharp maximum. Both equality cases were checked including \(n=3\) and \(v=0\). The Laplace moment derivation of \(v\) for Poisson contacts and exponential recovery is direct. Independently enumerated exact rational small-tree cases in `verify_tree_variance.py` replay to `VERIFY_OK`, but finite enumeration is explicitly not the proof for arbitrary size.

## Originality — PASS, restricted to the precise theorem

The full 2026 source explicitly gives equality of marginal infection probabilities and means on trees; its Appendix A gives the outgoing-edge covariance and its Section VI observes increased large-network component-size variance. Those antecedents must not be relabeled as contributions. Kenah–Robins (2007) already provides exact epidemic-percolation representations, and Ramírez-Ramírez–Thompson (2013/2014) already develops variance formulas for configuration-model-type random networks with random infectious periods. The inspected sources do not state or logically directly specialize to the exact fixed-rooted-tree lowest-common-ancestor polynomial together with the unique finite-order star/broom extremal theorem: the general network branching approximation does not encode the positions of individual branches in an arbitrary fixed tree, and epidemic percolation alone requires further nontrivial expansion and optimization to give the theorem. Searches were made for synonymous outbreak dispersion, descendant-pair covariance, and rooted tree extrema; no matching result was identified. This is a self-review rather than a proof of absolute novelty. The most salient residual risk is that a general tree covariance theorem elsewhere might already imply the new formula and its extrema.

## Mathematical value — PASS

Finite-tree SIR risk analysis often uses a bond-percolation approximation because it gives exact infection marginals and expected outbreak size. The theorem establishes a structural, fully quantitative variance correction requiring only the first two moments of host transmissibility and the branching locations of a **known** rooted contact network. It distinguishes unbranched contact chains (zero excess), early centralized branching (maximal excess), and the sharp smallest nonzero risk distortion (one terminal split). The result therefore turns a qualitative modeling caveat into a computable sharp finite-network uncertainty bound and an extremal classification. No unproved claim is made for cyclic networks or stochastic tail probabilities beyond second moments.

## Literature limitations

The 2013 variance framework is the closest earlier analysis; its formula covers random network degree laws, not this exact fixed finite rooted-tree claim. Unindexed sources or implicit reductions may exist. The finding is not independently audited.

Self-review: passed. Independent audit: not yet performed.
