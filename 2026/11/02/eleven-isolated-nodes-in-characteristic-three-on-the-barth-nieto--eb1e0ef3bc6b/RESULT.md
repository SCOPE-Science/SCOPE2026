# Eleven isolated nodes in characteristic three on the Barth–Nieto quintic

## Finding
Let \(k\) be an algebraically closed field of odd characteristic \(p\). In \(\mathbb P^5_k\), write \(e_r\) for the \(r\)-th elementary symmetric polynomial in six homogeneous coordinates, and put
\[
N_p=V(e_1,e_5),\qquad e_1=\sum_{i=0}^{5}x_i,\qquad e_5=\sum_{i=0}^{5}\prod_{j\ne i}x_j.
\]
The reduced geometric singular locus of this integral symmetric model is the union of the **twenty coordinate lines**
\[
L_I=\{x_i=0\ (i\in I),\ \textstyle\sum_jx_j=0\},\quad I\subset\{0,\ldots,5\},\quad |I|=3,
\]
and the **ten isolated ordinary double points** given by permutations of
\[
[1:1:1:-1:-1:-1].
\]
In characteristic \(3\), and **only** in that odd characteristic, there is exactly **one further isolated ordinary double point**, namely
\[
P_*=[1:1:1:1:1:1].
\]
The twenty lines and all isolated nodes are defined over the prime field. The ten classical nodes constitute one symmetric-group orbit, and the extra characteristic-three node is fixed by the entire symmetric group. In characteristic three the isolated nodal set therefore has two orbits, of cardinalities \(10\) and \(1\).

For \(q=3^m\) with \(m\ge1\), the **reduced singular locus** has exactly
\[
\#\operatorname{Sing}(N_3)_{\mathrm{red}}(\mathbb F_q)=20q-14
\]
rational points; equivalently, its coordinate-line part has \(20q-25\) points and its isolated part has eleven. For an odd prime \(p\ge5\) and \(q=p^m\), the corresponding reduced singular-locus count is \(20q-15\).

## Assumptions and scope
The statement concerns the literal coefficientwise reduction of the integral complete intersection \(V(e_1,e_5)\), not an unspecified resolved or moduli-theoretic model. Geometric singular points are taken after base extension to an algebraic closure. A node means an isolated ordinary double point of a three-dimensional hypersurface in a smooth four-dimensional ambient variety, equivalently a nondegenerate quadratic tangent cone on a four-dimensional regular local parameter space. No assertion is made about the scheme structure or transversal analytic types along the twenty singular lines, or about a characteristic-three simultaneous resolution.

## Proof
**1. Exhausting the coordinate boundary.** If precisely one coordinate vanishes, exactly one term of \(e_5\) is nonzero, so the point is not on \(N_p\). With exactly two zero coordinates \(x_a=x_b=0\) and the other four nonzero, one has \(e_5=0\), but the gradient of \(e_5\) has the same nonzero value \(\prod_{i\ne a,b}x_i\) in positions \(a,b\), and zero in the other four positions. It is not proportional to \(\nabla e_1=(1,\ldots,1)\); thus the point is smooth. If three or more coordinates vanish, every term of \(e_5\) and every first partial derivative vanishes. Such points, under \(e_1=0\), lie on exactly the union of the twenty lines \(L_I\). These cases exhaust the coordinate boundary geometrically.

**2. Exhausting the torus.** Suppose that all coordinates are nonzero, and put \(P=\prod_i x_i\). On this torus,
\[
e_5=P\sum_i x_i^{-1}.
\]
At a point of \(N_p\), the derivative is
\[
\frac{\partial e_5}{\partial x_i}=-\frac{P}{x_i^2}.
\]
Consequently, the two defining gradients are dependent precisely when all six squares \(x_i^2\) are equal. Because \(p\ne2\), a projective rescaling makes each coordinate a sign \(s_i\in\{1,-1\}\). The conditions \(e_1=e_5=0\) both reduce to \(\sum_i s_i=0\). If exactly \(r\) of the signs are \(1\), this sum is \(2r-6\), with \(0\le r\le6\). For odd \(p\ge5\), its only zero residue is attained at \(r=3\), giving \(\binom63/2=10\) projectively distinct points. For \(p=3\), it is zero precisely for \(r\in\{0,3,6\}\). The cases \(r=0\) and \(r=6\) give the same additional projective point \(P_*\). Hence the torus contains precisely the asserted ten or eleven singular points, with no possible other geometric singularities.

