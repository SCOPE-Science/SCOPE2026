# Scientific review: two logarithmic modal scales in order-\(k\) Poisson laws

## Correctness — PASS
The claim concerns the separate thresholds \(s_k\), at which the probability mass at zero loses modal dominance, and \(r_k\), at which masses at zero and \(k\) coincide. The proof establishes the exact generating-function coefficient, derives \(s_k\ge\log(k+1)/k\) by conditioning on a uniform-jump compound Poisson representation, and shows \(s_k\le(1+\epsilon)\log k/k\) eventually for each \(\epsilon>0\) by Chebyshev concentration and an atom-counting argument. These arguments preserve the limit order and all quantifiers.

For \(r_k\), the exact coefficient polynomial is compared termwise with \(F(u)=\sqrt u I_1(2\sqrt u)\); the product inequality has the all-parameter bound \(0\le F(u)-kQ_k(u/k)\le uF(u)/(2k)\). The standard Bessel large-argument expansion then yields the asserted second-order relation. Root uniqueness and strict decrease follow directly from positive coefficients. The finite rational coefficient comparison at order 15 and the verifier's independent algebraic constructions corroborate, rather than prove, the asymptotic claims. A separate independent proof audit is not claimed.

## Originality — PASS (self-review)
The full text of Georghiou–Philippou–Saghafi (2013) gives mode bounds and the recurrence; Philippou (2014) gives a sufficient threshold of order \(k^{-2}\); Kwon–Philippou (2023) defines \(r_k\), proves its existence, and asks for the decay rate. Mane's two September 2023 preprints treat exactly the first double mode and provide the order-15 example, a monotonicity result, and *numerical* extrapolations. Their numerical power-law fit does not mathematically cover—and is asymptotically incompatible with—the proved \((\log k)/k\) law. Mane's October 2023 analytical note addresses other coefficient and mode inequalities. None of these materially inspected arguments implies the two proved logarithmic scales or the second-order crossover formula.

Searches also covered the aliases “Poisson distribution of order \(k\),” “stuttering Poisson,” “compound Poisson with uniform jumps,” “first double mode,” zero-mode thresholds, and Bessel crossover formulas. A search without a hit alone is not novelty evidence; the substantive support is the statement-level comparison of the inspected papers. There remains residual bibliographic risk from uninspected older or later mathematical work, and no independent priority determination is represented.

## Value — PASS
This theorem resolves the asymptotic scale of the first zero-mode loss in a natural count family and sharply separates it from a distinct zero-versus-\(k\) crossing that the primary literature had used as a candidate transition. The latter has a precise second-order logarithmic correction. As a consequence, the first modal transition eventually cannot occur at index \(k\), and a previously published finite-range numerical power-law interpretation does not describe the true large-order limit. This is a substantive global classification of two motivated thresholds, not a routine finite check, a renamed identity, or a new claim for an already-known order-15 example.

## Closest sources and scientific limitations
Kwon and Philippou, *Entropy* 25 (2023), 699, DOI 10.3390/e25040699; S. R. Mane, arXiv:2309.05190 and arXiv:2309.09278 (2023); A. N. Philippou, *Fibonacci Quarterly* 52 (2014), 203–205. Exact values of the first zero-mode threshold and the first positive modal location at arbitrary finite orders remain unclassified; the asymptotic statement does not yield an effective uniform cutoff without additional estimates.

Self-review: passed. Independent audit: not yet performed.
