# Exact mean-square relaxation frontier and transient-growth window for two-row averaged Kaczmarz

## Finding

For averaged randomized Kaczmarz on two equally weighted normalized, nonparallel rows with absolute correlation \(0<c<1\) and independent minibatches of integer size \(q\ge1\), there are two distinct sharp relaxation thresholds. For a fixed common positive relaxation \(\alpha\), **global mean-square convergence from every nonzero deterministic initial error** holds precisely when

\[
0<\alpha<\alpha_{\mathrm{ms}}(q,c)
:=\frac{4}{1+\sqrt{c^2+(1-c^2)/q^2}}.
\]

In contrast, **one-step conditional mean-square nonexpansion at every possible initial error** holds exactly when

\[
0\le\alpha\le\alpha_{\mathrm{one}}(q,c)
:=\frac{4}{1+c+(1-c)/q}.
\]

For \(q>1\), these thresholds are strictly ordered: \(2<\alpha_{\mathrm{one}}<\alpha_{\mathrm{ms}}<4/(1+c)\). Thus, a nonempty interval of relaxations admits some transient expected-error amplification yet guarantees geometric mean-square convergence. At the exact mean-square boundary the error tends to a positive nonzero limit; above it, it grows exponentially. The asymptotic convergence factor has a unique rate-minimizing \(\alpha_*\in(1,2)\), with explicit high-coherence behavior described below.

## Assumptions and scope

Let \(a_1,a_2\in\mathbb R^2\) be distinct normalized linearly independent row vectors, with \(|\langle a_1,a_2\rangle|=c\in(0,1)\). By changing one row's sign, which does not affect its projection, take their inner product to be \(c\). Consider a consistent system \(a_i^\top x=b_i\) and its unique solution \(x^\star\). At iteration \(n\), choose \(i_{n,1},\ldots,i_{n,q}\) independently, each uniformly in \(\{1,2\}\), with fresh independent draws at each \(n\). Update

\[
x_{n+1}=x_n-\frac{\alpha}{q}\sum_{j=1}^q a_{i_{n,j}}(a_{i_{n,j}}^\top x_n-b_{i_{n,j}}).
\]

The update uses all rows at the same current iterate. The two basis directions are the normalized sum and difference of the two rows; changing the sign of a row if necessary gives the chosen orientation. Set

\[
p=\frac{1+c}{2},\qquad r=\frac{1-c}{2},\qquad u=pr=\frac{1-c^2}{4}.
\]

In this orthonormal basis the row vectors are \((\sqrt p,\sqrt r)\) and \((\sqrt p,-\sqrt r)\). All assertions are for fixed finite \(q\), fixed \(c\in(0,1)\), exact arithmetic, and any deterministic \(x_0\ne x^\star\).

## Proof

**1. Exact covariance reduction.** Put \(e_n=x_n-x^\star\) and let \(K_n\) be the number of the \(q\) selections of the first row. Writing \(\xi_n=(2K_n-q)/q\), we have \(\mathbb E\xi_n=0\) and \(\mathbb E\xi_n^2=1/q\). The one-step random error map is

\[
e_{n+1}=M(\xi_n)e_n,\qquad
M(\xi)=\begin{pmatrix}
1-\alpha p&-\alpha\sqrt u\,\xi\\
-\alpha\sqrt u\,\xi&1-\alpha r
\end{pmatrix}.
\]

Let \(d_n=(\mathbb E(e_{n,1}^2),\mathbb E(e_{n,2}^2))^\top\). Independence of current sampling from the past, and the first two moments of \(\xi\), give the exact deterministic recurrence

\[
d_{n+1}=T_q(\alpha,c)d_n,\qquad
T_q=\begin{pmatrix}
(1-\alpha p)^2&\alpha^2u/q\\
\alpha^2u/q&(1-\alpha r)^2
\end{pmatrix}.
\]

This is a closed recurrence for diagonal covariance entries even when the two coordinates are correlated. Since all entries of \(T_q\) are nonnegative and its off-diagonal entries are strictly positive, its Perron eigenvalue \(R_q\) governs the expected squared error \(\mathbb E\|e_n\|_2^2=\boldsymbol 1^\top T_q^n d_0\). Both \(\boldsymbol1\) and \(d_0\) have strictly positive pairing with the Perron eigenvector when \(e_0\ne0\). Thus

\[
\lim_{n\to\infty}\bigl(\mathbb E\|e_n\|_2^2\bigr)^{1/n}=R_q;
\]

