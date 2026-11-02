# Sharp Euler stability and nonuniform covariance bias for reversible Stratonovich Gaussian sampling

## Finding

For the two-dimensional reversible Stratonovich-perturbed Langevin diffusion of Louis--Pavliotis--Vilmart, let \(0<\lambda\leq1\), \(\delta>0\), \(c=\lambda\delta^2\), \(m=1+c\), and \(n=\lambda+c\). Its Itô Euler--Maruyama chain with independent Brownian increments has a unique invariant law with finite second moment **if and only if**
\[
0<h<h_*(\lambda,c):=\frac{1+\lambda+2c-\sqrt{(1-\lambda)^2+4c^2}}{(1+c)(\lambda+c)}.
\]
At equality the second moments from zero initial data diverge linearly; above it they diverge exponentially. This is a necessary and sufficient **mean-square** stability threshold, not merely a deterministic-drift bound.

For every stable \(h\), the stationary covariance is diagonal. In normalized coordinates \(Y=(X_1,\sqrt\lambda X_2)\), put
\[
\mathscr D=mn(2-mh)(2-nh)-4c^2>0.
\]
Its two exact stationary variances are
\[
U_h=\frac{2n(2-nh)+4c\lambda}{\mathscr D},\qquad
V_h=\frac{4c+2\lambda m(2-mh)}{\mathscr D},\qquad U_h>1,\ V_h>1.
\]
Thus both variances strictly exceed the corresponding Gaussian-target variances, although the invariant *distribution* of this multiplicative-noise chain is not asserted to be Gaussian.

The spectral-gap-optimized perturbation \(\delta=\lambda^{-1/2}\) has a nonzero limiting Euler stability ceiling
\[
\lim_{\lambda\downarrow0}h_*(\lambda,1)=\frac{3-\sqrt5}{2}.
\]
For any fixed \(0<h<(3-\sqrt5)/2\), its normalized stationary variances converge to
\[
\lim_{\lambda\downarrow0}U_h=\frac{2-h}{2(1-3h+h^2)},\qquad
\lim_{\lambda\downarrow0}V_h=\frac{1}{1-3h+h^2}.
\]
More generally, if \(\delta=\lambda^{-\alpha}\), \(\alpha\geq0\), then
\[
h_*(\lambda,\lambda^{1-2\alpha})\longrightarrow
\begin{cases}
2,&0\leq\alpha<1/2,\\
(3-\sqrt5)/2,&\alpha=1/2,
\end{cases}
\qquad
h_*(\lambda,\lambda^{1-2\alpha})\sim\lambda^{4\alpha-2}\quad(\alpha>1/2).
\]
In the supercritical case \(\alpha>1/2\), choosing any fixed \(0<t<1\) and \(h=t\lambda^{4\alpha-2}=t/c^2\) yields an asymptotically stable chain with \(h\to0\), yet \(U_h,V_h\to(1-t)^{-1}>1\). Hence a vanishing timestep proportional to the sharp stability scale does **not** ensure vanishing normalized covariance bias.

## Assumptions and scope

Set \(S=\operatorname{diag}(1,\lambda)\), \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), and take \(0<\lambda\leq1\), \(\delta>0\). The Itô equation under study is
\[
dX_t=-B X_t\,dt+\sqrt2\,\delta JS X_t\,d\beta_t+\sqrt2\,dW_t,
\qquad B=\operatorname{diag}(1+\lambda\delta^2,\lambda(1+\delta^2)),
\]
where the scalar Brownian motion \(\beta\) and two-dimensional standard Brownian motion \(W\) are independent. This is the Itô representation of the reversible Stratonovich diffusion and targets the centered Gaussian measure with covariance \(S^{-1}\). The Euler scheme uses independent standard normals for **each** Brownian increment, and constant \(h>0\):
\[
X_{k+1}=(I-hB)X_k+\sqrt{2h}\,\delta JS X_k\,\xi_k+\sqrt{2h}\,\zeta_k.
\]
All convergence assertions about stationary laws require finite second moments; the unstable claims concern the second moments started at \(X_0=0\). The multiplicative noise is discretized in the Itô Euler convention, not a Stratonovich midpoint or splitting scheme.

