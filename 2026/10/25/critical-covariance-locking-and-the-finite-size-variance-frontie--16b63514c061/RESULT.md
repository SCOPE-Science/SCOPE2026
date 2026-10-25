# Critical covariance locking and the finite-size variance frontier in local-reset growth

## Finding

Fix an integer \(N\ge2\), a positive intrinsic growth rate \(m\), a resetting rate \(r>m\), a redistribution rate \(\varphi\ge0\), and a reset level \(x_0>0\). Let \(X(t)=(X_1(t),\ldots,X_N(t))\) be the nonnegative piecewise-deterministic Markov process defined as follows. Between jumps,
\[
\dot X_i=mX_i+\varphi(\overline X-X_i),\qquad
\overline X=N^{-1}\sum_{j=1}^{N}X_j.
\]
Independently for each \(i\), at the times of a rate-\(r\) Poisson clock, replace only \(X_i\) by \(x_0\). The process has a unique invariant probability measure \(\pi\) with a finite first moment, and
\[
\mathbb E_\pi X_i=M=\frac{r x_0}{r-m}.
\]

Define \(\delta=r-m\) and the sharp second-moment threshold
\[
m_*(N,\varphi)=\frac{3r+2\varphi-\sqrt{(r-2\varphi)^2+8r\varphi/N}}4.
\]
**Complete moment classification:** \(\int X_i^2\,d\pi<\infty\) for every \(i\) if and only if \(m<m_*(N,\varphi)\). At equality and above the invariant second moments are infinite. This includes \(\varphi=0\), where the threshold is \(m<r/2\).

In the finite-second-moment regime set
\[
D=\delta(r-2m)+\varphi(2\delta-r/N),\qquad
Q=\frac{r x_0^2m^2}{\delta^2}.
\]
Then \(D>0\), and for distinct \(i,j\) the exact variance \(V\), covariance \(C\), and correlation are
\[
V=\operatorname{Var}_\pi(X_i)=Q\frac{\delta+\varphi/N}{D},\qquad
C=\operatorname{Cov}_\pi(X_i,X_j)=Q\frac{\varphi/N}{D},
\]
\[
\operatorname{Corr}_\pi(X_i,X_j)=\frac{\varphi}{N(r-m)+\varphi}.
\]
For fixed \(N,r,m,x_0\), increasing \(\varphi\) strictly decreases \(V\) wherever finite (when \(m>0\)); for \(\varphi>0\) it strictly increases the correlation. The *unstandardized* intersite covariance obeys the sharp three-way law
\[
\operatorname{sgn}\frac{dC}{d\varphi}=\operatorname{sgn}(r-2m).
\]
At the critical growth \(m=r/2\), **the entire stationary intersite covariance is locked independently of \(r\) and of positive redistribution**:
\[
\boxed{\operatorname{Cov}_\pi(X_i,X_j)=\frac{x_0^2}{N-1}\quad(\varphi>0,\ i\ne j)}.
\]
Meanwhile \(V=x_0^2(1+Nr/(2\varphi))/(N-1)\) decreases with redistribution and diverges as \(\varphi\downarrow0\).

The boundary is genuinely finite-size: for fixed \(N\), \(m_*(N,\varphi)\) increases strictly from \(r/2\) at zero redistribution to \(r(1-1/(2N))\) at infinite redistribution. In particular, \(r/2<m<r(1-1/(2N))\) has finite stationary variance exactly when
\[
\varphi>\frac{N(r-m)(2m-r)}{2N(r-m)-r}.
\]
Growth \(m\ge r(1-1/(2N))\) cannot be made second-moment stable by any finite redistribution. In the large-system critical window \(\varphi=r/2+\eta r/\sqrt N\) with fixed real \(\eta\),
\[
m_*(N,\varphi)
=r+\frac{r}{2\sqrt N}\left(\eta-\sqrt{\eta^2+1}\right)+O(N^{-1}).
\]
This square-root window joins the large-\(N\) thresholds \(\min\{r,r/2+\varphi\}\).

## Assumptions and scope

