# Review of ternary-support orthograph clique construction

## Correctness — PASS
Every representative is nonzero, and fixing its first sign prevents duplicate projective lines. For unequal size-\(k\) supports, a coordinate disappearing in each direction witnesses both orthogonality inequalities for every scalar. For identical supports, the first common positive coordinate and one opposite-sign coordinate yield the sharp inequality \(\max(|1+\lambda|,|1-\lambda|)\ge1\) over \(\mathbb R\) and \(\mathbb C\). Layer cardinalities, the maximizing support size, and binomial asymptotics are derived analytically. A bundled Python standard-library checker reproduces 475172 exact real pair checks across representative finite layers; it does not prove the infinite family.

## Originality — PASS with residual risk
The 2021 primary article, Example 3.7, gives \(2^{n-1}\) orthogonal projective sign-cube points using *all* coordinates. The 2024 projective orthodigraph classification gives graph-characterization theorems, not the equal-support combinatorial construction or its exponential improvement. published-finding corpus alias and statement searches did not yield a covering claim. The relevant 2022 survey could be read only at abstract/reference level, and equivalent unindexed literature remains possible. Full-document noncoverage is *not* asserted for that survey.

## Value — PASS
The construction raises a published clique-growth lower bound from base \(2\) to base \(3\) (up to the unavoidable binomial-layer factor \(n^{-1/2}\)), for every dimension and both scalar fields. Cross-support orthogonality is the key structural lemma rather than a relabeling of full-support corners. Its scope is precise: the true clique number may be larger, and the layer maximum is not claimed to be a global maximum.

Same-model review: passed. Independent audit: not yet performed.
