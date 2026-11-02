# Sharp positivity frontier for energy-scaled diagonal inverse fitting in dimension three

## Finding

Consider the energy-scaled Frobenius fitting problem
\[
\min_{x\in\mathbb R^n} F_A(x),\qquad
F_A(x)=\frac12\left\|I-A^{1/2}\operatorname{diag}(x)A^{1/2}\right\|_F^2,
\]
where \(A\) is any real symmetric positive-definite matrix. The minimizer is unique. In dimensions one and two, its diagonal entries are strictly positive. In dimension three, write \(d_i=A_{ii}\) and normalize
\[
R=\operatorname{diag}(d)^{-1/2}A\operatorname{diag}(d)^{-1/2}
=\begin{pmatrix}1&a&b\\a&1&c\\b&c&1\end{pmatrix}.
\]
Set \(u=a^2\), \(v=b^2\), \(t=c^2\) and \(\Delta=1+2uvt-u^2-v^2-t^2>0\). The exact fitted coefficients satisfy
\[
\begin{aligned}
d_1x_1&=\frac{(1-t)(1+t-u-v)}{\Delta},\\
d_2x_2&=\frac{(1-v)(1+v-u-t)}{\Delta},\\
d_3x_3&=\frac{(1-u)(1+u-v-t)}{\Delta}.
\end{aligned}
\]
Thus the unique optimal diagonal inverse is positive definite if and only if
\[
a^2+b^2<1+c^2,\quad a^2+c^2<1+b^2,\quad b^2+c^2<1+a^2.
\]
Equality in one condition gives a singular optimum; violation gives an indefinite optimum. At most one fitted coefficient can be nonpositive. Three is the smallest dimension admitting positivity failure.

For the symmetric-coupling family
\[
R(r,s)=\begin{pmatrix}1&r&r\\r&1&s\\r&s&1\end{pmatrix},\quad 0<s<1,\quad r>0,
\]
the matrix is positive definite exactly when \(2r^2<1+s\). Its unconstrained diagonal fit is indefinite exactly in the nonempty, sharp window
\[
\frac{1+s^2}{2}<r^2<\frac{1+s}{2}.
\]
In this window, imposing \(x_i\ge0\) has a unique optimizer and an exact excess squared-objective cost:
\[
x^{\mathrm{psd}}=\left(0,\frac1{1+s^2},\frac1{1+s^2}\right),\qquad
F_{R(r,s)}(x^{\mathrm{psd}})-\min F_{R(r,s)}
=\frac{(2r^2-1-s^2)^2}{2(1+s^2)(1+s^2-2r^4)}.
\]
Over strictly positive diagonal matrices, the same number is an infimum gap, not a attained minimum.

## Assumptions and scope

The coefficient matrix \(A\) is real, symmetric and strictly positive definite; all optimization is in exact arithmetic. The fitting pattern consists only of diagonal entries, with no sign constraints in the first optimization. The positive-semidefinite constrained problem is \(x_i\ge0\); a symmetric positive-definite diagonal preconditioner instead requires \(x_i>0\). The affine factor \(A^{1/2}\operatorname{diag}(x)A^{1/2}\) has the same inertia as \(\operatorname{diag}(x)\), so diagonal coefficient signs determine preconditioner definiteness.

The dimension-three classification holds for **all** real SPD matrices, without assuming that their off-diagonal entries are positive or that they arise from a particular PDE discretization. The exact constrained gap is claimed only for the displayed symmetric-coupling family, not for an arbitrary three-by-three matrix.

## Proof

**Normal equations and strict convexity.** Expanding the squared Frobenius norm, using cyclicity of the trace and symmetry of \(A\), gives
\[
F_A(x)=\frac n2-\sum_i A_{ii}x_i+\frac12\sum_{i,j}A_{ij}^2 x_ix_j.
\]
Its Hessian is \(A\circ A\), the entrywise Hadamard square. By the Schur product theorem, this Hessian is strictly positive definite when \(A\) is SPD, and therefore the unique minimizer obeys
\[
(A\circ A)x=\operatorname{diag}(A).
\]
Writing \(D=\operatorname{diag}(d)\), \(R=D^{-1/2}AD^{-1/2}\), \(H=R\circ R\) and \(w=Dx\) transforms these equations into \(Hw=\mathbf 1\). For dimensions one and two, respectively, \(w=(1)\) and \(w=(1+a^2)^{-1}(1,1)\), which are strictly positive.

**Complete three-dimensional sign classification.** In dimension three,
\[
H=\begin{pmatrix}1&u&v\\u&1&t\\v&t&1\end{pmatrix}.
\]
SPD of \(R\) implies \(0\le u,v,t<1\), while SPD of \(H\) gives \(\Delta=\det H>0\). Cramer's rule yields the three displayed formulas. Since the prefactors \(1-u,1-v,1-t\) and \(\Delta\) are positive, the three sign tests are necessary and sufficient. If two coefficients were nonpositive, for example the first and second, then \(u+v\ge1+t\) and \(u+t\ge1+v\) would imply \(u\ge1\), impossible. The other pairs are symmetric. In particular, zero and negative entries cannot coexist at two different positions.

