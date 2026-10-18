# A subfield criterion and five-point individualization threshold for projective-plane colour refinement

## Finding
Let \(q=p^e\) be a prime power with \(e\ge2\). Equip the point--line incidence graph of the Desarguesian projective plane \(\mathrm{PG}(2,q)\) with different initial colours for point vertices and line vertices. Only **point vertices** may be individually coloured, each using its own distinct initial colour. Every unmarked point has a single common colour, and every line has another common colour. Refinement uses the vertex's current colour and the multiset of its neighbours' colours at each synchronous iteration.

Choose any marked set \(S\) containing four points in general position (an ordered projective quadrangle). Use its unique projective coordinate normalization
\[
Q=((0,0,1),(1,0,0),(0,1,0),(1,1,1)).
\]
Write \(K\) for the smallest subfield of \(\mathbb F_q\) containing every coordinate of the normalized marked points. Then **the singleton stable colour classes are precisely the embedded \(K\)-rational points and \(K\)-rational lines**. Both singleton sets have cardinality
\[
|K|^2+|K|+1.
\]
In particular, the entire point--line graph becomes discrete if and only if \(K=\mathbb F_q\).

Even without a quadrangle assumption, the least number of individually coloured **point vertices** making refinement discrete is exactly
\[
\boxed{5}\qquad(q=p^e,\ e\ge2).
\]
Any projective quadrangle together with \((\alpha,0,1)\), for a generator \(\alpha\) of \(\mathbb F_q\) as a field over \(\mathbb F_p\), achieves this bound. More generally, any five marked points containing a quadrangle and generating the full coordinate field achieve it. The theorem does not classify non-quadrangle five-point sets.

## Assumptions and scope
A projective point is a one-dimensional subspace of \(\mathbb F_q^3\), represented by a nonzero homogeneous coordinate triple up to scaling. A projective line is a nonzero linear form up to scaling; incidence means evaluation zero. A quadrangle is four points with no three collinear. The normalizing projective collineation is uniquely determined by an **ordered** quadrangle. A point/line is \(K\)-rational when it has a homogeneous representative in \(K^3\). The subfield \(K\) is intrinsic up to the chosen quadrangle normalization; reordering that quadrangle may transform coordinates by rational projective operations, but the generated subfield and the statement are unaffected.

There is no requirement on the number of additional marked points or their arrangement. Initial point/line sorts are part of the hypothesis. All claims apply uniformly to all primes \(p\) and extension degrees \(e\ge2\), including even characteristic.

## Proof
**1. Singleton-closure lemma.** A vertex in a singleton colour class remains singleton at every later iteration because its own colour is retained in its refinement signature. If two distinct points are singleton, then after one more round their unique joining line is singleton: it is the unique line whose neighbour-colour multiset contains both of the two distinct singleton colours. Dually, if two distinct lines are singleton, their unique intersection point becomes singleton after one more round. This argument works for ordinary one-dimensional colour refinement, not a stronger logical procedure. Therefore every point and line obtainable from marked points by finitely many join and meet operations must eventually have a singleton colour.

**2. Coordinates obtainable from a quadrangle.** Work in the affine chart \((x,y,1)\), with the line at infinity \(z=0\). The four normalized marked points are the origin \(O=(0,0)\), the horizontal and vertical infinity points \(X_\infty=(1,0,0)\) and \(Y_\infty=(0,1,0)\), and \(I=(1,1)\). Joins and meets construct the coordinate axes, the line at infinity, the points \((1,0)\) and \((0,1)\), and the infinity point \(D_\infty=(1,-1,0)\) of slope minus one (join \((1,0)\) to \((0,1)\), then meet with the infinity line).

Given \((a,0)\), draw its line through \(D_\infty\) and meet the vertical axis to obtain \((0,a)\). Given \((a,0)\) and \((b,0)\), first transfer the second to \((0,b)\), then meet the vertical through \((a,0)\) and the horizontal through \((0,b)\) to obtain \((a,b)\). The line from \((a,b)\) through \(D_\infty\) meets the horizontal axis at \((a+b,0)\). Thus the construction realizes addition.

To realize multiplication, join \((0,b)\) to \((1,0)\), mark its intersection direction on the infinity line, and draw the line with this direction through \((a,0)\). Its intersection with the vertical axis is \((0,ab)\), because the first line has equation \(y=b(1-x)\). Transfer again via \(D_\infty\). Thus multiplication is constructible using only joins and meets. As \(q\ge4\), these constructions are valid even in characteristic two, when \(-1=1\).

Any extra marked affine point \((a,b,1)\) gives its coordinates via horizontal and vertical projection onto the axes. A marked infinity point \((1,t,0)\) gives \(t\) by intersecting its line through the origin with the constructible vertical line \(x=1\), and then projecting onto the vertical axis. The remaining infinity point \((0,1,0)\) is already in the quadrangle. Hence the join--meet closure includes every scalar in the field generated by marked coordinates and \(0,1\). The closure is closed under addition and multiplication; every nonzero element of this finite field has an inverse given by a positive power. It therefore contains all points \((a,b,1)\) for \(a,b\in K\), all their points at infinity, and all \(K\)-rational lines. By Step 1, all these points and lines acquire singleton colours.

