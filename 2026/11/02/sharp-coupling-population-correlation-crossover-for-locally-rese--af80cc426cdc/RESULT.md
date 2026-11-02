# Sharp coupling–population correlation crossover for locally reset harmonic Brownian gases

## Finding

For a locally reset, attractive Curie–Weiss harmonic Brownian gas, the exact finite-population stationary Pearson correlation is

\[
\rho_N=\frac{\lambda}{N(\nu+r)+\lambda}.
\]

It is universal over all independent, identically distributed reset-location laws with finite second moment, regardless of the thermal diffusivity and resetting-site variance. In a joint large-population/strong-coupling limit, normalized correlations have a sharp interaction scale \(\lambda\asymp N\). The full stationary time-covariance matrix has precisely two relaxation rates; at the critical scale the tagged-particle autocovariance exhibits an explicit \(N^{-1}\)-time boundary layer.

## Assumptions and scope

Fix an integer \(N\ge2\), constants \(\nu>0\), \(D>0\), \(r>0\), and \(\lambda\ge0\). Between reset events, the real-valued coordinates satisfy

\[
dX_i(t)=\left[-\nu X_i(t)-\lambda\left(X_i(t)-\overline X(t)\right)\right]dt+\sqrt{2D}\,dW_i(t),\qquad \overline X=\frac1N\sum_{j=1}^NX_j.
\]

The Brownian motions are independent. Independently for each particle, a rate-\(r\) Poisson clock replaces its coordinate instantaneously by a fresh random variable \(R\) drawn from a common law; all Brownian motions, reset clocks and reset locations are mutually independent. Write \(\mu_0=\mathbb ER\), \(\tau^2=\operatorname{Var}(R)<\infty\). Degenerate, discrete, continuous and mixed reset laws are allowed. There is no simultaneous common resetting. All formulas concern the unique stationary state; \(t\ge0\) is a nonnegative time lag.

Set

\[
\begin{aligned}
m&=\frac{r\mu_0}{\nu+r}, & b&=\nu+r,\\
Q&=2D+r\bigl[(\mu_0-m)^2+\tau^2\bigr], & A&=r+2\nu,\\
T_N&=ANb+\lambda\bigl[A+2(N-1)b\bigr].
\end{aligned}
\]

Here \(Q>0\) and \(T_N>0\). For distinct \(i,j\), let \(S_N=\operatorname{Var}(X_i)\), \(C_N=\operatorname{Cov}(X_i,X_j)\), and \(K_{ij}(t)=\operatorname{Cov}(X_i(t),X_j(0))\).

The complete finite-size formula is

\[
\boxed{S_N=\frac{Q(Nb+\lambda)}{T_N},\qquad C_N=\frac{Q\lambda}{T_N},\qquad \rho_N=\frac{C_N}{S_N}=\frac{\lambda}{Nb+\lambda}.}
\]

In particular \(C_N>0\) for \(\lambda>0\), while \(C_N=0\) for \(\lambda=0\). Define the slow and fast covariance eigenvalues \(u_N=S_N+(N-1)C_N\) and \(v_N=S_N-C_N\). Then

\[
\boxed{
\begin{aligned}
K_{ii}(t)&=\frac{u_N}{N}e^{-bt}+\left(1-\frac1N\right)v_Ne^{-(b+\lambda)t},\\
K_{ij}(t)&=\frac{u_N}{N}e^{-bt}-\frac{v_N}{N}e^{-(b+\lambda)t},\quad i\ne j.
\end{aligned}}
\]

These two formulas are exact even at \(\lambda=0\). For \(\lambda>0\), the distinct-particle lag covariance is strictly positive at every finite lag.

Let \(\lambda_N\ge0\) vary with \(N\), keeping \(\nu,D,r,\mu_0,\tau^2\) fixed. If \(\lambda_N/N\to c\in[0,\infty)\), then \(\rho_N\to c/(b+c)\); if \(\lambda_N/N\to\infty\), then \(\rho_N\to1\). Equivalently, \(\rho_N\to0\) exactly when \(\lambda_N=o(N)\). At the critical scale \(\lambda_N=cN\) for fixed \(c>0\),

\[
\boxed{\lim_{N\to\infty}N K_{ii}(s/N)=\frac{Q}{2b}+\frac{Q}{2c}e^{-cs},\quad s\ge0,}
\]

whereas at each fixed \(t>0\),

\[
\boxed{\lim_{N\to\infty}NK_{ii}(t)=\lim_{N\to\infty}NK_{ij}(t)=\frac{Q}{2b}e^{-bt},\quad i\ne j.}
\]

The limits describe normalized fluctuations, not an order-one unscaled covariance. They do not assert failure of weak propagation of chaos, since both individual variances and pair covariances vanish in the critical scaling.

## Proof

**Stationarity and mean.** Couple two copies of the process using the same Brownian paths, reset times and reset targets. Between resets their displacement difference evolves under the symmetric drift matrix \(-\nu I-\lambda(I-P)\), where \(P=\mathbf1\mathbf1^\top/N\). Its Euclidean norm contracts at least as \(e^{-\nu t}\). A shared single-coordinate reset can only reduce the norm of the difference. Standard second-moment Lyapunov bounds from \(\nu>0\) and \(\mathbb ER^2<\infty\) therefore give existence and uniqueness of a finite-second-moment stationary law. By exchangeability, each coordinate has the same stationary mean; taking expectations in its generator gives \(0=-(\nu+r)m+r\mu_0\).

