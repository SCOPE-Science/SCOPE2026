# No constant heavy-ball momentum improvement under scalar stochastic curvature

## Finding
Consider stochastic interpolation quadratics \(f(x;H)=Hx^2/2\), with random nonnegative curvature \(H\). The exact asymptotic **uniform mean-square contraction factor** of Polyak heavy-ball with fixed step \(\eta>0\) and fixed momentum \(0\le\beta<1\) is the spectral radius \(R(\eta,\beta)\) of its second-moment evolution. If the curvature variance \(v\) is strictly positive, then

\[
\boxed{\inf_{\eta>0,\ 0\le\beta<1} R(\eta,\beta)
=\frac{v}{\mu^2+v},\qquad
(\eta_*,\beta_*)=\left(\frac{\mu}{\mu^2+v},0\right).}
\]

The minimizing pair is unique: **every strictly positive constant momentum produces a strictly worse uniform mean-square factor**, at every step size. In addition, the exact open stability region is

\[
\boxed{0<\eta<\frac{2\mu(1-\beta^2)}{\mu^2(1-\beta)+v(1+\beta)}.}
\]

For an average of \(m\) independent Bernoulli curvature samples of success probability \(p\in(0,1)\), the globally best factor is \((1-p)/(1-p+mp)\). Thus increasing minibatch size helps, but cannot make constant nonnegative heavy-ball momentum outperform the optimally tuned no-momentum scheme in this isotropic scalar model.

## Assumptions and scope
Let \((H_k)_{k\ge0}\) be independent identically distributed nonnegative real random variables with \(\mu=\mathbb E H_k\in(0,\infty)\), variance \(v=\mathbb E(H_k-\mu)^2\in(0,\infty)\), and finite second moment. The objective is the strictly convex population quadratic \(F(x)=\mu x^2/2\), and every sample loss has minimizer zero. Fix \(\eta>0\) and \(0\le\beta<1\), independent of \(k\). Given any deterministic finite state \((x_0,x_{-1})\), iterate

\[
 x_{k+1}=x_k-\eta H_kx_k+\beta(x_k-x_{k-1}).
\]

Write \(\mathcal T(P)=\mathbb E[K(H)PK(H)^{\mathsf T}]\), with \(K(H)=\begin{psmallmatrix}1+\beta-\eta H&-\beta\\1&0\end{psmallmatrix}\). This positive linear operator acts on real symmetric \(2\times2\) matrices; its spectral radius \(R=\rho(\mathcal T)\) determines uniform asymptotic exponential mean-square stability. Precisely, \(R<1\) if and only if \(\mathbb E[x_k^2+x_{k-1}^2]\to0\) for every deterministic initial state, and \(R\) is the sharp exponential upper growth factor over all initial states. No statement is made about negative momentum, varying steps, normalized momentum conventions, Nesterov-type updates, additive noise, or multidimensional matrices with non-scalar random Hessians.

## Proof
**1. Exact covariance recurrence.** Set \(\alpha=\eta\mu\), \(t=v/\mu^2>0\), \(a=1+\beta-\alpha\), and \(\nu=t\alpha^2\). For \(u_k=\mathbb E[x_k^2]\), \(w_k=\mathbb E[x_kx_{k-1}]\), and \(z_k=\mathbb E[x_{k-1}^2]\), independence of the new curvature gives

\[
\begin{pmatrix}u_{k+1}\\w_{k+1}\\z_{k+1}\end{pmatrix}
=M\begin{pmatrix}u_k\\w_k\\z_k\end{pmatrix},\qquad
M=\begin{pmatrix}a^2+\nu&-2\beta a&\beta^2\\a&-\beta&0\\1&0&0\end{pmatrix}.
\]

Its characteristic polynomial is

\[
P(s)=(s+\beta)(s^2-\beta^2)-s(s-\beta)a^2-s(s+\beta)\nu.
\]

Although the coordinate matrix is not entrywise nonnegative, the corresponding covariance map preserves the positive-semidefinite cone; its spectral radius is the relevant uniform second-moment factor.

**2. Momentum has a strict spectral penalty.** Let \(r=t/(1+t)\in(0,1)\). For \(\beta=0\), the only nonzero eigenvalue is \(R=(1-\alpha)^2+t\alpha^2\), uniquely minimized at \(\alpha=1/(1+t)\), with value \(r\).

Now fix \(\beta>0\). The identities \(P(\beta)=-2\beta^2\nu<0\) and \(P(s)\to+\infty\) as \(s\to+\infty\) show that \(P\) has a real root larger than \(\beta\); hence \(R>\beta\). This already gives \(R>r\) if \(\beta\ge r\). If \(0<\beta<r\), put \(\theta=(r-\beta)/(r+\beta)>0\). Exact division gives

\[
\frac{P(r)}{r(r+\beta)}
=\frac{r^2-\beta^2}{r}-\theta(1+\beta-\alpha)^2-t\alpha^2.
\]

The right side is maximized over all real \(\alpha\) at \(\alpha_0=\theta(1+\beta)/(\theta+t)\). Substitution, using \(t=r/(1-r)\), yields the **strictly negative** upper bound

\[
\frac{P(r)}{r(r+\beta)}
\le -\frac{\beta^2(r-\beta)(1-r)^2}{r(r-\beta+2r\beta)}<0.
\]

Since \(P(s)\to+\infty\) as \(s\to+\infty\), there is a real eigenvalue larger than \(r\). Thus \(R(\eta,\beta)>r\) for every \(\eta>0\) and \(\beta>0\), proving the claimed unique optimizer.

