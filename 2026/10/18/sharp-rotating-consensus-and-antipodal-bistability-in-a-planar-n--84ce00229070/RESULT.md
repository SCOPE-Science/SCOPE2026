# Sharp rotating-consensus and antipodal bistability in a planar normalized two-agent map

## Finding
Consider the exactly normalized, discrete two-agent, uniform-interaction map on the unit circle
\[
T(x,y)=\left(\frac{x+\eta c(x+y)/2}{|x+\eta c(x+y)/2|},\frac{y+\eta c(x+y)/2}{|y+\eta c(x+y)/2|}\right),\qquad c=a+ib,
\]
where \(x,y\in S^1\subset\mathbb C\), \(\eta>0\), \(a,b\in\mathbb R\), and \(L=1+\eta a>0\). Write \(h=\eta b\) and \(K=L^2+h^2\). The diagonal \(\mathcal C=\{(x,x):x\in S^1\}\) is a rigid rotating circle, with angular increment \(\omega=\arctan(h/L)\). The antipodal circle \(\mathcal A=\{(x,-x):x\in S^1\}\) is pointwise fixed.

Every initial pair off \(\mathcal A\) admits unique midpoint and half-separation coordinates
\[
x=e^{i(\phi+\delta)},\quad y=e^{i(\phi-\delta)},\quad -\pi/2<\delta<\pi/2,\qquad t=\tan\delta\in\mathbb R.
\]
Their exact update is
\[
\begin{aligned}
\delta^+&=\tfrac12\!\left[\arctan\frac{h+t}{L}-\arctan\frac{h-t}{L}\right],\\
\phi^+-\phi&=\tfrac12\!\left[\arctan\frac{h+t}{L}+\arctan\frac{h-t}{L}\right].
\end{aligned}
\]
The following is the complete relative-phase portrait, including all parameter boundaries:

1. If \(L>1\), or if \(L=1\) and \(h\ne0\), every nonantipodal pair approaches \(\mathcal C\) in separation; the rotating diagonal is transversely attracting. The antipodal circle is repelling (parabolically so at \(L=1\)).
2. If \(0<L<1\) and \(K\le L\), every pair outside \(\mathcal C\) approaches a point of \(\mathcal A\); the diagonal is unstable, including the nonhyperbolic boundary \(K=L\).
3. If \(0<L<1\) and \(K>L\), there are exactly two additional invariant circles of constant half-separation \(\delta=\pm\arctan t_*\), where
\[
t_*=\sqrt{\frac{K-L}{1-L}}.
\]
They each carry rigid rotation at the explicit increment
\[
\omega_*=\frac12\left[\arctan\frac{h+t_*}{L}+\arctan\frac{h-t_*}{L}\right].
\]
Both are transverse basin separators: \(|t_0|<t_*\) converges in separation to rotating consensus, while \(|t_0|>t_*\) converges to an antipodal fixed pair. Equality \(|t_0|=t_*\) stays on the relevant rotating separator. Both limiting sets have open basins.
4. If \(L=1\) and \(h=0\), the map is the identity.

At the marginal repulsion boundary \(L=1\), \(h\ne0\), the escaping time from near-antipodal initial data is sharp: for every fixed \(T>0\), with \(N_T(t_0)=\min\{n\ge0:|t_n|\le T\}\),
\[
\lim_{|t_0|\to\infty}\frac{N_T(t_0)}{t_0^2}=\frac{1}{2h^2},\qquad
\lim_{\epsilon_0\downarrow0}\epsilon_0^2N_T(t_0)=\frac{1}{2h^2},
\]
where \(\epsilon_0=\pi/2-|\delta_0|=\arctan(1/|t_0|)\). At every parameter with convergence to the diagonal, the shared phase satisfies \(\phi_n-n\omega\to\phi_\infty\) modulo \(2\pi\). At every parameter with convergence to the antipodal set, \(\phi_n\) converges modulo \(2\pi\).

