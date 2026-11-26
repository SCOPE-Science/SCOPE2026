# Direction-selective killing preserves exponential displacement magnitude but creates lifetime ageing

## Finding

In the telegraph model below, the terminal position has a two-sided exponential density with the same decay rate on both sides. Its sign and absolute displacement are independent, even when the probabilities of killing at events approached from the rightward and leftward directions differ.

Let \(d=p_++p_--p_+p_-\), \(\delta=(p_+-p_-)/2\), and \(\kappa=\lambda\sqrt d/c\). The terminal position has no atom and has density
\[
f_{X_T}(x)=\frac{\lambda}{2c}\bigl(\sqrt d+\delta\operatorname{sgn}(x)\bigr)e^{-\kappa|x|},\qquad x\ne0.
\]
In particular, \(R=|X_T|\) is exponential with rate \(\kappa\), independently of \(S=\operatorname{sgn}(X_T)\), and \(s=\Pr(S=+1)=1/2+\delta/(2\sqrt d)\). Here \(R\) is net displacement magnitude, not total distance travelled.

For fixed known \(\lambda,c>0\), the attainable pairs are exactly
\[
0<\kappa<\lambda/c,\qquad |s-1/2|<\frac{c\kappa}{4\lambda}.
\]
Each pair uniquely determines the two killing probabilities. Set \(d=(c\kappa/\lambda)^2\), \(\delta=2\sqrt d(s-1/2)\), and \(m=1-\sqrt{1-d+\delta^2}\); then \(p_\pm=m\pm\delta\). For \(0<\kappa<\lambda/c\), either sloping boundary is approached by letting one killing probability tend to zero and the other tend to \(d\). At the boundary \(\kappa=\lambda/c\), at least one probability tends to one in any convergent realization; every point of that boundary segment is approachable. At the vertex \((0,1/2)\), both probabilities tend to zero. These are boundary limits, not additional models in the stated parameter domain.

Write \(r=\sqrt{(1-p_+)(1-p_-)}\), \(A=(2-p_+-p_-)/(2r)\), and \(H(z)=\cosh z+A\sinh z\). For \(t\ge0\),
\[
\Pr(T>t)=e^{-\lambda t}H(\lambda rt),\qquad
h'(t)=\frac{\lambda^2(p_+-p_-)^2}{4H(\lambda rt)^2},
\]
where \(h(t)=-\frac{d}{dt}\log\Pr(T>t)\). Thus the hazard is strictly increasing for \(p_+\ne p_-\), with \(h(0)=\lambda(p_++p_-)/2\) and limit \(\lambda(1-r)\). If \(p_+=p_-=p\), then \(T\) is exponential with rate \(\lambda p\).

## Assumptions and scope

The particle starts at zero, with initial velocity independently uniform on \(\{+c,-c\}\), \(c>0\). A homogeneous Poisson process of rate \(\lambda>0\) generates events. At an event, with probability \(p_+\) or \(p_-\) according to the incoming velocity, the particle is killed and remains at its current position. If it survives, the velocity reverses. Event marks use the stated probabilities independently given the incoming states, and both probabilities are in \((0,1)\). The probability to survive \(j\) events is at most \((1-\min(p_+,p_-))^j\), so the killing time \(T\) is finite almost surely.

## Proof

**Terminal law.** Put \(q_\pm=1-p_\pm\). For real \(k\), write \(a_\pm=\lambda/(\lambda\mp ikc)\), the transforms of one signed run. The transforms \(g_\pm\) starting at the indicated velocities satisfy \(g_\pm=a_\pm(p_\pm+q_\pm g_\mp)\), by conditioning on the first event and its independent exponential waiting time. Solving gives
\[
g_+=\frac{a_+p_++a_+a_-q_+p_-}{1-a_+a_-q_+q_-},\qquad
g_-=\frac{a_-p_-+a_+a_-q_-p_+}{1-a_+a_-q_+q_-}.
\]
Hence
\[
\frac{g_++g_-}{2}=\frac{\lambda^2d+ikc\lambda\delta}{\lambda^2d+c^2k^2}.
\]
The two half-line integrals of the stated density yield the same transform: they are \(\lambda(\sqrt d+\delta)/(2c(\kappa-ik))\) and \(\lambda(\sqrt d-\delta)/(2c(\kappa+ik))\). The coefficients are positive by \(|\delta|<d/2\) and \(0<d<1\), shown below. The density integrates to one, so uniqueness of the characteristic function proves the full law with no atom. On each half-line the conditional magnitude has the same exponential density \(\kappa e^{-\kappa u}\) for \(u>0\); integration gives the stated sign mass.

