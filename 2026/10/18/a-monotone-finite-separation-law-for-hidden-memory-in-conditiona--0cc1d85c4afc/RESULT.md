# A monotone finite-separation law for hidden memory in conditional quantum resetting

## Finding

For the symmetric two-site conditional-reset tight-binding walk defined below, the post-reset sign is a stationary two-state Markov chain. Its exact correlation after \(k\) resets is \(\mathbb E[\sigma_0\sigma_k]=m_a(\varepsilon)^k\), where \(a\in\mathbb N\) is the reset-site distance and \(\varepsilon=r/\gamma>0\) is the ratio of resetting and hopping rates. The one-step eigenvalue is
\[
 m_a(\varepsilon)=1-2a\int_0^\infty e^{-\varepsilon x}\frac{J_a(x)^2}{x}\,dx.
\]
It lies strictly between zero and one, increases strictly with either \(a\) or \(\varepsilon\), and determines the entire sign autocorrelation sequence. In particular, the stationary reset-sign marginals are always fair even though the correlations are not.

Under the physical large-separation scaling \(\varepsilon=z/a\), where \(z>0\) is fixed, define \(F_a(z)=m_a(z/a)\). Let \(E\) have the standard rate-one exponential law, and define
\[
 W_a=2a\sinh\!\left(\frac{E}{2a}\right),\qquad
 h_z(w)=\frac2\pi\arcsin\!\left(\min\left\{1,\frac zw\right\}\right).
\]
Then the **exact coupling**
\[
 F_a(z)=\mathbb E[h_z(W_a)]
\]
implies the sharp all-size ordering
\[
 0<F_1(z)<F_2(z)<\cdots<F_a(z)<F_{a+1}(z)<F(z)<1,
 \qquad F(z)=\frac2\pi\int_0^zK_0(s)\,ds.
\]
Here \(K_0\) is the modified Bessel function of the second kind. In particular, the integer lattice approaches its ballistic crossover from **strictly below**, not merely in asymptotic order.

There is also a quantitative sharp finite-separation correction, with \(K_1\) the next modified Bessel function:
\[
 \boxed{\displaystyle
 F_a(z)=F(z)-\frac{z^2K_1(z)+z^3K_0(z)}{12\pi a^2}
       +O(a^{-4}) .}
\]
The remainder is **uniform in \(z\ge 0\)** (with the continuous interpretation at \(z=0\)), whereas the displayed coefficient is strictly negative for every \(z>0\). Consequently the sign-label spectral gap \(1-F_a(z)\) has the corresponding strictly positive finite-distance correction at order \(a^{-2}\). For fixed reset count \(k\), the full scaled correlation converges to \(F(z)^k\).

## Assumptions and scope

Take the infinite one-dimensional lattice \(\mathbb Z\), Planck's constant one, and Hamiltonian
\[
 H=-\frac\gamma2\sum_{j\in\mathbb Z}
 \bigl(|j+1\rangle\langle j|+|j\rangle\langle j+1|\bigr),\qquad \gamma>0.
\]
Between successive independent rate-\(r>0\) Poisson alarms, the particle evolves unitarily from its most recent reset basis state. At an alarm, a position measurement with a positive outcome resets the state to \(|+a\rangle\), a negative outcome to \(|-a\rangle\), and an outcome zero chooses either with probability one-half. The integer \(a\ge1\) is fixed within a given process. All flight times and tie-breaker coins are independent. The label \(\sigma_k\in\{-1,+1\}\) refers to the location **just after** reset number \(k\), and correlations are sampled by reset number rather than by laboratory time. The stationary label law is used for \(\mathbb E[\sigma_0\sigma_k]\). The result does not assert independence of labels at different reset events.

The law of free-flight displacement from any starting site is \(\Pr\{X(t)-X(0)=j\}=J_j(\gamma t)^2\). This is the conventional continuous-time nearest-neighbour quantum walk; the conditional protocol and the symmetric two-site geometry occur in Acharya–Gupta (2023).

## Proof

**Step 1: Exact two-state kernel.** Put \(x=\gamma t\). By reflection, the probability of choosing the opposite reset site following a flight from \(+a\) is
\[
 q_a(x)=\sum_{j=a+1}^\infty J_j(x)^2+\frac12J_a(x)^2,
\]
where the index \(j\) represents the magnitude of a leftward displacement. Consequently the conditional expected outgoing label is
\[
 M_a(x)=1-2q_a(x)=J_0(x)^2+2\sum_{j=1}^{a-1}J_j(x)^2+J_a(x)^2.
\]
The same formula applies to a flight from \(-a\), after reversing signs. Averaging the independent exponential flight length \(x\sim\operatorname{Exp}(\varepsilon)\) gives the transition matrix \(\bigl(\begin{smallmatrix}1-q&q\\q&1-q\end{smallmatrix}\bigr)\), with \(q=(1-m_a)/2\) and \(m_a=\varepsilon\int_0^\infty e^{-\varepsilon x}M_a(x)\,dx\). Since its invariant law is \((1/2,1/2)\), and its centered eigenvector is \((1,-1)\), the stationary \(k\)-step covariance is exactly \(m_a^k\).

