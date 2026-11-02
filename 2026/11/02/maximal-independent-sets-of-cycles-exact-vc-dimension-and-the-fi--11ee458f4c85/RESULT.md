# Maximal independent sets of cycles: exact VC dimension and the first adaptive gap

## Finding

For every finite simple cycle \(C_n\), \(n\ge3\), let \(\mathcal I(C_n)\) be the Boolean concept class of its inclusion-maximal independent vertex sets; membership of a vertex is the binary query. Then
\[
\boxed{\operatorname{VCdim}(\mathcal I(C_n))=\left\lfloor\frac{n+1}{3}\right\rfloor\qquad(n\ge3).}
\]
More generally, for every finite simple \(2\)-regular graph \(G=\bigsqcup_{i=1}^t C_{n_i}\),
\[
\boxed{\operatorname{VCdim}(\mathcal I(G))=\sum_{i=1}^t\left\lfloor\frac{n_i+1}{3}\right\rfloor.}
\]
The first cycle on which fixed-query and adaptive-query shattering differ has thirteen vertices:
\[
\operatorname{VCdim}(\mathcal I(C_{13}))=4,
\qquad \operatorname{Ldim}(\mathcal I(C_{13}))=5.
\]
For every cycle of order between three and twelve inclusive, the two dimensions agree. On the thirteen-cycle there are exactly \(39\) maximal independent sets. Across all \(\binom{13}{5}=1287\) five-vertex query supports, the largest number of different traces is exactly \(29\), attained on exactly \(13\) supports, so none is shattered. Nevertheless, a complete adaptive decision tree of depth five has \(32\) distinct valid terminal witnesses.

For every integer \(m\ge1\), the graph \(G_m=\bigsqcup_{j=1}^m C_{13}\) is \(2\)-regular and vertex-transitive, and
\[
\boxed{\operatorname{VCdim}(\mathcal I(G_m))=4m,
\qquad \operatorname{Ldim}(\mathcal I(G_m))=5m.}
\]
Thus the adaptive-minus-static dimension gap is unbounded even among finite vertex-transitive \(2\)-regular graphs. For \(2\)-regular graphs whose cycle components all have at most thirteen vertices, the gap equals the number of thirteen-cycle components.

## Assumptions and scope

Graphs are finite, undirected and simple. A set is maximal independent when no further vertex can be added without destroying independence; equivalently, it is independent and dominates every vertex. Write \(\mathcal I(G)\) for the family of all such subsets of \(V(G)\). The VC dimension is the maximum cardinality of a fixed vertex support on which all binary patterns occur. The Littlestone dimension is the maximum depth of a complete binary decision tree with vertex queries at its internal nodes and one realizable concept on every root-to-leaf answer path. A singleton concept class has Littlestone dimension zero. For a disjoint union, the underlying vertex sets are distinct and concepts factor componentwise.

The exact VC formula holds for every \(n\ge3\) and every finite \(2\)-regular graph (the empty graph has dimension zero by the empty-sum convention). The exact Littlestone classification for individual cycles is asserted only for \(3\le n\le13\). No formula for all longer connected cycles is claimed.

## Proof

**1. Cycle words and the cyclic-gap obstruction.** A maximal independent set of \(C_n\) is represented by a cyclic binary word with no adjacent ones and no run of three zeros. Equivalently, the clockwise distances between consecutive selected vertices are each two or three. This immediately supplies the independent enumeration in `cycle_combinatorial.py`.

Fix a VC-shattered set \(Q\) of \(k\ge1\) vertices, listed in cyclic order, and let its \(k\) positive cyclic gaps be \(d_1,\ldots,d_k\), with sum \(n\). The all-one labeling of \(Q\) is realizable, so every gap has length at least two.

**Obstruction lemma.** Two gaps of length two cannot be separated, clockwise, by only gaps of length three. To prove this, name the first short gap \((q_a,q_{a+1})\), the second \((q_b,q_{b+1})\), and suppose all intervening gaps have length three. Prescribe the responses \(1\) at \(q_a\) and \(q_{b+1}\), and \(0\) at all intermediate queried vertices. Because \(q_a\) is selected, the unique vertex between \(q_a\) and \(q_{a+1}\) is unselected. The zero at \(q_{a+1}\) must therefore be dominated from its clockwise neighbor. In a three-step gap, selecting the neighbor immediately clockwise of the left endpoint forces the neighbor immediately counterclockwise of the right endpoint to be unselected. The same domination requirement propagates through every intervening three-step gap. At \(q_b\), the clockwise neighbor is forced unselected because \(q_{b+1}\) is selected and their gap has length two. Thus \(q_b\) is undominated, a contradiction. This also applies when the two short gaps are consecutive or cyclically wrap around the end of the indexing.

