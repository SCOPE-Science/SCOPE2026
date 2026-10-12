# Self-review

## Correctness
**PASS.** For \(R_0\ne1\), the Euler–Lotka kernel \(x\mapsto\lambda^{-x}\) is strictly convex at the root, so convex-order comparison of reproductive ages translates into the same ordering of growth factors after using strict monotonicity of the Euler–Lotka left side in \(\lambda\). The adjacent-age law is the least element in convex order among integer-valued laws of a fixed mean, and the endpoint law is the greatest under a fixed support window. Equality cases and the neutral case \(R_0=1\) are stated explicitly. The packaged exact-rational verifier returns `VERIFY_OK`.

Risk: the theorem assumes a strict age-class reduction and fixed \(R_0\) and \(\mu\); stage-structured systems need a separate argument.

## Originality
**PASS.** The continuous Jensen benchmark is prior: Jonasson and coauthors prove \(\lambda\ge R_0^{1/\mu}\), and Cochran and coauthors derive broader constrained-moment Euler–Lotka bounds. The accepted claim does not relabel those facts as new. Its surviving contribution is the order-theoretic statement that mean-preserving reproductive spread raises \(\lambda\) at fixed \(R_0\) and mean, together with the exact integer-lattice lower extremizer on the two adjacent ages and the resulting strict lattice correction. Targeted source, alias, exact-structure, and implication searches did not locate this statement.

Risk: the argument uses standard convex-order ideas, so an unindexed probability exercise or textbook lemma could imply the same lattice extremizer even if it was not located in demographic literature.

## Value
**PASS.** Age-class demographic models and microbial generation-time measurements naturally discretize reproductive timing. The usual Jensen lower benchmark is unattainable when the observed mean age is noninteger; the theorem replaces it with the exact attainable minimum and simultaneously identifies the maximum under a reproductive-age window. The result separates lifetime reproductive level, mean timing, and timing dispersion in a form directly usable for bounding growth from coarse life-history summaries.

Self-review: passed. Independent audit: not yet performed.
