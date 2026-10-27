# Three rank-four theories of finite projective point-line geometries

## Finding

Let \(\mathcal G\) consist of all finite projective planes of orders \(q\ge2\), whether Desarguesian or not, and all finite projective spaces \(\mathrm{PG}(d,q)\) over finite fields, where \(d\ge3\). Interpret each as a one-sorted relational structure with disjoint unary predicates \(P,L\) naming points and lines and binary incidence \(I\subseteq P\times L\). No coordinates, field operations, or higher-dimensional subspaces are named.

**Theorem.** For \(A,B\in\mathcal G\), their first-order sentences of quantifier rank at most four agree precisely when \(A,B\) belong to the same one of the following three classes:

1. projective planes of order \(2\);
2. projective planes of order at least \(3\);
3. projective spaces of projective dimension at least \(3\).

The minimum universe sizes (points plus lines) for these classes are, respectively, \(14,26,50\), attained by \(\mathrm{PG}(2,2)\), \(\mathrm{PG}(2,3)\), and \(\mathrm{PG}(3,2)\). Hence the uniform bound \(50\) is optimal for representatives from \(\mathcal G\). The two plane classes are indistinguishable at rank three but not rank four.

## Assumptions and scope

Projective order means that each line contains \(q+1\) points and each point lies on \(q+1\) lines in a projective plane; the plane has \(q^2+q+1\) of each sort. For higher-dimensional members, \(q\) is a prime power and \(P,L\) denote one- and two-dimensional vector subspaces of \(\mathbb F_q^{d+1}\). Incidence is subspace containment. Projective dimension at least three means the geometry contains skew lines. All structures are finite, and all quantifiers range over their disjoint union of points and lines.

## Proof

**1. Rank types.** For a finite relational structure and an ordered tuple \(\bar a\), let \(T_0(\bar a)\) be its complete atomic diagram (including sorts, equality, and incidences). Recursively define \(T_{j+1}(\bar a)\) by the pair of \(T_0(\bar a)\) and the set of all \(T_j(\bar a,b)\), with \(b\) ranging over the structure. The standard induction on formulas shows that \(T_j\) determines precisely the formulas of quantifier rank at most \(j\) in the named tuple. Thus the rank-four sentence theory is determined by the extension tree for tuples of lengths \(0,1,2,3\); at length three only the set of possible *atomic one-point extensions* is needed.

**2. The three-object extension lemma.** Classify three distinct named objects by their sorts and incidences, also retaining the elementary geometric relations needed to determine one further atomic extension. The complete cases are as follows.

* Three points: either collinear or noncollinear. New-line incidence patterns with these points are determined by this dichotomy. If the points are collinear, the pattern of avoiding all three occurs in a plane of order \(q\) exactly when \(q\ge3\); if they are noncollinear it always occurs.
* Two points and one line: the line contains zero, one, or both named points. The unique line joining the named points and the availability of a fresh line meeting exactly zero or one of them determine all new-line patterns. A fresh point both on and off the named line is always available.
* One point and two lines: retain whether the named point is on either line, and whether two distinct lines meet at the named point, meet elsewhere, or are skew. The common-point pattern is possible for a fresh point exactly if the lines meet away from the named point. Fresh points of each single-line or no-line incidence pattern exist; a fresh line through or avoiding the named point also exists.
* Three lines: retain the intersection graph of the three lines, and, in the all-intersecting case, whether their intersections are concurrent or form a triangle. A fresh point lying on any prescribed single line exists. Membership in two or three lines occurs exactly when the indicated intersections exist at the required point. A fresh point on none of the three lines exists in every case except three distinct concurrent lines in a plane of order two.

Repeated objects reduce to shorter tuples, with equality-specific extensions supplied by reselecting a named object. For the non-repeated cases, these assertions are exhaustive: the fourth object has one of two sorts, with incidences only to the already named objects of the opposite sort, and its equality to previously named objects is separately fixed.

