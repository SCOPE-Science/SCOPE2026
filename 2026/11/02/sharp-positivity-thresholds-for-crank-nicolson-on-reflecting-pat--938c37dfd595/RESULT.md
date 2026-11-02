# Sharp positivity thresholds for Crank–Nicolson on reflecting paths

## Finding
Let \(P_n\) be the unweighted path with \(n\ge2\) vertices, let \(L_n\) be its combinatorial Laplacian, and define the Crank–Nicolson end-step matrix
\[
C_n(s)=(I+sL_n)^{-1}(I-sL_n),\qquad s\ge0.
\]
For every \(n\ge3\), there is a unique sharp threshold \(\sigma_n\) such that
\[
C_n(s)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le s\le\sigma_n.
\]
Set \(z=z(s)\in(0,1)\) by \(s=z/(1-z)^2\). The threshold is \(\sigma_n=z_n/(1-z_n)^2\), where \(z_n\in(1/3,1)\) is the unique root, in that open interval, of
\[
\begin{cases}
(1-3z)+(3-z)z^n=0,&n\text{ odd},\\[2mm]
(1-3z)+2(1-z)(z^{n-1}+z^{n+1})+(3-z)z^{2n}=0,&n\text{ even}.
\end{cases}
\]
For \(n=2\), the matrix is nonnegative for every \(s\ge0\). For \(n\ge3\), the finite thresholds strictly decrease with \(n\), beginning with \(\sigma_3=1\), and
\[
\frac34<\sigma_n\le1,\qquad \lim_{n\to\infty}\sigma_n=\frac34.
\]
Their sharp parity-dependent finite-size corrections are
\[
\sigma_n=\frac34+\begin{cases}
4\,3^{-n}+O(n9^{-n}),&n\text{ odd},\\[1mm]
\dfrac{20}{3}\,3^{-n}+O(n9^{-n}),&n\text{ even}.
\end{cases}
\]
At \(s=\sigma_n\), the only zero diagonal entries of \(C_n(s)\) occur at the middle vertex (odd \(n\)) or two middle vertices (even \(n\)); every off-diagonal entry is strictly positive. For every \(s>\sigma_n\) the middle diagonal entries are negative; other diagonal entries may also become negative for larger steps.

Consequently, \(s\le3/4\) is the necessary and sufficient *mesh-size-uniform* positivity condition: it guarantees entrywise nonnegativity simultaneously for every path length \(n\ge2\), and no larger fixed value of \(s\) does so.

## Assumptions and scope
The path Laplacian has entries \((L_n)_{ii}=1\) at the two endpoints and \((L_n)_{ii}=2\) at interior vertices, with \((L_n)_{i,i+1}=(L_n)_{i+1,i}=-1\). Thus it is a symmetric finite-volume or cell-centered no-flux/reflecting path operator; it is **not** the homogeneous Dirichlet second-difference matrix, nor the alternative unsymmetrized ghost-point endpoint stencil. Unit edge weights and unit vertex masses are assumed.

For the semidiscrete heat equation \(\dot u=-(\kappa/\Delta x^2)L_nu\), the dimensionless parameter is \(s=\kappa\Delta t/(2\Delta x^2)\). In those physical units the sharp all-mesh condition is \(\kappa\Delta t/\Delta x^2\le3/2\), whereas at any fixed finite \(n\ge3\) the threshold is larger. Positivity means preservation of every nonnegative initial vector in **one end-step**; the claim does not concern internal stages or errors against the continuous heat equation.

## Proof
**1. A resolvent reduction.** Write \(G_n(s)=(I+sL_n)^{-1}\). The matrix \(I+sL_n\) is a nonsingular irreducible \(M\)-matrix for \(s>0\), so \(G_n(s)\) has strictly positive entries. Since
\[
C_n(s)=2G_n(s)-I,
\]
all off-diagonal entries of \(C_n(s)\) are positive, and entrywise nonnegativity is equivalent to \(G_n(s)_{ii}\ge1/2\) at every vertex. Also \(G_n(s)\mathbf1=\mathbf1\) and \(C_n(s)\mathbf1=\mathbf1\).

