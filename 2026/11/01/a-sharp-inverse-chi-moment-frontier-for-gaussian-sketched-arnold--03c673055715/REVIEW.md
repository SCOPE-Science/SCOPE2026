# Scientific review: a sharp inverse-chi moment frontier for Gaussian-sketched Arnoldi Hessenberg noise

## Correctness (PASS)

The theorem specifies the three-dimensional SPD matrix, Gaussian sketch dimensions and normalization, and the coefficient recorded before termination. The key identity \(h_{13}=C_\ell/r_{33}\) was reconstructed symbolically from \(RAR^{-1}\), with the matrix basis interpretation checked against the exact sketched Arnoldi recurrence. The Bartlett distribution makes \(r_{33}\sim\chi_{\ell-2}\) independent of a nonzero numerator \(C_\ell\) having a finite \((\ell-2)\)-moment. This proves the complete if-and-only-if moment threshold, the positive tail constant and the weak Gaussian limit. The finite regression tests verify algebra and algorithm consistency but do not substitute for these infinite statements. The theorem is not a claim about conditionally embedded sketches, other matrices or floating-point error.

## Originality (PASS, qualified)

The closest motivating source is Timsit, Grigori and Balabanov, arXiv:2302.07466 (first public preprint 2023-02-15), whose randomized Arnoldi section and Section 4.1 report a visually Gaussian pattern for the coefficients above the tridiagonal band and treat Gaussianity as an assumption. It does not establish the unconditional inverse-chi tail or sharp moment cutoff in this particular minimal SPD example. Balabanov and Grigori, arXiv:2011.05090, and Balabanov, arXiv:2210.09953, explain randomized Gram–Schmidt and sketch-based QR, but their inspected methodological sections do not state this coefficient law. Simoncini and Wang (2025) analyze stabilized randomized Krylov recurrences, not this exact distributional threshold. Searches for Gaussian-sketch Arnoldi Hessenberg Student, chi, Bartlett, power tails and exact moments did not expose an implication-equivalent theorem. These are best-knowledge comparisons, not proof of publication priority; specialized work on QR ratios or non-Gaussian Hessenberg coefficients is a residual risk. Gaussian QR independence and chi small-ball asymptotics themselves are standard and explicitly excluded from novelty.

## Value (PASS)

The source literature uses empirically Gaussian-looking above-tridiagonal coefficients to motivate short-recurrence analysis. This exact small model shows that the same coefficient's central limit is Gaussian even though an \(\ell=4\) Gaussian sketch has infinite coefficient variance. The first nontrivial above-tridiagonal entry, the whole dimension-dependent moment cutoff and the explicit tail are a naturally motivated diagnostic for what empirical histograms and standard embedding estimates cannot establish. The theorem does not imply a method-wide instability or assert performance failure; its value is a sharp boundary for unconditioned statistical modeling of this coefficient.

## Checks and limitations

Symbolic similarity identities, 900 independently seeded sketch QR/direct-Arnoldi comparisons and five small-chi CDF checks were executed using the standalone `verify.py`. The proof's weak Gaussian limit is not uniform moment convergence. The finite-dimensional matrix is intentionally the first example in which an above-tridiagonal entry exists; extension to higher Krylov dimensions or non-Gaussian sketches is unproved. Earlier equivalent specialized results may exist despite the searches and paper sections inspected.

Self-review: passed. Independent audit: not yet performed.
