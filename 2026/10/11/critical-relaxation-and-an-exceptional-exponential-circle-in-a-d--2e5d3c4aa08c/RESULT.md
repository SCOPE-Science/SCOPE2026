# Critical relaxation and an exceptional exponential circle in a discrete repulsive oscillator triangle

## Finding

Fix three phase oscillators with identical natural frequencies, repulsive sine coupling on the edges \(12\) and \(23\) of weight \(1\), and repulsive coupling on edge \(13\) of weight \(1/2\). Remove the common rotation. For the explicit-Euler phase map with step \(0<h<2/3\), the phase class \(P=(\pi,\pi)\) is locally attracting despite having one unit eigenvalue. In local coordinates
\[
u=\frac{x+y}{2}-\pi,\qquad v=\frac{x-y}{2},\qquad x=\theta_2-\theta_1,\quad y=\theta_3-\theta_2,
\]
all sufficiently nearby initial states satisfy \((u_n,v_n)\to(0,0)\). If \(u_0=0\), the convergence is exponential; if \(u_0\ne0\), the sign of \(u_n\) is constant and there is a finite constant \(C=C(u_0,v_0,h)\) such that
\[
\boxed{\frac1{u_n^2}=hn+\frac{3h-1}{4}\log n+C+o(1),\qquad n\to\infty.}
\]
At the distinguished step \(h=1/3\) the logarithmic coefficient vanishes; it is negative below this value and positive above it.

For \(0<h<1/3\), the stronger global conclusion holds: every orbit on the quotient two-torus converges to one of four fixed phase classes, and almost every initial condition converges to \(P\). Exactly the points of the invariant circle \(\theta_1=\theta_3\pmod{2\pi}\) that are not at the fully synchronized source converge exponentially to \(P\). Every other point in the basin of \(P\) follows the displayed algebraic-and-logarithmic law after entering a local chart. The source and the stable manifolds of the two saddles form a measure-zero exceptional set to almost-everywhere attraction.

## Assumptions and scope

The map acts on \(\mathbb T^3\), modulo common phase shifts, by
\[
\theta_i^{+}=\theta_i+h\sum_{j\ne i}w_{ij}\sin(\theta_i-\theta_j)\pmod{2\pi},
\qquad w_{12}=w_{23}=1,\quad w_{13}=1/2.
\]
The phase quotient is \(\mathbb T^2\) with edge differences \((x,y)\). There is no imposed frequency disorder, phase lag or noise. The sign convention is **repulsive**; it is the gradient-descent map of \(V(\theta)=\cos(\theta_1-\theta_2)+\cos(\theta_2-\theta_3)+\tfrac12\cos(\theta_1-\theta_3)\). The result concerns the exact discrete map, not an asymptotic numerical integration of its continuous-time analogue. The step restrictions are strict. Haar measure refers to the usual normalized area on the quotient torus. Local coordinates are chosen by continuous real lifts close to \(P\); inverse powers are asserted only when \(u_0\ne0\).

## Proof

**1. Exact reduction.** Subtracting adjacent node updates gives the torus map
\[
\begin{split}
x^+&=x+h(2\sin x-\sin y+\tfrac12\sin(x+y)),\\
y^+&=y+h(2\sin y-\sin x+\tfrac12\sin(x+y)).
\end{split}
\]
Around \(P\), put \(x=\pi+u+v\) and \(y=\pi+u-v\). Without any approximation,
\[
\boxed{u^+=u+h\sin u(\cos u-\cos v),\qquad
v^+=v-3h\cos u\sin v.}\tag{1}
\]
In particular \(u=0\) is invariant and its normal return is not linear: \(\partial u^+/\partial u\vert_{(0,0)}=1\), whereas the transverse multiplier is \(1-3h\).

