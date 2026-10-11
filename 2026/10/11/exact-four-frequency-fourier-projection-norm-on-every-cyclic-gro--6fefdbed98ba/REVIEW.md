# Same-model scientific review

## Correctness
**PASS.** The endpoint projection norm is reduced exactly to the normalized sampled \(L^1\) norm of the four-term Dirichlet kernel. The absolute kernel is \(4|\cos(\pi j/N)\cos(2\pi j/N)|\); its only sign split on the half-grid occurs at the quarter period. Exact finite cosine sums then give the all-\(N\) formula. Residue-specific algebra and Taylor expansion give the stated second-order coefficients. The included verifier checks the closed formula against direct kernel summation but is not used as an infinite proof.

## Originality
**PASS.** Searches covered exact four-character projection norms, sampled Dirichlet-kernel \(L^1\) norms, Lebesgue-constant aliases, support \(\{0,1,2,3\}\), modulo-four sampling defects, and possible arbitrary-block formulas. The nearest published statement concerns three consecutive characters and does not imply the four-character formula. Bonami--Révész and Ash provide the closest inspected primary literature context but do not state the theorem in the material read. The current and prior private ledgers were checked for implication-equivalent claims. An older equivalent formula under different terminology remains a stated residual risk, and full-text noncoverage is not claimed for the inaccessible closest published comparison.

## Value
**PASS.** This is an exact classical operator norm with a structural sampling phenomenon: the quarter-period zeros of the four-term kernel can lie on the cyclic mesh, and that alignment reverses the sign of the leading \(N^{-2}\) sampling error. The result therefore gives more than another fixed-size numerical constant.

## Closest literature and limitations
Bonami--Révész treat finite cyclic idempotents and Dirichlet kernels in a concentration framework. Ash treats Lebesgue constants and Dirichlet kernels, including the classical one-dimensional norm interpretation. The theorem here is restricted to the four consecutive frequencies and endpoint \(\ell^1/\ell^\infty\) projection norms; it does not classify arbitrary four-point spectra or intermediate exponents.

Same-model review: passed. Independent audit: not yet performed.
