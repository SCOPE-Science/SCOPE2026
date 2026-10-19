# Gaussian diagonal trajectories and identifiable hidden switching in a complementary-diffusivity harmonic trap

## Finding

A two-temperature harmonic diffusion can have **two orthogonal observed trajectories that are each exactly Gaussian Ornstein–Uhlenbeck processes at every collection of times**, while their joint process is strictly non-Gaussian. In this example all matrix-valued two-time covariances coincide with those of an ordinary isotropic Gaussian OU diffusion. Nevertheless, the hidden temperature-switching rate is recovered exactly from a two-time fourth-order cross-covariance, and the two exactly Gaussian projection directions are classified sharply.

Let \(\kappa,\gamma,\bar D>0\) and \(0<|\delta|<\bar D\). Let \(S_t\in\{-1,1\}\) be a stationary symmetric continuous-time chain that reverses sign at rate \(\gamma\), independent of two independent Brownian motions. Define the stationary planar process by
\[
\begin{aligned}
dX_t&=-\kappa X_t\,dt+\sqrt{2(\bar D+\delta S_t)}\,dW^1_t,\\
dY_t&=-\kappa Y_t\,dt+\sqrt{2(\bar D-\delta S_t)}\,dW^2_t.
\end{aligned}
\]
The full centered covariance is exactly
\[
Z_t=(X_t,Y_t)^{\mathsf T},\qquad\mathbb E[Z_t Z_s^{\mathsf T}]
=\frac{\bar D}{\kappa}e^{-\kappa|t-s|}I_2,
\]
where the left-hand side is a \(2\times2\) matrix.

For every angle \(\theta\), the projection \(P_\theta(t)=X_t\cos\theta+Y_t\sin\theta\) obeys
\[
\operatorname{cum}_4(P_\theta(t))
=\frac{3\delta^2}{\kappa(\kappa+\gamma)}\cos^2(2\theta).
\]
Consequently \(P_\theta\) is a Gaussian process **if and only if** \(\theta=\pi/4\pmod{\pi/2}\). At those two orthogonal directions its complete process law equals that of a stationary scalar OU process with drift \(-\kappa\) and diffusivity \(\bar D\). Let \(U=(X+Y)/\sqrt2\) and \(V=(X-Y)/\sqrt2\). Despite these two Gaussian process laws and their vanishing linear cross-covariance at all lags,
\[
\operatorname{Cov}(U_t^2,V_s^2)
=\frac{2\delta^2}{\kappa(\kappa+\gamma)}e^{-2\kappa|t-s|}>0.
\]

