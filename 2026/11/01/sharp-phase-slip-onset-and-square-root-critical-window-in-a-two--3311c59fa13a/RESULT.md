# Sharp phase-slip onset and square-root critical window in a two-cluster discrete Kuramoto map

## Finding

**Theorem (exact no-slip phase diagram and fold law).** Consider the discrete-time, all-to-all phase-lag system
\[
\theta_i^{(n+1)}=\theta_i^{(n)}+\omega+\frac{K}{N}\sum_{j=1}^{N}\sin\big(\theta_j^{(n)}-\theta_i^{(n)}-\beta\big)\pmod{2\pi},
\]
with a common frequency \(\omega\), \(K>0\), and \(0<\beta<\pi/2\). Suppose the initial state has exactly two internally synchronized clusters of integer sizes \(p>q\ge1\), \(N=p+q\), and define \(d=(p-q)/N\in(0,1)\). For the oriented phase separation \(x\in(0,2\pi)\) from the larger cluster to the smaller one, put
\[
 A=K\cos\beta,\qquad B=Kd\sin\beta,
 \qquad F_{A,B}(x)=x-A\sin x+B(1-\cos x).
\]
The *no-slip property* means that the distinguished real lift \(F_{A,B}\) takes every \(x\in(0,2\pi)\) into \((0,2\pi]\); equality at the upper endpoint denotes synchronization at one step rather than an overshoot. Then:

**1. Exact parameter boundary.** For \(0<A<1\), let \(t_A\in(0,\pi)\) be the unique solution of
\[
 t_A\cot(t_A/2)=1+A,
 \qquad B_c(A)=\frac{t_A-A\sin t_A}{1-\cos t_A}.
\]
The no-slip property holds *if and only if* \(A\le1\) and \(B\le B_c(A)\), interpreting \(B_c(1)=0\). In the stated positive-lag, unequal-cluster family there is, for each fixed \((d,\beta)\), one and only one coupling \(K_c(d,\beta)\in(0,1/\cos\beta)\) satisfying
\[
 K_c d\sin\beta=B_c(K_c\cos\beta).
\]
Exactly \(0<K\le K_c(d,\beta)\) is phase-slip-free for every two-cluster separation. For \(K>K_c\), some initial separations cross a representative endpoint in one step (the real lift does not preserve the fundamental interval).

