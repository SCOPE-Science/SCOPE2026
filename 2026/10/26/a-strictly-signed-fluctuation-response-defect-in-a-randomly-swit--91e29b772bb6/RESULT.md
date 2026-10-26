# A strictly signed fluctuation–response defect in a randomly switching harmonic trap

## Finding

Consider a stationary overdamped particle whose harmonic restoring coefficient switches between two values according to an independently evolving two-state Markov chain. Its equilibrium-form fluctuation–response identity has a *strictly positive* and explicitly computable defect at every positive time whenever the two stiffnesses differ. More remarkably, if one state is completely untrapped, the integrated defect does not depend on the nonzero trap stiffness.

Precisely, let the state \(S_t\in\{1,0\}\) jump from \(1\) to \(0\) at rate \(a>0\) and from \(0\) to \(1\) at rate \(b>0\), independently of a standard Brownian motion \(W_t\). For \(k_1>0\), \(k_0\ge0\), and \(D>0\), consider the stationary solution of
\[
 dX_t=-k_{S_t}X_t\,dt+\sqrt{2D}\,dW_t.
\]
Let \(C(t)=\mathbb E[X_tX_0]\), and let \(R(t)\) be the causal impulse response of the mean position to an **additive drift perturbation** \(f(t)\,dt\), with the environment left unperturbed; equivalently, \(R(t)=\mathbb E[\exp(-\int_0^t k_{S_u}\,du)]\) for \(t\ge0\). Put
\[
\begin{aligned}
 s&=a+b,\\
 Z&=ak_0+bk_1+2k_0k_1,\\
 Y&=ak_0+bk_1+k_0k_1,\\
 \Delta&=\sqrt{(k_1-k_0+a-b)^2+4ab},\\
 \lambda_{\pm}&=\frac{k_1+k_0+a+b\pm\Delta}{2}.
\end{aligned}
\]
Both \(Z,Y,\Delta\) and \(\lambda_\pm\) are strictly positive, with \(\lambda_+>\lambda_-\). Then for every \(t\ge0\),
\[
\boxed{\mathcal F(t):=-C'(t)-DR(t)
 =\frac{Dab(k_1-k_0)^2}{sZ\Delta}
 \left(e^{-\lambda_- t}-e^{-\lambda_+ t}\right).}
\]
Consequently \(\mathcal F(t)>0\) for **every** \(t>0\) if and only if \(k_1\ne k_0\); when the stiffnesses agree it vanishes identically. In the unequal case, its sole maximizer is
\[
 \boxed{t_*=\frac{\log(\lambda_+/\lambda_-)}{\Delta}.}
\]
The integrated sum rule is
\[
\boxed{\int_0^\infty\mathcal F(t)\,dt
=C(0)-D\int_0^\infty R(t)\,dt
=\frac{Dab(k_1-k_0)^2}{sZY}.}
\]
For a trap that is fully off in state \(0\), so \(k_0=0\), this reduces for every \(k_1>0\) to
\[
\boxed{\int_0^\infty\mathcal F(t)\,dt=\frac{Da}{b(a+b)},}
\]
independent of \(k_1\). In the symmetric-switching case \(a=b=r\), the value is \(D/(2r)\).

## Assumptions and scope

The Markov environment has rates \(a,b>0\) and stationary weights \(p=(b/s,a/s)^{\mathsf T}\), with vector coordinates ordered as trapped state \(1\), followed by state \(0\). The Brownian forcing is additive, homogeneous, and independent of the environment. A unique stationary joint state with finite second moments exists because \(k_1>0\) and the chain visits state \(1\) recurrently even when \(k_0=0\). In the response experiment only the additive force changes; the switching rates, trap stiffnesses and diffusion coefficient remain fixed. The response is defined with unit mobility absorbed into the force, not as the response to changing trap stiffness or bath temperature.

## Proof

