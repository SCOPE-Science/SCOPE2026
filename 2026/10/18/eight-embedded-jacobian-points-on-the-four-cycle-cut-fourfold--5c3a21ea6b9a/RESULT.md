# Eight embedded Jacobian points on the four-cycle cut fourfold

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic. Let \(X\subset\mathbb P^7_k\) be the projective cut variety of the graph \(C_4\). In paired homogeneous coordinates \((x_i,y_i)_{i=1}^4\), its homogeneous ideal is
\[
I_X=(x_1y_1-x_2y_2,\;x_1y_1-x_3y_3,\;x_1y_1-x_4y_4).
\]
Let \(\Sigma\subset X\) be the **scheme-theoretic singular locus**, defined by the maximal minors of the Jacobian matrix of these three equations (and projectively sheafified). Then its nilradical is a square-zero skyscraper sheaf of length eight:
\[
0\longrightarrow\bigoplus_{i=1}^{4}\bigl(k_{P_{x_i}}\oplus k_{P_{y_i}}\bigr)
\longrightarrow\mathcal O_\Sigma\longrightarrow\mathcal O_{\Sigma_{\mathrm{red}}}\longrightarrow0,
\]
where \(P_{x_i},P_{y_i}\) are the eight coordinate points. In particular \(\Sigma\) has exactly eight isolated embedded associated points, each of embedded length one, and is otherwise reduced.

The reduced support, **already determined more generally for cycle cut toric varieties**, is the union of the 24 coordinate lines spanned by coordinate points belonging to distinct pairs. It has degree \(24\) and arithmetic genus \(17\), whereas the **full Jacobian singular scheme** has the same degree but arithmetic genus \(9\). At a general point of each line the transverse local equation is the threefold ordinary double point \(ab-cd=0\). At each coordinate point the reduced singular support has six coordinate-axis branches; precisely one infinitesimal embedded point is added by the Jacobian scheme.

## Assumptions and scope
The base field is algebraically closed, with no characteristic restriction. Subscripts \(i,j\) range over \(\{1,2,3,4\}\). Each pair consists of two independent homogeneous coordinates \(x_i,y_i\), and \(z_i=x_i y_i\). The Jacobian singular scheme uses the \(3\times3\) minors of the \(3\times8\) matrix of partial derivatives because \(X\) is a codimension-three complete intersection. The phrase embedded length one means the length of the local nilradical as a module at the specified closed point; it is **not** a claim that the entire singular scheme has finite length.

## Proof
**1. Prior defining equations.** Sturmfels and Sullivant, Example 1.2, give the three quadratic binomial generators of the four-cycle cut ideal. Relabel their eight cut coordinates as four pairs to obtain exactly \(I_X\) above. Their toric construction proves \(X\) is integral. Since the generators form a codimension-three complete intersection, the Jacobian criterion applies to the displayed matrix over every algebraically closed field.

**2. Exact Jacobian-minor ideal.** Set \(z_i=x_i y_i\). Every derivative column belonging to the \(i\)-th pair is its opposite coordinate multiplied by one of the four vectors
\[
(1,1,1),\quad(-1,0,0),\quad(0,-1,0),\quad(0,0,-1).
\]
Any three vectors with distinct indices have determinant \(\pm1\); two columns from one pair are proportional. Therefore the maximal minors generate **exactly** the 32 squarefree-in-groups cubic monomials
\[
T=(u_i u_j u_\ell:\ i,j,\ell\text{ distinct},\quad u_h\in\{x_h,y_h\}).
\]
Thus the homogeneous Jacobian singular ideal before saturation is \(J=I_X+T\). This identity is integral, so it holds in characteristic two as well.

**3. Support and generic reduction.** The monomial ideal \(Q=(z_1,z_2,z_3,z_4)+T\) is squarefree and hence radical. Its projective zero set is precisely the union of coordinate lines containing one coordinate from each of two distinct pairs:  \(\binom42\cdot 2^2=24\) lines. The relations in \(J\) identify all \(z_i\) with a common element \(t\), and \(t^3=z_1z_2z_3=0\) modulo \(T\); hence \(\sqrt J=Q\). On the open part of a line where two coordinates from distinct pairs are nonzero, eliminate the partner variables of those pairs. The remaining equation is \(x_r y_r-x_s y_s=0\) in four transverse coordinates, so the Jacobian singular scheme is reduced along that open part.

