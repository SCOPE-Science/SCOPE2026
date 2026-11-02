# Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets

## Finding
Consider a stable multivariate Ornstein–Uhlenbeck diffusion with an independent Poisson clock that replaces the entire state by a fresh draw from a fixed probability law. This result gives **necessary and sufficient conditions** for a prescribed nondegenerate Gaussian law to be stationary, including a sharp reset-rate threshold, singular covariance boundaries, and a unique explicit source law. In particular, a genuinely non-Gaussian source can yield an exactly Gaussian stationary marginal.

Let \(G=N(m,S)\), where \(m\in\mathbb R^d\) and \(S\) is symmetric positive definite. Define
\[
Q=\frac{AS+SA^{\mathsf T}}2-D,\qquad h=Am,\qquad \tau=\operatorname{tr}(S^{-1}Q).
\]
For any fixed reset rate \(r>0\), **a resetting probability law yielding stationary law \(G\) exists if and only if**
\[
Q\succeq0,\quad h\in\operatorname{Ran}Q,\quad
r\ge r_{\min}:=\tau+\frac14 h^{\mathsf T}Q^+h.
\]
Here \(Q^+\) is the Moore–Penrose pseudoinverse. Whenever feasible, the resetting law is **unique** and has density
\[
\boxed{\quad\rho(x)=\varphi_{m,S}(x)\left[1+\frac{y^{\mathsf T}Qy+h^{\mathsf T}y-\tau}{r}\right],\qquad y=S^{-1}(x-m).\quad}
\]
The lower bound on \(r\) is attained, not merely approached, whenever \(Q\ne0\) and the displayed conditions hold. At equality the source density vanishes on the minimizing affine subspace; below it the forced source would be negative on an open set. If \(Q=0\), feasibility forces \(m=0\), and the only source is the ordinary equilibrium Gaussian.

**Sharp isotropic displacement transition.** If \(A=kI_d\), \(D=D_0I_d\), \(S=sI_d\), with \(k,D_0,s>0\), put \(\beta=\sqrt{k}\,\lVert m\rVert/(2\sqrt{dD_0})\). With \(s\) allowed to vary, a Gaussian stationary state with prescribed mean \(m\) exists precisely under the following reset-rate conditions:
\[
\begin{array}{ll}
0<r<dk:&\displaystyle \lVert m\rVert\le2\sqrt{\frac{dD_0}{k}}\left(1-\sqrt{1-\frac{r}{dk}}\right),\\[6pt]
r=dk:&\displaystyle \lVert m\rVert<2\sqrt{\frac{dD_0}{k}},\\[6pt]
r>dk:&\displaystyle m\in\mathbb R^d\text{ arbitrary}.
\end{array}
\]
Thus **the attainable mean range changes discontinuously from bounded to unbounded as the reset rate passes \(dk\)**, when output variance is unrestricted. This is a feasibility boundary, not a discontinuity of the invariant law at fixed source parameters.

## Assumptions and scope
Fix an integer \(d\ge1\); a real \(d\times d\) matrix \(A\) with all eigenvalues in the open right half-plane; and a real symmetric positive-definite diffusion matrix \(D\). Between reset times,
\[
dX_t=-AX_t\,dt+\sqrt{2D}\,dW_t.
\]
At rate \(r>0\), independently of the Brownian noise and state, replace \(X_t\) by an independent draw from a time-independent Borel probability measure \(\mu\). The entire vector resets together. All assertions concern the unique stationary one-time probability law, not the finite-time distribution or the assertion that the path process is Gaussian. The target covariance \(S\) is strictly positive definite; degenerate Gaussian targets are excluded. The mean \(m\) and \(S\) are in physical state coordinates, and \(D\) is the diffusion coefficient in generator \(\operatorname{tr}(D\nabla^2)\), not the noise-amplitude covariance itself.