if \(R_q=1\), the expectation tends to a strictly positive constant, and if \(R_q>1\), it increases exponentially asymptotically. Direct diagonalization of the symmetric two-by-two matrix yields

\[
R_q=1-\alpha+\frac{\alpha^2(1+c^2)}4+
\frac{\alpha}{2}\sqrt{c^2(2-\alpha)^2+
\frac{\alpha^2(1-c^2)^2}{4q^2}}.
\]

**2. Sharp mean-square boundary.** A two-by-two positive-definiteness test shows \(R_q<1\) exactly when \(I-T_q\) is positive definite. The determinant identity is

\[
\det(I-T_q)=\alpha^2u\left(4-2\alpha+
\alpha^2u(1-q^{-2})\right).
\]

For \(q=1\), its positive nonzero root is \(2\). For \(q>1\), the smaller positive root is \(\alpha_{\mathrm{ms}}=4/[1+\sqrt{c^2+(1-c^2)/q^2}]\), while the larger root lies beyond \(2/p\). The smaller root is strictly below \(2/p\), so \(1-(1-\alpha p)^2>0\) throughout \(0<\alpha\le\alpha_{\mathrm{ms}}\). Hence \(I-T_q\) is positive definite exactly below the displayed threshold; between the roots its determinant is negative, and at or beyond \(2/p\) its first diagonal is nonpositive. This settles every \(\alpha>0\), including equality and supercritical behavior. The same conclusion holds at \(q=1\) directly from the determinant and the diagonal test.

**3. Sharp one-step frontier and a separation witness.** Using \(\mathbb E\xi=0\),

\[
\mathbb E\bigl[M(\xi)^\top M(\xi)\bigr]=
\operatorname{diag}\!\left((1-\alpha p)^2+\alpha^2u/q,
(1-\alpha r)^2+\alpha^2u/q\right).
\]

Both diagonal entries are at most one precisely when \(0\le\alpha\le\min\{2/(p+r/q),2/(r+p/q)\}\). As \(p>r\), this is the stated \(\alpha_{\mathrm{one}}=2/(p+r/q)\). Its strict difference from the mean-square threshold for \(q>1\) follows from

\[
\left(c+\frac{1-c}{q}\right)^2-
\left(c^2+\frac{1-c^2}{q^2}\right)
=\frac{2c(1-c)(q-1)}{q^2}>0.
\]

For example, choose \(q=2\), \(c=3/5\), \(\alpha=9/4\), and initial error aligned with the row bisector. Then

\[
T_2=\begin{pmatrix}16/25&81/200\\81/200&121/400\end{pmatrix},
\qquad \mathbb E\|e_1\|^2=\frac{209}{200}\|e_0\|^2>\|e_0\|^2.
\]

Nevertheless, \(I-T_2\) is positive definite: its first diagonal is \(9/25\), and \(\det(I-T_2)=3483/40000>0\). Hence \(\mathbb E\|e_n\|^2\to0\) geometrically for **every** initial error.

**4. Unique fastest fixed relaxation.** Write \(T_q(\alpha)=I-2\alpha\operatorname{diag}(p,r)+\alpha^2H_q\), where \(H_q=\begin{pmatrix}p^2&u/q\\u/q&r^2\end{pmatrix}\succeq0\). Its largest eigenvalue is simple for \(\alpha>0\), with a strictly positive normalized eigenvector \(v\). Standard differentiation of a simple top eigenvalue gives

