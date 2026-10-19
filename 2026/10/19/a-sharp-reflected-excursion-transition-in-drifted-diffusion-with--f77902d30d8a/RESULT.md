# A sharp reflected-excursion transition in drifted diffusion with sign-reversing proportional resetting

## Finding
For a one-dimensional particle with drift \(\mu>0\), diffusivity \(D>0\), rate-\(r>0\) Poisson resetting and position update \(x\mapsto-bx\) with \(0<b<1\), the stationary density exhibits a sharp left-tail phase transition. Put
\[
\lambda_+=\frac{\sqrt{\mu^2+4Dr}-\mu}{2D},\qquad
\lambda_-=\frac{\sqrt{\mu^2+4Dr}+\mu}{2D},\qquad
b_c=\frac{\lambda_+}{\lambda_-}.
\]
There are finite strictly positive constants \(C_+,C_0,C_c,C_1\), specified below, such that as \(t\to\infty\),
\[
 f(t)\sim C_+e^{-\lambda_+t},\qquad
 f(-t)\sim
 \begin{cases}
 C_0e^{-\lambda_-t},&0<b<b_c,\\
 C_c\,t e^{-\lambda_-t},&b=b_c,\\
 C_1e^{-(\lambda_+/b)t},&b_c<b<1.
 \end{cases}
\]
In particular the logarithmic decay rate of the tail opposing the drift changes from \(\lambda_-\) to \(\lambda_+/b\). Exactly at the boundary, two independent slow negative exponential components coincide and produce a linear prefactor. The stationary moment-generating function is finite **exactly** for
\[
 -\min\{\lambda_-,\lambda_+/b\}<s<\lambda_+.
\]
For example, \(\mu=2,D=1,r=3\) gives \(\lambda_+=1\), \(\lambda_-=3\), and \(b_c=1/3\): the left density decays like \(e^{-3t}\) for \(b=1/4\), like \(t e^{-3t}\) at \(b=1/3\), and like \(e^{-2t}\) for \(b=1/2\), with strictly positive finite coefficients.

## Assumptions and scope
Between independent Poisson reset times of rate \(r\), let the position solve \(dX_t=\mu\,dt+\sqrt{2D}\,dB_t\), with \(\mu,D,r>0\). At a reset replace \(X_{t-}\) by \(-bX_{t-}\), \(0<b<1\). Brownian increments and reset times are independent. All statements concern the unique invariant probability measure on the entire real line and its Lebesgue density \(f\). The exponent \(\lambda_+\) is associated with a positive Brownian excursion between resets and \(\lambda_-\) with a negative one; \(0<b_c<1\) follows from \(\mu>0\).

Define independent \(U_j\sim\operatorname{Exp}(\lambda_+)\) and \(V_j\sim\operatorname{Exp}(\lambda_-)\) for all integers \(j\ge0\), with all \(U_j,V_j\) mutually independent. Set \(Z_j=U_j-V_j\), and define the almost-surely absolutely convergent series
\[
 X_\infty=\sum_{j=0}^{\infty}(-b)^jZ_j.
\]
The stationary density of the physical process equals the law of \(X_\infty\). Introduce
\[
 H(s)=\frac{\lambda_+\lambda_-}{(\lambda_+-s)(\lambda_-+s)},\qquad \Sigma=\lambda_++\lambda_-.
\]
The strictly positive constants in the finding can be written as the following absolutely convergent products (each product is evaluated only at an argument where its factors are finite):
\[
 C_+=\frac{\lambda_+\lambda_-}{\Sigma}\prod_{j=1}^{\infty}H\big(\lambda_+(-b)^j\big),
\]
\[
 C_0=\frac{\lambda_+\lambda_-}{\Sigma}\prod_{j=1}^{\infty}H\big(-\lambda_-(-b)^j\big)\quad(0<b<b_c),
\]
\[
 C_1=\frac{\lambda_+\lambda_-}{b\Sigma}\prod_{\substack{j\ge0\\j\ne1}}H\big(-\tfrac{\lambda_+}{b}(-b)^j\big)\quad(b_c<b<1),
\]
\[
 C_c=\frac{\lambda_+\lambda_-^3}{\Sigma^2}\prod_{j=2}^{\infty}H\big(-\lambda_-(-b)^j\big)\quad(b=b_c).
\]

