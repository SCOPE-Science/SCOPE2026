# Self-review

## Correctness — PASS

The claim specifies the open-neighborhood, fully proper version of conflict-free coloring and includes the isolated singleton. For each nonisolated cell, all neighbor-color multiplicities are the sum of two zero-one row/column indicators; the proof gives a necessary and sufficient row-versus-column palette inequality. Nonsquare palette cardinality automatically implies the inequality. In the square case, every \((n+1)\)-palette coloring has equal numbers of rows and columns omitting any given color; at least one color is omitted, so the same color is omitted by a row and a column, producing an invalid cell. The \((n+2)\)-palette modular construction has distinct cyclic gaps in omitted pairs for all \(n\ge2\), so no row-color set equals a column-color set. Both bounds are tight. A separately written brute-force verifier checked 91 constructions and 156,563 complete enumerated proper color arrays in 16 selected cases without disagreement. Finite tests are supplementary, not a substitute for the proof.

## Originality — PASS, with residual bibliographic uncertainty

The latest motivating source, Pradhan–Sharma (arXiv:2608.10874, 2026-08-11), reports complexity, approximability and algorithms for several graph classes; its accessible abstract does not state a rook-graph exact formula. Its full text was not accessible and was **not** classified as noncovering. Caro–Petruševski–Škrekovski (arXiv:2203.01088, inspected full paper) determines PCF numbers for trees, cycles, hypercubes and complete-graph subdivisions; its cycle result includes the \(2\)-by-\(2\) case and is acknowledged. Jiménez et al. (arXiv:2308.00170, full paper inspected) give general PCF bounds for quasi-line graphs but do not establish the rook-square two-color gap or its all-coloring criterion. The 2026 IWOCA article on improved bounds could only be checked at abstract level. Searches for the equivalent line-graph and proper edge-coloring formulations and indexed exact PCF results yielded no stronger claim implying this result. Absence in these searches is not a uniqueness proof; residual priority risk remains.

## Mathematical value — PASS

The result yields a sharp arithmetic change at the equality of the two clique-system sizes and a strict two-color separation from ordinary chromatic number for all square dimensions. The structural criterion determines precisely which *individual* proper colorings are PCF, while the formula decides the invariant across an infinite family also recognized as line graphs of complete bipartite graphs. The proof identifies a nontrivial obstruction (synchronized missing colors at palette size \(n+1\)) and an explicit matching construction at \(n+2\); general quasi-line bounds alone do not determine these values. This is an exact structural classification motivated by a recent graph-coloring invariant, not an unmotivated computation or an improvement of one fixed tiny example.

## Limits

Independent external mathematical validation and definitive publication priority are not established. The inaccessible full texts remain a material search risk. The finite checker cannot prove the unrestricted theorem.

Self-review: passed. Independent audit: not yet performed.
