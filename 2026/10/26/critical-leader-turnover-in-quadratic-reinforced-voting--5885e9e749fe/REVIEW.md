# Research review: critical leader turnover in quadratic reinforced voting

## Correctness — PASS
The proof reconstructs the full first-round occupancy law and its concentration from factorial moments; bounds the number of top and runner-up boxes uniformly in the factorial phase; controls the selected multinomial cells by independent Poisson approximation; and separates their maxima using complementary Poisson upper and lower moderate-deviation bounds. In particular the logarithmic threshold compensates for arbitrary ties and all \(n\), not just subsequences. Exact finite verification is supplementary, not the asymptotic proof. The eventual-winner corollary imports the specific published second-round containment conclusion, instead of asserting a new proof of that conclusion.

## Originality — PASS
The primary paper [1, Definition 1.1, Theorem 1.6, §1.3] covers the named model and off-critical winner identification, but specifically leaves first-round winner noncontainment at quadratic reinforcement conjectural while stating second-round winner containment. Strict disjointness of first- and second-round leader sets is stronger, and not implied by the published statement alone. Model/alias/extreme-value searches and research-record comparisons found no exact covering claim. Earlier work on reweighted occupancy extremes could still overlap, especially under a different name.

## Mathematical value — PASS
This is a natural boundary problem with a published motivation: the exact first critical exponent. Its resolution uses a generalizable mechanism, namely that a growing class of one-vote-behind competitors overcomes a slight conditional expected-count disadvantage after multinomial resampling. The proof quantifies why first-round maximum identity fails where a merely single-leader comparison would miss the effect.

## Scope and limitations
Only quadratic reinforcement in the equal-population n-candidate chain is proved, and only in the infinite-population limit. No effective finite-size threshold, uniqueness of round-two leaders, other critical powers or neighboring reinforcement exponents is established. The exact prior source discussed in [1] is arXiv:2607.22324; broader works [2] and [3] were checked at abstract level only, with no claim of whole-document noncoverage. Independent external validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
