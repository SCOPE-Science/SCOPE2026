# A sharp dispersal window for reducing two-patch regional population fluctuations

## Finding

For two coupled, linearly regulated habitats with independent additive environmental noise, a finite positive dispersal rate uniquely minimizes the stationary variance of **total** regional fluctuations if and only if the ratio of local noise intensities lies strictly between two explicit dimensionless thresholds. Outside this window the variance is monotone; an interior maximum is impossible. A natural equal-isolated-variance regime has an exact optimal dispersal rate and a sharp, unattained one-half bound on the possible fractional variance reduction.

Specifically, take \(a,b,u,v>0\) and \(d\geq0\). Define
\[
L=\frac{b^2}{a^2},\qquad U=\frac{a+3b}{3a+b},\qquad q=\frac vu.
\]
If \(a\neq b\), the stationary regional variance \(V(d)\) has a unique strict global minimum at \(d_*>0\) precisely when
\[
\min\{L,U\}<q<\max\{L,U\}.
\]
In that case \(d_*\) is the unique positive solution of
\[
\frac vu=\frac{b^2(a+b)+4b(a+b)d_*+2(a+3b)d_*^2}{a^2(a+b)+4a(a+b)d_*+2(3a+b)d_*^2}.
\]
If \(a=b\), the variance is constant for all \(d\geq0\). If \(a\ne b\) and the strict window fails, there is no interior stationary point and \(V\) is strictly monotone on \(d>0\); the optimum then lies at zero dispersal or is the unattained limiting value as \(d\to\infty\). No member of this family has a strict interior maximum.

In the equal-isolated-variance noise regime \(u=a\) and \(v=b\), the two endpoint variances agree and the unique optimum for \(a\ne b\) is
\[
\boxed{d_*=\sqrt{ab/2}},\qquad V(0)=\lim_{d\to\infty}V(d)=1.
\]
For every \(d>0\), \(V(d)>1/2\); the best fractional suppression of regional variance can approach but never reach one half as the regulation-rate contrast grows without bound.

## Assumptions and scope

Let \(W_1,W_2\) be independent standard Brownian motions and \(X_1,X_2\) be real-valued deviations of habitat abundances from reference equilibria. Their exact continuous-time Ornstein–Uhlenbeck model is
\[
\begin{aligned}
\mathrm dX_1&=[-(a+d)X_1+dX_2]\,\mathrm dt+\sqrt{u}\,\mathrm dW_1,\\
\mathrm dX_2&=[dX_1-(b+d)X_2]\,\mathrm dt+\sqrt{v}\,\mathrm dW_2.
\end{aligned}
\]
All regulation rates \(a,b\) and noise intensities \(u,v\) are strictly positive and **fixed while dispersal varies**; \(d\geq0\) is the symmetric per-individual exchange rate. Here \(V(d)=\operatorname{Var}(X_1+X_2)\) is measured in the unique stationary Gaussian law. Fluctuations, not nonnegative integer populations, are modeled: the Gaussian process may take negative values. There are no absorptions, species interactions, temporally correlated environmental shocks, or nonlinear demographic claims.

## Proof

Set \(s=a+b\), \(B=s+2d\), and \(K=ab+sd\). The drift matrix
\[
A=\begin{pmatrix}a+d&-d\\-d&b+d\end{pmatrix}
\]
is symmetric positive definite since its trace is positive and its determinant is \(K>0\). Thus the stationary covariance matrix \(C\) is unique, symmetric positive definite, and solves the continuous Lyapunov equation
\[
AC+CA=\operatorname{diag}(u,v).
\]
Writing \(C=(c_{ij})\), its three scalar equations are
\[
\begin{aligned}
2(a+d)c_{11}-2dc_{12}&=u,\\
(s+2d)c_{12}-d(c_{11}+c_{22})&=0,\\
2(b+d)c_{22}-2dc_{12}&=v.
\end{aligned}
\]
Solving this nonsingular system gives the **exact** regional variance
\[
\boxed{V(d)=\frac{(s+4d)[bu+av+d(u+v)]}{2(s+2d)(ab+sd)}}.
\]
Differentiating and simplifying yields
\[
V'(d)=\frac{(a-b)[uP_b(d)-vP_a(d)]}{2(s+2d)^2(ab+sd)^2},
\]
where the positive polynomials are
\[
\begin{aligned}
P_b(d)&=b^2s+4bsd+2(a+3b)d^2,\\
P_a(d)&=a^2s+4asd+2(3a+b)d^2.
\end{aligned}
\]
Put \(R(d)=P_b(d)/P_a(d)\). A second exact identity is
\[
R'(d)=\frac{4(a-b)s(s+2d)(ab+sd)}{P_a(d)^2}.
\]
Hence, for unequal regulation rates, \(R\) is strictly monotone, with endpoint values
\[
R(0)=\frac{b^2}{a^2},\qquad \lim_{d\to\infty}R(d)=\frac{a+3b}{3a+b}.
\]
Moreover, the sign of \(V'(d)\) is the sign of \((a-b)(R(d)-v/u)\). When \(R\) crosses the noise ratio, this sign changes only from negative to positive: it cannot change in the reverse direction, since the sign of \(R'\) is also the sign of \(a-b\). This proves the necessary-and-sufficient open window, strict uniqueness and global minimality, the boundary monotonicity assertions, and the absence of interior maxima. For \(a=b\), the displayed derivative vanishes identically and the formula reduces to \((u+v)/(2a)\).

