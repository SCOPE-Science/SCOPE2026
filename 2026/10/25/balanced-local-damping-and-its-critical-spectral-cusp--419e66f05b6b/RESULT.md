# Balanced local damping and its critical spectral cusp

## Finding
Consider two identical unit point masses, each attached to ground by a spring of stiffness \(a>0\), joined by a spring of stiffness \(b>0\), and equipped with nonnegative individual viscous dampers \(\gamma_1,\gamma_2\) of fixed total \(G>0\). Define the spectral decay rate \(R\) as the negative of the largest real part of the four characteristic exponents, counting algebraic multiplicity. For every positive \(a,b,G\), **the unique allocation maximizing \(R\) is \(\gamma_1=\gamma_2=G/2\)**, and its exact value is
\[
R_*(G)=\frac G4-\sqrt{\max\{0,G^2/16-a\}}.
\]
If the total budget is also freely optimized over \(G>0\), the sole global optimizer is \(G=4\sqrt a\), \(\gamma_1=\gamma_2=2\sqrt a\), attaining \(R=\sqrt a\), independent of coupling \(b\).

The loss of optimality under an imbalance has a sharp change of scaling. For fixed \(a,b,G>0\), put \(d=(\gamma_1-\gamma_2)/2\). As \(d\to0\) through admissible allocations, the exact leading laws are
\[
R_*(G)-R(G,d)=\begin{cases}
\dfrac{G}{8b}d^2+O(d^4),&0<G<4\sqrt a,\\[4pt]
\sqrt{\dfrac{a}{2b}}\,|d|+O(d^2),&G=4\sqrt a,\\[4pt]
\dfrac{R_*(G)^2}{2b\sqrt{G^2/4-4a}}d^2+O(d^4),&G>4\sqrt a.
\end{cases}
\]
Thus the unique jointly optimal (critical-damping) design is linearly sensitive to small imbalance, whereas every noncritical fixed-budget balanced design is quadratically sensitive.

## Assumptions and scope
The undriven linear, finite-dimensional equations are
\[
\ddot x+\begin{pmatrix}\gamma_1&0\\0&\gamma_2\end{pmatrix}\dot x+
\begin{pmatrix}a+b&-b\\-b&a+b\end{pmatrix}x=0.
\]
All springs are positive, masses are one, and both dampers satisfy \(\gamma_i\ge0\), \(\gamma_1+\gamma_2=G>0\). In the notation \(q=G/2\), \(d=(\gamma_1-\gamma_2)/2\), feasibility means \(|d|\le q\). The characteristic polynomial and rate are
\[
P_{a,b,G,d}(s)=(s^2+qs+a)(s^2+qs+a+2b)-d^2s^2,\qquad
R(G,d)=-\max_{P(s)=0}\Re s.
\]
The rate is the asymptotic spectral decay exponent. At a defective eigenvalue it does not assert a uniform state norm bound with exactly that exponent; for every strictly smaller exponential rate, such a bound holds.

## Proof
**Stability.** The positive mechanical energy \(E=(|\dot x|^2+x^TKx)/2\), where \(K\) denotes the displayed stiffness matrix, has derivative \(\dot E=-\gamma_1\dot x_1^2-\gamma_2\dot x_2^2\le0\). Thus no characteristic root lies in the open right half-plane. The matrix \(K\) is positive definite so \(s=0\) is not a root. If a nonzero imaginary root existed, taking the imaginary part of the complex modal energy identity forces all velocity coordinates with positive damping to vanish; since \(G>0\), at least one coordinate vanishes. The off-diagonal coupling \(-b\ne0\) then forces the other coordinate to vanish, a contradiction. Hence all four characteristic roots lie strictly in the open left half-plane even if one damper vanishes.

**Balanced spectrum.** At \(d=0\), the characteristic polynomial factors into the two normal-mode quadratics \(F_-(s)=s^2+qs+a\), \(F_+(s)=s^2+qs+a+2b\). The slower spectral root is governed by \(F_-\), giving exactly \(R_*(G)\) above.

**Global uniqueness for undercritical and critical budgets.** Assume \(0<G\le4\sqrt a\). Every balanced root has real part \(-G/4\). In any allocation the sum of the four roots is \(-G\), so the largest real part is at least \(-G/4\). Suppose an imbalanced allocation achieved equality. Then all four roots would have identical real part \(-G/4\). After translation \(s=z-G/4\), they would all be purely imaginary. A monic real quartic whose four roots are purely imaginary (with multiplicities) must be an even polynomial; however direct expansion of \(P(z-G/4)\) yields the coefficient \(Gd^2/2\) multiplying \(z\). As \(G>0\), this coefficient cannot vanish unless \(d=0\). Therefore imbalance is strictly suboptimal.