**Envelope.** Since \(d=1-q_+q_-\), \(0<d<1\). If \(p_+\ge p_-\), then \(d-(p_+-p_-)=p_-(2-p_+)>0\), with the analogous identity after interchanging signs. Thus \(2|\delta|<d\). Conversely, for \(0<d<1\) and \(2|\delta|<d\), the proposed \(m\) satisfies \(d=2m-m^2+\delta^2\). The inequality \(m>|\delta|\) follows from \(1-d+\delta^2<(1-|\delta|)^2\), and \(m+|\delta|<1\) follows from \(1-d+\delta^2>\delta^2\). This gives two interior probabilities. The other quadratic root for \(m\) exceeds one, so the inverse is unique.

At \(2|\delta|=d\), \(0<d<1\), the same inverse gives \(m=|\delta|\), hence the probabilities are \(d\) and zero in the appropriate order. At \(d=1\), the inverse is \(m=1-|\delta|\) for \(|\delta|\le 1/2\), giving probabilities \(1\) and \(1-2|\delta|\) in the appropriate order. Approximating these probability pairs by interior pairs proves sharpness there. Finally, \(d\ge\max(p_+,p_-)\) and the sign bound give the vertex limit at \(d=0\).

**Lifetime.** Conditional on \(2j\) events by time \(t\), survival through them has probability \((q_+q_-)^j\); conditional on \(2j+1\), multiply this by \((q_++q_-)/2\). Summing the Poisson probabilities separately for even and odd event counts gives \(e^{-\lambda t}H(\lambda rt)\). Since \(H''=H\) and \((H')^2-H^2=A^2-1\), differentiation gives
\[
h(t)=\lambda-\lambda r\frac{H'(\lambda rt)}{H(\lambda rt)},\qquad
h'(t)=\lambda^2r^2\frac{A^2-1}{H(\lambda rt)^2}.
\]
The identity \(4r^2(A^2-1)=(q_+-q_-)^2\) proves the criterion. The endpoints of the hazard follow from \(H'(0)=A\) and \(H'(z)/H(z)\to1\). For equal killing probabilities \(A=1\), so the survival function is exponential.

## Verification

The accompanying `verify.py` can be run with Python 3, NumPy and SciPy. It compares the characteristic function and the integrated half-line density with a matrix resolvent, compares survival with matrix exponentiation, and checks the hazard derivative and interior inverse on finite parameter grids. It also simulates 180,000 trajectories at one parameter tuple. These comparisons corroborate the interior formulas; the model-wide claims and the boundary limits follow from the proof, not from finite tests.

## Relationship to prior work and limitations

Orsingher and Marchione [1] derive the symmetric Laplace terminal law and exponential lifetime for equal event-killing probabilities. Those are recovered as the equal-probability case. Direction-modulated telegraph frameworks [2,3], resolvents, and finite-state survival representations are not new here. The specific conclusions are the common terminal decay and sign law under unequal probabilities, the sharp identifiable region for the distribution, and the precise lifetime ageing criterion in this model. The full text of [3] was not available for a decisive priority comparison; general potential or phase-type formulas may provide alternative derivations.

The result uses two fixed velocities of equal magnitude, a constant event rate, orientation-dependent but position-independent probabilities, and unbiased initialization. It makes no claim about unequal speed magnitudes, spatial variation, non-Poisson waiting times, or the joint law of lifetime and terminal position.

## References

1. E. Orsingher and M. M. Marchione, *Killing random motions with finite velocity*, arXiv:2610.15094v1, 2026-10-10. https://arxiv.org/abs/2610.15094
2. N. Ratanov, *Damped jump-telegraph processes*, arXiv:1303.2796, 2013. https://arxiv.org/abs/1303.2796
3. N. Ratanov and A. Kolesnik, *Asymmetric Jump-Telegraph Processes*, 2022. https://doi.org/10.1007/978-3-662-65827-7_3
