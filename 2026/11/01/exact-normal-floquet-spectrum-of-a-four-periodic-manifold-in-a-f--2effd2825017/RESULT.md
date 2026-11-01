# Exact normal Floquet spectrum of a four-periodic manifold in a fifth-order rational recurrence

## Finding
Consider the autonomous, four-component fifth-order recurrence (1) below with a common parameter \(p>0\), \(p\ne1\). Its positive four-periodic states form a smooth \(12\)-dimensional submanifold \(\mathcal M_p\) of the \(20\)-dimensional history space. At **every** state in this manifold, the return map \(F_p^4\) has the exact derivative spectrum
\[
\operatorname{spec}D(F_p^4)|_{\mathcal M_p}=\{1\text{ (multiplicity }12),\ p^2\text{ (multiplicity }8)\}.
\]
Both eigenvalues are semisimple. Consequently, for \(0<p<1\), sufficiently close histories approach a (generally different) four-periodic state exponentially under the return map, while no individual four-periodic state attracts a full neighborhood. For \(p>1\), all these periodic states are linearly unstable, with eight expanding directions. In particular, the four-periodic states of the \(p=2\) specialization illustrated in the source have eight transverse return multipliers exactly \(4\).

## Assumptions and scope
Let \(x_n,y_n,w_n,z_n\) be strictly positive and define
\[
\begin{aligned}
x_{n+1}&=\frac{x_{n-3}y_{n-4}}{y_n\,[p+(1-p)x_{n-3}y_{n-4}w_{n-1}z_{n-2}]},\\
y_{n+1}&=\frac{y_{n-3}w_{n-4}}{w_n\,[p+(1-p)y_{n-3}w_{n-4}z_{n-1}x_{n-2}]},\\
w_{n+1}&=\frac{w_{n-3}z_{n-4}}{z_n\,[p+(1-p)w_{n-3}z_{n-4}x_{n-1}y_{n-2}]},\\
z_{n+1}&=\frac{z_{n-3}x_{n-4}}{x_n\,[p+(1-p)z_{n-3}x_{n-4}y_{n-1}w_{n-2}]}.
\end{aligned}\tag{1}
\]
The phase state comprises all four component histories at times \(n-4,\ldots,n\), hence belongs to \((0,\infty)^{20}\). The one-step map is denoted by \(F_p\); it is locally defined and smooth near each positive four-periodic state for every stated parameter. When \(0<p<1\), all its denominators remain positive on the entire positive state space. Here four-periodic includes minimal periods \(1\), \(2\), and \(4\).

In a periodic sixteen-coordinate block indexed by \(j\in\mathbb Z/4\mathbb Z\), set
\[
P_j=x_{j+1}y_jw_{j+3}z_{j+2}.
\]
Then \(\mathcal M_p\) consists exactly of histories extending a positive block periodically, with \(P_j=1\) for all four residues \(j\). There are sixteen freely positive block entries subject to four independent smooth constraints, so \(\dim\mathcal M_p=12\). These constraints are independent because \(P_j\) contains the otherwise unique entry \(x_{j+1}\).

## Proof
**Periodic states and dimension.** On a four-periodic block, each numerator in (1), divided by its adjacent variable, is the prescribed next-period value. Equality with the recurrence therefore requires its denominator to equal \(1\). Since \(p\ne1\), this condition is equivalent to the corresponding cyclic product equalling \(1\). The four component equations correspond to the four products \(P_j\). Conversely, these four product identities force all equations for all indices. In logarithmic block coordinates the four constraints have independent gradients (the coefficients of \(\log x_{j+1}\) form an identity submatrix). The resulting positive manifold is smooth and twelve-dimensional, and \(F_p^4\) fixes it pointwise.

**Logarithmic derivative.** Write \(X_n,Y_n,W_n,Z_n\) for infinitesimal perturbations of the logarithms of the four components along any four-periodic state. Since every cyclic product equals \(1\), its denominator is \(p+(1-p)\cdot1=1\). Differentiating the logarithm of the first equation of (1) gives
\[
X_{n+1}=pX_{n-3}+pY_{n-4}-Y_n+(p-1)(W_{n-1}+Z_{n-2}).\tag{2}
\]
The other three equations follow by cyclic replacement \(X\to Y\to W\to Z\to X\). In the history ordering \((X_{n-4},\ldots,X_n;Y_{n-4},\ldots,Y_n;W_{n-4},\ldots,W_n;Z_{n-4},\ldots,Z_n)\), denote the associated constant \(20\times20\) one-step matrix by \(T_p\). Its coefficient matrix is the same at all four phases and all points of \(\mathcal M_p\). Thus the derivative of the return map, in logarithmic coordinates, is \(T_p^4\).