**Closed second moments.** Put \(Y_i=X_i-m\), \(S=\mathbb EY_i^2\), \(C=\mathbb EY_iY_j\) for distinct \(i,j\). For the coordinate-square observable, Ito's formula and the replacement generator give

\[
0=-(2\nu+2\lambda+r)S+\frac{2\lambda}{N}\bigl[S+(N-1)C\bigr]+Q.
\]

For the distinct-coordinate product, the two independent reset clocks each remove one centered factor; the reset expectation vanishes because every other centered coordinate has mean zero. Thus

\[
0=-2(\nu+\lambda+r)C+\frac{2\lambda}{N}\bigl[S+(N-1)C\bigr].
\]

The latter identity yields \(C=\lambda S/(Nb+\lambda)\); substitution into the former yields the displayed \(S_N,C_N\). In particular this derivation uses only \(\mathbb ER\) and \(\operatorname{Var}R\); no Gaussian assumption on reset targets is made. Differentiating the exact functions at fixed \(N\) shows

\[
\frac{dS_N}{d\lambda}=-\frac{2QN(N-1)b^2}{T_N^2}<0,
\qquad
\frac{dC_N}{d\lambda}=\frac{QANb}{T_N^2}>0.
\]

So stronger attraction simultaneously reduces individual variance and increases interparticle covariance. As \(\lambda\to\infty\) at fixed \(N\), both tend to \(Q/[2N(\nu+r)-r]\).

**Time correlations.** For the centered coordinate vector \(Y\), the full generator acting on linear functions is the matrix \(-bI-\lambda(I-P)\); the constant force from confinement cancels the constant mean reset contribution because \(r(\mu_0-m)=\nu m\). Accordingly,

\[
\mathbb E[Y(t)\mid Y(0)]=\bigl[e^{-bt}P+e^{-(b+\lambda)t}(I-P)\bigr]Y(0).
\]

The stationary covariance matrix is \(u_NP+v_N(I-P)\). Matrix multiplication yields exactly the two displayed lag formulas. For \(\lambda>0\), \(u_N>v_N>0\), proving strict positivity of the cross covariance at each finite nonnegative lag.

**Sharp scale and boundary layer.** The Pearson formula yields the complete large-\(N\) classification without compactness assumptions on the sequence \(\lambda_N\). For \(\lambda_N=cN\), direct substitution shows \(u_N\to Q/(2b)\) and \(Nv_N\to Q/(2c)\). Insert these limits into the exact time-covariance formulas: at \(t=s/N\), the slow exponential approaches one while the fast exponential approaches \(e^{-cs}\); at any fixed positive \(t\), the fast exponential vanishes. All stated limits follow.

## Verification

The standalone standard-library program `verify_correlation.py` independently solves the stationary generator's **uncentered** coordinate, coordinate-square and cross-product equations using exact rational arithmetic. It compares the results against the closed centered formulas for 512 parameter tuples, checks 10 spectral-regression identities, and runs 9 critical-scale boundary-layer diagnostics: **531 checks in total**. Execute it with `python3 verify_correlation.py`. These finite checks are supplementary; the universal domain and asymptotic limits follow from the proof above.

For example, at \(N=2\), \(\nu=r=D=1\), \(\lambda=2\), and deterministic resets to \(R=2\), the formulas give \(m=1\), \(S_2=9/13\), \(C_2=3/13\), and \(\rho_2=1/3\). The exact stationary lag cross covariance is \(K_{12}(t)=(6e^{-2t}-3e^{-4t})/13\).

## Relationship to prior work

Bressloff's 2024 treatment introduces the underlying finite-particle local and global resetting dynamics, derives the Dean–Kawasaki and mean-field equations and computes the interaction-independent one-particle stationary mean for quadratic confinement [1]. Its distinct global-reset analysis explains correlations induced by a *shared* reset clock; the present result instead retains independent local reset clocks, works at finite particle number, determines the full two-time covariance and identifies the normalized-correlation boundary \(\lambda\asymp N\).

Nagar and Gupta [2] review interacting systems with global and local resetting, including exclusion and interacting-restart mechanisms. Olsen [3] derives single-particle harmonic resetting moments for arbitrary reset-location laws; those one-body moments do not determine the off-diagonal covariance of an interacting finite population. These comparisons do not establish priority over every general theorem about affine jump-diffusions; generic Lyapunov-equation and linear-response methods are a residual literature risk.

## Limitations

The law assumes attractive symmetric all-to-all coupling, homogeneous confinement and reset rates, independent reset clocks and targets, finite reset variance and strictly positive Brownian diffusivity and trap strength. It makes no assertion for common resetting, nonquadratic forces, heterogeneous populations, heavy-tailed reset targets with infinite second moment, or non-Poisson clocks. The stationary distribution need not be Gaussian. Persistent **normalized** correlations in the critical scaling do not mean unscaled correlations are nonvanishing or that the limiting coordinates fail to converge weakly to the deterministic mean.

## References

[1] P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501v1 (first public version 2024-01-07). https://arxiv.org/abs/2401.03501

[2] A. Nagar and S. Gupta, *Stochastic resetting in interacting particle systems: A review*, arXiv:2305.16955v2 (2023). https://arxiv.org/abs/2305.16955

[3] K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E **108**, 044120 (2023). https://doi.org/10.1103/PhysRevE.108.044120
