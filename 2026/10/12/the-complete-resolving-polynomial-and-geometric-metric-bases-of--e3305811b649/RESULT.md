# The complete resolving polynomial and geometric metric bases of the Pappus graph

## Finding

Let \(H\) be the eighteen-vertex Pappus graph, the incidence graph of the biaffine plane obtained by omitting one direction from the affine plane of order three. A resolving set \(S\subseteq V(H)\) is a set for which all eighteen distance vectors \((d(v,s))_{s\in S}\) are distinct. Its resolving polynomial is \(R_H(z)=\sum_{S\text{ resolving}}z^{|S|}\).

**Theorem.** Every minimum resolving set has four vertices. There are exactly \(216\) such sets, characterized geometrically below, and exactly two full-automorphism orbits, each of cardinality \(108\), distinguished by the number \(0\) or \(1\) of edges induced by the four landmarks. The complete polynomial is

\[
\begin{aligned}
R_H(z)={}&216z^4+2808z^5+13500z^6+29232z^7\\
&+42894z^8+48440z^9+43740z^{10}+31824z^{11}\\
&+18564z^{12}+8568z^{13}+3060z^{14}\\
&+816z^{15}+153z^{16}+18z^{17}+z^{18}.
\end{aligned}
\]

In particular there are \(243834\) resolving sets and \(18310\) nonresolving subsets.

## Assumptions and scope

All coordinates are in \(\mathbb F_3\). Vertices are the nine points \(P(x,y)\) and the nine retained lines \(L(m,b)\), where \(x,y,m,b\in\mathbb F_3\); adjacency means \(y=mx+b\). The three vertical classes \(x=0,1,2\) are **not** line vertices. Thus points in the same vertical class have graph distance four, while points in different classes have distance two. Likewise, two distinct line vertices have distance four if their slopes coincide and distance two otherwise. A point and a line have distance one when incident and three otherwise. These formulas follow by direct two-step incidence checks and bipartiteness, and agree with shortest-path computation.

For distinct points \(p=P(x_p,y_p)\), \(q=P(x_q,y_q)\) with \(x_p\ne x_q\), write \(j=j(p,q)\) for their unique common retained line, with slope \(m_0=(y_q-y_p)/(x_q-x_p)\). Two distinct, nonparallel retained lines intersect at one affine point \(r\); this point need not be selected.

**Geometric classification.** A four-element set \(S\) resolves \(H\) if and only if \(S=\{p,q,a,b\}\) with two point vertices and two line vertices satisfying every one of the following conditions:

1. The points have \(x_p\ne x_q\).
2. The lines have different slopes.
3. Exactly one selected line is parallel to \(j(p,q)\), and this selected parallel line is **not** \(j(p,q)\) itself.
4. The affine intersection \(r=a\cap b\) satisfies \(x_r\in\{x_p,x_q\}\).

For each of the \(27\) unordered pairs of points from different vertical classes there are exactly \(2\) allowed parallel lines, \(2\) allowed intersection classes, and \(2\) allowed second-line slopes, giving \(27\cdot2\cdot2\cdot2=216\) bases.

## Proof

**Lower bound and bipartition.** A set consisting entirely of at most four points cannot resolve the graph: among the three vertical point classes, one contains at least two unselected points, and both have equal distances to all selected points. Dually no all-line set of at most four vertices resolves. If a set contains exactly three point landmarks and one line landmark, consider the six other line vertices belonging to the two slopes different from the selected line's slope. All six have equal distance to that line landmark. Each of the three selected points is incident with exactly two of these six lines, so the six binary incidence signatures on the selected points together have exactly six \(1\)-entries. But any six distinct three-bit words have at least seven \(1\)-entries (their lowest-weight possible selection has weights \(0,1,1,1,2,2\)). Therefore two of these six lines have equal distance vectors. Duality rules out one point and three lines. For a two-points-and-one-line set, the same six lines have at most four possible two-bit signatures, so this also fails; its dual rules out one point and two lines. The remaining configurations with at most three landmarks reduce to these or the all-one-part cases. Thus any four-vertex basis must contain two points and two lines, and no set with at most three landmarks resolves.

**Distinct point classes and slopes.** If the two chosen points are in the same vertical class, then all six points in the two other classes are at distance two from both point landmarks. The two line landmarks give them at most four distinct binary incidence signatures, so at least two remain unresolved. Thus \(x_p\ne x_q\). The dual argument forces the two chosen line slopes to differ.

**The parallel-line condition.** Among the three line slopes, one slope is not represented by the selected lines. All three line vertices in that missing slope class are equidistant from both line landmarks. To be distinguished by the two selected points, those points must lie on **different** lines of the missing slope. The unique line \(j\) through \(p,q\) must therefore have a slope represented by the selected lines. Because their slopes differ, exactly one of \(a,b\) has the slope of \(j\). Call it \(a\). If \(a=j\), then the third vertical class contains three unselected points, all with equal distances to \(p,q\), so \(a,b\) must each meet that class in distinct points to distinguish them. This forces \(b\cap j\) to lie in the vertical class of \(p\) or \(q\), and hence \(b\cap j=p\) or \(q\). In that selected point's vertical class, however, the two other points meet neither \(a=j\) nor \(b\); they also have equal distances to both selected points. This contradiction proves \(a\ne j\).