**2. Exact reflecting Green kernel.** For \(s>0\) let \(z\in(0,1)\) be the unique solution of \(s=z/(1-z)^2\). Then for indices \(1\le i,j\le n\),
\[
G_n(s)_{ij}=\frac{1-z}{1+z}\,
\frac{z^{|i-j|}+z^{i+j-1}+z^{2n-i-j+1}+z^{2n-|i-j|}}{1-z^{2n}}.
\tag{1}
\]
To verify (1), multiply \(I+sL_n\) by \((1-z)^2\). Its interior diagonal entries become \(1+z^2\), endpoint diagonal entries become \(1-z+z^2\), and neighbor entries become \(-z\). Each geometric term solves the interior recurrence away from its source because
\[
(1+z^2)z^r-z(z^{r-1}+z^{r+1})=0.
\]
The terms reflected across the half-integer endpoints impose \(u_0=u_1\) and \(u_{n+1}=u_n\). At the source, the jump of the \(z^{|i-j|}\) term is \(1-z^2\); the prefactor \((1-z)/(1+z)\) changes it to \((1-z)^2\). The geometric sum of the two reflected image trains is exactly the quotient in (1). Thus \((I+sL_n)G_n=I\); uniqueness follows from positive definiteness. Alternatively, the complete matrix identity can be checked by substitution in the tridiagonal recurrence.

**3. The central vertex is the unique obstruction.** From (1), with \(a=2i-1\),
\[
G_n(s)_{ii}=\frac{1-z}{1+z}\,
\frac{1+z^{2n}+z^a+z^{2n-a}}{1-z^{2n}}.
\]
For fixed \(0<z<1\), the sum \(z^a+z^{2n-a}\) is strictly increasing in \(|a-n|\). Therefore the smallest diagonal occurs only at the central vertex for odd \(n\), or at the central pair for even \(n\). Denote the minimum by \(H_n(z)\); it is
\[
H_n(z)=\frac{1-z}{1+z}
\begin{cases}
\dfrac{1+z^n}{1-z^n},&n\text{ odd},\\[2mm]
\dfrac{(1+z^{n-1})(1+z^{n+1})}{1-z^{2n}},&n\text{ even}.
\end{cases}
\tag{2}
\]
Every diagonal \(G_n(s)_{ii}\) is strictly decreasing in \(s\): the spectral theorem gives
\[
G_n(s)_{ii}=\frac1n+\sum_{k=1}^{n-1}\frac{|v_k(i)|^2}{1+s\lambda_k},
\]
where \(0<\lambda_1\le\cdots\le\lambda_{n-1}\) are nonzero Laplacian eigenvalues and the nonconstant squared coefficients sum to \(1-1/n>0\). Thus the minimum decreases continuously from \(1\) to \(1/n\). For \(n=2\), it is always strictly above \(1/2\) at finite \(s\). For \(n\ge3\), it crosses \(1/2\) exactly once. Setting (2) equal to \(1/2\) and clearing positive denominators gives precisely the two claimed polynomial equations. Their possible endpoint root at \(z=1\) is excluded by \(z\in(1/3,1)\). Formula (2) also shows \(H_n(1/3)>1/2\), proving \(z_n>1/3\) and \(\sigma_n>3/4\). Direct substitution for \(n=3\) gives \(\sigma_3=1\).

**4. Strict mesh-size monotonicity.** For fixed \(z\in(0,1)\), formula (2) gives, for odd \(n\),
\[
\frac{H_{n+1}(z)}{H_n(z)}=
\frac{(1-z^n)(1+z^{n+2})}{1-z^{2n+2}}<1,
\]
and, for even \(n\),
\[
\frac{H_{n+1}(z)}{H_n(z)}=
\frac{1-z^{2n}}{(1-z^{n+1})(1+z^{n-1})}<1.
\]
Both strict inequalities follow by subtracting numerator from denominator, obtaining respectively \(z^n(1-z^2)\) and \(z^{n-1}(1-z^2)\). Since each \(H_n\) is strictly decreasing in \(s\), the crossings \(\sigma_n\) strictly decrease. As \(n\to\infty\), (2) tends to \((1-z)/(1+z)\), whose unique \(1/2\) crossing is \(z=1/3\), or \(s=3/4\). This proves both the limit and the uniform sharpness statement.

