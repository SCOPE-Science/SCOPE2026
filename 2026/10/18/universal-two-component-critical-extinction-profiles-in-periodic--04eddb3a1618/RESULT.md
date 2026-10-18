# Universal two-component critical extinction profiles in periodically forced cooperative Lotka–Volterra systems

## Finding
At the zero-invasion boundary for a two-species cooperative Lotka–Volterra system with periodic intrinsic growth rates, **every strictly positive forward trajectory shares the same leading periodic extinction and resident-correction profiles**. The decaying population is of order \(t^{-1}\), and the surviving population approaches its scalar periodic resident orbit from above at the same order, regardless of the initial positive densities.

Here is the exact statement. Let \(T>0\), and let \(a_1,a_2:\mathbb R\to\mathbb R\) be continuous \(T\)-periodic functions. Fix \(d_1,d_2,\sigma,\tau>0\), with \(d_1d_2>\sigma\tau\), and suppose
\[
\frac1T\int_0^T a_2(s)\,ds>0,\qquad
\int_0^T\left(a_1(s)+\frac{\sigma}{d_2}a_2(s)\right)ds=0.
\]
For the equations
\[
\dot x=x\bigl(a_1(t)-d_1x+\sigma y\bigr),\qquad
\dot y=y\bigl(a_2(t)+\tau x-d_2y\bigr),
\]
consider any initial state \(x(0)>0\), \(y(0)>0\). Let \(Y(t)>0\) be the unique \(T\)-periodic solution of \(\dot Y=Y(a_2(t)-d_2Y)\). Set
\[
p=\frac{\sigma}{d_2},\quad k=d_1-\frac{\sigma\tau}{d_2}>0,\quad
G(t)=\int_0^t\bigl(a_1(s)+p a_2(s)\bigr)\,ds,
\]
\[
Q(t)=e^{G(t)}Y(t)^{-p},\qquad I=\frac1T\int_0^TQ(s)\,ds,\qquad
f(t)=\frac{Q(t)}{kI}.
\]
Then \(G,Q,f\) are \(T\)-periodic and \(I>0\). Let \(H\) be the unique \(T\)-periodic solution of the linear equation
\[
H'(t)+d_2Y(t)H(t)=\tau f(t),\qquad Z(t)=Y(t)H(t).
\]
Both \(f\) and \(Z\) are strictly positive everywhere. As \(t\to\infty\), uniformly in the forcing phase,
\[
\boxed{\;x(t)=\frac{f(t)}{t}+O\!\left(\frac{\log t}{t^2}\right),\qquad
 y(t)=Y(t)+\frac{Z(t)}{t}+O\!\left(\frac{\log t}{t^2}\right).\;}
\]
The profiles are independent of the initial positive state; only the error constants can depend on it. Moreover the phase-averaged leading extinction coefficient is **independent of both seasonal growth-rate functions**:
\[
\frac1T\int_0^T f(s)\,ds=\frac1k,
\qquad
\lim_{t\to\infty}\frac{t}{T}\int_t^{t+T}x(s)\,ds=\frac1k.
\]
In particular, \(x(t)\to0\) and \(y(t)-Y(t)\to0\), and \(y(t)>Y(t)\) for every sufficiently large \(t\) along every strictly positive trajectory.

## Assumptions and scope
The growth rates are continuous, jointly \(T\)-periodic and otherwise arbitrary: they may change sign or have large seasonal variation. Both cross-interaction parameters are positive (cooperation), while \(d_1d_2>\sigma\tau\) is the standard weak-cooperation/diagonal-dissipativity condition. The time-independent interaction coefficients are essential to the exact cancellation used below. The equal-mean hypothesis is an exact codimension-one boundary, not a strict extinction hypothesis. All statements concern finite strictly positive initial data and forward time; no claim about a complete backward attractor classification is made.

For explicit reconstruction, put \(B(t)=\int_0^t a_2(s)\,ds\). The positive resident orbit is
\[
Y(t)=\frac{e^{B(t)}}{c+d_2\int_0^te^{B(s)}\,ds},\qquad
c=\frac{d_2\int_0^T e^{B(s)}\,ds}{e^{B(T)}-1}>0.
\]
The periodic correction also admits the positive, convergent representation
\[
H(t)=\tau\int_{-\infty}^t f(s)\exp\left(-d_2\int_s^tY(u)\,du\right)ds.
\]