**Cyclic Fourier factorization.** Complexify and decompose the four component labels into characters \(q\) with \(q^4=1\). Substituting \((X_n,Y_n,W_n,Z_n)=\lambda^n(1,q,q^2,q^3)\) into (2) gives
\[
L_q(\lambda)=\lambda^5+q\lambda^4-(p-1)q^2\lambda^3-(p-1)q^3\lambda^2-p\lambda-pq.
\]
The four factors are
\[
\begin{aligned}
L_1&=(\lambda+1)(\lambda^2+1)(\lambda^2-p),\\
L_{-1}&=(\lambda-1)(\lambda^2+1)(\lambda^2-p),\\
L_{i}&=(\lambda-1)(\lambda+1)(\lambda+i)(\lambda^2+p),\\
L_{-i}&=(\lambda-1)(\lambda+1)(\lambda-i)(\lambda^2+p).
\end{aligned}
\]
Consequently,
\[
\det(\lambda I-T_p)=(\lambda-1)^3(\lambda+1)^3(\lambda^2+1)^3(\lambda^2-p)^2(\lambda^2+p)^2.
\]
For \(p>0\) and \(p\ne1\), the five roots of each \(L_q\) are distinct. Each Fourier-mode companion block, and therefore \(T_p\), is diagonalizable over \(\mathbb C\). Raising its eigenvalues to the fourth power gives exactly twelve unit multipliers and eight multipliers \(p^2\), semisimply. Alternatively, direct matrix multiplication yields the exact identity
\[
(T_p^4-I)(T_p^4-p^2I)=0
\]
and trace \(\operatorname{tr}(T_p^4)=12+8p^2\).

**Local dynamics.** At any point of \(\mathcal M_p\), the eigenspace of multiplier \(1\) contains the twelve-dimensional tangent space because \(F_p^4\) fixes the manifold pointwise. Equality of their dimensions identifies the entire unit eigenspace with that tangent space. The eight-dimensional normal spectrum is \(p^2\). If \(0<p<1\), smooth local coordinates \((\theta,\xi)\) straightening \(\mathcal M_p\) put the return map into the form
\[
(\theta,\xi)\mapsto(\theta+O(\|\xi\|),\ p^2\xi+O(\|\xi\|^2)),
\]
with the estimates uniform in a small coordinate box. After choosing a sufficiently small box, normal displacements decay geometrically and tangential drift is summable; shrinking the initial box if necessary, iterates remain inside, and \(\theta\) converges. Hence each sufficiently close orbit converges exponentially to a point of \(\mathcal M_p\) under \(F_p^4\). The manifold's positive dimension excludes asymptotic attraction of any single periodic state. For \(p>1\), the eight multipliers \(p^2>1\) give Lyapunov instability of every periodic state via the standard unstable-eigenvalue criterion for differentiable maps.

## Verification
The standalone \(`verification/check_floquet.py`\) constructs \(T_p\) directly from the four logarithmic recurrences, evaluates \(T_p^4\), and checks the full characteristic polynomials, the annihilating identity, exact traces, and the dimensions of the unit-multiplier eigenspaces at \(p=2\) and \(p=1/2\). It uses symbolic rather than approximate arithmetic and completed all five asserted checks. The universal statement follows from the analytical Fourier decomposition and local-map argument above, not from finitely many sampled parameters.

## Relationship to prior work
Murovhi, Folly-Gbetoula and Anani (2026), Theorem 2.1, derive a four-periodicity criterion for their more general nonautonomous rational recurrences and provide a \(p=2\) numerical illustration. Their affine reciprocal-product reductions (equations (39)–(42)) already exhibit the scalar factor \(AE=p^2\) on the present common-parameter slice; this scalar factor and their reconstruction formulas (45)–(52) are explicitly credited. What those equations do not state is the complete original twenty-dimensional return derivative, the twelve-dimensional semisimple unit eigenspace, the full eight-dimensional transverse multiplicity, or the local manifold-attraction theorem. Deriving the original history-space spectrum and interpreting the unit directions are the additions here. The \(p>1\) instability of those periodic examples and the \(0<p<1\) normally attracting manifold are the additional conclusions here. Elsayed and Alofi (2023) treat related autonomous sign cases; their full article was not accessible during this comparison, so possible prior overlap there is a residual priority risk. Other stability treatments listed below concern distinct lower-order or different-parameter systems, rather than the return map (1).

## Limitations
The result is local to the positive periodic manifold and does not claim global attraction or exclude other attractors. It is restricted to a common autonomous parameter, \(p>0\), \(p\ne1\); it does not classify general nonautonomous coefficients or the degenerate parameter \(p=1\). A transverse contraction to an invariant manifold does not mean convergence to a predesignated periodic orbit. Historical-priority assessment is subject to the explicitly stated inaccessible related article; independent mathematical validation has not been performed.

## References
1. T. Murovhi, M. Folly-Gbetoula, and K. Anani, *Analytical Methods for Solving Non-Autonomous Higher-Order Nonlinear Difference Equations*, arXiv:2610.24657v1 (first publicly posted 2026-10-17), https://arxiv.org/html/2610.24657v1 ; especially system (1), Theorem 2.1, and conclusion.
2. E. M. Elsayed and B. S. Alofi, *The periodic nature and expression on solutions of some rational systems of difference equations*, Alexandria Engineering Journal **74** (2023), 269–283, https://doi.org/10.1016/j.aej.2023.05.026 (full text inaccessible during comparison).
3. K. Mkhwanazi and M. Folly-Gbetoula, *Invariance Analysis and Dynamics of Difference Equations*, Journal of Applied Nonlinear Dynamics **14** (2025), 483–498, https://doi.org/10.5890/JAND.2025.06.015 (different recurrence family; only abstract accessible).
4. B. S. Alofi and A. S. Alofi, *Behavior of solutions of higher-order difference equations*, AIMS Mathematics **11** (2026), 13485–13499, https://doi.org/10.3934/math.2026555 (distinct recurrence family; publisher abstract and figure descriptions inspected).
