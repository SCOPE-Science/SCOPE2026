# All-rate uniqueness and logarithmic contraction for same-sign opinion–leadership equilibria

## Finding

**Theorem (positive-sector equilibrium rigidity).** Fix an integer \(n\geq1\), a nonnegative row-stochastic matrix \(W\in\mathbb R^{n\times n}\), parameters \(\alpha,\beta>0\), and an anchor-opinion vector \(a\in(0,1]^n\). Consider the co-evolving opinion–leadership differential equations
\[
\dot x_i=-(1-y_i)(x_i-(Wx)_i)-y_i(x_i-a_i),\qquad
\dot y_i=\alpha(1-y_i)x_i^2-\beta y_i(x_i-(Wx)_i)^2.
\]
They have **exactly one equilibrium with every opinion strictly positive and every leadership in \([0,1]\)**, for every positive ratio \(\rho=\alpha/\beta\), without any connectivity, irreducibility, or small-disagreement assumption. At that equilibrium, all leadership components are strictly positive; the opinions lie between \(m=\min_i a_i\) and \(M=\max_i a_i\).

There is a globally convergent **algebraic fixed-point iteration**, distinct from the differential-equation flow, that computes this equilibrium: set \(s_i=(Wu)_i\), and let \(F_\rho(s,a)\) be the unique positive root \(r\) of
\[
r+\frac{(r-s)^3}{\rho r^2}=a.
\]
For any starting point \(u^{(0)}\in[m,M]^n\), put
\[
u_i^{(k+1)}=F_\rho((Wu^{(k)})_i,a_i).
\]
Its convergence is geometrically fast in the logarithmic sup metric: with \(d_{\log}(u,v)=\max_i|\log(u_i/v_i)|\) and
\[
q=\frac{3M(M-m)^2}{3M(M-m)^2+\rho m^3}<1,
\]
one has \(d_{\log}(u^{(k)},x^*)\le q^k d_{\log}(u^{(0)},x^*)\) for all nonnegative integers \(k\). When \(m=M\), take \(q=0\) and the iteration reaches the equilibrium in one step.

For fixed \(W,\rho\), increasing one or more anchor opinions cannot decrease any equilibrium opinion: \(a\le b\) implies \(x^*(a)\le x^*(b)\). The equilibrium varies smoothly with positive anchors and cannot undergo a positive-opinion saddle-node fold. By changing signs, the uniqueness and construction apply equally to anchors that are all strictly negative.

## Assumptions and scope

The leadership law is the **linear-in-leadership** law displayed above, not a replicator equation. The network may be directed and reducible; only \(W_{ij}\ge0\) and \(\sum_jW_{ij}=1\) are used. The positive-anchor assumption gives \(0<m\le M\le1\). The result concerns equilibrium solutions with all opinion coordinates positive, not all equilibrium solutions: the original model also admits the zero-opinion, zero-leadership equilibrium. Opposite-sign, zero, or mixed-sign anchors are outside the assertion. No global convergence or local stability statement for trajectories of the differential equations is made.

## Proof

**1. Exact scalar equilibrium reduction.** Write \(s_i=(Wx)_i\), \(d_i=x_i-s_i\), and \(\rho=\alpha/\beta>0\). Whenever \(x_i>0\), the leadership balance implies
\[
y_i=\frac{\rho x_i^2}{\rho x_i^2+d_i^2}\in(0,1].\]
Substitution into the opinion balance gives exactly
\[
d_i^3+\rho x_i^2(x_i-a_i)=0,
\]
which is equivalent to \(x_i=F_\rho(s_i,a_i)\). Conversely, any positive solution of this scalar system, together with the displayed expression for \(y_i\), satisfies both equilibrium equations. Thus no equation or boundary restriction is lost in the reduction.

