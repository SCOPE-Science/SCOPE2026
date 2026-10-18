# Two-support-ratio asymmetry law for symmetric Cayley prismatoids

## Finding

For two full-dimensional centrally symmetric convex bodies placed in parallel affine hyperplanes, the Minkowski asymmetry of their convex hull depends on exactly two directional containment ratios. An explicit three-phase formula determines the optimal reflection factor, the unique height of every minimizing center, and the complete horizontal center set. For orthotope bases this set is a coordinate box with an exact affine-dimension classification. In every ambient dimension the asymmetry is strictly below three, with sharp supremum three in dimensions at least three.

Let \(h_K,h_L\) denote the support functions of the origin-symmetric bases. Set
\[
\alpha=\min\left\{1,\min_{u\in S^{d-1}}\frac{h_L(u)}{h_K(u)}\right\},\qquad
\beta=\min\left\{1,\min_{u\in S^{d-1}}\frac{h_K(u)}{h_L(u)}\right\}.
\]
These numbers lie in \((0,1]\). Define \((U,V)\) by the following exhaustive, boundary-compatible rules:
\[
(U,V)=\begin{cases}
(0,1-\beta),&\alpha(2-\beta)\ge1,\\
(1-\alpha,0),&\beta(2-\alpha)\ge1,\\
\left(\dfrac{1-2\alpha+\alpha\beta}{1-\alpha\beta},\dfrac{1-2\beta+\alpha\beta}{1-\alpha\beta}\right),&\text{otherwise}.
\end{cases}
\]
At \(\alpha=\beta=1\) the first branch returns \(U=V=0\); otherwise the two boundary branches cannot give inconsistent values. Put \(Q=2+U+V\). The exact Minkowski asymmetry is
\[
\boxed{s(C)=Q-1=1+U+V.}
\]
All minimizing centers have the same vertical coordinate \(t_*=(1+V)/Q\). Their entire horizontal fiber is
\[
\boxed{\mathcal Z=\left\{z:\ Q|\langle u,z\rangle|\le
(1+U)h_K(u)+(1+V)h_L(u)-2\max\{h_K(u),h_L(u)\}
\text{ for all }u\in\mathbb R^d\right\}.}
\]
In particular, \(1\le s(C)<3\); the upper constant is sharp as a supremum for \(d\ge2\).

