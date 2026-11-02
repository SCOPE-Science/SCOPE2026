# Mathematical review

## Correctness — PASS

The claimed parameter class is explicitly defined by three symmetric stochastic edge semigroups with identical \(t>0\). Reconstructed exact matrix products yield the nonstationary quadratic, determinant and factored discriminant. The complex region has modulus \(r^{3/2}\), and the negative-real region has two manifestly strictly decreasing positive contributions to its spectral radius as \(r\) increases; thus the sole boundary point is globally optimal. The antisymmetric-entry identity excludes diagonalizability at the repeated eigenvalue, and the limiting \(r=0\) polynomial gives \(1/8\). Exact-rational independent computations in `verify.py` check finite identities but are not substituted for the polynomial and monotonicity proof. The rate is only per sweep, not per wall-clock or physical diffusion time.

## Originality — PASS (qualified)

Backlund et al. (arXiv:1808.09047, abstract and systematic-versus-random scan introductory material), Shimizu--Shiraga (arXiv:2102.08002, introductory/results sections and mixing analysis), and Dyer--Greenhill--Ullrich (arXiv:1301.4055, heat-bath definition, Lemma 1.2 and proof) were inspected at their primary open-access full texts. They establish general algorithm classes, common-invariant-measure bounds, and nonnegative spectra of *mixtures*, respectively; none of those specific results implies the ordered three-edge product's exact discriminant, defective transition or unique sharp tuning. published-finding corpus searches of triangle edge sweeps, stochastic projection products, reversible factors, and relaxation/eigenvalue aliases returned related but not covering findings. General nonreversibility and noncommutativity are acknowledged as known. Specialized cyclic-projection optimal-relaxation literature (Censor et al., DOI 10.1137/050639399) could only be checked through its abstract; priority remains qualified.

## Value — PASS

The canonical smallest cycle with three reversible, strictly positive-definite local heat semigroups has an exact optimal nonzero damping duration. The proof quantifies a counterintuitive phenomenon: an ordered local diffusion sweep can converge substantially more slowly when its individual edge steps are allowed to fully equilibrate. The defective spectral transition also distinguishes asymptotic tuning from finite-iterate guarantees. This is a natural complete one-parameter optimization relevant to cyclic operator splitting, Markov sweeps, and distributed averaging, not an arbitrary numerical slice.

## Limitations and closest literature

No optimality over arbitrary Markov kernels, unequal edge rates, different sweep orders, total physical time or finite-time total variation is asserted. Closest sources: arXiv:1301.4055 for mixtures of heat-bath kernels; arXiv:2102.08002 for dynamic reversible transitions; arXiv:1808.09047 for systematic versus random scan; DOI 10.1137/050639399 for related projection relaxation (abstract only).

Self-review: passed. Independent audit: not yet performed.
