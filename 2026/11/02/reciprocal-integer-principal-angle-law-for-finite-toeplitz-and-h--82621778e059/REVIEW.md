# Review of the reciprocal-integer Toeplitz–Hankel principal-angle law

## Correctness

PASS. The finite cross-Gram entry formula follows directly by intersection of a diagonal and an antidiagonal. The parity-block continuum embedding uses mesh \(2/n\) and kernel normalization \(G_n/h\); the boundary contribution has a uniform \(O(\delta)\) squared Hilbert–Schmidt estimate. The reflected limit is the weighted Volterra operator whose positive singular values are exactly \(1/k\), by the explicit terminating-hypergeometric Sturm–Liouville eigenpolynomials and their completeness. Combining two blocks supplies two copies. The principal-vector argument gives the **sharp** decomposition constant, with equality in each finite dimension. The standalone finite checker passed 43,864 assertions, but finite checks do not establish the asymptotic theorem.

## Originality

PASS under a best-knowledge literature comparison, not a claim of certified publication priority. The closest source is Babbar–Majee–Maji, arXiv:2610.35897v1 (Theorems 5.5 and 6.1), which identifies and parametrizes the two-dimensional intersection but gives no quantitative principal-angle spectrum. Bhuia–Majee, arXiv:2606.09370v1 (Section 5), identifies the checkerboard ambiguity and matrix recurrence, again without this spectrum. Established projection-angle theory explains what the cross-Gram singular values represent but not the reciprocal-integer numbers. Searches for Toeplitz/Hankel subspace canonical correlations, Frobenius principal angles, and stable decompositions returned no equivalent theorem. Residual risk: a historical treatment of canonical correlations between uniform-coordinate sum and difference, or Toeplitz–Hankel alternating projections, may imply some of these asymptotics indirectly.

## Mathematical value

PASS. Recent algebraic analysis leaves an intrinsically numerical question: how stable is the Toeplitz-plus-Hankel decomposition after its unavoidable two-dimensional ambiguity is removed? The complete limiting principal-angle distribution provides substantially more than one numerical bound and produces a sharp, dimension-uniform asymptotic lower stability constant of \(1/2\). It connects finite structured-matrix geometry to an exactly solvable weighted Volterra spectrum. The restriction to unweighted square Frobenius spaces is explicit; no general model-space uniform stability is asserted.

## Limitations

The result determines limiting singular values and their squared sum but not every finite-dimensional singular value in closed form. The limit concerns fixed spectral ranks as dimension increases and the strong \(\ell^2\) spectral topology. It does not establish priority or independent correctness verification.

Self-review: passed. Independent audit: not yet performed.