All clocks are independent homogeneous Poisson processes; no Brownian growth noise is present; growth rates and reset levels are identical across sites. Redistribution uses the simultaneous empirical mean, not its deterministic expectation. Parameters satisfy \(N\in\{2,3,\ldots\}\), \(x_0>0\), \(0<m<r\), and \(\varphi\ge0\). The invariant law is taken on \([0,\infty)^N\). No claims are made for negative redistribution, heterogeneous sites, correlated resets, or infinite second moments as an asymptotic tail equivalent.

## Proof

**Existence, uniqueness, and the mean.** Couple two copies with identical site-reset clocks. Their difference follows a deterministic positive linear flow between jumps, with drift matrix \(mI-\varphi(I-J/N)\), and at a jump its resetting coordinate becomes zero. Because this Metzler matrix has every column sum equal to \(m\), the expected \(\ell^1\) difference contracts at rate at least \(r-m\):
\[
\mathbb E\|X^x(t)-X^y(t)\|_1
\le e^{-(r-m)t}\|x-y\|_1.
\]
Consequently the Markov semigroup is a strict contraction in the first-Wasserstein metric at every fixed positive time. The Banach fixed-point theorem and the semigroup property give a unique invariant measure with finite first moment. Permutation symmetry makes it exchangeable. The generator applied to one coordinate yields \(0=(m-r)M+rx_0\), proving the displayed mean.