**2. Global motion on the no-slip side.** Write
\[
 x_* =2\arctan(A/B)\in(0,\pi).
\]
Within the invariant two-cluster family, \(x_*\) is the only nonsynchronous fixed phase separation and is repelling, with derivative \(F'_{A,B}(x_*)=1+A\). For every other initial separation, the orbit converges to exact cluster synchrony modulo \(2\pi\): a lift beginning below \(x_*\) decreases to \(0\), and one beginning above \(x_*\) increases to \(2\pi\), possibly reaching the endpoint in finite time at \(K=K_c\). Along a non-finite-hitting trajectory the distance from the relevant endpoint obeys
\[
 \lim_{n\to\infty}\frac{\operatorname{dist}(x_{n+1},\{0,2\pi\})}
 {\operatorname{dist}(x_n,\{0,2\pi\})}=1-A\in(0,1).
\]
These are statements *inside* the exactly invariant two-cluster family, not transverse stability claims for general oscillator configurations.

**3. Quantitative fold onset.** At \(K=K_c\), put \(A_c=K_c\cos\beta\), \(t_c=t_{A_c}\), and
\[
 D_c=\frac{A_c-\cos t_c}{\sin t_c}>0.
\]
The unique additional endpoint-hitting initial separation is \(x_c=2\pi-t_c\), where \(F_{A_c,B_c}(x_c)=2\pi\) and \(F'_{A_c,B_c}(x_c)=0\). Immediately above \(K_c\), the set of separations whose first lifted iterate strictly exceeds \(2\pi\) is one open interval, of length
\[
 \boxed{\quad
 \ell(K)=2\sqrt{\frac{2t_c}{K_c D_c}}\sqrt{K-K_c}+O(K-K_c)
 \quad(K\downarrow K_c).\quad}
\]
The boundary curve has the singular endpoint and the fixed-imbalance weak-lag coupling asymptotics
\[
 B_c(A)=\sqrt{\frac83}\sqrt{1-A}+O((1-A)^{3/2})\quad(A\uparrow1),
\]
\[
 K_c(d,\beta)=1+\left(\frac12-\frac{3d^2}{8}\right)\beta^2+O(\beta^4)
 \quad(\beta\downarrow0).
\]
For illustration, \(d=1/2\), \(\beta=\pi/4\) gives \(K_c=1.2994873552017\ldots\).

## Assumptions and scope

The two groups remain internally synchronized because every member of the same group experiences exactly the same update. The orientation and representative are fixed: \(x=\theta_{\mathrm{minority}}-\theta_{\mathrm{majority}}\pmod{2\pi}\), represented in \((0,2\pi)\). Only such initial two-group states are considered; a generic configuration with more than two initial phases is not covered. The nonzero repeller separates the two monotone convergence channels. The no-slip property is deliberately stronger than a zero rotation number or eventual convergence modulo \(2\pi\); its definition is physical (avoiding an ordering reversal at the synchronization cut) and depends on the distinguished lift. A one-step overshoot beyond threshold does not by itself establish failure of eventual synchronization, and no such stronger claim is made.

## Proof

**Invariant scalar reduction.** Let \(u\) and \(v\) be the two group phases and \(x=v-u\). Within each group, the within-group sine term is \(-\sin\beta\). Subtracting the two exact finite-population updates gives
\[
 x^+=x-K\cos\beta\sin x+K\frac{p-q}{N}\sin\beta(1-\cos x)\pmod{2\pi}.
\]
This is the stated real lift, with no continuum or weak-coupling approximation. It can also be written \(F(x)=x+B-\sqrt{A^2+B^2}\sin(x+\varphi)\), where \(\cos\varphi=A/\sqrt{A^2+B^2}\), so it is a particular sine-circle map with a synchronization-selected cut.

**The lower endpoint.** For \(A\le1\), \(x-A\sin x\ge(1-A)x\ge0\) on \((0,2\pi)\), with strict positivity. Adding \(B(1-\cos x)\ge0\) preserves the inequality. Conversely, when \(A>1\), expansion at \(x=0\) gives \(F(x)=(1-A)x+O(x^2)<0\) for sufficiently small positive \(x\). Thus \(A\le1\) is necessary and sufficient for *avoiding lower-endpoint crossings*, regardless of \(B\ge0\).

**Sharp upper endpoint.** Put \(y=2\pi-x\). The condition \(F(x)\le2\pi\) for all \(x\in(0,2\pi)\) is equivalent to
\[
 y-A\sin y-B(1-\cos y)\ge0\quad(0<y<2\pi),
\]
and for \(0\le A<1\) to
\[
 B\le\inf_{0<y<2\pi} H_A(y),\qquad
 H_A(y)=\frac{y-A\sin y}{1-\cos y}.
\]
As \(y\to0\), \(H_A(y)\sim2(1-A)/y\to+\infty\); at \(y\to2\pi\), the ratio diverges to \(+\infty\). Its derivative has the same sign as
\[
 Q_A(y)=(1+A)(1-\cos y)-y\sin y.
\]
For \(\pi<y<2\pi\), this is positive. For \(0<y<\pi\), the sign of \(Q_A(y)\) is the sign of \((1+A)-y\cot(y/2)\). The function \(y\cot(y/2)\) decreases strictly from \(2\) to \(0\) on \((0,\pi)\), since
\[
 \frac{d}{dy}\big[y\cot(y/2)\big]
 =\frac{\sin y-y}{2\sin^2(y/2)}<0.
\]
Therefore there is exactly one critical point \(t_A\), a strict global minimum. The formula for \(B_c(A)\) follows. For \(A=1\), near \(y=0\), \(H_1(y)\sim y/3\to0\), so the only admissible nonnegative \(B\) is zero. This establishes the full \((A,B)\) no-slip criterion.

**Unique physical coupling threshold.** The mapping \(A\mapsto B_c(A)\) is continuous and strictly decreasing on \([0,1)\), with envelope derivative
\[
 B_c'(A)=-\frac{\sin t_A}{1-\cos t_A}=-\cot(t_A/2)<0.
\]
It satisfies \(B_c(0)>0\), \(B_c(1)=0\). Along \(A=K\cos\beta\), \(B=Kd\sin\beta\), the left side increases strictly in \(K\), while \(B_c\) decreases. There is exactly one intersection before \(A=1\). For greater \(K\), either the upper bound fails (if \(A<1\)) or the lower bound fails (if \(A>1\)); hence there is a genuine one-step slip. At equality in the upper bound, its unique minimizer yields the sole interior separation \(x_c=2\pi-t_c\) that maps precisely to the upper endpoint.

**Attraction and multipliers.** Factoring the increment gives
\[
 F(x)-x=2\sin(x/2)\big[-A\cos(x/2)+B\sin(x/2)\big].
\]
For \(A,B>0\), this is negative on \((0,x_*)\) and positive on \((x_*,2\pi)\), with exactly one interior root \(x_*\). If no slip occurs, an orbit below this root is strictly decreasing and remains positive; one above is strictly increasing and remains at most \(2\pi\). Any non-finite-hitting monotone orbit converges to a fixed point, and the sign inequalities exclude convergence to the repeller from either side. Direct differentiation gives \(F'(x_*)=1+A>1\) and \(F'(0)=F'(2\pi)=1-A\in(0,1)\). Taylor expansion at the endpoint establishes the exact asymptotic distance ratio. The endpoint itself is a synchronized phase class, with equal phases remaining equal at each later step.

**Square-root tangency.** Define
\[
 G(y,K)=y-K\cos\beta\sin y-Kd\sin\beta(1-\cos y).
\]
At \((t_c,K_c)\), both \(G\) and \(G_y\) vanish. The second derivative equals
\[
 G_{yy}(t_c,K_c)=A_c\sin t_c-B_c\cos t_c
 =\frac{A_c-\cos t_c}{\sin t_c}=D_c>0.
\]
The strict inequality follows from the critical equation and \(\sin t_c<t_c\):
\(A_c-\cos t_c=\cos(t_c/2)(t_c-\sin t_c)/\sin(t_c/2)>0\). Also \(G_K(t_c,K_c)=-t_c/K_c<0\). The implicit nondegenerate fold expansion gives two endpoint-crossing boundaries
\[
 y_\pm(K)=t_c\pm\sqrt{\frac{2t_c}{K_cD_c}}\sqrt{K-K_c}+O(K-K_c).
\]
Their separation is the stated length. Since \(G(y,K_c)\) is strictly positive outside its unique quadratic zero, compactness away from that zero and the endpoint expansions ensure that, for \(K>K_c\) sufficiently close, these are the only crossing points and the slip set is precisely the interval between them.

**Endpoint asymptotics.** Writing \(\varepsilon=1-A\), Taylor expansion of \(t\cot(t/2)=2-t^2/6+O(t^4)=2-\varepsilon\) yields \(t_A=\sqrt{6\varepsilon}(1+O(\varepsilon))\). Substitution into the definition of \(B_c\) gives \(B_c=\sqrt{8/3}\sqrt\varepsilon+O(\varepsilon^{3/2})\). Along the physical coupling ray, write \(K_c=1+c\beta^2+O(\beta^4)\). Then \(A_c=1+(c-1/2)\beta^2+O(\beta^4)\) and \(B_c=d\beta+O(\beta^3)\), so the boundary relation gives \(c=1/2-3d^2/8\). Smooth even-parameter expansion of the implicit nondegenerate positive solution yields the indicated \(O(\beta^4)\) remainder.

## Verification

The accompanying standard-library script `verify.py` checks the exact two-group reduction against the unreduced all-oscillator update, solves the scalar critical equations by independent bisection, tests confinement and one-step overshoot, checks the nontrivial fixed-point multiplier, measures the near-fold square-root interval, and tests the singular \(A\uparrow1\) coefficient. Running it prints `VERIFIED 40916 finite diagnostics` and the coupling threshold for \(d=1/2,\beta=\pi/4\). These are finite corroborations only; the preceding analysis proves the universal statements.

## Relationship to prior work

Gade and Gupta, arXiv:2609.22715v1 (2026), introduce the exact discrete-time Kuramoto phase-lag system and obtain a continuum incoherence-instability threshold. They do not classify the present finite-population unequal two-cluster invariant family. The prior public result *Sharp no-slip locking and logarithmic relaxation at quadrature phase lag* establishes the exceptional \(\beta=\pi/2\) boundary \(B_c(0)=1.3800501396893\ldots\) and its parabolic relaxation. Its exact two-cluster reduction is used as prior art here; the current theorem concerns the **strictly nonquadrature** \(0<\beta<\pi/2\) geometry, with an interior repelling separation, exponential attraction, a curved coupling boundary, and a two-sided square-root onset. Gong, Zheng, Toenjes and Pikovsky (arXiv:1812.05883) treat the corresponding continuous-time stochastic Kuramoto–Sakaguchi two-cluster dynamics and transverse stability; the continuous drift does not imply this finite-step threshold. Standard sine-circle-map and Arnold-tongue theory is acknowledged: the map is algebraically a standard sine-circle map, and the fixed-point existence/zero-rotation tongue is **not** the same as fundamental-interval no-slip confinement. In particular, this theorem is not a claimed new class of circle maps.

## Limitations

The proof is specific to identical natural frequencies, exact two-cluster initial data, positive unequal group sizes, \(0<\beta<\pi/2\), and the given synchronous all-to-all update. It does not prove transverse attraction of the two-cluster manifold, classify arbitrary multicluster initial states, or characterize their dynamics beyond the first slip. The definition of no-slip uses the synchronization-selected representative and is stronger than zero rotation. Priority regarding specialized older standard-circle-map results remains a documented residual risk; an independent mathematical review has not been performed.

## References

1. P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1, first public September 19, 2026. https://arxiv.org/abs/2609.22715
2. *Sharp no-slip locking and logarithmic relaxation at quadrature phase lag*, publicly indexed mathematical research record (2026). The earlier theorem treats \(\beta=\pi/2\) only.
3. C. C. Gong, C. Zheng, R. Toenjes, and A. Pikovsky, *Repulsively Coupled Kuramoto–Sakaguchi Phase Oscillators Ensemble Subject to Common Noise*, arXiv:1812.05883. https://arxiv.org/abs/1812.05883
4. N. Goncharuk and M. Yampolsky, *Renormalization of circle maps and smoothness of Arnold tongues*, arXiv:2307.15195v2, introduction and standard-map family. https://arxiv.org/html/2307.15195v2