For \(u=a\) and \(v=b\), substitution gives the exact identity
\[
V(d)=1-\frac{d(a-b)^2}{2(s+2d)(ab+sd)}.
\]
Thus \(V(0)=V(\infty)=1\) and, for unequal rates, the variance is strictly smaller than one at every finite positive dispersal rate. The reduction is maximized when the positive function \(d/[(s+2d)(ab+sd)]\) is maximized. Its derivative has the sign of \(ab-2d^2\), so the unique maximizer is \(d_*=\sqrt{ab/2}\).

To prove sharpness, observe
\[
(s+2d)(ab+sd)-d(a-b)^2=abs+6abd+2sd^2>0.
\]
Therefore the decrease from the endpoint value one is strictly below one half. At \(a=1\), \(b\to\infty\), with \(d=\sqrt{b/2}\), the decrease tends to one half, establishing that the bound is sharp but unattainable. For the exact illustration \(a=u=1\), \(b=v=2\), the minimizer is \(d=1\) and \(V(1)=49/50\).

## Verification

Run `python3 verify_ou.py` using Python 3's standard library. The script tests the two displayed derivative identities and the matched-noise identity as multivariate **integer-polynomial identities**, not at sampled parameters; it also solves the stationary Lyapunov equations by rational Gaussian elimination in 288 independent rational-parameter cases and checks the rational witness. Its expected final line is

`VERIFY_OK polynomial_derivative=1 polynomial_ratio_monotonicity=1 matched_noise_identity=1 rational_lyapunov_cases=288 exact_witness=1`

These checks corroborate the algebra. The proof of all-parameter monotonicity and uniqueness additionally uses the positive-denominator sign argument given above; the finite parameter checks are not substituted for that proof.

## Relationship to prior work

Liebhold, Johnson and Bjørnstad (2006) examined how heterogeneous density dependence changes dispersal-induced synchronization in ecological populations, using historical observations and a second-order stochastic model. Abbott (2011) synthesized the competing stabilizing and synchronizing consequences of dispersal. Wang, Haegeman and Loreau (2015) studied total metapopulation variability using a continuous-time logistic model with environmental noise and covariance linearization: in their homogeneous setting total variability is invariant under dispersal, while their heterogeneous two-patch numerical comparisons show context-dependent stabilizing and destabilizing effects. The present claim does not appropriate those general ecological mechanisms or the classical Lyapunov equation. It gives an exact necessary-and-sufficient **noise-ratio** condition, uniqueness of an interior symmetric-coupling optimum, a closed-form equal-isolated-variance optimum, and a sharp half-suppression boundary for the separately specified additive-noise Ornstein–Uhlenbeck system. The published nonlinear-logistic model and its equilibrium-dependent noise normalization do not state this additive-noise phase law; the present theorem is not a claim about the nonlinear model. Ben Zion, Yaari and Shnerb (2010) optimized expected extinction time in nonlinear stochastic systems, a different quantity and dynamics.

## Limitations

The theorem is exact only for two patches, independent additive white noises of fixed strengths, symmetric exchange, and linear mean reversion. It is not a bound on absolute abundance or extinction probability. Underlying nonlinear ecological fluctuations need not obey the theorem away from a locally valid, fixed-parameter approximation. The half-suppression result assumes the special, biologically interpretable calibration of equal isolated fluctuation variances; no uniform one-half bound is claimed for unrestricted noise intensities. Earlier general stochastic-control or covariance-optimization results may subsume parts of the calculation; no independent external validation has been performed.

## References

1. A. M. Liebhold, D. M. Johnson, and O. N. Bjørnstad, “Geographic variation in density-dependent dynamics impacts the synchronizing effect of dispersal and regional stochasticity,” *Population Ecology* **48** (2006), 131–138, doi:10.1007/s10144-005-0248-6. First publicly available online January 26, 2006.
2. K. C. Abbott, “A dispersal-induced paradox: synchrony and stability in stochastic metapopulations,” *Ecology Letters* **14** (2011), 1158–1169, doi:10.1111/j.1461-0248.2011.01670.x.
3. S. Wang, B. Haegeman, and M. Loreau, “Dispersal and metapopulation stability,” *PeerJ* **3** (2015), e1295, doi:10.7717/peerj.1295.
4. Y. Ben Zion, G. Yaari, and N. M. Shnerb, “Optimizing metapopulation sustainability through a checkerboard strategy,” *PLOS Computational Biology* **6** (2010), e1000643, doi:10.1371/journal.pcbi.1000643.