**Second-moment dynamics.** Put \(s(t)=\mathbb E[X_1(t)^2]\) and \(u(t)=\mathbb E[X_1(t)X_2(t)]\) for an exchangeable finite-moment start, and \(h(t)=\mathbb E X_1(t)\). The exact generator computation (with resets of only one coordinate at a time) gives
\[
\binom{s'}{u'}=K\binom{s}{u}
+\binom{r x_0^2}{2rx_0h(t)},
\]
where
\[
K=\begin{pmatrix}
2m-r-2\varphi(N-1)/N&2\varphi(N-1)/N\\
2\varphi/N&2m-2r-2\varphi/N
\end{pmatrix}.
\]
The first moment satisfies \(h'=(m-r)h+rx_0\), so it is bounded whenever its initial value is finite. For positive \(\varphi\), \(K\) is irreducible Metzler, with Perron (spectral-abscissa) eigenvalue
\[
\lambda_+=2m-3r/2-\varphi+
\frac12\sqrt{(r-2\varphi)^2+8r\varphi/N}.
\]
Thus \(\lambda_+<0\) exactly when \(m<m_*(N,\varphi)\).

If \(\lambda_+<0\), choose the deterministic initial vector \((x_0,\ldots,x_0)\). The forcing in the moment system is bounded and the matrix exponential is exponentially decaying; hence \(s(t),u(t)\) are uniformly bounded. Convergence in first-Wasserstein to \(\pi\), followed by lower semicontinuity of \(x_i^2\), shows that \(\pi\) has finite second moments. Conversely, if \(\pi\) has a finite second moment, its stationary raw moments satisfy \(K(s,u)^\top+(r x_0^2,2r x_0M)^\top=0\), justified by the integrable quadratic generator. A positive left Perron eigenvector gives
\[
0=\lambda_+\,w^\top(s,u)^\top+w^\top(r x_0^2,2r x_0M)^\top.
\]
The second term is strictly positive; therefore \(\lambda_+\) must be negative. At \(\varphi=0\), each coordinate is an independent growth-and-reset process, whose stationary second moment is finite exactly when \(2m<r\); this is also immediate from its scalar moment equation. This establishes necessity and sufficiency including the boundary.

**Explicit covariance and the locking threshold.** In the finite-moment regime define \(Z_i=X_i-M\). Stationarity and the same generator give, for \(V=\mathbb E Z_i^2\) and \(C=\mathbb E Z_iZ_j\),
\[
0=(2m-r-2\varphi(N-1)/N)V+2\varphi(N-1)C/N+Q,
\]
\[
0=2\varphi V/N+(2m-2r-2\varphi/N)C.
\]
Solving this two-by-two system yields the displayed \(V,C\). Direct algebra gives \(\det K=2D\). Differentiating the exact expressions (holding other parameters fixed) yields
\[
\frac{dV}{d\varphi}=-\frac{2r x_0^2m^2(N-1)}{ND^2}<0,
\qquad
\frac{dC}{d\varphi}=\frac{Q\delta(r-2m)}{ND^2}.
\]
At \(m=r/2\), cancellation in \(D\) gives \(D=r\varphi(N-1)/N\) and \(Q=rx_0^2\), so \(C=x_0^2/(N-1)\) identically, while \(V\) retains its \(\varphi\)-dependence. All equalities concern stationary moments and are not merely limits of finite-time approximations.

**Parameter frontiers.** Solving \(\lambda_+=0\) gives \(m_*\). Its strict increase with \(\varphi\) follows either by differentiating the explicit square root or from the positive identity
\[
(r-2\varphi)^2+8r\varphi/N
-(2\varphi-r+2r/N)^2=4r^2(N-1)/N^2>0.
\]
The limiting threshold, the exact lower boundary in \(\varphi\), and the \(N^{-1/2}\) crossover follow by rearrangement and Taylor expansion of the same radical; the remainder is uniform for \(\eta\) in any fixed compact set.

## Verification

The independent standard-library program `VERIFY.py` checks exact rational stationary raw-moment and centered-covariance equations across a parameter grid, matrix determinants, finite-\(N\) boundaries, critical locking, and the independence limit; it also checks representative numerical eigenvalue boundaries. Its recorded execution reports 57,501 successful assertions. These computational tests cannot certify an infinite-time moment theorem; the contraction, Perron-eigenvector argument, and Lyapunov/moment boundedness reasoning above establish that result.

## Relationship to prior work

Bernard, Del Vecchio Del Vecchio, Bouchaud, and Le Doussal (2026, arXiv:2610.22038v1) introduce the same local-reset and mean-field growth mechanism with heterogeneous site parameters, focusing on localization, population fractions, and typical growth. The homogeneous finite-\(N\) covariance-locking law and sharp second-moment frontier are not stated there. Assefa, Keller-Ressel, and Palmowski (2026, arXiv:2610.01363v1) provide a general matrix-exponential calculus for moments of affine-reset polynomial processes; the moment-generator method is therefore established prior art, and no novelty is claimed for moment closure itself. Jolakoski and collaborators (2024, arXiv:2411.12390v1) examine a closely related reset/reallocation growth model with multiplicative Brownian noise, including paired moment equations and moment regimes. That overlap presents a substantive deducibility/priority risk. The specific contribution assessed here is the sharp finite-system if-and-only-if invariant-moment boundary, the redistribution-invariant cross-covariance at the critical growth ratio, and the accompanying finite-size critical window, rather than generic moment recursions.

## Limitations

The classification is for the homogeneous, positive-growth, positive-redistribution, independent local-reset model only. Finite first moments require the stated \(m<r\). Divergence of the second moment at and beyond the threshold is not a statement about almost-sure pathwise divergence. The large-\(N\) expansion treats only the stated critical scaling; it does not prove convergence of full stationary laws or fluctuations. The exact cross-covariance is not a full dependence characterization. Earlier general moment methods provide a route to parts of these formulas, so independent priority and mathematical review remain necessary.

## References

1. M. Bernard, G. Del Vecchio Del Vecchio, J.-P. Bouchaud and P. Le Doussal, *Partial Localization and Multifractality in Heterogeneous Population Growth with Resetting*, arXiv:2610.22038v1 (first public 2026-10-15), https://arxiv.org/html/2610.22038v1.
2. J. Assefa, M. Keller-Ressel and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363v1 (first public 2026-10-01), https://arxiv.org/html/2610.01363v1.
3. P. Jolakoski et al., *The impact of stochastic resetting on resource allocation: The case of Reallocating geometric Brownian motion*, arXiv:2411.12390v1 (first public 2024-11-19), https://arxiv.org/html/2411.12390v1.