## Proof
**1. Positive global trajectories with two-sided bounds for the resident species.** By the inequality \(d_1d_2>\sigma\tau\), choose a number \(r\) with \(\tau/d_2<r<d_1/\sigma\). For each positive initial state choose \(K\) large enough that the state belongs to \([0,K]\times[0,Kr]\) and
\[
K(d_1-\sigma r)>\sup a_1,\qquad K(d_2r-\tau)>\sup a_2.
\]
Increasing \(K\), if needed, makes the right-hand side point strictly inward on the upper and right edges of this rectangle. The coordinate axes are invariant. Standard ODE continuation therefore gives global positive solutions \(0<x(t)\le K\), \(0<y(t)\le Kr\). Since \(\tau x(t)\ge0\), scalar logistic comparison shows that \(y(t)\) dominates the solution of \(v'=v(a_2(t)-d_2v)\) from the same initial \(y(0)>0\). The reciprocal linear equation for \(1/v\), together with \(\int_0^T a_2>0\), shows that \(v(t)\to Y(t)\) exponentially. Consequently \(y(t)\) also has a strictly positive lower bound for \(t\ge0\).

**2. Exact cancellation at the boundary.** Define the strictly positive quantity
\[
W(t)=x(t)y(t)^p e^{-G(t)}.
\]
Direct logarithmic differentiation, using \(p d_2=\sigma\) and the mean-zero definition of \(G\), yields the **exact identity**
\[
\frac{W'(t)}{W(t)}=-kx(t),\qquad
\boxed{\;\frac{d}{dt}\frac1{W(t)}=k e^{G(t)}y(t)^{-p}.\;}
\]
The periodic function \(G\) is bounded; also \(y(t)\) is bounded above. Hence the last derivative has a strictly positive uniform lower bound. Thus \(W(t)=O((1+t)^{-1})\). Because \(y(t)\) is bounded below, \(x(t)=W(t)e^{G(t)}y(t)^{-p}=O((1+t)^{-1})\).

**3. Relaxation of the resident species.** Write \(h(t)=\log(y(t)/Y(t))\). Then
\[
h'(t)=\tau x(t)-d_2Y(t)\bigl(e^{h(t)}-1\bigr).
\]
The bounds from step 1 imply that \(h\) is bounded. As \(Y\) is bounded away from zero, the quotient \((e^h-1)/h\), continuously interpreted as \(1\) at \(h=0\), has a strictly positive uniform lower bound. Thus the preceding equation is a scalar uniformly dissipative linear equation with a coefficient depending on \(h\), driven by \(O((1+t)^{-1})\). Variation of constants gives \(h(t)=O((1+t)^{-1})\), and hence \(y(t)-Y(t)=O((1+t)^{-1})\).

**4. Universal first profile and a logarithmic error.** The exact inverse equation in step 2 now gives
\[
\frac1{W(t)}=\frac1{W(0)}+k\int_0^t e^{G(s)}y(s)^{-p}\,ds
=\frac1{W(0)}+k\int_0^tQ(s)\,ds+O(\log(2+t)).
\]
Here \(e^G y^{-p}-Q=O((1+t)^{-1})\) by step 3. Since \(Q\) is periodic with positive mean \(I\), its primitive is \(It+O(1)\). It follows that
\[
W(t)=\frac1{kIt}+O\!\left(\frac{\log t}{t^2}\right),\quad
x(t)=\frac{Q(t)}{kIt}+O\!\left(\frac{\log t}{t^2}\right).
\]
This proves the claimed profile \(f\) and its independence of initial data.

**5. Universal resident correction.** Because the positive periodic coefficient \(d_2Y(t)\) has a strictly contracting scalar evolution, the equation \(H'+d_2YH=\tau f\) has a unique periodic solution. Its positive past-integral representation above proves \(H(t)>0\). From step 3 and the first-profile estimate,
\[
h'(t)+d_2Y(t)h(t)=\frac{\tau f(t)}{t}
+O\!\left(\frac{\log t}{t^2}\right).
\]
Subtract the derivative identity for \(H(t)/t\). The difference \(e(t)=h(t)-H(t)/t\) solves
\[
e'(t)+d_2Y(t)e(t)=O\!\left(\frac{\log t}{t^2}\right).
\]
Variation of constants against a uniformly exponentially decaying kernel yields \(e(t)=O((\log t)/t^2)\). Expanding \(y=Y e^h\) proves
\[
y(t)=Y(t)+\frac{Y(t)H(t)}{t}
+O\!\left(\frac{\log t}{t^2}\right),
\]
with positive \(Z=YH\), so the eventual strict inequality follows.

**6. Seasonal mean.** Since \(f=Q/(kI)\), its average over a full period is exactly \(1/k\). Average the first asymptotic over a fixed subsequent period \([t,t+T]\) and use \(t/s\to1\) uniformly for \(s\) in this interval. This yields the second claimed limit. Every error estimate uses only the hypotheses above.

## Verification
The crucial identity is algebraic: after differentiating \(\log x+p\log y-G\), the coefficient of \(y\) is \(\sigma-pd_2=0\), the coefficient of \(x\) is \(-d_1+p\tau=-k\), and the remaining growth term cancels against \(G'\). Positivity and logarithmic remainders are proved analytically, not inferred from finite simulation.

The accompanying standalone `check.py` uses only the Python standard library. With \((d_1,d_2,\sigma,\tau)=(2,3,4/5,11/10)\), periodic growth rates \(a_2(t)=1.4+0.5\cos t+0.3\sin(2t)\) and \(a_1(t)=-(4/15)(1.4)+0.6\sin t-0.25\cos(2t)\), it verifies the cancellation with exact rational arithmetic, constructs the scalar resident orbit and both predicted periodic profiles, and compares two positive initial states after \(320\) forcing cycles. Its integration tests illustrate the stated asymptotics; they do not replace the proof. Reproduce by running `python3 check.py` in a directory containing the embedded file.

## Relationship to prior work
Garcia-Fuentes, Kalita, and Langa (2024) describe forward attractor structures under strict periodic average inequalities. In their §4.4, they explicitly leave the cooperative boundary with non-strict inequalities unresolved. The present result addresses the equality \(\langle a_1\rangle=(b_{12}/b_{22})\langle a_2\rangle\), in their sign convention \(b_{12}=-\sigma\), for positive forward trajectories: extinction, both exact first asymptotic profiles, and a universal mean coefficient. It does **not** establish their wider backward/complete-attractor classification.

Garcia-Fuentes, Kalita, Langa, and Suárez (arXiv:2301.04955; first public 12 January 2023) address cooperative forward attractors under strict extinction conditions; their §6.2 contains a positive gap parameter. At the present exactly zero invasion exponent that gap vanishes, so its exponential-attraction statement does not supply the algebraic asymptotic profiles here. Tineo (2005) treats the *competitive* sign structure; its critical-boundary conclusions are not a theorem for cooperative cross-interactions. No exact implication from these inspected results to the displayed two-component periodic profile was identified.

## Limitations
The conclusion is for strictly positive forward trajectories, fixed interaction parameters, and periodic continuous growth rates with positive resident average. It does not prove the full geometry of bounded complete solutions, a backward attractor classification, any stochastic/noisy extension, or analogous conclusions with time-dependent cross-interaction coefficients. The observed logarithmic error is an upper bound, not a claimed optimal rate. Mathematical priority is based on the sources materially inspected and targeted searches, not on an exhaustive literature census; overlapping work outside those sources remains possible. Independent validation has not been performed.

## References
1. J. Garcia-Fuentes, P. Kalita, and J. A. Langa, *Forwards Attractor Structures in a Planar Cooperative Non-autonomous Lotka–Volterra System*, Qualitative Theory of Dynamical Systems **23**, article 163 (2024), DOI: 10.1007/s12346-024-01020-0; first journal publication 12 April 2024. Especially §§2, 4.2, and 4.4.
2. J. Garcia-Fuentes, J. A. Langa, P. Kalita, and A. Suárez, *Forwards attractors for non-autonomous Lotka–Volterra cooperative systems: a detailed geometrical description*, arXiv:2301.04955, first posted 12 January 2023, especially §§4.4, 6.2.
3. A. Tineo, *Necessary and sufficient conditions for extinction of one species*, Advanced Nonlinear Studies **5** (2005), 57–71, DOI: 10.1515/ans-2005-0105; competitive-system comparison (abstract available).
