# Scientific review

## Correctness — PASS

The morphism recurrences identify the \(1\)-positions with positive indices of odd \(2\)-adic valuation. The alternating floor formula converts each factor-prefix difference to an alternating binary-carry sum. Pairing carries bounds the excess by the number of set odd-position bits of the total endpoint, and their least possible total is the explicit geometric threshold. Equal summands realize every threshold, and the equality conditions force the unique first witness. Direct exhaustive checks through length \(4096\) are reproducible with `checker.py` and are not substituted for the general proof. No assumptions about arbitrary other morphic words are used.

## Originality — PASS, with residual historical risk

The closest framework is Fici–Lipták's prefix-normal factor-count invariant (2011); their examined paper gives the general concept and algorithms but no all-prefix exact threshold for the period-doubling word. Parreau–Rigo–Rowland–Vandomme (2014) analyze Abelian complexity of the infinite period-doubling language, rather than the location-restricted prefix excess and unique first attainment. Cicalese–Lipták–Rossi (2018) treat infinite prefix-normal forms and related examples but do not state this theorem in their accessible full text. A closely related research record proves *unbounded* prefix-normal defect for the distinct ordinary paperfolding word; it neither implies an exact bound for period doubling nor describes its carry rigidity. Published-record searches were negative for an equivalent theorem, but no search proves universal novelty.

## Value — PASS

The sharp step function identifies exactly how long an initial automatic-word prefix must be before any length admits a prescribed deficit from prefix normality. It resolves all \(N\), not only a handful of iterates, and gives unique first-attainment witnesses. This quantifies the failure of prefix-normality for a classical automatic word and gives a transparent binary-carry explanation for the threshold sequence, directly connected to jumbled indexing and prefix-normal forms.

## Scope and remaining risks

Only one infinite word and its initial finite prefixes are covered; no full lengthwise profile is claimed. An unidentified equivalent older argument cannot be ruled out. Finite checker tests are supporting evidence rather than an infinite certificate. No independent mathematical assessment has occurred.

Self-review: passed. Independent audit: not yet performed.