**3. Exact stability region.** The deterministic mean transition matrix \(K_0=K(\mu)\) is Schur stable exactly when \(0<\alpha<2(1+\beta)\). Outside this region the mean state cannot converge for all initializations, so neither can its second moment. Inside, let \(E=e_1e_1^{\mathsf T}\). The second-moment map is a positive rank-one perturbation of the deterministic covariance map:

\[
\mathcal T(P)=K_0PK_0^{\mathsf T}+\nu P_{11}E.
\]

Solving the discrete Lyapunov equation \(S=K_0SK_0^{\mathsf T}+E\) gives

\[
S_{11}=\sum_{j=0}^{\infty}(e_1^{\mathsf T}K_0^je_1)^2
=\frac{1+\beta}{(1-\beta)((1+\beta)^2-a^2)}.
\]

The positive rank-one resolvent identity implies \(\rho(\mathcal T)<1\) exactly when \(\nu S_{11}<1\): the positive geometric resolvent exists under that inequality and diverges when it fails. Because \((1+\beta)^2-a^2=\alpha(2(1+\beta)-\alpha)\), this is equivalent to

\[
0<\alpha<\frac{2(1-\beta^2)}{(1-\beta)+t(1+\beta)}.
\]

Rewriting in \(\eta,\mu,v\) proves the displayed stability bound. At equality the characteristic polynomial satisfies \(P(1)=0\), so the boundary is not asymptotically mean-square stable.

**4. Exact minibatch specialization.** For \(H_k=m^{-1}\sum_{j=1}^m\xi_{k,j}\), with independent \(\xi_{k,j}\sim\mathrm{Bernoulli}(p)\), one has \(\mu=p\), \(v=p(1-p)/m\). Direct substitution gives

\[
 r_* =\frac{1-p}{1-p+mp},\qquad
 \eta_* =\frac{m}{1-p+mp},\qquad
\eta_{\max}(\beta)=\frac{2m(1-\beta^2)}{mp(1-\beta)+(1-p)(1+\beta)}.
\]

For the normalized high-momentum choice \(\eta p=c(1+\beta)\) with fixed \(0<c<2\), this model is mean-square stable exactly if

\[
 m>\frac{c(1-p)(1+\beta)}{p(2-c)(1-\beta)}.
\]

Consequently, in this normalization, a momentum weight tending to one requires minibatch size of order at least \((1-\beta)^{-1}\) to maintain mean-square stability.

## Verification
The standalone `verify.py` uses exact rational arithmetic only. It matched the covariance recurrence to fully enumerated Bernoulli minibatch trajectories in 1,152 cases, checked 120 strict characteristic-polynomial inequalities, 48 stability-boundary and side-sign identities, and three zero-momentum optimizer identities. These tests check finite computations, not all real parameters: the preceding symbolic inequalities and Lyapunov argument supply the infinite-parameter proof. Running `python3 verify.py` prints these counts and `PASS`.

## Relationship to prior work
Garg and Dereziński (2026) prove minibatch momentum-acceleration upper bounds for interpolation quadratics with nontrivial spectral geometry. Their result is not a claim of strict acceleration on every individual scalar instance; the present exact lower bound isolates the curvature-noise-only case where extra momentum cannot help. Kidambi, Netrapalli, Jain and Kakade (2018) give an explicit two-dimensional stochastic least-squares example obstructing accelerated heavy-ball rates, not the distribution-universal scalar optimum and sharp minibatch frontier here. Paquette and Paquette (2021) analyze large-dimensional random least squares under a high-dimensional limit, rather than this exact finite-dimensional all-batch optimizer. Kamo and Iiduka (2025) study nonconvex momentum with fixed versus growing minibatch sizes and gradient-norm guarantees, not an optimized scalar interpolation moment spectrum. Loizou and Richtárik (2017), Remark 4, observe that their *sufficient convergence bound* for stochastic heavy-ball becomes worse as momentum increases. That bound is not the actual sharp mean-square factor and does not establish the global all-scalar-distribution optimizer or minibatch frontier proved here. The first two moments \(\mu,v\) determine the complete result, regardless of the finer curvature distribution.

## Limitations
The theorem is about **uniform mean-square** convergence, not pathwise almost-sure rates or every fixed initialization's rate. The noise is purely multiplicative, nonnegative, and i.i.d. The momentum coefficient is constant and nonnegative; changing momentum, step schedule, signed momentum, and Nesterov lookahead are outside scope. Earlier stochastic-recursion and Lyapunov literature could contain equivalent scalar expressions, so mathematical priority needs independent review. Finite numerical checks do not establish the theorem; the analytic proof does. The claim neither contradicts acceleration results for heterogeneous multidimensional spectra nor rules out practical benefits of momentum under other metrics.

## References
Garg, S. and Dereziński, M. (2026), *Perfect Parallelization in Mini-Batch SGD with Classical Momentum Acceleration*, arXiv:2605.18609, first posted 2026-05-18, https://arxiv.org/abs/2605.18609.

Kidambi, R., Netrapalli, P., Jain, P., and Kakade, S. (2018), *On the Insufficiency of Existing Momentum Schemes for Stochastic Optimization*, arXiv:1803.05591, https://arxiv.org/abs/1803.05591.

Paquette, C. and Paquette, E. (2021), *Dynamics of Stochastic Momentum Methods on Large-scale, Quadratic Models*, arXiv:2106.03696, https://arxiv.org/abs/2106.03696.

Kamo, K. and Iiduka, H. (2025), *Increasing Batch Size Improves Convergence of Stochastic Gradient Descent with Momentum*, arXiv:2501.08883, https://arxiv.org/abs/2501.08883.

Loizou, N. and Richtárik, P. (2017), *Linearly Convergent Stochastic Heavy Ball Method for Minimizing Generalization Error*, arXiv:1710.10737, https://arxiv.org/abs/1710.10737.
