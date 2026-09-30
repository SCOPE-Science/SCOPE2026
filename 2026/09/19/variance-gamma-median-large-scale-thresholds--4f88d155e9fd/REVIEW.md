# Review

**Independent audit on 2026-09-29 UTC: correctness passed; provenance/originality repaired.**

## Correctness

The five asymptotic regimes are correct. The zero-CDF imbalance from the symmetric beta representation is of order \(\kappa^{-1/2}\), and the small-argument branches of the Bessel-\(K\) density produce the power, logarithmic, fractional, resonant, and smooth corrections at \(r<1\), \(r=1\), \(1<r<3\), \(r=3\), and \(r>3\). The constants agree algebraically with the earlier SCOPE theorem; in particular the \(r=2\) coefficient is \(1/2\), matching the exact asymmetric-Laplace formula. The Wishart formulas follow by direct substitution into the variance-gamma marginal law.

## Originality and provenance correction

The original standalone novelty claim for the five-regime theorem is withdrawn. The same theorem, including both critical thresholds and the same constants, already appears in
`2026/09/18/variance-gamma-median-large-noise-phase-transitions--2d5865f4207e`,
first committed at 2026-09-18T17:10:12Z. The present record was first committed at 2026-09-19T04:05:38Z.

The retained role is an alternate derivation and a Wishart small-correlation corollary package. Any priority claim for the underlying five-regime variance-gamma asymptotics belongs to the earlier repository record.

## Scientific value

Useful as corroboration and as a direct statistical specialization: the \(r=3\) resonance becomes the \(n=3\) Wishart off-diagonal median transition. The value is incremental relative to the earlier SCOPE theorem.

## Literature access and limitations

The Kotz--Kozubowski--Podgórski monograph was not available through open-access routes. Authorized Oxford retrieval was queued and later timed out; the book is not claimed as read. This does not affect the internal provenance repair. The expansions are not uniform as \(r\) approaches 1 or 3 and no nonasymptotic remainder is proved.
