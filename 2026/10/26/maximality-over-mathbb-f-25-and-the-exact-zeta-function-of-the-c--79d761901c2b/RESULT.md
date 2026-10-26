# Maximality over \(\mathbb F_{25}\) and the exact zeta function of the characteristic-five Clebsch Hessian K3 surface

## Finding
Let \(k=\mathbb F_5\), let \(e_j\) be the \(j\)-th elementary symmetric polynomial in \(x_0,\dots,x_4\), and let
\[
H=V(e_1,e_4)\subset\mathbb P^4_k\cong\mathbb P^3_k.
\]
This is the Hessian quartic of the Clebsch diagonal cubic \(V(e_1,\sum_i x_i^3)\). The surface \(H\) is geometrically integral and has exactly eleven geometric singularities, all ordinary double points defined over \(\mathbb F_5\): the ten points with two nonzero coordinates of opposite signs and the diagonal point \(E=[1:1:1:1:1]\). Let \(Y\to H\) be the minimal resolution. Then \(Y\) is a K3 surface, and
\[
\#H(\mathbb F_5)=41,\quad \#H(\mathbb F_{25})=901,\quad
\#Y(\mathbb F_5)=96,\quad \#Y(\mathbb F_{25})=1176.
\]
In particular \(Y\) is maximal over \(\mathbb F_{25}\), its geometric Frobenius eigenvalues on degree-two \(\ell\)-adic cohomology (\(\ell\ne5\)) are \(5\) with multiplicity \(18\) and \(-5\) with multiplicity \(4\), and
\[
\boxed{Z(Y/\mathbb F_5,T)=\frac{1}{(1-T)(1-25T)(1-5T)^{18}(1+5T)^4}.}
\]
This determines \(\#Y(\mathbb F_{5^r})=1+25^r+5^r(18+4(-1)^r)\) for every \(r\ge1\).

## Assumptions and scope
All equations are coefficientwise reductions of the indicated integer symmetric polynomials. The model is the complete intersection \(e_1=e_4=0\) in five homogeneous coordinates, not a smooth-characteristic-five deformation of a general Hessian quartic. Geometric assertions are over an algebraic closure of \(\mathbb F_5\). The zeta function refers to the smooth minimal resolution \(Y\), not the singular quartic \(H\). The base field, Frobenius convention and exceptional curves are specified explicitly below.

## Proof
**The Hessian equation.** Eliminate \(x_4=-\sum_{i=0}^3x_i\) in the Clebsch cubic. For the resulting cubic \(F=\sum_{i=0}^4x_i^3\), its four-by-four Hessian is \(6(D+x_4J)\), with \(D=\operatorname{diag}(x_0,\dots,x_3)\) and \(J\) the all-ones matrix. The rank-one determinant formula, valid as a polynomial identity even when some coordinates vanish, gives
\[
\det(\operatorname{Hess}F)=6^4\Big(\prod_{i=0}^3x_i+x_4\sum_{j=0}^3\prod_{0\le i\le3,\ i\ne j}x_i\Big)=6^4e_4(x_0,\dots,x_4).
\]
Since \(6\) is invertible modulo five, the Hessian surface is exactly \(H\).

**Complete geometric singularity locus.** A projective point of \(H\) is singular precisely when all partial derivatives \(\partial e_4/\partial x_i\) are equal, because the gradient of \(e_1\) is \((1,\dots,1)\). If exactly two coordinates are nonzero, their sum is zero and all derivatives of \(e_4\) vanish. This gives the ten projective points indexed by unordered coordinate pairs. One nonzero coordinate is impossible by \(e_1=0\). With exactly three nonzero coordinates \(a,b,c\), derivatives at these positions vanish but derivatives at the zero positions equal \(abc\ne0\); hence the point is smooth. With exactly four nonzero coordinates, \(e_4\) is their nonzero product, so no such point lies on \(H\).

For five nonzero coordinates put \(P=\prod_i x_i\) and \(S=\sum_i1/x_i\). Then \(e_4=PS\), so on \(H\) one has \(S=0\) and \(\partial e_4/\partial x_i=-P/x_i^2\). The gradients agree exactly when all \(x_i^2\) agree. Since the characteristic is odd, each coordinate equals \(a\) or \(-a\) for some \(a\ne0\). Five such signs sum to zero in characteristic five only if they are all equal, yielding \(E=[1:1:1:1:1]\). This exhausts the geometric singular locus.

**Ordinary double points and K3 property.** At \([1:-1:0:0:0]\), take affine coordinates \(x_0=1\), \(x_1=-1-u-v-w\), \((x_2,x_3,x_4)=(u,v,w)\). The quadratic initial form of \(e_4\) is \(-(uv+uw+vw)\); its symmetric Hessian determinant is nonzero modulo five. At \(E\), write \(x_0=1\), \(x_i=1+y_i\) for \(1\le i\le4\), with \(\sum_i y_i=0\). Translation gives \(e_4=3e_2(y)+2e_3(y)+e_4(y)\); its quadratic form on the three-dimensional tangent coordinate space is \(\sum_{i=1}^3y_i^2+(y_1+y_2+y_3)^2\), whose coefficient matrix \(I_3+J_3\) has determinant \(4\ne0\) in \(\mathbb F_5\). By permutation symmetry all eleven points are ordinary double points (\(A_1\)). Since a quartic hypersurface in \(\mathbb P^3\) with only isolated singularities cannot be nonreduced or geometrically reducible (distinct projective surface components intersect along curves), \(H\) is geometrically integral and normal. Its eleven rational double points have crepant minimal resolutions, and the usual quartic-surface cohomology and adjunction show \(\omega_Y\cong\mathcal O_Y\) and \(H^1(Y,\mathcal O_Y)=0\). Thus \(Y\) is a K3 surface with \(b_2(Y)=22\).

**Exact finite-field counts.** The standalone file `check_counts.py` performs exhaustive, integer-only arithmetic in \(\mathbb F_5\) and \(\mathbb F_{25}=\mathbb F_5[\theta]/(\theta^2-2)\). It independently counts the zero set of \(e_4\) in the hyperplane \(e_1=0\) in two ways: (i) normalizing the first nonzero among \(x_0,\dots,x_3\) and solving for \(x_4\); (ii) enumerating five-coordinate multisets, weighting by their permutation-orbit sizes and dividing by the number of nonzero scalars. Both methods give \(41\) and \(901\). The chart totals are \((23,12,5,1)\) and \((803,72,25,1)\), respectively; the multiset weighted affine totals are \(164\) and \(21624\), which equal \(4\cdot41\) and \(24\cdot901\).

All eleven nodes are defined over \(\mathbb F_5\). Resolving an ordinary node replaces one rational point with a smooth exceptional conic, isomorphic over a finite field to \(\mathbb P^1\), hence adds \(q\) rational points over \(\mathbb F_q\). It follows that the two counts on \(Y\) are \(96\) and \(1176\).

**Frobenius and the zeta function.** For smooth projective K3 surface \(Y/\mathbb F_5\), the Lefschetz trace formula is
\[
\#Y(\mathbb F_{5^r})=1+5^{2r}+\sum_{j=1}^{22}\alpha_j^r,
\]
where each complex-conjugate absolute value satisfies \(|\alpha_j|=5\). The two counts yield \(\sum_j\alpha_j=70\) and \(\sum_j\alpha_j^2=550=22\cdot25\). Equality in the complex triangle inequality forces \(\alpha_j^2=25\) for all \(j\). Thus each \(\alpha_j\) is either \(5\) or \(-5\); the first trace forces multiplicities \(18\) and \(4\). The displayed zeta function and the all-extension formula follow. This also proves maximality over \(\mathbb F_{25}\): the count \(1176=1+25^2+22\cdot25\) attains the K3 Weil upper bound.

## Verification
Run `python3 check_counts.py` with Python 3. No external packages or internet access are needed. The script constructs the field operations, exhaustively visits every projective point of the specified hyperplane over the two finite fields, and cross-checks the result by a permutation-multiset enumeration. It asserts both counts, the eleven-node resolution corrections, Frobenius traces, and final eigenvalue multiplicities. Its exact output is recorded in `VERIFICATION.md`. The global geometric singularity proof and K3-property arguments are mathematical, not deduced merely from finite-field enumeration.

## Relationship to prior work
Dardanelli–van Geemen [1] study the Hessian quartic of the classical Clebsch cubic, including its ten classical nodes and Néron–Severi configuration; their 2004 treatment is over characteristic zero and does not give this special-fibre zeta function. Kondō [2], especially Example 4.12 and the surrounding Hessian construction, identifies the characteristic-five fixed point and the associated Coble surface, and establishes supersingularity of the K3 covering surface. Those results motivate and support the geometric setting but do not state the \(\mathbb F_5\)-form's Frobenius multiplicities or its exact zeta function. The present result uses the specified five-coordinate model, the eleven-node correction and two exhaustive finite-field counts to determine that arithmetic. The characteristic-five geometry itself is not claimed as previously unknown.

## Limitations
The result is specific to this integral Hessian model over \(\mathbb F_5\); it does not compute the zeta functions of other twists or of nearby Hessian quartics. The detailed Artin invariant, integral Néron–Severi lattice and full integral reduction theory are not determined here. The novelty comparison is subject to possible equivalent presentations in historical arithmetic literature.

## References
[1] E. Dardanelli and B. van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322v1 (18 September 2004), https://arxiv.org/abs/math/0409322 .

[2] S. Kondō, *Coble surfaces with finite automorphism group*, arXiv:2102.00591v2 (20 July 2021), especially Section 4, Example 4.12, https://arxiv.org/abs/2102.00591 .
