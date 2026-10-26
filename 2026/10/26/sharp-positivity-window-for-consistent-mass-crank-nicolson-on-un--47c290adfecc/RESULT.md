# Sharp positivity window for consistent-mass Crank–Nicolson on uniform Dirichlet meshes

## Finding

For every number of interior nodes \(n\ge3\) on a uniform one-dimensional mesh of spacing \(h>0\), let \(M\) and \(K\) be the consistent piecewise-linear finite-element mass and stiffness matrices for unit-diffusivity heat flow with homogeneous Dirichlet boundary values. The Crank–Nicolson update is
\[
P_n(\tau)=(M+\tfrac\tau2K)^{-1}(M-\tfrac\tau2K),\qquad z=\tau/h^2.
\]
It is entrywise nonnegative **exactly** for
\[
\boxed{\tau=0\quad\text{or}\quad\tfrac13\le z\le\rho_n.}
\]
Define the polynomials (for the same value of \(z\))
\[
a=4+6z,\quad b=3z-1,\quad D_0=1,\quad D_1=a,\quad
D_j=aD_{j-1}-b^2D_{j-2}\quad(2\le j\le n).
\]
The upper endpoint \(\rho_n>1/3\) is the **unique** root above \(1/3\) of
\[
36zD_{n-1}=(3z+1)D_n.
\]
The thresholds increase strictly with the number of nodes, with
\[
\rho_3=\sqrt2-\tfrac23\approx0.747546895706,
\qquad\rho_n\nearrow\rho_\infty\approx0.747597827128115,
\]
where \(\rho_\infty\) is the unique root in \((0.7,0.8)\) of
\[
27z^3-207z^2+141z-1=0.
\]
The boundary mechanism is explicit: at \(0<z<1/3\), the update has a negative entry at every distance-two position; at \(1/3<z<\rho_n\), **every** entry is strictly positive; and at \(z>\rho_n\), both endpoint diagonal entries are negative. Thus the familiar \(z\le2/3\) elementwise-sign bound does not give the sharp upper positivity boundary for this homogeneous interior map.

## Assumptions and scope

The physical problem is \(u_t=u_{xx}\) on an interval, with zero boundary data and zero forcing. There are \(n\ge3\) interior finite-element nodes and \(n+1\) equal elements of length \(h>0\). All claims concern a **single** update of the interior coefficient vector for arbitrary nonnegative interior initial data. No assertion is made about spatial interpolation positivity between nodes, arbitrary time-dependent boundary forcing, variable coefficients, nonuniform meshes, or other time integrators.

Let \(T_n\) be the adjacency matrix of the path on the \(n\) interior nodes. Direct element integration gives
\[
M=\frac h6(4I+T_n),\qquad K=\frac1h(2I-T_n).
\]
After multiplication by the positive factor \(6/h\), the update is \(P_n=A^{-1}B\), where
\[
A=(4+6z)I+(1-3z)T_n,\qquad
B=(4-6z)I+(1+3z)T_n.
\]
All inverses exist because the continuous mass and stiffness bilinear forms are positive definite on the Dirichlet interior space and \(\tau\ge0\).

## Proof

**1. Resolvent identity and the short-step obstruction.** For \(z\ne1/3\), cancellation of the common path-adjacency term gives
\[
P_n=\frac{1+3z}{1-3z}I-\frac{36z}{1-3z}A^{-1}.
\]
When \(0<z<1/3\), the off-diagonal entries of \(A\) are positive. Conjugating \(A\) by the alternating-sign diagonal matrix produces an irreducible positive-definite Stieltjes matrix. Its inverse is strictly positive; hence \((A^{-1})_{ij}\) has sign \((-1)^{i-j}\). Therefore \((P_n)_{i,i+2}<0\) for every \(1\le i\le n-2\). At \(z=0\), \(P_n=I\); at \(z=1/3\), direct substitution yields \(P_n=(I+T_n)/3\ge0\).

**2. The sole possible obstruction at larger steps.** For \(z>1/3\), put \(b=3z-1>0\) and \(a=4+6z\). Now \(A=aI-bT_n\) is an irreducible Stieltjes matrix because \(a>2b>0\). Its inverse has all entries strictly positive, and the resolvent identity becomes
\[
P_n=\left(-1-\frac2b\right)I+\frac{36z}{b}A^{-1}.
\]
Consequently every off-diagonal entry of \(P_n\) is strictly positive. Write \(\cosh\theta=a/(2b)>1\). The tridiagonal Green formula gives
\[
(A^{-1})_{ii}=\frac{\sinh(i\theta)\sinh((n+1-i)\theta)}{b\sinh\theta\sinh((n+1)\theta)}.
\]
Since \(\sinh(i\theta)\sinh((n+1-i)\theta)=\bigl(\cosh((n+1)\theta)-\cosh((n+1-2i)\theta)\bigr)/2\), its minimum is at \(i=1\) and \(i=n\). Thus the smallest diagonal entries of \(P_n\) are precisely its two endpoint diagonal entries. Entrywise positivity holds if and only if \((P_n)_{11}\ge0\).

**3. Exact finite-size threshold.** The continuant determinant formula for \(A\) is
\[
\det(A_j)=D_j,\quad D_0=1,\quad D_1=a,\quad D_j=aD_{j-1}-b^2D_{j-2},
\qquad (A^{-1})_{11}=D_{n-1}/D_n.
\]
Therefore
\[
(P_n)_{11}=-1-\frac2b+\frac{36z}{b}\frac{D_{n-1}}{D_n},
\]
and its zero is exactly \(36zD_{n-1}=(3z+1)D_n\), with the restriction \(z>1/3\) required because this formula divides by \(b\).

