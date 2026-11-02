# A complete equilibrium-covariance camouflage manifold for a switching harmonic trap

## Finding

Let a Brownian particle experience two strictly positive, distinct harmonic stiffnesses. Although its stationary position distribution is non-Gaussian, the **entire stationary position autocovariance** can be exactly that of an equilibrium Ornstein--Uhlenbeck particle. For each prescribed effective relaxation rate \(\rho>0\), the complete set of such strictly switching traps is parametrized by arbitrary \(0<k_1<\rho<k_2\), with transition rates

\[
\alpha=\frac{(\rho-k_1)(\rho+k_2)}{k_2-k_1},\qquad
\beta=\frac{(k_2-\rho)(\rho+k_1)}{k_2-k_1}.
\]

Their exact stationary covariance is

\[
\mathbb E[X_tX_0]=\frac{D}{\rho}e^{-\rho|t|}\qquad(t\in\mathbb R),
\]

identical to that of \(dY_t=-\rho Y_t\,dt+\sqrt{2D}\,dW_t\) in equilibrium. Conversely, every positive-rate, two-distinct-positive-stiffness model with a one-exponential stationary covariance occurs in this family. However, its stationary fourth cumulant is strictly positive:

\[
\boxed{\kappa_4(X_0)=
\frac{9D^2(\rho-k_1)(k_2-\rho)}{
\rho^2\,[\rho^2+\rho(k_1+k_2)+3k_1k_2]}>0.}
\]

Thus arbitrary ideal **second-order temporal measurements of position** cannot distinguish these nonequilibrium models from the indicated equilibrium process, whereas a stationary fourth-order measurement does.

## Assumptions and scope

Fix \(D>0\), \(0<k_1<k_2\), and \(\alpha,\beta>0\). Independently of a standard one-dimensional Brownian motion \(W\), let \(J\) be an irreducible two-state continuous-time Markov chain jumping \(1\to2\) at rate \(\alpha\) and \(2\to1\) at rate \(\beta\). Consider the unique stationary solution of

\[
 dX_t=-k_{J_t}X_t\,dt+\sqrt{2D}\,dW_t.
\]

All covariances refer to a *single particle's position at two different times*, not correlations between different particles at the same time. Stationary means vanish. Both stiffnesses are strictly positive and distinct; switching rates are finite and strictly positive. No claim is made for coincident stiffnesses, vanishing switching rates, correlated thermal noise, or noisy finite data. The stationary solution exists with moments of every order: its stochastic convolution is bounded in conditional variance by \(D/k_1\).

## Proof

**Step 1: exact second moments.** Put \(q=\alpha+\beta\),

\[
 K=\begin{pmatrix}k_1&0\\0&k_2\end{pmatrix},\quad
 Q^{\mathsf T}=\begin{pmatrix}-\alpha&\beta\\\alpha&-\beta\end{pmatrix},\quad
 \pi=\frac1q\binom{\beta}{\alpha}.
\]

The stationary state-resolved second moments \(w_i=\mathbb E[X_0^2\mathbf1_{\{J_0=i\}}]\) satisfy, by the stationary generator identity,

\[
 (2K-Q^{\mathsf T})w=2D\pi.
\]

Solving this nonsingular system yields

\[
 w_1=\frac{D\beta(q+2k_2)}{qH},\qquad
 w_2=\frac{D\alpha(q+2k_1)}{qH},\qquad
 H=2k_1k_2+\alpha k_2+\beta k_1,
\]

and therefore

\[
 v:=\mathbb E[X_0^2]=\frac{D(q^2+2\alpha k_1+2\beta k_2)}{qH}>0.
\]

Stationarity of \(X^2\) implies \(\mathbb E[k_{J_0}X_0^2]=D\).

**Step 2: full covariance and its spectral test.** For \(t\ge0\), the Markov property and independence of future Brownian increments give

\[
 C(t):=\mathbb E[X_tX_0]=\mathbf1^{\mathsf T}
 \exp[(Q^{\mathsf T}-K)t]w,
\]

