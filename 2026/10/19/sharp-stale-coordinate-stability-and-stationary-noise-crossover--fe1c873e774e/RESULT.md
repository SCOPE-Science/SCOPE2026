# Sharp stale-coordinate stability and stationary-noise crossover in randomized two-variable relaxation

## Finding

For an SPD two-variable linear system, an asynchronous coordinate update can use a current local coordinate and a one-update-old remote coordinate. In the normalized setting below, this rule has the **exact** mean-square stability frontier
\[
0<\beta<\beta_{\mathrm{crit}}(r):=\frac{4}{1+\sqrt{1+4r^2}}.
\]
Within that interval, adding independent, centered update noise of variance \(\sigma^2>0\) yields the exact limiting per-coordinate mean squared error
\[
V_{\mathrm{stale}}=
\frac{\sigma^2(2-\beta r^2)}{\beta(1-r^2)(4-2\beta-\beta^2r^2)}.
\]
For the otherwise identical fresh-read coordinate iteration, the limiting error is
\[
V_{\mathrm{fresh}}=\frac{\sigma^2}{\beta(2-\beta)(1-r^2)}.
\]
Their exact difference is
\[
\boxed{V_{\mathrm{stale}}-V_{\mathrm{fresh}}=
\frac{2\sigma^2r^2(\beta-1)}{(2-\beta)(1-r^2)(4-2\beta-\beta^2r^2)}.}
\]
Hence a one-step stale remote read strictly **reduces** the asymptotic per-coordinate noise floor for \(0<\beta<1\), agrees with the fresh-read noise floor at \(\beta=1\), and strictly **increases** it for \(1<\beta<\beta_{\mathrm{crit}}(r)\). This comparison concerns stationary second moments, not iteration count or time to convergence. The stability frontier is sharp for convergence in mean square from **every** deterministic initial history.

## Assumptions and scope

Let \(0<r<1\) and \(A=\begin{pmatrix}1&r\\r&1\end{pmatrix}\), a real symmetric positive-definite matrix. Consider homogeneous error coordinates \(e_k\in\mathbb R^2\), equivalently the error in solving \(Ax=b\). Fix a deterministic finite initial history \((e_{-1},e_0)\), an independent sequence of fair coordinate selections \(I_k\in\{1,2\}\), a relaxation parameter \(\beta>0\), and mutually independent scalar update noises \(\xi_k\) with \(\mathbb E\xi_k=0\), \(\mathbb E\xi_k^2=\sigma^2\) (no Gaussian assumption). All randomness is independent of the initial history.

For the **stale-remote** iteration, if \(I_k=1\), set
\[
e_{k+1,1}=(1-\beta)e_{k,1}-\beta r e_{k-1,2}+\xi_k,\qquad e_{k+1,2}=e_{k,2};
\]
if \(I_k=2\), interchange indices 1 and 2. The own-coordinate read is current; only the cross-coordinate read is delayed by exactly one global update. This is distinct from delaying both reads or simultaneously committing two updates. For the **fresh-remote** comparator, replace the stale cross-coordinate by its current value, retaining exactly one uniformly chosen coordinate and the same noise law and per-update noise variance. Mean-square stability means \(\mathbb E\|e_k\|_2^2\to0\) for every deterministic initial history when \(\sigma^2=0\). Limiting squared errors in the formulas above refer to \(\sigma^2>0\) and \(k\to\infty\).

## Proof

**Step 1: An exact covariance operator.** Put \(z_k=(e_{k,1},e_{k,2},e_{k-1,1},e_{k-1,2})^\top\). Then
\[
z_{k+1}=T_{I_k}z_k+\xi_k v_{I_k},\quad
T_1=\begin{pmatrix}1-\beta&0&0&-\beta r\\0&1&0&0\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
T_2=\begin{pmatrix}1&0&0&0\\0&1-\beta&-\beta r&0\\1&0&0&0\\0&1&0&0\end{pmatrix},
\]
where \(v_1=(1,0,0,0)^\top\) and \(v_2=(0,1,0,0)^\top\). With \(\mathcal L(X)=(T_1XT_1^\top+T_2XT_2^\top)/2\) and \(Q=\sigma^2\operatorname{diag}(1,1,0,0)/2\), independence and centering give the exact second-moment recursion \(X_{k+1}=\mathcal L(X_k)+Q\), without distributional assumptions beyond the stated second moments.

