# Gaussian–Laplace–Pareto homodyne transition in a telegraph-pumped optical cavity

## Finding

Consider the ideal linear single-mode degenerate parametric cavity described below, driven by an independent on/off Markov pump. The stationary **intracavity** homodyne statistics have three distinct and sharp tail regimes, even though every state conditioned on the complete pump history is Gaussian. The result includes the exact stationary pump-resolved variance laws, the tail amplitude in the heavy-tail regime, and the sharp mean-photon and second-factorial-photon thresholds.

Use dimensionless time \(s=\Gamma t\), thermal quadrature scale \(c=2n_{\mathrm b}+1\), off-to-on rate \(a>0\), on-to-off rate \(b>0\), and normalized pump strengths \(0\) (off) and \(h>0\) (on). Define the antisqueezed variance \(Y_s=\Delta Y_s^2/c\), the shifted variance \(Z_s=Y_s-1\), and the stationary homodyne observation \(Q\), whose conditional law given a pump path is centered Gaussian with variance \(cY_s\).

**Stationarity:** a proper stationary distribution for \(Y_s\) exists if and only if
\[
 h<1+\frac ba.
\]
For \(h>1\) in this interval, put \(k=h-1\), \(\theta=b/k-a>0\), and \(p_0=b/(a+b)\). Then the stationary pump-off and pump-on densities in the coordinate \(U=kZ/(h+kZ)\in(0,1)\), respectively, are
\[
 f_0(u)=\frac{p_0}{B(a,\theta)}u^{a-1}(1-u)^{\theta-1},\qquad
 f_1(u)=\frac{u}{k}f_0(u).
\]
In particular, their integrals are \(p_0\) and \(1-p_0\), and
\[
 \Pr(Y>y)\sim K_Yy^{-\theta},\quad
 K_Y=\frac{p_0(h/k)^{\theta+1}}{\theta B(a,\theta)},\qquad y\to\infty.
\]
The *unconditioned* intracavity homodyne observation has the exact Pareto tail equivalent
\[
 \boxed{\Pr(|Q|>R)\sim K_QR^{-2\theta}},\qquad
 K_Q=K_Y(2c)^\theta\frac{\Gamma(\theta+\tfrac12)}{\sqrt\pi},\qquad R\to\infty.
\]

The two remaining regimes yield different logarithmic rates. For \(0<h<1\), \(Y\) has upper endpoint \(1/(1-h)\), and
\[
 \lim_{R\to\infty}\frac{\log\Pr(|Q|>R)}{R^2}=-\frac{1-h}{2c}.
\]
At the exact deterministic parametric threshold \(h=1\), the shifted variance has an explicit gamma mixture (see below) and
\[
 \lim_{R\to\infty}\frac{\log\Pr(|Q|>R)}{R}=-\sqrt{\frac{2b}{c}}.
\]
Thus the homodyne tail changes from Gaussian to exponential to power-law as the pump strength crosses unity; the heavy-tailed stationary phase terminates at \(h=1+b/a\).

For \(h>1\), and every real \(m>0\),
\[
 \mathbb E[Y^m]<\infty\quad\Longleftrightarrow\quad m<\theta
 \quad\Longleftrightarrow\quad h<1+\frac{b}{a+m}.
\]
A proper stationary density operator can consequently have an *infinite mean intracavity photon number* when \(1<\!h<1+b/a\) but \(h\ge1+b/(a+1)\). When \(1+b/(a+2)\le h<1+b/(a+1)\), the mean photon number is finite but its second factorial moment is infinite. Statements at the equality thresholds are strict: the corresponding moments diverge.

## Assumptions and scope

The cavity has one bosonic mode \(\hat a\), a thermal Markovian bath with occupation \(n_{\mathrm b}\ge0\), amplitude-damping normalization \(\Gamma>0\), zero coherent displacement, no Kerr nonlinearity, no pump depletion, zero detuning, and a real pump phase that remains fixed as its **amplitude** switches. The parametric pump is a classical, independent, stationary continuous-time two-state Markov chain with rates \(\Gamma a\) and \(\Gamma b\). The normalization of the optical quadratures is chosen so vacuum has variance one. Thermal noise acts continuously in either pump mode, and it is independent of the Markov pump.

Conditioned on a complete pump history, the standard Gaussian Lindblad dynamics give \(\dot X=1-(1+g)X\) and \(\dot Y=1-(1-g)Y\), where \(X=\Delta X^2/c\), \(Y=\Delta Y^2/c\), a dot denotes derivative in dimensionless time, and \(g\in\{0,h\}\). The quantity \(X\) always admits a stationary law supported in \([1/(1+h),1]\); the theorem concerns the possibly unbounded \(Y\) and the quantum mixture obtained by forgetting the pump history. \(Q\) is a *single-time intracavity* phase-sensitive homodyne quadrature, not the full time-integrated emitted-output field.

