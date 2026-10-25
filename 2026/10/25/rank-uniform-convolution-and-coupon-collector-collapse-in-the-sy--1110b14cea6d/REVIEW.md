# Mathematical assessment

## Correctness — PASS

Every uniform fixed-rank partial bijection has precisely \(a!\) extensions to a full permutation. Pulling each independent deletion set back through preceding permutations gives independent uniform subsets, jointly independent of the final uniform permutation. Inclusion-exclusion on their union proves the complete individual-map product probabilities. Hypergeometric survival gives the exact rank kernel and its falling-factorial eigenbasis; the fixed-batch Poisson/Gumbel limit follows from factorial moments. Endpoints \(a=0\), \(a=n\), \(k=1\), and \(t=0\) are handled explicitly. Independent exhaustive exact-arithmetic enumeration and matrix-free transition checks pass. Limitations: the computer checks do not prove infinite assertions; those have separate analytic proofs.

## Originality — PASS, with documented historical uncertainty

The closest inspected semigroup paper (André–Fernandes–Mitchell, DOI:10.1017/S0013091505001598) determines maximal two-generated subsemigroups and rank-stratum counts, not the uniform-product probability distribution. Malandro (arXiv:1212.6462) supplies general FFT methods for arbitrary inverse-semigroup convolution; its general algorithm can in principle evaluate the present convolution but does not imply the concise closed rank-uniform structure *as a stated theorem*. Ivanov–Kerov (arXiv:math/0302203) work with support-preserving partial permutations and support-union multiplication, distinct from the symmetric inverse monoid. The explicit batch-coupon absorption consequences overlap classical coupon-collection research; those consequences are not independently claimed as novel. Comparisons against relevant published statements identified no covering semigroup-valued claim. Older monographs and implicit Fourier-derived presentations remain priority risks; a failed search cannot establish uniqueness.

## Value — PASS

The rank strata are the canonical \(S_n\times S_n\)-orbits of a natural inverse monoid. Their convolution constants quantify products of arbitrary many factors at the **individual transformation** level. The symmetric deletion-set coupling proves commutativity and diagonalizes the complete induced rank Markov chain, while identifying precise absorption behavior. This resolves a natural finite-semigroup random-product invariant with exact and asymptotic descriptions, rather than an arbitrary narrow numerical slice.

Self-review: passed. Independent audit: not yet performed.
