# Direction-selective killing preserves exponential travel radius but creates lifetime ageing

## Finding

For a telegraph particle killed at velocity reversals with distinct killing probabilities \(p_+\) and \(p_-\), the terminal position has an asymmetric two-sided exponential density, but its **absolute travel displacement is exactly exponential and independent of the terminal displacement sign**. The full family has a sharp identifiable parameter envelope, whereas the killing time exhibits a strictly increasing hazard precisely when the two killing probabilities differ.

Let \(X_T\) be the position at the killing event, \(d=p_++p_--p_+p_-\), \(\delta=(p_+-p_-)/2\), and \(\kappa=\lambda\sqrt d/c\). Then
\[
 f_{X_T}(x)=\frac{\lambda}{2c}\bigl(\sqrt d+\delta\operatorname{sgn}(x)\bigr)e^{-\kappa|x|},\qquad x\ne0.
\]
There is no atom at zero. With \(R=|X_T|\) and \(S=\operatorname{sgn}(X_T)\),
\[
 R\sim\operatorname{Exp}(\kappa),\qquad
 R\perp S,\qquad
 \Pr(S=+1)=s=\frac12+\frac{p_+-p_-}{4\sqrt d}.
\]
For fixed, known \(\lambda,c>0\), the attainable pairs \((\kappa,s)\) are *exactly*
\[
 0<\kappa<\lambda/c,\qquad
 \left|s-\frac12\right|<\frac{c\kappa}{4\lambda}.
\]
Each pair in this open envelope uniquely determines the two killing probabilities: put \(d=(c\kappa/\lambda)^2\), \(\delta=2\sqrt d(s-1/2)\), and \(m=1-\sqrt{1-d+\delta^2}\); then \(p_+=m+\delta\) and \(p_-=m-\delta\). The inequalities in the envelope are sharp as an individual killing probability approaches zero.

Writing \(r=\sqrt{(1-p_+)(1-p_-)}\) and \(A=(2-p_+-p_-)/(2r)\), the survival function of the killing time is
\[
 \Pr(T>t)=e^{-\lambda t}\left[\cosh(\lambda rt)+A\sinh(\lambda rt)\right],\qquad t\ge0.
\]
Its hazard \(h(t)=-\frac{d}{dt}\log\Pr(T>t)\) obeys
\[
 h'(t)=\frac{\lambda^2(p_+-p_-)^2}{4[\cosh(\lambda rt)+A\sinh(\lambda rt)]^2}.
\]
Thus \(h\) is strictly increasing for \(p_+\ne p_-\), whereas \(T\sim\operatorname{Exp}(\lambda p)\) when \(p_+=p_-=p\). In the asymmetric case \(h(0)=\lambda(p_++p_-)/2\) and \(h(t)\to\lambda(1-r)\).

## Assumptions and scope

A particle starts at \(X_0=0\). Independently of subsequent randomness, its initial velocity is uniformly distributed between \(+c\) and \(-c\), with fixed \(c>0\). A homogeneous Poisson process of rate \(\lambda>0\) generates potential turning events. When an event occurs while the pre-event velocity is \(+c\), killing occurs with fixed probability \(p_+\in(0,1)\); when it is \(-c\), the probability is \(p_-\in(0,1)\). Conditional on no killing, the velocity reverses. Successive event marks are conditionally independent given their incoming velocities; the Poisson clock and initial velocity are independent. The particle is stationary after killing. All assertions concern the finite killing time \(T\), the pre-killing trajectory, and its terminal location \(X_T\). By a lower bound on the killing probability per Poisson event, \(T<\infty\) almost surely.

## Proof

**Terminal resolvent.** Let \(q_+=1-p_+\), \(q_-=1-p_-\), \(\pi=(1/2,1/2)\), and define the transient orientation generator and killing-rate vector
\[
 Q=\lambda\begin{pmatrix}-1&q_+\\q_-&-1\end{pmatrix},\quad
 V=\begin{pmatrix}c&0\\0&-c\end{pmatrix},\quad
 b=\lambda\begin{pmatrix}p_+\\p_-\end{pmatrix}.
\]
Conditional on the current orientation, the Fourier transform of the terminal displacement follows the first-step equations of a killed two-state velocity process. Equivalently the killed Markov-additive resolvent yields, for every real \(k\),
\[
 \phi(k)=\mathbb E(e^{ikX_T})=\pi(-Q-ikV)^{-1}b
 =\frac{\lambda^2d+ikc\lambda\delta}{\lambda^2d+c^2k^2}.
\]
Here the denominator has determinant \(\lambda^2[1-q_+q_-]+c^2k^2=\lambda^2d+c^2k^2\). The numerator follows by expanding the two-by-two inverse and summing its entries against the unbiased initial direction. Since \(d>0\), this transform determines a unique probability law. Direct Fourier integration of the claimed positive density gives
\[
 \frac{\lambda}{2c}\left(\frac{\sqrt d+\delta}{\kappa-ik}+\frac{\sqrt d-\delta}{\kappa+ik}\right)
 =\frac{\lambda^2d+ikc\lambda\delta}{\lambda^2d+c^2k^2}.
\]
The coefficients are strictly positive because \(|p_+-p_-|<d\), shown below. The density integrates to one, so there is no additional atomic component. On each half-line its conditional radius density is \(\kappa e^{-\kappa u}\,du\) for \(u>0\), independent of the half-line. This proves independence of \(R\) and \(S\) and the asserted expression for \(s\).

