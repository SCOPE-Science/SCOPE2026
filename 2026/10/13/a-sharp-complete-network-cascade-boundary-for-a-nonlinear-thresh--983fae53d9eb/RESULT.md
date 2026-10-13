# A sharp complete-network cascade boundary for a nonlinear threshold relaxation

## Finding

**Theorem (exact one-seed cascade boundary and tied-threshold clock).** Let \(n\ge 2\) be an integer and \(0<\gamma<1/(4n^2)\). For the homogeneous, unit-weight complete graph on \(n\) vertices, consider the persistent linear threshold model (LTM) with strict activation condition \(\sum_{j\ne i}\zeta_j>\tau\), together with the nonlinear opinion dynamics (NOD) relaxation defined below. Start both dynamics with exactly one active agent. Set
\[
\tau_c(\gamma,n)=\left(1+\frac{n-2}{2}\sqrt\gamma\right)^2.
\]
For every \(0<\tau<1/(4\gamma)\), the NOD relaxation has a full cascade, meaning all agents tend to opinion \(1\), **if and only if** \(\tau<\tau_c(\gamma,n)\). At equality its unseeded opinions tend to \(\sqrt\gamma<1\) algebraically; above equality they tend to the positive value \(r_-<\sqrt\gamma\) given below. The strict LTM has a full cascade if and only if \(\tau<1\). Accordingly, the exact interval of different cascade sets is
\[
1\le\tau<\tau_c(\gamma,n).
\]
This interval is nonempty exactly when \(n\ge3\). In particular, at the exact LTM tie \(\tau=1\), every \(n\ge3\) has an NOD full cascade for arbitrarily small positive \(\gamma\). With \(n\ge3\) fixed, the first time \(T_{1/2}\) that an unseeded opinion reaches \(1/2\) satisfies
\[
T_{1/2}(\gamma,n)\sim\frac{\pi}{\sqrt{n-2}}\gamma^{-3/4}
\qquad(\gamma\downarrow0).
\]

## Assumptions and scope

Let \(A\) be the adjacency matrix with \(A_{ii}=0\), \(A_{ij}=1\) for distinct vertices; no normalization by degree is applied. Every vertex has the same positive threshold \(\tau\). In the source's LTM, each binary state persists once active, and an inactive vertex activates only when its integer neighbor sum is **strictly greater** than \(\tau\). In the source's NOD relaxation use \(k=1\), zero external bias, and
\[
\dot z_i=-z_i+\operatorname{sat}\!\left(\mu z_i+z_i^2+\gamma\sum_{j\ne i}z_j\right),\qquad
\mu=1-2\sqrt{\gamma\tau},\quad
\operatorname{sat}(u)=\max\{0,\min\{1,u\}\}.
\]
The parameter bounds guarantee \(\mu>0\); \([0,1]^n\) is forward invariant. The initial state is \(z_1(0)=1\) and \(z_i(0)=0\) for \(i\ge2\), and the LTM uses the same binary seed. Cascade means convergence to \(1\), rather than merely crossing a positive threshold at a finite time. The fixed upper bound on \(\gamma\) ensures that \(\tau_c(\gamma,n)<1/(4\gamma)\), so all three NOD regimes occur in the declared admissible threshold interval. The primary subject is mathematical sociology and network contagion (MSC2020 91D30).

## Proof

**Step 1: exact symmetric reduction.** By saturation, the seeded coordinate remains \(z_1(t)=1\) for all time: at \(z_1=1\) the unsaturated input is at least \(\mu+1>1\). Existence and uniqueness of the piecewise-Lipschitz vector field preserve equality of the unseeded coordinates. Write their common value as \(x(t)\). Then
\[
\dot x=\min\bigl\{1-x,q_\tau(x)\bigr\},\quad x(0)=0,
\qquad
q_\tau(x)=x^2+\bigl((n-2)\gamma-2\sqrt{\gamma\tau}\bigr)x+\gamma.
\]
The lower saturation bound is inactive because the unsaturated argument is nonnegative on \([0,1]\). Define \(s=\sqrt\gamma\) and \(c=n-2\). The polynomial has the identity
\[
q_\tau(x)=(x-s)^2+2s\bigl(\sqrt{\tau_c}-\sqrt\tau\bigr)x,
\qquad \sqrt{\tau_c}=1+\frac c2s.
\]

**Step 2: exact trichotomy.** If \(\tau<\tau_c\), both terms make \(q_\tau(x)>0\) on \([0,1]\), and \(1-x>0\) for \(x<1\). Thus \(x(t)\) increases to the only possible limit \(1\). In fact convergence is eventually exponential since the saturated input is strictly above \(1\) at \(x=1\), where it equals \(\mu+1+\gamma(n-1)>1\). At \(\tau=\tau_c\), \(q_\tau(x)=(x-s)^2\); since \(0<s<1\), the trajectory stays below \(s\), and throughout that range \(q_\tau(x)<1-x\). Separation of variables gives the *exact* critical solution
\[
x(t)=\frac{\gamma t}{1+\sqrt\gamma\,t},\qquad
s-x(t)=\frac{s}{1+s t}.
\]
If \(\tau>\tau_c\), put \(d=\sqrt\tau-\sqrt{\tau_c}>0\). The polynomial has two positive roots, with smaller root
\[
r_-=s\left(1+d-\sqrt{d(2+d)}\right),\qquad0<r_-<s<1.
\]
Because \(q_\tau(0)=\gamma>0\), the trajectory rises strictly toward \(r_-\) and cannot cross this equilibrium. Thus \(x(t)\to r_-\), and no unseeded node is active in the NOD cascade set. The three cases exhaust the admissible threshold range.