**2. Single-valued monotone scalar root.** For \(s,a>0\), define \(G_s(r)=r+(r-s)^3/(\rho r^2)\) on \(r>0\). Its derivative is
\[
G_s'(r)=1+\frac{(r-s)^2(r+2s)}{\rho r^3}>0.
\]
As \(r\downarrow0\), \(G_s(r)\to-\infty\); as \(r\to\infty\), \(G_s(r)\to+\infty\). Hence the root \(G_s(r)=a\) exists uniquely. Because \(G_s(s)=s\) and \(G_s(a)-a=(a-s)^3/(\rho a^2)\), it obeys
\[
\min\{a,s\}\le F_\rho(s,a)\le\max\{a,s\}.
\]
Implicit differentiation gives \(\partial_sF_\rho\ge0\), \(\partial_aF_\rho>0\); explicitly, \(\partial_sG_s(r)=-3(r-s)^2/(\rho r^2)\le0\).

**3. Uniform logarithmic contraction.** For \(s,a,r=F_\rho(s,a)>0\), implicit differentiation yields
\[
\frac{\partial\log F_\rho(s,a)}{\partial\log s}
=\frac{3s(r-s)^2}{\rho r^3+(r-s)^2(r+2s)}
=\frac{3s(r-s)^2}{3s(r-s)^2+\rho a r^2}
\in[0,1).
\]
The second equality uses \(\rho ar^2=\rho r^3+(r-s)^3\), which is **the root equation**, not an unproved estimate. For \(s,a,r\in[m,M]\), the numerator is at most \(3M(M-m)^2\) and the remaining positive denominator term is at least \(\rho m^3\). Consequently the scalar logarithmic derivative is at most the stated \(q<1\), uniformly throughout the box.

Because each row of \(W\) consists of nonnegative weights summing to one, for any positive \(u,v\) and \(\delta=d_{\log}(u,v)\), the inequalities \(e^{-\delta}v\le u\le e^\delta v\) imply \(e^{-\delta}Wv\le Wu\le e^\delta Wv\); thus \(d_{\log}(Wu,Wv)\le d_{\log}(u,v)\). Combining this with the scalar logarithmic derivative proves \(d_{\log}(T_a u,T_a v)\le q\,d_{\log}(u,v)\), where \(T_a u=(F_\rho((Wu)_i,a_i))_i\). The root bounds from step 2 show \(T_a([m,M]^n)\subseteq[m,M]^n\). The logarithmic box is complete, so Banach's contraction theorem yields exactly one fixed point therein and the claimed error bound.

**4. No other positive equilibrium.** If \(x>0\) is any equilibrium, the leadership formula gives \(y_i>0\), and opinion balance yields \(x_i=(1-y_i)(Wx)_i+y_i a_i\). Let \(x_j\) be a greatest coordinate. If \(x_j>M\), then \((Wx)_j\le x_j\) and \(a_j<x_j\); because \(y_j>0\), their convex combination is strictly smaller than \(x_j\), contradiction. The analogous argument for a least coordinate rules out \(\min_i x_i<m\). Therefore every positive equilibrium belongs to the box and must be the Banach fixed point. Recovering leadership by step 1 proves unique positive-sector equilibrium.

**5. Order and absence of folds.** The scalar map is nondecreasing in \(s\) and strictly increasing in \(a\), and \(W\ge0\). Thus for \(a\le b\) the associated iterations satisfy \(T_a u\le T_b u\) for any positive \(u\), and each iteration preserves order. On a common positive box containing both anchor vectors, start both iterations at the same point and pass to their unique fixed points: \(x^*(a)\le x^*(b)\).

For local regularity define \(H_i(x)=x_i+(x_i-(Wx)_i)^3/(\rho x_i^2)\), so \(H(x^*)=a\). Its Jacobian \(J\) has nonpositive off-diagonal entries, namely \(J_{ij}=-3(x_i-(Wx)_i)^2W_{ij}/(\rho x_i^2)\) for \(j\ne i\). The map \(H\) is homogeneous of degree one on the positive cone, hence Euler's identity gives \(Jx^*=H(x^*)=a>0\). Therefore \(J\operatorname{diag}(x^*)\) has nonpositive off-diagonals and strictly positive row sums, making it strictly row-diagonally dominant and invertible. Its inverse is nonnegative by the standard inverse-positivity argument for a strictly diagonally dominant matrix with nonpositive off-diagonals. Accordingly \(J\) is nonsingular, \(a\mapsto x^*(a)\) is smooth by the implicit function theorem, and a fold of the positive equilibrium branch is impossible.