Here are the critical numerical bounds, which also establish the exceptional zeros. In a projective plane, three concurrent lines cover \(1+3q\) points, leaving \(q(q-2)\) points, and three nonconcurrent lines cover \(3q\) points, leaving \((q-1)^2\). Dually, three collinear points have \(q(q-2)\) lines avoiding all three, while three noncollinear points have \((q-1)^2\) such lines. One line or pencil contains at least three objects, so after accounting for at most two pair-intersection points or joining lines there is still a fresh singleton-pattern witness. Two distinct intersecting lines leave \(q(q-1)\ge2\) points off both, and two distinct points leave \(q(q-1)\ge2\) lines through neither; omitting one previously named object still leaves a witness. In dimension at least three, three lines cover at most \(3(q+1)\) points out of at least \(q^3+q^2+q+1\); three points exclude at most three pencils out of the much larger line set. Consequently every required zero-incidence pattern exists. The same inequalities hold for arbitrary finite projective planes, since only the projective-plane axioms were used.

**3. Uniform two-object extension lemma.** The possible geometric configurations of a third object extending any one- or two-object configuration depend only on the following trichotomy: a plane of order two, a plane of order at least three, or a space of dimension at least three. For two named points, a third point may lie on or off their unique joining line, and a third line may meet zero, one, or both points. For a point and line, a third point may lie on or off the line, and a third line may be chosen through or away from the point, meeting or missing the named line whenever that arrangement is geometrically permitted. For two named lines in a plane all pairs intersect, and a third line is concurrent with them or forms a triangle. In dimension at least three, the original two lines may intersect or be skew; all the expected meet/skew choices of a third line occur.

For completeness, these last assertions need no lower bound stronger than \(q\ge2\). Two intersecting lines span a plane; a line through a point of that plane outside their union and a point outside the plane is skew to both. A line through a nonintersection point of one original line and a point outside the spanned plane meets only that original line. For two skew lines, a line through any pair of points, one on each, meets both. The number of lines skew to both in \(\mathrm{PG}(3,q)\) is \(q(q-1)^2(q+1)>0\): subtract the union of the two collections of lines meeting the originals from the total \((q^2+1)(q^2+q+1)\), using \((q+1)^2\) common transversals. The same choices can be made inside an embedded three-dimensional subspace for \(d>3\). All meet/skew graphs on three lines occur (with concurrency or triangle as the two all-meeting possibilities), by these constructions. The resulting two-prefix extension repertoires are therefore identical throughout each of the three classes.

**4. Four-round back-and-forth.** From Step 2, the one-extension atomic type of a triple depends only on the indicated geometric triple configuration and on its one class from the theorem. Step 3 asserts that the sets of these triple types extending any geometric one- or two-object configuration are the same in any two members of one class. Working backwards through the recursion in Step 1, the resulting rank-two types of pairs, rank-three types of singletons, and rank-four type of the empty tuple are the same. Thus every two members of a class are rank-four equivalent. This uses the real geometric extension lemmas, not extrapolation from finite computations.

**5. Distinguishing the classes.** The rank-three sentence asserting that there exist two distinct lines having no common incident point is true exactly in the dimension-at-least-three class. Among planes, the rank-four sentence asserting the existence of three distinct concurrent lines together with a point avoiding all three is true exactly when \(q\ge3\), by the count \(q(q-2)\). More explicitly, the latter sentence is
\[
\exists \ell_1\exists \ell_2\exists \ell_3\;\bigl(\operatorname{Distinct}(\ell_1,\ell_2,\ell_3)\land\bigwedge_iL(\ell_i)\land [\exists p\;(P(p)\land\bigwedge_i I(p,\ell_i))]\land[\exists z\;(P(z)\land\bigwedge_i\neg I(z,\ell_i))]\bigr).
\]
Its quantifier rank is four because the two innermost existential quantifiers appear in separate conjuncts. It follows that all three classes differ.

