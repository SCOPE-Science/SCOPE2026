# Four-point contranominal scales in nonbinary Hamming radius-one contexts

## Finding
For integers \(q\ge3\) and \(d\ge2\), take the formal context with objects and attributes both \([q]^d\) and incidence \(xIy\) if and only if their Hamming distance is at most one. A \(k\)-point contranominal scale is a selection of distinct objects \(x_1,\ldots,x_k\) and distinct attributes \(y_1,\ldots,y_k\) with \(x_iIy_j\) exactly when \(i\ne j\).

The largest possible scale dimension is **four**. Every four-object scale has **unique matching attributes**, and its objects belong to exactly one of these disjoint geometric families:

* **Two-line type:** all coordinates except two are constant; within those two coordinates the objects form two points on each of two parallel coordinate lines. Interchanging the two coordinates is allowed. Rectangles are the overlap of the two presentations.
* **Parity-tetrahedron type:** all coordinates except three are constant; exactly two alphabet symbols occur in each varying coordinate, and the four objects form one parity class of the resulting binary three-dimensional face.

Writing \(c=\binom q2\), the exact number of distinct four-object contranominal subcontexts, with their uniquely determined matching attributes, is
\[
N_{d,q}=\binom d2q^{d-2}c^2(2c-1)+2\binom d3q^{d-3}c^3.
\]
The second term is zero when \(d=2\). Thus the maximum scale size does not grow with either alphabet size or dimension, even though the number of maximal scales grows rapidly.

## Assumptions and scope
All Hamming words have exactly \(d\) coordinates in an alphabet of size \(q\). A scale is counted as a subcontext: permutations of matched object–attribute pairs do not create different scales. No claim is made about scales below maximum dimension, or about arbitrary non-Hamming formal contexts. The nonbinary parameter range is the new classification scope; the binary instance provides a useful consistency check.

## Proof
**Intersection lemma.** For distinct centers \(a,b\), the radius-one balls \(B_1(a),B_1(b)\) meet in exactly one full coordinate line of \(q\) points if \(d_H(a,b)=1\), in exactly two points if \(d_H(a,b)=2\), and not at all if \(d_H(a,b)\ge3\). In the distance-one case, every common word agrees with the centers outside their single differing coordinate. In the distance-two case it makes exactly one of the two possible coordinate swaps. These claims follow directly by counting mismatching coordinates.

**Upper bound.** If a scale had five matched pairs, two distinct attributes would both contain the other three objects. By the lemma, those attributes are distance one apart and those three objects lie on a common coordinate line \(L\). Any other pair of attributes likewise shares three objects; in particular, pairing the first or second attribute with the third forces each of the two remaining objects onto \(L\), since two already-known common objects determine that coordinate line. All five objects lie on \(L\). But a radius-one ball meets \(L\) either in all of \(L\) (center on the line) or in at most one point (center off it), so no attribute can contain four of the objects and omit the fifth. Thus a five-scale is impossible, and any larger scale would contain a five-scale.

**Four-scale classification.** Fix an attribute \(y_1\), translate its coordinates to base symbols zero, and consider the three incident objects \(x_2,x_3,x_4\). Each differs from \(y_1\) in at most one coordinate. They cannot all lie on one coordinate line: an attribute incident with two of them would then belong to that line and also be incident with the third, contradicting a prescribed missing incidence. Consequently there are three cases.

If one of these objects equals \(y_1\), the remaining two lie on different coordinate lines. Let their changed coordinates be \(i,j\). Each attribute omitting one of these two while containing the other and \(y_1\) must lie on the corresponding one-coordinate line; the fourth object, not incident with \(y_1\), is forced to change exactly coordinates \(i,j\). The four objects form a coordinate rectangle.

If none equals \(y_1\), and the three objects change three different coordinates \(i,j,k\), the attribute omitting any one must be the noncentral common neighbor of the other two, namely the word changed in those other two coordinates. The remaining object must lie in all three of their radius-one balls while outside \(B_1(y_1)\), forcing the word changed in all three coordinates. This is precisely one parity class in a binary three-face.

In the remaining case, two of \(x_2,x_3,x_4\) change one common coordinate \(i\) (to different symbols), and the third changes a different coordinate \(j\). The attributes omitting the first two are the opposite corners obtained by changing \(j\) together with the other \(i\)-symbol. Their two balls intersect in the coordinate-\(i\) line at the changed \(j\)-value. The omitted fourth object must lie on that line, with a nonbase \(i\)-value because it is not incident with \(y_1\). It and the third object give two points of one coordinate-\(j\) line; the original first two points occupy another parallel line. Hence the two-line type. This exhaustive argument also shows that no other four-object types exist.

**Existence and uniqueness of witnesses.** For a two-line configuration, an object in row \(r\) and column \(a\), with the other object in its row at column \(b\), is uniquely omitted by the attribute at the other row and column \(b\). That attribute is incident with the three other selected objects but not with the omitted one. The fact that two different points in one row must both be incident forces the attribute onto that row, proving uniqueness. For a parity tetrahedron, each object's matched attribute is the opposite parity word in the binary three-face that differs from the object in all three varying coordinates; it is distance one from the three other objects and distance three from its omitted object. The intersection lemma makes these witnesses unique.

**Enumeration.** Choose the two varying coordinates and fix the other coordinates, in \(\binom d2q^{d-2}\) ways. On their \(q\)-by-\(q\) grid, choose two rows (\(c\) possibilities) and two points in each row (\(c^2\) possibilities), or transpose rows and columns. The twice-counted configurations are rectangles, of which there are \(c^2\), giving \(2c^3-c^2=c^2(2c-1)\) distinct two-line types. Every such configuration varies in exactly two coordinates, so this count does not overlap between faces. For parity tetrahedra, choose three varying coordinates, the fixed symbols elsewhere, two symbols in each varying coordinate, and one of the two parity classes; this gives \(2\binom d3 q^{d-3}c^3\). Their three-coordinate support separates the two families. The asserted formula follows.

## Verification
Run `python verify.py` with Python 3 and no third-party packages. It independently builds the relation and enumerates all four-object subcontexts in selected small dimensions, checks every witness and its uniqueness, compares the geometry and formula, and excludes all five-scales in those finite cases. Successful execution ends with `VERIFY_OK`. These experiments corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Koyda and Stumme (2021) established the general relationship of contranominal subcontexts to Boolean suborders of concept lattices. Dürrschnabel, Koyda and Stumme (2021) developed a general algorithm based on induced matchings for detecting scales. Neither inspected work states this nonbinary Hamming-radius-one geometric classification or its exact counting polynomial. The general algorithms can in principle enumerate individual examples; they do not imply this closed-form all-parameter classification without additional geometric arguments. Binary-Hamming specialization is related and is not presented as a separate new contribution.

## Limitations
The result is for radius one, the full Hamming product, and nonbinary alphabets; other metrics or arbitrary formal contexts may behave differently. Computational tests are finite. An equivalent unpublished or differently named geometrical enumeration may exist; the priority comparison is based on the searched and inspected literature, not a proof of global novelty. Independent mathematical audit remains to be performed.

## References
1. M. Koyda and G. Stumme, *Boolean Substructures in Formal Concept Analysis* (2021), arXiv:2104.07159, first posted 2021-04-14.
2. D. Dürrschnabel, M. Koyda, and G. Stumme, *Attribute Selection using Contranominal Scales* (2021), arXiv:2106.10978, first posted 2021-06-21.
