# Exact quantitative diameter-partition spectra of the five Platonic vertex sets

## Finding

Let \(V\) be the Euclidean vertex set of any regular tetrahedron, cube, octahedron, icosahedron, or dodecahedron. For each integer \(k\geq1\), define the quantitative diameter-partition constant
\[
\beta_k(V)=\min_{V=V_1\sqcup\cdots\sqcup V_k}\frac{\max_i\operatorname{diam}(V_i)}{\operatorname{diam}(V)},
\]
where empty parts are permitted and an empty or singleton part has diameter zero. Put \(\varphi=(1+\sqrt5)/2\). The **complete exact spectra**, including all thresholds and all positive integers \(k\), are as follows.

| Vertex set | Number of parts \(k\) | Exact \(\beta_k(V)\) |
| :-- | :-- | :-- |
| Tetrahedron | \(1\le k\le3\) | \(1\) |
| Tetrahedron | \(k\ge4\) | \(0\) |
| Cube | \(k=1\) | \(1\) |
| Cube | \(2\le k\le3\) | \(\sqrt{2/3}\) |
| Cube | \(4\le k\le7\) | \(1/\sqrt3\) |
| Cube | \(k\ge8\) | \(0\) |
| Octahedron | \(k=1\) | \(1\) |
| Octahedron | \(2\le k\le5\) | \(1/\sqrt2\) |
| Octahedron | \(k\ge6\) | \(0\) |
| Icosahedron | \(k=1\) | \(1\) |
| Icosahedron | \(2\le k\le3\) | \(\sqrt{(1+\varphi)/(2+\varphi)}\) |
| Icosahedron | \(4\le k\le11\) | \(1/\sqrt{2+\varphi}\) |
| Icosahedron | \(k\ge12\) | \(0\) |
| Dodecahedron | \(k=1\) | \(1\) |
| Dodecahedron | \(2\le k\le3\) | \(\varphi/\sqrt3\) |
| Dodecahedron | \(k=4\) | \(\sqrt{2/3}\) |
| Dodecahedron | \(5\le k\le9\) | \(1/\sqrt3\) |
| Dodecahedron | \(10\le k\le19\) | \(\sqrt{(2-\varphi)/3}\) |
| Dodecahedron | \(k\ge20\) | \(0\) |

In particular, the exact four-part ratios of the five solids, in the order above, are \(0,1/\sqrt3,1/\sqrt2,1/\sqrt{2+\varphi},\sqrt{2/3}\).

## Assumptions and scope

The objects are **finite vertex sets**, not their polyhedral interiors or surfaces. All distances are ordinary Euclidean chord distances, independent of the scale and orientation of the regular solid. Parts need not be geometrically connected. The result includes the endpoint conventions at exact distance thresholds; it is not a claim about arbitrary three-dimensional finite sets.

For reproducibility, use \(\varphi=(1+\sqrt5)/2\). A tetrahedron has vertices \((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1)\); a cube has \((\pm1,\pm1,\pm1)\); an octahedron has \(\pm e_i\), \(1\le i\le3\). An icosahedron has vertices
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1),
\]
and a dodecahedron has the eight points \((\pm1,\pm1,\pm1)\) together with
\[
(0,\pm\varphi^{-1},\pm\varphi),\quad(\pm\varphi^{-1},\pm\varphi,0),\quad(\pm\varphi,0,\pm\varphi^{-1}).
\]
All coordinate sign choices in each displayed family are independent.

## Proof

For any threshold \(t\geq0\), define the **far-distance graph** \(G_t(V)\): distinct vertices \(p,q\) are adjacent exactly when \(\|p-q\|^2>t\). A partition has every part's squared diameter at most \(t\) if and only if it is a proper coloring of \(G_t(V)\). Thus \(\beta_k(V)\) is the square root of the smallest threshold with \(\chi(G_t(V))\leq k\), divided by the diameter of \(V\). Only finitely many squared distances need consideration.

Using the coordinates above and the exact relation \(\varphi^2=\varphi+1\), the complete squared-distance threshold lists, and the corresponding chromatic numbers **starting at threshold zero**, are:

| Solid | Increasing positive squared-distance thresholds | \(\chi(G_t)\) at \(t=0\), then at each threshold |
| :-- | :-- | :-- |
| Tetrahedron | \(8\) | \(4,1\) |
| Cube | \(4,8,12\) | \(8,4,2,1\) |
| Octahedron | \(2,4\) | \(6,2,1\) |
| Icosahedron | \(4,4+4\varphi,8+4\varphi\) | \(12,4,2,1\) |
| Dodecahedron | \(8-4\varphi,4,8,4+4\varphi,12\) | \(20,10,5,4,2,1\) |

