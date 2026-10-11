# Cauchy time concentration and the order-one moment threshold in a cubic global center

## Finding
For the real cubic vector field
\[\dot x=(1+\kappa x^2)y,\qquad\dot y=-x,\qquad\kappa>0,\]
every non-equilibrium trajectory is periodic. Let \(\Gamma_A\) start at \((A,0)\), where \(A>0\), and write \(T_A\) for its **minimal period in the original time**. Set \(L_A=\log(1+\kappa A^2)\). Sampling \(t\) uniformly in one period makes the \(x\)-coordinate a probability law \(\mu_A\), with the **exact** Lebesgue density
\[
f_A(x)=\frac{2\sqrt\kappa\,\mathbf1_{\{|x|<A\}}}{T_A(1+\kappa x^2)\sqrt{L_A-\log(1+\kappa x^2)}}.
\]
The law converges weakly as \(A\to\infty\) to the centered Cauchy distribution
\[\mu_\infty(dx)=\frac{\sqrt\kappa}{\pi(1+\kappa x^2)}\,dx.\]
The accompanying loss of uniform integrability has a **sharp threshold at order one**. Define \(M_p(A)=T_A^{-1}\int_0^{T_A}|x(t)|^p\,dt\). For each fixed \(p\ge0\),
\[
\begin{aligned}
M_p(A)&\longrightarrow\frac{\kappa^{-p/2}}{\cos(\pi p/2)} &&(0\le p<1),\\
\frac{M_1(A)}{L_A}&\longrightarrow\frac{2}{\pi\sqrt\kappa},\\
M_p(A)&\sim\frac{A^{p-1}}{\sqrt\kappa}\sqrt{\frac{2L_A}{\pi(p-1)}} &&(p>1).
\end{aligned}
\]
In particular, a sequence of compactly supported periodic-orbit measures converges to a law with finite absolute moments precisely below order one. The constants above refer to original physical time, without any time rescaling.

The result also identifies a global phase limit. Put \(q(t)=\kappa^{-1/2}\arctan(\sqrt\kappa x(t))\), \(s=t/T_A\), and \(h=\pi/(2\sqrt\kappa)\). Then \(q(sT_A)\) converges **uniformly for \(0\le s\le1\)** to
\[
q_\infty(s)=\begin{cases}h(1-4s),&0\le s\le1/2,\\h(4s-3),&1/2\le s\le1.\end{cases}
\]
The supporting period normalization is \(T_A\sqrt{L_A}\to2\pi\). The novelty asserted here concerns the original-time occupation law, the moment transition and the phase limit, not the established global-center classification or period-function background of the conjugate cubic field.

## Assumptions and scope
Fix arbitrary \(\kappa\in(0,\infty)\). Each amplitude \(A\in(0,\infty)\) specifies the unique smooth orbit through \((A,0)\). Time starts at that point and uses the differential equations exactly as written. All limiting statements are for \(A\to\infty\) at **fixed** \(\kappa\); the moment exponent \(p\ge0\) is fixed before the limit. No uniformity as \(p\to1\) or \(\kappa\to0\) is asserted. The Cauchy limit is weak convergence against bounded continuous functions on \(\mathbb R\), not total-variation convergence on all amplitudes.

## Proof
**1. Exact Hamiltonian coordinates and energy.** Define
\[q=\frac{1}{\sqrt\kappa}\arctan(\sqrt\kappa x),\quad h=\frac\pi{2\sqrt\kappa},\quad V(q)=\frac1\kappa\log\sec(\sqrt\kappa q).\]
Then \(q\in(-h,h)\) and the equations become \(\dot q=y\), \(\dot y=-V'(q)=-\tan(\sqrt\kappa q)/\sqrt\kappa\). Indeed \(\dot q=\dot x/(1+\kappa x^2)=y\) and \(V'(q)=\tan(\sqrt\kappa q)/\sqrt\kappa=x\). Thus \(H=y^2/2+V(q)\) is conserved. Since \(V\) is even, strictly increasing on \([0,h)\), tends to infinity at the boundary and has a unique minimum at the origin, each positive energy level is a smooth simple periodic oval with minimal period \(T_A\). Its energy is \(E_A=L_A/(2\kappa)\) and its right turning point is \(Q_A=\kappa^{-1/2}\arctan(\sqrt\kappa A)\). Write \(I_E=\int_0^{Q_A}(1-V(q)/E)^{-1/2}\,dq\) whenever \(E=E_A\). The exact physical-time quadrature is \(T_A=4I_E/\sqrt{2E}\).

