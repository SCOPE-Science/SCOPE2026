# Review of complete cubic spline Zak zeros

## Correctness (C): PASS

The proof handles every \(\lambda\in[1/2,1]\), \(x,\nu\in[0,1)\). Its critical nonstandard step is nonnegativity of four parameter-dependent cubic polynomials for all real parameters. The standalone rational-arithmetic certificate checks all 400 triangular Bernstein coefficients on a covering of the entire parameter rectangle and verifies total area exactly one, not a finite grid of sample points. At interior frequencies the final Bernstein coefficient is strictly positive; the edges use the sinc-fourth formula and positivity of the spline. The half-frequency classification invokes the published larger-scale B-spline Zak theorem after an exactly normalized aliasing identity. The endpoint at \(\lambda=1/2\) is separately covered.

## Originality (O): PASS

Hasannasab–Lemvig (arXiv:2609.13116v1) gives the superunit classification used in the half-frequency proof and already identifies the half-frequency subunit zero intervals in Proposition 4.1, but not the missing all-frequency cubic subunit continuum. Lemvig–Nielsen (arXiv:1507.03982v3) treats B-spline Gabor obstructions rather than this complete zero-set classification. An order-three real-scale result has different spline order and does not imply the cubic inequality; a known reciprocal-integer result covers a discrete endpoint only. A bounded literature/record search checked aliases, broader ranges, table implications and mathematical statement overlap. An older equivalent positivity observation remains an unresolved historical-priority risk.

## Value (V): PASS

This closes a natural interval of scale parameters left outside the full larger-scale classification for the first cubic B-spline, precisely locates a sharp transition at \(4/7\), and rigorously excludes otherwise hidden complex-frequency zeros. The key two-variable exact positivity certificate is not a renaming, a single numerical example or an order increment by substitution.

## Limits

No claim is made for lower scales, other spline orders or Gabor frame sufficiency. The exact Bernstein certificate is necessary for the provided proof, and the larger-scale theorem is an acknowledged dependency. Literature priority is bounded, and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
