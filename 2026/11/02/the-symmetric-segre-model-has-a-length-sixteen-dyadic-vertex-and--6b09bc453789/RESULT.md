# The symmetric Segre model has a length-sixteen dyadic vertex and twenty-seven reduced Fano planes

## Finding

Let \(e_j\) denote the \(j\)-th elementary symmetric polynomial in six variables, and let
\[
\mathscr X=V(e_1,e_3)\subset\mathbb P^5_{\mathbb Z}.
\]
The generic fiber is the classical Segre cubic threefold. Its characteristic-two fiber \(X\) is **not** the usual characteristic-two moduli model of the Segre cubic: rather, it is the projective cone over the smooth Clebsch diagonal cubic surface \(S\) over \(\mathbb F_2\). Its only geometric singular point is \(P=[1:1:1:1:1:1]\), an isolated ordinary triple point. The intrinsic Jacobian singular subscheme is supported at \(P\) and has completed coordinate ring
\[
\widehat{\mathcal O}_{\operatorname{Sing}(X),P}
\cong k[\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3]/
(\varepsilon_0^2,\varepsilon_1^2,\varepsilon_2^2,\varepsilon_3^2),
\qquad k=\overline{\mathbb F}_2.
\]
It has length \(16\) and local Hilbert function \((1,4,6,4,1)\). The blow-up of the vertex is smooth, with exceptional divisor \(S\).

The entire geometric Fano scheme of projective planes in \(X\) is a reduced zero-dimensional scheme of degree \(27\), and over \(\mathbb F_2\) it is the finite étale scheme
\[
\boxed{\operatorname{Fano}_2(X)\cong
\coprod_{15}\operatorname{Spec}(\mathbb F_2)
\;\sqcup\;
\coprod_{6}\operatorname{Spec}(\mathbb F_4).}
\]
The fifteen rational planes are exactly the specializations of the fifteen classical pair-partition planes; the twelve other geometric planes occur in six Frobenius-conjugate pairs and are all defined over \(\mathbb F_4\), not \(\mathbb F_2\).

For comparison, in every algebraically closed odd characteristic the elementary-symmetric model has exactly ten ordinary double points. Its ten canonical sign-pattern singular-point sections coalesce to \(P\) modulo two; the singular subscheme nevertheless has length \(16\), not \(10\). The generic characteristic-zero fiber contains fifteen planes.

## Assumptions and scope

All statements about the characteristic-two fiber refer to the **specified integral equations** \(e_1=e_3=0\), not to an arbitrary flat model of the Segre cubic or to its characteristic-two GIT compactification. A geometric plane means a projective linear \(\mathbb P^2\subset\mathbb P^4\) contained in the threefold. \(\operatorname{Fano}_2(X)\) denotes its ordinary Hilbert/Fano scheme. The intrinsic singular subscheme is defined locally by the hypersurface equation and all of its first partial derivatives. Fields are perfect where finite étaleness and rationality are discussed.

## Proof

**1. The cone identity.** Over \(\mathbb F_2\) make the invertible linear substitution
\[
y_i=x_i+x_5\quad(0\leq i\leq4),\qquad t=x_5.
\]
Expanding \(e_1,e_3\) after translating each of six coordinates by \(t\), the coefficients of \(t^3,t^2,t\) in \(e_3\) are respectively \(\binom63=20\), \(\binom52=10\), and \(\binom41=4\), all zero in characteristic two. Therefore
\[
e_1(x)=\sum_{i=0}^4y_i,\qquad e_3(x)=e_3(y_0,\ldots,y_4).
\]
The variable \(t\) does not occur: \(X\) is the cone from \(P\) over \(S=V(\sum y_i,e_3(y))\subset\mathbb P^4\), the characteristic-two Clebsch diagonal cubic surface. Indeed, Newton's identities give \(e_3(y)=\sum y_i^3\) on \(\sum y_i=0\) in characteristic two.