## Assumptions and scope
The state space is exactly \((S^1)^2\), each state has Euclidean length one, attention weights are equal and constant, and the value operator in real coordinates is \(aI+bJ\), where \(J(u,v)=(-v,u)\). The update has a residual connection and exact Euclidean renormalization. The restriction \(L>0\) ensures denominators never vanish: away from \(\mathcal A\), divide the unnormalized complex updates by \(e^{i\phi}\cos\delta\) to obtain \(L+i(h\pm t)\), both with positive real part; on \(\mathcal A\) the numerator equals the original nonzero point. The claim includes all \(a,b\) obeying \(1+\eta a>0\), not arbitrary value matrices, attention kernels, or more than two agents.

## Proof
**Exact reduction.** For a nonantipodal pair, \((x+y)/2=e^{i\phi}\cos\delta\). Since \(x=e^{i\phi}(\cos\delta+i\sin\delta)\), the first numerator equals
\[
e^{i\phi}\cos\delta\big(L+i(h+t)\big),
\]
and the second equals \(e^{i\phi}\cos\delta\big(L+i(h-t)\big)\). Their arguments give the two displayed angular recurrences, showing that the nonantipodal region is forward invariant, the sign of \(\delta\) is preserved, and \(0<|\delta^+|<\pi/2\) for nonzero \(\delta\). When \(\delta=0\), the same equations give a rigid rotation by \(\omega\); on the antipodal set the shared influence vanishes, giving pointwise fixation.

**Exact monotonicity and separator.** It suffices to consider \(t>0\) since the separation recurrence is odd. Twice the updated separation is the argument in \((0,\pi)\) of
\[
\big(L+i(h+t)\big)\big(L-i(h-t)\big)=K-t^2+2iLt,
\]
whereas twice the original separation is the argument of \((1+it)^2=1-t^2+2it\). The oriented cross-product of these two plane vectors (old then new) is
\[
(1-t^2)(2Lt)-(2t)(K-t^2)=2t\big[(L-K)+(1-L)t^2\big].
\]
Because both angles lie strictly between zero and \(\pi\), their signed difference lies in \((-\pi,\pi)\); hence its sine and the angle difference have the same sign. Since tangent is strictly increasing on \((0,\pi/2)\),
\[
\operatorname{sgn}(t^+-t)=\operatorname{sgn}\big((L-K)+(1-L)t^2\big),\qquad t>0.
\]
This sign identity is exact; there are no hidden circle-wrapping branches. If \(L>1\), then \(K\ge L^2>L\), so the expression is negative. If \(L=1\), it equals \(-h^2\). If \(0<L<1\), it is positive for all \(t>0\) when \(K\le L\), and otherwise changes from negative to positive at the unique positive zero \(t_*\). The recurrence is continuous and strictly increasing in positive separation, since
\[
\frac{d\delta^+}{dt}=\frac L2\left[\frac1{L^2+(h+t)^2}+\frac1{L^2+(h-t)^2}\right]>0.
\]
It fixes \(t_*\) when present. Strictly monotone bounded iterates must converge to fixed points; the above sign identity lists all fixed points on the finite \(t\)-axis. Thus every claimed basin limit follows, including all boundary cases. In the mixed case, the two circles \(t=\pm t_*\) are invariant with constant midpoint advance \(\omega_*\), and repel adjacent separation trajectories in both directions.

**Rates and full-state convergence.** The derivative of the induced \(t\)-map at zero is \(L/K\). At large positive \(t\), write \(\epsilon=\arctan(1/t)\), the distance in half-angle from antipodality. Taylor expansion of the angular formula gives \(\epsilon^+=L\epsilon+O(\epsilon^3)\). Thus whenever the diagonal attracts it does so exponentially once the orbit enters a small neighborhood (the special identity case excluded), and whenever \(L<1\) the antipodal circle attracts exponentially in half-angle. Moreover the midpoint increment is \(\omega+O(t^2)\) as \(t\to0\) and is \(O(t^{-2})\) as \(|t|\to\infty\), uniformly at each fixed parameter. These errors are summable along the exponentially convergent ends of each orbit. Consequently diagonal-bound orbits asymptotically track a unique rigidly rotating trajectory, while antipodal-bound orbits converge to a unique point.

