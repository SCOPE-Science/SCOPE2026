# Review: Boolean Hamming radius-two ball dimensions

## Correctness

**PASS.** The statement concerns closed metric radius-two balls, not exact-distance spheres. The all-dimensional VC upper bound reduces every hypothetical five-query shattered set to one of 7,260 finite coordinate-incidence types. Exhaustively computing all nonzero traces in both independent implementations gives a maximum of 26, strictly below the necessary 31. Four-query witnesses provide the matching lower bound for every dimension from five onward. The all-dimensional adaptive upper bound uses explicit branch reductions through center supports of size at most two, then star- or singleton-supported branches. This is a structural proof, not a finite-experiment extrapolation. A complete 31-query, 32-distinct-witness depth-five tree gives the matching lower bound from dimension six. Direct version-space dynamic programming confirms the stated smaller dimensions. The certificate and source-code checks were replayed locally before review.

## Originality

**PASS with stated historical-priority risk.** The closest inspected prior full text is Adler, Benediktsson and Macpherson (arXiv:2007.16042), Sections 1 and 4. Its central relation is open adjacency in Hamming graphs (distance exactly one); its closed-neighborhood remark concerns radius one, not the square graph and closed radius two. Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805), Theorem 3.10, concerns zero sets of linear combinations, a family whose dimension-equality theorem does not cover the present metric-ball family (where the two dimensions differ). Ghazi et al. (PMLR 132, 2021), abstract, gives general closure estimates rather than exact constants for these hypotheses. Public research-record searches for Hamming balls, hypercube-square graph neighborhoods, exact-radius versus closed-radius semantics, and VC/Littlestone terminology found no logically stronger covering claim. The closest records concern Turán positive-definite mass of Hamming balls, not shattering. A previously recorded result about exact-distance-two shells is a different class and neither implies nor includes this finding. Exact synonyms and older literature may be unindexed.

## Mathematical value

**PASS.** Fixed-radius Hamming neighborhoods are natural translation-invariant range spaces for coding, graph learning and model-theoretic shattering. An exact all-dimensional classification reveals a sharp, stable strict gap: the VC dimension stabilizes at four but adaptive Littlestone dimension at five, first at six binary coordinates. The finite obstruction gives a reusable coordinate-incidence argument; the adaptive upper bound isolates a nontrivial star-reduction mechanism. The result is not a routine cardinality-bound calculation or a restatement of a distance-two shell invariant.

## Scope and risks

The finite normal-form obstruction is exhaustively checked, with independent Python and C++17 implementations. The adaptive upper bound depends on the explicitly listed exceptional-query case analysis. Potential priority overlap under terms such as closed neighborhoods in square powers of Hamming graphs or fixed-radius range-space dimensions remains. No nonbinary or other-radius theorem is claimed.

Self-review: passed. Independent audit: not yet performed.