**Sharp family and the exact positivity cost.** The antisymmetric \((0,1,-1)\) mode of \(R(r,s)\) has eigenvalue \(1-s\). The remaining two-by-two principal compression has determinant \(1+s-2r^2\), so SPD is equivalent to \(0<s<1\) and \(2r^2<1+s\). Put \(u=r^2\) and \(t=s^2\). Symmetry and direct inversion give
\[
x_1=\frac{1+t-2u}{1+t-2u^2},\qquad
x_2=x_3=\frac{1-u}{1+t-2u^2}.
\]
The denominator is positive by strict convexity. Therefore \(x_1<0\) precisely when \(2u>1+t\), while positive definiteness of \(R(r,s)\) requires \(2u<1+s\). The interval between these bounds is nonempty for every \(0<s<1\) because \(s^2<s\), establishing sharpness.

For \(2u>1+t\), consider \(y=(0,(1+t)^{-1},(1+t)^{-1})\). The partial derivatives of \(F_{R(r,s)}\) at \(y\) vanish in coordinates two and three, while the first derivative equals \(2u/(1+t)-1>0\). Thus the Karush–Kuhn–Tucker conditions for the nonnegative orthant hold. Strict convexity proves \(y\) is its unique minimizer. Substitution in the quadratic objective gives
\[
F_{R(r,s)}(y)-F_{R(r,s)}(x)
=\frac{(2u-1-t)^2}{2(1+t)(1+t-2u^2)},
\]
which is strictly positive on the window. Because the unique constrained minimizer has first coordinate zero, there is no minimizer in the open strictly positive cone, although feasible vectors with first coordinate approaching zero attain the stated infimum.

**Exact rational witness.** With \(r=9/10\) and \(s=7/10\), the matrix \(R(r,s)\) has leading principal minors \(1\), \(19/100\) and \(3/125\), hence is SPD. Its unique optimal diagonal coefficients are
\[
x=\frac1{889}(-650,950,950),
\]
whereas the positive-semidefinite constrained optimum is \(y=(0,100/149,100/149)\). Their exact cost difference is
\[
F_{R(r,s)}(y)-F_{R(r,s)}(x)=\frac{4225}{132461}>0.
\]
This gives a positive-definite input whose unconstrained best energy-scaled diagonal approximate inverse has one negative eigenvalue.

## Verification

The supplied standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It checks the rational witness, the exact objective gap, the formulas and sign constraints on a seeded grid of three-dimensional SPD correlation matrices, the sharp symmetric-coupling window on a rational parameter grid, and positivity for all sampled two-dimensional correlations. Running `python verify.py` returned `PASS: 3614 exact-rational assertions / grouped checks; analytic proof required for universal quantifiers.` The symbolic derivations and inequalities in the proof, not the finite tests, establish the universal statements.

## Relationship to prior work

Xia and Moxey [1] introduce the weighted Frobenius inverse-fitting objective in their Section 4.4, equations (27)–(32), and note in Section 4.4.2 and Appendix A.3 that symmetry does not ensure positive definiteness. They use an empirical corrective diagonal shift. The optimization objective and the qualitative positivity warning are therefore **not claimed as new**. The additional assertions here are the complete all-SPD dimension-three sign test, the proof that dimension three is minimal, the exact nonempty phase window, and the exact constrained objective penalty in a natural correlated family.

Qu and collaborators [2] and Demmel [3] study diagonal scaling to optimize condition numbers, not the unrestricted weighted-Frobenius inverse-fitting normal equations. Amsel and collaborators [4] study the matrix-vector query complexity of approximating a target matrix under prescribed sparsity with an ordinary Frobenius objective; that is not the congruence-weighted inverse-fitting objective. The older literature on sparse approximate inverses provides context but does not establish historical uniqueness of the present formulas.

## Limitations

The result is an exact-algebraic model for diagonal inverse fitting; it is not a claim that the rational witness occurs as an elemental matrix in a specified DG mesh. It does not analyze the cost or convergence of iterative approximate least-squares solvers, the subsequent empirical diagonal shift, the full spatial multigrid method, or floating-point rounding. In the indefinite window, the strictly positive-cone optimal value is an infimum, not an attained minimum. Historical-priority comparisons are necessarily limited to the accessible primary sources and searchable records; independent mathematical review remains unperformed.

## References

[1] B. Xia and D. Moxey, *A Novel Matrix-Free Approximate Elemental Inverse for Efficient Preconditioning of Discontinuous Galerkin Spectral Elements*, arXiv:2610.31982v1 (first public version 2026-10-22), https://arxiv.org/abs/2610.31982 . See Sections 4.4.1–4.4.2 and Appendix A.3.

[2] Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809 (2022), https://arxiv.org/abs/2209.00809 .

[3] J. Demmel, *Nearly Optimal Block-Jacobi Preconditioning*, SIAM Journal on Matrix Analysis and Applications **44** (2023), 408–413, doi:10.1137/22M1504901 .

[4] N. Amsel, T. Chen, F. D. Keles, D. Halikias, C. Musco and C. Musco, *Fixed-Sparsity Matrix Approximation from Matrix-Vector Products*, arXiv:2402.09379 (2024), https://arxiv.org/abs/2402.09379 .