A second, negative fourth-order signature is \(A(t)=\operatorname{Cov}(X_t^2,Y_0^2)\), for \(t\ge0\). It satisfies \(A(t)=-\delta^2 F(t)<0\), where
\[
F(t)=
\begin{cases}
\displaystyle\frac{\kappa e^{-2\gamma t}-\gamma e^{-2\kappa t}}{\kappa(\kappa+\gamma)(\kappa-\gamma)},&\kappa\ne\gamma,\\[7pt]
\displaystyle e^{-2\kappa t}\left(\frac1{2\kappa^2}+\frac t\kappa\right),&\kappa=\gamma.
\end{cases}
\]
In particular \(A(0)=-\delta^2/[\kappa(\kappa+\gamma)]\), \(A'(0^+)=0\), and
\[
\boxed{\quad\gamma=-\frac{A''(0^+)}{4\kappa A(0)},\qquad
\delta^2=-\kappa(\kappa+\gamma)A(0).\quad}
\]
Thus the observed second-order covariance and this one fourth-order lag function identify \(\kappa,\bar D,\gamma,|\delta|\) exactly; the sign of \(\delta\) is unidentifiable because reversing the hidden state labels leaves the observed law unchanged.

The stationary law is a non-Gaussian Gaussian-variance mixture with an exact beta mixing variable. Its characteristic function is
\[
\mathbb E[e^{i(pX+qY)}]
=\exp\left[-\frac{\bar D}{2\kappa}(p^2+q^2)\right]
{}_0F_1\!\left(;\frac12+\frac\gamma{2\kappa};
\frac{\delta^2(p^2-q^2)^2}{16\kappa^2}\right).
\]
For any \(\theta\), the sixth cumulant is zero and the eighth cumulant is strictly negative off the two Gaussian directions:
\[
\operatorname{cum}_8(P_\theta(t))
=-\frac{630\delta^4}{\kappa(\kappa+\gamma)^2(3\kappa+\gamma)}\cos^4(2\theta).
\]

## Assumptions and scope

All parameters are finite. Both effective noise intensities remain strictly positive by \(0<|\delta|<\bar D\). The telegraph chain is stationary and independent of the Brownian motions. All initial data refer to the unique stationary solution, constructed by integrating from past infinity. The phase-space hidden state is time-even for the probabilistic statements; no thermodynamic entropy-production or experimental observability claim is made. Projection-Gaussianity means joint Gaussianity at every finite set of observation times, not merely at a single time.

## Proof

**1. Stationary construction and conditional normality.** The unique stationary solution is
\[
X_t=\int_{-\infty}^t e^{-\kappa(t-r)}\sqrt{2(\bar D+\delta S_r)}\,dW^1_r,
\quad
Y_t=\int_{-\infty}^t e^{-\kappa(t-r)}\sqrt{2(\bar D-\delta S_r)}\,dW^2_r.
\]
Convergence holds in \(L^2\) (indeed in every finite moment). Two solutions with the same drivers contract by \(e^{-\kappa t}\). Conditional on the whole telegraph path, the two coordinates are independent centered Gaussian processes. Let
\[
Q_t=2\kappa\int_{-\infty}^t e^{-2\kappa(t-r)}S_r\,dr.
\]
Then \(|Q_t|<1\) almost surely and the conditional one-time variances are
\[
V_X(t)=\frac{\bar D+\delta Q_t}{\kappa},
\qquad V_Y(t)=\frac{\bar D-\delta Q_t}{\kappa}.
\]
For \(t\ge s\), unconditional cross-coordinate covariance is zero and each same-coordinate covariance is \((\bar D/\kappa)e^{-\kappa(t-s)}\), since \(\mathbb E S_t=0\). This proves the covariance claim.

**2. The exact mixing law.** Between telegraph flips, \(\dot Q=2\kappa(S-Q)\). Write stationary densities \(p_+(q),p_-(q)\) for the two telegraph states on \((-1,1)\). The stationary total probability flux vanishes (the state is confined inside \((-1,1)\)); hence \((1-q)p_+(q)=(1+q)p_-(q)\). The first balance equation then gives
\[
\frac{d}{dq}\big((1-q^2)p(q)\big)=-\frac{\gamma}{\kappa}q p(q),\qquad p=p_++p_-.
\]
Putting \(\nu=\gamma/(2\kappa)>0\), normalization yields the unique density
\[
p(q)=\frac{\Gamma(\nu+\tfrac12)}{\sqrt\pi\,\Gamma(\nu)}(1-q^2)^{\nu-1},\qquad -1<q<1.
\]
Thus \(\mathbb E Q=0\), \(\mathbb E Q^2=1/(2\nu+1)=\kappa/(\kappa+\gamma)\), and
\(\mathbb E Q^4=3/[(2\nu+1)(2\nu+3)]\). The beta integral gives \(\mathbb E e^{zQ}={}_0F_1(;\nu+1/2;z^2/4)\); conditioning on \(Q\) proves the claimed characteristic function.

**3. Classification of Gaussian directions and fourth/eighth cumulants.** Conditional on the telegraph path, \(P_\theta(t)\) is centered Gaussian with variance \(\bar D/\kappa+(\delta/\kappa)Q_t\cos2\theta\). The exact Gaussian-mixture identity \(\operatorname{cum}_4(P)=3\operatorname{Var}(\operatorname{Var}(P\mid S))\) gives the fourth-cumulant formula, strictly positive unless \(\cos2\theta=0\). For a Gaussian direction and times \(t_1,\dots,t_n\), its entire conditional covariance matrix has entries
\[
\operatorname{Cov}(P_\theta(t_i),P_\theta(t_j)\mid S)
=(\bar D/\kappa)e^{-\kappa|t_i-t_j|},
\]
independent of \(S\); hence its unconditional finite-dimensional law is the same Gaussian OU law. The fourth cumulant proves the converse. Expansion of the log-moment-generating function \(\bar D z^2/(2\kappa)+\log\mathbb E\exp[(\delta z^2/(2\kappa))Q\cos2\theta]\) gives the sixth cumulant zero and eighth cumulant
\(105(\delta\cos2\theta/\kappa)^4\operatorname{cum}_4(Q)\), where \(\operatorname{cum}_4(Q)=-6\kappa^3/[(\kappa+\gamma)^2(3\kappa+\gamma)]\).

**4. Correlated squares of two Gaussian projections.** Given \(S\), both \(U\) and \(V\) have constant (nonrandom) conditional variance \(\bar D/\kappa\), but their *conditional* cross-time covariance is \(\delta e^{-\kappa|t-s|}Q_{\min(t,s)}/\kappa\). Wick's identity for a centered Gaussian pair gives \(\operatorname{Cov}(U_t^2,V_s^2\mid S)=2(\delta/\kappa)^2 e^{-2\kappa|t-s|}Q_{\min(t,s)}^2\). Averaging yields the displayed positive formula. Unconditional \(\operatorname{Cov}(U_t,V_s)=0\) since \(\mathbb EQ=0\), so the joint process cannot be Gaussian.

**5. Fourth-order lag and parameter identification.** Conditional independence of the whole coordinate paths gives \(A(t)=\operatorname{Cov}(V_X(t),V_Y(0))=-(\delta/\kappa)^2\mathbb E[Q_tQ_0]\). Let \(B(t)=\mathbb E[S_tQ_0]\) and \(G(t)=\mathbb E[Q_tQ_0]\). The telegraph generator gives \(B'(t)=-2\gamma B(t)\); the filter equation gives \(G'(t)=-2\kappa G(t)+2\kappa B(t)\). Stationarity yields \(B(0)=G(0)=\kappa/(\kappa+\gamma)\). Solving the two linear equations gives \(G(t)=\kappa^2F(t)\) with \(F\) above, including the repeated-root limit \(\kappa=\gamma\). It follows that \(G(t)>0\) because it is the convolution of a positive kernel with the strictly positive covariance \(\mathbb E S_tS_0=e^{-2\gamma|t|}\); hence \(A(t)<0\). Differentiating at zero gives \(A'(0^+)=0\) and \(A''(0^+)=-4\kappa\gamma A(0)\), proving both inverse formulas. The second-order curve provides \(\kappa\) from its exponential decay and \(\bar D\) from its amplitude.

## Verification

The companion executable `VERIFY.py` independently reconstructs the stationary polynomial generator recurrence for mixed moments \(\mathbb E[S^\eta X^{2p}Y^{2q}]\), derives fourth-, sixth-, and eighth-cumulant formulas, checks the beta-integral moments, and checks the repeated-pole lag formula and inverse parameter identity symbolically. It uses exact rational/symbolic algebra, not finite sampling. The proof of process-level Gaussianity is the deterministic conditional-covariance calculation in step 3 and does not rely on the checker.

## Relationship to prior work

Chechkin et al. [1] establish Brownian-yet-non-Gaussian fluctuating diffusivity; the conditional-Gaussian-mixture mechanism is well known and not claimed as novel. Huang et al. [2] establish general moment and transform machinery for Markov-modulated OU systems, including multiple components driven by one switching environment; their general model contains this SDE as a parameter specialization, so the conditional-normal representation and polynomial moment recurrences are prior knowledge. Alexandre et al. [3] derive general fourth-cumulant fluctuation formulas for spatially varying diffusivity near surfaces; generic fourth-cumulant positivity is not the new claim. Ślęzak et al. [4] explain how Gaussian marginals can conceal non-Gaussian temporal dependence in superstatistical Langevin systems.

The assessed contribution is narrower and comparative: for *complementary* switching noise in a planar harmonic trap, it identifies **all and only** the two Gaussian process projections despite isotropic covariance, proves the two Gaussian processes jointly non-Gaussian by an exact signed fourth-order law, and recovers the hidden flip rate from a two-time fourth-order derivative with a sharp nonzero-modulation condition. These linked statements are not stated in the inspected treatments. They follow by additional model-specific analysis from broad known conditional-Gaussian methods. The possibility of unlocated equivalent special-case statements remains a priority risk.

## Limitations

The rates and noise intensities are constant except for a symmetric two-state common modulator; the theorem is not asserted for arbitrary switching laws, asymmetric stationary sign probabilities, time-dependent traps, nonlinear interactions or infinite-dimensional systems. No independent assessment of mathematical priority has occurred. The statistical inverse formula uses exact expected fourth-order functions and may be ill-conditioned with finite noisy data, particularly for small \(|\delta|\); it is not an estimator-performance theorem. The sign of \(\delta\) is not identifiable; when \(\delta=0\), switching is wholly unidentifiable. The result concerns dynamical distributions, not entropy production.

## References

[1] A. V. Chechkin, F. Seno, R. Metzler, I. M. Sokolov, *Brownian yet non-Gaussian diffusion: from superstatistics to subordination of diffusing diffusivities*, arXiv:1611.06202 (first public 2016-11-18). https://arxiv.org/abs/1611.06202

[2] G. Huang, H. M. Jansen, M. Mandjes, P. Spreij, K. De Turck, *Markov-modulated Ornstein-Uhlenbeck processes*, arXiv:1412.7952 (2014), esp. Sections 2, 4, 6 and Proposition 6.1. https://arxiv.org/abs/1412.7952

[3] A. Alexandre et al., *Non-Gaussian diffusion near surfaces*, arXiv:2207.01880 (first public 2022-07-05), including fourth-cumulant theory and supplementary material. https://arxiv.org/abs/2207.01880

[4] J. Ślęzak, R. Metzler, M. Magdziarz, *Superstatistical generalised Langevin equation: non-Gaussian viscoelastic anomalous diffusion*, arXiv:1710.02222 (2017). https://arxiv.org/abs/1710.02222
