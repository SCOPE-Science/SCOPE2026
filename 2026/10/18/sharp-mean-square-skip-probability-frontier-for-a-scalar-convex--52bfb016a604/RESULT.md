# Sharp mean-square skip-probability frontier for a scalar convex RandProx model

## Finding

Consider the Bernoulli-skip primal-dual proximal algorithm described below. With fixed unit primal and dual stepsizes, there is a sharp update-probability threshold
\[
p_*=\frac{\sqrt{73}-7}{12}=0.128666978776\ldots.
\]
For every probability \(p\in(0,1]\) and every nonzero deterministic starting primal-dual pair, the complete mean-square classification is:

1. If \(p>p_*\), the expected squared norm of the primal-dual state tends to zero geometrically.
2. If \(0<p<p_*\), it grows at least geometrically.
3. At \(p=p_*\), an expected positive-definite quadratic energy is exactly conserved, implying two-sided positive bounds on the expected squared norm at every iteration.

Thus reducing the probability of computing a dual proximal update, *without adjusting the dual stepsize*, crosses from convergence to mean-square instability even on a strictly convex one-dimensional problem. No assertion about almost-sure divergence is made.

## Assumptions and scope

The optimization problem is
\[
\min_{x\in\mathbb R}\bigl(g(x)+h(Kx)\bigr),\qquad
K=1,\qquad f=0,\qquad g(x)=h(x)=\frac{x^2}{2}.
\]
Its unique primal and dual solution is \((x_*,u_*)=(0,0)\), with \(h^*(u)=u^2/2\). In the *RandProx-Skip* iteration of Condat and Richtárik [1, Algorithm 5], set the *fixed* parameters \(\gamma=\tau=1\), independent of \(p\in(0,1]\). At each step draw an independent Bernoulli variable \(\delta_k\) with \(\mathbb P(\delta_k=1)=p\). Starting from deterministic \(z_0=(x_0,u_0)^\mathsf T\ne0\), compute
\[
\widehat x_k=\operatorname{prox}_{g}(x_k-u_k)=\frac{x_k-u_k}{2}.
\]
If \(\delta_k=0\), put \(u_{k+1}=u_k\) and \(x_{k+1}=\widehat x_k\). If \(\delta_k=1\), put
\[
u_{k+1}=\operatorname{prox}_{h^*}(u_k+\widehat x_k)=\frac{x_k+u_k}{4},\qquad
x_{k+1}=\widehat x_k-\frac{u_{k+1}-u_k}{p}.
\]
The two linear update matrices, acting on \(z_k=(x_k,u_k)^\mathsf T\), are therefore
\[
M_0=\begin{pmatrix}1/2&-1/2\\0&1\end{pmatrix},\qquad
M_1(p)=\begin{pmatrix}1/2-1/(4p)&-1/2+3/(4p)\\1/4&1/4\end{pmatrix}.
\]
The probability \(p=0\) is excluded because the correction divides by \(p\). Mean-square stability means \(\mathbb E\|z_k\|_2^2\to0\) as \(k\to\infty\).

## Proof

For any symmetric matrix \(S\), define the positive congruence map
\[
\mathcal L_p(S)=(1-p)M_0^\mathsf T S M_0+pM_1(p)^\mathsf T S M_1(p).
\]
Conditional expectation gives
\(\mathbb E[z_{k+1}^\mathsf T S z_{k+1}\mid z_k]
=z_k^\mathsf T\mathcal L_p(S)z_k\).

Write
\[
D(p)=6p^2+7p-1,\qquad
W(p)=\begin{pmatrix}
p(15p+13)&9p-5\\
9p-5&(12p^2+7p+9)/p
\end{pmatrix}.
\]
Direct exact multiplication establishes the *polynomial Lyapunov identity*
\[
W(p)-\mathcal L_p(W(p))=2D(p)I_2,\qquad p>0.
\]
The leading principal minor of \(W(p)\) is \(p(15p+13)>0\) and its determinant is
\[
\det W(p)=4(3p+1)(15p^2+10p+23)>0.
\]
Thus \(W(p)\) is positive definite for every \(p>0\). The polynomial \(D(p)\) has exactly one positive root, \(p_*=(\sqrt{73}-7)/12\); its sign is negative below this root and positive above it.

