# Scientific review: sharp component-sensitive sorting-supersequence bounds

## Correctness — PASS

The width-two slot construction emits each element of one chain in every permissible gap among elements of the other chain. Prefix/suffix comparability proves that the permissible gaps form a contiguous interval, and selecting each element in its extension slot gives a subsequence embedding. Length counts one base copy of every element plus one additional copy per incomparable cross-chain pair. A ply-two interval graph is both triangle-free by interval Helly and chordal by the minimum-right-endpoint argument, hence a forest with \(n-c\) edges. The path family realizes the identity and all isolated adjacent swaps. Charging each swapped edge to a distinct nonidentity occurrence proves the matching lower bound for every component count. The supplementary checker exhaustively validates small endpoint orders and independently reproduces finite path minima. The proof does not infer an infinite conclusion from finite tests.

## Originality — PASS within examined sources

The closest primary article, Löffler and Raichel, arXiv:2601.19453v1 (2026), introduces exactly this notion of sorting-supersequence and gives asymptotic length bounds, including Theorem 6 for general bounded-ply intervals. Figure 2 exhibits a related connected ply-two example, so a large repeated-label effect is **not** claimed as new. The inspected text does not give the exact sharp extremal value \(2n-c\), the two-chain slot formula \(n+i(P)\), or a matching universal lower-bound charging argument. Radomirović, *Electronic Journal of Combinatorics* 19(4) P31 (2012), concerns words containing every unrestricted alphabet permutation, rather than constrained interval-order linear extensions. Targeted phrase, equivalence, and broader-construction searches and mathematical-record comparisons did not reveal a statement implying this result. This is a best-knowledge originality determination, not an exhaustive novelty certificate. Unindexed folklore on width-two posets and later work not covered by the search remain residual risks.

## Mathematical value — PASS

The object is a preprocessing supersequence for sorting uncertain points, introduced as a central object in the 2026 primary paper. The exact optimal worst-case length for the entire natural ply-two class is determined, including every possible number of overlap components; the lower-bound witness shows that the numerical constant cannot be reduced. The useful width-two order decomposition explains the construction and extends the upper bound beyond interval families. This resolves a quantitative extremal problem rather than merely substituting a parameter into a known universal-word bound. No claim about individual-instance optimality, the smoothness condition, or hidden-sorting computational complexity is made.

## Closest sources and limits

- Löffler and Raichel (2026), arXiv:2601.19453v1, Definitions 1–2, Figure 2, Theorems 5–6, and Section 3: general asymptotic bounds and an illustrative ply-two family, not the exact component-sensitive extremum.
- Radomirović (2012), DOI 10.37236/2859: unrestricted permutation supersequences, not this restricted extremum.
- Main limits: pairwise distinct endpoints; ply at most two; worst-case rather than every-instance shortest words; no general smoothness property; possible unindexed equivalent poset constructions. Independent validation remains unperformed.

Self-review: passed. Independent audit: not yet performed.
