# A square-root spectral edge in the stationary correlations of a Poisson-reset Kuramoto order parameter

## Finding

Let \(\sigma,K,\lambda>0\) and \(R_0\in(0,1]\). In the thermodynamic-limit Lorentzian-frequency Kuramoto model restricted to the real, phase-aligned Ott–Antonsen manifold, reset the entire oscillator state to the same manifold state of order-parameter magnitude \(R_0\) at independent Poisson times of rate \(\lambda\). Between resets the order-parameter magnitude solves
\[
\dot R=\left(\frac K2-\sigma\right)R-\frac K2R^3.
\]
Write \(\mathcal C(t)=\operatorname{Cov}(R_s,R_{s+t})\) for its strictly stationary covariance, \(t\geq0\), and let \(f(t)\) be the deterministic solution with \(f(0)=R_0\). With \(A\sim\operatorname{Exp}(\lambda)\), the **exact all-lag identity** is
\[
\mathcal C(t)=e^{-\lambda t}\operatorname{Cov}(f(A),f(A+t)). \tag{1}
\]
Unless \(K>2\sigma\) and \(R_0=\sqrt{1-2\sigma/K}\), this covariance is strictly positive for every finite \(t\geq0\).

There are precisely three long-lag regimes.

**Below critical coupling, \(K<2\sigma\).** Put \(d_-=\sigma-K/2\) and
\[
H_- =\frac{R_0}{\sqrt{1+KR_0^2/(2d_-)}}.
\]
Then
\[
\mathcal C(t)\sim B_- e^{-(\lambda+d_-)t},\qquad
B_-=H_-\operatorname{Cov}\bigl(f(A),e^{-d_-A}\bigr)>0. \tag{2}
\]

**Above critical coupling, \(K>2\sigma\).** Put \(d_+=K-2\sigma\), \(R_*=\sqrt{1-2\sigma/K}\), and \(v_0=(R_*/R_0)^2-1\). If \(R_0\ne R_*\), then
\[
\mathcal C(t)\sim B_+e^{-(\lambda+d_+)t},\qquad
B_+=-\frac{R_*v_0}{2}\operatorname{Cov}\bigl(f(A),e^{-d_+A}\bigr)>0. \tag{3}
\]
If \(R_0=R_*\), the trajectory is constant and \(\mathcal C(t)=0\) identically.