Under \(x\mapsto-x\) and \(a\mapsto-a\), the opinion equation changes sign and the leadership equation is unchanged, proving the all-negative counterpart.

## Verification

The accompanying standalone standard-library program `verify.py` evaluates the scalar identity, derivative signs and logarithmic contraction using exact rational identities and high-precision arithmetic; it also computes the fixed point for directed, reducible four-agent networks at three positive parameter ratios and checks the equilibrium equations and anchor-order comparison. Its finite tests supplement, rather than replace, the uniform proof. Run with `python3 verify.py` from the extracted file directory; the expected success prefix is `VERIFY_OK`.

For instance, \(W=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), \(a=(1/5,4/5)\), and \(\rho=1\) yield approximately \(x^*=(0.4087710674,0.7355170098)\) and \(y^*=(0.6101504462,0.8351783706)\). For \(\varepsilon=m=1/5\), the sufficient condition in the motivating paper's Theorem 3(ii) has left-hand side \(243\), exceeding the required upper bound \(1\), whereas the present theorem applies. This example demonstrates a genuine extension of the **equilibrium** uniqueness guarantee, not a conclusion about temporal stability.

## Relationship to prior work

Alutto, Zino, Johansson and Fontan [1] introduce the differential equations, derive their cubic equilibrium equation (their Eq. (5)), and prove a restricted sufficient uniqueness/convergence criterion (their Theorem 3(ii)); their Corollary 5 treats the uniform-anchor case. The present result reuses their model and cubic reduction, but replaces the sufficient **equilibrium** restriction in the same-sign sector with an all-positive-parameter theorem; the core added device is the implicit scalar-root map and its strict logarithmic derivative bound.

The same authors' subsequent leadership-emergence preprint [2] studies a distinct game-theoretic replicator law \(\dot y_i=y_i(1-y_i)(\rho_i x_i^2-(x_i-(Wx)_i)^2)\), rather than the linear-in-leadership law in [1], so its equilibrium statements do not imply this theorem. Reynolds and Tudisco [3] study different friction-inspired nonlinear stubbornness equations; their Nash-equilibrium uniqueness result does not specialize to the cubic condition here. The FJ-MM work [4] modifies linear Friedkin–Johnsen updates with memory and higher-order neighbors and does not contain endogenous leadership governed by the cubic balance.

## Limitations

The result is a statement about existence, uniqueness, monotone comparative statics and a **numerical fixed-point algorithm for equilibria**, not about the stability or convergence of solutions of the nonlinear ODE. It does not exclude the original system's zero-opinion equilibrium or classify equilibria when some anchors vanish or have opposing signs. Strongly mixed initial opinions, time-varying networks, stochastic learning and the replicator variant are not treated. No claim of exhaustive uniqueness in all related literature is made; standard nonlinear positive-operator results may offer equivalent abstract formulations.

## References

[1] M. Alutto, L. Zino, K. H. Johansson and A. Fontan, *On a Co-evolving Opinion-Leadership Model in Social Networks*, arXiv:2603.24381v1 (first public 2026-03-25), https://arxiv.org/html/2603.24381v1 .

[2] M. Alutto, L. Zino, K. H. Johansson and A. Fontan, *On Leadership Emergence in Opinion Dynamics on Social Networks*, arXiv:2606.05825v1 (2026-06-04), https://arxiv.org/abs/2606.05825 .

[3] D. N. Reynolds and F. Tudisco, *Unique Nash equilibrium of a nonlinear model of opinion dynamics on networks with friction-inspired stubbornness*, arXiv:2304.07556 (2023), https://arxiv.org/abs/2304.07556 .

[4] R. Raineri, L. Zino and A. Proskurnikov, *FJ-MM: The Friedkin–Johnsen Opinion Dynamics Model with Memory and Higher-Order Neighbors*, arXiv:2504.06731v1 (2025), https://arxiv.org/abs/2504.06731 .