**Sharp inverse envelope.** If \(p_+\ge p_-\), then
\[
 d-(p_+-p_-)=p_-(2-p_+)>0.
\]
The other ordering is symmetric. Therefore \(|\delta|<d/2\), which becomes the displayed bound on \(s\). Conversely, fix \(0<d<1\) and \(|\delta|<d/2\). Set \(m=1-\sqrt{1-d+\delta^2}\). The quadratic identity \(d=2m-m^2+\delta^2\) holds. Moreover \(m>|\delta|\): squaring the equivalent positive inequality \(\sqrt{1-d+\delta^2}<1-|\delta|\) reduces it to \(d>2|\delta|\). Also \(m+|\delta|<1\) because \(\sqrt{1-d+\delta^2}>|\delta|\), as \(d<1\). Hence \(p_\pm=m\pm\delta\in(0,1)\), with exactly the prescribed \((d,\delta)\). Any solution for the mean probability \(m\) must solve the same quadratic; its other root exceeds one, proving uniqueness. Boundary points are limits of admissible models with a vanishing killing probability.

**Lifetime.** The orientation substochastic semigroup before killing is \(e^{Qt}\). With \(B=\bigl(\begin{smallmatrix}0&q_+\\q_-&0\end{smallmatrix}\bigr)\) one has \(B^2=r^2I\), whence
\[
 e^{Qt}=e^{-\lambda t}\left[\cosh(\lambda rt)I+\frac{\sinh(\lambda rt)}rB\right].
\]
Multiplying by \(\pi\) on the left and the all-ones vector on the right yields the stated survival function. Put \(H(z)=\cosh z+A\sinh z\), \(z=\lambda rt\). Then
\[
 h(t)=\lambda-\lambda r\frac{H'(z)}{H(z)},\qquad
 h'(t)=\lambda^2r^2\frac{A^2-1}{H(z)^2}
 =\frac{\lambda^2(q_+-q_-)^2}{4H(z)^2}.
\]
The last equality uses \(4r^2(A^2-1)=(q_+-q_-)^2=(p_+-p_-)^2\). This is positive exactly when the killing probabilities differ. The initial value and limiting value follow by evaluating at \(t=0\) and by \(H'(z)/H(z)\to1\). For equal probabilities \(A=1\), the survival function reduces to \(e^{-\lambda pt}\); the terminal density simultaneously becomes the symmetric Laplace law previously derived in the source article.

## Verification

The supplied standalone `verify.py` reproduces the two-state resolvent and inverse Fourier representation, compares the hyperbolic survival formula with independent matrix exponentials, checks the hazard derivative numerically, confirms the inverse envelope throughout a two-dimensional grid, and independently simulates 180,000 killed trajectories. It prints its comparison count and observed versus predicted terminal-direction and radius statistics. Its tests support the algebra but do not replace the proof. Reproduction: install Python 3 with NumPy and SciPy, then run `python verify.py` from the extracted package. All formulas above hold without numerical approximations.

## Relationship to prior work

Orsingher and Marchione [1] introduced killing at direction-change events for a symmetric telegraph process and proved the terminal position has a Laplace law when the killing probability is the same in both orientations; they also derived exponential killing time and explicit pre-killing distributions. Those are prior results, and are recovered here only as the special case \(p_+=p_-\). Our question concerns **different mortality at rightward and leftward events**: Poisson independent thinning at one common killing rate no longer applies. The density, sharp inverse characterization, sign-radius independence, and increasing-hazard criterion are assessed together for this extension. Earlier Markov-modulated telegraph and jump-telegraph frameworks, including Ratanov [2] and Ratanov and Kolesnik [3], supply general modeling tools. The underlying two-by-two matrix-resolvent technique is standard and is not claimed as new. The 2022 chapter [3] was accessible only at abstract/contents level, leaving a genuine risk of implicit broader coverage; no novelty conclusion is based on an inaccessible full text.

## Limitations

The model requires a two-state fixed-speed Markov velocity, a homogeneous Poisson event process, position-independent orientation-dependent killing probabilities, unbiased initialization, and strictly interior probabilities. More general directional dependence, spatially varying hazards, nonexponential run durations, and joint location-lifetime distributions are not classified. An external independent novelty or mathematical audit has not been carried out; broader Markov-additive potential theory might implicitly imply some formulas. Numerical simulations verify finite samples, not infinite laws.

## References

[1] E. Orsingher and M. M. Marchione, *Killing random motions with finite velocity*, arXiv:2610.15094v1, publicly available October 10, 2026. https://arxiv.org/abs/2610.15094

[2] N. Ratanov, *Damped jump-telegraph processes*, arXiv:1303.2796v1, 2013. https://arxiv.org/abs/1303.2796

[3] N. Ratanov and A. Kolesnik, *Asymmetric Jump-Telegraph Processes*, 2022. https://doi.org/10.1007/978-3-662-65827-7_3