## Proof
**1. Stationary series and innovation law.** Let \(T\sim\operatorname{Exp}(r)\) be independent of standard Brownian motion. A Brownian segment between independent resetting times has displacement \(Z=\mu T+\sqrt{2D}B_T\), with moment-generating function
\[
 \mathbb E[e^{sZ}]=\frac{r}{r-\mu s-Ds^2}=H(s),\qquad -\lambda_-<s<\lambda_+.
\]
Because \(r=D\lambda_+\lambda_-\), the right-hand side factors into the moment-generating functions of independent \(\operatorname{Exp}(\lambda_+)\) and the negative of \(\operatorname{Exp}(\lambda_-)\), proving \(Z\overset d=U-V\). Looking backward from a stationary observation time through an independent two-sided Poisson process, each earlier displacement acquires one additional factor \(-b\), yielding the stated series. Absolute convergence follows from \(\sum_{j\ge0}b^j\mathbb E|Z_j|<\infty\). For two trajectories driven by the same noise and resets, their difference at time \(t\) is \((-b)^{N_t}\) times the initial difference, and \(N_t\to\infty\) almost surely. This coupling establishes uniqueness and convergence to the series law. The \(j=0\) innovation has a strictly positive continuous asymmetric-Laplace density, so convolution with the independent remainder gives a strictly positive continuous stationary density.

**2. Exact moment-generating-function domain.** Independence and convergence, with uniform integrability on every compact subinterval of the finite exponential-moment domain, imply
\[
 M(s)=\mathbb E[e^{sX_\infty}]=\prod_{j=0}^\infty H\big((-b)^js\big).
\]
For \(s\) inside the claimed interval, the factors are finite and positive, and \(H(w)=1+O(w)\) as \(w\to0\), making the product convergent and finite. Each independent summand \((-b)^jU_j\) or \(-(-b)^jV_j\) is an exponential of one sign with explicit rate. The slowest positive component is \(U_0\), with rate \(\lambda_+\). The two candidates for the slowest negative component are \(-V_0\), of rate \(\lambda_-\), and \(-bU_1\), of rate \(\lambda_+/b\); every other negative component has strictly larger rate. If the exponential parameter exits the specified domain, at least one independent component has an infinite exponential moment. The independent remainder assigns strictly positive probability to a bounded interval, so no cancellation can restore finiteness. Thus the domain is exact.

**3. Elementary convolution tail lemma.** If \(E\sim\operatorname{Exp}(\kappa)\) is independent of \(R\) and \(\mathbb E[e^{-\kappa R}]<\infty\), the density of \(R-E\) satisfies
\[
 f_{R-E}(-t)=\kappa e^{-\kappa t}\mathbb E[e^{-\kappa R}{\bf1}_{\{R\ge-t\}}]\sim\kappa e^{-\kappa t}\mathbb E[e^{-\kappa R}].
\]
Similarly, if \(\mathbb E[e^{\kappa R}]<\infty\), then
\[
 f_{R+E}(t)=\kappa e^{-\kappa t}\mathbb E[e^{\kappa R}{\bf1}_{\{R\le t\}}]\sim\kappa e^{-\kappa t}\mathbb E[e^{\kappa R}].
\]
Both limits are direct consequences of monotone convergence. For two independent identical negative exponentials, \(G=E_1+E_2\sim\operatorname{Gamma}(2,\kappa)\). If the moment-generating function of \(R\) is finite in an open neighborhood of \(-\kappa\), then
\[
 f_{R-G}(-t)=\kappa^2e^{-\kappa t}\mathbb E[(t+R)e^{-\kappa R}{\bf1}_{\{R\ge-t\}}]
 \sim\kappa^2 t e^{-\kappa t}\mathbb E[e^{-\kappa R}].
\]
Indeed the integrand after division by \(t\) is dominated by \((1+|R|)e^{-\kappa R}\), which is integrable under the neighborhood hypothesis; the indicator also forces \(t+R\ge0\).

