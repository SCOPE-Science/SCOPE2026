# Review

## Correctness
PASS. The proof separates the petal-count argument from the finite enumeration. From nine petals to one, any path has \(d-a=4\), so its length is \(2a+4+p\). Published hardness forces \(a\ge 1\); a path shorter than eight moves would therefore have one addition, five deletions, and at most one preserving move. The verifier searches a strict relaxation in which \(\mathsf R\) and \(\mathsf S\) are free and still finds no such path. Both published eight-move paths are replayed successfully.

## Originality
PASS. The closest source proves hardness and exact excess, not exact move distance. Its Section 5 search is parameterized by maximum petal count, and Section 6.1 presents the sequences as upper bounds for excess. Targeted literature searches for shortest petal-move distance, geodesic untangling sequences, and minimum numbers of petal moves returned no covering result. The earlier Reidemeister-type theorem establishes connectivity but not quantitative shortest paths. The remaining risk is that unreported ancillary computations could contain path-length information not stated in the article; no such claim appears in the inspected article, tables, or described outputs.

## Value
PASS. Move count is a natural second complexity coordinate for hard diagrams, distinct from the maximum intermediate petal count measured by excess. The two words are canonical representatives of the smallest known hard petal unknots, so proving that their displayed untanglings are geodesic gives an exact baseline for quantitative petal-move complexity rather than an arbitrary finite slice.

## Closest literature and limitations
Vernitski, arXiv:2610.01596v1, supplies the hard words, exact excess values, and eight-step upper paths. Colton--Glover--Hughes--Sandberg, arXiv:1812.08930, supplies the petal move calculus and completeness theorem. The claim does not extend to \(\gamma\) or to every hard word.

Same-model review: passed. Independent audit: not yet performed.
