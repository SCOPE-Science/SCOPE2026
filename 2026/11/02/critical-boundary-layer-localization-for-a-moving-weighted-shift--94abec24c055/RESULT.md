# Critical boundary-layer localization for a moving weighted-shift defect

## Finding
For integers \(L\ge1\) and \(t>0\), define the unilateral weighted shift \(W_{L,t}\) on the complex Hilbert space \(\ell^2(\mathbb N_0)\) by \(W_{L,t}e_j=w_je_{j+1}\), where \(w_{L-1}=t\) and every other \(w_j=1\). Write \(\omega_{L,t}=\sup_{\|x\|_2=1}|\langle W_{L,t}x,x\rangle|\).

The exact threshold is
\[
\omega_{L,t}=1\quad\Longleftrightarrow\quad t^2\le1+L^{-1}.
\]
Above this threshold there is a unique \(\kappa>0\) satisfying
\[
t^2-1=\frac{e^{2\kappa}-1}{1-e^{-2L\kappa}},\qquad
\omega_{L,t}=\cosh\kappa>1.
\]
These fixed-\(L\) statements are preparatory special cases of established finite-boundary Jacobi spectral methods, **not asserted to be new**.

The main critical-window statement is the following. Fix any real \(\beta\) and, for all sufficiently large \(L\), set \(t_L=\sqrt{1+\beta/L}\). If \(\beta\le1\), then \(\omega_{L,t_L}=1\); if \(\beta>1\), there exists exactly one \(y_\beta>0\) satisfying
\[
\beta=\frac{2y_\beta}{1-e^{-2y_\beta}}.
\]
In the latter case,
\[
\lim_{L\to\infty}L^2(\omega_{L,t_L}-1)=\frac{y_\beta^2}{2}.
\]
For each \(L\), let \(v^{(L)}\) be the uniquely normalized strictly positive eigenvector of \((W_{L,t_L}+W_{L,t_L}^*)/2\) at eigenvalue \(\omega_{L,t_L}>1\). Then the rescaled step functions
\[
F_L(s)=\sqrt{L}\,v^{(L)}_{\lfloor Ls\rfloor}\quad(s\ge0)
\]
converge strongly in \(L^2([0,\infty))\) to the norm-one function
\[
F_\beta(s)=\frac{u_\beta(s)}{\left(\int_0^\infty u_\beta(r)^2\,dr\right)^{1/2}},\qquad
u_\beta(s)=\begin{cases}
\sinh(y_\beta s)/\sinh(y_\beta),&0\le s\le1,\\
e^{-y_\beta(s-1)},&s\ge1.
\end{cases}
\]
In particular the fraction of squared eigenvector mass *before* the exceptional edge converges to the exact value
\[
\boxed{\ \lim_{L\to\infty}\sum_{j=0}^{L-1}|v^{(L)}_j|^2
=\frac{\sinh(2y_\beta)-2y_\beta}{e^{2y_\beta}-1-2y_\beta}\ }.
\]
This fraction rises from \(0\) at the spectral threshold \(\beta\downarrow1\) toward \(1/2\) as \(\beta\to\infty\). No positive eigenvalue above the essential spectral edge exists in the subcritical or critical case.

## Assumptions and scope
All operators are on complex \(\ell^2(\mathbb N_0)\). The edge between vertices \(L-1\) and \(L\) is the sole modified edge, and the perturbation is positive. The scaling parameter \(\beta\in\mathbb R\) is held fixed as \(L\to\infty\); a positive \(t_L\) exists for every sufficiently large \(L\). Convergence of profiles means norm convergence with respect to Lebesgue measure in the specified \(L^2\) space, not merely pointwise convergence. The ratio concerns eigenvectors only in the strictly supercritical regime \(\beta>1\). The underlying numerical radius is the complex Hilbert-space numerical radius, not the Banach-space spatial numerical radius at other exponents.

## Proof
**Reduction to a half-line Jacobi problem.** Diagonal unimodular conjugations rotate a unilateral weighted shift through arbitrary phases, so its numerical range is a disk centered at zero and its numerical radius is \(\|H_{L,t}\|\) for \(H_{L,t}=(W_{L,t}+W_{L,t}^*)/2\). Let \(J_{L,t}=2H_{L,t}\). It is the half-line Jacobi adjacency operator with zero diagonal and positive adjacent weights \(w_j\). The free Jacobi matrix has spectrum \([-2,2]\). Since \(J_{L,t}\) is a finite-rank perturbation, its essential spectrum remains \([-2,2]\). Sign alternation of coordinates changes \(J_{L,t}\) to \(-J_{L,t}\), and thus \(\omega_{L,t}=\frac12\sup\sigma(J_{L,t})\ge1\).

**Exact eigenvalue condition.** For a spectral point \(2\cosh\kappa>2\), with \(\kappa>0\), an \(\ell^2\) eigenvector satisfies \(x_{-1}=0\) and the free recurrence \(x_{j-1}+x_{j+1}=2\cosh(\kappa)x_j\) away from the exceptional edge. Every nonzero solution is therefore proportional on the left to \(\sinh((j+1)\kappa)\) for \(0\le j<L\), and on the right to \(e^{-k\kappa}\) at index \(j=L+k\), \(k\ge0\). Normalize \(x_{L-1}=1\). The two exceptional-vertex equations give
\[
x_L=\frac{\sinh((L+1)\kappa)}{t\sinh(L\kappa)}
\quad\text{and}\quad t=e^\kappa x_L,
\]
so
\[
t^2=\frac{e^\kappa\sinh((L+1)\kappa)}{\sinh(L\kappa)}
=1+\frac{e^{2\kappa}-1}{1-e^{-2L\kappa}}.
\]
The rightmost expression is strictly increasing from \(1+1/L\) to infinity: differentiating the logarithm of the hyperbolic-sine quotient shows derivative \(1+(L+1)\coth((L+1)\kappa)-L\coth(L\kappa)>0\), because \(a\mapsto a\coth(a\kappa)\) is strictly increasing for \(a>0\). Consequently a positive outlier exists if and only if \(t^2>1+1/L\), and the matching solution is a strictly positive, unique-up-to-scalar, square-summable eigenvector. The recursion rules out any other positive outlier and also rules out an \(\ell^2\) eigenvector at the band edge. This completes the fixed-depth statements.

