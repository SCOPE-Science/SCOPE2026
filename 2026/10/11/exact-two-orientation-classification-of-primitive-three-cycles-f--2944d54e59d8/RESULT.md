# Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map

## Finding
Consider the farthest-orthogonal-projection map on the **three complete supporting lines** of a nondegenerate Euclidean triangle with vertices \(A=(0,0)\), \(B=(1,0)\), \(C=(u,v)\), for any \(u\in\mathbb R\) and \(v>0\). Put
\[
a=u^2+v^2,\qquad b=(u-1)^2+v^2,\qquad S=a-u+1>0.
\]
There are at most two primitive periodic orbits of least period three. The clockwise and counterclockwise candidates, respectively, have ordered points
\[
\begin{aligned}
P_0&=(u/S,0),&P_1&=((u+v^2)/S,v(1-u)/S),&P_2&=(u/S,v/S),\\
Q_0&=(a/S,0),&Q_1&=(u^2/S,uv/S),&Q_2&=(a/S,v/S).
\end{aligned}
\]
The \(P\)-orbit exists **if and only if** all three strict inequalities hold:
\[
ab>u^2,\qquad a>(u-1)^2,\qquad b>(a-u)^2.
\]
The \(Q\)-orbit exists **if and only if** all three hold:
\[
ab>(u-1)^2,\qquad b>u^2,\qquad a>(a-u)^2.
\]
The exact number of primitive three-cycles is the number (zero, one, or two) of satisfied triples. Equality in any one of the applicable tests **excludes** that itinerary, because a tie is a fixed point of the map. Each existing cycle is locally attracting, with the absolute multiplier of its fixed-itinerary third iterate equal to the product of the absolute cosines of the triangle's three interior angles.

For the isosceles family \(u=1/2\), there are exactly two primitive three-cycles precisely when
\[
\frac12<v<\sqrt{\frac34+\frac{\sqrt3}{2}},
\]
and none for any other positive \(v\), including the two boundary values. For example, the three-cycle counts for \((u,v)=(1/2,1/4),(-1/5,6/5),(1/2,1)\) are respectively \(0,1,2\).

## Assumptions and scope
Let \(\ell_0=AB\), \(\ell_1=BC\), \(\ell_2=CA\) denote the entire infinite supporting lines, and \(X=\ell_0\cup\ell_1\cup\ell_2\). Given a point on \(\ell_i\), compare the Euclidean distances from the point to its orthogonal projections onto the other two lines; move to the more distant projection, and stay at the starting point when the distances tie. At a vertex, the result is independent of which of its two incident lines is regarded as the source. This is the map defined in Everett's Definition 2.1 on \(X\). No boundary-only map, edge-clipping convention, or upper restriction on \(v\) is imposed. A primitive three-cycle consists of three distinct points \(x_0,x_1,x_2\) with \(T(x_j)=x_{j+1}\) (indices modulo three), and is counted once up to cyclic ordering. The names \(P\) and \(Q\) are orientation labels, not claims about embedding inside the bounded triangle.

## Proof
**1. Only two itineraries.** A nonfixed step is an orthogonal projection onto a supporting line different from that of the incoming step. If an orbit point is a vertex, its two incident lines give zero projection distance, so the nonfixed next step is necessarily to the third line; the label of the preceding target is a valid incoming-line choice. For any nonconstant periodic orbit, label every point by the supporting line targeted by the immediately preceding step. Consecutive labels differ. On the cyclic graph of three transitions, a proper labeling by three line indices must use all three. Therefore a primitive three-cycle traverses either \(\ell_0\to\ell_1\to\ell_2\to\ell_0\) or \(\ell_0\to\ell_2\to\ell_1\to\ell_0\). In particular there is no third possible itinerary, even when one orbit point lies at a vertex.

**2. Uniqueness of a candidate for each itinerary.** Restrict the composition of the three indicated ordinary orthogonal projections to \(\ell_0\). Its Lipschitz factor in the induced Euclidean line metric is
\[
\eta=|\cos\angle A\,\cos\angle B\,\cos\angle C|<1.
\]
Thus this affine composition has exactly one fixed point. Substituting a starting coordinate \((t,0)\) into the three standard projection formulas and solving its affine fixed-point equation gives \(t=u/S\) for \(0\to1\to2\to0\), and \(t=a/S\) for \(0\to2\to1\to0\). Direct projection gives the displayed triples \((P_0,P_1,P_2)\) and \((Q_0,Q_1,Q_2)\). Here \(S=(u-1/2)^2+3/4+v^2>0\), so the formulas exist for all admissible triangles. The strict admissibility inequalities below also ensure that these are three distinct orbit points.

