# Same-model review

## Correctness
PASS. The generalized Vandermonde determinant factors exactly as the ordinary Vandermonde product times \(z_1+z_2+z_3+z_4\). For four distinct unit roots, zero sum forces both the first and third elementary symmetric functions to vanish, so the root polynomial is even and the roots are precisely two antipodal pairs. The converse is immediate. This gives the full all-\(N\) classification, and the rank-\(3\) assertion follows from the ordinary Vandermonde rank of the first three rows. Exact symbolic and cyclotomic checks through \(N=40\) corroborate the argument.

## Originality
PASS. The closest full-text source proves an iff criterion for prime-power DFT sizes, proves uniform distribution necessary for all sizes, and explicitly shows that sufficiency fails for general composite sizes. It therefore covers the odd prime-power subcase but does not imply the all-modulus special-family theorem, the antipodal classification of every singular minor, the exact bad-minor count, or the rank statement. Searches under harmonic-frame, DFT-minor, generalized-Vandermonde, and roots-of-unity formulations found no covering result. The determinant factorization itself is classical and is not claimed as new. Residual risk remains for older material indexed only under roots-of-unity sums or generalized Vandermonde identities.

## Value
PASS. The row set \(\{0,1,2,4\}\) is the first one-step perturbation of four consecutive DFT rows, and its generalized Vandermonde quotient collapses to a single elementary symmetric function. The result gives a complete all-modulus answer to a natural harmonic-frame instance inside a setting where the general composite-size criterion is known to fail, and it identifies the entire failure geometry rather than only deciding full spark.

## Closest literature and limitations
Alexeev-Cahill-Mixon is the decisive comparison: prime powers are already covered, while arbitrary composite sizes are not. Isaacs-Evans is relevant generalized-Vandermonde/root-of-unity background for prime order. The accepted claim is intentionally restricted to the fixed row pattern and makes no general four-row classification claim.

Same-model review: passed. Independent audit: not yet performed.