**2. Sharp period scale and phase.** Invert \(v=V(q)\) on the positive half-axis:
\[\frac{dq}{dv}=g(v):=\frac{\sqrt\kappa}{\sqrt{e^{2\kappa v}-1}},\qquad\int_0^\infty g(v)\,dv=h.\]
Here \(g(v)\) is integrable at zero (it is \(O(v^{-1/2})\)) and has an exponential tail. Therefore
\[I_E=\int_0^E\frac{g(v)}{\sqrt{1-v/E}}\,dv\longrightarrow h.\]
To justify this including the moving square-root singularity, split at \(E/2\). The first part is dominated by \(\sqrt2\,g(v)\) and converges to \(\int_0^\infty g\); for the second part \(g(v)\le C e^{-\kappa E/2}\), so its contribution is at most \(CE e^{-\kappa E/2}\). Consequently \(T_A\sqrt{L_A}=4\sqrt\kappa I_E\to4\sqrt\kappa h=2\pi\).

The same estimate gives uniform convergence of the first-quadrant time primitive to the Euclidean length: for \(0\le q\le Q_A\),
\[0\le\int_q^{Q_A}\!\bigl[(1-V(z)/E)^{-1/2}-1\bigr]dz\le I_E-Q_A\longrightarrow0.\]
Since \(Q_A\to h\), the elapsed normalized time during the descent from \(Q_A\) to any position \(q\in[-Q_A,Q_A]\) differs uniformly by \(o(1)\) from \((h-q)/(4h)\). Inverting these strictly monotone time-to-position maps yields \(\sup_{s\in[0,1]}|q(sT_A)-q_\infty(s)|\to0\), using symmetry of the descending and ascending halves.

**3. Exact occupation law and its Cauchy limit.** On a regular orbit \(y^2=[L_A-\log(1+\kappa x^2)]/\kappa\) and \(dt/dx=1/[(1+\kappa x^2)|y|]\) along a monotone branch. Every \(x\in(-A,A)\) is traversed twice in one period. Dividing by \(T_A\) proves the stated \(f_A\), and its normalization follows by the period quadrature. Alternatively, the uniform triangular-wave convergence from Step 2 shows that the \(q\)-coordinate under normalized original time tends to the uniform law on \((-h,h)\). For any bounded continuous \(F:\mathbb R\to\mathbb R\), exclude first boundary strips of small uniform \(q\)-mass; on the remaining compact interior the map \(q\mapsto \tan(\sqrt\kappa q)/\sqrt\kappa\) is continuous, so uniform-phase convergence gives weak convergence of the \(x\)-law. Pushing \(dq/(2h)\) forward under this tangent map yields \(\sqrt\kappa/[\pi(1+\kappa x^2)]\,dx\).

**4. All moment exponents and the critical constant.** For \(p\ge0\), integrating the exact density over the positive half-axis and substituting \(u=\log(1+\kappa x^2)\) yields the identity
\[M_p(A)=\frac{2\kappa^{-p/2}}{T_A}\int_0^{L_A}\frac{(e^u-1)^{(p-1)/2}}{\sqrt{L_A-u}}\,du.\tag{1}\]
At \(p=1\), the integral is exactly \(2\sqrt{L_A}\), so \(M_1(A)=4\sqrt{L_A}/(T_A\sqrt\kappa)\); Step 2 gives the critical limit.

For \(0\le p<1\), set \(a_p(u)=(e^u-1)^{(p-1)/2}\). It is integrable on \((0,\infty)\), since near zero it is \(O(u^{(p-1)/2})\) and at infinity decays exponentially. The same splitting at \(L_A/2\) as in Step 2 gives
\[\sqrt{L_A}\int_0^{L_A}\frac{a_p(u)}{\sqrt{L_A-u}}\,du\longrightarrow \int_0^\infty a_p(u)\,du=B\!\left(\frac{1-p}{2},\frac{1+p}{2}\right)=\frac\pi{\cos(\pi p/2)}.\]
Here the beta integral follows from the substitution \(z=e^{-u}\). Combine with \(T_A\sim2\pi/\sqrt{L_A}\) in (1).