**At critical coupling, \(K=2\sigma\).** Define \(\theta=(KR_0^2)^{-1}\) and
\[
\mu(\lambda)=\mathbb E[f(A)]
=\sqrt{\frac{\pi\lambda}{K}}\,e^{\lambda\theta}
\operatorname{erfc}\!\left(\sqrt{\lambda\theta}\right).
\]
Then \(\mu'(\lambda)>0\), and the sharp critical decorrelation law is
\[
\boxed{\mathcal C(t)=\frac{\mu'(\lambda)}{2\sqrt K}
 e^{-\lambda t}t^{-3/2}\bigl(1+O(t^{-1})\bigr),\qquad t\to\infty.} \tag{4}
\]
In particular, the algebraic factor is \(t^{-3/2}\), **not** the \(t^{-1/2}\) decay of the unrestarted critical trajectory.

The critical covariance also has the strictly positive spectral representation
\[
\mathcal C(t)=\int_0^\infty e^{-(\lambda+v)t}\rho(v)\,dv,
\]
where
\[
\boxed{\rho(v)=\frac{\lambda\sqrt v\,e^{-\theta v}}{\pi K(\lambda+v)}
\int_0^\infty\frac{\sqrt u\,e^{-\theta u}}{(\lambda+u+v)(\lambda+u)}\,du,\quad v>0,} \tag{5}
\]
and
\[
\boxed{\rho(v)\sim\frac{\mu'(\lambda)}{\sqrt{\pi K}}\sqrt v,\qquad v\downarrow0.} \tag{6}
\]
Thus the spectral edge is square-root rather than atomic, and \(\mathcal C\) is strictly completely monotone at criticality.

## Assumptions and scope

The intrinsic-frequency law is the centered Lorentzian of half-width \(\sigma\). The large-population, phase-aligned Ott–Antonsen reduction is assumed exact, and each reset reinitializes the *whole* system to the same compatible state, not merely its scalar order parameter while retaining hidden microscopic information. The resetting process is homogeneous Poisson, independent of the deterministic flow. Stationarity is the two-sided Poisson-renewal construction, for which the elapsed age at any fixed time has law \(\operatorname{Exp}(\lambda)\). All statements concern population-order-parameter fluctuations **across reset realizations**, not single-oscillator phase covariances or finite-population sampling noise.

## Proof

1. **Deterministic flow.** Put \(a=K/2-\sigma\) and \(b=K/2\). Integrating \(\dot f=af-bf^3\) gives, for \(a<0\) with \(d=-a\),
\[
f(s)=\frac{R_0e^{-ds}}{\sqrt{1+(bR_0^2/d)(1-e^{-2ds})}},
\]
and, for \(a>0\),
\[
f(s)=\frac{R_*}{\sqrt{1+v_0e^{-2as}}},\qquad R_*=\sqrt{a/b}.
\]
For \(a=0\), \(f(s)=[K(s+\theta)]^{-1/2}\). These formulas hold for all \(s\geq0\). Each nonconstant trajectory is strictly monotone.

2. **Exact stationary two-time law.** In a stationary Poisson-reset process, the age \(A\) is exponential and independent of future reset events. If no reset occurs in the following interval of length \(t\), an event of probability \(e^{-\lambda t}\), the future value is \(f(A+t)\). If at least one reset occurs, the future value is independent of \(A\). Apply total expectation to \(\mathbb E[f(A)R_{s+t}]\) and to the stationary mean \(\mathbb E[R_{s+t}]=\mu\); eliminating the conditional post-reset mean gives (1). For a nonconstant monotone \(f\), both \(f(A)\) and \(f(A+t)\) are strictly monotone in the same direction, so their covariance is positive, by the independent-copy covariance identity.

3. **Off-critical rates and coefficients.** When \(a<0\), the first flow formula yields \(e^{ds}f(s)\to H_-\). For any fixed \(A\), \(e^{dt}f(A+t)\to H_-e^{-dA}\). Uniform exponential domination permits passage through the age expectation and covariance in (1), proving (2). When \(a>0\), Taylor expansion gives \(f(A+t)-R_*=-(R_*v_0/2)e^{-2at}e^{-2aA}+O(e^{-4at}e^{-4aA})\) with an integrable dominating bound, proving (3). The strict sign follows from the same-direction or opposite-direction monotonicity of \(f(A)\) and the decreasing exponential and the sign of \(-v_0\).

4. **Critical asymptotic and its coefficient.** The critical flow equals \([K(s+\theta)]^{-1/2}\). Its stationary mean is the displayed complementary-error-function integral. Differentiation of the exponential age density, justified by boundedness of \(f\), gives
\[
\mu'(\lambda)=-\operatorname{Cov}(f(A),A)>0.
\]
For \(t\to\infty\), Taylor's formula with globally bounded second derivative of \((1+z)^{-1/2}\) on \(z\ge0\) yields
\[
f(A+t)=\frac{t^{-1/2}}{\sqrt K}
-\frac{A+\theta}{2\sqrt K}\,t^{-3/2}
+O\bigl((A+\theta)^2t^{-5/2}\bigr).
\]
Taking covariance with bounded \(f(A)\) cancels the leading age-independent term. The exponential age has every moment, so the integrated remainder is \(O(t^{-5/2})\), establishing (4), with \(\mu'(\lambda)=(\theta+1/(2\lambda))\mu(\lambda)-\sqrt{\theta/K}\).

5. **Positive spectral density.** Write
\[
f(s)=\frac1{\sqrt{\pi K}}\int_0^\infty u^{-1/2}e^{-(s+\theta)u}\,du.
\]
The elementary exponential-age covariance identity is
\[
\operatorname{Cov}(e^{-uA},e^{-vA})
=\frac{\lambda uv}{(\lambda+u+v)(\lambda+u)(\lambda+v)}.
\]
Substitute both integral representations into (1); Tonelli's theorem applies since the covariance kernel is nonnegative. Collecting the \(v\)-dependent factor gives (5) and the positive Laplace mixture. By dominated convergence as \(v\downarrow0\), the edge coefficient is
\[
\frac1{\pi K}\int_0^\infty\frac{\sqrt u\,e^{-\theta u}}{(\lambda+u)^2}\,du
=\frac{\mu'(\lambda)}{\sqrt{\pi K}},
\]
which proves (6). Differentiation under the positive Laplace integral gives strict complete monotonicity, and its square-root edge independently reproduces (4) by \(\Gamma(3/2)=\sqrt\pi/2\).

## Verification

Run `python verify.py` after installing the version specified by `requirements.txt`. The standalone script reconstructs the flow and stationary covariance by exponential-age quadrature; checks the critical complementary-error-function mean and its derivative; tests positivity and off-critical large-lag coefficients on both sides of the synchronized fixed point; verifies the strictly stationary constant exception; and integrates the independent two-layer positive spectral density to reproduce the direct covariance. In its recorded execution it passed **35 numerical checks**. These finite-precision calculations corroborate, but do not replace, the analytical inequalities, dominated limits, and covariance identities above.

## Relationship to prior work

Sarkar and Gupta (2022) established the global-reset Lorentzian Kuramoto dynamics, the Ott–Antonsen order-parameter flow, stationary one-point order-parameter densities and phase boundaries. Their formulas are prerequisites and are not claimed as new here. The present statement addresses the two-time stationary covariance, its critical spectral edge, and its exact all-phase decay exponents and amplitudes. Rose et al. (2018) supply general generator spectral-shift principles for resetting, without this nonlinear Kuramoto spectral density. Stojkoski et al. (2021) develop correlations for reset Brownian diffusion, not the Lorentzian Kuramoto order parameter. Das and Gupta (2018) address autocorrelations under continuous Gaussian forcing rather than whole-system Poisson reinitializations. The 2024 work of Majumder et al. studies *subsystem* resetting and therefore does not have the same complete-renewal process. These general frameworks motivate (1), but neither an exponential shift nor one-point densities alone specify the square-root edge coefficient (5)–(6). Priority against every broader spectral or renewal theorem is not established.

## Limitations

This is an exactly reduced thermodynamic-limit, Ott–Antonsen-manifold result. It does not establish a corresponding power law for finite oscillator populations, arbitrary initial phase distributions outside that manifold, Gaussian intrinsic frequencies, partial resets, or non-Poisson reset waiting times. The spectral representation concerns the scalar stationary order parameter, not the spectrum of the full microscopic oscillator generator. The source-to-claim comparison is a targeted literature comparison, not an independent priority certification.

## References

- M. Sarkar and S. Gupta, *Synchronization in the Kuramoto model in presence of stochastic resetting*, arXiv:2203.00339 (first submitted 2022-03-01), https://arxiv.org/abs/2203.00339.
- D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), https://arxiv.org/abs/1806.01298.
- V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686 (2021), https://arxiv.org/abs/2107.11686.
- D. Das and S. Gupta, *Exact correlations in the nonequilibrium stationary state of the noisy Kuramoto model*, arXiv:1806.09113 (2018), https://arxiv.org/abs/1806.09113.
- R. Majumder, R. Chattopadhyay and S. Gupta, *Kuramoto model subject to subsystem resetting: How resetting a part of the system may synchronize the whole of it*, arXiv:2402.14921 (2024), https://arxiv.org/abs/2402.14921.