## Proof
**1. The inverse source equation.** The ordinary diffusion generator and its forward adjoint are
\[
Lf(x)=-(Ax)\cdot\nabla f(x)+\operatorname{tr}(D\nabla^2 f(x)),\qquad
L^*p=\nabla\cdot(Axp)+\operatorname{tr}(D\nabla^2p).
\]
For a stationary probability density \(p\) with independent resets to \(\mu\), the distributional forward equation is \(0=L^*p-rp+r\mu\). Consequently, if the stationary target is a Gaussian \(p=\varphi_{m,S}\), the source is forced uniquely as a distribution:
\[
\mu=p-r^{-1}L^*p.
\]
In particular, no singular resetting measure can generate this target unless it equals the displayed absolutely continuous measure.

**2. Compute the density exactly.** Writing \(z=x-m\), \(y=S^{-1}z\), direct Gaussian differentiation gives \(\nabla p=-yp\) and \(\nabla^2p=(yy^{\mathsf T}-S^{-1})p\). Hence
\[
\frac{L^*p}{p}
=\operatorname{tr}(A)-\operatorname{tr}(DS^{-1})-y^{\mathsf T}Qy-h^{\mathsf T}y
=\tau-y^{\mathsf T}Qy-h^{\mathsf T}y.
\]
Here the first equality uses the symmetrized drift covariance \((AS+SA^{\mathsf T})/2\); the second uses \(\operatorname{tr}(A)-\operatorname{tr}(DS^{-1})=\operatorname{tr}(S^{-1}Q)\). Inserting this into the inverse source equation gives exactly the asserted \(\rho\). Since \(y\) under \(p\) is Gaussian with covariance \(S^{-1}\), \(\mathbb E_p[y^{\mathsf T}Qy]=\tau\) and \(\mathbb E_p[h^{\mathsf T}y]=0\). Thus \(\int\rho=1\) independently of the sign constraint.

**3. Complete classification of nonnegativity.** The sign is controlled by \(F(y)=r-\tau+y^{\mathsf T}Qy+h^{\mathsf T}y\). If \(Q\) has a negative direction, \(F\) tends to \(-\infty\) along that direction. If \(Q\succeq0\) but \(h\notin\operatorname{Ran}Q\), then a null direction of \(Q\) has nonzero linear slope, so \(F\) is negative somewhere. Conversely, when \(Q\succeq0\) and \(h\in\operatorname{Ran}Q\), let \(w=Q^+h/2\). The precise completion of squares is
\[
F(y)=r-\tau-\frac14h^{\mathsf T}Q^+h+(y+w)^{\mathsf T}Q(y+w).
\]
It is nonnegative for every \(y\) precisely when \(r\ge\tau+h^{\mathsf T}Q^+h/4\). Continuity and strict positivity of the target density turn any negative point into a negative-measure open set, so these are also the necessary conditions for \(\mu\) to be a probability law.

**4. Stationary existence and uniqueness.** For every probability source \(\mu\), the stochastic process has a stationary law given by the last-reset resolvent \(\pi=r\int_0^\infty e^{-rt}\mu P_t\,dt\), where \(P_t\) is the unreset OU transition semigroup. The candidate \(\rho\) is a probability density by Step 3 and solves the forward stationarity equation, hence coincides with \(\pi\). Uniqueness can also be seen by coupling two copies with identical first reset time, reset draw, and subsequent Brownian increments: their laws agree after the first reset, whose nonoccurrence probability is \(e^{-rt}\). The source uniqueness has already been proved distributionally in Step 1.

**5. Isotropic sharp range.** If \(A=kI_d\), \(D=D_0I_d\), \(S=sI_d\), then \(Q=(ks-D_0)I_d\). For \(m\ne0\), feasibility requires \(s>D_0/k\), and the exact minimum rate is
\[
r_{\min}(s,m)=d\left(k-\frac{D_0}{s}\right)+\frac{k^2\lVert m\rVert^2}{4(ks-D_0)}.
\]
Set \(q=ks/D_0>1\) and \(\beta^2=k\lVert m\rVert^2/(4dD_0)\). Then
\[
\frac{r_{\min}}{dk}=1-\frac1q+\frac{\beta^2}{q-1},\qquad
\frac1{dk}\frac{dr_{\min}}{dq}=\frac1{q^2}-\frac{\beta^2}{(q-1)^2}.
\]
For \(0<\beta<1\), the unique global minimum is attained at \(q=1/(1-\beta)\) and equals \(dk(2\beta-\beta^2)\). For \(\beta\ge1\), the function is strictly decreasing to \(dk\) as \(q\to\infty\), but no finite \(q\) attains the infimum. At \(m=0\), the equilibrium choice \(s=D_0/k\) is feasible for every \(r>0\). Solving these inequalities for \(\lVert m\rVert\) proves the three claimed sharp cases, including the strict boundary at \(r=dk\).

