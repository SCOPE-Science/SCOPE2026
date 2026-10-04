# Sharp signed-area amplification for ordered points in a convex set
## Finding
Let \(H\subseteq\mathbb{R}^2\) be a convex set of finite area and let \(P_0,\ldots,P_{m-1}\in H\), with \(m\ge3\), be an arbitrary cyclically ordered list. Repeated point locations are allowed. Put \(P_m=P_0\) and
\[
F(P)=\frac12\sum_{i=0}^{m-1} P_i\times P_{i+1},
\]
where \(u\times v\) denotes the planar determinant. Then
\[
|F(P)|\le \left\lfloor\frac m3\right\rfloor\operatorname{area}(H).
\]
For every \(m\ge3\), the coefficient \(\lfloor m/3\rfloor\) is best possible.

Equivalently, if \(C_m\) is the least constant such that every ordered \(m\)-point list in every planar convex set satisfies \(|F(P)|\le C_m\operatorname{area}(H)\), then
\[
C_m=\left\lfloor\frac m3\right\rfloor.
\]

## Assumptions and scope
The result concerns the signed shoelace expression of an arbitrary ordered list of points constrained only to lie in one planar convex set. It permits self-intersections, degeneracies, and repeated point locations. If \(H\) has zero area, all its points are collinear and the claim is immediate; infinite-area sets are excluded only to keep the stated ratio finite.

The motivating source proves the factor-one inequality for lists of three, four, or five points and observes that factor one fails for six points by traversing a triangle twice. The present result determines the exact optimal factor for every list length. It does not by itself improve the numerical bounds in the motivating universal-cover problem; rather, it supplies a sharp unconditional baseline for longer shoelace certificates when the stronger fan or separating-chord hypotheses are unavailable.

## Proof
The proof uses the small-polygon bound from Keller, arXiv:2609.21968v1: if \(3\le r\le5\) and \(Q_0,\ldots,Q_{r-1}\in H\) are in arbitrary order, then
\[
F(Q)\le\operatorname{area}(H).
\]
Applying the same statement to the reversed list gives
\[
|F(Q)|\le\operatorname{area}(H)
\]
for \(3\le r\le5\).

We prove the upper bound by induction on \(m\). The cases \(m=3,4,5\) are exactly the small-polygon bound. Suppose \(m\ge6\). Delete the three consecutive entries \(P_1,P_2,P_3\), and let
\[
Q=(P_0,P_4,P_5,\ldots,P_{m-1}),
\]
which has \(m-3\) entries. Only the edge from \(P_0\) to \(P_4\) changes. Direct subtraction of the shoelace sums gives
\[
F(P)-F(Q)
=\frac12\bigl(P_0\times P_1+P_1\times P_2+P_2\times P_3+P_3\times P_4+P_4\times P_0\bigr).
\]
The right-hand side is exactly the signed shoelace expression of the five-point list \((P_0,P_1,P_2,P_3,P_4)\). Therefore the small-polygon bound yields
\[
F(P)-F(Q)\le\operatorname{area}(H).
\]
By induction,
\[
F(Q)\le\left\lfloor\frac{m-3}{3}\right\rfloor\operatorname{area}(H).
\]
Consequently
\[
F(P)\le\left(1+\left\lfloor\frac{m-3}{3}\right\rfloor\right)\operatorname{area}(H)
=\left\lfloor\frac m3\right\rfloor\operatorname{area}(H).
\]
Reversing the full cyclic list changes \(F(P)\) to \(-F(P)\), so the same one-sided estimate gives the absolute-value bound.

For sharpness, write \(m=3q+r\) with \(q=\lfloor m/3\rfloor\) and \(r\in\{0,1,2\}\). Take \(H\) to be a nondegenerate triangle with counterclockwise vertices \(A,B,C\). Traverse \((A,B,C)\) counterclockwise exactly \(q\) times. This contributes \(q\operatorname{area}(H)\) to the signed area. If \(r>0\), insert \(r\) consecutive repeated copies of any existing vertex. Such an insertion replaces one determinant term by a zero determinant plus the same original determinant, so it does not change \(F(P)\). Thus an \(m\)-entry list attains
\[
|F(P)|=q\operatorname{area}(H)=\left\lfloor\frac m3\right\rfloor\operatorname{area}(H),
\]
proving optimality.

## Verification
The induction step is an exact algebraic identity: deleting three consecutive vertices changes the shoelace sum by precisely one five-point shoelace sum. The base cases are the published three-to-five-point bound. Reversal verifies the negative side, and repeated-vertex insertion verifies sharpness for all three residue classes of \(m\) modulo \(3\). No numerical experiment or limiting argument is used in the proof.

## Relationship to prior work
Keller's September 2026 preprint proves the factor-one inequality for arbitrary ordered lists only for \(3\le m\le5\). It explicitly notes that the analogous factor-one statement fails already at \(m=6\), using a twice-traversed triangle, and then imposes fan or separating-chord conditions to recover factor one for selected longer lists. The present theorem instead asks for the optimal unconditional coefficient as a function of \(m\) and gives the complete sequence \(C_m=\lfloor m/3\rfloor\).

A classical result of Fáry and Makai, as summarized and compared in Vysotsky's 2025 open-access treatment of polygonal-line convexification, says that reordering the edge vectors into a convexification does not decrease absolute signed area. That statement does not keep the convexified vertices inside the original containing set \(H\), so it does not imply a bound by \(\operatorname{area}(H)\) with a coefficient depending only on the number of listed vertices.

Targeted searches for the exact coefficient, algebraic-area aliases, self-intersecting polygons in convex bodies, and the Keller small-polygon lemma found no published statement implying the all-\(m\) sharp formula. The main residual risk is terminological: an equivalent elementary inequality may exist in older polygonal-line literature under different language.

## Limitations
The theorem controls signed area, not the sum of absolute lobe areas or the area of the geometric union of a self-intersecting polygonal line. Repeated point locations are used to attain equality for \(m\not\equiv0\pmod3\); if all listed points are required to be distinct, the same constant remains a sharp supremum by arbitrarily small perturbations, but exact attainment is not asserted here.

The result is an unconditional sharp baseline. It does not replace the stronger factor-one estimates obtainable from geometric fan or chord-decomposition hypotheses, and it does not claim a new numerical bound for Moser's worm problem.

## References
1. Ethan Keller, “Improved bounds for universal convex covers of unit arcs,” arXiv:2609.21968v1, 18 September 2026. Section 3.3, especially Lemma 3.3 and the discussion immediately following it.
2. Vladislav Vysotsky, “The isoperimetric problem for convex hulls and large deviations rate functionals of random walks,” Stochastic Processes and their Applications 180 (2025), 104519, DOI: 10.1016/j.spa.2024.104519. Its appendix summarizes the Fáry–Makai signed-area convexification lemma.
3. István Fáry and Endre Makai Jr., “Isoperimetry in variable metric,” Studia Scientiarum Mathematicarum Hungarica 17 (1982), 143–158.
