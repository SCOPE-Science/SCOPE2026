# Harmonic event-time asymptotics at a safety barrier

## Finding

Consider the two-dimensional sample-and-hold counterexample in which the safe-set function is \(h(x)=1-\|x\|_2^2\), the held gain at event \(t_i\) is \(k_i=h_i/2\), and \(h_i=h(x(t_i))\). Let \(\rho>1\), \(0<\sigma<1\), and trigger the next event at the first positive time \(\tau_i=t_{i+1}-t_i\) satisfying

\[
2\rho^3\,\|x(t_i)-x(t_i+\tau_i)\|_2=\sigma h(x(t_i+\tau_i)).
\]

For every nonzero initial state with \(0<h_0<1\), the resulting event sequence has the exact asymptotic laws

\[
h_i\sim\frac{2\rho^3}{\sigma i},\qquad \tau_i\sim\frac1i,\qquad t_i\sim\log i.
\]

Consequently, if \(N(t)=\max\{i:t_i\le t\}\), then \(\log N(t)/t\to1\). Thus this specific safe trajectory has no positive minimum inter-event time, but it also has no finite-time accumulation of events: the event count grows exponentially on the logarithmic scale. The leading coefficient in \(\tau_i\sim1/i\) is independent of \(\rho\) and \(\sigma\).

## Assumptions and scope

The plant and controller are exactly those of the two-state counterexample in Taylor, Ong, Cortés, and Ames, *Safety-Critical Event Triggered Control via Input-to-State Safe Barrier Functions*. Write

\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad h(x)=1-\|x\|_2^2,\qquad k(x)=\tfrac12h(x).
\]

Between events the controller is held at \(k(x(t_i))\), so the state satisfies \(\dot x=(k_i I+J)x\) on \([t_i,t_{i+1})\). The trigger is the equation above, with the state remaining in the interior of the unit disk before each event. The initial condition is nonzero and strictly interior, equivalently \(0<h_0<1\). The result is specific to this trigger and this counterexample; it is not a general rate theorem for all event-triggered controllers.

## Proof

Put \(x_i=x(t_i)\), \(h_i=1-\|x_i\|_2^2\), and \(E_i(\tau)=\|x_i-x(t_i+\tau)\|_2\). Since \(J^T=-J\) and \(J^2=-I\), the matrix \(R(\tau)=e^{J\tau}\) is orthogonal. The exact held-input flow is therefore

\[
x(t_i+\tau)=e^{h_i\tau/2}R(\tau)x_i,
\]

which gives the exact identities

\[
h(t_i+\tau)=1-(1-h_i)e^{h_i\tau}
\]

and

\[
E_i(\tau)^2=(1-h_i)\left[(e^{h_i\tau/2}-1)^2+4e^{h_i\tau/2}\sin^2(\tau/2)\right].
\]

The barrier first reaches zero at \(\tau_b=h_i^{-1}\log(1/(1-h_i))\). At \(\tau=0\), the trigger residual \(2\rho^3E_i(\tau)-\sigma h(t_i+\tau)\) is negative; at \(\tau_b\), it is positive because the state norm has increased from \(\sqrt{1-h_i}\) to \(1\). Thus a next trigger occurs before the barrier reaches zero.

The sequence \(h_i\) is positive and decreasing. To show \(h_i\to0\), suppose instead that \(h_i\to h_\infty>0\). Since \(h_i\le h_0<1\), the held-state speed is uniformly bounded, so \(E_i(\tau)\le \sqrt{5/4}\,\tau\). At a trigger, \(E_i(\tau_i)=\sigma h_{i+1}/(2\rho^3)\ge \sigma h_\infty/(2\rho^3)\); hence \(\tau_i\) is bounded below by a positive constant. Meanwhile, while \(h\ge0\),

\[
-\frac{d}{d\tau}h(t_i+\tau)=h_i(1-h(t_i+\tau))\ge h_\infty(1-h_0)>0.
\]

Every event would then decrease \(h_i\) by a fixed positive amount, contradicting convergence to \(h_\infty>0\). Therefore \(h_i\to0\).

Next, \(\tau_i\to0\). Indeed, for each fixed \(0<\delta<1\), the exact error formula gives \(E_i(\delta)\to2\sin(\delta/2)>0\), while \(h(t_i+\delta)\to0\). For sufficiently large \(i\), the trigger residual is positive at \(\delta\), so the first root occurs before \(\delta\). Since \(\delta\) is arbitrary, \(\tau_i\to0\).

The exact error formula now yields

\[
\frac{E_i(\tau_i)}{\tau_i}\to1,
\]

because the squared exponential increment divided by \(\tau_i^2\) vanishes as \(h_i\to0\), and \(4\sin^2(\tau_i/2)/\tau_i^2\to1\). The trigger equality then implies

\[
\frac{\tau_i}{h_{i+1}}\to c:=\frac{\sigma}{2\rho^3}.
\]

Also, the exact barrier identity gives

\[
h_i-h_{i+1}=(1-h_i)(e^{h_i\tau_i}-1)\sim h_i\tau_i,
\]

so \(h_{i+1}/h_i\to1\) and hence \(\tau_i/h_i\to c\). It follows that

\[
\frac1{h_{i+1}}-\frac1{h_i}
=\frac{h_i-h_{i+1}}{h_i h_{i+1}}\to c.
\]

Summing these increments (equivalently, applying Stolz–Cesàro) gives \(1/h_i\sim ci\), or \(h_i\sim1/(ci)=2\rho^3/(\sigma i)\). Substitution into \(\tau_i/h_i\to c\) gives \(\tau_i\sim1/i\). Finally, summing the inter-event intervals yields \(t_i\sim\sum_{j<i}1/j\sim\log i\); inversion of this monotone relation gives \(\log N(t)/t\to1\). Since \(\sum_i1/i\) diverges, the events do not accumulate in finite time.

## Verification

The standalone standard-library script `verify.py` evaluates the exact flow and trigger equations for 2,000 successive updates at one admissible parameter pair. It checks positivity and decrease of the barrier margin and the trigger residual at each computed root. These finite checks are corroborative only; the asymptotic laws are established by the proof above, not by numerical extrapolation.

## Relationship to prior work

Taylor, Ong, Cortés, and Ames introduced this exact two-dimensional example to show that a safety-preserving trigger may fail to have a positive minimum inter-event time. Their paper proves that the barrier margin tends to zero and that inter-event times are not uniformly bounded below, and it displays numerical inter-event times approaching zero. The present claim is narrower and quantitative: it derives the reciprocal-index asymptotic for the barrier margin and the inter-event intervals, and the resulting logarithmic event-time law. The exact held-flow and trigger equations are the same as in the source; the new step is the limit argument yielding the sharp leading rates.

## Limitations

The rates apply only to the stated two-dimensional counterexample, the specified trigger, and nonzero initial conditions with \(0<h_0<1\). They do not establish a uniform rate for other plants, barriers, trigger laws, or initial conditions. The finite script is not a proof of the limit statements. An exhaustive literature search is not claimed.

## References

1. A. J. Taylor, P. Ong, J. Cortés, and A. D. Ames, “Safety-Critical Event Triggered Control via Input-to-State Safe Barrier Functions,” arXiv:2003.06963 (first public version 2020-03-16); journal version, *IEEE Control Systems Letters* (2021), DOI: 10.1109/LCSYS.2020.3005101.
