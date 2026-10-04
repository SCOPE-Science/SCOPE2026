# Additive Brownian forcing breaks positivity in the stochastic syphilis model
## Finding
Consider Eq. (24) of Khan, Khan, and Alqarni (2026), whose twelve displayed compartment equations have additive diffusion terms \(\sigma_i\,dB_i(t)\). Assume the Brownian coordinates \(B_1,\ldots,B_{12}\) are independent standard Brownian motions, as in the article's stochastic setup, and put
\[
\sigma_\Sigma^2=\sum_{i=1}^{12}\sigma_i^2>0.
\]
For every strictly positive initial state and every \(t>0\), the solution of the displayed SDE cannot remain in the strictly positive orthant through time \(t\) with probability one. More quantitatively, let \(\tau_+\) denote the first time at which at least one compartment ceases to be strictly positive. Then
\[
\mathbb P(\tau_+\le t)\ge
\Phi\!\left(-\frac{m_t}{\sqrt{v_t}}\right)>0,
\]
where \(\Phi\) is the standard normal distribution function,
\[
m_t=T_0e^{-\mu t}+\frac{\Pi}{\mu}(1-e^{-\mu t}),
\qquad
v_t=\frac{\sigma_\Sigma^2}{2\mu}(1-e^{-2\mu t}),
\]
\(T_0\) is the sum of the twelve initial coordinates, and \(\Pi=\pi_m+\pi_f\). Therefore the source's Theorem 1, which asserts a unique global positive solution for Eq. (24), is incompatible with the equation as printed whenever \(\sigma_\Sigma>0\).

The mismatch is structural rather than a numerical edge case. In the later proof material, diffusion contributions are written with state factors such as \(\sigma_iX_i\), and a total-population Itô calculation uses \(\sum_i\sigma_iX_i\,dB_i\). Those terms belong to a multiplicative-noise model, not to Eq. (24)'s additive-noise model.

## Assumptions and scope
The claim concerns exactly the twelve-equation stochastic system printed as Eq. (24), not a repaired multiplicative, reflected, truncated, or otherwise constrained model. All epidemiological rate parameters are taken nonnegative with \(\mu>0\), and the initial twelve coordinates are strictly positive. The Brownian coordinates are independent standard Brownian motions. The argument only needs \(\sigma_\Sigma>0\), so it applies if even one displayed additive noise intensity is nonzero.

The quantity \(T\) below is defined as the sum of all twelve coordinates appearing in Eq. (24). This avoids relying on any separate interpretation of the article's symbol \(N\) in the incidence denominators. The incidence terms cancel in the sum regardless of that interpretation.

## Proof
Write
\[
T=S_m+I_{mp}+I_{ms}+L_m+R_m+S_f+I_{fp}+I_{fs}+L_f+R_f+C+D.
\]
Summing the twelve drift equations in Eq. (24) cancels every transfer between displayed compartments: infection, stage progression, treatment, loss of immunity, congenital transfer, and the disease-death transfers into \(D\). The prevention terms on infected female compartments also cancel against their displayed transfers to \(R_f\) and \(C\). What remains is
\[
dT=(\Pi-\mu T-\pi_pS_f)dt+\sum_{i=1}^{12}\sigma_i\,dB_i(t),
\qquad \Pi=\pi_m+\pi_f.
\]
Because the Brownian coordinates are independent,
\[
W(t)=\sigma_\Sigma^{-1}\sum_{i=1}^{12}\sigma_iB_i(t)
\]
is a standard Brownian motion. Let \(Y\) solve the scalar Ornstein--Uhlenbeck equation
\[
dY=(\Pi-\mu Y)dt+\sigma_\Sigma\,dW(t),
\qquad Y(0)=T_0.
\]
Variation of constants gives the exact pathwise identity, for as long as the displayed compartment solution is defined,
\[
T(t)-Y(t)=-\pi_p e^{-\mu t}\int_0^t e^{\mu s}S_f(s)\,ds.
\]
On any sample path that remains in the nonnegative orthant through time \(t\), one has \(S_f(s)\ge0\) and \(T(t)\ge0\). Hence on that event
\[
0\le T(t)\le Y(t).
\]
Therefore the event \(\{Y(t)<0\}\) is disjoint from the event that all twelve compartments stay nonnegative through time \(t\). The Gaussian variable \(Y(t)\) has mean and variance
\[
m_t=T_0e^{-\mu t}+\frac{\Pi}{\mu}(1-e^{-\mu t}),
\qquad
v_t=\frac{\sigma_\Sigma^2}{2\mu}(1-e^{-2\mu t}).
\]
For every \(t>0\), \(v_t>0\), so
\[
\mathbb P(Y(t)<0)=\Phi\!\left(-\frac{m_t}{\sqrt{v_t}}\right)>0.
\]
This proves the stated lower bound for failure of strict positive-orthant invariance and contradicts an almost-sure global positivity assertion for the additive system.

