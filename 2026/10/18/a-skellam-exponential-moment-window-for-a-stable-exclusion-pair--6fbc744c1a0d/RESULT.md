# A Skellam exponential-moment window for a stable exclusion pair

## Finding
For a stable pair of heterogeneous nearest-neighbor exclusion walkers on \(\mathbb Z\), a tagged coordinate has the *local scaled cumulant generating function* of a free bilateral Poisson walk, although its finite-time law is generally not Skellam. This statement also gives an explicit strictly positive multiplicative boundary factor in the moment-generating asymptotic and a local large-deviation rate. The established law of large numbers and Gaussian central limit theorem for the same two-particle process are not part of the claimed contribution.

Fix positive left/right jump rates \(a_1,b_1,a_2,b_2\) satisfying \(\beta:=a_1+b_2<\delta:=b_1+a_2\). The two particles start at ordered integer sites; set \(h_0=X_2(0)-X_1(0)-1\in\mathbb Z_{\ge0}\). Their attempted jumps into occupied sites are suppressed. Write
\[
 r_+=\frac{b_1b_2}{\delta},\qquad r_-=\frac{a_1a_2}{\delta},\qquad
 \Lambda(\theta)=r_+(e^\theta-1)+r_-(e^{-\theta}-1).
\]
For a real tilt \(\theta\), put \(B_\theta=a_1e^{-\theta}+b_2\), \(C_\theta=b_1e^\theta+a_2\), \(\beta_\theta=B_\theta C_\theta/\delta\), and \(u_\theta=\log(C_\theta/\delta)\). On the explicit open interval
\[
 I=\{\theta\in\mathbb R:\ \beta_\theta<\delta,\ B_\theta<\delta\},
\]
which contains zero, the exact asymptotic is
\[
\boxed{\quad
 \mathbb E\exp\{\theta[X_1(t)-X_1(0)]\}
 =e^{t\Lambda(\theta)}\left[e^{u_\theta h_0}
 \frac{\delta-\beta_\theta}{\delta-B_\theta}+o(1)\right]
 \quad(t\to\infty).\quad}
\]
Here \(o(1)\) is for each fixed real \(\theta\in I\). The bracketed leading constant is finite and positive, and equals one at \(\theta=0\). In particular,
\[
\lim_{t\to\infty}t^{-1}\log\mathbb E e^{\theta[X_1(t)-X_1(0)]}=\Lambda(\theta)
\quad(\theta\in I).
\]
This is a *local* cumulant-generating identity; it makes no assertion about tilts outside \(I\).