**Step 2: Solve the stationary equations.** Exchanging coordinate labels commutes with \(\mathcal L\) and fixes \(Q\). A swap-invariant symmetric matrix at stationarity has the form
\[
X=\begin{pmatrix}a&b&c&d\\b&a&d&c\\c&d&a&b\\d&c&b&a\end{pmatrix}.
\]
Direct expansion of \(X=\mathcal L(X)+Q\) gives
\[
\begin{aligned}
a&=\tfrac12[1+(1-\beta)^2]a-\beta r(1-\beta)d+\tfrac12\beta^2r^2a+\tfrac12\sigma^2,\\
b&=(1-\beta)b-\beta rc,\\
c&=(1-\tfrac12\beta)a-\tfrac12\beta rd,\\
d&=(1-\tfrac12\beta)b-\tfrac12\beta rc.
\end{aligned}
\]
The second and fourth relations give \(b=d=-rc\). The third gives \(c=(2-\beta)a/(2-\beta r^2)\) whenever the denominator is nonzero; elimination without division by that denominator yields the unique swap-invariant solution for \(\beta\ne\beta_{\mathrm{crit}}\):
\[
X_*=\frac{\sigma^2}{D}
\begin{pmatrix}
u&-rv&v&-rv\\-rv&u&-rv&v\\v&-rv&u&-rv\\-rv&v&-rv&u\end{pmatrix},\quad
D=\beta(1-r^2)(4-2\beta-\beta^2r^2),\quad u=2-\beta r^2,\quad v=2-\beta.
\]
The two-parameter block structure makes the four commuting symmetry eigenmodes explicit. At \(4-2\beta-\beta^2r^2=0\), the stationary equations imply \(0=\sigma^2(2-\beta r^2)\), impossible because \(0<r<1\), \(\sigma^2>0\), and \(\beta_{\mathrm{crit}}<2\).

**Step 3: Prove the exact stability threshold, not just its sufficiency.** The four eigenvalues of \(DX_*/\sigma^2\) are
\[
\beta(1-r^2),\quad\beta(1-r^2),\quad
(1-r)[4-\beta(1-r)],\quad(1+r)[4-\beta(1+r)].
\]
For \(0<\beta<\beta_{\mathrm{crit}}\) one has \(0<\beta<2\), \(D>0\), and all these eigenvalues strictly positive. Hence \(X_*\succ0\). Furthermore,
\[
X_*-\mathcal L^2(X_*)=Q+\mathcal L(Q)\succ0:
\]
the first term has a positive-definite current-coordinate block and \(\mathcal L(Q)\) has a positive-definite previous-coordinate block, so their sum is positive definite. It follows that \(\mathcal L^2(X_*)\preceq\gamma X_*\) for some \(0\le\gamma<1\). Since \(\mathcal L\) preserves positive semidefiniteness, any deterministic initial second-moment matrix is dominated by a multiple of \(X_*\) and its homogeneous second moments contract geometrically over two-update blocks. The same contraction proves \(X_k\to X_*\) under positive update noise, irrespective of the initial history.

For necessity, if the homogeneous iteration were mean-square stable for every deterministic history, then \(\mathcal L^k(zz^\top)\to0\) for every \(z\), and rank-one symmetric matrices span the finite-dimensional symmetric matrix space. Thus the spectral radius of \(\mathcal L\) would be strictly less than one; the convergent series \(\sum_{j\ge0}\mathcal L^j(Q)\) would be a positive semidefinite stationary solution. Averaging this solution under coordinate swapping would produce a swap-invariant positive semidefinite stationary solution. At the boundary no stationary solution exists. Above the boundary, every swap-invariant solution has an eigenvalue
\[
\frac{\sigma^2}{4-2\beta-\beta^2r^2}<0
\]
(the temporally antisymmetric modes), which is incompatible with positive semidefiniteness. Thus homogeneous universal mean-square stability is impossible whenever \(\beta\ge\beta_{\mathrm{crit}}\). The stationary per-coordinate variance equals \(X_{*,11}=\sigma^2u/D\), proving the stale formula.

