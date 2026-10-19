# Exact finite-population memory decomposition for a three-regime noisy-voter model

## Finding

The three-environment noisy-voter model with randomly switching influencers has an **exact stationary two-time covariance at every integer population size**, not merely a large-population or linear-noise approximation. Its finite-population correction is a strictly positive, single-rate exponential:

\[
\operatorname{Cov}(X_N(0),X_N(t))
= C_\infty(t)+\frac{\kappa}{Nc+q}e^{-ct},\qquad t\geq0,
\]

where the continuum-limit covariance \(C_\infty\) is an explicit sum of two environmental relaxation kernels, and \(\kappa>0\) is explicitly computable and independent of \(N\). Thus changing population size affects only one decay component; the environmental contribution is identical for every \(N\). No stationary probability density or simulation is required.

## Assumptions and scope

There are \(N\ge1\) changeable voters, \(I(t)\in\{0,\ldots,N\}\) currently supporting opinion A, and a three-state independent continuous-time influencer environment \(S(t)\in\{0,1,2\}\). Let \(X_N=I/N\), \(a\ge0\), \(\alpha>0\), \(0<\delta<1\), \(\lambda>0\). Fix the voter herding rate to one, as in the source. Set

\[
q=\frac1{1+\alpha},\quad \beta=\frac{\alpha}{1+\alpha},\quad c=2a+\beta>0,
\qquad (z_0,z_1,z_2)=(0,\delta,1).
\]

At state \((i,s)\), the voter count increases/decreases by one with respective rates

\[
T^+_{i,s}=(N-i)\left[a+q\frac{i}{N}+\beta z_s\right],
\qquad
T^-_{i,s}=i\left[a+q\frac{N-i}{N}+\beta(1-z_s)\right].
\]

The environment independently jumps from \(0\) to \(1\) and from \(2\) to \(1\) with rate \(\lambda\), and from \(1\) to either endpoint with rate \(\lambda/2\). There are no simultaneous environment/voter jumps. The joint finite Markov chain is irreducible, including when \(a=0\), so its stationary covariance is well-defined. This theorem concerns its stationary law.

Define the stationary environment mean, and the voter mean,

\[
\bar z=\frac{1+2\delta}{4},\qquad \mu=\frac{a+\beta\bar z}{c}.
\]

Let the environment mode variances, relaxation rates, and their filtered stationary-variance contributions be

\[
V_1=\frac18,\quad V_2=\frac{(1-2\delta)^2}{16},\quad
\eta_1=\lambda,\quad\eta_2=2\lambda,
\quad E_j=\frac{\beta^2V_j}{c(c+\eta_j)}.
\]

Write \(V_\infty=E_1+E_2\),

\[
H_0=a+2q\mu(1-\mu)+\beta(\mu+\bar z-2\mu\bar z),
\qquad
\kappa=\frac{H_0}{2}-(c+q)V_\infty.
\]

For \(c,\eta>0\), define the continuous resonance-safe kernel

\[
G_{c,\eta}(t)=\begin{cases}
\dfrac{c e^{-\eta t}-\eta e^{-ct}}{c-\eta},&c\ne\eta,\\[4pt]
(1+ct)e^{-ct},&c=\eta.
\end{cases}
\]

Then the complete formulas for all integers \(N\ge1\), all indicated parameters, and all \(t\ge0\) are

\[
\boxed{\operatorname{Var}(X_N)=V_\infty+\frac{\kappa}{Nc+q}},
\quad
\boxed{C_\infty(t)=E_1G_{c,\lambda}(t)+E_2G_{c,2\lambda}(t)},
\]

\[
\boxed{\operatorname{Cov}(X_N(0),X_N(t))=
E_1G_{c,\lambda}(t)+E_2G_{c,2\lambda}(t)
+\frac{\kappa}{Nc+q}e^{-ct}}.
\]

The displayed \(V_\infty\) and \(C_\infty\) are exactly the stationary variance and covariance of the infinite-population piecewise-deterministic limit. The correction is strictly positive for every finite \(N\), and it is monotone decreasing in \(N\).

For example, \(a=1/10\), \(\alpha=1/2\), \(\delta=4/5\), \(\lambda=7/10\) give \(c=8/15\), \(q=2/3\), \(\mu=19/32\), \(V_\infty=3233/137344\), and \(\kappa=717501/2746880\). The exact variance at \(N=10\) is \(368487/5493760\), compared with the limiting variance \(3233/137344\).

## Proof

**1. Environmental eigenmodes.** The unique stationary environment weights are \((1/4,1/2,1/4)\). Its generator has orthogonal centered eigenfunctions \(f_1=(-1,0,1)\) and \(f_2=(1,-1,1)\), with eigenvalues \(-\lambda\) and \(-2\lambda\). Direct orthogonal projection gives

\[
z_s-\bar z=\frac12 f_1(s)+\frac{1-2\delta}{4}f_2(s),
\quad \operatorname{Var}_\pi(f_1)=\frac12,\quad\operatorname{Var}_\pi(f_2)=1.
\]

Therefore \(\operatorname{Cov}(z_{S(0)},z_{S(t)})=V_1e^{-\lambda|t|}+V_2e^{-2\lambda|t|}\).

**2. Exact first and cross moments at any \(N\).** The voter-count generator, applied to \(X_N\), gives \(LX_N=a+\beta z_s-cX_N\). Stationarity implies \(\mathbb E X_N=\mu\), with no dependence on \(N\). Applying the joint generator to \((X_N-\mu)f_j(S)\), whose two factors cannot jump together, yields

\[
\operatorname{Cov}(X_N,z_{S})=
\beta\left[\frac{V_1}{c+\lambda}+\frac{V_2}{c+2\lambda}\right].
\]

