# Isospectral factor order produces a square-root separation of optimal periodic oscillator stability constants

## Finding
Let \(D=d/dt\). For fixed \(a,b>0\), a real \(P\)-periodic function \(Q\), and \(\delta>0\), define
\[
u_\delta(t)=a+\delta Q'(t),\qquad L_A=(D+b)(D+u_\delta),\qquad L_B=(D+u_\delta)(D+b).
\]
For either operator \(L\), its best whole-line Ulam constant \(K(L)\) is the smallest \(K\) such that every \(\eta\in C^2(\mathbb R,\mathbb R)\) satisfying \(\|L\eta\|_\infty\le\varepsilon\) is within \(K\varepsilon\), uniformly on \(\mathbb R\), of an exact solution \(Lx=0\). Write \(K_A=K(L_A)\) and \(K_B=K(L_B)\).

Suppose \(Q\in C^4(\mathbb R)\) has, on the circle of period \(P\), precisely one global maximum \(t_M\) and one global minimum \(t_m\), both nondegenerate. Define
\[
\Delta=Q(t_M)-Q(t_m)>0,\quad \kappa_M=-Q''(t_M)>0,\quad \kappa_m=Q''(t_m)>0,
\]
and let \(\tau\in(0,P)\) be the positive forward time from \(t_M\) to \(t_m\), modulo \(P\). Then the sharp asymptotics are
\[
\lim_{\delta\to\infty}\sqrt\delta\,e^{-\delta\Delta}K_A(\delta)
 =\frac{e^{-a\tau}}{b(1-e^{-aP})}\sqrt{\frac{2\pi}{\kappa_M}},
\]
\[
\lim_{\delta\to\infty}\delta\,e^{-\delta\Delta}K_B(\delta)
 =\frac{2\pi e^{-a\tau}}{(1-e^{-aP})(1-e^{-bP})\sqrt{\kappa_M\kappa_m}},
\]
and therefore
\[
\boxed{\lim_{\delta\to\infty}\frac{K_A(\delta)}{\sqrt\delta\,K_B(\delta)}
=\frac{1-e^{-bP}}{b}\sqrt{\frac{\kappa_m}{2\pi}}>0.}
\]
Both second-order equations have the same Floquet multipliers \(e^{-aP}\) and \(e^{-bP}\), as well as the same mean damping \(a+b\) and mean stiffness \(ab\). Nevertheless their optimal uniform residual-to-solution constants differ by an unbounded factor of order \(\sqrt\delta\). The exact integral representations for the constants themselves are special cases of existing general Green-operator theory; the asserted contribution is the sharp **two-order large-modulation comparison**, including its constants and the unbounded norm separation.

## Assumptions and scope
All time variables and suprema are over the real line; coefficients are real and \(P\)-periodic. The parameter \(\delta\) tends to positive infinity while \(Q,P,a,b\) remain fixed. The hypotheses require global uniqueness and quadratic nondegeneracy of both extrema, not positivity of the instantaneous damping. The Ulam norm is the ordinary scalar uniform norm on \(\mathbb R\), not a weighted norm or a phase-space norm. No assertion is made about finite-time numerical dynamics or uniformity across varying \(a,b,Q\).