**Intersection condition.** The three points of the third vertical class are at distance two from both selected points; they have distinct full signatures if and only if \(a\) and \(b\) meet that class in different points. Because the lines are nonparallel, that happens exactly when their intersection is **not** in that third class, equivalent to \(x_r\in\{x_p,x_q\}\).

**Sufficiency.** Suppose all four conditions hold. The two selected points distinguish the point classes (apart from the selected points themselves, their distance-to-pair patterns are \((4,2)\), \((2,4)\), and \((2,2)\)). The line \(a\), parallel but unequal to \(j\), selects a different point than \(p\) in the class of \(p\) and a different point than \(q\) in the class of \(q\); the two unselected vertices in each such class therefore have different incidences with \(a\). In the third class, \(a\) and \(b\) meet distinct points, distinguishing all three. Thus all point vertices are resolved. For line vertices, selected lines separate the three slope classes by distances \(0,2,4\) as applicable. In the slope of \(j\), the remaining two line vertices are \(j\), incident to both \(p,q\), and a third line, incident to neither. In the slope of \(b\), the distinct lines through \(p\) and \(q\) are distinct, so any unselected lines there have distinct incidence patterns. In the remaining slope, the three lines have patterns \((1,0)\), \((0,1)\), \((0,0)\) because this slope differs from that of \(j\). Thus all line vertices are resolved. A point and a line are distinguished by the parity of their distance to any nonempty landmark. Therefore \(S\) resolves the entire graph.

**Counting and symmetry.** There are \(3\cdot3\cdot3=27\) pairs of points in distinct vertical classes. Once \(p,q\) are fixed, choose one of the two other lines parallel to \(j\); choose the intersection on either selected vertical class, and one of the two other slopes, uniquely determining \(b\). This yields \(216\) sets. The graph admits \(108\) affine incidence-preserving transformations \(x\mapsto ax+b\), \(y\mapsto cx+dy+e\) with \(a,d\in\mathbb F_3^\times\), together with a point-line duality, giving \(216\) automorphisms in all. The known full automorphism-group order is \(216\) [4], so these are all. Direct application to the \(216\) bases gives two orbits, of size \(108\) each, distinguished by whether the four selected vertices induce zero or one incidence edge. Exact orbit generation is implemented in the standalone verifier.

**All cardinalities.** For each unordered pair \(\{u,v\}\) of the eighteen vertices form the distinguishing mask \(M_{uv}=\{s:d(s,u)\ne d(s,v)\}\). A subset is resolving exactly when it meets all \(153\) such masks. The verifier enumerates all \(2^{18}=262144\) subsets, independently evaluates the mask-intersection condition and every distance signature from the finite-field formulas, and tallies resolving subsets by cardinality. The printed coefficient vector is the one stated in the theorem; finite exhaustive enumeration is valid for this fixed finite graph, not asserted to generalize to larger orders.

## Verification

Run `python3 verify.py` with the Python 3.9+ standard library, from the directory containing `verify.py`. The script constructs the graph directly from the displayed incidence equation, obtains all graph distances by BFS, compares each one against the coordinate formulas, exhaustively evaluates all \(262144\) vertex subsets using two equivalent but independently implemented tests, and verifies the geometric characterization on all \(\binom{18}{4}=3060\) four-vertex subsets. It then constructs and checks each of the \(216\) automorphisms, checks exact orbit partitions and induced-edge counts, and confirms the full resolving polynomial.

The output asserts: metric dimension \(4\), \(216\) minimum bases, \(243834\) resolving subsets, \(18310\) nonresolving subsets, and orbit sizes \(108,108\). No floating-point arithmetic or external datasets are needed.

## Relationship to prior work

Bailey [1] determined the metric dimension \(4\) of the Pappus graph, a fact **not** claimed here as new. Bailey's later discussion [2] also records the exceptional biaffine order-three case. Bartoli–Héger–Kiss–Takáts [3] treat metric-dimension bounds for biaffine incidence graphs in larger orders, rather than this complete exceptional graph classification. The general construction and automorphism order are standard [4]. These published results give neither the explicit if-and-only-if description of all four-landmark bases nor the full cardinality generating polynomial or the two optimum orbits. Generic results about resolving polynomials do not by themselves imply the coefficients of this instance.

## Limitations

The theorem concerns **ordinary vertex metric resolving sets** of this specific eighteen-vertex graph; it does not concern edge, strong, doubly, or multiset resolving variants, nor other biaffine orders. The polynomial's coefficients and orbit split are rigorously exhaustive finite computations checked by the supplied standalone source, not a symbolic closed expression uniform in graph order. Existing unpublished or unindexed instance enumerations cannot be ruled out. Prior literature is credited for the known minimum cardinality and group order.

## References

[1] R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973 (initially public 17 December 2013), particularly Table 1. https://arxiv.org/abs/1312.4973

[2] R. F. Bailey, *On the metric dimension of incidence graphs*, arXiv:1707.02899, Corollary 3.4. https://arxiv.org/abs/1707.02899

[3] D. Bartoli, T. Héger, G. Kiss and M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583. https://arxiv.org/abs/1706.06583

[4] A. E. Brouwer, Pappus graph reference table, including automorphism group order. https://aeb.win.tue.nl/graphs/Pappus.html
