# Research review

## Correctness
PASS. The first and extreme Fourier-mode Rayleigh inequalities give a universal lower bound using only average spoke and rim weights. A fully constructed invariant kernel attains the bound, including the hub-versus-rim eigenvalue constraint. Positive-semidefinite saturation of the first harmonic yields a quantitative residual bound; its imaginary rim coordinates control cyclic rim-weight variations via the cycle Poincaré gap, and its real coordinates control spoke variations. The proof explicitly treats every integer rim size at least four and nonnegative holding probabilities. A standard-library Jacobi spectral checker completed 22,532 finite numerical assertions. Those checks are corroboration, not an infinite proof.

## Originality
PASS under the checked literature, with a residual equivalence risk. Boyd–Diaconis–Parrilo–Xiao already give the wheel optimum value and a symmetric optimizer: neither is represented as new. Their automorphism argument supplies existence, whereas the additional theorem rules out all noninvariant competing optimizers and quantifies deviations of *each* edge from the optimum for arbitrary feasible symmetric kernels. The original wheel derivation in arXiv:0709.0955v1, Section 5.3.3, was inspected in detail; the general SDP formulation and symmetry literature were compared, as were published related cycle results and relevant public mathematical records. No equivalently strong all-edge quantitative stability result was found in these comparisons. Unindexed work may contain such a result.

## Value
PASS. Symmetry averaging by itself leaves open whether an optimally mixing wheel can conceal an inhomogeneous edge assignment. The uniqueness theorem resolves that exact design question. The global \(O_m(\sqrt\varepsilon)\) bounds also ensure that **every** nearly optimal feasible stochastic matrix, not just an invariant representative, has individual edge weights near the prescribed design. This supports sensitivity analysis and interpretation of numerically optimized near-solutions. No best-possible constant or stronger rate is asserted.

## Closest coverage and limitations
The exact spectral value and invariant transition weights are those of Boyd–Diaconis–Parrilo–Xiao (2007 preprint, 2009 journal). The scalar two-frequency minimax bound alone is not the contribution. The new equality-case Fourier reconstruction and quantitative residual-to-edge estimate require additional arguments. No comparison claims uniqueness among nonsymmetric or nonreversible chains. Independent external auditing remains outstanding.

Self-review: passed. Independent audit: not yet performed.
