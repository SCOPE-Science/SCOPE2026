# A sharp class-L transition for a two-rate intermittently confined Brownian particle

## Finding

The stationary position of a Brownian particle intermittently subjected to a harmonic trap has an exact and **sharp self-decomposability phase boundary**. The position law is infinitely divisible for **every** positive parameter choice, but it is self-decomposable (class \(L\)) if and only if
\[
\boxed{\beta(4\mu+\alpha)\ge 4\mu^2.}
\]
Here \(\alpha\) is the on-to-off switching rate, \(\beta\) is the off-to-on rate, and \(\mu\) is the trapping relaxation rate. The boundary is independent of diffusivity \(D\).

This same inequality is necessary and sufficient for an ordinary linear Ornstein–Uhlenbeck process with independent-increment Lévy forcing to reproduce the **stationary one-time position marginal** of the intermittently trapped particle. Above and at the boundary, an explicit Brownian-plus-compound-Poisson driving bath realizes that marginal; below it, no Lévy bath can do so. No equality of temporal correlation functions or whole stochastic processes is asserted.

For equal on-to-off and off-to-on rates \(\alpha=\beta=\gamma\), the boundary becomes
\[
\boxed{\gamma\ge2(\sqrt2-1)\mu.}
\]
The strict and critical regimes therefore distinguish Lévy–Khintchine infinite divisibility from the strictly stronger Ornstein–Uhlenbeck stationary representability property.

## Assumptions and scope

Let \(D,\mu,\alpha,\beta\in(0,\infty)\). Let \(W_t\) be standard one-dimensional Brownian motion and \(S_t\in\{0,1\}\) an independent irreducible two-state continuous-time Markov chain. The state \(S=1\) (trap on) changes to \(S=0\) at rate \(\alpha\), while \(S=0\) changes to \(S=1\) at rate \(\beta\). The joint process obeys the Itô equation
\[
 dX_t=-\mu S_tX_t\,dt+\sqrt{2D}\,dW_t.
\]
The stationary chain has on/off probabilities \(\beta/(\alpha+\beta)\) and \(\alpha/(\alpha+\beta)\). These assumptions exclude zero switching rates, state-dependent diffusivities, inertial motion, and non-harmonic confinement.

Define
\[
 a=\frac{\alpha}{2\mu},\qquad c=\sqrt{\frac\beta D},\qquad d=\sqrt{\frac{\alpha+\beta}{D}},\qquad \sigma^2=\frac D\mu.
\]
Thus \(a>0\) and \(0<c<d\). The joint stationary distribution exists uniquely: on a two-sided stationary switching path, the stochastic convolution
\[
 X_0=\sqrt{2D}\int_{-\infty}^0
 \exp\!\left(-\mu\int_s^0 S_u\,du\right)dW_s
\]
converges in mean square after averaging over the chain. For example, the expected squared kernel is a positive combination of exponentially decaying functions, because the chain spends a positive stationary fraction of time in its on state. Solutions driven by a shared noise/chain path contract almost surely, establishing uniqueness of the stationary joint law.

## Proof

**1. Exact stationary transform.** Let \(f_1(k)=\mathbb E[e^{ikX}\mathbf1_{\{S=1\}}]\), and similarly \(f_0(k)\), under stationarity. The stationary forward equations, transformed in space, read
\[
 \begin{aligned}
 0&=-\mu kf_1'(k)-Dk^2f_1(k)-\alpha f_1(k)+\beta f_0(k),\\
 0&=-Dk^2f_0(k)+\alpha f_1(k)-\beta f_0(k).
 \end{aligned}
\]
The second equation gives \(f_0(k)=\alpha f_1(k)/(\beta+Dk^2)\). The first then integrates, using \(f_1(0)=\beta/(\alpha+\beta)\), to
\[
 f_1(k)=\frac\beta{\alpha+\beta}
 e^{-Dk^2/(2\mu)}\left(1+\frac{Dk^2}\beta\right)^{-a}.
\]
Adding both states gives the exact characteristic function
\[
 \boxed{\phi(k)=e^{-\sigma^2 k^2/2}
 \left(1+\frac{k^2}{c^2}\right)^{-(a+1)}
 \left(1+\frac{k^2}{d^2}\right).}
\]
The equal-switching restriction was obtained in Santra--Das--Nath (2021). More importantly, the general zero-drift/two-rate stationary transform is already contained in Zhang--Wang (2017), Theorem 2.1(ii), on relabelling the switching states and diffusion normalization. Accordingly, **this Fourier transform is not claimed as new**; it is recalled and independently derived solely to fix normalization and make the class-\(L\) comparison exact.

**2. Infinite divisibility for all rates.** The elementary Fourier integral identity
\[
 \int_{\mathbb R}\frac{\cos(kx)-1}{|x|}e^{-u|x|}\,dx
 =-\log\left(1+\frac{k^2}{u^2}\right),\quad u>0,
\]
shows that \(\phi\) has a Lévy–Khintchine exponent with Gaussian variance \(\sigma^2\), zero drift, and Lévy density
\[
 \boxed{\nu(x)=\frac{h(|x|)}{|x|},\qquad
 h(r)=(a+1)e^{-cr}-e^{-dr}.}
\]
Since \(d>c\), \(h(r)>a e^{-cr}>0\) for every \(r>0\). The density satisfies \(\int_{\mathbb R}\min(1,x^2)\nu(x)\,dx<\infty\). Hence the unique stationary position marginal is infinitely divisible at every allowed parameter value.

