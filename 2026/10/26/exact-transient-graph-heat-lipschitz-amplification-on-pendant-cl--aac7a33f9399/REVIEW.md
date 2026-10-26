# Scientific review

**Correctness — PASS.** The proof specifies the unnormalized graph Laplacian and graph-distance Lipschitz seminorm. All three symmetry classes of edges have exact signed heat-kernel decompositions and Wasserstein costs; comparison identifies the pendant edge. The derivative gives the unique expansion threshold and peak. Independent finite-dimensional checks in `verify.py` solve the transport LP directly. The 147 finite instances validate algebraic formulas but do not replace the all-time analytic proof.

**Originality — PASS with residual risk.** Searches for pendant-clique heat Lipschitz norms, exact two-exponential profiles, aliases such as lollipop/pineapple/whiskered clique, and related published-finding corpus findings returned no implication-equivalent exact family. Joulin's continuous-time definition and Ollivier's duality are general frameworks; Lin–Lu–Yau's graph curvature treats a different operator normalization. The previous diameter-sharp graph-heat result controls all graphs but does not imply this fixed-family exact profile or first failure at clique size four. Unindexed older heat-kernel calculations remain possible.

**Mathematical value — PASS.** A complete graph alone is strongly heat contractive, but a single pendant measurement location creates a noncontractive transient. The exact first dimension of failure and explicit peak quantify how a single bottleneck changes regularity. The bound asymptotically attains the diameter-two envelope on a graph family of minimal bottleneck complexity.

**Limitations.** Simple unweighted pendant cliques, unnormalized heat, real graph-distance Lipschitz seminorm; no transfer to normalized chains or multiple leaves is asserted.

Self-review: passed. Independent audit: not yet performed.