This identity is *exact* for every finite population; no diffusion or closure approximation has been made.

**3. Exact finite-size stationary variance.** The generator applied to \(X_N^2\) is \(2X_NLX_N+H(X_N,z_S)/N\), where

\[
H(x,z)=a+2q x(1-x)+\beta(x+z-2xz).
\]

Put \(v_N=\operatorname{Var}(X_N)\). Combining the quadratic stationary identity with step 2 gives

\[
2cv_N=2\beta\operatorname{Cov}(X_N,z_S)+\frac1N\,
\mathbb E H(X_N,z_S).
\]

Expanding the polynomial \(H\) and using the exact means and cross covariance produces

\[
\mathbb E H=H_0-2qv_N-2\beta\operatorname{Cov}(X_N,z_S).
\]

Solving this single linear equation yields

\[
v_N=\frac{\beta\operatorname{Cov}(X_N,z_S)(1-1/N)+H_0/(2N)}{c+q/N}
=V_\infty+\frac{\kappa}{Nc+q}.
\]

**4. Positivity.** In the stationary infinite-population system \(\dot X=c(\frac{a+\beta z_S}{c}-X)\), its bounded pullback solution is a strictly interior weighted average of past influencer targets: \(0<X<1\) almost surely, since the environment visits endpoints with positive frequency. From the same quadratic stationarity calculation without voter noise, \(V_\infty=\beta\operatorname{Cov}(X,z_S)/c\) and \(\mathbb E H(X,z_S)=H_0-2(c+q)V_\infty=2\kappa\). For every \(0<x<1\), \(0\le z\le1\), the expression \(H(x,z)>0\) because \(\beta[x(1-z)+(1-x)z]>0\). Hence \(\kappa>0\), including the boundary case \(a=0\).

**5. Two-time covariance.** Conditional expectations of the future centered count given the entire present joint state solve the linear drift equation. The environmental eigenfunctions satisfy \(\mathbb E[f_j(S(t))\mid S(0)]=e^{-\eta_jt}f_j(S(0))\), and step 2 supplies their exact stationary cross covariances with \(X_N(0)\). Integration gives

\[
C_N(t)=e^{-ct}v_N+
\sum_{j=1}^{2}\frac{\beta^2V_j}{(c+\eta_j)(c-\eta_j)}
\big(e^{-\eta_jt}-e^{-ct}\big),
\]

with each resonant quotient interpreted by its continuous limit. Rearrangement gives the boxed formula. Sending \(N\) to infinity verifies the stated limit kernel directly. No infinite-population proof is inferred from numerical finite enumeration; every identity above follows from generators.

## Verification

The accompanying `verification/check.py` uses only the Python standard library. It builds the *actual* finite-state Markov generator, solves its stationary equations in exact rational arithmetic, and compares the predicted cross moments, variance and covariance derivatives at lag zero against direct generator powers. Its 30 combinations cover populations from one through five, symmetric/asymmetric intermediate influence, zero/positive spontaneous opinion switching, and resonances \(c=\lambda\) or \(c=2\lambda\) when encountered. The test reports 210 exact covariance-derivative comparisons (orders zero through six) and positive finite-population coefficients. These checks are finite corroborations; the proof is the generator calculation above.

## Relationship to prior work

Caligiuri and Galla, *Noisy voter models in switching environments* (arXiv:2305.19096; *Physical Review E* 108, 044301, 2023), introduce the precise voter rates and the three-regime environment (their Eqs. (1), (2), and (34)). Their analysis obtains finite-population stationary densities numerically or through a linear-noise approximation about a piecewise-deterministic limit; the inspected text does not state an all-\(N\) exact two-time covariance or an exact single-exponential finite-size difference. The limiting colored-noise filter is classical, and the present claim does not assert that its component eigenmode calculation is new. The assessed distinction is the full finite-state voter chain's exact all-size correction, including its strictly positive coefficient, at **every** lag.

Hufton, Lin, Galla and McKane (arXiv:1512.00785) study intrinsic noise under environmental switching primarily through linear-noise approximations. Peralta and collaborators (arXiv:1807.04615) consider dynamic correlations on heterogeneous voter networks without this switching-influencer chain. Mankin, Ainsaar and Reiter (*Physical Review E* 60, 1374, 1999) treat a related three-level Markovian forcing and stationary densities, but not the present finite binary-voter covariance theorem. Related prior derivations of exact moments in other linear jump systems remain a publication-priority risk.

## Limitations

The result is stationary and assumes homogeneous complete mixing, constant herding and noise rates across environmental states, autonomous three-regime switching with the precise specified rates, and a fixed influencer population strength. It does not give the full stationary distribution, transient covariance from arbitrary starts, nonhomogeneous graphs, or arbitrary influencer switching. For \(N\) finite the count process without the environment is generally hidden-Markov rather than Markov; no contrary claim is made. Exact mathematical correctness does not by itself establish publication novelty. An independent literature-priority and scientific audit has not been performed.

## References

1. A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, arXiv:2305.19096 (first posted 2023-05-30); *Physical Review E* 108, 044301 (2023), DOI: 10.1103/PhysRevE.108.044301.
2. P. G. Hufton, Y. T. Lin, T. Galla and A. J. McKane, *Intrinsic noise in systems with switching environments*, arXiv:1512.00785 (2015); *Physical Review E* 93, 052119 (2016).
3. A. F. Peralta, A. Carro, M. San Miguel and R. Toral, *Stochastic pair approximation treatment of the noisy voter model*, arXiv:1807.04615 (2018); *New Journal of Physics* 20, 103045 (2018).
4. R. Mankin, A. Ainsaar and E. Reiter, *Trichotomous noise-induced transitions*, *Physical Review E* 60, 1374–1380 (1999), DOI: 10.1103/PhysRevE.60.1374.