## Proof

**1. Random affine flow and stationary existence.** Setting \(Z=Y-1\), its deterministic vector fields are \(F_0(z)=-z\) when the pump is off, and \(F_1(z)=h+(h-1)z\) when it is on. They preserve \(z\ge0\). The homogeneous scalar flow over \([s,t]\) has multiplier \(\exp\{-\int_s^t(1-g(v))\,dv\}\). The stationary Markov chain spends fractions \(p_0=b/(a+b)\) and \(p_1=a/(a+b)\) in the two modes. Its multiplicative Lyapunov exponent is \([-b+a(h-1)]/(a+b)\). The pullback affine integral
\[
 Y_*(0)=\int_{-\infty}^0\exp\!\left[-\int_u^0(1-g(v))\,dv\right]du
\]
is finite almost surely exactly when that exponent is negative. It then gives the unique invariant pullback law (two solutions driven by the same chain contract exponentially). For nonnegative exponent, the integral diverges almost surely: at positive exponent its integrand eventually grows exponentially; at zero exponent the additive functional sampled at successive complete on/off cycles is a nondegenerate centered random walk with independent cycle increments (exponential sojourn durations). This random walk oscillates recurrently across any fixed finite level; the continuous-time integral consequently contains infinitely many disjoint intervals of positive length on which its positive integrand is bounded below, giving divergence. Equivalently, the stationary forward flux equation below has no normalizable nonnegative solution. The condition simplifies to \(h<1+b/a\).

**2. Exact flux solution and normalization.** Write \(\rho_j(z)\) for the stationary joint density of \(Z\) and pump state \(j\). The two stationary balance equations are
\[
 0=-\partial_z(F_0\rho_0)-a\rho_0+b\rho_1,\qquad
 0=-\partial_z(F_1\rho_1)+a\rho_0-b\rho_1.
\]
The total probability flux vanishes at the natural inaccessible boundary \(z=0\), so \(F_0\rho_0+F_1\rho_1=0\), hence \(\rho_1=z\rho_0/(h+(h-1)z)\). The off-state equation gives, up to normalization,
\[
 \rho_0(z)\propto z^{a-1}\,[h+(h-1)z]^{-b/(h-1)}\quad(h\ne1),
\]
with exponential replacement \(\rho_0(z)\propto z^{a-1}e^{-bz}\) at \(h=1\). Integrating these densities fixes their separate state masses to \(p_0,p_1\), rather than guessing one common constant.

For \(0<h<1\), put \(d=1-h\), \(\eta=b/d\), and \(U=dZ/h\in(0,1)\). The transformed joint densities are
\[
 f_0(u)=\frac{p_0}{B(a,\eta+1)}u^{a-1}(1-u)^\eta,
 \qquad f_1(u)=\frac{u}{d(1-u)}f_0(u).
\]
For \(h=1\), in the coordinate \(z=Z\),
\[
 \rho_0(z)=\frac{p_0b^a}{\Gamma(a)}z^{a-1}e^{-bz},\qquad \rho_1(z)=z\rho_0(z).
\]
For \(1<h<1+b/a\), put \(k=h-1\), \(\theta=b/k-a\), and \(U=kZ/(h+kZ)\). The stated beta densities follow. Their normalization is direct: \(\int f_0=p_0\) and \(\int f_1=p_0a/[k(a+\theta)]=p_1\). As \(u\uparrow1\), the total beta-coordinate density is asymptotic to \(p_0(h/k)(1-u)^{\theta-1}/B(a,\theta)\). Since \(Z=(h/k)u/(1-u)\), integration yields the exact constant \(K_Y\), and also proves that moments of positive order \(m\) are finite exactly when \(m<\theta\). At \(\theta\le0\) the same stationary flux solution is nonintegrable at infinity; there is no finite invariant measure.