**6. Sharp representative bound.** A projective plane of order \(q\) has \(2(q^2+q+1)\) objects; thus the smallest two planar representatives have \(14\) and \(26\) objects. For \(\mathrm{PG}(d,q)\) with \(d\ge3\), the numbers of points and lines increase with both \(d\) and \(q\); the minimum is at \(d=3,q=2\), with \(15\) points and \(35\) lines, hence \(50\) objects. All representatives attain the claimed upper bound, and no smaller representative from \(\mathcal G\) can belong to the third class.

## Verification

`verify_projective_qr4.cpp` enumerates points and lines as normalized vector spans for prime fields and computes exact rank-four Hintikka types, including equality and both sorts. Its dynamic recursion reports three different root types for \(\mathrm{PG}(2,2)\), \(\mathrm{PG}(2,3)\), and \(\mathrm{PG}(3,2)\), with stabilization also observed at \(\mathrm{PG}(2,5)\), \(\mathrm{PG}(3,3)\), and \(\mathrm{PG}(4,2)\). The counts of distinct three-tuple one-extension types are \(48\), \(48\), and \(67\) in the three representative classes, respectively; they are not by themselves proof of cross-field stabilization. `verify_small_projective.py` independently enumerates literal atomic four-tuples for both small planes and checks that their rank-four sentence types differ. See `verification_output.txt` for actual results. The universal part is proved in Steps 2–4 and does not depend on enumeration of unbounded dimensions or orders.

Build and run the C++ verifier with `g++ -O3 -std=c++17 verify_projective_qr4.cpp -o verify_pg && ./verify_pg 2,2 2,3 2,5 3,2 3,3 4,2`; run the independent small checker with `python3 verify_small_projective.py`. Arithmetic in the C++ verifier treats \(q\) as prime, and the supplied test points are prime; prime powers are covered by the geometric proof, not by that program.

## Relationship to prior work

Hirschfeld gives the classical finite projective-space geometry, including line counts and subspace incidence. Venema develops a *modal*, two-sorted point-line logic for projective planes, with completeness, decidability and complexity theorems; his modal language and goals differ from the full first-order four-round classification here. The independent literature on lines and reguli in three-space supplies broader geometric background, not the bounded-rank logical trichotomy. Recent model-theoretic work on all-subspace inclusion and bi-interpretability uses a strictly richer language and does not state this fixed four-quantifier-rank classification. In contrast to uncoloured Levi-graph arguments, naming points and lines makes the exceptional Fano-versus-larger-plane distinction visible at rank four. A previously noted Fano-versus-order-three separator alone does not imply the global three-class statement.

## Limitations

The result is restricted to the explicit point-line-incidence signature, the stated family, and rank four. It does not classify arbitrary partial linear spaces, rank five, arbitrary infinite fields, or structures with named planes/hyperplanes or algebraic operations. Computations verify selected prime-field cases only. Exact coverage by difficult-to-index prior work remains a literature-search risk; no independent audit has been conducted.

## References

1. J. W. P. Hirschfeld, *Projective Geometries over Finite Fields*, second edition, Oxford University Press (1998), DOI: 10.1093/oso/9780198502951.001.0001.
2. Y. Venema, *Points, lines and diamonds: a two-sorted modal logic for projective planes*, *Journal of Logic and Computation* 9 (1999), 601–621, DOI: 10.1093/logcom/9.5.601 (1998 technical report ML-1998-04).
3. J. Cardinal, M. S. Payne, N. Solomon, *Ramsey-type theorems for lines in 3-space*, arXiv:1512.03236 (2015).
4. B. A. Berger, A. G. Myasnikov, *Model Theory of Projective Spaces*, *Algebra and Logic* 63 (2024), 323–348, DOI: 10.1007/s10469-025-09796-z (comparison in a richer signature).
