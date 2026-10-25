# Scientific review

## Correctness — PASS

The included standalone Python certificate explicitly enumerates every matching of the five specified rectangular grids, creates disjoint incident face pairs from literal edge-index permutations, orients every Hasse cover, and independently topologically sorts the complete oriented graph to verify acyclicity. The critical-face vector is exactly one critical vertex and \((5,9,16,31,55)\) critical cells in dimensions \((2,3,4,5,6)\) respectively; the empty-pair removal argument produces a legal ordinary face-poset matching. The resulting CW models are unequivocally wedges of spheres integrally. The largest run checks all 196785 faces and 1239360 covers, not a subsample. This proof is finite and does not extend to unknown widths.

## Originality — PASS, with documented residual risk

The 2021 article already *asserted* precisely the five numerical sphere-wedge answers in its Table 1, but retracted its main theorem and recurrence following a 2025 corrigendum. Accordingly, neither their dimensions nor multiplicities are claimed as new. The distinct theorem proved here is that each of these complexes admits an **explicit perfect discrete-Morse matching on the entire face poset**. Mere knowledge of a homotopy equivalence does not entail a perfect *simplicial* Morse matching. The original paper used deletion/link and suspensions, not the exhibited complete acyclic matching. The later 2026 preprint's accessible abstract states connectivity/homology rather than a perfect Morse matching. Closest public records include the matching complex of a four-by-four grid, which concerns a different complex. Full text of the current 2026 preprint was not obtainable for final comparison, leaving a documented risk of overlooked similar certificates.

## Mathematical value — PASS

This is a finite but motivated constructive result for a conjectural problem whose earlier general proof was formally retracted. Producing perfect Morse witnesses, particularly the seven-column case with 196785 faces and over one million Hasse covers, gives a reproducible integral homotopy proof independent of the abandoned non-induced-subgraph arguments. Five consecutive widths provide a natural, not arbitrarily selected, computational cutoff. The proof neither assumes the retracted formula nor misrepresents previously stated homotopy numbers as novel.

## Closest literature and limits

The 2021 retracted Table 1 is the closest numerical overlap; the 2026 paper's homology/connectivity statement is the closest current motivation; the 2019 two-row result is structurally adjacent but does not cover these graphs. No claim is made for larger widths; no external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