**3. The three homodyne tails.** For every fixed pump history the intracavity state is centered Gaussian, so an unobserved-pump homodyne sample can be represented as \(Q=\sqrt{cY}\,G\), with \(G\sim N(0,1)\) independent of \(Y\). If \(0<h<1\), essential supremum \(Y=1/d\) and positive stationary mass arbitrarily close to that endpoint give the Gaussian logarithmic rate by sandwiching conditional normal tails. At \(h=1\), the law of \(Z\) has a polynomial-times-\(e^{-bz}\) density; the Laplace principle for \(bz+R^2/[2c(1+z)]\) gives the rate \(R\sqrt{2b/c}\). For \(h>1\) in the stationary phase, \(\Pr(Y>y)\sim K_Yy^{-\theta}\). Conditioning on \(G\), regular variation and finite moments of every Gaussian power give
\[
 \Pr(|Q|>R)\sim K_Yc^\theta\mathbb E|G|^{2\theta}\,R^{-2\theta},
\quad \mathbb E|G|^{2\theta}=2^\theta\Gamma(\theta+1/2)/\sqrt\pi.
\]
This proves the coefficient \(K_Q\), not just the exponent.

**4. Physical energy and factorial moments.** For every pump history, the centered Gaussian photon number and anomalous moment are
\[
 n_g=\frac{c(X+Y)-2}{4},\qquad
 |m_g|=\frac{c|Y-X|}{4}.
\]
The boundedness of \(X\), together with \(Y\ge1\), shows \(n_g\asymp Y\) at large \(Y\). Gaussian Wick factorization gives the conditional second factorial photon moment \(2n_g^2+|m_g|^2\asymp Y^2\) at large \(Y\). Integrating over pump histories shows that mean photon number is finite iff \(\theta>1\), and that the second factorial moment is finite iff \(\theta>2\). A convex mixture of trace-one Gaussian density operators remains a trace-one density operator even when these unbounded observables have infinite expectation.

## Verification

The included `verify.py` recomputes all three stationary pump-state normalizations by adaptive quadrature; checks stationary forward balance at nontrivial points; checks the closed-form first and second \(Z\)-moments against independent numerical integration; and integrates the exact Gaussian survival mixture to compare its predicted Gaussian, exponential, and Pareto tails. In one supercritical test, the normalized Pareto-tail ratio approaches \(0.9998510744\) at measurement threshold \(R=160\). Finite numerical tests are corroboration; the infinite-limit and if-and-only-if claims follow from the analytic proof above.

## Relationship to prior work

Hughes and Dignam (2024, arXiv:2406.18694) derive the Gaussian quadrature evolution for a prescribed pump in a thermal bath; these quadrature equations and the conditional Gaussian state are **not** new. Bena (2006, arXiv:cond-mat/0606116) gives general two-state dichotomous-noise stationary density methods, which encompass the flux technique and bounded switching-law calculation as specializations. Eab and Lim (2016, arXiv:1612.03013) study classical Ornstein–Uhlenbeck dynamics with fluctuating damping, including moment stability. These generic switched-linear-system ingredients are **not** claimed as new. The contribution assessed here is the complete optical observable-level conjunction: sharp *intracavity* homodyne Gaussian/exponential/Pareto transition and its explicit heavy-tail coefficient, the stationary-above-deterministic-threshold interval, and separate finite mean-energy/second-factorial-photon thresholds. A remotely related analysis of parametrically pumped oscillator statistics with fixed drive is not a covering result for classical telegraph pumping.

## Limitations

The pump is imposed externally and may exceed the usual deterministic parametric threshold. No saturation or pump depletion is included, so the ideal stationary heavy-tailed phase should not be extrapolated to a real oscillator with nonlinear stabilization. The theorem does not concern time-integrated output-field homodyne statistics, transient tails, pump phase flips, non-Markov pump holding times, nonthermal reservoirs, or simultaneous uncertainty in the quadrature axes. The density calculation is a specialization of established dichotomous-noise theory; an exactly equivalent quantum-optical tail calculation in less accessible literature remains a possible originality risk. No independent validation has been performed.

## References

1. P. R. B. Hughes and M. M. Dignam, *Analytic solution to the nonlinear generation of squeezed states in a thermal bath*, arXiv:2406.18694 (first public 2024-06-26). https://arxiv.org/abs/2406.18694
2. I. Bena, *Dichotomous Markov noise: Exact results for out-of-equilibrium systems. A review*, Int. J. Mod. Phys. B 20 (2006), arXiv:cond-mat/0606116. https://arxiv.org/abs/cond-mat/0606116
3. C. H. Eab and S. C. Lim, *Ornstein–Uhlenbeck Process with Fluctuating Damping*, arXiv:1612.03013 (first public 2016-12-09). https://arxiv.org/abs/1612.03013
4. F. A. A. El-Orany, J. Peřina and M. S. Abdalla, *Quantum properties of the parametric amplifier with and without pumping field fluctuations*, arXiv:0909.0313 (2009), a different pumping-fluctuation model. https://arxiv.org/abs/0909.0313