**Sharp parabolic escape.** Set \(L=1\) and \(h\ne0\). Expanding the arctangents as \(|t|\to\infty\) gives
\[
t^+=t-\frac{h^2}{t}+O(t^{-3}),\qquad
(t^+)^2=t^2-2h^2+O(t^{-2}).
\]
For large positive \(t\), this square-decrement is arbitrarily close to \(2h^2\), and the positive orbit decreases to zero. For each sufficiently large fixed \(B>T\), telescope the inequalities \(2h^2-\varepsilon\le t_n^2-t_{n+1}^2\le2h^2+\varepsilon\) until the first entry into \((0,B]\). The remaining number of steps needed to cross the fixed \(T\) is bounded independently of the initial \(t_0\) (strict descent and continuity on the compact interval \([T,B]\)); the overshoot contributes at most a bounded square error. Dividing by \(t_0^2\), then sending \(t_0\to\infty\), \(B\to\infty\), and \(\varepsilon\to0\), yields the claimed constant. Oddness gives negative initial separations. Finally \(\epsilon_0t_0\to1\) as \(|t_0|\to\infty\).

## Verification
The standalone script `verify.py` uses a direct complex-vector implementation independent of the half-angle formulas. It checks 10,000 random parameter/phase states against the derived map, monotonicity signs, invariant separator values, representative parameter regimes, the parabolic square-decrement coefficient, and the zero-skew identity case. Execute `python3 verify.py`. It reports `CHECK_OK finite_diagnostics=20057`. This is numerical diagnostic evidence; the global classifications and infinite-time limits are established by the analytic proof above rather than by finite tests.

## Relationship to prior work
Altafini [1], §§II–III, formulates precisely the residual, renormalized uniform-attention map and analyzes it assuming a symmetric value matrix with a simple positive dominant real eigenvalue; the present rotational value map has a nonreal conjugate eigenpair when \(b\ne0\), and its rotating invariant circles and sharp basin boundary are not implications of that assumption. Tomihari–Karakida [2], §§3 and 5.2, analyze Jacobian effects of normalization, including suppression of oscillatory eigenvalues, without a global two-agent phase portrait. Gao–Yang–Chen [3], §V.1, discuss rotating invariant value planes and the angle of rotating consensus clusters, but explicitly leave nonlinear stability regions and attraction-basin questions open for that broader model. Uniform-attention dynamics are a special, mathematically tractable subcase; the present threshold \(h^2=L(1-L)\), separating circles, and sharp \(L=1\) escape coefficient are the additional claims. Existing general theory of monotone circle maps and of parabolic fixed points is a plausible source of equivalent formulations or consequences; no claim of a new general method is made.

## Limitations
No conclusion is asserted for \(L\le0\), where normalization or angular branches may change, for state-dependent softmax attention, for more than two agents, or for dimensions above two. The separating invariant circles may support irrational rigid rotations rather than periodic trajectories; convergence is transverse toward the indicated circles, not necessarily to a fixed state. The original source's related classification of symmetric value matrices and the known generic theory of one-dimensional monotone maps are prior knowledge, not novel ingredients. Independent mathematical checking and a comprehensive historic-literature exhaustiveness search remain outstanding.

## References
[1] C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first submitted 2026-10-09), §§II–III and §V-C. https://arxiv.org/abs/2610.13518 .

[2] A. Tomihari and R. Karakida, *Recurrent Self-Attention Dynamics: An Energy-Agnostic Perspective from Jacobians*, arXiv:2505.19458v4, §§3, 5.2. https://arxiv.org/abs/2505.19458 .

[3] Q. Gao, Z. Yang and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1, §V.1, especially the orthogonal value-map discussion. https://arxiv.org/abs/2609.28448 .