\[
R_q''(\alpha)=2v^\top H_qv+
\frac{2|w^\top T_q'(\alpha)v|^2}{R_q(\alpha)-\lambda_-(\alpha)}>0,
\]

where \(w\) is the orthonormal second eigenvector. Even at \(q=1\), the first summand is positive because \(v\) is strictly positive and \(H_q\) is positive on positive vectors. At \(\alpha=1\), \(T_q'(1)=2u\begin{pmatrix}-1&1/q\\1/q&-1\end{pmatrix}\); the Perron Rayleigh derivative is negative for \(q>1\), and for \(q=1\) it is negative because \(c>0\) makes \(v\) not proportional to \((1,1)\). At \(\alpha=2\), the Perron vector is \((1,1)/\sqrt2\) and \(R_q'(2)=c^2+(1-c^2)/q>0\). Therefore the unique global minimizer of \(R_q\) lies strictly between \(1\) and \(2\) and is characterized by \(R_q'(\alpha_*)=0\).

For fixed \(q\) and \(\delta=1-c\downarrow0\), the minimizing relaxation approaches two. With \(\alpha=2-k\sqrt\delta\) and fixed \(k>0\), expanding the positive simple eigenvalue, or using the larger diagonal entry and second-order Schur correction, gives uniformly on compact positive \(k\)-intervals

\[
R_q(2-k\sqrt\delta,1-\delta)
=1-2\delta+\left(k+\frac{2}{kq^2}\right)\delta^{3/2}+O_{q,k}(\delta^2).
\]

The unique minimum of the displayed coefficient occurs at \(k=\sqrt2/q\). Comparing the minimum with a fixed positive choice of \(k\) excludes scales with \((2-\alpha_*)/\sqrt\delta\to0\) or \(\infty\): either the off-diagonal Schur correction or the weak-coordinate diagonal loss would then exceed the displayed \(\delta^{3/2}\) optimum. Strict convexity gives the unique limiting stationary coefficient \(k=\sqrt2/q\); the uniform differentiated expansion gives an \(O_q(\sqrt\delta)\) correction to \(k\). Therefore

\[
\alpha_*=2-\frac{\sqrt{2\delta}}q+O_q(\delta),\qquad
R_q(\alpha_*,1-\delta)=1-2\delta+
\frac{2\sqrt2}{q}\delta^{3/2}+O_q(\delta^2).
\]

## Verification

The accompanying `verify.py` uses exact rational arithmetic to check the covariance recurrence against explicit binomial minibatch averaging, across several rational correlations, batch sizes, relaxations, and four time steps. It also checks the determinant factorization, the rational transient-growth witness, and finite diagnostic samples of the sharp thresholds. Floating-point high-coherence optimization checks the leading asymptotic constants; these numerical checks are supplementary, not proofs of quantification over infinitely many parameters. Execute `python3 verify.py` in a standard Python installation.

## Relationship to prior work

Moorman, Tu, Molitor, and Needell introduced the averaged randomized Kaczmarz update, proved one-step contraction bounds for consistent systems, and selected relaxation by optimizing those bounds [1, sections 1, 3--5, appendix]. Their Theorem 2 selects the fastest **guarantee**, not the exact asymptotic covariance growth rate. The threshold \(\alpha_{\mathrm{one}}\) above is the specialization of their one-step contraction calculation; it is not asserted to be novel. The new difference is an exact infinite-horizon transition \(\alpha_{\mathrm{ms}}>\alpha_{\mathrm{one}}\) and its transient-growth witness, together with the exact optimizer of the asymptotic rate on the correlated two-row family. Richtárik and Takáč [2] treat broader sketch-and-project algorithms and analyze optimized convergence guarantees, without stating this two-row covariance threshold. Tondji and Lorenz [3] study sparse Bregman-Kaczmarz averaging and optimize a different rate bound. Earlier exact MSE work [4] concerns classical non-averaged randomized Kaczmarz and row-selection probabilities, not the simultaneous independent-minibatch relaxation frontier. These are statement-level comparisons, not a claim of exhaustive priority coverage.

## Limitations

This is an exact result for two independent normalized rows in \(\mathbb R^2\), not a general bound for arbitrary matrices, noisy or inconsistent systems, alternative sampling probabilities, adaptive steps, variable minibatch sizes, asynchronous updates, or floating-point effects. The fastest relaxation minimizes the infinite-horizon expected squared-error exponent, **not** the error at every finite time or the wall-clock runtime. The asymptotic coefficient is for fixed finite \(q\) as \(c\uparrow1\), not a joint limit where \(q\) also grows. A literature search does not establish global uniqueness of the mathematical result.

## References

[1] J. D. Moorman, T. K. Tu, D. Molitor, D. Needell, *Randomized Kaczmarz with Averaging*, arXiv:2002.04126v1 (first publicly posted 2020-02-10), https://arxiv.org/html/2002.04126v1.

[2] P. Richtárik, M. Takáč, *Stochastic Reformulations of Linear Systems: Algorithms and Convergence Theory*, arXiv:1706.01108, https://arxiv.org/pdf/1706.01108.

[3] L. Tondji, D. A. Lorenz, *Faster randomized block sparse Kaczmarz by averaging*, Numerical Algorithms 93 (2023), DOI:10.1007/s11075-022-01473-x, https://link.springer.com/article/10.1007/s11075-022-01473-x.

[4] A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, IEEE GlobalSIP 2014, DOI:10.1109/GLOBALSIP.2014.7032145, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b.
