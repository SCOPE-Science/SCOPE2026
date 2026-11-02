# Scientific review: scale-stationary Parikh laws

## Correctness — PASS

The all-exponent assertion follows from two exact identities: a length-\(B^{e+1}\) factor starting at \(Bj+s\) differs from a balanced union of \(B^e\) substitution blocks by the difference of their two boundary prefixes; adding \(B^e\) to \(j\) changes its digit-sum residue by \(1+C_e(j)\). For each fixed carry length, one unrestricted digit above the carry supplies a rigorously uniform starting letter, and the tail has density at most \(B^{-K}\) after truncation at \(K\). Consequently the joint endpoint-letter distribution exists over *all* natural-density cutoffs and is independent of \(e\). Summing geometric carry classes gives the stated rational probabilities; the finite sum is normalized. The perfect-balance formula uses injectivity of every proper cyclic interval. The exact `fractions.Fraction` verifier checks formulas and independent substitution-generated finite prefix samples; finite sampling is not used to prove the limit.

Limits: no claim for \(m\nmid B\), arbitrary window lengths or uniform-in-scale empirical convergence.

## Originality — PASS, with residual bibliographic risk

The relevant full text of Chen–Wen (arXiv:1809.06554) determines the **set and count** of Parikh classes, not their frequencies. Popoli–Shallit–Stipulanti (arXiv:2410.02409, Theorems 22–23) determine the number of additive classes, including the ternary instance, but no distribution of starting positions among them. Golafshan–Rigo–Whiteland (arXiv:2412.18425, especially Sections 1–2 and 9) classify binomial equivalence and count Abelian Rauzy-graph vertices and edges, not mass distributions. Balková (arXiv:1107.5033, Section 4) describes frequencies of **individual full factors** and sets of distinct possible factor-frequency values. Its general algorithm could in principle compute aggregate class probabilities at a fixed length after extensive additional factor enumeration; the specific closed Parikh-vector formula, perfect-balance mass and all-scale equality are not stated there and do not follow from the reported sets alone. Actual published-record and related-research searches looked for aliases including digit-sum carries, abelian-class frequencies, substitution-scale Parikh measures and weighted-letter-sum distributions. No statement with the same implication was located. This is best-knowledge originality rather than a uniqueness guarantee; an unindexed equivalent remains possible.

## Mathematical value — PASS

Generalized Thue–Morse words provide a standard family where **support size** of abelian/additive factor statistics was studied. The new result resolves the more informative and natural question of how often each Parikh profile occurs when a window has substitution-scale length: a complete rational law valid simultaneously over unbounded lengths and all bases divisible by their alphabet size. Exact stationarity across these scales is a structural property, not a finite table. The probability of perfect balance and every weighted additive marginal become explicit, distinguishing rare and common factor classes that previous complexity counts treat identically. The divisible-base condition is forced by balanced substitution images rather than selected to manufacture an unrelated small example.

## Checked primary sources and uncertainty

- P. Popoli, J. Shallit, M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409, especially Definitions 1–3 and Theorems 21–23: class counts, not class probabilities.
- J. Chen, Z.-X. Wen, *On the abelian complexity of generalized Thue-Morse sequences*, arXiv:1809.06554, especially Theorem 1 and Lemmas 1–4: Parikh support/number, not measured distribution.
- Ľ. Balková, *Factor frequencies in generalized Thue-Morse words*, arXiv:1107.5033, Sections 2 and 4: individual-factor frequency algorithm and sets of frequency values; closest general-frequency source but no demonstrated implication of stationary aggregate Parikh law.
- M. Golafshan, M. Rigo, M. Whiteland, *Computing the k-binomial complexity of generalized Thue–Morse words*, arXiv:2412.18425, Sections 1–2 and 9: class equivalence and Rauzy-graph counts, not class frequencies.

Residual risk: an equivalent probability formula may exist in other indexed or unindexed literature; no claim of an independent external audit is made.

Self-review: passed. Independent audit: not yet performed.