**Step 3: exact discrete comparison.** With one seed, each initially inactive LTM vertex has total active neighbor weight exactly \(1\). If \(\tau<1\), all activate together after one step; if \(\tau\ge1\), none activates and the configuration is fixed. Therefore the LTM cascade is full exactly when \(\tau<1\). Since \(\tau_c=1+cs+c^2s^2/4\), it equals \(1\) at \(n=2\) and strictly exceeds \(1\) for every \(n\ge3\). This proves the exact disagreement interval and demonstrates that the source's non-tie hypothesis for its general small-coupling equivalence theorem cannot simply be discarded.

**Step 4: exact tied-threshold passage clock.** Fix \(n\ge3\), set \(\tau=1\), \(c=n-2\), and write
\[
B=s-\frac c2\gamma,\qquad
D^2=\gamma-B^2=c\gamma^{3/2}-\frac{c^2}{4}\gamma^2>0.
\]
Then \(q_1(x)=(x-B)^2+D^2\). While \(0\le x\le1/2\), the unsaturated input is increasing in \(x\), and at \(1/2\) it equals \(3/4-s+n\gamma/2<1\). Thus the upper clipping never intervenes before the first passage to \(1/2\), and
\[
T_{1/2}
=\int_0^{1/2}\frac{dx}{(x-B)^2+D^2}
=\frac1D\left[\arctan\frac{1/2-B}{D}+\arctan\frac BD\right].
\]
As \(\gamma\downarrow0\) with \(c>0\) fixed, \(D\sim\sqrt c\,\gamma^{3/4}\), while \(B/D\to+\infty\) and \((1/2-B)/D\to+\infty\). Both arctangents tend to \(\pi/2\), establishing the asserted \(\gamma^{-3/4}\) law and exact coefficient. This asymptotic concerns one fixed graph size and the exact-tie threshold; it is not uniform as \(n\to\infty\).

## Verification

Run `python3 verify.py` with only the Python standard library. The program checks the critical quadratic identity and admissible parameters by exact rational arithmetic for \(n=2,\ldots,12\) and three couplings per size; it checks the direction of the critical polynomial sign, tie-status for the discrete model, the no-clipping inequality, and the convergence of four explicit passage-time asymptotics. Expected output begins `VERIFY_OK`. The theorem for all admissible real parameters follows from the analytical proof above, not from this finite numerical test.

## Relationship to prior work

Belaustegui et al. [1] introduce the clipped quadratic NOD relaxation, its relation \(\mu=1-2\sqrt{\gamma k\tau}\), and a cascade-set equivalence theorem requiring **no equality** between any binary neighbor sum and its threshold (Theorem 2). The complete-network equality threshold, exact triad of outcomes and tied-threshold passage-time coefficient are not established there. The present result works at exactly the hypothesis boundary, and does not claim that general saddle-node normal forms or feedback-induced cascades are new. Zhong and Leonard [2] study another continuous threshold model with smooth sigmoid and real signed states; it has different update equations and no direct implication of the clipped-quadratic threshold here. General saddle-node ghost scaling is classical [3]; the contribution here is its exact coefficient and nontrivial \(\gamma^{-3/4}\) parametrization for the NOD-to-LTM comparison. Discrete graph threshold classifications and general critical-relaxation results do not by themselves imply this particular network-specific boundary.

## Limitations

The result covers one binary seed, a *homogeneous* threshold, the *unit-weight* complete network, \(k=1\), zero bias, and a restricted coupling range. It is not a general graph criterion, not a theorem for arbitrary seed sets, and not an inference about observed human adoption. Equality at \(\tau=\tau_c\) is **not** an NOD full cascade, even though trajectories approach a strictly positive equilibrium. The passage-time asymptotic is for fixed \(n\ge3\) and the exact LTM tie \(\tau=1\); it does not describe time to full convergence or finite-time crossing at \(\tau=\tau_c\). The algebraic calculation may be an instance of known saddle-node normal-form theory, and independently discovering the same specific model reduction remains a literature risk. No independent scientific audit has been performed.

## References

[1] I. X. Belaustegui, H. Sinhmar, L.-W. Kong, A. M. Hein, N. E. Leonard, *A Continuous-Time and State-Space Relaxation of the Linear Threshold Model with Nonlinear Opinion Dynamics*, arXiv:2603.29214v1 (31 March 2026), https://arxiv.org/html/2603.29214v1.

[2] Y. D. Zhong, N. E. Leonard, *A Continuous Threshold Model of Cascade Dynamics*, arXiv:1909.11852v1 (26 September 2019), https://arxiv.org/pdf/1909.11852.

[3] C. Kuehn, *Scaling of saddle-node bifurcations: degeneracies and rapid quantitative changes*, arXiv:0807.1546 (2008), https://arxiv.org/abs/0807.1546. Background on generic passage-time scaling; not a source for the network-specific coefficient.
