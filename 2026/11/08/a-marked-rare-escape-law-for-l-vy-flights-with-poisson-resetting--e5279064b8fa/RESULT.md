# A marked rare-escape law for Lévy flights with Poisson resetting

## Finding
Fix a stability index \(0<\alpha<2\), scale \(\sigma>0\), Poisson resetting rate \(r>0\), and relative start \(-1<\lambda<1\). Let \(X\) be a symmetric one-dimensional \(\alpha\)-stable Lévy process with characteristic function
\[
\mathbb E[e^{i\xi X_t}]=\exp(-t\sigma^\alpha|\xi|^\alpha).
\]
For each interval radius \(L>0\), start at \(\lambda L\), evolve using independent copies of \(X\) between independent rate-\(r\) Poisson resets to \(\lambda L\), and stop upon first leaving \((-L,L)\). Denote the stopping time by \(S_L\), the number of resets before exit by \(R_L\), the elapsed time since the final reset by \(B_L\), and the positions just before and at exit by \(P_L\) and \(Z_L\). The initial launch counts as the start of an excursion, not a reset.

Define the positive Lévy-density constant and two exit intensities
\[
 c_{\alpha,\sigma}=\frac{\sigma^\alpha\alpha 2^{\alpha-1}\Gamma((1+\alpha)/2)}{\sqrt\pi\Gamma(1-\alpha/2)},\qquad
 a_+=\frac{c_{\alpha,\sigma}}{\alpha(1-\lambda)^\alpha},\qquad
 a_-=\frac{c_{\alpha,\sigma}}{\alpha(1+\lambda)^\alpha},\qquad a=a_++a_-.
\]
Then the full **joint** weak limit is
\[
 \left(\frac{S_L}{L^\alpha},\frac{R_L}{L^\alpha},B_L,\frac{P_L}{L},\frac{Z_L}{L}\right)
 \ \Longrightarrow\ (T,rT,B,\lambda,Y),\qquad L\to\infty,
\]
where \(T\), \(B\), and \(Y\) are mutually independent, with \(T\sim\mathrm{Exp}(a)\), \(B\sim\mathrm{Exp}(r)\), and \(Y\) supported on the exterior of \((-1,1)\) with density
\[
 f_Y(y)=\frac{c_{\alpha,\sigma}}{a}|y-\lambda|^{-1-\alpha}\,\mathbf1_{\{|y|>1\}}.
\]
The second coordinate \(rT\) is necessarily coupled to \(T\). In particular, the limiting exit-side probabilities are \(a_+/a\) and \(a_-/a\). For a centered launch \(\lambda=0\), the exit sign is fair and independent of the absolute exit coordinate, and
\[
 \mathbb P(|Y|>z)=z^{-\alpha}\quad(z\ge1).
\]
Thus the scaled exit coordinate has an exact Pareto radial law, while the lifetime and the final-excursion age become independent exponentials on *different* time scales.

## Assumptions and scope
All parameters are fixed while \(L\to\infty\), including \(r>0\) and \(\lambda\in(-1,1)\). The process is càdlàg and exits when it first belongs to the closed complement of the open interval; its position at exit includes the jump overshoot. Reset times are independent of every Lévy-flight excursion. The theorem excludes the Gaussian endpoint \(\alpha=2\), a boundary-near initial position varying with \(L\), and non-Poisson resetting. The result is about a single spatial interval, not hitting an isolated point.

## Proof
**1. One-excursion marked short-time lemma.** Write \(\varepsilon=L^{-\alpha}\). By stable scaling, a fresh excursion divided by \(L\) has the law \(\lambda+X_{\varepsilon t}\) at physical time \(t\). Let \(\theta_\varepsilon\) be its first exit from \((-1,1)\), \(U_\varepsilon\) its pre-exit position, and \(V_\varepsilon\) its position at exit. The Lévy measure of \(X\) is \(\nu(dh)=c_{\alpha,\sigma}|h|^{-1-\alpha}dh\).