**Critical scaling.** Put \(\kappa_L=y_L/L\). When \(\beta>1\), the outlier equation becomes
\[
\beta=G_L(y_L):=\frac{L(e^{2y_L/L}-1)}{1-e^{-2y_L}}.
\]
Each \(G_L\) increases continuously from \(1\) to infinity, and uniformly on compact positive intervals it tends to \(G(y)=2y/(1-e^{-2y})\). The limiting \(G\) is strictly increasing from \(1\) to infinity: its derivative has the sign of \(1-e^{-2y}(1+2y)>0\) for \(y>0\). Thus a compact bracketing argument implies \(y_L\to y_\beta\), the unique positive root of \(G(y)=\beta\). Since \(\omega_{L,t_L}=\cosh(y_L/L)\), the claimed scaled spectral limit follows. When \(\beta\le1\), the finite-depth threshold gives \(\omega_{L,t_L}=1\).

**Eigenvector profile and localization mass.** Use the unnormalized positive eigenvector with \(x_{L-1}=1\):
\[
x_j=\frac{\sinh((j+1)y_L/L)}{\sinh(y_L)}\quad(0\le j<L),\qquad
x_{L+k}=c_L e^{-ky_L/L}\quad(k\ge0),
\]
where
\[
c_L=\frac{\sinh((L+1)y_L/L)}{t_L\sinh(y_L)}\longrightarrow1.
\]
The left norm satisfies a Riemann-sum limit
\[
\frac1L\sum_{j=0}^{L-1}x_j^2\longrightarrow
I(y_\beta)=\int_0^1\frac{\sinh^2(y_\beta s)}{\sinh^2(y_\beta)}\,ds
=\frac{\sinh(2y_\beta)-2y_\beta}{4y_\beta\sinh^2(y_\beta)}.
\]
The infinite right norm is an exact geometric sum:
\[
\frac1L\sum_{k=0}^\infty x_{L+k}^2
=\frac{c_L^2}{L(1-e^{-2y_L/L})}
\longrightarrow\frac1{2y_\beta}.
\]
The rescaled step profiles converge pointwise except possibly at \(s=1\) to the piecewise function \(u_\beta\) given above; for large \(L\) their tails are bounded by a common integrable exponential envelope because \(y_L\to y_\beta>0\). Dominated convergence and convergence of the normalization constants therefore give the asserted strong \(L^2\) limit. Dividing the left norm by the total norm yields \(I/(I+1/(2y_\beta))\), which simplifies algebraically to the displayed hyperbolic ratio. Its endpoint limits follow from Taylor expansion at zero and exponential dominance at infinity. This proves all claims.

## Verification
The accompanying stand-alone program `check_boundary_layer.py` recomputes characteristic roots using bisection, verifies eigenvector three-term recurrences, compares isolated eigenvalues with finite tridiagonal sections, and checks continuum spectral and mass limits numerically over several depths and coupling regimes. It reports 2723 successful diagnostic comparisons in one run. These finite computations are corroborative only: the infinite-dimensional eigenvalue uniqueness, threshold, and strong-convergence claims follow from the analytical arguments above. Run with Python 3 and SciPy installed: `python check_boundary_layer.py`.

## Relationship to prior work
The finite-rank half-line Jacobi reduction, Chebyshev recurrences, and exact methods for the numerical radius of an eventually constant weighted shift are established, including Undrakh–Nakazato–Vandanjav–Chien (2015), Theorem 3.2 and the finite-boundary determinantal formula. Chakraborty–Ojha–Birbonshi (2022) develops comparable determinantal approaches. Sharif (2023) studies the numerical-radius norm of general weighted shifts and a fixed boundary defect. This note does **not** claim novelty for those methods, individual finite-depth secular equations, or the numerical radius of a fixed first-edge perturbation. Its narrower contribution is the simultaneous defect-depth/strength critical window and the strongly convergent normalized continuum eigenmode with the explicit left-mass phase law; these statements do not appear in the inspected portions of those sources.

## Limitations
The eigenmode convergence requires \(\beta>1\) fixed; the limit is not uniform at \(\beta=1\), where no normalized top eigenvector exists. The exact result applies only to a single moving positive edge defect and only to Hilbert-space numerical radius. Prior general Jacobi recurrence formulae encompass the fixed-depth algebra. An equivalent scaling result in the broader discrete-Schrödinger/half-line Jacobi literature remains a bibliographic possibility. No external independent mathematical verification is asserted.

## References
1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876, first public version 2023-03-02. https://arxiv.org/abs/2303.00876.
2. B. Undrakh, H. Nakazato, A. Vandanjav, and M.-T. Chien, *The Numerical Radius of a Weighted Shift Operator*, Electronic Journal of Linear Algebra 30 (2015), 944–963. https://journals.uwyo.edu/index.php/ela/article/download/1617/1617/.
3. B. Chakraborty, S. Ojha, and R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, Operators and Matrices 16 (2022), 1155–1174. https://files.ele-math.com/articles/oam-16-75.pdf.
