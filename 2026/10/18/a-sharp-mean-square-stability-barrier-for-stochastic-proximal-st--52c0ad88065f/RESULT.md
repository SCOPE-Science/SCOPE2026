# A sharp mean-square stability barrier for stochastic proximal steps with momentum variance reduction

## Finding

For the exact, constant-parameter SPAM method of Karagulyan, Shulgin, Sadiev, and Richtárik, consider independently and equiprobably sampled convex scalar losses
\[
f_0(x)=0,\qquad f_2(x)=x^2.
\]
Their average is the strongly convex objective \(f(x)=x^2/2\), with common minimizer \(0\). Fix momentum-refresh parameter \(p=1/2\) and proximal stepsize \(t>0\). Define
\[
F(t)=3t^5+19t^4+5t^3-54t^2-54t-12
\]
and let \(t_\star\) be its unique positive zero, satisfying
\[
1.797<t_\star<1.798,\qquad t_\star=1.79714225327545\ldots.
\]
The exact SPAM recursion converges in mean square to the minimizer from **every deterministic augmented initial state** if and only if \(0<t<t_\star\). At \(t=t_\star\), the standard compatible initialization \(x_{-1}=x_0=1\), \(g_{-1}=0\) fails to converge in mean square; at each \(t>t_\star\) its expected squared primal iterate grows at least geometrically.

In particular, at \(t=2\) the signed expected augmented state tends to zero for every initial state, with eigenvalue moduli \(1/2\) and \(\sqrt{2/5}\), whereas from the stated standard initialization \(\mathbb E[x_k^2]\) grows exponentially. The mean-square operator has a real eigenvalue \(1.09935065080672\ldots>1\). Thus first-moment stability can coexist with an increasing squared optimization error even though **each client objective is convex and each proximal subproblem is solved exactly**.

## Assumptions and scope

The client sample at every iteration is fresh, independent of prior samples, and equals curvature \(a_k=0\) or \(a_k=2\), each with probability \(1/2\). All calculations are in exact real arithmetic; the algorithm is the exact-SPAM branch of Algorithm 1 in arXiv:2405.20127v1, with \(p_k=1/2\) and \(\gamma_k=t\) constant. For \(k\ge0\), its estimator and proximal recursion are
\[
g_k=a_k x_k+\frac12(g_{k-1}-a_kx_{k-1}),
\qquad
x_{k+1}=\operatorname{prox}_{t f_{a_k}}\!\left(x_k+t(a_kx_k-g_k)\right).
\]
Here \(f_a(x)=ax^2/2\); thus \(f_0=0\) and \(f_2=x^2\). The augmented state is \(z_k=(x_k,x_{k-1},g_{k-1})^\top\). The all-initial-states stability assertion allows arbitrary deterministic \(z_0\); the instability witness uses the compatible algorithm initialization \(x_{-1}=x_0=1\), \(g_{-1}=0\).

The two scalar client gradients do **not** have bounded uniform variance over the whole real line: \(\operatorname{Var}(\nabla f_{a_k}(x))=x^2\). Accordingly, this theorem is not a counterexample to the source paper's convergence theorem, which assumes a global uniform gradient-variance bound as well as a sufficiently small stepsize.

## Proof

**1. Exact algorithm map.** For \(a\in\{0,2\}\), the proximal minimization gives
\[
x_{k+1}=x_k-\frac{t}{1+ta}g_k.
\]
Consequently \(z_{k+1}=M_a(t)z_k\), where
\[
M_a(t)=\begin{pmatrix}
(1+ta)^{-1}&ta/[2(1+ta)]&-t/[2(1+ta)]\\
1&0&0\\
a&-a/2&1/2
\end{pmatrix}.
\]
Let the positive operator \(\mathcal L_t\) act on real symmetric \(3\times3\) matrices by
\[
\mathcal L_t(Q)=\tfrac12M_0(t)QM_0(t)^\top+
\tfrac12M_2(t)QM_2(t)^\top.
\]
Independence of samples yields \(Q_k:=\mathbb E[z_kz_k^\top]=\mathcal L_t^k(z_0z_0^\top)\). Hence mean-square decay from every deterministic augmented state is equivalent to \(\rho(\mathcal L_t)<1\). Indeed, this condition suffices by finite-dimensional spectral theory; conversely a positive operator has a nonzero positive-semidefinite spectral-radius eigenmatrix, which is a sum of rank-one initial covariances.