where \(\mathbf1=(1,1)^{\mathsf T}\). In particular \(C(0)=v\) and \(C'(0+)=-D\). By Cayley--Hamilton, writing

\[
 T=k_1+k_2+q,\qquad
 \Delta=k_1k_2+k_1\beta+k_2\alpha,
\]

we have

\[
 C''(t)+T C'(t)+\Delta C(t)=0\qquad(t>0).
\]

The two characteristic relaxation rates are positive and distinct because

\[
 T^2-4\Delta=(k_1+\alpha-k_2-\beta)^2+4\alpha\beta>0.
\]

If \(C(t)\) is a single exponential, its exponent must be \(\rho=D/v\) by its initial slope, and necessarily \(\rho^2-T\rho+\Delta=0\). Substituting the displayed exact \(v\), direct denominator-clearing gives the identity

\[
 \left(\frac Dv\right)^2-T\frac Dv+\Delta
 =\frac{\alpha\beta(k_2-k_1)^2\,F}
 {[q^2+2\alpha k_1+2\beta k_2]^2},
 \quad F=q^2+2(\beta-\alpha)(k_2-k_1)-4k_1k_2.
\]

Every prefactor outside \(F\) is strictly positive. Conversely, if \(F=0\), then \(\rho=D/v\) solves the characteristic polynomial; the function \(v e^{-\rho t}\) has the same two initial conditions and solves the same second-order ODE as \(C\). ODE uniqueness makes them equal for all \(t\ge0\). Stationarity extends the equality to negative lags. Thus **single-exponential covariance is equivalent to \(F=0\)**.

**Step 3: solve the complete positive-rate family.** Set \(q=\alpha+\beta\) and \(\delta=k_2-k_1>0\). Solving \(F=0\) together with the definition of \(q\) gives

\[
 \alpha=\frac{(q-2k_1)(q+2k_2)}{4\delta},\qquad
 \beta=\frac{(2k_2-q)(q+2k_1)}{4\delta}.
\]

Consequently \(\alpha,\beta>0\) is equivalent to \(2k_1<q<2k_2\). Direct substitution into the variance expression gives \(v=2D/q\), so \(\rho=D/v=q/2\). Replacing \(q\) by \(2\rho\) yields exactly the two rate formulas in the finding. Their positivity is equivalent to \(k_1<\rho<k_2\). This proves both directions and exhaustiveness, including the exclusion of the boundary values for strictly positive switching.

**Step 4: fourth cumulant and strict non-Gaussianity.** Let \(z_i=\mathbb E[X_0^4\mathbf1_{\{J_0=i\}}]\). Itô's formula and the stationary generator give the exact fourth-moment system

\[
 (4K-Q^{\mathsf T})z=12Dw.
\]

Hence \(\mathbb E[X_0^4]=\mathbf1^{\mathsf T}12D(4K-Q^{\mathsf T})^{-1}w\). Subtracting \(3v^2\), substituting the rates from Step 3, and simplifying yields precisely the boxed positive formula. Positivity is strict since \(k_1<\rho<k_2\); hence \(X_0\) is not Gaussian. All moments used exist by the uniform conditional-variance bound.

For intuition, conditional on the entire past path of \(J\), \(X_0\) is centered Gaussian with variance

\[
 V=2D\int_0^\infty \exp\!\left(-2\int_0^s k_{J_{-u}}\,du\right)ds.
\]

The nondegenerate mixing of variances is an established property of this model, not a new assertion. The new exact expression quantifies its fourth cumulant *on the complete covariance-camouflage family*.

**Exact example.** Choose \(k_1=1\), \(k_2=4\), \(\rho=2\), \(D=1\). Then \(\alpha=\beta=2\), \(C(t)=\frac12e^{-2|t|}\), yet

\[
 \mathbb E[X_0^4]=\frac{12}{13},\qquad
 \kappa_4(X_0)=\frac9{52},\qquad
 \frac{\mathbb E[X_0^4]}{v^2}=\frac{48}{13}>3.
\]

This example uses symmetric switching, but the full manifold permits unequal switching rates.

## Verification

`verify.py` uses exact symbolic algebra and rational arithmetic. It derives the state-resolved second/fourth moments directly from two matrix inverses; checks the characteristic polynomial factorization as a rational identity in all free parameters; checks the rate-parameterization, the exact covariance initial slope, and the fourth-cumulant identity; and verifies multiple strictly admissible rational parameter examples and an off-resonance control. With SymPy installed, run `python verify.py`. The completed run reported `PASS: 229 exact symbolic and rational identity checks`. The mathematical claims about all positive real parameters rely on the analytic generator, algebra, positivity, and ODE-uniqueness argument above, not on the finite sample checks.

## Relationship to prior work

Biroli, Kulkarni, Majumdar, and Schehr [1] study exactly the switching harmonic trap, deriving the stationary Gaussian variance mixture and *spatial* inter-particle correlations. The distributional mixture and ensuing non-Gaussian marginal behavior are therefore prior results. Their inspected article does not isolate the present one-particle **temporal covariance** equivalence to equilibrium, its complete positive-rate locus, or the displayed fourth-cumulant identity restricted to that locus.

Huang, Jansen, Mandjes, Spreij, and De Turck [2] already develop general forward covariance and all-order moment methods for Markov-modulated OU processes. Equations in Steps 1, 2, and 4 are specializations of that general machinery, not independently new general techniques. The contribution assessed here is the **inverse iff classification of a nontrivial two-dimensional hidden-parameter fiber that completely cancels one covariance mode**, plus its explicitly non-Gaussian fourth-cumulant signature. General forward formulae give the raw ingredients but do not themselves state that classification; algebraic implication risk remains.

Zhang and Wang [3] analyze stationary *one-time distributions* of two-state Markov-switching OU processes. Frydel [4] analyzes stationary laws with *on/off* rather than two strictly positive stiffnesses. Neither inspected work identifies the present complete temporal-covariance camouflage manifold. Only publication-priority comparison, not independent confirmation of novelty, is intended.

## Limitations

Equality here is exclusively of covariance functions (and hence of all second-order spectral statistics), **not** of the complete finite-dimensional distributions or path laws. Distinguishability by the fourth cumulant assumes ideal stationary measurements; no finite-data statistical power bound is proved. The theorem requires independent additive Brownian noise of constant diffusivity, two strictly positive distinct stiffnesses, and a two-state time-homogeneous Markov environment with strictly positive rates. More general colored-noise, non-Markov, or random-diffusivity systems are outside the statement. The earlier published general Markov-modulated forward formulas can be specialized to rederive these identities; definitive publication priority and independent scientific audit remain outstanding.

## References

1. M. Biroli, M. Kulkarni, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570, first posted 2023-12-05, https://arxiv.org/abs/2312.02570.
2. G. Huang, H. M. Jansen, M. Mandjes, P. Spreij, and K. De Turck, *Markov-modulated Ornstein-Uhlenbeck processes*, arXiv:1412.7952, https://arxiv.org/abs/1412.7952.
3. Z. Zhang and W. Wang, *The stationary distribution of Ornstein-Uhlenbeck process with a two-state Markov switching*, Communications in Statistics--Simulation and Computation 46 (2017), 4783--4794, https://doi.org/10.1080/03610918.2015.1132321.
4. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213, https://arxiv.org/abs/2407.12213.
