# Two-block Schur rings of rectangular bands: biregularity and the sharp non-automorphic threshold

## Finding
Let \(a,b\ge1\), let \(S_{a,b}=[a]\times[b]\) with product \((i,j)(k,l)=(i,l)\), and let \(\mathcal P=\{E,F\}\) be a partition into exactly two nonempty blocks. Call it a *Schur partition* when its two block sums span a subring of \(\mathbb Q[S_{a,b}]\). Then the following conditions are equivalent:

1. \(\mathcal P\) is a Schur partition.
2. Either \(E\) is a union of whole rows, \(E\) is a union of whole columns, or its \(a\)-by-\(b\) incidence matrix has one constant row sum \(r\) and one constant column sum \(s\), where \(0<r<b\), \(0<s<a\), and \(ar=bs\).

In the third case, \(E\) is precisely the edge set of a spanning biregular bipartite graph. Such a partition is *automorphic* (the orbit partition of a subgroup of \(\operatorname{Aut}(S_{a,b})\)) exactly when the color-preserving group \(S_a\times S_b\) is transitive on both its edges and its nonedges. Row-cut and column-cut partitions are always automorphic.

**Sharp threshold:** Every two-block Schur partition of a rectangular band with fewer than \(24\) elements is automorphic. At \(S_{4,6}\) the property first fails. This band has exactly \(968\) two-block Schur partitions on its fixed labeled set: \(428\) automorphic and \(540\) non-automorphic. In particular the first failure is not isolated: it accounts for more than half of these partitions.

## Assumptions and scope
The semigroup has \(ab\) labeled elements and is considered over \(\mathbb Q\). No identity or inverse axiom is imposed on Schur partitions. A two-block partition is unordered: exchanging \(E\) and \(F\) does not produce a new Schur ring. An automorphic partition means **exactly** the orbits of some subgroup of the semigroup automorphism group; an arbitrary permutation-group realization is not enough. The threshold concerns rectangular bands and two-block partitions only, not arbitrary finite semigroups or partitions with three or more blocks.

## Proof
**Step 1: a necessary-and-sufficient multiplication test.** For a subset \(X\subseteq S_{a,b}\), set \(r_X(i)=|X\cap(\{i\}\times[b])|\) and \(c_X(j)=|X\cap([a]\times\{j\})|\). The coefficient of \((i,j)\) in the product of the block sums \(\underline X\,\underline Y\) is exactly \(r_X(i)c_Y(j)\), because an input pair multiplying to \((i,j)\) must have left row \(i\) and right column \(j\). The span of the two block sums consists of exactly those coefficient functions constant on each of \(E,F\).

For two cells \((i,j),(i',j')\) of the same block, requiring constancy of all four products \(r_X(i)c_Y(j)\) for \(X,Y\in\{E,F\}\) implies \(r_X(i)=r_X(i')\) by summing over \(Y\), since \(c_E(j)+c_F(j)=a\). Likewise summing over \(X\) gives \(c_Y(j)=c_Y(j')\), since \(r_E(i)+r_F(i)=b\). The converse is immediate by multiplying these equalities. Writing \(d_i=r_E(i)\) and \(e_j=c_E(j)\), the partition is Schur exactly when, within each of the two colors, all cells have the same \(d_i\) and the same \(e_j\).

**Step 2: classify the row/column profiles.** If any row contains only \(E\), then its \(E\)-degree is \(b\). Every row containing an \(E\)-cell consequently has \(E\)-degree \(b\), so all rows are monochromatic and \(E\) is a union of rows. Likewise, a row containing only \(F\) forces all rows monochromatic. Otherwise every row contains both colors, and comparing cells of either color shows that all \(d_i\) equal one integer \(r\) strictly between \(0\) and \(b\). Applying the same argument to columns shows that either \(E\) is a union of columns or all columns have a common degree \(s\) strictly between \(0\) and \(a\). If neither kind of cut occurs, double-counting \(|E|\) gives \(ar=bs\). In each of the three stated cases the within-block row and column degrees are constant, so Step 1 gives sufficiency.

**Step 3: the orbit criterion.** The principal right ideals and principal left ideals of \(S_{a,b}\) recover its row and column classes, respectively. Every automorphism therefore permutes rows and columns separately, and every pair of such permutations is an automorphism: \(\operatorname{Aut}(S_{a,b})\cong S_a\times S_b\). The largest subgroup preserving both \(E\) and \(F\) is the color-preserving automorphism group of the bipartite incidence graph. A subgroup has exactly these two orbits if and only if this largest preserving group is transitive on both classes. Row and column cuts admit the obvious product-of-symmetric-groups actions.

**Step 4: all smaller sizes.** If \(\min(a,b)\le2\), any proper biregular incidence graph is a balanced collection of equal-sized stars or its complement; permutations of the short side and matched permutations of the long-side fibers act transitively on each color. The same holds for \(\min(a,b)=3\): proper column degrees on the three-vertex side are \(1\) or \(2\); the possible column neighborhoods are respectively singleton sets or their complements, and uniform row degrees force equal multiplicities of each of the three neighborhood types. The induced symmetric-group action is transitive on both incident and nonincident row-column pairs.

