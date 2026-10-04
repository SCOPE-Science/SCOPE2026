# Review
## Correctness
**PASS.** The claim has one exact object: the maximum insertion distance from a full-support length-\(n\) word to the language of \(k\)-subsequence-universal words over the same \(q\)-letter alphabet. The proof establishes the exact partition identity \(I_k(w)=qk-C_k(w)\), proves \(C_k(w)\ge\min\{n,q+k-1\}\) by a repeated-symbol refinement argument, and shows equality for \(a_0^{\,n-q+1}a_1\cdots a_{q-1}\). Quantifiers and boundary cases are explicit: \(q\ge2\), \(n\ge q\), and \(k\ge1\). The verifier independently agrees with the literal definition on small cases and exhaustively checks the claimed extremum on larger finite grids; the infinite conclusion rests on the proof, not the computation.

## Originality
**PASS with residual risk.** The closest inspected source is *The Edit Distance to k-Subsequence Universality* (arXiv:2007.09192; DOI:10.4230/LIPIcs.STACS.2021.25). Its insertion section gives a per-input dynamic program based on the number of missing symbols in segments. The inspected material does not state the extremal full-support radius, the phase transition at \(n=q+k-1\), or the heavy-symbol extremizer. Exact-formula, alias, covering-radius, and broader subsequence-universality searches did not identify a statement implying the theorem. A later journal record, DOI:10.1016/j.jcss.2025.103681, is the same line of work rather than independent prior coverage. An unindexed or differently phrased derivation remains a residual risk.

## Value
**PASS.** The result turns the known per-word insertion-distance problem into a sharp global invariant of the fixed-length full-support layer. The exact formula separates two mathematically distinct obstructions and supplies an extremal construction for every alphabet size, length, and target universality level. This is an all-parameter structural result rather than an arbitrary finite slice.

## Closest literature and limitations
The result concerns insertions only. It does not classify all maximizing words, does not cover words missing ambient alphabet symbols, and does not assert analogous formulas for deletion or substitution distance. The finite verifier is corroborative only. Literature search cannot exclude inaccessible or unindexed prior work.

Same-model review: passed. Independent audit: not yet performed.