**Global uniqueness for overcritical budgets.** Suppose \(G>4\sqrt a\), and let \(s_*=-R_*(G)<0\) be the greater real root of \(F_-\). Then \(P(s_*)=-d^2s_*^2<0\) whenever \(d\ne0\), whereas \(P(0)=a(a+2b)>0\). By continuity there is a characteristic real root strictly between \(s_*\) and zero, so the imbalanced allocation has strictly slower spectral decay.

**Joint optimization of the total damping.** For \(G\le4\sqrt a\), \(R_*(G)=G/4\) increases strictly. For \(G>4\sqrt a\), differentiate \(G/4-\sqrt{G^2/16-a}\); its derivative is strictly negative. Thus the unique optimal total budget is \(G=4\sqrt a\), proving the global rate and allocation statements.

**Imbalance sensitivity.** Write \(F_-F_+-d^2s^2=0\) and perturb its simple balanced roots in powers of \(d^2\). The leading root correction at any simple root \(s_0\) is
\[
\delta s=\frac{s_0^2}{F_-'(s_0)F_+(s_0)}d^2+O(d^4)
\]
for a root of \(F_-\), and the analogous expression exchanging the factors for a root of \(F_+\). If \(0<G<4\sqrt a\), the two roots of \(F_+\) have positive real-part shift \(Gd^2/(8b)\); the roots of \(F_-\) have the negative shift. Hence the first sensitivity line holds. If \(G>4\sqrt a\), the rightmost root \(s_*=-R_*\) is simple, and \(F_+(s_*)=2b\), \(F_-'(s_*)=\sqrt{G^2/4-4a}\). Its positive root shift gives the third line. At \(G=4\sqrt a\), the critical low-mode factor is \((s+\sqrt a)^2\). Setting \(s=-\sqrt a+\delta s\) gives to leading order \(2b(\delta s)^2=ad^2\), so the rightmost root separates as \(\delta s=\sqrt{a/(2b)}|d|+O(d^2)\). This gives the second line and completes the proof.

## Verification
The accompanying standalone `check.py` reproduces six exact polynomial identities using symbolic algebra, compares 1,200 random constrained damping allocations with independently computed quartic roots, and checks eight small-imbalance asymptotic instances. Run `python3 check.py` with Python, NumPy, and SymPy installed. These finite checks are diagnostic; the all-parameter theorem and asymptotic laws are proven above.

## Relationship to prior work
Freitas and Lancaster studied optimizing the spectral abscissa over the **entire space of real symmetric damping matrices** for a given oscillator system. Their unrestricted matrix optimization, including its two-dimensional characterization, does not impose a constant total damping budget or diagonal, physically local damping. In fact their unrestricted best rate generally exceeds the \(\sqrt a\) limit of this constrained model. Ryu and coauthors studied exceptional points and transient optimization in coupled dissipative oscillators, analyzing a different parameter variation (including a model with damping concentrated in one oscillator); their investigated stability calculation does not establish the all-budget, unique equal-split optimum or the three-regime imbalance law. Krenk and Høgsberg optimize tuned-mass vibration absorption with damping in the relative coordinate, a distinct actuator and objective. Pavić treats spatial distribution of hysteretic damping and forced-response energy reduction, not this fixed-budget viscous spectral optimization.

## Limitations
This is a statement about identical masses, positive tether springs, positive coupling, two grounded viscous dampers, and linear autonomous evolution. It does not assert optimality for unequal masses, damping between rather than to ground, non-diagonal damping matrices, nonlinear damping, transient peak amplification, or finite-time response. The all-level rate at critical damping is a spectral exponent, not an unqualified uniform prefactor bound. Historical priority remains uncertain outside the compared sources, particularly regarding alternate mechanical-engineering formulations of constrained damping placement.

## References
1. P. Freitas and P. Lancaster, *On the Optimal Value of the Spectral Abscissa for a System of Linear Oscillators*, SIAM Journal on Matrix Analysis and Applications 21 (1999), 195–208. DOI: 10.1137/S0895479897331850. Author-uploaded full text: https://www.researchgate.net/publication/2671050_On_the_Optimal_Spectral_Abscissa_for_a_System_of_Linear_Oscillators .
2. J.-W. Ryu, W.-S. Son, D.-U. Hwang, S.-Y. Lee, and S. W. Kim, *Exceptional points in coupled dissipative dynamical systems*, Physical Review E 91 (2015), 052910. arXiv:1504.08085, first public 2015-04-30. https://arxiv.org/abs/1504.08085 .
3. S. Krenk and J. Høgsberg, *Tuned mass absorber on a flexible structure*, Journal of Sound and Vibration 333 (2014), 1577–1595. DOI: 10.1016/j.jsv.2013.11.029.
4. G. Pavić, *Analysis of Vibration Reduction by Damping Using Simple Analytical Modelling*, Shock and Vibration (2018), article 1098531. DOI: 10.1155/2018/1098531.
5. I. Nakić, *Minimization of the trace of the solution of Lyapunov equation connected with damped vibrational systems*, Mathematical Communications 18 (2013), 219–229. https://hrcak.srce.hr/101454 (abstract consulted; complete manuscript not inspected).
