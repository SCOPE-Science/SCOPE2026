# Scientific review

## Correctness — PASS

Graph automorphism averaging validly reduces the globally unconstrained symmetric stochastic zero-diagonal problem to a single scalar rim-edge probability. Exact cycle-layer spectral decomposition identifies two antisymmetric modes whose minimax balance forces a unique optimal scalar. Every remaining Fourier eigenvalue is shown explicitly to lie in the same symmetric interval. Even prisms are bipartite and therefore have a universal eigenvalue \(-1\). A standalone numerical verifier corroborates the exact inequalities. The proof, not the finite checks, supports all dimensions.

## Originality — PASS, qualified

The sections of the 2007 Boyd–Diaconis–Parrilo–Xiao preprint inspected present global FMMC symmetry reduction and Cartesian graph products while allowing self-loops; the accessible formulation of the 2004 Boyd–Diaconis–Xiao problem also allows holding. A related exact fastest-mixing prism result with holding permitted provides a different optimum and does not solve the additional zero-diagonal constraint. The new claim is the complete constrained optimum and its odd/even dichotomy, not the underlying symmetry principle. The accessible search did not identify a published all-size loopless-prism formula; however, absence of a match does not prove novelty and specialized historical coverage remains a residual risk.

## Value — PASS

Forbidding waiting steps is a natural protocol constraint and can completely prevent mixing even on a connected graph. For the complementary nonbipartite sizes, the theorem supplies an explicit globally optimal transition rule and quantifies the exact spectral penalty: a fourfold reduction in the asymptotic gap compared with protocols permitting holding. These finite-dimensional exact design prescriptions are useful independently of a more general downstream theorem. They are not obtained by merely plugging the unrestricted optimal weights into a constraint, because those weights have positive holding probabilities.

## Sources and limits

Boyd et al., *Fastest Mixing Markov Chain on a Graph* (2004), https://doi.org/10.1137/S0036144503423264; Boyd et al., *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007), https://arxiv.org/abs/0709.0955. The exact claim concerns symmetric walks only. Finite tests supplement the proof; historical completeness and independent review are not established.

Self-review: passed. Independent audit: not yet performed.