**2. Local attraction and exponential transverse decay.** Fix \(0<h<2/3\). Choose \(q\) with \(|1-3h|<q<1\). In a sufficiently small rectangle \(|u|,|v|<\delta\), the second equation of (1) yields \(|v^+|\le q|v|\). Also
\[
1-\tfrac h2u^2\le\frac{u^+}{u}\le1+\tfrac h2v^2
\]
for \(u\ne0\), after shrinking \(\delta\) if necessary; the same inequality defines the multiplier by continuity at \(u=0\). Choose \(\delta\) so that \(r_0=1-h\delta^2/2>q\). The upper bound and the geometric estimate on \(v_n\) imply
\[
|u_n|\le |u_0|\exp\left(\frac{h v_0^2}{2(1-q^2)}\right).
\]
Taking initial data in a smaller rectangle keeps all iterates in the \(\delta\)-rectangle. The multiplier stays positive, so the sign of nonzero \(u_n\) is preserved. Moreover
\[
\left|\frac{v_n}{u_n}\right|
\le\left|\frac{v_0}{u_0}\right|\left(\frac q{r_0}\right)^n.\tag{2}
\]
Eventually \(|v_n|<|u_n|/2\), and equation (1) then gives \(0<u_{n+1}/u_n\le1-c_hu_n^2\), with some \(c_h>0\), for sufficiently small nonzero \(u_n\). Hence \(u_n\to0\). If \(u_0=0\), equation (1) instead gives \(v_n=O(q^n)\) for any fixed \(q>|1-3h|\), with \(q<1\). This includes \(h=1/3\), where the transverse multiplier is zero.

**3. Exact first logarithmic correction.** With \(z=u^2\), Taylor expansion of (1) at the origin and (2) give, uniformly along a nonzero-center orbit,
\[
\frac{u^+}{u}=1-\frac h2z+\frac h8z^2+O(z^3+v^2).
\]
Since \(v_n^2/u_n^2\) decays geometrically by (2), setting \(Y_n=u_n^{-2}\) yields
\[
Y_{n+1}-Y_n=h+\frac{h(3h-1)}{4Y_n}
+O\left(Y_n^{-2}+\rho^n\right),\qquad 0<\rho<1.\tag{3}
\]
The coefficient is obtained by expanding \((1+az+bz^2)^{-2}\) with \(a=-h/2\) and \(b=h/8\): its \(z\)-coefficient after multiplication by \(1/z\) is \(3a^2-2b=h(3h-1)/4\). Equation (3) first implies \(Y_n=hn+o(n)\); it then implies \(Y_n=hn+O(\log n)\). Subtracting \(h\) and \((3h-1)/(4n)\) from (3) leaves an absolutely summable sequence, because \(1/Y_n=1/(hn)+O(\log n/n^2)\), \(Y_n^{-2}=O(n^{-2})\), and \(\rho^n\) is summable. Therefore \(Y_n-hn-(3h-1)\log n/4\) converges to a finite real limit \(C\). No numerical orbit was used to infer this limit.

**4. Complete equilibrium census and global descent for small steps.** Stationarity in edge coordinates forces \(\sin x=\sin y\). If \(x+y=\pi\pmod{2\pi}\), the remaining stationary equation reduces to \(\sin x=0\); if \(x=y\), it reduces to \(\sin x(1+\cos x)=0\). Thus the only four stationary phase classes are
\[
(0,0),\quad(\pi,0),\quad(0,\pi),\quad P=(\pi,\pi).
\]
The edge-Jacobian eigenvalues before multiplication by \(h\) are respectively \(2,3\) at \((0,0)\), \((-1\pm\sqrt{13})/2\) at each of \((\pi,0),(0,\pi)\), and \(0,-3\) at \(P\). Hence for \(0<h<1/3\), the first is a source, the middle two are hyperbolic saddles, and \(P\) is the locally attracting parabolic fixed point proved above.