For every bounded continuous test function \(h(t,u,v)\) whose time support is compact, the small-time marked exit limit is
\[
 \frac1\varepsilon\mathbb E\left[h(\theta_\varepsilon,U_\varepsilon,V_\varepsilon)\right]
 \longrightarrow\int_0^\infty\!dt\int_{|v|>1}
 h(t,\lambda,v)c_{\alpha,\sigma}|v-\lambda|^{-1-\alpha}\,dv.
 \tag{1}
\]
This follows directly from the Lévy–Itô decomposition. Choose a small jump cutoff \(\delta\) strictly smaller than the distance from \(\lambda\) to the boundary. Jumps larger than \(\delta\) constitute a finite-rate compound Poisson process. Over a time interval of length \(\varepsilon M\), two or more such jumps have probability \(O(\varepsilon^2)\). The compensated process with jumps bounded by \(\delta\) stays within an arbitrarily prescribed displacement \(\eta>0\) with probability \(1-o(\varepsilon)\). To see the quantitative point, take the exponential-martingale parameter \(h=\log(1/\varepsilon)/(2\delta)\). For either sign, its cumulant over time \(\varepsilon M\) is at most \(C\varepsilon M h^2 e^{h\delta}\int_{|z|\le\delta}z^2\nu(dz)=O(\varepsilon^{1/2}\log^2(1/\varepsilon))\), while the maximal bound contributes \(e^{-h\eta}=\varepsilon^{\eta/(2\delta)}\). Taking \(\delta<\eta/4\) gives \(o(\varepsilon)\). On the one-large-jump event, the location before the jump converges to \(\lambda\), and its single jump crosses the boundary exactly when \(|\lambda+h|>1\). Potential ambiguities in a boundary strip of width \(\eta\) have first-order mass at most \(\varepsilon M\nu\{h:||\lambda+h|-1|\le\eta\}\), which vanishes after \(\eta\downarrow0\). Compensation of the one-jump event gives (1), including the exit location and the pre-jump position. The Lévy density has no atoms at the two boundary jump sizes.

For passage from compact time tests to exponential weighting, the symmetric Lévy maximal inequality and the stable tail bound give, with \(d=1-|\lambda|>0\),
\[
 \mathbb P(\theta_\varepsilon\le t)\le C\min(1,\varepsilon t d^{-\alpha}).
 \tag{2}
\]
Integration by parts then bounds the scaled contribution from \(t>M\), after multiplication by \(e^{-rt}\), by a constant multiple of \((M+r^{-1})e^{-rM}\). Thus (1) extends to all bounded continuous tests of the pre-exit position and exit location multiplied by a factor \(e^{-rt}\). In particular, the one-excursion success probability satisfies
\[
 q_\varepsilon:=\mathbb P(\theta_\varepsilon<E_r)=\mathbb E[e^{-r\theta_\varepsilon}]
 \sim \varepsilon a/r,
 \tag{3}
\]
where \(E_r\sim\mathrm{Exp}(r)\) is independent. Moreover the unnormalized successful-excursion measure, divided by \(\varepsilon\), converges to
\[
 e^{-rt}dt\ c_{\alpha,\sigma}|v-\lambda|^{-1-\alpha}\mathbf1_{\{|v|>1\}}dv\ \delta_\lambda(du).
 \tag{4}
\]
Equation (4) also gives the conditional successful duration \(\mathrm{Exp}(r)\), the explicit normalized mark distribution, and their independence.

**2. Renewal and separation of time scales.** Independent excursions are attempted until the first success. For \(s\ge0\), put
\[
 q_\varepsilon(s)=\mathbb E[e^{-(r+s)\theta_\varepsilon}],\qquad
 b_\varepsilon(s)=\mathbb E[e^{-sE_r};E_r<\theta_\varepsilon]
 =\frac r{r+s}(1-q_\varepsilon(s)).
\]
The Laplace transform of the complete resetting exit time and the final marks has the exact geometric-renewal identity
\[
 \mathbb E\left[e^{-sS_L}g(B_L,P_L/L,Z_L/L)\right]
 =\frac{\mathbb E[e^{-(r+s)\theta_\varepsilon}g(\theta_\varepsilon,U_\varepsilon,V_\varepsilon)]}
 {1-b_\varepsilon(s)}
 \tag{5}
\]
for bounded continuous \(g\). By (3) and (4), at \(s=\varepsilon u\) the numerator is
\[
 \varepsilon\int_0^\infty e^{-rt}\int_{|v|>1}
 g(t,\lambda,v)c_{\alpha,\sigma}|v-\lambda|^{-1-\alpha}dv\,dt+o(\varepsilon),
\]
and the denominator equals \(\varepsilon(u+a)/r+o(\varepsilon)\). Therefore
\[
 \lim_{L\to\infty}\mathbb E\left[e^{-u S_L/L^\alpha}g(B_L,P_L/L,Z_L/L)\right]
 =\frac{a}{a+u}\mathbb E[g(B,\lambda,Y)].
 \tag{6}
\]
The factorization for every \(u\ge0\) and every bounded continuous \(g\) proves joint convergence and independence of \(T\) from the terminal marks. The factorization of the \(B\)- and \(Y\)-measure in (4) proves their mutual independence.