**1. Moment and response equations.** Let
\[
 Q=\begin{pmatrix}-a&b\\a&-b\end{pmatrix},\qquad
 K=\operatorname{diag}(k_1,k_0),\qquad A=Q-K,
\]
and define \(u_i=\mathbb E[X_0^2\mathbf1_{\{S_0=i\}}]\). The stationary Itô equations give the *exact* linear system \((2K-Q)u=2Dp\), whence direct inversion yields
\[
 u=\frac{D}{sZ}\begin{pmatrix}b(s+2k_0)\\a(s+2k_1)\end{pmatrix}.
\]
Conditional expectation over future switching and Brownian increments gives, for all \(t\ge0\),
\[
 C(t)=\mathbf1^{\mathsf T}e^{At}u,
 \qquad R(t)=\mathbf1^{\mathsf T}e^{At}p.
\]
In particular, \(-C'(t)=k^{\mathsf T}e^{At}u\) with \(k=(k_1,k_0)^{\mathsf T}\). Both observables are finite because the stationary second moment is finite.

**2. Exact spectral defect.** The eigenvalues of \(A\) are \(-\lambda_-\) and \(-\lambda_+\). Indeed \(-\operatorname{tr} A=k_1+k_0+a+b\), \(\det A=Y>0\), and the spectral gap is \(\Delta>0\). It follows that \(\mathcal F(t)=-C'(t)-DR(t)\) is a linear combination of the two exponentials. Stationarity of \(\mathbb E[X_t^2]\) gives \(k^{\mathsf T}u=D\), hence \(\mathcal F(0)=0\). Also \(Au=Ku-2Dp\), so
\[
\begin{aligned}
\mathcal F'(0)
&=k^{\mathsf T}Au+Dk^{\mathsf T}p\\
&=k_1^2u_1+k_0^2u_0-D(k_1p_1+k_0p_0)\\
&=\frac{Dab(k_1-k_0)^2}{sZ}.
\end{aligned}
\]
A two-exponential function with these initial data is uniquely
\[
 \mathcal F(t)=\frac{\mathcal F'(0)}{\Delta}
 \left(e^{-\lambda_-t}-e^{-\lambda_+t}\right),
\]
which proves the claimed identity including all coefficients and limits. The exponential difference is strictly positive for all \(t>0\). Differentiating it gives the unique maximizer because its derivative starts positive and crosses zero once.

**3. Integrated identity and fully intermittent universality.** Since \(C(t)\to0\) and \(R(t)\to0\), integrating the defect yields the difference between stationary positional variance and the integrated drift susceptibility. Using \(\lambda_+\lambda_-=Y\),
\[
\int_0^\infty\mathcal F(t)\,dt
=\frac{\mathcal F'(0)}{\Delta}
\left(\frac1{\lambda_-}-\frac1{\lambda_+}\right)
=\frac{\mathcal F'(0)}Y.
\]
For \(k_0=0\), both \(Z\) and \(Y\) equal \(bk_1\), so the factor \(k_1^2\) cancels exactly. This proves the stiffness-independent sum rule without a strong-trap or slow-switching approximation.

## Verification

The accompanying standalone `verify_fluctuation_response.py` evaluates the two-state generator and second moments independently of the closed-form defect, then uses matrix exponentials to compare the predicted \(C(t)\), \(R(t)\), and their derivative combinations. It checks 960 time/parameter comparisons across 160 parameter regimes, including 40 fully off-trap cases, plus 160 sum-rule and peak checks. Two event-driven Monte Carlo tests simulate switching times and exact conditional Brownian increments as an independent numerical corroboration. The reproducibility command is `python verify_fluctuation_response.py` with NumPy and SciPy installed. These finite numerical tests corroborate, but do not replace, the analytic proof above.

## Relationship to prior work

Santra, Das, and Nath [1] studied intermittently harmonic Brownian motion, including unforced variance dynamics and stationary distributions. Alston, Cocconi, and Bertrand [2] established nonequilibrium entropy-production results for Markov-switching potentials, including harmonic stiffness switching. Frydel [3] derived stationary distributions and moments for fluctuating harmonic confinement and provides the most directly relevant recent model. Those model formulations, stochastic generators, stationary moment equations, entropy production, and standard response formalism are not claimed as new. The specific contribution here is the evaluated **all-lag sign-definite fluctuation–response defect**, its single-lag maximum, and the **exact stiffness-independent integrated defect** when one trap state is absent. The inspected relevant primary sections do not state this combined theorem.

## Limitations

The result is an exact statement for a scalar overdamped particle, independently Markov-switching *nonnegative* harmonic stiffness, additive white noise, and additive-drift linear response from stationarity. It makes no claim for non-Markov residence times, position-dependent switching, multiplicative diffusion, arbitrary nonlinear traps, or forcing that perturbs the switching mechanism. A known equilibrium-form relation can also be modified in alternative fluctuation–dissipation conventions, so the normalization of \(\mathcal F\) is essential. The formula is elementary once the precise coupled moment–response structure is derived, and a broader uninspected result on Markov-modulated linear diffusions could imply it; definitive publication priority is not established. Later work on semi-Markov fluctuating traps may contain related formulas and was not comprehensively inspected.

## References

[1] I. Santra, S. Das, and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (first public 2021-04-01), https://arxiv.org/abs/2104.00609.

[2] H. Alston, L. Cocconi, and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (first public 2022-02-05), https://arxiv.org/abs/2202.02630.

[3] D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (first public 2024-07-16), https://arxiv.org/abs/2407.12213.