**4. Apply the tail lemma in all three regimes.** For the right tail, isolate \(U_0\), setting \(R_+=X_\infty-U_0\). Every component of \(R_+\) has a strictly faster positive exponential rate than \(\lambda_+\); hence \(\mathbb E[e^{\lambda_+R_+}]<\infty\), giving \(C_+=\lambda_+\mathbb E[e^{\lambda_+R_+}]\). In the first left regime, isolate \(-V_0\) and use \(R_0=X_\infty+V_0\); every remaining negative rate exceeds \(\lambda_-\), giving \(C_0=\lambda_-\mathbb E[e^{-\lambda_-R_0}]\). In the third regime, isolate \(-bU_1\) and use \(R_1=X_\infty+bU_1\); its negative rate is \(\lambda_+/b\), strictly below all other negative rates, giving \(C_1=(\lambda_+/b)\mathbb E[e^{-(\lambda_+/b)R_1}]\). At \(b=b_c\), the two independent negative components \(-V_0\) and \(-bU_1\) have common rate \(\lambda_-\); isolate both and put \(R_c=X_\infty+V_0+bU_1\). All remaining negative rates strictly exceed \(\lambda_-\), so the gamma-tail lemma applies and gives \(C_c=\lambda_-^2\mathbb E[e^{-\lambda_-R_c}]\). In each case, the requisite exponential moments are finite by geometric decay of later summand scales. Evaluation of the independent exponential moments of the omitted companion variables \(-V_0\), \(U_0\), and \(bV_1\) gives the explicit product formulas above. All coefficients are strictly positive, and this completes the proof.

## Verification
Run `python verify.py` with Python and SymPy installed. The program checks stationary moment recurrences through order twelve for four rational sign-reversal factors, and checks rational Laplace-transform pole coefficients against independently factored exponential components for four truncation depths. It reports 96 successful exact assertions. These finite symbolic checks corroborate normalizations and rates; the proof of the infinite-series asymptotics is analytic and does not rely on finite truncation. The stationary raw moments additionally satisfy
\[
 r(1-(-b)^n)\mathbb E[X_\infty^n]=n\mu\mathbb E[X_\infty^{n-1}]+n(n-1)D\mathbb E[X_\infty^{n-2}],\quad n\ge1,
\]
with the last term zero when \(n=1\).

## Relationship to prior work
Pierce, *An advection-diffusion process with proportional resetting* (arXiv:2204.07215v1, 2022), studies drift and Brownian noise with **positive** proportional resetting \(0<\varepsilon<1\), including a stationary distribution and exact moments. Tal-Friedman, Roichman, and Reuveni, *Diffusion with Partial Resetting* (arXiv:2205.03363v1, 2022), establish an infinite-product stationary law for positive contraction. Biroli, Feld, Hartmann, Majumdar, and Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension* (arXiv:2406.08387v1, 2024), allow sign-reversing rescalings for **zero-drift** diffusion. These works supply the motivating proportional-resetting and series frameworks. The finding here is the sharp rare-left-excursion competition arising only when **both** positive drift and negative rescaling act, including its exact critical linear prefactor and strict positive coefficients. It does not claim that exponential innovations, proportional-reset stationary expansions, or elementary exponential convolution tails are new.

## Limitations
The theorem assumes one-dimensional constant positive drift, strictly positive Brownian diffusivity, homogeneous independent Poisson resetting, and a deterministic strictly contractive sign-reversing multiplier. At zero drift the distinct positive and negative innovation rates coincide and the proposed threshold \(b_c\) lies at the excluded boundary \(b=1\); the classification must not be extrapolated to that case. At zero diffusivity or random/non-Poisson resetting the innovation decomposition changes. The theorem concerns stationary one-point density extremes, not finite-time exit probabilities or multidimensional statistics. A broad pre-existing general theorem for signed affine perpetuities may imply parts of the classification; independent literature priority validation has not been performed.

## References
1. J. Kevin Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1 (public 14 April 2022), https://arxiv.org/abs/2204.07215v1.
2. O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v1 (2022), https://arxiv.org/abs/2205.03363v1.
3. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (2024), https://arxiv.org/abs/2406.08387v1.