We certify all upper bounds by complete explicit color vectors in `verify.py`. The script generates the vertices in a fixed order and checks every within-class pair by exact arithmetic in \(\mathbb Q(\sqrt5)\). No numerical tolerance is involved.

For the lower bounds, a color class is an admissible subset with pairwise squared distances at most the selected threshold. The script enumerates **all** subsets of the stated sizes, not random examples. For the cube at \(t=4\) no three-point admissible subset exists, hence at least four colors are required; at \(t=8\), a diameter pair requires two. For the octahedron at \(t=2\) no four-point admissible subset exists, forcing two colors. For the icosahedron at \(t=4\) no four-point admissible subset exists, forcing four colors; at \(t=4+4\varphi\) a diameter pair forces two. For the dodecahedron at \(t=8-4\varphi\) no three-point admissible subset exists, forcing ten colors.

Two further dodecahedral obstructions determine the nontrivial intervening transitions. At \(t=4\) the maximum admissible class size is five and **exactly 12** five-point subsets are admissible. The script checks all four-tuples of these twelve sets and establishes that none covers the 20 vertices. A four-color partition would require four disjoint sets of size five, an impossibility. Thus \(\chi(G_4)\geq5\).

At \(t=8\), exactly **100** admissible seven-point subsets exist and no admissible eight-point subset exists. If a three-color partition existed, its class sizes would necessarily be \(7,7,6\). There are exactly **820** disjoint unordered pairs among the 100 seven-point candidates. For every such pair, the six-point complement contains a pair at squared distance greater than eight. Thus \(\chi(G_8)\geq4\). The explicit five- and four-color witnesses attain these bounds. At dodecahedral \(t=4+4\varphi\), an antipodal diameter pair still forces two colors, and the checker verifies a two-color assignment. Analogous diameter-pair obstructions establish the two-color minima for the other centrally symmetric solids. All remaining thresholds are resolved by the obvious distinction between zero and at least one positive distance together with monotonicity in \(t\).

Because the threshold lists exhaust every actual squared vertex distance, no intermediate cutoff can improve these profiles. Reversing the threshold-coloring correspondence gives exactly the displayed \(\beta_k\) tables for all \(k\).

## Verification

Run `python3 verify.py` from a directory containing the included standalone script. Its final output must contain `EXACT_CERTIFICATE_OK 19 threshold witnesses, and all necessary obstructions`. The verifier constructs all five vertex sets in \(\mathbb Q(\varphi)\), obtains the complete pair-distance spectra independently of the displayed lists, checks 19 explicit coloring certificates, and exhaustively enumerates the decisive forbidden classes and dodecahedral disjoint-set configurations. Arithmetic signs are determined by integer comparisons of squared radicals. Exhaustiveness follows directly from use of the standard-library `itertools.combinations` over all indicated vertex subsets.

## Relationship to prior work

Voronov's October 20, 2026 counterexample to Gale's conjecture motivates precise quantitative diameter-partition constants for finite three-dimensional point sets, and provides a 101-point four-part lower-bound construction. It does not state or entail the complete five-Platonic-vertex spectra above. Hujter and Lángi's work develops Borsuk numbers and multi-colorings of diameter graphs of symmetric finite sets, but does not determine the chromatic numbers at **all** vertex-distance thresholds. Makai and Tarnai analyze a different five-color constraint on dodecahedral vertices: **every pentagonal face must contain all five colors**, yielding inscribed tetrahedral color classes. The present admissible classes instead have bounded chord diameter and its decisive five-vertex classes lie within pentagonal faces. Those statements neither imply nor contradict each other.

## Limitations

The novelty assessment concerns the complete exact threshold classification; elementary coordinate formulas, threshold-graph equivalence, and particular coarse colorability observations are not asserted as new. It is possible that older graph-coloring tables or unindexed geometric literature contain some or all of the resulting finite values. The proof is an exhaustive finite mathematical certificate and does not generalize the classification to arbitrary semiregular polytopes, infinite point sets, or higher dimensions. The comparison is not a refutation of Gale's conjecture; the four-part ratios of these five vertex sets all lie below the sphere benchmark. Independent audit has not been performed.

## References

1. V. Voronov, *A counterexample to Gale's conjecture in R³*, arXiv:2610.28828 (first posted 2026-10-20), https://arxiv.org/abs/2610.28828.
2. M. Hujter and Z. Lángi, *On the multiple Borsuk numbers of sets*, arXiv:1206.0892 (first posted 2012-06-05), https://arxiv.org/abs/1206.0892.
3. E. Makai Jr. and T. Tarnai, *A colouring problem for the dodecahedral graph*, arXiv:1812.08453 (first posted 2018-12-20), https://arxiv.org/abs/1812.08453.
