# Review of the binary block-retrieval monotonicity obstruction

## Correctness (C): PASS

The four-column code has exact expectations \(E_1=2\) and \(E_2=6\). The proof treats all five-column binary rank-three matrices by the number \(m\in\{0,1,2,3\}\) of columns equal to the first file's basis vector. For \(m=0\) repeated first two draws certify \(E_1\ge11/5\); for \(m=1\) the at-most-four complementary-pair bound gives \(E_1\ge53/25\). For \(m=2\), the rank condition limits complementary pairs, and the three exact alternatives give \(E_1\in\{25/12,9/4,5/2\}\). For \(m=3\), the rank condition forces \(E_1=5/3\) and requires two separate rare columns to recover the two-dimensional file, so \(E_2\ge15/2\). The arguments allow repeated and zero columns. Two independent exact rational recurrences agree for all 476 rank-three five-column binary multisets, validating the finite certificate without replacing the written proof.

## Originality (O): PASS

Bar-Lev's 2026 paper states the one-step monotonicity conjecture for two files when at least one dimension exceeds one; it exhibits a counterexample only for two one-dimensional files. Lifting that example to a larger file is not a logical proof because new mixed-column codes might dominate it. The new five-column dichotomy excludes precisely that possibility in the smallest nontrivial binary dimension. The inspected 2026 one-mixed-column paper and the later hyperbolic-bound preprint concern a different inequality \(\dim(F_1)/E_1+\dim(F_2)/E_2\le1\), which neither entails nor contradicts monotonicity of attainable pairs across block lengths. Queries against indexed research records, this paper, and related literature found no equivalent fixed-field counterexample. Priority risk remains from unindexed work and the uninspected full text of a separate hyperbolic-bound preprint.

## Value (V): PASS

This answers an explicitly posed structural conjecture, not an arbitrary small numerical search. The result identifies why one extra encoded symbol cannot always weakly improve both file-retrieval times despite increasing one file dimension: short-block sampling granularity and rank constraints produce a sharp obstruction. The proof also gives a complete characterization of the only five-column regime with \(E_1\le2\). It changes the appropriate formulation of possible monotonicity theorems, while leaving the universal hyperbolic conjecture separate and open.

## Scope and risk

The result covers exactly binary rank-three linear coding, file dimensions one and two, and the step from four to five uniform-with-replacement sampled coordinates. It does not establish counterexamples for every code length or larger alphabet and does not claim general channel-capacity improvements. Earliest public source date was verified from the primary arXiv submission history. Independent audit and exhaustive publication-priority confirmation have not been performed.

Self-review: passed. Independent audit: not yet performed.
