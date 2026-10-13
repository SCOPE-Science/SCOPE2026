# The complete resolving polynomial and all metric bases of the Heawood graph

## Finding

Let \(H\) be the fourteen-vertex point-line incidence graph of the Fano plane. A set \(S\subseteq V(H)\) is *resolving* when, for each pair of distinct vertices \(x,y\), some vertex \(s\in S\) has \(d(x,s)\ne d(y,s)\). Define its ordinary resolving polynomial by
\[
 R_H(z)=\sum_{\substack{S\subseteq V(H)\\S\text{ resolves }H}}z^{|S|}.
\]
Then
\[
\boxed{R_H(z)=168z^5+1890z^6+3096z^7+2961z^8+2002z^9+1001z^{10}+364z^{11}+91z^{12}+14z^{13}+z^{14}.}
\]
Consequently the previously known metric dimension \(\mu(H)=5\) has exactly \(168\) minimum resolving sets (metric bases). Exactly \(84\) bases comprise three points and two lines, and the other \(84\) are their duals. All \(168\) form one orbit under the order-\(336\) automorphism group of \(H\).

More precisely, choose two distinct Fano lines \(\ell,m\) meeting in \(x\). Choose a point \(a\in\ell\setminus\{x\}\), a point \(b\in m\setminus\{x\}\), and a point \(c\) outside \(\ell\cup m\), subject to \(a,b,c\) being noncollinear. Then \(\{a,b,c,\ell,m\}\) is a metric basis. These are exactly the \(84\) bases of the three-point/two-line type; applying point-line duality produces every other basis.

There is also an exact all-set criterion: for each pair of distinct same-type vertices \(x,y\) (both points or both lines), put \(E_{xy}=\{v\in V(H):d(v,x)=d(v,y)\}\). The \(42\) sets \(E_{xy}\) are distinct and each has cardinality eight. A subset \(S\) resolves \(H\) if and only if it is contained in none of these \(42\) sets. Opposite-type vertex pairs have empty equidistance sets.

## Assumptions and scope

The Fano plane has point set \(P=\{0,1,\ldots,6\}\) and seven lines \(L_i=\{i,i+1,i+3\}\) for \(i\in\mathbb Z/7\mathbb Z\); all entries in line descriptions are reduced modulo seven. Vertices of \(H\) are the seven points and the seven lines, with an edge precisely for an incidence. Graph distances use the unweighted undirected shortest-path metric. The polynomial counts labelled vertex subsets, not orbits, up to the fourteen-vertex set. The complete coefficient and orbit statements concern this fixed finite graph, not all projective planes or all cubic graphs.

## Proof

**Equidistance geometry.** Two distinct points are distance two apart; their distance vectors to a vertex of opposite type are one or three according to incidence, while distance vectors to points take values zero at that point and two at other points. For points \(x\ne y\), precisely the five other points are equidistant to \(x,y\). Among lines, precisely one line through both and two lines through neither are equidistant, contributing three more vertices. Thus \(|E_{xy}|=8\). By duality the same holds for two lines. These \(21+21=42\) sets are distinct: in the point-pair case the omitted point vertices uniquely recover \(\{x,y\}\); the dual case instead omits two line vertices. In the bipartite graph, if \(x\) is a point and \(y\) is a line, their distances from every fixed vertex have opposite parity. Hence \(E_{xy}=\varnothing\) in that case. For any graph, \(S\) fails to resolve precisely when \(S\subseteq E_{xy}\) for some distinct \(x,y\), proving the all-set criterion.

**Minimum-base classification.** Write \(S=A\cup B\) with selected Fano points \(A\) and selected lines \(B\). Suppose at most one line is selected. Relative to one selected line, the other seven points have two distance-signature classes, of sizes three and four, so identifying all points requires selecting at least two of the first class and three of the second: at least five selected points in addition to the selected line. With no selected line, at least six points must be selected. The dual bounds apply to selected points. Therefore a five-vertex resolving set must have three points and two lines, or the reverse.

Fix the two selected lines \(\ell,m\), intersecting at \(x\). Their incidence patterns split the seven Fano points into one singleton \(\{x\}\) and three two-point classes \(\ell\setminus\{x\}\), \(m\setminus\{x\}\), and \(P\setminus(\ell\cup m)\). Three selected points distinguish the other points if and only if they consist of one representative from each two-point class. The selected points also must distinguish all remaining lines. If these three points are noncollinear, their line-incidence signatures on all seven Fano lines are exactly the seven distinct binary triples: three weight-two, three weight-one, and one weight-zero. If the selected points are collinear, the other six Fano lines give three duplicate signature pairs (each singleton incidence pattern twice); the two selected lines \(\ell,m\) remove at most two of the three duplicates, so resolution fails. Thus noncollinearity is both necessary and sufficient.