## Proof

**1. Closed second-moment operator.** Define the normalized vector \(Y_k=(X_{k,1},\sqrt\lambda X_{k,2})^\mathsf T\). Because \(\sqrt\lambda\,\delta JS\) transforms into \(\sqrt c\,J\) under this normalization, the update becomes
\[
Y_{k+1}=\operatorname{diag}(1-mh,1-nh)Y_k+\sqrt{2ch}\,JY_k\,\xi_k+\sqrt{2h}\,\operatorname{diag}(1,\sqrt\lambda)\zeta_k.
\]
The diagonal second moments \(z_k=(\mathbb E Y_{k,1}^2,\mathbb E Y_{k,2}^2)^\mathsf T\) therefore satisfy
\[
z_{k+1}=Tz_k+2h(1,\lambda)^\mathsf T,
\qquad T=\begin{pmatrix}(1-mh)^2&2ch\\2ch&(1-nh)^2\end{pmatrix}.
\]
The off-diagonal covariance/moment is multiplied by \(\tau=(1-mh)(1-nh)-2ch\), with no forcing. Writing \(a=1-mh\), \(b=1-nh\), the Perron eigenvalue of the nonnegative symmetric matrix \(T\) satisfies
\[
\rho(T)\geq\frac{a^2+b^2}{2}+2ch\geq|ab|+2ch\geq|\tau|.
\]
The full symmetric-matrix second-moment propagator is consequently stable exactly when \(\rho(T)<1\).

**2. The sharp threshold and its boundary.** Since \(0<n\le m\), for \(0<h<2/m\) both diagonal entries of \(I-T\) are positive; positive definiteness of \(I-T\) is then equivalent to its determinant being positive. Direct expansion gives
\[
\det(I-T)=h^2\bigl(mn(2-mh)(2-nh)-4c^2\bigr)=h^2\mathscr D.
\]
The function \(\mathscr D\) strictly decreases on \((0,2/m)\), from \(4[\lambda+c(1+\lambda)]>0\) to \(-4c^2<0\); hence it has exactly one root there. Solving the quadratic produces the stated \(h_*\). For \(h\ge2/m\), the first diagonal entry of \(T\) is at least one, so \(\rho(T)\ge1\). This proves the global if-and-only-if threshold. Since \(c,h>0\), \(T\) has a strictly positive Perron left eigenvector \(p\). For the zero-start recursion, the scalar \(p^\mathsf Tz_k\) is \(p^\mathsf T2h(1,\lambda)^\mathsf T\) times \(k\) if \(\rho(T)=1\), or times \((\rho(T)^k-1)/(\rho(T)-1)\) if \(\rho(T)>1\). Thus the asserted divergence is exact. Conversely, \(\rho(T)<1\) yields a strict mean-square contraction after finitely many synchronized random updates, so the affine random recursion has a unique invariant probability law in the quadratic Wasserstein space; its covariance is finite. Beyond the threshold no finite-second-moment stationary law can exist, since multiplication of its forced second-moment equation by \(p^\mathsf T\) would give \((1-\rho(T))p^\mathsf Tz=p^\mathsf T2h(1,\lambda)^\mathsf T>0\), impossible for \(\rho(T)\ge1\).

**3. Covariance formula and strict inflation.** For stable \(h\), solve \((I-T)z=2h(1,\lambda)^\mathsf T\) by the explicit two-by-two inverse to obtain \(U_h,V_h\) above. The off-diagonal invariant moment is zero because \(|\tau|<1\). The Gaussian target covariance corresponds to \(z=(1,1)^\mathsf T\). A one-step evaluation at that target gives
\[
T(1,1)^\mathsf T+2h(1,\lambda)^\mathsf T
=(1,1)^\mathsf T+h^2(m^2,n^2)^\mathsf T.
\]
Therefore
\[
\binom{U_h-1}{V_h-1}=(I-T)^{-1}h^2\binom{m^2}{n^2}>0,
\]
entrywise, because \((I-T)^{-1}=\sum_{j\ge0}T^j\) has strictly positive entries.

