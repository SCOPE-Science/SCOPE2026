# Review: exact minimum binary two-attractors

## Correctness — PASS

The proof works for every nonempty indexed binary word. A one-position attractor cannot cover both letter types, and a two-position attractor for a word containing all four digrams must match the four digram types into two pairs of adjacent factors. Exactly two such matchings exist. The absence of both matching witnesses yields two, and only two, explicitly parameterized alternating-interior families; each has a constructive three-position attractor. An independent incidence-mask program exhausted all 65,534 nonempty binary words of lengths at most fifteen and checked the fixed-weight totals, with the all-length derivation supplied separately from computation.

## Originality — PASS (qualified)

The closest primary literature is Kempa, Policriti, Prezza and Rotenberg (2018, arXiv:1803.01695) on the general \(k\)-attractor and sharp-two algorithms; Fuchs and Whittington (2023, arXiv:2304.06523) on ordinary two-attractor NP-completeness for unrestricted alphabets; and Mantaci et al. (2021) on full attractors and specific infinite word families. None of the inspected results states or dominates the full binary cutoff-two classification plus bivariate count. The general algorithms do not themselves supply the structural classification. Targeted exact-formula and published-record searches identified no equivalent. Unindexed equivalent work remains a real priority risk, not a proven absence.

## Mathematical value — PASS

The boundary between a general NP-complete covering problem and the fixed binary alphabet is mathematically natural. A complete structural solution is more informative than per-instance optimization: it shows the minimum is always at most three, identifies precisely the words for which two positions fail, gives the rational weight-enumerator and establishes exponentially rare exceptional behavior. The composition-refined result supplies finer information than a length-only table.

## Limitations

Only linear, non-sharp two-attractors of finite binary words are classified; circular, larger-alphabet, and higher-cutoff problems are not addressed. The proof, rather than the finite checker, carries the universal quantifiers. A future independent priority review is needed.

Self-review: passed. Independent audit: not yet performed.