**6. Gaussian output does not imply Gaussian resets or Gaussian temporal statistics.** A polynomial of degree two times a nondegenerate Gaussian density can itself be Gaussian only when the polynomial is constant: comparing logarithms at infinity forces equality of quadratic and linear exponents. Thus for feasible \(Q\ne0\), \(\rho\) is genuinely non-Gaussian. For a stable \(A\), \(Q=0\) uniquely specifies the ordinary OU covariance, and feasibility then forces \(Am=0\), hence \(m=0\). Moreover, the stationary lag covariance is
\[
\operatorname{Cov}(X_{t+s},X_t)=e^{-(A+rI_d)s}S\qquad(s\ge0).
\]
This follows by conditioning on the first reset and using the linear conditional-mean equation, so the reset rate remains visible in temporal data despite an exactly Gaussian stationary marginal.

## Verification
The included standalone `verify_gaussian_reset.py` checks the source normalization and exact moment equations by tensor-product Gauss–Hermite quadrature for two distinct two-dimensional configurations, including a nonsymmetric stable drift and off-diagonal diffusion. It checks generator stationarity for every bivariate monomial of degree at most five, tests the sharp minimum of the quadratic source tilt, verifies the lag-covariance identity, treats an exactly rank-deficient boundary, and uses exact rational symbolic differentiation to verify the isotropic minimizer and threshold cases. The program completes 71 deterministic checks. These computations supplement, rather than replace, the all-dimension analytic proof above.

## Relationship to prior work
Olsen, *Steady-state moments under resetting to a distribution* (arXiv:2310.04840, 2023), establishes the renewal representation and arbitrary-order stationary moment recursion for the one-dimensional harmonic diffusion with distributed resets. Those are antecedents, not new claims here. The present theorem instead inverts the stationary forward equation and solves the **global positivity problem** for the unique source, in arbitrary dimension with general stable drift and noncommuting diffusion. It then derives the exact rate/mean reachability boundary and its dimension-dependent discontinuity.

Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting* (arXiv:2301.12304, 2023), analyze OU resetting (notably resetting to a fixed location) and comb-related transport. Their stationary Green-function and moment calculations do not supply a classification of arbitrary reset measures realizing a Gaussian target. The inverse-source equation itself is a direct standard Fokker–Planck identity; novelty is not claimed for that identity, the OU semigroup, Gaussian differentiation, or the matrix completion-of-squares technique separately.

The nearest relevant earlier local findings concern Gaussian covariance twins under equilibrium rethermalization and stationary fluctuations under resetting, not an inverse design classification for Gaussian stationary marginals. Broader inverse-generator design work may imply parts of the result, and priority is not conclusively established. The sharp all-dimensional positivity and reachable-mean criteria are the specific assessed claim.

## Limitations
The model requires independent Poisson refreshment to an external state law, a constant stable linear drift, additive nondegenerate Brownian forcing, and a nondegenerate Gaussian *one-time* target. It does not yield a finite-sample estimator, a stability bound for noisy observations, optimal physical reset-work costs, or analogous feasibility conditions for state-dependent or finite-duration resetting. Stationary marginal Gaussianity does not assert pathwise Gaussianity. Literature coverage is not an independent priority certification.

## References
1. K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (initial public preprint October 7, 2023), Phys. Rev. E **108**, 044120 (2023), https://arxiv.org/abs/2310.04840, https://doi.org/10.1103/PhysRevE.108.044120.
2. P. Trajanovski, P. Jolakoski, K. Zelenkovski, A. Iomin, L. Kocarev, and T. Sandev, *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304 (initial public preprint January 28, 2023), https://arxiv.org/abs/2301.12304.
3. Mathematical Subject Classification MSC2020, category 82C31, stochastic methods in time-dependent statistical mechanics, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C26.