**5. Parity-sensitive correction.** Let \(z_n=1/3+\delta_n\). Since \(z_n\to1/3\), eventually \(z_n<2/5\). Either polynomial equation then implies \(\delta_n=O((2/5)^{n-1})\), so \(n\delta_n\to0\). Writing \(z_n^n=3^{-n}(1+3\delta_n)^n\) in the same equations now gives \(\delta_n=O(3^{-n})\); consequently \(z_n^n=3^{-n}+O(n9^{-n})\). Expanding the odd equation yields
\[
3\delta_n=(3-z_n)z_n^n
=\frac83\,3^{-n}+O(n9^{-n}),
\]
so \(\delta_n=(8/9)3^{-n}+O(n9^{-n})\). For even \(n\), the equation gives
\[
3\delta_n=2(1-z_n)(z_n^{n-1}+z_n^{n+1})
+(3-z_n)z_n^{2n}
=\frac{40}{9}\,3^{-n}+O(n9^{-n}),
\]
so \(\delta_n=(40/27)3^{-n}+O(n9^{-n})\). Since
\[
\left.\frac{d}{dz}\frac{z}{(1-z)^2}\right|_{z=1/3}=\frac92,
\]
Taylor expansion gives the displayed coefficients \(4\) and \(20/3\). The error estimate is uniform along either parity subsequence.

## Verification
`verify.py` is a standalone standard-library Python 3 script. It constructs (1) with exact rational arithmetic, verifies \((I+sL_n)G_n=I\) and row sums, central diagonal dominance, the full off-diagonal sign pattern, and the diagonal positivity equivalence on 105 rational \((n,z)\) combinations with \(2\le n\le16\). It separately checks the exact three-vertex threshold, computes twenty root values to test the strict mesh-size trend, and tests the two parity-dependent asymptotic coefficients. All checks passed when replayed from the packaged script. The infinite statements are proved above and do not rely on this finite replay.

For illustration, \(\sigma_3=1\), \(\sigma_4\approx0.854637679718\), \(\sigma_5\approx0.767591879244\), and \(\sigma_6\approx0.759478307119\).

## Relationship to prior work
The general resolvent-return criterion for Crank–Nicolson end-step positivity on Markov generators is prior work; it is not asserted to be new. The present finding evaluates that criterion completely for **every reflecting finite path**, proves central rather than endpoint control, determines two explicit parity equations, and computes the exponentially small finite-size corrections and the sharp uniform threshold.

Higueras and Roldán (2023), Theorem 1 and its proof, establish sharp finite-mesh positivity cutoffs for the **homogeneous Dirichlet** heat difference operator. Their values increase to the Dirichlet limit \(\kappa\Delta t/\Delta x^2=2(2-\sqrt2)\), in contrast with the decreasing reflecting-path thresholds and their limit \(3/2\) obtained here. Different endpoint rows mean that their theorem does not imply the reflecting formulas. Gao and Sun (first online December 18, 2012) study **compact higher-order Neumann difference schemes**, chiefly convergence estimates; only their publisher abstract and references were accessible. That material cannot establish full-document noncoverage. A specialist full text could still contain an equivalent limit or finite-path bound; this remains an originality risk.

## Limitations
This result concerns the symmetric first-neighbor reflecting path operator with uniform rates and vertex masses; it does not cover variable diffusion coefficients, Robin boundaries, the nonsymmetric ghost-point Neumann stencil, higher-dimensional grids, or arbitrarily weighted graphs. Entrywise positivity does not imply high accuracy of large time steps. The finite checker cannot prove the all-\(n\) theorem, and independent mathematical validation has not been performed. A relevant inaccessible primary paper remains a specific priority uncertainty.

## References
1. G.-H. Gao and Z.-Z. Sun, *Compact difference schemes for heat equation with Neumann boundary conditions (II)*, Numer. Methods Partial Differential Equations 29 (2013), 1459–1486. First published online 2012-12-18. DOI: https://doi.org/10.1002/num.21760.
2. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank–Nicolson scheme for the heat equation*, arXiv:2301.01066 (2023), especially Theorem 1 and Section 6.1. https://arxiv.org/abs/2301.01066.
3. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026), public finding at https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
4. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), 309–326. DOI: https://doi.org/10.1016/S0168-9274(98)00050-6.