If \(p>p_*\), define \(P(p)=W(p)/(2D(p))\). It is positive definite and satisfies
\[
\mathcal L_p(P)=P-I_2.
\]
Since \(\mathcal L_p(P)\) is positive semidefinite, \(P\succeq I_2\). Let \(a=\lambda_{\max}(P)\) and \(b=\lambda_{\min}(P)>0\). The conditional drift identity yields
\[
\mathbb E[z_{k+1}^\mathsf T Pz_{k+1}]
=\mathbb E[z_k^\mathsf T Pz_k]-\mathbb E\|z_k\|_2^2
\le(1-a^{-1})\mathbb E[z_k^\mathsf T Pz_k].
\]
Consequently, for every deterministic \(z_0\),
\[
\mathbb E\|z_k\|_2^2
\le\frac{a}{b}(1-a^{-1})^k\|z_0\|_2^2.
\]
This proves geometric mean-square convergence.

If \(0<p<p_*\), the matrix \(Q(p)=-W(p)/(2D(p))\) is positive definite and obeys
\(\mathcal L_p(Q)=Q+I_2\). Let \(c=\lambda_{\max}(Q)\) and \(d=\lambda_{\min}(Q)\). Then
\[
\mathbb E[z_{k+1}^\mathsf T Q z_{k+1}]
=\mathbb E[z_k^\mathsf T Q z_k]+\mathbb E\|z_k\|_2^2
\ge(1+c^{-1})\mathbb E[z_k^\mathsf T Qz_k].
\]
Hence, for every nonzero deterministic \(z_0\),
\[
\mathbb E\|z_k\|_2^2
\ge\frac{d}{c}(1+c^{-1})^k\|z_0\|_2^2.
\]
This is strict geometric mean-square growth, not merely failure of a proposed convergence bound.

At \(p=p_*\), the polynomial identity reduces to \(\mathcal L_{p_*}(W)=W\). Therefore
\[
\mathbb E[z_k^\mathsf T W(p_*)z_k]=z_0^\mathsf T W(p_*)z_0=:V_0>0
\]
for every \(k\ge0\). With \(a_*=\lambda_{\max}(W(p_*))\) and \(b_*=\lambda_{\min}(W(p_*))\),
\[
\frac{V_0}{a_*}\le\mathbb E\|z_k\|_2^2\le\frac{V_0}{b_*},
\qquad k\ge0.
\]
This proves the boundary classification. All inequalities include exactly the stated quantifiers, and no inference from finite simulation is used.

## Verification

The standalone file `verify.py` reconstructs the two update matrices, checks both matrix Lyapunov identities and the determinant factorization symbolically, and independently checks
\[
\det(I_3-B(p))=\frac{6p^2+7p-1}{16},
\]
where \(B(p)\) advances the three covariance entries. It also enumerates every Bernoulli history through six updates for five rational probabilities and three nonzero initial states, comparing exact rational path sums with the moment lift. Run `python verify.py` after installing the packages in `requirements.txt`. The verifier reports 111 exact algebraic and finite-horizon consistency checks. The proof above—not those finite checks—establishes the infinite-horizon statements.

## Relationship to prior work

Condat and Richtárik [1] introduce the underlying RandProx-Skip algorithm and prove broad linear-convergence results. Their general sufficient condition specializes here to \(\gamma\tau/p\le1\), which with the fixed choice \(\gamma=\tau=1\) covers only \(p=1\). It does not assert instability below one, nor give the exact transition \(p_*\). Their appendix describes the reduction to ProxSkip only when \(\tau=p/\gamma\), not for the fixed \(\tau=1\) family considered here.

Mishchenko and collaborators [2] analyze ProxSkip with its probability-scaled proximal parameter. The distinct update map in [2] does not give the fixed-dual-step Lyapunov identity or its critical probability. More general randomized primal-dual convergence results supply context but do not, by themselves, compute this specialized sharp boundary.

## Limitations

The finding applies only to the exact stated scalar, strongly convex model, fixed unit stepsizes, iid Bernoulli update decisions, and full-state expected squared error. It is not a stability claim for arbitrary convex functions, parameter choices, ProxSkip, nor for sampling without replacement. Below the threshold, mean-square growth does not establish almost-sure growth; at the threshold the invariant expectation does not classify sample paths. An equivalent spectral calculation in less directly related literature might predate this treatment; independent priority review has not been performed.

## References

[1] L. Condat and P. Richtárik, *RandProx: Primal–Dual Optimization Algorithms with Randomized Proximal Updates*, first publicly posted 2022-07-26, arXiv:2207.12891. Relevant material: Algorithm 5, Appendix A.1, Theorem 1 and its proof. https://arxiv.org/abs/2207.12891

[2] K. Mishchenko, G. Malinovsky, S. U. Stich, and P. Richtárik, *ProxSkip: Yes! Local Gradient Steps Provably Lead to Communication Acceleration! Finally!*, first posted 2022-02-18, arXiv:2202.09357. Relevant material: Algorithm 1, Section 3 and Appendix B. https://arxiv.org/abs/2202.09357