For uniqueness, diagonalize simultaneously in the Dirichlet sine basis. With \(\vartheta_j=\pi j/(n+1)\), the mass and stiffness eigenvalues after common positive scaling are \(m_j=4+2\cos\vartheta_j>0\) and \(k_j=12-12\cos\vartheta_j>0\). Each scalar amplification factor \((m_j-zk_j/2)/(m_j+zk_j/2)\) strictly decreases with \(z\), and its contribution to the first diagonal entry has strictly positive weight \(2\sin^2\vartheta_j/(n+1)\). Thus \((P_n)_{11}\) is strictly decreasing for all \(z\ge0\). It equals \(1/3\) at \(z=1/3\) and tends to \(-1\) as \(z\to\infty\), proving the existence and uniqueness of \(\rho_n>1/3\) and the claimed complete sign classification. For \(n=3\), the nonspurious positive root of the displayed equation is \(\sqrt2-2/3\).

**4. Strict growth and limiting constant.** When a new interior node is appended to the path, the top-left diagonal entry of the inverse \((aI-bT_n)^{-1}\) strictly increases: this follows from its Schur-complement recursion, since \(b>0\) and the off-diagonal inverse entries are nonzero. Hence for every fixed \(z>1/3\), \((P_{n+1})_{11}>(P_n)_{11}\), and consequently \(\rho_{n+1}>\rho_n\).

The same recursion has the infinite-path limit
\[
\lim_{n\to\infty}(A^{-1})_{11}=\frac2{a+\sqrt{a^2-4b^2}}=
\frac2{4+6z+\sqrt{12+72z}}.
\]
The limiting endpoint entry crosses zero uniquely because the same positive spectral-measure monotonicity persists, or directly by differentiating the displayed scalar expression. Its zero is characterized before squaring by
\[
72z=(3z+1)\bigl(4+6z+\sqrt{12+72z}\bigr).
\]
Squaring and factoring produces \(4(3z-1)(27z^3-207z^2+141z-1)=0\). The unsquared equation and \(z>1/3\) select the unique root of the cubic in \((0.7,0.8)\). The monotone sequence \(\rho_n\) converges to this root: for any fixed \(z\) below or above that crossing, the limiting endpoint sign agrees eventually with the finite-size sign. This proves the asserted exact algebraic limit.

## Verification

Run `python verify.py` with Python 3. The standalone checker constructs the full mass/stiffness path matrices using exact fractions, solves every Crank–Nicolson system using exact Gaussian elimination, and compares actual matrix entries with the determinant/Green expression for the endpoint diagonal. It tests 90 rational parameter pairs \((n,z)\) with \(3\le n\le12\) and nine values including \(0\), \(1/3\), \(2/3\), \(7/10\), \(3/4\), and \(1\). It also checks symmetry, negative distance-two entries below the lower threshold, positivity above the lower threshold, the location of the least diagonal, and negativity above \(3/4\).

A fully exact witness outside the older sufficient upper bound is \(n=3\) and \(z=7/10\):
\[
P_3(7/10)=
\begin{pmatrix}
527/18983&180/463&990/18983\\
180/463&37/463&180/463\\
990/18983&180/463&527/18983
\end{pmatrix}>0.
\]
The finite checker confirms formulas and catches implementation mistakes; the proof for all mesh sizes is the independent tridiagonal argument above, not finite enumeration.

## Relationship to prior work

Faragó and Horváth (2006), Sections 4–6 and especially Theorems 6.4–6.5, analyze the discrete maximum principle for more general parabolic finite-element iterations. Their stated uniform-grid step interval for the full DMP involves an upper \(2/3\) condition when the time integration parameter is \(1/2\). The present narrowly defined homogeneous Dirichlet interior map has an exact upper endpoint greater than \(0.7475\), as the explicit rational witness confirms. The broad DMP framework and the exact question of entrywise nonnegativity for this fixed interior propagator must therefore not be conflated. The full-DMP theorem does **not** give the mesh-size-dependent endpoint equation obtained here. Comparison with the earlier 2001 work cited in that paper is limited by unavailable full text.

Li and Huang (2012 preprint; journal 2013), Theorem 3.1, derive sufficient step-size bounds for maximum-principle preservation on possibly anisotropic simplicial meshes. Their sufficient, elementwise matrix-sign conditions do not determine the sharp finite-\(n\) Crank–Nicolson interval or its cubic limit.

Other published results on Crank–Nicolson positivity for finite Markov generators or for backward-Euler-filtered lattice schemes use different update operators and do not imply this consistent-mass finite-element classification. A proof of a new formula is not, by itself, a guarantee that no earlier equivalent formulation exists.

## Limitations

The classification is only for uniform one-dimensional meshes, a consistent (not lumped) mass matrix, zero time-dependent boundary data, zero forcing, and the one-step update of the interior coefficient vector. Positivity of all future iterations follows from nonnegativity of this fixed matrix, but the result does not classify positivity for nonuniform meshes or other numerical schemes. The original 2001 work on finite-element nonnegativity was not available in full; the possibility of independent earlier coverage remains a literature risk. The exact-arithmetic checks are reproducible but finite.

## References

1. I. Faragó and R. Horváth, *Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems*, SIAM Journal on Scientific Computing 28 (2006), 2313–2336, DOI: 10.1137/050627241; first online 2006-12-21. Sections 4–6, Theorems 6.4–6.5.
2. X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657 (first posted 2012-09-25), Theorem 3.1; subsequently Numerical Methods for Partial Differential Equations 29 (2013), 1963–1985, DOI: 10.1002/num.21784.
3. I. Faragó and R. Horváth, *On the nonnegativity conservation of finite element solutions of parabolic problems*, Proceedings of the Conference on Finite Element Methods: Three-Dimensional Problems, 2001, pp. 76–84. Bibliographic citation only; full text not examined.