**3. Each torus point is an ordinary node.** Let \(s=(s_0,\ldots,s_5)\) be any of the signed representatives found above; thus \(\sum_i s_i=0\) in \(k\). Write \(x_i=s_i+u_i\). On the affine cone over the hyperplane \(e_1=0\), the tangent parameter space is \(W=\{\sum_i u_i=0\}\), of dimension five. Since \(s_i^2=1\), the inverse-coordinate expansion gives
\[
\sum_i(s_i+u_i)^{-1}=\sum_i s_i-\sum_i u_i+\sum_i s_i u_i^2+O(u^3)=\sum_i s_i u_i^2+O(u^3)
\]
on \(W\). The product \(\prod_i(s_i+u_i)\) has nonzero constant term, so the quadratic tangent cone is a nonzero scalar multiple of
\[
Q(u)=\sum_i s_i u_i^2.
\]
The radical of the polar form of \(Q\) restricted to \(W\) is exactly the radial line \(ks\): indeed, if \(\sum_i s_i u_i v_i=0\) for all \(v\) with \(\sum_i v_i=0\), then the vector \((s_i u_i)_i\) is constant, whence \(u_i=c s_i\). As \(s\in W\), the quadratic form induced on the projective tangent space \(W/ks\), of dimension four, is nondegenerate. Thus each isolated singular point is an ordinary double point, including \(P_*\) in characteristic three.

**4. Rational singular-locus counts.** Over any odd finite field \(\mathbb F_q\), the boundary lines \(L_I\) are rational. A point on their union has either exactly three nonzero coordinates or exactly two. For every choice of three nonzero positions, the projective equation that their sum is zero gives \(q-2\) points where all three remain nonzero. There are \(\binom63=20\) choices. For every choice of two nonzero positions there is exactly one point, of ratio \([1:-1]\); there are \(\binom62=15\) choices. Accordingly the union has \(20(q-2)+15=20q-25\) rational points. All ten signed nodes are rational in every odd characteristic, and the extra node is rational in characteristic three. Adding these disjoint sets gives the two formulas in the Finding.

## Verification
The included standalone `verify.py` uses exact symbolic derivatives of the integral quintic on a four-parameter affine chart and computes the local quadratic Hessian determinants modulo three and five. It also exhaustively enumerates the projective \(\mathbb F_3\)- and \(\mathbb F_5\)-points to cross-check the singular-support classification against the explicit line and node sets. The recorded program output ends in `VERIFY_OK`: in characteristic three the two Hessian determinants are nonzero (\(2\) at \(P_*\) and \(1\) at a classical signed node), and the projective singular-point census has \(35+10+1=46\) points. In characteristic five the independent census gives \(75+10=85\). These finite checks corroborate, but do not replace, the algebraic-closure arguments in Proof paragraphs 1–3 or the all-extension counting argument in paragraph 4. Run with `python3 verify.py` and the documented SymPy dependency.

## Relationship to prior work
The Barth–Nieto quintic and its complex or characteristic-zero singular set are classical. Hulek, Nieto and Sankaran (1997 preprint, subsequently revised) explicitly record twenty desmic coordinate lines and ten singular points, while Hulek, Spandaw, van Geemen and van Straten (2000 preprint, published 2001) identify the ten signed points as ordinary double points. The latter paper explicitly confines its smooth-reduction arguments to primes at least five and excludes primes two and three as bad primes. These prior results give the twenty lines and ten nodes, but do not state the extra characteristic-three \(S_6\)-fixed node or the odd-characteristic comparison and its exact singular-support counts. A separate characteristic-two analysis concerns a different special fiber and does not imply the characteristic-three ordinary-node result. Published records and the most relevant earlier treatments were compared for equivalent or stronger coverage; possible unindexed exceptional-characteristic computations remain a historical priority risk.

## Limitations
This is an exact classification of the *reduced singular support* and of the eleven *isolated* nodal analytic types in characteristic three. It does not determine the nonreduced Jacobian scheme on the boundary, a simultaneous crepant resolution at the bad prime, the cohomology of such a resolution, or a zeta function of the threefold itself. All-extension formulas count singular-support points only. The original literature does not establish the new positive-characteristic claim merely by reduction of its characteristic-zero statements. Historical originality is assessed against inspected sources and searchable records, without a claim of exhaustive global bibliographic coverage.

## References
- K. Hulek, I. Nieto and G. K. Sankaran, *Heisenberg-invariant Kummer surfaces*, arXiv:alg-geom/9712025, initially posted 1997-12-19, especially the definition and classical singular-locus description in Section 1. https://arxiv.org/abs/alg-geom/9712025
- V. Gritsenko and K. Hulek, *The Modular Form of the Barth–Nieto Quintic*, arXiv:math/9806011, initially posted 1998-06-03, Introduction. https://arxiv.org/abs/math/9806011
- K. Hulek, J. Spandaw, B. van Geemen and D. van Straten, *The modularity of the Barth–Nieto quintic and its relatives*, arXiv:math/0010049, initially posted 2000-10-05, Sections 1 and 2.1. https://arxiv.org/abs/math/0010049
