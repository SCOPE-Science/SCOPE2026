# Complete Hessian-isotropy classification for the root-lattice isoperimetric minima

## Finding
Let \(d\ge4\). Novaga--Song compute the optimized logarithmic second variation of the isoperimetric quotient at the root lattice \(D_d\). For a traceless symmetric metric strain \(X\in\operatorname{Sym}_0(\mathbb R^d)\), write
\[
X=X_{\mathrm{diag}}+X_{\mathrm{off}},
\qquad
X_{\mathrm{diag}}=\operatorname{diag}X,
\qquad
X_{\mathrm{off}}=X-\operatorname{diag}X.
\]
The source formula is
\[
Q_d(X)=
\frac{\lVert X_{\mathrm{diag}}\rVert_F^2}{2(3d-2)}
+
\frac{d-2}{2d(2d-3)}\lVert X_{\mathrm{off}}\rVert_F^2.
\]
Among the irreducible root lattices that the source proves are strict local isoperimetric minima, the optimized Hessian is a scalar multiple of the Frobenius norm exactly for
\[
A_2,\quad D_4,\quad E_6,\quad E_7,\quad E_8.
\]
For every integer \(d\ge5\), the lattice \(D_d\) is the only anisotropic case in that local-minimizer list, with exact condition number
\[
\kappa_d=
\frac{(d-2)(3d-2)}{d(2d-3)}
=1+\frac{(d-1)(d-4)}{d(2d-3)}.
\]
The sequence is strictly increasing and satisfies
\[
1<\kappa_d<\frac32,
\qquad
\lim_{d\to\infty}\kappa_d=\frac32.
\]
Thus \(D_4\) is the unique \(D_d\) with an isotropic optimized isoperimetric Hessian, and for every \(d\ge5\) the diagonal traceless strains are precisely the least-stiff metric modes.

## Assumptions and scope
The statement concerns the local problem studied by Novaga--Song: nearby lattice Voronoi cells of an irreducible root lattice, followed by unrestricted volume-preserving affine maps, modulo similarities. The metric is written \(H=I+X\) with \(X\) symmetric and traceless to first order. The norm is the Frobenius norm \(\lVert X\rVert_F^2=\operatorname{tr}(X^2)\).

The classification is only about the quadratic term of the optimized logarithmic isoperimetric quotient. It does not claim that \(D_d\) is a global minimizer among all parallelohedra for \(d>4\), and it does not compare non-root lattices.

## Proof
The source proves that the irreducible root-lattice strict local minima are exactly \(A_2\), \(D_d\) for \(d\ge4\), and \(E_6,E_7,E_8\). Its equation (9.1) gives, for \(D_d\),
\[
Q_d(X)=a_d\lVert X_{\mathrm{diag}}\rVert_F^2+b_d\lVert X_{\mathrm{off}}\rVert_F^2,
\]
where
\[
a_d=\frac1{2(3d-2)},
\qquad
b_d=\frac{d-2}{2d(2d-3)}.
\]
The diagonal traceless and off-diagonal symmetric subspaces are Frobenius-orthogonal and both are nonzero for \(d\ge4\). Hence the quadratic-form condition number is the ratio of the larger coefficient to the smaller coefficient. Direct division gives
\[
\frac{b_d}{a_d}
=\frac{(d-2)(3d-2)}{d(2d-3)}
=1+\frac{(d-1)(d-4)}{d(2d-3)}.
\]
For \(d=4\) this ratio is \(1\). For every \(d>4\) it is strictly larger than \(1\), so the diagonal coefficient is the smaller one. Therefore \(D_4\) is the unique isotropic member of the \(D_d\) family and, for \(d\ge5\), diagonal traceless strains are the least-stiff modes.

The successive difference factors as
\[
\kappa_{d+1}-\kappa_d
=
\frac{7d^2-9d+4}{d(d+1)(2d-3)(2d-1)}.
\]
The numerator is positive for \(d\ge4\), so \(\kappa_d\) is strictly increasing. Comparing leading terms gives \(\kappa_d\to3/2\).

For the remaining local minima, the same source states that the \(A_2\) quadratic coefficient is the scalar \(1/12\), while equation (9.2) gives the scalar quadratic form
\[
\frac{\lVert X\rVert_F^2}{4(d+1)}
\]
for \(E_6,E_7,E_8\). Together with the \(D_4\) equality \(a_4=b_4=1/20\), this proves the complete isotropy classification within the source's irreducible root-lattice local-minimizer list.

## Verification
The proof uses only the source's explicit second-variation formulas and exact rational algebra. Substitution at \(d=4\) gives
\[
a_4=b_4=\frac1{20}.
\]
At \(d=5\), the first anisotropic case has
\[
\kappa_5=\frac{39}{35}>1,
\]
and the factored difference formula is positive for every integer \(d\ge4\). The limiting ratio follows from the degree-two leading terms. No finite enumeration or numerical experiment is used as a substitute for the all-rank argument.

## Relationship to prior work
Novaga--Song prove the four-dimensional global theorem for parallelohedra and, in their root-lattice application, derive the exact all-rank quadratic forms used here. They explicitly identify the strict local-minimizer list and note the special scalar behavior at the \(D_4\) metric, but the checked source does not state the cross-rank classification of Hessian isotropy, the exact \(D_d\) condition-number formula, its strict monotonicity, or its limit \(3/2\).

The three-dimensional local work of Cesaroni--Novaga treats the BCC/truncated-octahedron Voronoi cell in a different rank and parameterization. It does not imply the root-lattice all-rank stiffness profile proved here.

## Limitations
This is a second-order local statement. Higher-order terms can matter along directions outside the quadratic regime, and the result does not give a dimension-uniform neighborhood in which the quadratic approximation alone controls the full nonlinear deficit. The condition number is for the optimized metric Hessian after the affine minimization used in the source; it is not a condition number for every unoptimized parameterization of a Voronoi cell.

## References
1. Matteo Novaga and Lark Song, “The isoperimetric problem for four-dimensional parallelohedra,” arXiv:2610.01653v1, 2026. In particular Theorem 9.1 and equations (9.1)--(9.2).
2. Annalisa Cesaroni and Matteo Novaga, “Local minimality of the truncated octahedron for the isoperimetric problem on parallelohedra,” Bollettino dell'Unione Matematica Italiana, 2026, DOI 10.1007/s40574-026-00542-6.