**Step 4: Compare against current reads.** The fresh-read transition is \(e_{k+1}=U_{I_k}e_k+\xi_k\hat v_{I_k}\), with
\[
U_1=\begin{pmatrix}1-\beta&-\beta r\\0&1\end{pmatrix},\qquad
U_2=\begin{pmatrix}1&0\\-\beta r&1-\beta\end{pmatrix}.
\]
For \(0<\beta<2\), each deterministic selected-coordinate step decreases the quadratic energy \(e^\top A e\) by \(\beta(2-\beta)[(Ae)_i]^2\); averaging gives a strict contraction. The stationary covariance has diagonal \(a\) and offdiagonal \(-ra\). Its exact covariance balance gives \(a=\sigma^2/[\beta(2-\beta)(1-r^2)]\). Subtracting this expression from the stale stationary diagonal and factoring gives the boxed difference. All denominator factors are positive in the common stability interval, so the sign is exactly the sign of \(\beta-1\). At \(\beta\uparrow\beta_{\mathrm{crit}}\), the stale variance diverges.

## Verification

The standalone Python 3 script `artifacts/verify_asynchronous.py` uses only the standard library. It constructs both random-update matrices, checks the full four-by-four stationary Lyapunov identity entrywise for hundreds of positive rational parameter choices, checks all four covariance eigenvalue identities, checks the fresh-read two-by-two Lyapunov identity, and checks the exact sign-change formula, totaling 6,908 successful rational assertions. These finite checks do not establish the theorem; the universal proof is the covariance identity, positive-definite two-step certificate, and necessity argument above.

## Relationship to prior work

Carson and Ma (arXiv:2609.15605, first public 2026-09-14), Sections 3–5, formulate asynchronous Jacobi/randomized Gauss–Seidel with locally current and remotely delayed components, and prove a **sufficient** convergence-rate condition for general SPD systems. Their Theorem 1 and discussion do not give the sharp two-coordinate stability boundary above or an additive-noise stationary covariance comparison. The earlier exact delay-distribution law for two-coordinate randomized Gauss–Seidel published in published-finding corpus (2026-09-20, record `9ae0040f2dac`) treats **unrelaxed exact overwrites** and a noise-free scalar norm recurrence for bounded delay distributions; it explicitly excludes general relaxation parameters and stationary noise. At \(\beta=1\), that model includes the noise-free special case here, so no novelty is claimed for that overlap. Beidas and Papavassilopoulos (1993) establish general second-moment sufficient conditions for random-delay asynchronous linear iterations; Verkama (1996) studies random coordinate relaxation; Moga and Dubois (1995) analyze two-variable random delays. The specific *sharp* relaxation threshold and *opposite-sign* exact stationary-noise comparison are the present claims. General convergence criteria should not be confused with necessary-and-sufficient conditions in this model.

## Limitations

The conclusion is for two equal-diagonal normalized SPD variables, independent uniform single-coordinate selection, precisely one-step stale **cross** reads, constant relaxation, additive independent centered finite-variance update noise, and exact arithmetic. It is not a result for time-varying/multi-step/correlated delays, simultaneous commits, or arbitrary matrix dimension. The reduction in stationary noise at \(\beta<1\) does not imply faster convergence, reduced wall-clock cost, or improved transient error. Earlier specialized results might subsume parts of the theorem; a complete full-text comparison with the 1993 Beidas–Papavassilopoulos article was not possible.

## References

1. E. Carson and Y. Ma, *Asynchronous Jacobi and randomized Gauss–Seidel methods in shared and distributed memory: A unified convergence-rate analysis*, arXiv:2609.15605v1, 2026-09-14. https://arxiv.org/html/2609.15605v1
2. *Exact delay-distribution law for two-coordinate randomized Gauss-Seidel*, published-finding corpus mathematical research record, 2026-09-20, identifier `9ae0040f2dac`. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-exact-stochastic-delay-law-randomized-gauss-seidel--9ae0040f2dac
3. B. F. Beidas and G. P. Papavassilopoulos, *Convergence analysis of asynchronous linear iterations with stochastic delays*, Parallel Computing 19 (1993), 281–302. https://doi.org/10.1016/0167-8191(93)90038-M
4. M. Verkama, *Random Relaxation of Fixed-Point Iteration*, SIAM J. Sci. Comput. 17 (1996), 906–912. https://doi.org/10.1137/0917058
5. A. C. Moga and M. Dubois, *Performance of Asynchronous Linear Iterations with Random Delays*, USC technical report CENG 95-06 (1995). https://ceng.usc.edu/techreports/1995/Dubois%20CENG%2095-06.pdf
