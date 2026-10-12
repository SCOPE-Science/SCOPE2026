# Sharp finite-grid positivity threshold for Peaceman–Rachford heat stepping
## Finding
Let \(T_k=\operatorname{tridiag}(-1,2,-1)\) be the standard \(k\times k\) Dirichlet second-difference matrix. Define
\[
D_0(s)=1,\qquad D_1(s)=1+2s,\qquad D_j(s)=(1+2s)D_{j-1}(s)-s^2D_{j-2}(s).
\]
For every \(k\ge1\), let \(\sigma_k\) be the unique positive number satisfying
\[
D_k(\sigma_k)=2D_{k-1}(\sigma_k).
\]
Consider the Dirichlet heat semidiscretization on an \(m\times n\) interior rectangular grid,
\[
u'(t)=-(A_x+A_y)u(t),\qquad
A_x=h_x^{-2}T_m\otimes I_n,\qquad
A_y=I_m\otimes h_y^{-2}T_n,
\]
with \(m,n\ge2\). One full Peaceman–Rachford step is
\[
(I+\tfrac{\Delta t}2A_x)u^{(1/2)}=(I-\tfrac{\Delta t}2A_y)u^{(0)},
\]
\[
(I+\tfrac{\Delta t}2A_y)u^{(1)}=(I-\tfrac{\Delta t}2A_x)u^{(1/2)}.
\]
Its one-step matrix is entrywise nonnegative, equivalently it maps every componentwise nonnegative grid vector to a componentwise nonnegative vector, if and only if
\[
\frac{\Delta t}{2h_x^2}\le\sigma_m
\quad\text{and}\quad
\frac{\Delta t}{2h_y^2}\le\sigma_n.
\]
The thresholds satisfy
\[
\sigma_1=\frac12,\qquad \sigma_2=\frac1{\sqrt3},\qquad
\sigma_k<\sigma_{k+1},\qquad
\lim_{k\to\infty}\sigma_k=2-\sqrt2.
\]
Consequently, on an \(N\times N\) square grid with mesh width \(h\), the sharp dimensionless condition is
\[
\frac{\Delta t}{h^2}\le 2\sigma_N,
\]
and the finite-grid frontiers increase to \(4-2\sqrt2\).

## Assumptions and scope
The statement concerns the classical constant-step Peaceman–Rachford factorization applied to the standard five-point Dirichlet heat semidiscretization on a rectangular tensor grid. Positivity means entrywise nonnegativity of the full end-step matrix, not positivity of either intermediate half-step. No claim is made for variable coefficients, nonrectangular grids, non-Dirichlet closures, nonlinear problems, or modified ADI formulas.

## Proof
Put
\[
R_k(s)=(I+sT_k)^{-1},\qquad C_k(s)=R_k(s)(I-sT_k)=2R_k(s)-I.
\]
The Peaceman–Rachford factors commute on the tensor grid, so with
\[
s_x=\frac{\Delta t}{2h_x^2},\qquad s_y=\frac{\Delta t}{2h_y^2},
\]
the full step is exactly
\[
G_{m,n}=C_m(s_x)\otimes C_n(s_y).
\]

For the tridiagonal matrix \(I+sT_k\), expansion of leading principal determinants gives the stated recurrence for \(D_j(s)\). The standard cofactor recurrence can be checked directly and yields, for \(i\le j\),
\[
(R_k(s))_{ij}=
\frac{s^{j-i}D_{i-1}(s)D_{k-j}(s)}{D_k(s)}.
\]
Thus every off-diagonal entry of \(R_k(s)\), hence of \(C_k(s)\), is strictly positive when \(s>0\). Only diagonal entries can obstruct positivity.

Define \(q_j(s)=D_j(s)/D_{j-1}(s)\). Then
\[
q_1=1+2s,\qquad q_j=1+2s-\frac{s^2}{q_{j-1}}.
\]
For \(s>0\), \(q_2<q_1\), and induction gives \(q_{j+1}<q_j\). Since
\[
(R_k(s))_{ii}=\frac{D_{i-1}(s)D_{k-i}(s)}{D_k(s)},
\]
we have
\[
\frac{(R_k(s))_{i+1,i+1}}{(R_k(s))_{ii}}=\frac{q_i(s)}{q_{k-i}(s)}.
\]
The diagonal therefore increases from either endpoint toward the center, and its minimum is
\[
(R_k(s))_{11}=(R_k(s))_{kk}=\frac{D_{k-1}(s)}{D_k(s)}=\frac1{q_k(s)}.
\]
Because \(C_k=2R_k-I\), this proves
\[
C_k(s)\ge0
\quad\Longleftrightarrow\quad
\frac{D_{k-1}(s)}{D_k(s)}\ge\frac12.
\]

