# Height determines the Euclidean inradius and centers of every order polytope
## Finding
Let \(P\) be a nonempty finite poset, and let its height \(h\) be the number of elements in a longest chain. For the order polytope
\[
\mathcal O(P)=\{x\in[0,1]^P:x_p\le x_q\text{ whenever }p<q\},
\]
with the standard Euclidean metric of \(\mathbb R^P\), the inradius is
\[
 r(\mathcal O(P))=\frac{1}{2+(h-1)\sqrt2}.
\]
Thus the inradius depends only on the poset height, even though the facial and enumerative geometry of order polytopes can depend on much finer structure.

The full Chebyshev-center set is also explicit. Put
\[
 r=\frac{1}{2+(h-1)\sqrt2}.
\]
Then a vector \(c\in\mathbb R^P\) is a center of a largest inscribed Euclidean ball if and only if
\[
 r\le c_p\le1-r\quad(p\in P),\qquad
 c_q-c_p\ge\sqrt2\,r\quad(p\prec q),
\]
where \(p\prec q\) denotes a cover relation.

For \(p\in P\), let \(d_-(p)\) be the largest number of cover edges in a saturated chain from a minimal element to \(p\), and let \(d_+(p)\) be the largest number of cover edges in a saturated chain from \(p\) to a maximal element. Two canonical centers are
\[
 L_p=r\bigl(1+\sqrt2\,d_-(p)\bigr),\qquad
 U_p=1-r\bigl(1+\sqrt2\,d_+(p)\bigr).
\]
The largest-ball center is unique if and only if every element of \(P\) lies on a longest chain; equivalently,
\[
 d_-(p)+d_+(p)=h-1\qquad\text{for every }p\in P.
\]

## Assumptions and scope
The poset is finite and nonempty. Height counts elements, so a one-element poset has \(h=1\). Distances are the ordinary coordinate Euclidean distances in \(\mathbb R^P\). The result concerns the standard order-polytope realization, not arbitrary affine images, other norms, or the chain polytope.

## Proof
The order polytope is the intersection of the coordinate halfspaces \(x_p\ge0\), \(x_p\le1\), and the cover halfspaces \(x_q-x_p\ge0\) for \(p\prec q\). The normal of a coordinate halfspace has Euclidean norm \(1\), while the normal \(e_q-e_p\) of a cover halfspace has norm \(\sqrt2\).

Suppose a closed Euclidean ball of radius \(\rho\), centered at \(c\), lies in \(\mathcal O(P)\). Then every coordinate satisfies
\[
 \rho\le c_p\le1-\rho,
\]
and every cover satisfies
\[
 c_q-c_p\ge\sqrt2\,\rho.
\]
Choose a longest chain \(p_1<\cdots<p_h\). It is saturated, and its endpoints are respectively minimal and maximal. Summing along its \(h-1\) covers gives
\[
 (h-1)\sqrt2\,\rho\le c_{p_h}-c_{p_1}\le1-2\rho.
\]
Hence
\[
 \rho\le\frac{1}{2+(h-1)\sqrt2}=r.
\]

For the reverse inequality, define \(L_p=r(1+\sqrt2\,d_-(p))\). Since \(0\le d_-(p)\le h-1\),
\[
 r\le L_p\le r\bigl(1+(h-1)\sqrt2\bigr)=1-r.
\]
If \(p\prec q\), then a longest saturated chain ending at \(p\), followed by that cover, shows \(d_-(q)\ge d_-(p)+1\). Therefore
\[
 L_q-L_p\ge\sqrt2\,r.
\]
So the distance from \(L\) to every defining halfspace boundary is at least \(r\), and the closed Euclidean ball \(B(L,r)\) lies in \(\mathcal O(P)\). This proves the inradius formula.

The same normalized-distance argument shows that a vector \(c\) is a largest-ball center exactly when it satisfies the displayed coordinate and cover inequalities. Defining \(U_p=1-r(1+\sqrt2\,d_+(p))\) gives a second feasible center by the dual argument.

Finally, any largest-ball center obeys
\[
 L_p\le c_p\le U_p.
\]
The lower inequality follows by summing the cover gaps along a longest saturated chain from a minimal element to \(p\); the upper inequality follows dually. Thus the center is unique precisely when \(L_p=U_p\) for every \(p\), namely when \(d_-(p)+d_+(p)=h-1\) for every \(p\). Concatenating longest prefix and suffix chains shows that this equality holds exactly when \(p\) lies on a longest chain.

## Verification
A standalone standard-library checker enumerates every distinct naturally labelled poset on at most six elements by taking transitive closures of all acyclic relations compatible with the natural order. This covers every isomorphism type after relabelling by a linear extension. For all \(5231\) resulting posets, it reconstructs the cover relation, height, the two depth functions, the two canonical centers, the cover margins, and the uniqueness criterion. It reports

`VERIFY_OK order-polytope inradius posets=5231 n=1..6`

The finite computation is corroboration only. The arbitrary finite-poset theorem is proved above from the halfspace distances and a longest-chain argument.

## Relationship to prior work
Stanley's foundational paper *Two Poset Polytopes* defines the standard Euclidean realization and proves that the facets of an order polytope are controlled by minimal elements, maximal elements, and cover relations. That facet description is the geometric input used here. The full text was inspected and contains no occurrence of “inradius”, “Chebyshev”, or “ball”.

The 2021 preprint *Triangulations, order polytopes, and generalized snake posets* (arXiv:2102.11306; first public 2021-02-22) is a modern geometry paper centered on order polytopes; its published record lists MSC 52B20 first. Its full text was inspected for metric-radius terminology and contains no occurrence of “inradius”, “Chebyshev”, “Euclidean”, or “ball”. Its results concern volume, circuits, flips, and triangulations rather than largest inscribed Euclidean balls.

The full text of Ahmad--Fourier--Joswig, *Order and chain polytopes of maximal ranked posets* (arXiv:2309.01626), was also inspected. It studies face vectors and chain-order interpolations and contains no occurrence of “inradius”, “Chebyshev”, or “Euclidean”. published-finding corpus searches over the claim, aliases, height, cover relations, and Chebyshev-center formulations found no statement implying the formula or the center classification.

The general Chebyshev-center reduction for a polyhedron \(a_i^Tx\le b_i\) is standard: the largest Euclidean ball is obtained by maximizing \(r\) subject to \(a_i^Tc+r\lVert a_iVert_2\le b_i\). That general optimization template does not itself give the height-only optimum or describe the full optimal-center set for order polytopes; those conclusions require solving the specialized difference-constraint system and proving its longest-chain rigidity.

## Limitations
The theorem is metric-dependent: a general affine image of an order polytope need not have the same Euclidean inradius. No claim is made about chain polytopes, other norms, John ellipsoids, or circumradii. Literature searches cannot exclude every unindexed thesis, book passage, or differently worded result; the main residual originality risk is an older metric treatment of order polytopes under terminology not captured by the inspected sources and searches.

## References
1. R. P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9--23, DOI 10.1007/BF02187680.
2. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez, and M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306; Combinatorial Theory 2(3) (2022), Article 10.
3. I. Ahmad, G. Fourier, and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626.
4. S. Boyd and L. Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004, Section 4.3.1 (Chebyshev center of a polyhedron).