**3. Exact switching tests.** For the \(P\) itinerary, at its successive points the pair of *target squared distance, competing squared distance* is, respectively,
\[
\frac{v^2}{S^2}\left(b,\frac{u^2}{a}\right),\quad
\frac{v^2}{S^2}\left(a,(u-1)^2\right),\quad
\frac{v^2}{S^2}\left(1,\frac{(a-u)^2}{b}\right).
\]
The target lines are \(\ell_1,\ell_2,\ell_0\). The three strict comparisons are exactly \(ab>u^2\), \(a>(u-1)^2\), \(b>(a-u)^2\). Likewise, the successive target-versus-competing distance pairs for \(Q\) are
\[
\frac{v^2}{S^2}\left(a,\frac{(u-1)^2}{b}\right),\quad
\frac{v^2}{S^2}\left(b,u^2\right),\quad
\frac{v^2}{S^2}\left(1,\frac{(a-u)^2}{a}\right).
\]
These produce the three \(Q\)-inequalities. They are individually necessary because ties are fixed by definition, and jointly sufficient because they force all three moves to follow the projected itinerary. Together with Step 1 and the contraction uniqueness from Step 2, this proves completeness and the exact \(0,1,2\) count, with no unstated genericity assumption. Strict inequalities hold on an open neighborhood of an orbit, where its three-step return coincides with the contracting affine composition; this proves local attraction and the stated multiplier.

**4. Sharp isosceles interval.** Put \(u=1/2\) and \(q=v^2+1/4=a=b\). Both tests then reduce to \(q^2>1/4\) and \(q>(q-1/2)^2\) (their middle inequalities are automatic). Since \(v>0\), these are equivalent to \(q>1/2\) and \(q<1+\sqrt3/2\). After solving for \(v\), they give the claimed open interval. At either endpoint the relevant strict comparison is equality, so neither candidate is a period-three orbit.

## Verification
The accompanying standalone `verify.py` uses only Python's standard-library `fractions.Fraction` and exact rational operations. It tests the two displayed candidate orbit formulas against literal farthest-projection map iterations for \(1184\) nondegenerate rational triangles on a stated two-parameter grid; it checks the strict-inequality equivalences, the least period of every accepted orbit, all three count regimes, and example shapes. Running `python3 verify.py` prints `CHECK_OK exact rational triangles: 1184 counts [1138, 18, 28]`. This finite diagnostic independently checks formulas but does **not** replace the proof for all \(u\in\mathbb R,v>0\). The proof uses only exact orthogonal projection, affine contraction and comparisons of squared distances.

## Relationship to prior work
Everett's *A Piecewise Contractive Map on Triangles* defines this global map in Definition 2.1, proves qualitative convergence and discusses odd-period orientation and numerical isosceles bifurcation pictures. It does not supply the two global algebraic three-cycle criteria or their exact critical isosceles heights. Its Section 4 modifies the setting to the **bounded triangle boundary** and hence is not interchangeable with the full-three-line theorem here. The earlier Wang–Zhang *A geometric iterated function system on triangles* concerns an iterated system on the **moduli of triangles**, not periodic points of Everett's farthest-projection map. Classical prescribed alternating projections concern externally fixed selection rules and do not by themselves prove the conditional farthest-choice inequalities.

## Limitations
Only least period three is classified; fixed points and other least periods, their basins, and global dynamics are outside the theorem. Local attraction does not assert global attraction of either cycle. Equalities are excluded by the original tie-as-fixed convention. The classification applies to the union of complete supporting lines; transferring it to a boundary-restricted version requires separate admissibility tests. Publication priority against further unpublished or obscure literature is not guaranteed. Source-publication-date evidence uses the publisher's verified January 7, 2021 online date, not the issue year or the later preprint upload date.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* 18(2) (2020), 183–192, DOI `10.1080/1726037X.2020.1847765`; lawful author preprint arXiv `2408.16019v1` (posted August 26, 2024). Journal publisher records online publication January 7, 2021.
2. Jiajun Wang and Ying Zhang, *A geometric iterated function system on triangles*, arXiv `1605.01794v1` (2016), in particular its introduction and geometric triangle-subdivision construction.