For each unordered pair of lines, there are two choices each for \(a,b,c\), giving eight candidates. After \(a\) and \(b\) are chosen, the third point of their joining line lies in the two-point set \(P\setminus(\ell\cup m)\). Exactly one of the two choices for \(c\) is collinear, so four choices work. There are \(\binom72=21\) pairs of lines and thus \(21\cdot4=84\) bases with three points and two lines. Duality gives another \(84\), with no overlap. In particular \(\mu(H)=5\), consistently with Héger--Takáts (2012).

**Complete coefficient verification.** The all-set criterion reduces counting to a finite union of Boolean subcubes: for each of the \(42\) eight-vertex equidistance sets \(E\), mark its \(2^8\) subsets as nonresolving. The accompanying standalone `verify.py` explicitly constructs those \(42\) subsets from Fano incidence, checks each against actual shortest-path equidistance sets, and enumerates all \(2^{14}=16{,}384\) vertex masks. It independently evaluates distance signatures for every mask and verifies agreement with the union criterion. The exact cardinality-by-cardinality counts of resolving masks are \(168,1890,3096,2961,2002,1001,364,91,14,1\) in sizes five through fourteen, with no smaller resolving masks; these are the displayed polynomial coefficients. This enumeration is exhaustive on the finite domain, not numerical extrapolation.

**Orbit check.** All point permutations preserving the seven Fano lines are exhaustively generated (there are \(168\)); the script also constructs and verifies an incidence-reversing polarity. These yield \(336\) distinct adjacency-preserving permutations, the entire automorphism group since a connected bipartite incidence graph automorphism either preserves or exchanges the bipartition and a part-preserving one is precisely a collineation. The orbit of one minimum base under these \(336\) maps contains all \(168\) minimum bases. The script checks this equality explicitly.

## Verification

Run `python3 verify.py` with Python 3.8 or later; no third-party packages or data files are required. The source constructs the Fano incidence graph from the seven explicitly given lines, checks its incidence axioms, computes all-pairs distances by BFS, builds all 42 exact equidistance masks, and compares the geometric predicate with direct distance-vector uniqueness for all 16,384 subsets. It reconstructs every minimum base, its point-line split, the 168 collineations, a duality, the 336 graph automorphisms, and the unique minimum-base orbit. Successful output contains the exact markers `all_masks=16384`, `resolving=11588`, `bases=168`, `full_automorphism_group=336`, and `base_orbits=1`.

## Relationship to prior work

Héger and Takáts (arXiv:1207.5469, first public preprint 23 July 2012) already proved the Fano plane's metric dimension equals five (Remark 2.6), and their Propositions 2.2--2.3 give a general necessary-and-sufficient point-line resolving-set condition for all finite projective planes. Their main classification concerns the minimum resolving sets for order at least 23; it does not give the complete Fano resolving polynomial, the 168-base enumeration, or the orbit decomposition. Bailey (arXiv:1312.4973, 2013) also records the Heawood metric dimension in a table of small distance-regular graphs but not these cardinality coefficients. The present finite calculation does not claim the general resolving criterion or the scalar metric dimension as new. Its contribution is the exact small-plane all-size enumeration, geometric description of *all* bases, and symmetry result.

## Limitations

This theorem concerns only the Fano incidence graph and ordinary vertex resolving sets. It neither settles a problem for higher-order projective planes nor asserts a general formula for their resolving polynomials. The self-review are reproducible but are not an independent external audit. Earlier equivalent enumerations under different terminology or in unindexed computational tables cannot be excluded absolutely; the closest inspected publications do not report the detailed counts.

## References

1. T. Héger and M. Takáts, *Resolving sets and semi-resolving sets in finite projective planes*, Electronic Journal of Combinatorics **19** (2012), P30; arXiv:1207.5469v1 (23 July 2012). https://arxiv.org/abs/1207.5469 . Propositions 2.2--2.3 and Remark 2.6.
2. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973v1 (17 December 2013). https://arxiv.org/abs/1312.4973 . Table of metric dimensions.
3. R. F. Bailey, *On the metric dimension of imprimitive distance-regular graphs*, arXiv:1312.4971v1 (17 December 2013). https://arxiv.org/abs/1312.4971 . Incidence graphs of symmetric designs.