For positive boxes \(K=\prod_i[-a_i,a_i]\), \(L=\prod_i[-b_i,b_i]\), the ratios are
\[
\alpha=\min\{1,b_1/a_1,\ldots,b_d/a_d\},\qquad
\beta=\min\{1,a_1/b_1,\ldots,a_d/b_d\}.
\]
The complete fiber is the box \(\mathcal Z=\prod_i[-\delta_i,\delta_i]\), where
\[
\boxed{\delta_i=\frac{(1+U)a_i+(1+V)b_i-2\max\{a_i,b_i\}}{Q}\ge0.}
\]
Thus \(\dim\operatorname{aff}\mathcal Z=\#\{i:\delta_i>0\}\), including every phase-boundary case.

## Assumptions and scope

Fix any integer \(d\ge1\). The sets \(K,L\subset\mathbb R^d\) are nonempty compact convex bodies, full-dimensional and symmetric about the origin. Their support functions are strictly positive on the unit sphere. Define the Cayley prismatoid
\[
C=\operatorname{conv}\bigl((K,0)\cup(L,1)\bigr)\subset\mathbb R^{d+1}.
\]
The asymmetry of a full-dimensional convex body \(C\) is
\[
s(C)=\min\{\lambda\ge1:\text{ some }c\in C\text{ satisfies }-(C-c)\subseteq\lambda(C-c)\}.
\]
A minimizing \(c\) is a Minkowski center. Bodies with distinct symmetry centers are covered after an affine shear aligning those centers; the claimed center set is then sheared back. We do not claim the formula for nonsymmetric bases.

## Proof

**1. Endpoint reflection reduction.** For \(q=1+\lambda\ge2\), a candidate center \(c=(z,t)\) satisfies the defining containment precisely when
\[
q c-C\subseteq(q-1)C.
\]
The reflected heights of the two bases are \(qt/(q-1)\) and \((qt-1)/(q-1)\). Both lie in \([0,1]\) exactly when \(qt\ge1\) and \(q(1-t)\ge1\). Since \(C\) is the convex hull of its two bases, it is enough to test their reflected copies. With \(y=qt\) and \(x=q(1-t)\), the slice-support formula \(h_{(C)_r}(u)=(1-r)h_K(u)+rh_L(u)\), and symmetry \(h_K(-u)=h_K(u)\), show that both endpoint copies are included if and only if
\[
q|\langle u,z\rangle|\le xh_K(u)+yh_L(u)-2\max\{h_K(u),h_L(u)\}
\quad\text{for all }u.
\]
This is an equivalence: it is not merely a sufficient containment test.

**2. Reduction to a two-variable linear program.** Write \(x=1+U\) and \(y=1+V\), with \(U,V\ge0\); then \(q=2+U+V\). Dropping the absolute value is necessary for the support inequalities. Conversely, if their right side is nonnegative for all directions then \(z=0\) is feasible. Directions with \(h_K(u)\ge h_L(u)\) impose
\[
U+(1+V)\frac{h_L(u)}{h_K(u)}\ge1,
\]
and the opposite ordering imposes
\[
V+(1+U)\frac{h_K(u)}{h_L(u)}\ge1.
\]
By positivity and compactness these conditions are equivalent to just
\[
\boxed{U+\alpha V\ge1-\alpha,\qquad\beta U+V\ge1-\beta,\qquad U,V\ge0.}
\]
Thus \(q\) is minimized by minimizing \(U+V\) in this planar linear program; no assumption about the horizontal center has been imposed.

**3. Exact optimizer and uniqueness.** If \(\alpha(2-\beta)\ge1\), the candidate \((0,1-\beta)\) is feasible; the second inequality yields \(U+V\ge1-\beta+(1-\beta)U\), hence it is the unique minimizer unless \(\beta=1\), in which case feasibility forces the same corner. The opposite branch is symmetric. In the remaining region both lower-bound lines bind at their intersection, giving the displayed rational formulas. The dual coefficients
\[
\frac{1-\beta}{1-\alpha\beta},\qquad
\frac{1-\alpha}{1-\alpha\beta}
\]
are strictly positive there and certify the sum objective; the two active lines have determinant \(1-\alpha\beta>0\), ensuring uniqueness. At \(\alpha=\beta=1\), the feasible minimum is \((0,0)\). Therefore \(U,V\) and the height \(t=y/q\) are uniquely fixed at all parameter values. Substituting the unique optimum in the endpoint inequalities proves the exact center fiber.

**4. Sharp universal cap.** In the mixed region,
\[
U+V=\frac{2(1-\alpha)(1-\beta)}{1-\alpha\beta}<2;
\]
in either corner phase the sum is at most one. Thus \(s(C)<3\). For the crossed boxes
\[
K=[-1,1]\times[-\varepsilon,\varepsilon],\qquad
L=[-\varepsilon,\varepsilon]\times[-1,1]
\]
with \(0<\varepsilon<1\), one has \(\alpha=\beta=\varepsilon\) and
\[
s(C)=\frac{3-\varepsilon}{1+\varepsilon}\longrightarrow3
\quad(\varepsilon\downarrow0).
\]
Products with common symmetric factors give the same approach in larger base dimensions.

**5. Exact orthotope centers.** Their support functions are \(h_K(u)=\sum_i a_i|u_i|\), \(h_L(u)=\sum_i b_i|u_i|\). Every ratio of these two sums is a convex combination of the coordinate ratios, proving the formulas for \(\alpha,\beta\). Testing the center-fiber inequality on \(u=\pm e_i\) gives the necessary inequalities \(|z_i|\le\delta_i\). Conversely,
\[
2\max\{\textstyle\sum_i a_i|u_i|,\sum_i b_i|u_i|\}
\le2\textstyle\sum_i\max\{a_i,b_i\}|u_i|
\]
shows that the individual coordinate bounds together imply the full support inequality. Consequently the fiber is exactly the stated product box. The affine dimension follows without generic-position assumptions.

## Verification

`verify_cayley.py` is a standalone Python standard-library checker using exact rational arithmetic. It independently enumerates the vertices of the reduced planar linear program and compares them with the three-phase formula. It also checks support inequalities at vertices of the proposed orthotope center fiber. The script passed 1,320 positive-integer box profiles in base dimensions one through six and 46,200 sampled directional support tests. Exact arithmetic eliminates roundoff in these finite tests. The proof above establishes the universal statements; sampling alone would not.

Two instructive three-dimensional prismatoids are generated by \((a_1,a_2)=(2,1)\), \((b_1,b_2)=(1,2)\), for which \(s=5/3\) and the center is unique, and by \((a_1,a_2)=(10,1)\), \((b_1,b_2)=(9,10)\), for which \(s=19/10\) and the center locus is a genuine line segment. This demonstrates why determining only a preferred axis center would be insufficient.

## Relationship to prior work

The Cayley-sum construction is standard. Hibi, Ohsugi and Tsuchiya study integer decomposition, unimodular triangulations and the Gorenstein property for Cayley sums. Bian, Demaine and Madhukara study edge unfolding for geometric prismatoids. Neither analysis gives the Minkowski reflection factor or the complete minimizing-center fibers treated here. Standard support-function calculus and planar linear programming are used openly as existing tools. The present claim is a support-ratio reduction and a complete optimizer classification, not a claim of discovering the Cayley construction or basic Minkowski asymmetry.

A homothetic frustum is a restricted one-parameter special case of this result: if \(L=\theta K\) with \(0<\theta\le1\), the formula specializes to \(s(C)=2-\theta\). The nonhomothetic crossed-base regime is not covered by that specialization. In contrast with free joins in independent spatial subspaces, the two bases here share the same spatial ambient space, and the result depends on their relative support functions rather than on the asymmetries of the factors (which both equal one).

## Limitations

The theorem assumes individually centrally symmetric bases, positive interior volume in a common \(d\)-space, and no constraint on smoothness. It does not classify center-fiber affine dimension for every pair of arbitrary smooth bodies beyond the exact intersection-of-support-slabs formula, nor does it provide volume formulas for the prismatoids. The scientific result has not undergone independent validation. While relevant published literature was compared, equivalent older results under alternate terminology remain a bibliographic possibility.

## References

1. T. Hibi, H. Ohsugi and A. Tsuchiya, *Integer decomposition property for Cayley sums of order and stable set polytopes*, arXiv:1807.05989v1, publicly submitted July 16, 2018. https://arxiv.org/abs/1807.05989
2. V. Bian, E. Demaine and R. Madhukara, *Edge-Unfolding Prismatoids: Tall or Rectangular Base*, arXiv:2106.14262v1, publicly submitted June 27, 2021. https://arxiv.org/abs/2106.14262