**Step 2: Flux identity and positivity.** The standard recurrences \(J_j'=(J_{j-1}-J_{j+1})/2\) and \(J_{j-1}+J_{j+1}=2jJ_j/x\) give, by telescoping,
\[
 M_a'(x)=-\frac{2a}{x}J_a(x)^2,\qquad
 M_{a+1}(x)-M_a(x)=J_a(x)^2+J_{a+1}(x)^2.
\]
As \(M_a(0)=1\), the boundary value \(M_a(x)\to0\) follows from the fixed-order Bessel large-argument asymptotic. Hence
\[
 M_a(x)=2a\int_x^\infty\frac{J_a(t)^2}{t}\,dt,
 \qquad 2a\int_0^\infty\frac{J_a(t)^2}{t}\,dt=1.
\]
Integrating by parts in the exponential average proves the asserted formula for \(m_a\). It lies in \((0,1)\), is strictly increasing in \(a\) by the positive difference above, and is strictly increasing in \(\varepsilon\) because a larger exponential rate stochastically shortens the flight and \(M_a\) is strictly decreasing in the sense of nonconstant monotone functions. This establishes the exact finite-site assertion.

**Step 3: Legendre representation.** The classical Bessel product Laplace formula gives, for \(\varepsilon>0\),
\[
 \int_0^\infty e^{-\varepsilon x}J_a(x)^2\,dx
 =\frac1\pi Q_{a-1/2}(1+\varepsilon^2/2).
\]
Differentiating \(F_a(z)=m_a(z/a)\) therefore yields
\[
 F_a'(z)=\frac2\pi Q_{a-1/2}\!\left(1+\frac{z^2}{2a^2}\right),
 \qquad F_a(0)=0.
\]
Use the standard integral representation
\[
 Q_{a-1/2}(\cosh\eta)
 =\frac1{\sqrt2}\int_\eta^\infty
 \frac{e^{-at}}{\sqrt{\cosh t-\cosh\eta}}\,dt .
\]
With \(w=2a\sinh(t/2)\), \(z=2a\sinh(\eta/2)\), it becomes the Abel-type integral
\[
 Q_{a-1/2}\!\left(1+\frac{z^2}{2a^2}\right)
 =\int_z^\infty\frac{f_a(w)}{\sqrt{w^2-z^2}}\,dw,
 \quad f_a(w)=\frac{\exp[-2a\operatorname{arsinh}(w/(2a))]}{\sqrt{1+w^2/(4a^2)}}.
\]
Integrating in \(z\) and interchanging two positive integrals gives
\[
 F_a(z)=\frac2\pi\int_0^\infty f_a(w)
 \arcsin\!\left(\min\{1,z/w\}\right)\,dw.
\]
Crucially, \(f_a\) is a probability density: the inverse substitution \(w=2a\sinh(u/(2a))\) gives \(f_a(w)\,dw=e^{-u}\,du\). This proves the exact exponential-variable coupling.

**Step 4: All-size ordering and ballistic limit.** For every fixed \(u>0\), the function \(2a\sinh(u/(2a))\) is strictly decreasing in \(a>0\) and strictly greater than \(u\). For fixed \(z>0\), the clipped arcsine function \(h_z(w)\) is nonincreasing in \(w\), and strictly decreasing for \(w>z\). A rate-one exponential variable assigns positive probability to \(E>z\), so the coupling gives \(F_a(z)<F_{a+1}(z)<\mathbb E[h_z(E)]\), strictly. Dominated convergence identifies \(F(z)=\mathbb E[h_z(E)]\). Differentiating its Abel form yields \(F'(z)=2K_0(z)/\pi\), with \(F(0)=0\), hence the displayed limiting integral. Positivity of \(K_0\) and \(\int_0^\infty K_0(z)\,dz=\pi/2\) imply \(0<F(z)<1\) for finite positive \(z\).

**Step 5: Uniform, sign-sharp correction.** Expanding the explicit probability density at fixed \(w\) gives
\[
 f_a(w)=e^{-w}\left[1+\frac{w^3-3w^2}{24a^2}\right]
      +R_a(w),\qquad \int_0^\infty|R_a(w)|\,dw=O(a^{-4}).
\]
For completeness, the \(L^1\) remainder follows by splitting at \(w=a^{1/5}\): on the lower interval, Taylor's theorem for \(\operatorname{arsinh}\) and \((1+s^2)^{-1/2}\) yields an integrated polynomial multiple of \(a^{-4}e^{-w}\); on the upper interval the exact density has tail \(\exp[-2a\operatorname{arsinh}(a^{1/5}/(2a))]\), exponentially small in \(a^{1/5}\), as does the approximation. Since \(0\le h_z\le1\), this bound is uniform in \(z\ge0\). Substituting into the coupling shows that the coefficient of \(a^{-2}\) is
\[
 \frac1{12\pi}\int_0^\infty
 e^{-w}(w^3-3w^2)\arcsin(\min\{1,z/w\})\,dw.
\]
Differentiate in \(z\) under the integral. The identity \(\int_z^\infty e^{-tw}/\sqrt{w^2-z^2}\,dw=K_0(tz)\) and two and three derivatives in \(t\) yield the exact moments
\[
\begin{aligned}
\int_z^\infty\frac{e^{-w}w^2}{\sqrt{w^2-z^2}}\,dw&=z^2K_0(z)+zK_1(z),\\
\int_z^\infty\frac{e^{-w}w^3}{\sqrt{w^2-z^2}}\,dw&=z^3K_1(z)+z^2K_0(z)+2zK_1(z).
\end{aligned}
\]
Thus the coefficient derivative is
\[
 \frac{(z^3-z)K_1(z)-2z^2K_0(z)}{12\pi}.
\]
The coefficient vanishes at \(z=0\), so the identities \(K_0'=-K_1\) and \(K_1'=-K_0-K_1/z\) integrate it exactly to \(-[z^2K_1(z)+z^3K_0(z)]/(12\pi)\). Both \(K_0\) and \(K_1\) are positive for \(z>0\). This proves the uniform \(O(a^{-4})\) expansion and its strict negative leading correction. Finally \(F_a(z)^k\to F(z)^k\) by the stationary Markov property.

## Verification

The accompanying `verify.py` checks the Bessel-flux identity, two independent exact representations of the post-reset eigenvalue, monotonicity at sampled positive parameters, the explicit uniform-order correction at sampled positive \(z\), the limiting bounds, and large-reset-rate scaling. It uses Python 3, NumPy and SciPy; execute `python verify.py`. All **81** numerical assertions passed for the packaged script. These finite checks are not a substitute for the preceding proofs; they do not certify every parameter value or mathematical priority.

## Relationship to prior work

Acharya and Gupta (2023), arXiv:2308.14040, establish the conditional two-site resetting rule, the bare tight-binding Bessel occupation law, an exact reset-history expansion, and the stationary one-point position distribution for symmetric reset sites. In particular their Eq. (53) explains why this one-point distribution involves only the most recent reset; Eqs. (27)–(31) contain the conditional probabilities from which a reset-epoch sign chain can be constructed. Their Eq. (58) also gives the Bessel–Legendre transform used here. The present finding concerns the **unobserved cross-reset sign memory**: an all-site-order coupling, a sharp ballistic scaling profile, and a uniform finite-distance correction, rather than another stationary spatial marginal.

Konno (2004), arXiv:quant-ph/0408140, proves the arcsine weak ballistic limit for the unreset continuous-time quantum walk. That limit motivates the scale \(r a/\gamma\) and is consistent with the leading crossover, but does not itself provide the exact all-distance coupling or the signed order-\(a^{-2}\) correction. Durand (2018), arXiv:1803.09396, develops general large-order Legendre-to-Bessel expansions that can imply aspects of the correction after specializing the parameters; no new general Legendre-function asymptotic calculus is claimed. The present result is the resetting-model implication and nonasymptotic monotonicity.

## Limitations

The label correlation is measured **per reset event**, not at fixed physical-time separation. The noise is independent exponential resetting, and the reset-site pair is symmetric with the origin-tie rule stated above; arbitrary reset geometries, biased decisions, random hopping strengths, and non-Poisson alarms are not covered. The parameter \(a\) is an integer, and the uniform expansion concerns the coupled regime \(r/\gamma=z/a\); it does not by itself cover unrelated joint parameter scalings. General special-function asymptotic formulae and the original conditional-protocol recursion may overlap with parts of the derivation, so independent priority comparison is needed. No independent verification or experimental validation is claimed.

## References

1. A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, arXiv:2308.14040 (first publicly posted 2023-08-27), https://arxiv.org/html/2308.14040v2.
2. N. Konno, *Limit Theorem for Continuous-Time Quantum Walk on the Line*, arXiv:quant-ph/0408140 (2004), https://arxiv.org/abs/quant-ph/0408140.
3. L. Durand, *Asymptotic Bessel-function expansions for Legendre and Jacobi functions*, arXiv:1803.09396 (2018), https://arxiv.org/abs/1803.09396.