For \(p>1\), writing \(v=L_A-u\) gives
\[\int_0^{L_A}\frac{(e^u-1)^{(p-1)/2}}{\sqrt{L_A-u}}\,du=e^{(p-1)L_A/2}\int_0^{L_A}\frac{(e^{-v}-e^{-L_A})^{(p-1)/2}}{\sqrt v}\,dv.\]
The last integral converges by dominated convergence to \(\int_0^\infty e^{-(p-1)v/2}v^{-1/2}\,dv=\sqrt{2\pi/(p-1)}\); domination is \(v^{-1/2}e^{-(p-1)v/2}\). Now \(e^{L_A}=1+\kappa A^2\sim\kappa A^2\) and \(T_A\sim2\pi/\sqrt{L_A}\), proving the third regime with its exact coefficient. These steps establish the theorem for every fixed real \(p\ge0\), not merely integer exponents.

**5. Already-known context: period monotonicity.** The same canonical system gives, with \(w=\sqrt{2V(q)}\), \(dq/dw=\sqrt\kappa\,w/\sqrt{e^{\kappa w^2}-1}\), strictly decreasing for \(w>0\) because \(t/(e^t-1)\) decreases. The period is \(4\int_0^1(dq/dw)(\sqrt{2E}\,r)(1-r^2)^{-1/2}\,dr\), strictly decreasing from \(2\pi\). This is included to make the normalization self-contained, **not** as a new period-function result.

## Verification
The companion `verify.py` evaluates the period and time moments by Simpson quadrature after the regularizing substitution \(u=L_A\sin^2\theta\). It checks that periods decrease at five finite energies; \(M_0(A)=1\); the exact \(M_1(A)=4\sqrt{L_A}/(\sqrt\kappa T_A)\) identity; and representative large-energy ratios for \(p=1/2,1,2\). Run `python verify.py` with the Python standard library. The expected terminal marker is `CHECK_OK`. These finite diagnostics do not establish limiting laws; Steps 1–5 above are the proofs.

## Relationship to prior work
Llibre and Rondón, *Global Centers of a Class of Cubic Polynomial Differential Systems* (2023, arXiv:2310.07454v1), Theorem 2(g) establishes global-center ownership for this precise subfamily upon setting \(\kappa=2d_1>0\). Appis and Llibre, *Global centers of a family of cubic systems* (2024), classify the **linearly conjugate** system \(\dot X=V\), \(\dot V=-X(1+\kappa V^2)\), obtained by \(X=y\), \(V=-x\). These papers establish the periodic-orbit setting, not the stated time-sampled Cauchy law and moment thresholds.

For the exactly conjugate vector field \(\dot X=V\), \(\dot V=-X(1+\kappa V^2)\), period-function methods are available; **the present finding does not assert novelty for its period asymptotic or monotonicity**. The present addition concerns the full occupancy distribution of the cubic coordinate and the sharp loss-of-integrability transition for its absolute moments. Cima, Gasull and Mañosas (2000) develop broad separable-Hamiltonian period theory; their Theorem C concerns potential-growth hypotheses and does not state the Cauchy occupation or all-moment threshold here.

## Limitations
The assertions concern a single positive-parameter cubic global-center family and fixed moment orders. They do not imply a comparable Cauchy law for arbitrary cubic centers or for a time-reparametrized vector field. No quantitative convergence rate in the weak topology is asserted, and no uniform near-critical scaling with \(p\to1\) is proved. A semantic literature comparison cannot conclusively establish publication priority against every older differently formulated occupation-measure theorem. The original-time period scale and monotonicity are previously covered under linear conjugacy; they are included only to normalize and prove the occupation statements. The supplied numerical diagnostics are finite checks rather than certificates of infinite-limit assertions.

## References
1. J. Llibre and G. Rondón, *Global Centers of a Class of Cubic Polynomial Differential Systems*, arXiv:2310.07454v1, first posted 11 October 2023, Theorem 2(g), https://arxiv.org/abs/2310.07454.
2. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, *Aequationes Mathematicae* **98** (2024), 1373–1389, DOI:10.1007/s00010-024-01051-7, https://doi.org/10.1007/s00010-024-01051-7.
3. A. Cima, A. Gasull and F. Mañosas, *Period Function for a Class of Hamiltonian Systems*, *Journal of Differential Equations* **168** (2000), 180–199, DOI:10.1006/jdeq.2000.3912, https://doi.org/10.1006/jdeq.2000.3912.
