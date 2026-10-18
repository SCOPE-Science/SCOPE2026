# Strict fourth-cumulant signs and fast-flip laws in cooperative telegraph-driven networks

## Finding
Let a finite stable cooperative harmonic network be driven by independent symmetric run-and-tumble (telegraph) forces, with optional independent Gaussian thermal forcing. Every nonnegative linear displacement observable reached by at least one active force has **strictly negative stationary fourth cumulant at every finite positive switching rate**, even though *all its two-time covariances* coincide exactly with those of an appropriately covariance-matched Gaussian active Ornstein–Uhlenbeck drive. The magnitude of the fourth cumulant decreases strictly and is a completely monotone function of the switching rate. Its rapid-switching limit has a sharp inverse-cubic coefficient determined by the fourth power of the deterministic impulse response.

Precisely, under the assumptions below, for a nonnegative probe \(c\), put \(h_\ell(t)=c^\mathsf{T}e^{At}b_\ell\) for \(t\ge0\) and define \(K_4(c;\gamma)=\mathbb E[Y^4]-3(\mathbb E[Y^2])^2\), \(Y=c^\mathsf{T}X\), where \(X\) has its unique stationary law. Then
\[
K_4(c;\gamma)=-48\sum_{\ell=1}^m a_\ell^4\int_0^\infty\!dt\int_{[0,\infty)^3}\!du\,dv\,dw\,h_\ell(t)h_\ell(t+u)h_\ell(t+u+v)h_\ell(t+u+v+w)e^{-2\gamma(u+2v+w)}.
\]
If at least one response \(h_\ell\) is not identically zero, then \(K_4(c;\gamma)<0\) for every \(\gamma>0\). Further, \(-K_4(c;\gamma)\) is strictly completely monotone:
\[
(-1)^j\frac{d^j}{d\gamma^j}\big[-K_4(c;\gamma)\big]>0\qquad(j=0,1,2,\ldots;\ \gamma>0).
\]
Its two extreme-rate laws are
\[
\lim_{\gamma\downarrow0}K_4(c;\gamma)=-2\sum_\ell a_\ell^4\left(\int_0^\infty h_\ell(t)\,dt\right)^4,
\qquad
\lim_{\gamma\to\infty}\gamma^3 K_4(c;\gamma)=-3\sum_\ell a_\ell^4\int_0^\infty h_\ell(t)^4\,dt.
\]
Both coefficients are strictly negative under the stated reachability condition. For zero thermal forcing the stationary excess kurtosis additionally has the sharp law
\[
\frac{K_4(c;\gamma)}{\operatorname{Var}(Y)^2}
\sim -\frac{3}{\gamma}\frac{\sum_\ell a_\ell^4\int_0^\infty h_\ell(t)^4dt}
{\left[\sum_\ell a_\ell^2\int_0^\infty h_\ell(t)^2dt\right]^2}.
\]

A two-site pinned spring network provides an exact interior-site witness. With \(A=\left(\begin{smallmatrix}-2&1\\1&-2\end{smallmatrix}\right)\), \(b_1=(1,0)^\mathsf{T}\), \(a_1=1\), no thermal forcing and probe \(c=(0,1)^\mathsf{T}\), the impulse response is \(h(t)=\tfrac12(e^{-t}-e^{-3t})\) and
\[
\operatorname{Var}(Y)=\frac{\gamma+2}{6(2\gamma+1)(2\gamma+3)},
\]
\[
K_4(c;\gamma)=-\frac{8\gamma^4+116\gamma^3+646\gamma^2+1655\gamma+1400}{20(2\gamma+1)^2(2\gamma+3)^2(2\gamma+5)(2\gamma+7)(2\gamma+9)}.
\]
At \(\gamma=1\), \(\operatorname{Var}(Y)=1/30\), \(K_4=-17/13860\), and excess kurtosis equals \(-85/77\). In particular, an active drive on the first site leaves an exact non-Gaussian signature at the second site, notwithstanding identical two-time covariances under Gaussian colored forcing.

The nonnegative-observable assumption has a sharp boundary: with \(A=\operatorname{diag}(-1,-3)\), \(b=(1,1)^\mathsf{T}\), the **signed** probe \(c=(1,-3)^\mathsf{T}\), and \(\gamma=1/10\), the response changes sign and instead \(K_4=10825/918528>0\). Thus the universal sign theorem does not extend to arbitrary signed spatial probes.

