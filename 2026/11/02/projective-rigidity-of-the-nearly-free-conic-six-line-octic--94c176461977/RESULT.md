# Projective rigidity of the nearly free conic–six-line octic

## Finding
Let \(\mathcal A\subset\mathbb P^2_{\mathbb C}\) be the reduced union of **one smooth conic and six distinct lines**, with no singularities other than nodes (\(A_1\)), tacnodes (\(A_3\)), and ordinary transverse triple points (\(D_4\)). If \(\mathcal A\) is nearly free, then its singularity counts are necessarily
\[
(n_2,t,n_3)=(3,3,6),
\]
and it belongs to **exactly one projective-equivalence class**. In fact, every arrangement of this component type with this singularity basket belongs to that class, whether or not near freeness is initially assumed.

A representative is \(F_r=0\), where
\[
\begin{aligned}
F_r&=xyz(y-z)(x-z)(x-r y)Q_r,\\
Q_r&=u^2x^2+v^2y^2+z^2-2uvxy-2uxz-2vyz,\\
u&=\frac{r+3}{3r+1},\qquad v=\frac{(r-1)^2}{2(3r+1)},\qquad r^2-18r+1=0.
\end{aligned}
\]
The two roots \(r=9\pm4\sqrt5\) yield projectively equivalent **unmarked** arrangements, exchanged by interchanging \(x\) and \(y\). The existence and near freeness of this representative (exponents \((4,4)\)) were previously established; the new assertion is the converse classification and projective rigidity.

## Assumptions and scope
The ground field is \(\mathbb C\). Every conic is smooth and irreducible; all six lines are distinct. At an ordinary triple point the three smooth local branches have distinct tangents. Projective equivalence means equivalence under \(\mathrm{PGL}_3(\mathbb C)\), with the line components **unlabeled**. No claim is made about arrangements containing more conics or about degree-nine nearly free arrangements.

## Proof

**1. Numerical necessity.** Let \(m=8\), and \(s=\operatorname{mdr}(F)\). The published lower bound for arrangements with these singularities gives \(s\ge 2m/3-2\), so \(s\ge4\). Near freeness gives \(s\le m/2=4\), hence \(s=4\). The near-free Tjurina identity then gives
\[
\tau= s^2-s(m-1)+(m-1)^2-1=36.
\]
Bézout's formula for one conic and six lines gives
\[
27=n_2+2t+3n_3,\qquad36=n_2+3t+4n_3.
\]
Consequently \(t+n_3=9\) and \(n_2=9-n_3\). The published orbifold inequality \(8+n_2+\tfrac34 n_3\ge6+\tfrac52 t\) gives \(9n_3\ge46\), hence \(n_3\ge6\).

**2. Separate the line-only triple points.** Let \(A\) be the number of intersections of three lines, and \(B\) the number of triple points comprising one conic branch and two line branches. Thus \(A+B=n_3\). Let \(N_{CL}\) count conic–line nodes. Because every tacnode involves the conic and one line, Bézout on the six conic–line pairs gives
\[
12=2B+2t+N_{CL},\qquad N_{CL}=2A-6.
\]
Thus \(A\ge3\). In a six-line arrangement with only double and triple intersections, a line can contain at most two line-only triple points (each consumes two of its five intersections with other lines). Hence \(A\le5\); equality would use all fifteen line pairs and leave each line incident with an odd number five of pair partners accounted for in pairs, impossible. Thus \(A=3\) or \(A=4\).

If \(A=4\), all six lines pass through exactly two of the four triple points, and they are exactly the six connecting lines of a complete quadrangle. Their three residual line-only nodes are the intersections of the three disjoint opposite-edge pairs. Since \(B=n_3-4\ge2\), the conic passes transversely through at least two of those residual nodes. These involve \(2B\) different lines, each now having precisely one conic intersection, so each requires a second, distinct conic–line node. This forces \(N_{CL}\ge2B\ge4\), contrary to \(N_{CL}=2\). Therefore \(A=3\) and \(N_{CL}=0\).

**3. Force the entire incidence graph.** For three line-only triple points, the nine line incidences must be supported on six lines, with each line containing at most two triple points. Therefore the three pairs of triple points are joined by three of the arrangement lines, and the remaining three lines pass individually through exactly one of the triple points. Indeed, fewer than three lines shared by pairs of triple points would require at least seven lines. The triple points cannot be collinear, since a line through all three would itself use six other pair partners and again require at least seven lines. The six-line arrangement is thus a triangle of three *connector* lines plus one *leaf* line through each triangle vertex.

Its six line-only double points have graph the triangle on the three leaf lines, with one additional pendant edge connecting each leaf to the one connector that does not meet it at a pure line triple point. Since \(N_{CL}=0\), every leaf or connector is either tangent to the conic (no conic–line triple point on it) or passes transversely through exactly two distinct conic–line triple points. The \(B\) line-only nodes on the conic therefore form a two-regular subgraph of the line-only double-point graph. This graph has **one cycle only**, namely the triangle on the leaves. Hence \(B=3\), the conic goes through precisely the three pairwise intersections of the leaf lines, and it is tangent to the three connector lines. Therefore \(n_3=A+B=6\), \(t=3\), and \(n_2=3\).

The graph assertion can be checked directly: two connectors meet only at pure line triple points; two leaves meet at ordinary double points; each connector meets its own incident leaf at a pure triple point and its sole nonincident leaf at a double point. The only cycle in the double-point graph is the three-leaf triangle.

