# Independent mathematical audit — SCOPE-20260914-039

Disposition: **passed**.

## Correctness
**PASS** — I independently checked that the displayed 22 triples are linear, have degree sequence twelve 5s and one 6, and contain no six-edge loose path by enumerating all 6-edge subsets and testing the intersection graph/13-vertex condition. A separate fresh enumeration rebuilt the punctured cyclic STS(13) pair, found exactly 144 linearly addable cross triples, and verified that each creates a P6. The n=9,10,11,12 witnesses are linear; the stated packing bounds prove n=9,10,12 optimal, and the n=11 degree/pair-deficit argument rules out 18 edges.

## Originality
**PASS** — The inspected linear-path Turan literature does not cover this explicit k=3, P6 linear-host witness or imply density 22/13. The principal exact theorem of Furedi-Jiang-Seiver is for uniformity at least 4, while the recent linear 3-graph paper located concerns P5.

### Equivalent formulations
The construction is equivalently a 22-block partial triple system on 13 points whose block-intersection structure avoids a loose 6-path; no matching prior construction was found.

### Broader coverage
Neither broader result mechanically implies this k=3 P6-free 13-vertex density witness.

### Exact database or table
The record does not claim ex(13)=22; it only needs existence, so absence of an exact table is supplementary.

### Claim versus prior implication
The density refutation follows directly from the independently verified witness and is not a corollary of those prior theorems.

### Source inspections
- **Exact solution of the hypergraph Turan problem for k-uniform linear paths** (https://arxiv.org/abs/1108.1247): does not cover k=3. Stated exact result is for k-uniform linear paths with k>=4.
- **The linear Turan number of the 3-graph P5** (https://arxiv.org/abs/2601.19068): different forbidden path. Concerns P5 rather than P6.

## Scientific value
**PASS** — The 22-edge witness improves the density from 5/3 to 22/13 and therefore invalidates a concrete proposed extremal block picture. That is a meaningful structural counterexample, and the auxiliary rigidity/small-order facts sharpen the boundary without claiming an unfinished global classification.

## Residual risks
- The record does not prove optimality at n=13 or a matching asymptotic upper bound; those limitations are correctly stated.

## Checked sources
- record best13_22.json and ilp witness files
- fresh independent subset enumeration
- Resultary
- arXiv:1108.1247
- arXiv:2601.19068