## Assumptions and scope
Fix arbitrary positive integers \(n,m\). Let \(A\in\mathbb R^{n\times n}\) be Hurwitz (all eigenvalues have negative real part) and Metzler (all off-diagonal entries are nonnegative). Let \(b_\ell\in[0,\infty)^n\), \(a_\ell>0\), and a common flipping rate \(\gamma>0\). Let \(\sigma_1,\ldots,\sigma_m\) be mutually independent, stationary, symmetric two-state continuous-time Markov chains, each taking values \(\pm1\) and changing sign at rate \(\gamma\). Let \(W\) be a standard Brownian motion independent of all switches, and let \(B\) be any fixed real matrix of compatible size. The dynamics are
\[
dX_t=AX_t\,dt+\sum_{\ell=1}^m a_\ell b_\ell\sigma_\ell(t)\,dt+B\,dW_t.
\]
For the conclusions about sign, take any \(c\in[0,\infty)^n\) such that \(c^\mathsf{T}e^{At}b_\ell>0\) for at least one \(\ell\) and some \(t\ge0\). Irreducibly connected pinned overdamped spring chains with an active forcing at any site satisfy this for all coordinate probes. A zero response means the corresponding probe cannot detect that active force, and strictness is not asserted in that case. For the displayed excess-kurtosis asymptotic assume \(B=0\), or alternatively that the thermal contribution to that observable vanishes.

## Proof
**1. Stationary realization and positivity.** Exponential stability of \(A\) gives \(\|e^{At}\|\le Ce^{-\omega t}\) for some \(C,\omega>0\). Using a two-sided stationary realization of the independent drives, the unique stationary position is
\[
X_t=\sum_\ell a_\ell\int_0^\infty e^{As}b_\ell\sigma_\ell(t-s)\,ds+\int_{-\infty}^t e^{A(t-s)}B\,dW_s.
\]
The first integral converges absolutely, and the second in mean square. All polynomial moments exist. Exponential decay of initial differences proves uniqueness among finite-moment stationary solutions. Because \(A\) is Metzler, \(e^{At}\) is entrywise nonnegative (shift \(A\) by a sufficiently large scalar multiple of the identity and use the exponential power series). Therefore every \(h_\ell(t)=c^\mathsf{T}e^{At}b_\ell\) is nonnegative and exponentially decaying. Reachability yields strict positivity on a nonempty time interval. Symmetry gives \(\mathbb E Y=0\).

**2. Telegraph fourth joint cumulant.** For \(t_1\le t_2\le t_3\le t_4\), the Markov property and the two-point identity \(\mathbb E[\sigma(t)\sigma(s)]=e^{-2\gamma|t-s|}\) give
\[
\mathbb E[\sigma(t_1)\sigma(t_2)\sigma(t_3)\sigma(t_4)]
=e^{-2\gamma[(t_2-t_1)+(t_4-t_3)]}.
\]
Subtracting all three pair-products leaves exactly
\[
\operatorname{cum}_4(\sigma(t_1),\ldots,\sigma(t_4))
=-2e^{-2\gamma[(t_3-t_1)+(t_4-t_2)]}.
\]
The thermal Gaussian convolution is independent and has zero fourth cumulant. Independent active sources contribute additively. Integrating the joint cumulant against four response kernels, partitioning the nonnegative time orthant into its 24 ordered chambers, and substituting \(t=t_1\), \(u=t_2-t_1\), \(v=t_3-t_2\), \(w=t_4-t_3\) gives the displayed integral, including its exact prefactor \(-48\). Its integrand is nonnegative and is positive on a set of positive four-dimensional measure whenever an active source reaches the probe. This proves strict negativity.

**3. Complete monotonicity and limits.** Differentiating under the exponentially integrable integral gives
\[
(-1)^j\frac{d^j}{d\gamma^j}[-K_4]
=48\,2^j\sum_\ell a_\ell^4\int h_\ell(t)h_\ell(t+u)h_\ell(t+u+v)h_\ell(t+u+v+w)
(u+2v+w)^j e^{-2\gamma(u+2v+w)}\,dt\,du\,dv\,dw>0.
\]
At \(\gamma\downarrow0\), dominated convergence and symmetry of the fourfold product replace the ordered fourfold time integral by \(\tfrac1{24}(\int h_\ell)^4\), establishing the stated frozen-switch limit. At \(\gamma\to\infty\), substitute \(u=U/\gamma\), \(v=V/\gamma\), \(w=W/\gamma\). Exponential stability supplies an integrable dominating function, and the remaining gap integral is \(\int_{[0,\infty)^3}e^{-2(U+2V+W)}dU\,dV\,dW=1/16\). Thus the limiting coefficient is \(-48/16=-3\). For \(B=0\), applying the exponential covariance kernel as an approximate identity gives \(\gamma\operatorname{Var}(Y)\to\sum_\ell a_\ell^2\int h_\ell^2\); division yields the excess-kurtosis formula.