Let \(r\) be the number of gaps of length two and \(s\) the number of gaps of length at least four. If \(r=0\), then \(n\ge3k\). If \(r=1\), then \(n\ge3k-1\). If \(r\ge2\), the obstruction lemma requires a gap of length at least four on each of the \(r\) cyclic arcs between successive short gaps; hence \(s\ge r\). Consequently
\[
n\ge2r+3(k-r-s)+4s=3k-r+s\ge3k.
\]
In every case \(n\ge3k-1\), giving \(k\le\lfloor(n+1)/3\rfloor\).

**2. Matching all-width VC lower bound.** Every integer at least two is a sum of twos and threes. On a long clockwise gap of length \(d\ge3\) between queried vertices with prescribed bits \(x,y\), put a selected vertex at offset zero if \(x=1\), or at offset one if \(x=0\); aim for a selected vertex at offset \(d\) if \(y=1\), or offset \(d+1\) if \(y=0\). The distance between the two selected endpoints is at least two in all four cases, so join them by steps of length two or three. The possible selected vertex at offset \(d+1\) belongs to the next gap and enforces domination of the query at offset \(d\). All selected-vertex distances are two or three, including at the joins. This directed filling therefore realizes every labeling of a query support whose gaps are all at least three. Reflecting clockwise and counterclockwise gives an equally valid incoming-directed filling.

Put \(k=\lfloor(n+1)/3\rfloor\). When \(n=3k\), choose \(k\) gaps of length three; when \(n=3k+1\), choose one gap of length four and the rest of length three. The directed filling proves both supports shattered.

When \(n=3k-1\), choose one gap of length two, with endpoints \(q_0,q_1\), and all remaining gaps of length three. This case arises only for \(n\ge5\) in the stated domain. Prescribe arbitrary query bits \((x,y)\) at the two endpoints. If \((x,y)=(0,1)\), set the short-gap interior bit to zero and fill all long gaps in the incoming direction; this dominates \(q_0\) from the preceding long gap. In the other three cases, fill all long gaps in the outgoing direction; set the short-gap interior bit to one precisely when \((x,y)=(0,0)\), and to zero otherwise. Both endpoints then satisfy independence and domination, and every other zero query is dominated by its outgoing neighbor. Thus every labeling extends to a maximal independent set. This proves the asserted VC formula for all \(n\ge3\).

**3. Exact first adaptive threshold.** For each \(3\le n\le13\), `cycle_exact.py` enumerates all \(2^n\) masks and retains exactly those satisfying the independent-dominating predicate; it enumerates all possible supports to compute VC dimension. It computes Littlestone dimension by exhaustive recursion over both nonempty answer restrictions to every vertex query. Every recursive call strictly decreases the number of concepts, so it is a finite exhaustive calculation, not a heuristic. A separately implemented checker, `cycle_combinatorial.py`, generates concepts from cyclic compositions into twos and threes and computes adaptive depth by a different Boolean feasibility recurrence. The exact results are:

| \(n\) | Number of concepts | VC dimension | Littlestone dimension |
|---:|---:|---:|---:|
| 3 | 3 | 1 | 1 |
| 4 | 2 | 1 | 1 |
| 5 | 5 | 2 | 2 |
| 6 | 5 | 2 | 2 |
| 7 | 7 | 2 | 2 |
| 8 | 10 | 3 | 3 |
| 9 | 12 | 3 | 3 |
| 10 | 17 | 3 | 3 |
| 11 | 22 | 4 | 4 |
| 12 | 29 | 4 | 4 |
| 13 | 39 | 4 | 5 |

The embedded `certificate.json` records the actual depth-five tree for \(C_{13}\): \(31\) internal vertex queries and \(32\) terminal masks, all distinct. Both checkers validate every labeled path. This proves \(\operatorname{Ldim}\ge5\). A complete depth-six tree would require at least \(64\) distinct concepts, but there are only \(39\); hence \(\operatorname{Ldim}\le5\). For each smaller cycle, the exhaustive adaptive recursion establishes equality with its VC dimension. The same certificate contains the complete four- and five-query trace histograms. In particular, all \(1287\) five-query supports are checked, the maximum trace count is \(29\), and exactly \(13\) supports attain it. All five-query supports therefore fail to be shattered.