**2. Exact threshold.** In the symmetric-coordinate order \((Q_{11},Q_{12},Q_{13},Q_{22},Q_{23},Q_{33})\), form the \(6\times6\) matrix \(C(t)\) of \(\mathcal L_t\) by applying it to each symmetric matrix unit (with both off-diagonal entries set to one). Exact rational algebra gives
\[
\boxed{\det(I_6-C(t))=-\frac{tF(t)}{16(2t+1)^3}.}
\]
The full symbolic calculation is reproduced by the standalone checker. The coefficient signs of \(F\), in descending order, are \(+,+,+,-,-,-\); Descartes' rule of signs and the opposite signs at \(0\) and positive infinity show that \(F\) has exactly one positive zero. Direct rational evaluation brackets that zero between \(1797/1000\) and \(1798/1000\).

We exhibit a strict quadratic mean-square Lyapunov certificate at \(t=1/2\):
\[
P=\frac1{1619}\begin{pmatrix}
14776&-1960&-1227\\
-1960&4005&-1193\\
-1227&-1193&3235
\end{pmatrix}\succ0,
\quad
P-\tfrac12\sum_{a\in\{0,2\}}M_a(1/2)^\top P M_a(1/2)=I_3.
\]
All three leading principal minors of \(P\) are strictly positive. Thus \(\rho(\mathcal L_{1/2})<1\). At \(t=2\), the determinant above equals \(-13/125<0\); since \(\det(\lambda I_6-C(2))\) is monic and positive for sufficiently large real \(\lambda\), it has a real zero above \(1\), whence \(\rho(\mathcal L_2)>1\).

The operator \(\mathcal L_t\) preserves the closed solid cone of positive-semidefinite matrices. The finite-dimensional Perron--Frobenius theorem for such cone-preserving operators ensures that \(\rho(\mathcal L_t)\) is a nonnegative real eigenvalue; the spectral radius is continuous in \(t>0\). Therefore any transition between \(\rho<1\) and \(\rho>1\) must occur where \(\det(I_6-C(t))=0\). Since the latter has exactly one positive root, the sign regions just established extend to **every** positive \(t\):
\[
\rho(\mathcal L_t)<1\ (0<t<t_\star),\qquad
\rho(\mathcal L_{t_\star})=1,\qquad
\rho(\mathcal L_t)>1\ (t>t_\star).
\]

**3. Failure from compatible initialization, including the endpoint.** For \(z_0=(1,1,0)^\top\), two covariance updates yield a positive-semidefinite \(Q_2\) with exact determinant
\[
\det Q_2=\frac{t^4(10t^2+14t+7)}{128(2t+1)^4}>0.
\]
Thus \(Q_2\succ0\). The adjoint \(\mathcal L_t^*(Y)=\tfrac12\sum_aM_a(t)^\top YM_a(t)\) has a nonzero positive-semidefinite eigenmatrix \(Y_t\) at eigenvalue \(\rho=\rho(\mathcal L_t)\). Accordingly, for every \(n\ge2\),
\[
\operatorname{tr}(Y_tQ_n)=\rho^{n-2}\operatorname{tr}(Y_tQ_2)>0.
\]
To transfer this growth to the primal coordinate, let \(E_{11}=\operatorname{diag}(1,0,0)\). The two-step observability matrix \(O_2=(\mathcal L_t^*)^2(E_{11})\) is positive semidefinite and has exact determinant
\[
\det O_2=\frac{9t^6(2t+3)^2(2t^2+2t+1)}{1024(2t+1)^6}>0.
\]
Hence \(O_2\succ0\). Since \(\operatorname{tr}(Y_tQ_n)\le \|Y_t\|_2\operatorname{tr}(Q_n)\), there exists a positive constant \(c(t)\) such that
\[
\boxed{\mathbb E[x_{n+2}^2]=\operatorname{tr}(O_2Q_n)\ge c(t)\rho^{n-2}\quad(n\ge2).}
\]
For \(t=t_\star\) the right-hand side stays positive; for \(t>t_\star\) it grows exponentially. For \(0<t<t_\star\), by contrast, the matrix power \(C(t)^k\) tends to zero and hence \(\mathbb E[x_k^2]\to0\) from every deterministic augmented initial state.

