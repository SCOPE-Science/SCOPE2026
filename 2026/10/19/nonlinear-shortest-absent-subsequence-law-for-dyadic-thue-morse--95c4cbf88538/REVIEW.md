# Self-review

## Correctness — PASS
The alignment lemma is established in both directions for arbitrary concatenations of complementary binary pairs. The resulting two allowed-transition matrices count every absent length-\(k+1\) binary subsequence exactly once. The Thue–Morse substitution gives a renormalized unimodular matrix product; its characteristic equation yields the stated integer recurrence with checked initial values. The logarithmic recurrence is contractive after normalization and gives the exact absolutely convergent series for the asymptotic base. The standalone verifier separately generates both representations of Thue–Morse words and checks direct absence, finite-state counting, matrix counting, and scalar recurrence on the documented bounded ranges. No finite search is used as a proof of the infinite formula.

## Originality — PASS, subject to residual literature risk
The 2013 binomial-equivalence study of Thue–Morse concerns subsequence multiplicities inside factors rather than shortest absent scattered subsequences of dyadic prefixes. Kosche–Koß–Manea–Siemer establish general shortest-absent-subsequence and arch-gluing theory, not this substitution-specific evaluation. A publicly available result on Fibonacci extremal counts evaluates a maximizing sequence of binary arch matrices; its complete mathematical statement has been compared to the present exact nonperiodic Thue–Morse product. It does not imply the explicit nonlinear recurrence or asymptotic base without additional analysis. Targeted searches for equivalent dyadic-block counts, arch-matrix products and automatic-sequence formulations found no equivalent theorem. Unindexed prior matrix identities remain a risk.

## Mathematical value — PASS
The dyadic blocks of the canonical Thue–Morse automatic word provide a natural parameter family for the shortest-absent-subsequence statistic. The result supplies an exact, infinite, non-Fibonacci nonlinear integer profile and a computable limiting exponential rate strictly smaller than the total binary candidate rate. The substitution renormalization is structural, explaining rather than merely enumerating the counts. Its scope does not require a downstream theorem or arbitrary large computed cutoff.

## Limits
The result addresses finite dyadic prefixes, not every prefix. The full generic subsequence transfer is prior work. The exact-index novelty assessment cannot exclude earlier unindexed or differently named automatic-matrix-product results.

Self-review: passed. Independent audit: not yet performed.