Let \(L\) be the graph Laplacian for the weights \((1,1,1/2)\). Its spectrum is \(\{0,2,3\}\), so, for every state and every real vector \(w\),
\[
|w^TD^2V(\theta)w|\le w^TLw\le3\|w\|^2.
\]
The phase map is \(F_h=I-h\nabla V\). The smooth descent estimate is
\[
V(F_h\theta)\le V(\theta)-h(1-3h/2)\|\nabla V(\theta)\|^2.
\]
For \(0<h<1/3\), the lift of \(F_h\) has everywhere positive definite derivative \(I-hD^2V\); it is globally injective by strict monotonicity and descends to a torus diffeomorphism. The gradient squares are summable, and every accumulation point is stationary. Because there are only four stationary classes and the steps tend to zero, every orbit converges to one of them. The stable manifolds of the two hyperbolic saddles are one-dimensional immersed curves, and the source has only itself as its stable set; their union has area zero. Almost every orbit therefore converges to \(P\).

**5. The exact exponential exception.** The invariant circle \(\mathcal C=\{\theta_1=\theta_3\pmod{2\pi}\}\) has scalar coordinate \(s=\theta_2-\theta_1\) and exact map \(s^+=s+3h\sin s\pmod{2\pi}\). For \(0<h<1/3\), it is a strictly increasing circle diffeomorphism with fixed points \(s=0\) (repelling) and \(s=\pi\) (attracting). Every other point on \(\mathcal C\) tends exponentially to \(P\), with nontrivial asymptotic ratio \(1-3h\). Since \(F_h\) is a diffeomorphism taking \(\mathcal C\) onto itself, no point outside \(\mathcal C\) ever enters it. Every other point converging to \(P\) eventually has nonzero local center coordinate and obeys (3), so it cannot converge exponentially. This proves the claimed sharp separation of convergence mechanisms.

## Verification

Run the standalone Python-standard-library script `verify.py` from the same directory, using `python verify.py`. It checks the exact rational series coefficient for four rational step sizes, both coordinate-map formulas on 125 trigonometric test cases at five step sizes, all four fixed classes, and the two-point stabilization of the renormalized quantity along five long finite trajectories. The program reports 279 finite coordinate/fixed/asymptotic checks and 12 exact rational Taylor equalities. The critical infinite assertions are proved in the preceding argument; numerical checks do not certify an infinite limit, novelty, or independent review.

## Relationship to prior work

Zhao and Zhou (arXiv:2407.11314, first posted July 16, 2024) determine the equilibria and linear stability of the continuous-time three-oscillator isosceles network, including signed couplings. These equilibrium bifurcations are **not** claimed as new. Shim (2020) establishes exponential rates for a different, attractive, homogeneous discrete-time Kuramoto regime. Gade and Gupta (arXiv:2609.22715, first posted September 19, 2026) analyze discrete-time Kuramoto synchronization with phase lag and distributed frequencies, motivating examination of discrete effects at a degenerate finite-network transition. The present result concerns a fixed repulsive weighted triangle and its sharp step-dependent inverse-square/logarithmic asymptotic, together with the exceptional exponential circle. Generic descent and local parabolic iteration techniques are standard inputs, not new tools.

## Limitations

The theorem is specific to three identical repulsively coupled oscillators and the weak edge weight exactly \(1/2\). The global almost-everywhere statement is restricted to \(0<h<1/3\), while the local asymptotic extends to \(0<h<2/3\). It neither establishes the global dynamics for larger steps nor addresses nonzero phase lag, heterogeneous frequencies, stochastic perturbations or the whole family of edge weights. The constant \(C\) is finite and orbit-dependent; no explicit closed form is claimed. An equivalent calculation in broader normal-form or oscillator literature may exist. No independent audit has been performed.

## References

1. P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1, September 19, 2026.
2. X. Zhao and X. Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network*, arXiv:2407.11314, July 16, 2024.
3. W. Shim, *On the generic complete synchronization of the discrete Kuramoto model*, Kinetic and Related Models **13** (2020), 979–1005, DOI:10.3934/krm.2020034.
4. *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993, October 2026, relevant for general gradient-descent context but later than the qualifying source date.
