# Exact Euclidean mean-square relaxation of random best response on complete networks

## Finding

For every integer \(n\ge3\) and \(0<\delta<1\), random single-agent best responses in the symmetric complete-network public-good game admit an **exact two-moment evolution**, not merely an upper rate bound. Write \(q=[1+(n-1)\delta]^{-1}\), \(e_i(t)=x_i(t)-q\), and define
\[
G_t=\mathbb E\left[\left(\sum_{i=1}^{n}e_i(t)\right)^2\right],\qquad
F_t=\mathbb E\left[\sum_{i=1}^{n}e_i(t)^2\right].
\]
For every initial profile in the explicitly specified non-clipping neighborhood below and all integers \(t\ge0\),
\[
\begin{pmatrix}G_{t+1}\\F_{t+1}\end{pmatrix}=
T_{n,\delta}\begin{pmatrix}G_t\\F_t\end{pmatrix},\qquad
T_{n,\delta}=\frac1n\begin{pmatrix}
(n-2)(1-\delta)^2&(1-\delta)^2\\
(n-2)\delta^2&n-1+\delta^2
\end{pmatrix}.
\]
Define \(a=(n-2)(1-\delta)^2\), \(b=(1-\delta)^2\), \(c=(n-2)\delta^2\), and \(d=n-1+\delta^2\). Its eigenvalues \(0<\sigma_{n,\delta}<\rho_{n,\delta}<1\) are
\[
\rho_{n,\delta}=\frac{a+d+\sqrt{(a-d)^2+4bc}}{2n},\qquad
\sigma_{n,\delta}=\frac{a+d-\sqrt{(a-d)^2+4bc}}{2n}.
\]
For every deterministic, non-equilibrium initial profile in that neighborhood,
\[
F_t=C_+\rho_{n,\delta}^{\,t}+C_-\sigma_{n,\delta}^{\,t},\qquad
C_+=\frac{F_1-\sigma_{n,\delta}F_0}{\rho_{n,\delta}-\sigma_{n,\delta}}>0,
\]
with \(C_-=F_0-C_+\). Hence \(\lim_{t\to\infty}F_t^{1/t}=\rho_{n,\delta}\); **every nonzero perturbation has the same exact asymptotic expected squared-Euclidean-error factor**. The sharp slowdown coefficients are
\[
\rho_{n,\delta}=1-\frac{2}{n}(1-\delta)+O_n((1-\delta)^2)\quad(\delta\uparrow1),
\]
\[
\rho_{n,\delta}=1-\frac{2(1-\delta)}{(2-\delta)n}+O_\delta(n^{-2})\quad(n\to\infty).
\]

## Assumptions and scope

There are \(n\ge3\) agents on the complete undirected graph, with simultaneous action space \([0,1]^n\). The payoff of agent \(i\) is \(u_i(x)=x_i-x_i^2/2-\delta x_i\sum_{j\ne i}x_j\), with \(0<\delta<1\). At each discrete step, independently of the history, one agent is selected uniformly at random and changes their effort to the (unique) constrained best response \(\max\{0,1-\delta\sum_{j\ne i}x_j\}\); all other efforts stay unchanged. Expectations are over these independent update indices and the initial profile is deterministic.

Let \(H=(1-\delta)I+\delta\mathbf 1\mathbf 1^\top\), \(m=\min\{q,1-q\}\) and \(r=m/[1+\delta\sqrt{n-1}]\). The theorem applies whenever
\[
(x(0)-q\mathbf1)^\top H(x(0)-q\mathbf1)<(1-\delta)r^2.
\]
This open ellipsoid is nonempty, lies within \([0,1]^n\), and guarantees every subsequently selected coordinate has an interior, unclipped best response. The strict inequality matters; at an arbitrary distant initial profile the exact two-moment recurrence need not hold while a response is clipped at zero.

## Proof

**Equilibrium and the non-clipping invariant.** The full-game potential is strictly concave because \(H\) is positive definite: its eigenvalues are \(1-\delta\) on the zero-sum subspace and \(1+(n-1)\delta\) on the constant vector. Thus the unique Nash equilibrium is the all-positive profile \(x^*=q\mathbf1\). The error potential \(\Phi(e)=e^\top H e\) strictly decreases whenever an unsatisfied coordinate is updated to its exact best response. More generally, the constrained best response minimizes \(\Phi\) over the selected coordinate and cannot increase it. Therefore \(\Phi(e(t))\le\Phi(e(0))<(1-\delta)r^2\) for every sample path and time, implying \(\|e(t)\|_2<r\). Because \(r<m\) and \(\delta\sqrt{n-1}\,r<m\), every candidate unconstrained new coordinate \(q-\delta\sum_{j\ne i}e_j(t)\) lies strictly between zero and one. Hence clipping never occurs.