Eliminate \(y_4=y_0+y_1+y_2+y_3\), writing \(z_i=y_i\) for \(i=0,1,2,3\). The homogeneous defining polynomial of \(S\subset\mathbb P^3\) is
\[
F(z)=\left(\sum_{i=0}^3z_i\right)^3+\sum_{i=0}^3z_i^3
=\sum_{i\ne j}z_i^2z_j.
\]
Its gradient is
\[
\frac{\partial F}{\partial z_i}
=\left(\sum_{j\ne i}z_j\right)^2=w_i^2.
\]
The transformation \(z\mapsto w\) has matrix \(I_4+J_4\), where \(J_4\) is the all-ones matrix. In characteristic two, \((I_4+J_4)^2=I_4\), so the only common zero of the derivatives in affine four-space is the origin. Thus \(S\) is geometrically smooth and the cone has precisely the one singular point \(P\). Since the local equation at \(P\) is exactly the homogeneous cubic \(F\) with smooth projectivized tangent cone, this is an ordinary triple point. The blow-up is smooth: it is a projective line bundle over \(S\), and its neighborhood of the exceptional divisor is the total space of \(\mathcal O_S(-1)\).

**2. Scheme structure at the vertex.** Work in the affine chart \(t=1\) centered at \(P\). The local Jacobian ideal is
\[
(F,F_{z_0},F_{z_1},F_{z_2},F_{z_3})
=(w_0^2,w_1^2,w_2^2,w_3^2),
\]
because Euler's identity is \(F=\sum z_iF_{z_i}\) in characteristic two (the degree is three). Since \(w\) is an invertible linear coordinate system, the completed local algebra is the claimed square-zero-coordinate complete intersection. Its monomial basis consists of \(\prod_iw_i^{a_i}\) for \(a_i\in\{0,1\}\). Thus the length is \(2^4=16\), the Hilbert series is \((1+T)^4\), and the singular subscheme is local Gorenstein and nonreduced.

**3. Classification and arithmetic of planes.** Any plane in the cone must contain \(P\). Otherwise projection from \(P\) takes the plane isomorphically onto a plane in the smooth cubic surface \(S\), which is impossible. Planes through \(P\) correspond bijectively to lines of \(S\) under projection. Every smooth cubic surface over an algebraically closed field, in any characteristic, has exactly \(27\) geometric lines; the standard theorem follows also from the degree-\(27\) line-scheme class and the fact that each line has normal bundle \(\mathcal O_{\mathbb P^1}(-1)\).

For an explicit arithmetic determination, enumerate all two-dimensional subspaces of \(\mathbb F_q^4\) in their **unique** reduced-row-echelon bases \((u,v)\), for \(q=2,4\). The line is contained in \(S\) precisely when the four coefficients of \(F(Uu+Vv)\) vanish. The exact exhaustive tests in `verify_segre.py` give
\[
\begin{array}{c|cc}
q&\text{candidate subspaces}&\text{contained lines}\\\hline
2&35&15\\
4&357&27
\end{array}
\]
with all twelve lines present over \(\mathbb F_4\) but absent over \(\mathbb F_2\) exchanged in pairs by Frobenius. This finite computation determines all geometric lines, since there can be no more than \(27\); it is not an extrapolation from finite points. The fifteen \(\mathbb F_2\)-lines are exactly those coming from the fifteen partitions of the six indices into three unordered pairs. For a partition \(\{a,b\},\{c,d\},\{e,f\}\), the equations
\[
x_a+x_b=x_c+x_d=x_e+x_f=0
\]
define one of the fifteen classical planes over \(\mathbb Z\). Pair symmetry shows that \(e_1=e_3=0\) on these planes over every characteristic; the verifier checks that they account for all \(15\) rational lines after specialization.

**4. Reduced Fano scheme.** Let \(L\subset S\) be any geometric line. Its normal sequence is
\[
0\longrightarrow\mathcal O_L(-1)
\longrightarrow\mathcal O_L(1)^{\oplus2}
\xrightarrow{(Q_1,Q_2)}\mathcal O_L(3)
\longrightarrow0.
\]
Thus the induced map on global sections is an isomorphism, since both \(H^0(L,\mathcal O(-1))\) and \(H^1(L,\mathcal O(-1))\) vanish. In particular, \(Q_1,Q_2\) are independent quadrics on \(L\). For the cone plane \(\Pi=\operatorname{Join}(P,L)\), take homogeneous coordinates \([U:V:T]\) with \(T\) the vertex direction. Its six-dimensional first-order ambient normal-deformation space consists of two linear forms \(a_iT+\ell_i(U,V)\). The defining cubic's first variation is
\[
T(a_1Q_1+a_2Q_2)+\ell_1Q_1+\ell_2Q_2.
\]
Independence of \(Q_1,Q_2\) forces \(a_1=a_2=0\); the line-normal isomorphism forces \(\ell_1=\ell_2=0\). Hence the Fano scheme has zero Zariski tangent space at **each** of its \(27\) geometric points. It is reduced and étale. Its \(15\) rational points and six degree-two closed points give the claimed disjoint-union formula.