**4. Projective normal form and finite rigidity.** Three distinct tangents to a smooth conic cannot be concurrent (through a point there are at most two tangents). Map the connector triangle to the coordinate axes. Diagonal coordinate rescalings and scalar changes of equations then send the three leaf lines to
\[
y-z=0,\qquad x-z=0,\qquad x-r y=0
\]
for some \(r\ne0,1\). The three leaf intersections are \([1:1:1]\), \([r:1:1]\), and \([r:1:r]\).

A nonsingular conic tangent to all three coordinate axes can, after scaling, be written as
\[
Q=u^2x^2+v^2y^2+z^2-2uvxy-2uxz-2vyz,\qquad uv\ne0.
\]
For completeness, the three axis tangencies make all three principal \(2\times2\) minors of its symmetric matrix vanish. Smoothness forces the product of the three off-diagonal coefficients to be the *negative* product of the diagonal coefficients, giving exactly this form after choosing signs and a scalar.

Substituting the three leaf intersections into \(Q\) yields three equations \(E_1=E_2=E_3=0\). Their differences are
\[
E_2-E_1=u(r-1)((r+1)u-2v-2),
\]
\[
E_3-E_2=-(r-1)(2ru-r+2v-1).
\]
Since \(r\ne1\) and \(u\ne0\), these force
\[
u=\frac{r+3}{3r+1},\qquad v=\frac{(r-1)^2}{2(3r+1)}.
\]
The case \(3r+1=0\) is inconsistent with the same linear equations. Substituting into \(E_1\) gives
\[
E_1=\frac{(r-1)^2(r^2-18r+1)}{4(3r+1)^2}=0.
\]
Thus \(r=9\pm4\sqrt5\), and the conic is uniquely determined once \(r\) is fixed. These roots are reciprocal. Interchanging \(x\) and \(y\) exchanges the leaves \(y-z\) and \(x-z\), sends \(x-r y\) to a scalar multiple of \(x-r^{-1}y\), and exchanges the corresponding \(u\) and \(v\); hence the two solutions are projectively equivalent.

**5. Existence.** For either root, \(uv\ne0\) and the symmetric matrix of \(Q\) has determinant \(-4u^2v^2\ne0\). Its restrictions to the coordinate axes are \((vy-z)^2\), \((ux-z)^2\), and \((ux-vy)^2\), giving the three prescribed tacnodes. It passes through the three pairwise leaf intersections and avoids the other six points of the six-line singular set; Bézout gives exactly the claimed basket. The published exact Jacobian calculation for this same representative gives \(\operatorname{mdr}=4\), and the numerical criterion gives near freeness with exponents \((4,4)\). That existence computation is attributed to the previous result, not claimed new. Combined with Steps 1–4, this completes the classification.

## Verification
The standalone Python/SymPy script `verify_rigidity.py` exhaustively checks the allowed size-three and size-four hypergraphs of pure line triple points (120 and 30 labeled configurations); it finds exactly the predicted cycle and opposite-edge structures. It verifies the explicit conic-incidence equations, their elimination factor, smoothness determinant, tangency-square restrictions, avoidance of the six other line singularities, and reciprocity of the two roots by exact algebra over \(\mathbb Q[r]/(r^2-18r+1)\). It also checks the numerical near-free identities. Its terminal marker is `RIGIDITY_REPLAY_OK`. The full classification is proved by the argument above; the finite hypergraph replay is a consistency check. The earlier exact Jacobian rank calculation is imported solely for the already-published existence half.

## Relationship to prior work
Gałecka's 2022 article derives the near-free numerical constraints but leaves degree-eight existence open. Dimca–Pokora classify **free**, not nearly free, arrangements and exclude six-line conic–line free cases. A previous research result (publicly available 4 October 2026) constructs precisely one degree-eight nearly free arrangement with basket \((3,3,6)\), using a parameter satisfying \(r^2-18r+1=0\); its statement expressly does **not** classify all degree-eight arrangements. The present theorem proves that no other basket or projective class is possible for one conic plus six lines, so it is not another construction or a numerical corollary of the prior existence result.

## Limitations
The theorem does not classify eight-degree arrangements with two or three conics, nor degree-nine arrangements. It classifies projective equivalence over \(\mathbb C\) with unlabeled lines, not forms over arbitrary ground fields. The near-freeness of the representative uses the prior exact syzygy calculation and the published near-free criterion; no new computation of the minimal Jacobian relation degree is claimed. As with any originality search, an unindexed earlier uniqueness theorem remains a priority risk.

## References
1. A. Gałecka, “On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points,” first preprint arXiv:2204.13969 (29 April 2022), Boletín de la Sociedad Matemática Mexicana 28 (2022), article 67, DOI 10.1007/s40590-022-00461-4. Full text: https://link.springer.com/article/10.1007/s40590-022-00461-4.
2. A. Dimca and P. Pokora, “On conic-line arrangements with nodes, tacnodes, and ordinary triple points,” arXiv:2111.12349v1 (first public 24 November 2021), Journal of Algebraic Combinatorics 56 (2022), 403–424, DOI 10.1007/s10801-022-01116-3. Full text: https://link.springer.com/article/10.1007/s10801-022-01116-3.
3. “A degree-eight nearly free conic-line arrangement over a quadratic field,” publicly indexed research record, 4 October 2026, identifier `2026/10/4/SCOPE-a-degree-eight-nearly-free-conic-line-arrangement-over-a-quadrat--2edf9ed667f2`, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-degree-eight-nearly-free-conic-line-arrangement-over-a-quadrat--2edf9ed667f2. Its exact existence and syzygy computations are expressly credited above.