**Moment closure.** Put \(S=\sum_i e_i\) and \(Q=\sum_i e_i^2\). Updating coordinate \(i\) sets \(e_i'=-\delta(S-e_i)\), and consequently
\[
S'=(1-\delta)(S-e_i),\qquad Q'=Q-e_i^2+\delta^2(S-e_i)^2.
\]
Averaging the squares over the uniformly random \(i\) uses exactly \(\sum_i(S-e_i)^2=(n-2)S^2+Q\). Thus the conditional expectations of \((S')^2\) and \(Q'\) give the two rows of \(T_{n,\delta}\). Taking expectations and iterating proves the displayed identity for every \(t\).

**Positive sharp eigenmode.** All four entries of \(T_{n,\delta}\) are strictly positive. Its determinant is \((n-2)(n-1)(1-\delta)^2/n^2>0\), and
\[
\det(I-T_{n,\delta})=\frac{2(1-\delta)[1+(n-1)\delta]}{n^2}>0.
\]
Both diagonal entries are strictly below one, so the positive eigenvalues obey \(0<\sigma_{n,\delta}<\rho_{n,\delta}<1\). By the spectral decomposition of the two-by-two recurrence,
\(F_t=C_+\rho_{n,\delta}^{\,t}+C_-\sigma_{n,\delta}^{\,t}\).
If \(e(0)\ne0\), then \(F_0>0\) and the second row gives \(F_1=[cG_0+dF_0]/n\ge(d/n)F_0\). Strict positivity of the off-diagonal entries implies \(\sigma_{n,\delta}<d/n\). Consequently \(C_+>0\), so the Perron root is genuinely attained for **every** nonzero initial perturbation, rather than merely a possible upper bound.

**Critical and large-population limits.** The characteristic equation is \((n\lambda-a)(n\lambda-d)=bc\). Substitution of \(\delta=1-\varepsilon\), \(\varepsilon\downarrow0\), on the larger root gives \(\rho=1-2\varepsilon/n+O_n(\varepsilon^2)\). For fixed \(\delta\in(0,1)\), substitution \(\lambda=1-\kappa/n+O_\delta(n^{-2})\) gives \(\delta(\delta-2)\kappa+2\delta(1-\delta)=0\), and therefore \(\kappa=2(1-\delta)/(2-\delta)\). The smaller eigenvalue converges to \((1-\delta)^2\), which is strictly separated from one; these expansions follow from the simple larger root.

## Verification

The standalone `checker.py` enumerates all update-index strings up to horizons four or five for nine small rational parameter instances with \(n\in\{3,4,5,6\}\) and checks the exact rational two-moment recurrence against direct enumeration. It additionally tests the positivity and characteristic equation of the larger root on a wider finite parameter grid. The program reports 145 passed assertions involving 14,744 update strings. This is a finite consistency check, not a proof of the universal statement; the preceding argument establishes the assertion for all admissible sizes, parameters, and times. Run with `python3 checker.py` using the standard Python library.

## Relationship to prior work

Misiak and Dziubiński (2026), arXiv:2602.15986, formulate exactly these linear substitute best responses and random single-agent updates, establish general probabilistic stability estimates (Theorem 3), and examine clique convergence numerically in Section 3.2.2, including slowdown near the interaction threshold. Those results do not state the two-moment Euclidean expectation identity, a sharp initial-condition-independent mean-square factor, or either coefficient above. The exact factor is not inferred by squaring a pathwise bound: expectation of squared error and norm of expected error are distinct observables.

Gower and Richtárik (2015), arXiv:1506.03296, show randomized coordinate descent is a case of a general randomized linear iteration, and give general expected squared-norm contraction inequalities (Theorem 8, Section 4.4) and exact mean-iterate evolution; such generic inequalities do not determine the present Euclidean second-moment sequence exactly. Carson and Ma (2026), arXiv:2609.15605, establish convergence bounds for asynchronous Jacobi and randomized Gauss–Seidel with communication delays, not this delay-free complete-network exact second-moment rate. The derivation is a special symmetry reduction within known randomized coordinate-update theory, not a new general convergence framework.

## Limitations

The exact closure requires complete-network symmetry, uniform independent sampling, the quadratic payoff and a non-clipping region; it is not asserted for generic graphs, heterogeneous update rates, clipped distant starts, or correlated choices. The asymptotic is in expectation and does not identify the pathwise almost-sure Lyapunov exponent. The rate is local but exact at every time for admissible initial states. Existing broader algorithms and possible unindexed exact computations pose a residual publication-priority risk. Independent scientific validation is not claimed.

## References

1. W. Misiak and M. Dziubiński, *Convergence rates of random-order best-response dynamics in public good games on networks* (2026), arXiv:2602.15986, https://arxiv.org/html/2602.15986v1 . First submitted 2026-02-17 UTC.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems* (2015), arXiv:1506.03296, https://arxiv.org/html/1506.03296v5 .
3. E. Carson and Y. Ma, *Asynchronous Jacobi and randomized Gauss–Seidel methods in shared and distributed memory: A unified convergence-rate analysis* (2026), arXiv:2609.15605, https://arxiv.org/abs/2609.15605 .
