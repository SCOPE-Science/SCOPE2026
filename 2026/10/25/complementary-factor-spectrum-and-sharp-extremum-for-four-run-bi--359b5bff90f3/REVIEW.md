# Scientific review

## Correctness — PASS

For exactly four positive alternating runs, the mutually exclusive one-/two-/three-/four-run factor classification proves the complete coefficientwise polynomial, including the indicator \(b=c\). Rectangle inclusion-exclusion gives the closed expression. For \(b=c\), an explicit deficit identity proves the sharp upper bound and precisely characterizes its equality. For \(b\ne c\), two exhaustive cases bound the half-count by \(n^2/8\), strictly below the attainable maximum for \(n\ge6\); the small lengths are checked separately. The standalone direct-factor verifier checks 2,401 spectra and all positive compositions through length 64. Finite checks do not replace these unlimited proofs. Risk: implementation could share a conceptual convention, mitigated by separately implemented literal factor enumeration.

## Originality — PASS, residual risk acknowledged

The nearest primary source is Currie et al., *Complement Avoidance in Binary Words*, arXiv:2209.09598, first public September 20, 2022 (journal publication October 2025). Its full accessible HTML text was checked at the definitions, infinite-word complementary-factor classes, critical-exponent theorems and finite-word complexity sections. The count here is for every four-run finite word and the exact fixed-length maximum and equality classification; these are not implied by the inspected infinite-word threshold statements. Sawada–Stevens–Williams (WALCOM 2011) studies complement-free de Bruijn cycles, not maximizing simultaneous complemented factors in linear four-run words. Searches were performed for factor-count aliases and extremal equivalent formulations. The absence of a matching database hit is not proof of global novelty; unindexed specializations remain a risk.

## Mathematical value — PASS

The source literature measures how many factors coexist with their complements to distinguish avoidance regimes. Restricting to four runs gives a natural first nontrivial family with all orientations of complementary one-/two-/three-run factors, and a discrete resonance phenomenon: complementary three-run factors exist only when the two interior runs are exactly equal. This resonance forces all length-extremizers and gives a linear-order gap between the optimal count and every unequal-interior-run word. The result solves the full four-parameter spectrum and complete sharp extremum; it is not a small numerical increment or arbitrary slice.

## Limitations and sources

The theorem is not a claim about five-run or arbitrary binary words. It counts distinct strings, not embeddings, and has no independent validation. Most relevant accessible source: Currie et al., arXiv:2209.09598v2 (primary full HTML). Additional background: Sawada, Stevens and Williams (2011), complement-free de Bruijn cycles. The closest background concerns a distinct object or weaker/different quantifiers. A possible hidden equivalent special case remains open to expert verification.

Self-review: passed. Independent audit: not yet performed.