In scalar second-order notation, the operators are
\[
L_Ax=x''+(a+b+\delta Q')x'+(ab+b\delta Q'+\delta Q'')x,
\]
\[
L_Bx=x''+(a+b+\delta Q')x'+(ab+b\delta Q')x.
\]
Thus \(L_A-L_B\) is multiplication by \(\delta Q''\), whereas both coefficient averages agree. Either factorization gives a triangular first-order realization with Floquet multipliers \(e^{-aP}\) and \(e^{-bP}\). These multipliers have modulus less than one, even when the instantaneous damping changes sign.

## Proof
**1. Causal inverses and the best constants.** For bounded continuous \(g\), let
\[
(G_ug)(t)=\int_{-\infty}^t e^{-a(t-s)-\delta(Q(t)-Q(s))}g(s)\,ds,
\quad
(G_bg)(t)=\int_{-\infty}^t e^{-b(t-s)}g(s)\,ds.
\]
Both integrals converge absolutely because \(a,b>0\) and \(Q\) is bounded. They solve \((D+u_\delta)G_ug=g\) and \((D+b)G_bg=g\), respectively. Hence the bounded scalar inverse solutions of \(L_Ae=g\) and \(L_Be=g\) are \(e=G_uG_bg\) and \(e=G_bG_ug\). Their kernels are nonnegative. Any nonzero homogeneous solution of either second-order equation is unbounded on \(\mathbb R\): a triangular periodic realization has both Floquet multipliers strictly inside the unit disk, hence no nonzero bounded bilateral orbit. Consequently the bounded error \(e\) is the unique error between an approximate solution and an exact solution. Positivity and the choice \(g\equiv1\) show that the operator norms of these inverses are the **best**, rather than merely admissible, Ulam constants.

Set \(v_\delta=G_u1\) and \(w_\delta=G_bv_\delta\). Since \(G_b1=1/b\),
\[
K_A=\frac1b\max_{t\in[0,P]}v_\delta(t),\qquad
K_B=\max_{t\in[0,P]}w_\delta(t).
\]
The two positive periodic responses have the exact period-cell formulas
\[
v_\delta(t)=\frac{e^{-\delta Q(t)}}{1-e^{-aP}}
\int_{t-P}^{t}e^{-a(t-s)+\delta Q(s)}\,ds,
\]
\[
w_\delta(t)=\frac{1}{1-e^{-bP}}
\int_{t-P}^{t}e^{-b(t-s)}v_\delta(s)\,ds.
\]
The first formula follows by partitioning the infinite past into periods; the second is analogous.

**2. Concentration of the first response.** Choose continuous lifts with \(t_m=t_M+\tau\), \(0<\tau<P\). The unique nondegenerate maximum gives, uniformly for \(t=t_m+z/\sqrt\delta\) with \(z\) in any fixed compact set, the Laplace estimate
\[
\int_{t-P}^{t}e^{-a(t-s)+\delta Q(s)}\,ds
\sim e^{-a\tau+\delta Q(t_M)}\sqrt{\frac{2\pi}{\delta\kappa_M}}.
\]
At the minimum, Taylor expansion gives
\[
Q(t_m+z/\sqrt\delta)=Q(t_m)+\frac{\kappa_m z^2}{2\delta}+o(\delta^{-1}).
\]
Combining these formulas yields the local Gaussian pulse profile
\[
\sqrt\delta\,e^{-\delta\Delta}v_\delta(t_m+z/\sqrt\delta)
\longrightarrow \frac{e^{-a\tau}}{1-e^{-aP}}
\sqrt{\frac{2\pi}{\kappa_M}}e^{-\kappa_m z^2/2}.
\]
A uniform bound for the period-cell integral is \(O(e^{\delta Q(t_M)}\delta^{-1/2})\): omit the bounded weight \(e^{-a(t-s)}\) and use the usual nondegenerate-maximum estimate for the integral of \(e^{\delta Q}\) over a whole period. Therefore \(v_\delta(t)\) is bounded by \(C\delta^{-1/2}e^{\delta(Q(t_M)-Q(t))}\). Outside any fixed neighborhood of \(t_m\), the normalized response is exponentially smaller; near \(t_m\), the quadratic minimum gives uniform integrable Gaussian tails. The maximum of \(v_\delta\) consequently has the same leading coefficient as its value at \(t_m\), proving the first displayed limit.

The same envelope permits dominated Gaussian rescaling of the pulse area. With \(M_\delta=\int_0^P v_\delta(s)\,ds\),
\[
\lim_{\delta\to\infty}\delta e^{-\delta\Delta}M_\delta
=\frac{2\pi e^{-a\tau}}{(1-e^{-aP})\sqrt{\kappa_M\kappa_m}}.
\]
This step uses both independent quadratic scales: one from the past maximum in the causal kernel and one from the current minimum of \(Q\).

**3. Averaging the concentrated pulse.** Positivity gives, for every \(t\),
\[
0<w_\delta(t)\le \frac{M_\delta}{1-e^{-bP}}.
\]
For the reverse asymptotic inequality choose \(t=t_m+\delta^{-1/3}\), interpreted on a fixed lifted period. The integration interval \([t-P,t]\) then contains all but an asymptotically negligible fraction of the single pulse near \(t_m\). Its pulse is at a vanishing distance behind \(t\), so its exponential weight \(e^{-b(t-s)}\) is \(1+o(1)\) throughout the mass-carrying region. Therefore
\[
\max_t w_\delta(t)\sim \frac{M_\delta}{1-e^{-bP}}.
\]
Substituting the pulse-area limit proves the second displayed limit; division establishes the square-root separation. Every step holds for each fixed \(a,b>0\), with no appeal to a numerical extrapolation.

**4. Floquet check.** In \(L_Ax=0\), setting \(z=(D+u_\delta)x\) produces \(z'=-bz\), \(x'=-u_\delta x+z\). In \(L_Bx=0\), setting \(z=(D+b)x\) produces \(z'=-u_\delta z\), \(x'=-bx+z\). Each triangular system has one-period diagonal multipliers \(e^{-bP}\) and \(e^{-\int_0^P u_\delta}=e^{-aP}\), so the scalar equations are isospectral at the Floquet-multiplier level.

## Verification
A standalone script, `verify_order_response.py`, computes the positive periodic Green responses for the test case \(Q(t)=\sin t\), \(P=2\pi\), \(a=b=1\) using composite trapezoidal quadrature. It checks the \(\delta=0\) normalization and compares the numerically maximized responses with both analytical leading coefficients at modulation levels \(\delta=25,80,240\). Run it with `python verify_order_response.py` in a standard Python environment. It prints `CHECK_OK` when its numerical assertions hold. This diagnostic is not an infinite-parameter proof; the proof above supplies the necessary limit justification.

For this test case, \(\Delta=2\), \(\kappa_M=\kappa_m=1\), \(\tau=\pi\), and the prediction simplifies to
\[
K_A(\delta)\sim\frac{e^{2\delta-\pi}}{1-e^{-2\pi}}\sqrt{\frac{2\pi}{\delta}},\qquad
K_B(\delta)\sim\frac{e^{2\delta-\pi}}{(1-e^{-2\pi})^2}\frac{2\pi}{\delta}.
\]
The response ratio converges comparatively slowly because a constant-rate downstream filter reaches its maximum just after the progressively narrower forcing pulse.

## Relationship to prior work
The exact use of Green integrals for best Hyers–Ulam constants is established in Fukutaka and Onitsuka (2019) for first-order periodic equations, in Fukutaka and Onitsuka (2020) for a class of Hill equations, and in Anderson, Onitsuka, and O'Regan (2023, Theorem 4.1) for more general nonautonomous damped linear oscillators. Those contributions already cover abstract best-constant representations and are not claimed here. Swapping first-order factors is also a standard Darboux-type structural operation, so factorization and equality of Floquet multipliers alone are not claimed as original.

The more specific point is that two periodic scalar second-order operators with **identical Floquet multipliers and coefficient averages** have sharply different leading optimal uniform stability constants, with a computed universal \(\sqrt\delta\) ratio and both precise prefactors. The inspected general theorems do not state this large-modulation factor-order comparison or its two-extremum Gaussian mechanism. Li and collaborators (2024) give later qualitative Ulam-stability criteria for periodic damping; the accessible material describes an optimal constant only for constant coefficients. No claim of exhaustive priority is made.

## Limitations
The proof assumes a unique nondegenerate global maximum and minimum of \(Q\) on each period. Degenerate/multiple extrema, nonsmooth coefficients, varying \(a\) or \(b\), negative modulation, other Ulam norms, and matrix-valued systems are outside scope. Neither the shared Floquet multipliers nor the mean coefficient values determine the uniform Green norm. The quadrature program is illustrative, and earlier results on general Green representations must remain credited; a complete exhaustive literature priority certification is unavailable.

## References
1. D. R. Anderson, M. Onitsuka, D. O'Regan, “Best Ulam constants for damped linear oscillators with variable coefficients,” arXiv:2307.15103v1 (first public July 27, 2023), Theorem 4.1; later J. Math. Anal. Appl. 543 (2025), 128908, DOI 10.1016/j.jmaa.2024.128908.
2. R. Fukutaka, M. Onitsuka, “Best constant in Hyers–Ulam stability of first-order homogeneous linear differential equations with a periodic coefficient,” J. Math. Anal. Appl. 473 (2019), 1432–1446, DOI 10.1016/j.jmaa.2019.01.030.
3. R. Fukutaka, M. Onitsuka, “Best constant for Ulam stability of Hill's equations,” Bull. Sci. Math. 163 (2020), 102888, DOI 10.1016/j.bulsci.2020.102888.
4. J. Li, X. Xia, C. Zhang, R. Chen, “Ulam Stability of Second-Order Periodic Linear Differential Equations with Periodic Damping,” Symmetry 16 (2024), 1459, DOI 10.3390/sym16111459.
