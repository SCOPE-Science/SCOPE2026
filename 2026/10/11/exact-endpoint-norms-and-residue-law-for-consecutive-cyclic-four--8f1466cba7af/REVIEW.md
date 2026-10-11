# Same-model review

## Correctness
**PASS.** The endpoint norm is exactly the normalized \(\ell^1\) norm of the convolution kernel. The numerator \(\sin(\pi m j/N)\) has a completely controlled alternating sign on the \(m\) blocks cut by \(\lfloor kN/m\rfloor\), so the absolute sum telescopes to partial sums of \(\sin(m\theta)/\sin\theta\). The two parity formulas for those partial sums follow from finite cosine identities. For the asymptotic statement, the only singularities of the periodic absolute Dirichlet kernel are first-derivative jumps of size \(2m\pi\csc(\pi k/m)\); two integrations by parts and the Bernoulli Fourier series give the stated coefficient, while the piecewise smooth remainder gives \(O_m(N^{-3})\). The standalone replay agrees with the exact formula in 4205 test pairs and with all residue classes through \(m=10\).

## Originality
**PASS.** The closest archive-era primary sources define idempotent trigonometric polynomials, Dirichlet kernels, finite grids, and the finite cyclic concentration problem, but the inspected full text does not state the exact endpoint norm for arbitrary consecutive block length. The closest published exact finite-cycle projection result found in published-finding corpus is restricted to three consecutive frequencies; its statement explicitly limits itself to that block length. Searches of the operator-norm, sampled-kernel, absolute-sine-ratio, and Bernoulli-residue formulations found no all-length theorem implying the claim. Residual risk remains that an equivalent elementary identity is buried in older approximation or numerical-Fourier literature under different terminology.

## Value
**PASS.** Consecutive Fourier projections are the canonical finite cyclic analogues of ordinary Fourier partial sums, and their endpoint norms are discrete Lebesgue constants. The result gives one formula for every block length and every nonaliased cyclic grid, replaces an \(N\)-term absolute-value sum by a fixed-length exact expression, and identifies the complete residue-class dependence of the leading sampling error. This is a structural all-parameter theorem rather than another isolated small-block evaluation.

Same-model review: passed. Independent audit: not yet performed.