**4. Covariance-matched Gaussian driving.** Replace each \(\sigma_\ell\) independently by the stationary mean-zero Gaussian Ornstein–Uhlenbeck process solving \(d\zeta_\ell=-2\gamma\zeta_\ell\,dt+\sqrt{4\gamma}\,dV_\ell\), whose stationary variance is 1 and two-time covariance is \(e^{-2\gamma|t-s|}\). The stationary network position is then jointly Gaussian. The original and replacement drives have identical covariance kernels and are processed by the same linear network, so their full position two-time covariance matrices agree for every lag. Yet the Gaussian replacement has \(K_4=0\), while the telegraph response has \(K_4<0\).

**5. Exact two-site computations and sign boundary.** In the pinned two-site example, diagonalizing \(A\) yields \(h(t)=\tfrac12(e^{-t}-e^{-3t})\). The two-time covariance is integrated termwise to give the stated rational variance. For \(h(t)=\sum_j d_j e^{-\lambda_jt}\), each term of the ordered fourth-cumulant integral evaluates exactly to
\[
\frac{d_jd_kd_ld_p}{(\lambda_j+\lambda_k+\lambda_l+\lambda_p)
(\lambda_k+\lambda_l+\lambda_p+2\gamma)
(\lambda_l+\lambda_p+4\gamma)(\lambda_p+2\gamma)}.
\]
Summing the sixteen terms gives the displayed rational \(K_4\). In the signed-probe example the impulse response is \(h(t)=e^{-t}-3e^{-3t}\), and the same sixteen-term identity at \(\gamma=1/10\) gives \(10825/918528>0\). An independent polynomial-generator calculation confirms both examples.

## Verification
The standalone `CHECKER.py` requires Python 3 and SymPy. Run `python CHECKER.py`. It passed 26 symbolic or exact-rational assertions. In the two-site example it (i) symbolically simplifies the independent two-time and ordered four-time convolution integrals to the closed rational functions, (ii) computes the asymptotic coefficients, and (iii) independently solves the Markov-generator stationary moment equations to degree four at four rational switching rates. It also verifies the positive signed-probe boundary case independently using generator moments. The all-network strict-sign and complete-monotonicity statements follow from the mathematical integral proof, not finite numerical enumeration.

## Relationship to prior work
Sarkar, Santra and Basu (arXiv:2210.09035, first posted 17 October 2022) compare RTP and Gaussian Ornstein–Uhlenbeck reservoirs driving an **inertial** harmonic chain, establish the two-point covariance mechanism, and discuss bulk Gaussian limits and non-Gaussian boundary distributions. Here the claim is instead a **finite overdamped cooperative** network, a universal **strict fourth-cumulant sign on every nonnegative reachable probe**, its rate-complete monotonicity, an exact inverse-cubic coefficient, and an explicit signed-probe boundary. The earlier qualitative Gaussian/non-Gaussian distinction and covariance equivalence are not claimed as new. Singh and Kundu (arXiv:2012.13910) investigate two-point motion statistics for interacting active harmonic particles; Di Bello et al. (arXiv:2309.13424) compute kurtosis under a distinct Poisson-shot-noise bath. Pawula (Phys. Rev. A 35, 3102 (1987)) reports general output-moment methods for filtered dichotomous noise; the accessible abstract does not resolve whether a stronger general inequality subsumes any present statement.

## Limitations
The universal negative sign requires a nonnegative deterministic impulse response; the signed two-mode counterexample proves that this condition matters. The OU and RTP laws are **not** asserted to have identical higher moments or distributions, only identical two-time covariances after matching forcing parameters. The \(\gamma^{-3}\) coefficient concerns the *unnormalized* fourth cumulant; without thermal noise the excess kurtosis is typically of order \(\gamma^{-1}\). Fixed-dimensional stability is assumed; no uniform limit as network size tends to infinity is proved. The 1987 general-output-moment paper was accessible only by abstract, so its priority relationship is unresolved; independent scientific examination is not claimed.

## References
1. R. Sarkar, I. Santra, and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035, first public version 17 October 2022, https://arxiv.org/abs/2210.09035 ; full HTML https://arxiv.org/html/2210.09035v3 .
2. P. Singh and A. Kundu, *Crossover behaviours exhibited by fluctuations and correlations in a chain of active particles*, arXiv:2012.13910, https://arxiv.org/abs/2012.13910 .
3. C. Di Bello, R. Majumdar, R. Marathe, R. Metzler, and E. Roldán, *Brownian particle in a Poisson-shot-noise active bath: exact statistics, effective temperature, and inference*, arXiv:2309.13424, https://arxiv.org/abs/2309.13424 .
4. R. F. Pawula, *Dichotomous-noise-driven oscillators*, Physical Review A **35**, 3102–3108 (1987), https://doi.org/10.1103/PhysRevA.35.3102 .