The same source later writes, in its positivity/stability calculations, quadratic-variation terms proportional to \(\sigma_i^2X_i^2\) and a stochastic total-population term proportional to \(\sum_i\sigma_iX_i\,dB_i\). Those expressions are the Itô terms for multiplicative diffusion \(\sigma_iX_i\,dB_i\), not for the additive diffusion \(\sigma_i\,dB_i\) displayed in Eq. (24). A later extinction theorem likewise explicitly assumes multiplicative noise in \(I_{fp}\). Thus the published proof machinery changes the diffusion structure instead of proving positivity for Eq. (24).

## Verification
The proof is analytic and does not infer an infinite-time assertion from simulation. The accompanying checker reconstructs the transfer cancellations in the twelve displayed drifts and verifies that their sum leaves precisely recruitment, natural loss, the unmatched susceptible-female prevention loss, and the twelve additive noise terms. It also checks a representative positive-parameter Gaussian lower bound numerically from the closed formula.

The critical logical boundary is explicit: the result refutes strict positive-orthant invariance for the additive SDE as printed. It does not analyze a multiplicative-noise repair, a reflected SDE, or the validity of every downstream threshold claim after such a repair.

## Relationship to prior work
The motivating article states that Eq. (24) is obtained by adding white noise to every compartment and then asserts a unique global positive solution. Its own later formulas use state-dependent diffusion factors, creating the model/proof mismatch identified here.

A closely related SIS construction by Cai, Cai, and Mao (2019), cited by the motivating article, uses diffusion coefficients containing the infected population itself, such as \(I(t)(N-I(t))\) and \(I(t)\sqrt{N-I(t)}\). Those coefficients vanish at the biologically relevant boundary and support a genuine positive-invariance argument under stated conditions. That model therefore does not cover the present additive-noise system; rather, it illustrates why boundary-compatible diffusion matters.

Exact-title, DOI, additive-noise, positive-orthant, Ornstein--Uhlenbeck comparison, and source-specific correction searches located no published correction giving the quantitative bound above. Related general stochastic-epidemic literature establishes positivity for different, state-dependent diffusion structures, not for the displayed twelve-dimensional additive system.

## Limitations
The observation that unconstrained additive Brownian forcing is generally incompatible with strict positivity is standard SDE intuition; the contribution here is the source-specific exact summation, quantitative Gaussian lower bound, and identification of the diffusion change inside the article's own proofs. No claim is made that a suitably reformulated stochastic syphilis model cannot be biologically well posed.

The earliest public date verified for the motivating article is its publisher date, 2 September 2026. Exact-title and DOI searches did not locate an earlier public preprint, but absence from those searches is not a proof that no earlier private or unindexed version existed.

## References
1. A. Khan, I. Khan, and A. J. Alqarni, “Stochastic dynamics of a syphilis epidemic model with perturbation: Stationary distribution and extinction thresholds,” *AIMS Mathematics* 11(9) (2026), 27890–27920. DOI: 10.3934/math.20261114.
2. S. Cai, Y. Cai, and X. Mao, “A stochastic differential equation SIS epidemic model with two independent Brownian motions,” *Journal of Mathematical Analysis and Applications* 474(2) (2019), 1536–1550. DOI: 10.1016/j.jmaa.2019.02.039.