**3. Sharp class-\(L\) boundary.** By the classical one-dimensional canonical Lévy-density criterion (Sato), a symmetric infinitely divisible distribution with this continuous density is self-decomposable if and only if its canonical profile \(h(r)\) is nonincreasing for all \(r>0\). Direct differentiation yields
\[
 h'(r)=-(a+1)c\,e^{-cr}+d\,e^{-dr}.
\]
Because \(d>c\), the inequality \(h'(r)\le0\) for **all** \(r>0\) is equivalent to \((a+1)c\ge d\); indeed \(h'(r)e^{cr}=d e^{-(d-c)r}-(a+1)c\) is strictly decreasing. If the inequality fails, \(h'(r)>0\) on a nonempty interval adjacent to zero. Substituting the definitions and squaring nonnegative quantities gives
\[
 (a+1)c\ge d
 \quad\Longleftrightarrow\quad
 \left(1+\frac\alpha{2\mu}\right)^2\beta\ge\alpha+\beta
 \quad\Longleftrightarrow\quad
 \boxed{\beta(4\mu+\alpha)\ge4\mu^2.}
\]
The equality case is included. Setting \(\alpha=\beta=\gamma\) and solving the resulting quadratic proves the stated universal equal-rate threshold.

**4. Explicit Lévy-bath equivalence and its obstruction.** Suppose the boundary inequality holds. Define the even function
\[
 q(x)=(a+1)c\,e^{-c|x|}-d\,e^{-d|x|}=-h'(|x|),\qquad x\ne0.
\]
The previous monotonicity argument gives \(q(x)\ge0\). Moreover
\[
 \int_{\mathbb R}q(x)\,dx=2a=\frac\alpha\mu.
\]
Let \(L\) be the sum of a centered Brownian Lévy process with variance rate \(2\sigma^2\), and an independent symmetric compound-Poisson process with total intensity \(\alpha/\mu\) and jump density \(q(x)/(2a)\). Define the ordinary linear Ornstein–Uhlenbeck process
\[
 dY_t=-Y_t\,dt+dL_t.
\]
The driving exponent is
\[
 \chi(k)=-\sigma^2 k^2
 -\frac{2(a+1)k^2}{c^2+k^2}
 +\frac{2k^2}{d^2+k^2}
 =k\frac{d}{dk}\log\phi(k).
\]
Its stationary Fourier logarithm is \(\int_0^\infty\chi(e^{-t}k)dt=\log\phi(k)\), by integrating the displayed derivative from \(k\) down to zero. Thus the Lévy-driven OU stationary marginal equals that of \(X\).

Conversely, any stationary one-dimensional OU process driven by independent Lévy noise has a self-decomposable marginal. Below the boundary the monotonicity test has failed, so **no** such driving noise can reproduce the stationary one-time law. This is a statement about exactly matched stationary marginals, not replacement of the switched dynamics at all times.

## Verification

Run `python verify.py` in the directory containing the standalone reproducibility script. The program checks eight even-moment orders for five independent positive rational parameter quadruples, comparing the Fourier series coefficients against moment recurrences obtained directly from the two-state Markov generator. It independently integrates the Lévy density and background-driving characteristic exponent for four physical parameter sets, tests both sides and equality of the class-\(L\) boundary, and checks recovery of the published equal-switching Fourier formula. The current run passed 112 assertions. All such computations are finite checks supporting, not replacing, the global proof.

## Relationship to prior work

Santra, Das and Nath (2021, arXiv:2104.00609, §§2--4) introduce the intermittently switched harmonic trap and calculate the stationary transform for equal switching rates, investigating distribution shapes and first-passage behavior. Their §4 mentions unequal switching rates in a singular strong-trapping limit, not the class-\(L\) boundary.

Zhang and Wang (2017, Theorem 2.1(ii), pp. 4787--4789) already supply the general stationary Fourier transform for the two-state linear switching diffusion with one zero drift. **The exact transform is fully covered by that paper**, and its derivation is not presented as an original contribution here. The new scientific claim is narrowly the sharp *self-decomposability / Lévy-driven OU representability classification* and its explicit positive background jump law across all switching rates. The classical one-dimensional class-\(L\) criterion is also prior mathematical knowledge, and the present parameter threshold follows by applying it to the known stationary transform. The contribution is a concrete, parameter-complete classification for the physical switching model, not a new abstract characterization of self-decomposability.

The variance-gamma review of Fischer, Gaunt and Sarantsev (2023 preprint; 2024 publication) discusses the canonical exponential Lévy profile and self-decomposability. A published Gaussian-compound-Poisson perturbation study applies the same general criterion in a different distribution family. It does not establish the present two-rate on/off trap inequality or OU driving law.

## Limitations

The claim is an elementary but physically motivated application of a classical class-\(L\) criterion to a previously known Fourier transform; its mathematical priority is subject to unlocated equivalent classifications in Markov-modulated OU or probability-distribution literature. It is limited to an on/off *linear* trap, equal Brownian diffusivity in both states, exponential switching, and stationary position marginals. The driving bath constructed here is not claimed to reproduce the joint or temporal law. The numerical checker is not a formal theorem prover and makes no infinite-parameter certification claim.

## References

1. I. Santra, S. Das and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (first public 1 April 2021), J. Phys. A 54 (2021) 334001. https://arxiv.org/abs/2104.00609
2. Z. Zhang and W. Wang, *The stationary distribution of Ornstein–Uhlenbeck process with a two-state Markov switching*, Communications in Statistics — Simulation and Computation 46 (2017), 4783–4794. First public accepted author version 20 January 2016. https://doi.org/10.1080/03610918.2015.1132321
3. K.-I. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press (1999), classical one-dimensional self-decomposability criterion.
4. A. Fischer, R. E. Gaunt and A. Sarantsev, *The Variance-Gamma Distribution: A Review*, arXiv:2303.05615 (2023), Statistical Science 39 (2024), 435–458. https://arxiv.org/abs/2303.05615