**4. A strictly stable signed mean with exploding squared error.** At \(t=2\), the signed-mean matrix \(B=\tfrac12(M_0(2)+M_2(2))\) satisfies
\[
\det(\lambda I_3-B)=\frac{(2\lambda-1)(5\lambda^2-3\lambda+2)}{10}.
\]
All three eigenvalues lie strictly inside the unit circle. Yet
\[
\det(\lambda I_6-C(2))=
\frac{\lambda(1000\lambda^5-1070\lambda^4-119\lambda^3+225\lambda^2-168\lambda+28)}{1000},
\]
whose positive root above one lies between \(1.099\) and \(1.100\). The lower bound from Step 3 demonstrates exponentially growing expected squared **primal** error for compatible initialization despite decay of \(\mathbb E[z_k]\).

## Verification

Run `python verify_spam.py` with SymPy installed. This self-contained checker reconstructs both sampled SPAM step matrices from the estimator and proximal formulas, builds their lifted covariance operator on all six symmetric coordinates, verifies the exact threshold determinant and the positivity certificate, checks the two-step covariance and observability determinants, and reproduces the signed-mean and mean-square characteristic polynomials at \(t=2\). It also checks forty direct symbolic-rational proximal updates and direct enumeration of both clients over two steps. The output is a PASS message plus the threshold approximation. These finite computations verify displayed algebraic identities; they do not independently certify literature priority or replace the cone-spectral argument proving the infinite-horizon statements.

## Relationship to prior work

Karagulyan, Shulgin, Sadiev, and Richtárik (2024, Algorithm 1, Section 3 and Appendix A) introduced SPAM and analyzed convergence under Hessian similarity, uniformly bounded stochastic-gradient variance and stepsize restrictions. Their results neither assert an exact all-stepsize mean-square threshold for this two-client example nor cover its unbounded gradient-variance regime.

A separate publicly available calculation titled *Exact first-moment stability frontier for two-client scalar SPAM* derives the general **signed first-moment** condition \((2-p)\rho^2t^2<(1+t)^2\) for two quadratic clients. That result expressly excludes mean-square claims. At the present example's \(p=1/2\), \(\rho=1\), \(t=2\), its condition is satisfied, while the exact second-moment operator here has spectral radius above one. Thus that result does not imply this theorem and highlights why the distinction matters.

Kim, Toulis, and Kyrillidis (2022) study direct heavy-ball momentum on stochastic proximal iterates, rather than momentum-variance reduction inside a same-sample shifted proximal step. Loizou and Richtárik (2017) also study heavy-ball variants of stochastic proximal algorithms, not the sampled estimator recursion displayed here. Results for those updates do not provide this covariance characteristic polynomial without an additional algorithm-specific reduction.

## Limitations

This is a sharp result only for one canonical two-client scalar family with equal sampling probabilities, refresh parameter \(p=1/2\), exact proximal solutions, and independent sampling. The observed effect is not a contradiction to the source convergence theorem because the example violates its globally bounded gradient-variance hypothesis; its stepsize also exceeds the theorem's sufficient regime near the instability boundary. No assertion is made about finite-precision stability, unequal sampling, higher-dimensional objectives, or almost-sure convergence. In particular, convergence of signed means is not a convergence guarantee for individual stochastic iterates.

## References

1. A. Karagulyan, E. Shulgin, A. Sadiev, and P. Richtárik, *SPAM: Stochastic Proximal Point Method with Momentum Variance Reduction for Non-convex Cross-Device Federated Learning*, arXiv:2405.20127v1, first posted 2024-05-30, https://arxiv.org/html/2405.20127v1.
2. *Exact first-moment stability frontier for two-client scalar SPAM*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-first-moment-stability-frontier-for-two-client-scalar-spam--170ca03b5dee (material inspected: `RESULT.md`).
3. J. L. Kim, P. Toulis, and A. Kyrillidis, *Convergence and Stability of the Stochastic Proximal Point Algorithm with Momentum*, PMLR 168 (2022), https://proceedings.mlr.press/v168/kim22a.html.
4. N. Loizou and P. Richtárik, *Momentum and Stochastic Momentum for Stochastic Gradient, Newton, Proximal Point and Subspace Descent Methods*, arXiv:1712.09677, first posted 2017-12-27, https://arxiv.org/abs/1712.09677.
