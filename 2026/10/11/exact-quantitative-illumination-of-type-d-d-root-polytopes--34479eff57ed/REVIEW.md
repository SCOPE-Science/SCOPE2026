# Scientific review: exact quantitative illumination of type-\(D_d\) root polytopes

## Correctness — PASS
For every integer \(d\ge3\), the claimed root polytope has the exact halfspace description \(\|x\|_\infty\le1\) and \(\|x\|_1\le2\). The active-facet illumination inequalities reduce any source's illuminated vertices to a pairwise-intersecting family of coordinate pairs, hence a star or a triangle. Summing these inequalities proves that a source illuminating \(k\) vertices has gauge strictly greater than \(k\). Covering all vertices gives the lower bound, while near-vertex exterior sources approach the same infimum and illuminate all boundary faces. The finite exact-rational verifier returned `EXACT_DIAGNOSTIC_OK cases=137200 illuminated_pairs=68296 max_single_source_count=3`; it only cross-checks the analytic proof.

## Originality — PASS
The 2012 initiating primary text gives the cuboctahedron value \(12\) only as an **upper bound**, and the authors explicitly withhold exact Archimedean values. Bezdek–Khan's 2016 Section 4.1 covers the invariant's general setting without the dimension-free exact family. A materially read published result on the cube–octahedron intersection gives the **ordinary** illumination number \(4\), which does not determine the quantitative weighted source sum. Searches for the root-system, cuboctahedral and 24-cell aliases found no matching lower-bound implication. A plausible 2006 successive-illumination paper was available only in abstract, so an unindexed older equivalent remains an explicit originality risk; novelty has not been independently certified.

## Value — PASS
The exact equality \(\mathcal I(P_d)=2d(d-1)\) solves a previously only upper-bounded natural Archimedean example, provides the exact \(24\)-cell value, and explains the entire type-\(D_d\) family via a nontrivial illuminated-edge intersection argument. It is a meaningful all-dimensional structural classification, not a small incidental numerical improvement.

## Closest literature and limits
G. Kiss and P. O. de Wet (2012), DOI 10.55016/ojs/cdm.v7i1.62108, Table in Theorem 3.4; K. Bezdek and M. A. Khan (2016), arXiv:1602.06040, Section 4.1; K. Bezdek, K. Böröczky and G. Kiss (2006), DOI 10.1007/s10998-006-0022-3, accessible abstract only. The theorem does not settle a universal three-dimensional conjecture. Its sharp parameter is an infimum, not a minimum over finite sources. Independent review has not been performed.

Same-model review: passed. Independent audit: not yet performed.