**3. No additional singleton vertices for a proper subfield.** If \(K\subsetneq\mathbb F_q\), write \(|K|=p^d\) with \(d\mid e\), \(d<e\). The nonidentity field automorphism \(\sigma:t\mapsto t^{p^d}\) fixes every element of \(K\). Applied coordinatewise to homogeneous vectors and line forms, it induces a type-preserving incidence-graph automorphism fixing every marked point. Colour refinement is invariant under colour-preserving automorphisms, so each singleton-coloured vertex is fixed by \(\sigma\). A projective point (or dual line) fixed by coordinatewise \(\sigma\) has all ratios of nonzero homogeneous coordinates fixed by \(\sigma\), hence in \(K\). Thus precisely the \(K\)-rational points and lines can be singleton. If \(K=\mathbb F_q\), Step 2 has already shown all vertices singleton.

**4. The sharp five-point threshold.** For an arbitrary marked set of at most four distinct points, extend it to four points, which is possible in every plane under consideration. If any three of those four are collinear, then either all four lie on that line, or three lie on a line and the fourth is outside. In the first case a nonidentity projective homology fixes the line pointwise; in the second, a homology with that line as axis and the fourth point as centre fixes all four. Such homologies exist because \(q>2\). If no three of the four are collinear, they form a quadrangle. Normalize it to the standard quadrangle; a conjugate of the nonidentity Frobenius automorphism \(t\mapsto t^p\) fixes it pointwise because \(e>1\). Thus in every case there is a nonidentity type-preserving incidence automorphism fixing the marked set. Consequently colour refinement cannot be discrete with four or fewer marked points. Conversely, the projective quadrangle plus \((\alpha,0,1)\), with \(\mathbb F_p(\alpha)=\mathbb F_q\), generates the entire field, so Steps 1--3 give a discrete partition with five marks. Every finite field extension has such a generator, for example a generator of its multiplicative group. This completes the proof.

## Verification
The accompanying standalone Python programs construct finite fields and projective planes directly from irreducible polynomials, run ordinary colour refinement on the complete point--line incidence graph, and independently enumerate all choices of up to four point marks in the smallest extension plane. The code and recorded outputs are embedded beside this manuscript.

Projective-plane checks include \(q=4,8,9,16\), where a normalized quadrangle alone produces exactly the corresponding proper-subfield singleton set and a fifth primitive field generator makes the graph discrete. The program additionally verifies in \(\mathrm{PG}(2,16)\) that adding a fifth mark with its coordinates in the proper subfield \(\mathbb F_4\) yields precisely \(21\) singleton points and \(21\) singleton lines, not a discrete graph. All \(\binom{21}{k}\) marked-point configurations for \(1\le k\le4\) are exhaustively checked for \(q=4\). These finite calculations are tests only; the infinite-family theorem is established by the proof above.

## Relationship to prior work
Bailey and Cameron survey distinguishing sets, permutation-group base size and EP-bases of coherent configurations, including their differences. Arvind and collaborators formalize the parameterized task of individualizing vertices until colour refinement is discrete; their general-complexity results do not provide this exact finite-projective-plane threshold. Arvind, Köbler, Rattan and Verbitsky give the foundational framework for colour refinement and graph isomorphism.

The projective-plane three-marker counting partition and the four-marker prime-field boundary are distinct previously studied cases and are **not** claimed as new here. The present extension-field result goes further by identifying the entire singleton subplane for every marking set containing a projective quadrangle, distinguishing full field generation from a merely trivial geometric projective-linear stabilizer, and proving five-point optimality against semilinear Frobenius symmetries. The analogous affine-plane generator threshold does not itself imply the projective incidence claim, because an affine frame fixes the designated line at infinity whereas an arbitrary projective quadrangle has residual field automorphisms.

## Limitations
The theorem covers only Desarguesian planes over proper finite field extensions and individualization of **point** vertices; line marks, mixed marks, non-Desarguesian planes, and other relational presentations are not classified. The number of refinement rounds and the nonsingleton colour-cell structure are not determined. The geometric closure argument proves eventual discreteness only, not a round-uniform bound. Literature searches cannot rule out all specialized earlier equivalent derivations, especially in coherent configurations and finite-projective-geometry literature. Independent scholarly audit and publication-priority verification remain outstanding.

## References
1. R. F. Bailey and P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, Bulletin of the London Mathematical Society **43** (2011), 209–242. DOI: 10.1112/blms/bdq096. First public journal posting 2011-01-21; author-available complete preprint: https://maths.qmul.ac.uk/~pjc/preprints/bsod.pdf.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first submitted 2015-02-04).
3. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, and G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383 (first submitted 2016-06-14).
