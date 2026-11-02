# Scientific review: nine rigid shortest absent subsequences

## Correctness (PASS)

The central two-set induction for the template `101(000101)^(r-1)` is reconstructed through first-occurrence residual suffixes. Its base at four ones and the six offset transitions yield the precise missing strings and shortest lengths. Embedding the template into any admissible gap-inflated word proves all noncandidate strings of the critical length are present, while the unit leading/trailing gaps give a one-unit shortage of available ones for each of the nine candidates. The Cantor gap calculation follows by carrying binary digits in their ternary image. The standalone checker independently recomputes actual SAS sets and exhaustive small cases. No finite test substitutes for the proof.

## Originality (PASS, qualified)

Closest literature includes the general framework of bounded scattered-subword spectra (Karandikar–Kufleitner–Schnoebelen, arXiv:1310.1278), shortest absent subsequence algorithms and monotonicity under subsequence containment (Kosche–Koß–Manea–Siemer, arXiv:2108.13968, Theorem 3.5, Lemma 3.20), and nearly universal words (Fleischmann et al., arXiv:2202.07981, Section 4). The full accessible text of these sources was compared at the relevant sections. Their general principles do not state or immediately identify the rigid nine-element Cartesian-product spectrum for all Cantor levels, nor the broader zero-gap-inflation family. Targeted published research-record searches returned general universality and extremal short-absence results but no covering special-family theorem. Risk remains that an earlier equivalent formulation outside the checked sources exists, and the 2020 universality paper was available only at abstract depth.

## Value (PASS)

The result gives the *exact identities* of all first missing deletion patterns at arbitrarily long fractal substitution iterates, not just their length or number. Its robust general-family theorem explains why enormous three-adic internal gaps do not alter the first forbidden subsequence spectrum. This is useful as a structural classification and exact benchmark for subsequence-based comparison, negative-pattern detection, and Simon-congruence spectra. It is not merely a numerical census or a textbook restatement of universality.

## Scientific limits

The theorem does not classify all minimal absent subsequences, non-complete Cantor prefixes, or occurrence multiplicities. Independent review and historical-priority certification are outstanding.

Self-review: passed. Independent audit: not yet performed.