**4. Critical scaling and noncommuting limits.** Put \(R=\sqrt{(1-\lambda)^2+4c^2}\). The continuous-time covariance decay gap computed in Louis--Pavliotis--Vilmart is \(g=1+\lambda+2c-R\), and the exact identity
\[
\boxed{h_*(\lambda,c)=\frac{g}{(1+c)(\lambda+c)}}
\]
relates it to the discretization ceiling. At \(c=1\), substitute directly into the formulae and let \(\lambda\downarrow0\), giving the golden-ratio threshold and the two displayed limiting variances. For \(c=\lambda^{1-2\alpha}\), the regimes \(c\to0\), \(c=1\), and \(c\to\infty\) prove the three thresholds: when \(c\to0\), \(\lambda\le c\) and \(g\sim2(\lambda+c)\); when \(c\to\infty\), \(g\to1\) and \((1+c)(\lambda+c)\sim c^2\). Finally for \(\alpha>1/2\) and \(h=t/c^2\), \(0<t<1\), the denominator \(\mathscr D\sim4c(1-t)\) and each variance numerator is asymptotic to \(4c\), proving the asserted persistent bias even though the timestep vanishes. This is a joint limit and is not a fixed-parameter convergence-order claim.

## Verification

The accompanying `verify.py` independently constructs the full three-component symmetric second-moment propagator rather than assuming that the cross moment is irrelevant. It checks the factorization of \(\det(I-T)\), the exact root \(h_*\), the two stationary variances, the critical \(c=1\) limits, and \(1{,}500\) independently sampled full-covariance stability comparisons. It also checks four rational-parameter stationary systems with exact arithmetic. Python 3, NumPy and SymPy are required. Run `python verify.py` from the extracted file directory. All infinite-index and limiting conclusions follow from the proof above, not from the finite checks.

## Relationship to prior work

The original reversible Stratonovich perturbation was introduced by Abdulle, Pavliotis and Vilmart in 2019. Louis, Pavliotis and Vilmart (October 2, 2026), Sections 3.1, 4.2 and 6.1, analyzed the two-dimensional Gaussian continuous-time spectral gap and simulated its Itô Euler--Maruyama discretization at a small fixed timestep. Their continuous-time calculation supplies the formula for \(g\), but their inspected sections do not give the sharp discrete-time finite-second-moment existence boundary, the invariant covariance expressions, or the supercritical joint limit. General linear-SDE mean-square stability methods provide a framework for the matrix test; they do not by themselves specify the sampler-specific frontier or the \(\lambda\)-dependent bias law. The new contribution here is the exact coupled step-size/covariance phase diagram for the stated Euler discretization, rather than the Stratonovich method or generic mean-square spectral-radius theory.

## Limitations

Only the specified two-dimensional Gaussian target, one scalar multiplicative Brownian channel, standard independent additive noise, and constant-step Itô Euler--Maruyama discretization are covered. The stationary **second moments** are classified; the full stationary probability law and mixing time of the discrete chain are not explicitly determined. This says nothing about Stratonovich integrators, higher-dimensional matching constructions, nonlinear targets, Metropolized samplers, or bias of arbitrary observables. Numerical tests are supplementary, not a proof of the infinite-iteration statements. The priority search did not rule out a previously published specialized equivalent of this two-by-two stochastic recurrence.

## References

- G. Louis, G. A. Pavliotis, and G. Vilmart, *Reversible Stratonovich perturbations for accelerating convergence to equilibrium of Langevin dynamics*, arXiv:2610.03191v1, first publicly posted October 2, 2026, especially Sections 3.1, 4.2 and 6.1. https://arxiv.org/html/2610.03191v1
- A. Abdulle, G. A. Pavliotis, and G. Vilmart, *Accelerated convergence to equilibrium and reduced asymptotic variance for Langevin dynamics using Stratonovich perturbations*, arXiv:1903.03024, first posted March 7, 2019. https://arxiv.org/abs/1903.03024
- E. Buckwar and T. Sickenberger, *A comparative linear mean-square stability analysis of Maruyama- and Milstein-type methods*, arXiv:0912.1968 (general stability context; abstract consulted). https://arxiv.org/abs/0912.1968