The endpoint resolvent entry is strictly decreasing in \(s\): with \(v=(I+sT_k)^{-1}e_1\),
\[
\frac{d}{ds}(R_k(s))_{11}=-v^{\mathsf T}T_kv<0.
\]
It equals \(1\) at \(s=0\) and tends to \(0\) as \(s\to\infty\). Hence there is a unique positive crossing, precisely \(D_k=2D_{k-1}\), proving the one-dimensional criterion.

For fixed \(s>0\), the strict decrease of \(q_k(s)\) in \(k\) makes \(1/q_k(s)\) strictly increase, so \(\sigma_k\) strictly increases. The recurrence converges to the larger fixed point
\[
q_\infty(s)=\frac{1+2s+\sqrt{1+4s}}2.
\]
The limiting threshold solves \(q_\infty(s)=2\), giving \(s=2-\sqrt2\). The formulas for \(\sigma_1\) and \(\sigma_2\) follow directly from \(D_1=2D_0\) and \(D_2=2D_1\).

Finally, if both one-dimensional factors are nonnegative, their Kronecker product is nonnegative. Conversely, if one factor has a negative endpoint diagonal, the other factor has either a positive off-diagonal entry when its parameter is positive or an identity diagonal when its parameter is zero; their tensor product therefore has a negative entry. This proves the two-dimensional if-and-only-if statement.

## Verification
At \(m=n=2\), \(h_x=h_y=1\), and \(\Delta t=6/5\), one has \(s_x=s_y=3/5>1/\sqrt3\) and exactly
\[
C_2(3/5)=\frac1{56}
\begin{pmatrix}-1&15\\15&-1\end{pmatrix}.
\]
Hence \(G_{2,2}=C_2(3/5)\otimes C_2(3/5)\) contains the negative entry
\[
(G_{2,2})_{(1,1),(1,2)}=-\frac{15}{3136}.
\]
Taking the corresponding coordinate vector as nonnegative initial data produces a negative component after one full step. By contrast, at \(\Delta t/h^2=11/10\), so \(s=11/20\),
\[
C_2(11/20)=\frac1{1643}
\begin{pmatrix}37&440\\440&37\end{pmatrix}>0,
\]
showing directly that the sharp finite-grid frontier is strictly larger than \(1\) already for the smallest nontrivial square grid. The accompanying exact-rational checker reproduces these matrices and verifies determinant identities and numerical root monotonicity for representative dimensions; the infinite-dimensional limit is established analytically above rather than by computation.

## Relationship to prior work
Peaceman and Rachford introduced the alternating-direction implicit heat scheme and proved unconditional stability of the alternating pair. Hundsdorfer and Verwer later analyzed stability and convergence of the Peaceman–Rachford ADI method for initial-boundary value problems; their classification includes MSC \(65\mathrm{M}20\). Dai developed a compact Peaceman–Rachford ADI discretization and again emphasized unconditional stability. Wade and collaborators studied positivity-preserving Padé smoothing for parabolic problems, while Hansen, Kramer, and Ostermann studied positivity-preserving Strang splitting. These sources establish that stability and positivity are distinct structural questions, but the inspected Peaceman–Rachford heat analyses do not state the finite-grid determinant threshold, its endpoint reduction, or the limit \(4-2\sqrt2\).

## Limitations
The result is specific to the tensor-product Dirichlet second-difference operator. The exact threshold can change under Neumann or mixed closures, variable diffusion, nonuniform meshes, reaction terms, or different ADI factorizations. Literature searches did not uncover an implication-equivalent finite-grid formula, but terminology in older discrete maximum-principle literature is a residual originality risk. The finding has undergone self-review only; no independent audit has been performed.

## References
1. D. W. Peaceman and H. H. Rachford, Jr., “The Numerical Solution of Parabolic and Elliptic Differential Equations,” Journal of the Society for Industrial and Applied Mathematics 3 (1955), 28–41, DOI 10.1137/0103003.
2. W. Hundsdorfer and J. G. Verwer, “Stability and Convergence of the Peaceman–Rachford ADI Method for Initial-Boundary Value Problems,” Mathematics of Computation 53 (1989), 81–101.
3. W. Dai, “Compact ADI Method for Solving Parabolic Differential Equations,” Numerical Methods for Partial Differential Equations 18 (2002), 129–142, DOI 10.1002/num.1037.
4. B. A. Wade, A. Q. M. Khaliq, M. Siddique, and M. Yousuf, “Smoothing with Positivity-Preserving Padé Schemes for Parabolic Problems with Nonsmooth Data,” Numerical Methods for Partial Differential Equations 21 (2005), 553–573, DOI 10.1002/num.20039.
5. E. Hansen, F. Kramer, and A. Ostermann, “A Second-Order Positivity Preserving Scheme for Semilinear Parabolic Problems,” Applied Numerical Mathematics 62 (2012), 1428–1435, DOI 10.1016/j.apnum.2012.06.003.