**5. Odd-characteristic comparison.** In any characteristic \(p\ne2\), a singular point of \(V(e_1,e_3)\) satisfies \(x_i^2=x_j^2\) for all indices, because on \(e_1=0\) the partial derivative of \(e_3\) at coordinate \(i\) is \(e_2+x_i^2\). Thus, up to scaling, its coordinates are signs \(\pm1\). If \(r\) of six coordinates are positive, \(e_1=2r-6\). For \(p\ge5\), only \(r=3\) is possible. For \(p=3\), \(r\in\{0,3,6\}\), but the all-equal choices have \(e_3=\pm20\ne0\). Consequently there are exactly \(\frac12\binom63=10\) singular points in every odd characteristic. At \((1,1,1,-1,-1,-1)\), after eliminating the hyperplane relation and choosing four local coordinates, the quadratic term is
\[
-2Q,\qquad Q=z_0z_1+z_0z_2+z_0z_3+z_1z_2+z_1z_3+z_2z_3+z_3^2.
\]
The determinant of its Hessian is \(16\), nonzero in every odd characteristic. Thus all ten are nodes. Their sign-pattern sections all specialize to \(P\) in characteristic two, while the special-fiber Jacobian scheme has length \(16\), as shown above.

## Verification

Run `python3 verify_segre.py` from the directory containing that file (Python standard library only). It checks the characteristic-two translation identity in the full polynomial ring, each gradient-square identity, invertibility of the linear substitution, complete RREF line enumerations over \(\mathbb F_2\) and \(\mathbb F_4\), Frobenius pairing of the twelve additional lines, identification of all classical pair-partition planes, and the nonzero normal-deformation determinant on each of the \(27\) planes. It also verifies the integer Hessian determinant used for the odd-characteristic comparison. Expected final output: `SYMMETRIC_SEGRE_CHAR2_JACOBIAN16_FANO_15PLUS6_ETALE_EXACT_OK`. These finite computations are exhaustive for the finite sets explicitly specified; the geometric completeness follows from the theoretical \(27\)-line theorem.

## Relationship to prior work

Cheltsov–Tschinkel–Zhang (first public preprint August 29, 2023) use the characteristic-zero Segre cubic, its ten nodes, and its classical \(\mathfrak S_6\)-structure. Dolgachev (first posted February 25, 2023), in discussing a characteristic-two moduli model, **explicitly notes** that the familiar power-sum symmetric coordinates only identify with his all-characteristic equation when \(p\ne2\). His good characteristic-two model retains ten nodes. The present finding concerns the different, coefficient-marked integral model \(V(e_1,e_3)\), not Dolgachev's good model. The classical \(27\)-line theorem and the \(15+12\) Clebsch line decomposition are background; the new asserted package is the exact singular-scheme, reduction, and arithmetic étale plane-Fano classification of the symmetric threefold model. The 2024 historical study by Rowe documents the classical fifteen-line and twelve-line decomposition of Clebsch's surface, but not the characteristic-two threefold degeneration.

## Limitations

The result is specific to this integral presentation. It does not assert that the Segre cubic's characteristic-two moduli compactification is a cone, nor that its ten ordinary nodes collide. No claim is made about the full deformation or stable-reduction theory of this model, arbitrary nonsymmetric models, or the complete family of its Fano schemes over \(\mathbb Z\). The determination of the twelve quadratic plane points uses a complete, independently reproducible finite-field enumeration together with the standard \(27\)-line bound. Independent external mathematical audit and validation have not been performed.

## References

1. I. V. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, arXiv:2302.13101 (first posted 2023-02-25), especially the Segre cubic discussion and characteristic-two warning. https://arxiv.org/abs/2302.13101 ; full-text journal version: https://doi.org/10.1112/blms.13033
2. I. Cheltsov, Y. Tschinkel, Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, arXiv:2308.15271 (first posted 2023-08-29), Sections 1, 2.4 and 6. https://arxiv.org/abs/2308.15271
3. D. E. Rowe, *Felix Klein's early contributions to anschauliche Geometrie*, *Archive for History of Exact Sciences* (2024), historical account of Clebsch's surface and its classical fifteen-plus-twelve line decomposition. https://doi.org/10.1007/s00407-024-00329-1
