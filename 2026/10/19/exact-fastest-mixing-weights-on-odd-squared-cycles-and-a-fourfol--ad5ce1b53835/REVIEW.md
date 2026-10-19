# Scientific review: Exact fastest-mixing weights on odd squared cycles and a fourfold spectral-gap gain

## Correctness — PASS

The proof reconstructs the domain and every nontrivial step: averaging an arbitrary supported symmetric stochastic chain over cycle symmetries; Fourier diagonalization; exact location of the discrete maximizer of a concave quadratic; strict holding-probability feasibility; and a three-contact affine impossibility certificate proving the full global optimal value and uniqueness only inside the invariant subclass. The comparison with single-step-length walks follows from the simple odd-cycle formula. The independently executed `verify.py` passed 1,651 finite tests including linear-program comparisons. Finite tests are not substituted for the mathematical proof.

## Originality — PASS, with residual risk

The 2004 Boyd–Diaconis–Xiao paper develops SDP optimization, and the 2009 Boyd–Diaconis–Parrilo–Xiao article supplies symmetry reduction and a one-orbit formula for the ordinary cycle, neither an explicit two-orbit odd cycle-square solution nor the fourfold spectral-gap limit. Previously recorded nearby claims concern resistance on squared cycles, even-cycle conductance-gap design, or stochastic polynomials on complete bipartite graphs; these do not imply this minimax result. Targeted published research and semantic research-record queries did not locate equivalent coverage. A thesis chapter about cycle mixing could not be inspected in full; equivalence there or elsewhere remains a priority for independent validation. Absence from search results is not proof of novelty.

## Value — PASS

A closed exact solution for every odd squared cycle, not one numerical graph, identifies positive near- and next-nearest-neighbor probabilities and a necessary holding probability. The asymptotic fourfold improvement from an \(O(n^{-2})\) correction is a substantive, structurally explained design phenomenon with direct meaning for spectral mixing and consensus. It is not a restatement of a general SDP algorithm.

## Limitations and closest sources

Full-text examined: Boyd et al., *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optimization 20 (2009), 792–819, especially Theorem 2.1 and Section 3; Boyd et al., *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. The inaccessible repository thesis and possible unindexed formulae are residual originality risks. The theorem does not establish unique arbitrary edgewise optimizers, address nonreversible kernels, or assert a universal finite-horizon mixing-time bound.

Self-review: passed. Independent audit: not yet performed.
