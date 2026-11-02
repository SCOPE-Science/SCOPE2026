# Four-variable collapse beyond the Fano plane

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge 2\). Regard it as a one-domain relational structure \(\mathfrak I(\Pi)\) whose disjoint domain consists of points and lines, with unary predicates \(P,L\) naming the sorts and a symmetric binary point–line incidence relation \(I\). Equality is available, but neither counting quantifiers nor geometric operations are named. The number of reusable variable symbols is counted **in total across both sorts**.

For any two such planes \(\Pi,\Pi'\) of orders \(q,r\), respectively,
\[
\mathfrak I(\Pi)\equiv_{\mathrm{FO}^{4}}\mathfrak I(\Pi')
\quad\Longleftrightarrow\quad
(q=2\Longleftrightarrow r=2).
\]
There are therefore exactly **two** unrestricted-quantifier-depth four-variable theories in this family: the Fano-plane class and the class of every plane of order at least three. Representatives of minimum size have 14 and 26 elements, respectively. Every pair of these planes, including the Fano plane, is equivalent in \(\mathrm{FO}^{3}\).

A sharp variable-width consequence is that the minimum number of variables separating an order-two plane from one of larger order is four, while the minimum separating an order-three plane from a plane of order at least four is five. The latter five-variable separation is a simple point-covering statement; the new substantive assertion is equivalence **at all quantifier depths** using four variables for *arbitrary* planes of orders at least three, without assuming Desargues' theorem.

## Assumptions and scope
A finite projective plane of order \(q\) has \(q^2+q+1\) points, the same number of lines, \(q+1\) points on each line and \(q+1\) lines through each point. Any two distinct points determine exactly one line, and any two distinct lines meet in exactly one point. This includes all finite non-Desarguesian planes if they exist at the indicated order. We assume \(q\ge2\), so no degenerate planes occur. Incidence is interpreted as symmetric and false on same-sort pairs. The finite-variable fragment uses at most four distinct variable **names**, allowing quantifiers to reuse names indefinitely. The theorem does not concern counting logic.

## Proof
**Enhanced diagrams.** For a tuple of at most four pebbled objects, record their sorts, equality pattern, all point–line incidences, whether each three *distinct* pebbled points are collinear, and whether each three *distinct* pebbled lines are concurrent. We prove that for planes of any orders \(q,r\ge3\), a matching enhanced diagram of at most three anchored objects admits exactly the same possible enhanced diagrams after adding any fourth object (of either sort). Multiplicities need not agree; only whether each extension type is nonempty matters.

It is enough to consider three distinct anchors. Permutation of anchors and point–line duality reduce the configurations to (a) three collinear points, (b) three noncollinear points, and (c) two distinct points \(A,B\) together with a line \(\ell\), containing respectively two, one or zero of the points. Repeated anchors reduce to the elementary zero-, one- and two-distinct-anchor cases, whose realization counts are positive for all \(q\ge2\). All counts below exclude a new object coinciding with an existing same-sort anchor; coincident choices themselves are always reproducible by equality.

**Case (a): three collinear points.** Let \(J\) be their common line. The numbers of new points on and off \(J\) are respectively \(q-2\) and \(q^2\). The numbers of new lines incident with all three anchors, with exactly a specified one anchor, and with none are, respectively, \(1\), \(q\), and \(q(q-2)\). A line incident with exactly two anchors is impossible. All the permitted categories are nonempty when \(q\ge3\).

**Case (b): three noncollinear points.** A new point lies on exactly one of the three pair-joining lines in \(q-1\) ways for each specified pair, and on none of these lines in \((q-1)^2\) ways. A new line passes through exactly a specified two anchors in one way, through exactly a specified one anchor in \(q-1\) ways, and through none in \((q-1)^2\) ways. There are no other possibilities. All displayed counts are positive for \(q\ge2\).

**Case (c): two points and one line.** Set \(J=AB\), and let \(h\in\{0,1,2\}\) be the number of these two points on \(\ell\). When \(h=1\), interchange the two anchor points so that \(A\in\ell\). For a fresh point \(X\notin\{A,B\}\), its enhanced extension is determined by the two indicators \((X\in\ell,X\in J)\), with the following exact counts:

| \(h\) | \((1,1)\) | \((1,0)\) | \((0,1)\) | \((0,0)\) |
| --- | ---: | ---: | ---: | ---: |
| \(2\) | \(q-1\) | \(0\) | \(0\) | \(q^2\) |
| \(1\) | \(0\) | \(q\) | \(q-1\) | \(q(q-1)\) |
| \(0\) | \(1\) | \(q\) | \(q-2\) | \(q(q-1)\) |

For a fresh line \(m\ne\ell\), its enhanced extension is determined by \((A\in m,B\in m)\):

| \(h\) | \((1,1)\) | \((1,0)\) | \((0,1)\) | \((0,0)\) |
| --- | ---: | ---: | ---: | ---: |
| \(2\) | \(0\) | \(q\) | \(q\) | \(q(q-1)\) |
| \(1\) | \(1\) | \(q-1\) | \(q\) | \(q(q-1)\) |
| \(0\) | \(1\) | \(q\) | \(q\) | \(q(q-1)-1\) |

These counts follow from the unique intersection \(\ell\cap J\), the \(q+1\) elements of each line or pencil, and the total \(q^2+q+1\). Their zero/nonzero patterns are identical for all \(q\ge3\). Point–line duality supplies the three-line and one-point/two-line cases. For fewer than three distinct anchors, the patterns depend only on whether the anchors are equal, incident, or of the same sort; every geometrically permitted category has a positive count at all orders \(q\ge2\).

**Permanent four-pebble strategy.** Pair the empty positions. If a player moves a pebble, discard its previous position; at most three anchored pairs remain. Their enhanced diagrams agree by induction. The support classification just proved supplies a matching reply for the new point or line, restoring equality of the full enhanced four-object diagrams. This works with moves in either structure and with repeated pebble positions. The enhanced diagram includes all atomic predicates, so each resulting position is a partial isomorphism. The strategy lasts arbitrarily many rounds. By the standard finite-variable pebble-game theorem, every two planes of orders at least three satisfy the same \(\mathrm{FO}^{4}\) sentences of **unbounded** quantifier depth.

**Separation and sharpness.** A plane of order two has three distinct concurrent lines covering all its seven points. For every \(q\ge3\), the union of any three lines has at most \(3q+1<q^2+q+1\) points. Consequently the four-variable, quantifier-rank-four sentence
\[
\exists x\,\exists y\,\exists z\,\Bigl(
L(x)\land L(y)\land L(z)\land x\ne y\land x\ne z\land y\ne z
\land\forall w\bigl(P(w)\rightarrow(I(w,x)\lor I(w,y)\lor I(w,z))\bigr)
\Bigr)
\]
separates order two from every larger order. With only three pebbles, equality, sorts and pairwise incidence already form a permanent invariant: after at most two anchors every required point/line incidence pattern has a fresh witness at all orders \(q\ge2\), by the point-joining, line-meeting and \(q+1\)-regularity axioms. Hence no three-variable sentence separates any two planes.

Finally, in an order-three plane four concurrent lines cover all 13 points; in every plane of order \(q\ge4\), any four lines cover at most \(4q+1<q^2+q+1\). The analogous five-variable covering sentence separates order three from all higher orders. Combined with the permanent four-pebble strategy, this proves the stated minimum width of five for that comparison; it does **not** purport to classify the full five-variable theory.

## Verification
Two standalone, independent finite checkers accompany this result. `support_refinement.py` constructs classical projective planes of orders \(2,3,4,5,7\) and tabulates every enhanced three-anchor extension support; it exhausts all ordered triples for the first three orders and checks representatives for the latter two. It reports 48 enhanced three-anchor types in each order and respectively 400 versus 410 supported extension patterns for order two versus any checked order at least three; there are zero support differences among the checked orders three through seven. `extension_count_audit.py` uses an independent affine-plus-infinity coordinatization and verifies the displayed symbolic category counts across the same five orders, including the field of order four. Both run under Python 3 using only the standard library. Recorded outputs are provided verbatim. These computations test, but cannot replace, the arbitrary-plane proof above.

## Relationship to prior work
Venema's *Points, Lines and Diamonds* studies a two-sorted **modal** language of projective planes, proving modal completeness, decidability and complexity results, not this finite-model-theoretic classification of four-variable first-order sentences. Grohe and Otto's *Pebble Games and Linear Equations* supplies a precise general four-pebble methodology without a projective-plane application of this form. De Winter, Lazebnik and Verstraëte characterize projective planes through extremal incidence-graph cycle counts; their theorem concerns a different invariant.

Related bounded-quantifier-rank classifications distinguish orders \(2,3,\ge4\) at five rounds in the named-sort incidence language, and other results establish shorter-rank equivalences or three-variable equivalences. None of those **statements** entails equality of all unrestricted-depth four-variable theories for orders at least three. Conversely, the present theorem does not settle the five-variable theory for orders at least four. Literature searches have not excluded every stronger result under alternative terminology; historical priority remains qualified.

## Limitations
The theorem applies only to finite projective planes of order at least two, in the pure point/line-sorted incidence language with equality and **no counting quantifiers**. Sorts are named and all variable names are counted together. It does not extend by assertion to partial planes, higher-dimensional projective spaces, named individual points/lines, enrichment by collinearity as a primitive relation, or five-variable equivalence. The concrete verification runs concern Desarguesian coordinate planes; arbitrary-plane validity relies on the combinatorial counting argument, not computations. Historical uniqueness and independent mathematical audit are not established.

## References
1. Y. Venema, *Points, lines and diamonds: a two-sorted modal logic for projective planes*, Journal of Logic and Computation 9(5), 601–621 (1999). DOI: 10.1093/logcom/9.5.601. Author manuscript: https://staff.science.uva.nl/y.venema/papers/vene-poin99.pdf.
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, first arXiv version 2012-04-09, arXiv:1204.1990, DOI: 10.4230/LIPIcs.CSL.2012.289. https://arxiv.org/abs/1204.1990.
3. S. De Winter, F. Lazebnik and J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics 15 (2008), R143. DOI: 10.37236/867. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1r143.