It remains to consider \(a,b\ge4\) with \(ab<24\), up to exchanging the two factors: \((a,b)=(4,4)\) or \((4,5)\). In the latter case \(4r=5s\) has no solution with \(0<r<5\) and \(0<s<4\). For the former, \(r=s\in\{1,2,3\}\). Degrees \(1\) and \(3\) are the perfect-matching/complement cases, which are color-transitive. A \(2\)-regular bipartite graph on four vertices per side is either one eight-cycle or two disjoint four-cycles. In the eight-cycle case, take edges \((i,i)\) and \((i,i+1)\) for indices modulo four; simultaneous rotations and the reflection \((i,j)\mapsto(-i,1-j)\) preserve both colors and act transitively on each. In the two-four-cycle case, within-component permutations and component exchange act transitively on both colors. Thus no smaller rectangular band gives a two-block counterexample.

**Step 5: the \(4\)-by-\(6\) witness and complete count.** Put \(E\) at the entries marked \(1\) in the matrix below and \(F\) at the entries marked \(0\):

```
1 1 0 0 1 0
1 1 0 0 0 1
0 0 1 1 1 0
0 0 1 1 0 1
```

Each row has three \(1\)'s and each column has two, so the partition is Schur. Two column-neighborhood types occur with multiplicity two, while the other two occur with multiplicity one. Any automorphism preserving \(E\) must preserve the size of each column-neighborhood twin class; consequently no such automorphism sends an \(E\)-cell in a doubled column type to an \(E\)-cell in a singleton column type. Thus \(E\) is not one orbit.

For an exact census, the number of unordered row cuts is \(2^{4-1}-1=7\), and the number of column cuts is \(2^{6-1}-1=31\). Every remaining two-block partition has row degree \(3\) and column degree \(2\), since \(4r=6s\) and both degrees are interior. Treat each of the six labeled columns as an edge on the four row vertices. The result is a loopless \(3\)-regular multigraph with six labeled edges. Its edge-multiplicity multiset must be precisely one of the following three types:

* \((3,3)\) on two disjoint pairs (\(3\) choices of perfect matching, times \(6!/(3!3!)=20\) orderings): \(60\) labeled incidence matrices.
* \((2,2,1,1)\) on two disjoint doubled pairs and one other matching of single pairs (\(3\) choices of the doubled matching, \(2\) choices of the single matching, times \(6!/(2!2!)=180\) orderings): \(1080\) matrices.
* \((1,1,1,1,1,1)\), one copy of each edge of the complete graph on four vertices: \(6!=720\) matrices.

These are exhaustive: a triple edge saturates its endpoints, forcing another disjoint triple; without triple edges, a double edge forces another disjoint double and two disjoint singleton edges; if there are no repeated edges, all six edges are present. The first and third types have color-preserving automorphism groups transitive on both incidence and nonincidence flags. The middle type does not, because of the different column-twin multiplicities. There are \(60+1080+720=1860\) *oriented* nontrivial biregular matrices. Each unordered partition is counted twice, once as \(E\) and once as \(F\). Therefore the total is \(7+31+1860/2=968\), of which \(1080/2=540\) are non-automorphic and \(7+31+(60+720)/2=428\) are automorphic.

The same non-automorphic obstruction survives uniform row and column blow-ups of the displayed witness, so it supplies examples on every rectangular band with factor sizes \((4u,6v)\) for positive integers \(u,v\).

## Verification
The accompanying standalone `verify.py` implements the block-sum multiplication criterion independently of the graph profile characterization, exhaustively checks every two-coloring (excluding empty/full colors) on \(2\times2\), \(3\times3\), \(3\times4\), and \(4\times4\) rectangular bands, and directly tests the automorphism-group orbit criterion for every Schur coloring in these cases. It separately checks the displayed \(4\times6\) counterexample and enumerates all \(6^6=46656\) labeled six-column endpoint assignments, counting each regular incidence matrix, its multiplicity profile, and its color-preserving orbit behavior. The expected exact output ends with `VERIFY_OK`.

The finite checks corroborate the boundary and census. The arbitrary-size structural theorem and the sharp minimality proof are established by the arguments above, not inferred from samples.

## Relationship to prior work
Marrow and Misseldine introduced semigroup Schur rings and the automorphic construction and observed that rectangular bands have at least the direct-product family of Schur rings; their full paper enumerates semigroups of size at most seven. Neither its rectangular-band discussion nor its enumeration gives a two-block characterization, a sharp automorphic failure threshold, or the \(4\times6\) numbers above. A related classification of all Schur partitions for two-row rectangular bands proves that those bands have only automorphic Schur rings; it gives no conclusion for the \(4\times6\) example and does not determine the sharp first failure. Biregular graphs and graph automorphism orbits are standard graph-theoretic notions; the contribution here is their precise Schur-partition equivalence and the sharp boundary with complete first-case counts.

## Limitations
Only partitions with exactly two nonempty blocks are classified. The result does not enumerate the total number of Schur rings with arbitrary block number on \(S_{4,6}\), nor does it determine the first non-automorphic Schur ring among all partitions with more than two blocks. Bibliographic searches cannot rule out differently named prior equivalents. No independent external mathematical audit has been performed.

## References
- J. E. Marrow and A. Misseldine, *On Schur Rings Over Semigroups*, first public arXiv submission January 14, 2026, arXiv:2601.09940; specifically Sections 1, 2.1–2.2, 5–6. https://arxiv.org/abs/2601.09940
- Standard terminology: *biregular (semiregular bipartite) graph* and color-preserving bipartite graph automorphisms.