For \(x\in\Lambda'(I)\), define
\[
 q(x)=\sqrt{x^2+4r_+r_-},\qquad
 \mathcal J(x)=r_++r_--q(x)+x\log\left(\frac{x+q(x)}{2r_+}\right).
\]
Then the first particle has the exact local large-deviation exponent
\[
\boxed{\quad
\lim_{\varepsilon\downarrow0}\liminf_{t\to\infty}\frac1t
 \log\Pr\left(\left|\frac{X_1(t)-X_1(0)}t-x\right|<\varepsilon\right)
=\lim_{\varepsilon\downarrow0}\limsup_{t\to\infty}\frac1t
 \log\Pr\left(\left|\frac{X_1(t)-X_1(0)}t-x\right|<\varepsilon\right)
=-\mathcal J(x).\quad}
\]
No global large-deviation principle, exact Skellam distribution, or result for unstable clouds is asserted.

## Assumptions and scope
Particles are labeled from left to right, with positive finite attempted jump rates \(a_i\) left and \(b_i\) right, suppression of attempted collisions, and any deterministic finite initial gap \(h_0\). All limits hold as continuous time \(t\to\infty\), at fixed jump rates and fixed tilt or speed. The stability inequality \(\beta<\delta\) is strict. The result is a probability theorem of primary classification MSC2020 60K35.

## Proof
**1. A marked birth–death representation.** Let \(H_t=X_2(t)-X_1(t)-1\). From every state \(h\ge0\), births \(h\to h+1\) occur through the left particle moving left at rate \(a_1\) (tagged displacement \(-1\)), or the right particle moving right at rate \(b_2\) (tagged displacement \(0\)). From \(h>0\), deaths \(h\to h-1\) occur through the left particle moving right at rate \(b_1\) (tagged displacement \(+1\)), or the right particle moving left at rate \(a_2\) (tagged displacement \(0\)). Thus \(H\) has birth rate \(\beta\), death rate \(\delta\) on positive states, and no death at zero.

**2. An exact exponential eigenfunction.** For \(\theta\in\mathbb R\) put \(u=u_\theta\), and let \(f(x,h)=e^{\theta x+uh}\). The two birth transitions contribute \(a_1(e^{-\theta+u}-1)+b_2(e^u-1)=\beta_\theta-\beta=\Lambda(\theta)\). At positive gaps the two extra death transitions contribute
\[
 b_1(e^{\theta-u}-1)+a_2(e^{-u}-1)
 =e^{-u}(b_1e^\theta+a_2)-\delta=0.
\]
Therefore the full Markov generator satisfies \(Lf=\Lambda(\theta)f\) at *every* gap, including zero. All original jump intensities are uniformly bounded; on each finite time interval the total jump count is dominated by a finite-rate Poisson count. Consequently exponential jump functionals are integrable and
\[
 M_t=\exp\{\theta[X_1(t)-X_1(0)]+u[H_t-h_0]-t\Lambda(\theta)\}
\]
is a true mean-one martingale for every fixed real \(\theta\). This is an exact finite-time statement.

**3. The tilted process and the boundary factor.** Change measure up to time \(t\) by \(M_t\). The resulting consistent law \(\Pr_\theta\) multiplies each original transition rate by its exponential jump weight. Under \(\Pr_\theta\), the gap is again an M/M/1 birth–death chain, now with birth rate \(\beta_\theta\) and death rate \(\delta\): its two tilted death intensities add to \(\delta\) by Step 2. This yields the exact identity
\[
 \mathbb E e^{\theta[X_1(t)-X_1(0)]}
 =e^{t\Lambda(\theta)+u h_0}\,
 \mathbb E_\theta e^{-uH_t}.
\]
For \(\theta\in I\), the tilted gap chain is irreducible positive recurrent with stationary probabilities \(\pi_\theta(h)=(1-\rho_\theta)\rho_\theta^h\), \(\rho_\theta=\beta_\theta/\delta\). Moreover \(\rho_\theta e^{-u}=B_\theta/\delta<1\), so the stationary expectation of \(e^{-uH}\) is finite.

For completeness, convergence of this expectation (rather than just weak convergence of \(H_t\)) follows from uniform integrability. If \(u<0\), choose \(s\) with \(-u<s<\log(\delta/\beta_\theta)\). The Lyapunov function \(V(h)=e^{sh}\) has generator \(L_\theta V(h)=-cV(h)\) for \(h>0\), for some \(c>0\), and finite generator at zero. Dynkin's formula implies \(\sup_t\mathbb E_\theta e^{sH_t}<\infty\), giving uniform integrability. If \(u\ge0\), the integrand is bounded. Thus
\[
\lim_{t\to\infty}\mathbb E_\theta e^{-uH_t}
=\sum_{h\ge0}(1-\rho_\theta)\rho_\theta^h e^{-uh}
=\frac{\delta-\beta_\theta}{\delta-B_\theta}.
\]
Substitution completes the asserted full moment-generating asymptotic. The formula \(\Lambda=\beta_\theta-\beta\) also follows by multiplying out \(B_\theta C_\theta\).

**4. Local rare-event rates.** Since \(\Lambda\) is strictly convex, each \(x\in\Lambda'(I)\) has a unique \(\theta\in I\) such that \(x=\Lambda'(\theta)=r_+e^\theta-r_-e^{-\theta}\). Under \(\Pr_\theta\), the rate of the tagged coordinate conditional on gap \(h>0\) is \(b_1e^{\theta-u}-a_1e^{-\theta+u}\), and at zero it is \(-a_1e^{-\theta+u}\). The tilted gap's ergodic theorem, together with a bounded-jump martingale strong law, gives
\[
 \lim_{t\to\infty}t^{-1}[X_1(t)-X_1(0)]
 =-a_1e^{-\theta+u}+\frac{\beta_\theta}{\delta}b_1e^{\theta-u}
 =\Lambda'(\theta),\qquad \Pr_\theta\text{-a.s.}
\]
Fix \(\varepsilon>0\). On the event that the tagged speed is within \(\varepsilon\) of \(x\) and \(H_t\le K\), the reverse likelihood ratio is bounded below by a positive \(K\)-dependent constant times \(e^{-t[\theta x-\Lambda(\theta)+|\theta|\varepsilon]}\). Choose fixed \(K\) so that the tilted stationary gap probability of \([0,K]\) is positive. The tilted strong law and convergence of the gap distribution show this event has nonvanishing tilted probability, so the required logarithmic lower bound follows. For \(\theta>0\), exponential Markov inequality gives an upper bound using \(X_1(t)/t\ge x-\varepsilon\); for \(\theta<0\), use \(X_1(t)/t\le x+\varepsilon\). In either case Step 3 gives limiting upper exponent at most \(-[\theta x-\Lambda(\theta)]+|\theta|\varepsilon\). When \(\theta=0\), the ordinary law of large numbers gives exponent zero. Send \(\varepsilon\downarrow0\), obtaining \(-\mathcal J(x)\) by explicitly solving \(\Lambda'(\theta)=x\).

## Verification
The standalone program `verify.py` gives exact rational tilted-generator identities for many stable positive integer jump-rate choices and rational exponential tilt variables, and independently compares two finite-time matrix-exponential evaluations of the Feynman–Kac identity. It passed 1265 exact rational identities and 72 independent finite-dimensional semigroup comparisons in the checked environment. These finite tests do not prove asymptotic convergence or publication priority; both depend on the written proof and source comparison. The program's numerical finite-state restriction is checked only for its own stated finite-state equality and is not used to justify an infinite-state convergence claim.

## Relationship to prior work
Malyshev, Menshikov, Popov and Wade (arXiv:2205.14990; first submitted May 30, 2022), §2 and §5, establish the two-particle cloud's stability condition, speed, geometric gap law, central limit theorem and *the very same* diffusion coefficient \((a_1a_2+b_1b_2)/(a_2+b_1)\). These are prior results and are not claimed as new. Their exact queue-marking construction and Burke's theorem are relevant established tools, but their Theorems 2.13 and 2.15 do not state the tilted exponential-moment asymptotic, its explicit initial-gap prefactor, or the local non-Gaussian rare-event rate. The present result goes beyond the first two cumulants and needs the exact tilted birth–death calculation and a uniform-integrability argument.

Menshikov, Popov and Wade's arXiv:2610.03206 (first submitted October 2, 2026) studies random-environment cloud decomposition and finite-cloud speeds and motivates examining more detailed distributional behavior of a stable cloud. Its §2.2 cites the earlier finite-cloud theory; it does not state the current tagged-coordinate moment-generating formula. The 2011 de Gier–Essler and 2021 Vanicat–Bertin–Lecomte–Ragoucy current-deviation studies address exclusion models with different geometries and observables. Generic M/M/1 quasi-reversibility is relevant, but a generic departure-count Poisson statement alone does not identify the correlated marked tagged-displacement exponential moments. These comparisons concern *claims and their implications*, not just shared terminology. A broader queueing-current theorem could subsume some or all of this specialized result; independent priority assessment remains necessary.

## Limitations
The result concerns only two fixed positive-rate particles in one strict stability phase, fixed initial gap, and a real tilt in \(I\). The local large-deviation assertion holds only for speeds in \(\Lambda'(I)\); outside this range a different spectral branch or other mechanism may contribute. No entire-line scaled cumulant-generating function, full large-deviation principle, asymptotic independence of arrivals and departures, exact Skellam finite-time law, higher-particle extension, or independent audit is claimed. The originality assessment is based on the inspected primary sources and documented searches; absence of a hit is not proof of priority.

## References
1. V. Malyshev, M. Menshikov, S. Popov and A. Wade, *Dynamics of finite inhomogeneous particle systems with exclusion interaction*, arXiv:2205.14990, first version May 30, 2022, especially Theorems 2.13 and 2.15 and §5. https://arxiv.org/html/2205.14990v3
2. M. Menshikov, S. Popov and A. Wade, *Dynamics for exclusion processes with random environments of particle jump rates*, arXiv:2610.03206v1, submitted October 2, 2026, §2.2. https://arxiv.org/html/2610.03206v1
3. P. J. Burke, *The output of a queuing system*, Operations Research 4 (1956), 699–704, as used in reference 1.
4. J. de Gier and F. H. L. Essler, *Large Deviation Function for the Current in the Open Asymmetric Simple Exclusion Process*, Physical Review Letters 107 (2011), 010602. https://doi.org/10.1103/PhysRevLett.107.010602
5. M. Vanicat, E. Bertin, V. Lecomte and E. Ragoucy, *Mapping current and activity fluctuations in exclusion processes: consequences and open questions*, SciPost Physics 10 (2021), 028. https://doi.org/10.21468/scipostphys.10.2.028
