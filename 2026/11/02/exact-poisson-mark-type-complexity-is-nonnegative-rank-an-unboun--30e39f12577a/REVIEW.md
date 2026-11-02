# Scientific review: exact marked-Poisson type complexity

## Correctness — PASS

The proposed theorem states an exact equality of the minimal latent child-type number and the ordinary nonnegative rank of the mean-mark interaction matrix, **within a precise parent-independent-emission Poisson reproduction model**. Independent Poisson splitting/superposition proves the forward representation, and normalization of every nonnegative factorization proves the reverse. An inductive generation argument upgrades reproduction equality to the entire unthinned marked tree. A support-antichain argument gives the known central-binomial nonnegative-rank bound for squared-distance matrices; a Vandermonde coefficient determinant equals \(2\delta^{k-3}\) after positive rank-\(k\) perturbation; compactness of normalized factors proves perturbation stability. All 2,206 finite rational assertions in `verify.py` passed. These computations corroborate the analytic proof and are not substituted for infinite arguments.

## Originality — PASS, qualified

The motivating work [1] explicitly poses the question whether bounded ordinary rank, beyond rank two, forces a bounded number of latent branching types. This result gives a negative answer for the exact Poisson child-type/mark-emission mechanism, by establishing that its minimum is the nonnegative rank. The rank-three squared-distance nonnegative-rank lower bound [2,3], general rank-three separations [4], and positive perturbation stability [5] were known and are expressly credited; none is individually claimed new. The specific stochastic exact-type correspondence and sparse full-support consequence were not found in the inspected sources. An earlier implicit/explicit formulation of that bridge remains a material priority risk, and the original 2009 full text was inaccessible (its bound is corroborated in [3]). No historical uniqueness or independent certification is claimed.

## Value — PASS

This supplies a structural answer to a question of intrinsic interest in probability and random-graph exploration: the number of exact latent Poisson channels cannot be controlled by ordinary matrix rank alone, even for strictly positive sparse graph kernels of each fixed rank at least three. The exact invariance and the need for a parent-independent emission law clarify the boundary of finite-type reductions. The finite rank gap alone is not the contribution; the probabilistic model implication is the motivation.

## Limitations

Positive perturbation amplitudes are existential rather than numerically specified. The result concerns unthinned exact offspring laws, not every alternative graph-neighborhood sampler or a process whose emissions depend on the parent mark. More general notions of minimal graph-exploration type remain unresolved. Independent audit and definitive priority assessment are outstanding.

## Closest literature

[1] Chakraborty, Raaijmakers, van der Hofstad (2022), arXiv:2207.11471v1, Sections 1, 2, 7. [2] Beasley and Laffey (2009), DOI 10.1016/j.laa.2009.02.034. [3] Gillis and Glineur (2010), arXiv:1009.0880, Sections 3, 4.2. [4] Shitov (2013), arXiv:1308.4716. [5] Bocci, Carlini and Rapallo (2010), arXiv:1010.3566, Theorem 2.

Self-review: passed. Independent audit: not yet performed.
