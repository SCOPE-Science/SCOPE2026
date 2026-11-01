# Exact cyclic Fourier-projection endpoint norms — scientific assessment

## Correctness

**PASS.** The normalized cyclic convolution kernel has both endpoint operator norms equal to its average absolute value. Replacing the sample at zero by the absolute quotient limit at one, segmenting by the zero locations k/m, and summing the trigonometric polynomial over each resulting interval gives the exact finite expression for every N≥m≥2. Endpoint m=N and exact zero-alignment cases are covered. For fixed m, the only derivative jumps of the periodic absolute sine quotient occur at k/m, have height 2mπ csc(πk/m), and yield the stated residue-dependent N^{-2} coefficient by Fourier aliasing and the Bernoulli B2 series. Independent high-precision finite calculations corroborate the result without replacing its proof.

## Originality

**PASS, best of knowledge for the complete finite all-block expression.** The published exact m=3 and m=4 projection results are special cases, not statements for every block length. Bonami–Révész address idempotent concentration rather than this exact cyclic endpoint norm. Importantly, the general Bernoulli jump-error mechanism and its specialization to this integrand are covered by the generalized Euler–Maclaurin theorem of Berrut–Trummer (2022, Theorem 2), with an earlier formulation by Berrut (2006). The present claim should not be described as discovering that generic mechanism. An equivalent exact all-block sign-summation identity in older approximation literature remains a historical-priority risk.

## Mathematical value

**PASS.** The result supplies the canonical exact finite cyclic Lebesgue constants for every nonaliased consecutive block, reducing an N-term absolute sum to a fixed-m trigonometric expression and quantifying the zero-grid alignment dependence for each fixed m. This is a natural reusable exact invariant; it does not extend to arbitrary spectral subsets, intermediate ℓp norms, or uniform growing-m asymptotics.

No external expert attestation or formal verification is asserted.
