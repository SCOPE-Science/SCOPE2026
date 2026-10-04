# Same-model review

## Correctness
PASS. The claim is finite and exhaustively checkable. The census covers every ordered pair of five-state binary transition maps, a domain of \((5^5)^2=9,765,625\) automata. Power-set BFS on all \(32\) state subsets computes exact shortest avoidance distances, not heuristic bounds. The census finds exactly \(960\) threshold-eight extremals. Independent replay reconstructs all four symmetry orbits, verifies that each has size \(240\), checks disjointness and total size \(960\), and validates the listed shortest witness words and distance vectors. The packaged verifier recompiles the census and requires exact output reproduction.

## Originality
PASS, with a residual access risk. Ferens–Szykuła–Vorel explicitly state that their five-state exceptional example \(\mathcal A_5\) has threshold \(8\), so neither that value nor that example is claimed as new. Their inspected paper describes isolated \(2n-2\) examples and reports small-state experiments, but it does not state an exact count of five-state binary extremals or a symmetry-complete classification. Targeted published-finding corpus searches for exact five-state avoiding-threshold counts and classes returned no statement equivalent to the \(960\)-element/four-orbit claim. The residual risk is that an unindexed or unpublished experimental dataset contains the same classification.

## Value
PASS. The finite layer is mathematically motivated by the published conjecture that \(2n-2\) occurs only in finitely many exceptional cases. The five-state case is a natural exceptional layer because the published \(\mathcal A_5\) already attains \(2n-2=8\). Showing that all extremals comprise four distinct symmetry types, rather than a single known example, resolves the exact structure of this smallest named five-state exceptional layer.

## Closest literature and limitations
The closest sources are Szykuła's avoiding-word upper-bound paper and Ferens–Szykuła–Vorel's lower-bound/exception paper. The present result is intentionally narrower than their general questions: it is an exact finite classification for five-state binary automata. It does not imply that \(2n-2\) is a universal bound, nor does it classify larger exceptional sizes.

Same-model review: passed. Independent audit: not yet performed.