**4. Exact embedded local module.** By symmetry consider the projective coordinate point \(P_{x_4}\) where \(x_4\ne0\), with all other homogeneous coordinates zero. Dehomogenize \(x_4=1\) and eliminate \(y_4\). Writing the other three pairs as \((u_a,v_a)\) for \(a=1,2,3\), the local equations become
\[
u_1v_1-u_2v_2=0,\qquad u_1v_1-u_3v_3=0.
\]
The \(2\times2\) Jacobian minors generate all twelve cross-pair products \(u_a u_b,u_a v_b,v_a u_b,v_a v_b\) for \(a<b\). Modulo these minors and the two equations, the three same-pair products coincide as an element \(\tau\). This element is nonzero: in homogeneous degree two the quotient has the six independent squares \(u_a^2,v_a^2\) and exactly one independent same-pair product \(\tau\). Every parameter in the maximal ideal annihilates \(\tau\), since \(\tau=u_bv_b\) can be represented using a pair different from that parameter's pair. Consequently \(\tau^2=0\), and the nilradical of the Jacobian singular scheme at this point is \(k\tau\), a module of length one. The reduced local ring is the union of six coordinate axes (impose \(u_av_a=0\) as well as the cross-pair products). All eight coordinate points have identical charts up to a coordinate permutation.

**5. No other embedded structure.** Step 3 proves reduction at every non-vertex singular point. Step 4 computes the full local nilradical at each of the eight remaining points. The kernels of \(\mathcal O_\Sigma\twoheadrightarrow\mathcal O_{\Sigma_{\rm red}}\) therefore glue to eight length-one skyscrapers, with square-zero product. This proves the claimed exact sequence and complete scheme-theoretic classification.

**6. Arithmetic genera.** The 24 coordinate lines form the complete four-partite incidence graph with four parts of size two, \(K_{2,2,2,2}\), on the eight coordinate points. Every point lies on six lines; other pairwise intersections are empty. At each coordinate point the reduced curve has local ring of six coordinate axes, whose normalization has cokernel of length five. The normalization is the disjoint union of 24 copies of \(\mathbb P^1\). Therefore
\[
\chi(\mathcal O_{\Sigma_{\rm red}})=24-8(6-1)=-16,\qquad p_a(\Sigma_{\rm red})=17.
\]
The length-eight nilradical from Step 5 increases Euler characteristic by eight, giving
\[
\chi(\mathcal O_\Sigma)=-8,\qquad p_a(\Sigma)=9.
\]
The dimension-one leading term is unchanged, so both schemes have degree \(24\).

## Verification
The standalone `verify.py` enumerates every \(3\times3\) maximal Jacobian minor over the integers and all \(2\times2\) minors of the fixed-point chart, checking the exact unit coefficients and monomial supports (32 and 12 respectively). It verifies the six-axis-plus-one quadratic tangent-space dimension and the 24-line incidence arithmetic. As an independent finite check, it exhaustively tests all nonzero affine-cone points satisfying the three quadrics over \(\mathbb F_2\) and \(\mathbb F_3\), comparing Jacobian rank with the predicted singular support. The exact algebraic argument, not this finite enumeration, proves the assertions over all algebraically closed fields.

## Relationship to prior work
Sturmfels and Sullivant established the binomial complete-intersection presentation of \(X_{C_4}\) and identified its cut polytope as the four-dimensional crosspolytope; they also established that it is not smooth. An earlier cycle-cut singular-support classification establishes the 24 reduced components at \(n=4\), their incidence, and generic determinantal transverse equations. Those **reduced-support results are prior**, not contributions of this note. What is established here is the exact additional scheme-theoretic information: a length-one embedded nilpotent at **each** of the eight coordinate points, with no further nilpotents, and the resulting arithmetic-genus change from \(17\) to \(9\). This distinction cannot be recovered from a reduced singular-support classification alone.

## Limitations
No independent expert audit has been performed. The result is for the named four-cycle cut variety; it does not claim a nonreduced-Jacobian classification for all cycle cut varieties. It does not determine the global minimal graded free resolution of the saturated Jacobian scheme. Equivalent calculations in more general literature on binomial complete intersections or toric singular schemes may exist; the available searches do not prove absolute novelty.

## References
1. B. Sturmfels and S. Sullivant, *Toric Geometry of Cuts and Splits*, arXiv:math/0606683, first publicly submitted 2006-06-27, especially Example 1.2, Corollary 2.4, and the comparison with binary phylogenetic models. https://arxiv.org/html/math/0606683v2
2. A. Engström, *Cut ideals of \(K_4\)-minor free graphs are generated by quadrics*, arXiv:0805.1762 (2008). Its graph-level generating-degree theorem is background, not a singular-scheme calculation.