**3. Reset count.** Let \(N_t\) be the rate-\(r\) reset Poisson process, so \(R_L=N_{S_L}\) almost surely. From (3) and the standard renewal-mean identity,
\[
 \mathbb E[S_L]=\frac{1-q_\varepsilon}{rq_\varepsilon}\sim \frac{L^\alpha}{a}.
\]
The stopped compensated Poisson martingale satisfies
\[
 \mathbb E[(R_L-rS_L)^2]=r\mathbb E[S_L],
\]
by localization and square-integrable optional stopping (the finite expected stopping time just established permits the limit). Consequently \((R_L-rS_L)/L^\alpha\to0\) in \(L^2\). Combined with (6), this gives the second coordinate \(rT\) in the asserted joint limit.

**4. Explicit normalization and centered Pareto law.** Integrating the Lévy measure over the positive and negative exterior gives respectively \(a_+\) and \(a_-\). Their sum \(a\) normalizes \(f_Y\). At \(\lambda=0\), the density becomes \((\alpha/2)|y|^{-1-\alpha}\mathbf1_{\{|y|>1\}}\); integration over both tails yields \(z^{-\alpha}\). This completes the proof.

## Verification
The standalone `CHECKER.py` evaluates both exterior integrals of the proposed exit density, the side probabilities, the centered Pareto survival function, the limiting joint Laplace-product identity, and the Cauchy-scale consistency \(c_{1,1}=1/\pi\) and \(1/a=\pi/2\) for \(\lambda=0\). It also performs a separately labeled coarse-grid Cauchy-flight diagnostic, which cannot prove a continuous-time exit theorem. Run `python CHECKER.py` in an environment with SciPy. The exact mechanism needed for the theorem is the Lévy–Itô one-large-jump limit plus the independent geometric renewal identity (5); no finite computation is used as a substitute for these arguments.

## Relationship to prior work
Żbik and Palmowski, arXiv:2610.20410 (first public October 14, 2026), establish the large-interval leading mean first-exit scaling for Lévy flights with resetting; this supplies the motivating gap but does not state the entire joint marked limit. Linn and Lawley, *Physical Review E* 108, 024114 (2023), prove generic exponential limits and moment asymptotics for first-passage times under frequent resetting. Thus the exponential marginal for \(T\) is **not** claimed as a new principle. Linn and Lawley, *Journal of Physics A* 57, 305003 (2024), derive conditional target-selection asymptotics, including two absorbing exterior regions for Lévy flights. Thus the separate asymptotic exit-side probabilities are also **not** claimed as new principles. The proposed combined result identifies the full continuous overshoot law, the terminal pre-jump position, the distinct-scale final age, the reset count, and their joint dependence/independence structure in the fixed-rate, expanding-interval model. Generic small-noise marked-exit theory for heavy-tailed perturbations provides related mechanisms but requires comparison of its dynamical hypotheses with hard resetting. The proof here is direct for this model.

## Limitations
The theorem is asymptotic as \(L\to\infty\); it supplies neither a finite-\(L\) error bound nor a universal finite-domain formula. The condition \(\lambda\) fixed in the strict interior is essential for the stated scaling. The Gaussian endpoint has a different large-interval regime. The exponential and side-probability marginals have prior theoretical coverage; any publication-priority claim is restricted to the specific continuous marked joint limit as a whole, and a broader unindexed marked-renewal theorem could imply it. The Cauchy mesh diagnostic has time-discretization error and is not evidence of exact finite-\(L\) first-passage statistics.

## References
1. B. Żbik and Z. Palmowski, *Asymptotic behaviour for escaping an interval by Lévy flights under stochastic resetting*, arXiv:2610.20410 (2026). https://arxiv.org/abs/2610.20410
2. S. Linn and S. D. Lawley, *First-passage times under frequent stochastic resetting*, Physical Review E 108, 024114 (2023), arXiv:2302.05409. https://arxiv.org/abs/2302.05409
3. S. Linn and S. D. Lawley, *Hitting probabilities for fast stochastic search*, Journal of Physics A 57, 305003 (2024), arXiv:2404.01142. https://arxiv.org/abs/2404.01142
4. B. Żbik and B. Dybiec, *Lévy flights and Lévy walks under stochastic resetting*, Physical Review E 109, 044147 (2024), arXiv:2311.16014. https://arxiv.org/abs/2311.16014
5. M. Högele and I. Pavlyukevich, *The exit problem from the neighborhood of a global attractor for heavy-tailed Lévy diffusions* (2013), arXiv:1303.5031. https://arxiv.org/abs/1303.5031