**4. Products, regularity and symmetry.** The maximal independent sets of a disjoint union are exactly the unions of independently chosen maximal independent sets of the components. For concept classes on disjoint domains, VC dimensions add by coordinatewise shattering. Littlestone dimensions add as well: the lower bound follows by grafting a full decision tree for the second factor below each leaf of a full tree for the first. For the upper bound, a first query belongs to one factor; at least one nonempty answer branch of that factor has Littlestone dimension at most one less than the factor's dimension. Induction on the sum of factor dimensions bounds the smaller product branch, proving the desired equality. (A factor of dimension zero is a singleton concept class, so contributes nothing.)

Applying these facts componentwise gives the all-\(2\)-regular VC formula, and for \(m\) copies of the thirteen-cycle the exact dimensions \(4m\) and \(5m\). Automorphisms of a cycle act transitively, and permutations of isomorphic components act transitively on the components. Therefore \(G_m\) is vertex-transitive and \(2\)-regular. The small-cycle table and product additivity also show that among \(2\)-regular graphs with all components of order at most thirteen, the adaptive gap is exactly the number of thirteen-cycle components.

## Verification

The package supplies `cycle_exact.py`, `cycle_combinatorial.py`, `make_certificate.py`, and the fixed data `certificate.json`. With Python 3, in the package directory execute:

```sh
python cycle_exact.py certificate.json
python cycle_combinatorial.py certificate.json
```

Both programs completed successfully on the embedded certificate. The first checks exhaustive concept enumeration and all shattering supports for eleven cycle sizes, a complete depth-five tree on thirteen vertices, and complete four-/five-query trace distributions. The second independently generates maximal independent sets using cyclic gap compositions, checks ranks through thirteen vertices, and directly scans all \(1287\) five-query supports. No external packages are needed. All-width VC statements and infinite disjoint-union claims are proved mathematically in the preceding sections rather than inferred from these finite checks.

## Relationship to prior work

Bhaskar's *Thicket Density* (first posted February 13, 2017, arXiv:1702.03956) provides general adaptive-shattering foundations. Drmota, Ramos, Requilé and Rué's *Maximal independent sets and maximal matchings in series-parallel and related graph classes* (first posted April 23, 2019, arXiv:1904.10244) develops enumerative and size-distribution methods, including maximal independent sets on cycles and cacti. Walker's *Tree Dimension and the Sauer–Shelah Dichotomy* (first posted March 23, 2022, arXiv:2203.12211) treats general binary shattering theory. Mofidi's *On partial cubes, well-graded families and their duals with some applications in graphs* (first posted December 16, 2022, arXiv:2212.08373) studies well-graded and extremal set families, including systems of independent sets and neighborhoods in graphs. Their inspected results do not supply the exact maximal-independent-cycle VC formula, the adaptive thirteen-cycle threshold, or the vertex-transitive product gap.

The elementary Perrin-number enumeration of maximal independent sets on cycles is background, not presented as new. The present classification uses the same underlying graph objects but evaluates static and adaptive *membership-query shattering*. An earlier path-based maximal-independent-set separation does not imply the all-cycle formula or the first-threshold statement for vertex-transitive degree-two graphs; closing a path into a cycle constrains both endpoint choices and all membership traces.

## Limitations

There is no claim of a closed formula for the Littlestone dimension of every connected cycle beyond order thirteen, nor an optimality statement across all vertex-transitive graphs of a given order. Finite exhaustive checking is not used to certify unbounded universal claims: those follow from the independent structural VC proof and the product-additivity argument. The literature comparison supports best-knowledge originality, not comprehensive historical priority; equivalent characterizations of cyclic independent-dominating families may exist in terminology not recovered by the searches. No independent validation or publication is asserted.

## References

1. S. Bhaskar, *Thicket Density*, arXiv:1702.03956, initial submission 2017-02-13. https://arxiv.org/abs/1702.03956
2. M. Drmota, L. Ramos, C. Requilé, J. Rué, *Maximal independent sets and maximal matchings in series-parallel and related graph classes*, arXiv:1904.10244, initial submission 2019-04-23. https://arxiv.org/abs/1904.10244
3. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, initial submission 2022-03-23. https://arxiv.org/abs/2203.12211
4. A. Mofidi, *On partial cubes, well-graded families and their duals with some applications in graphs*, arXiv:2212.08373, initial submission 2022-12-16. https://arxiv.org/abs/2212.08373
