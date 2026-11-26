# The sharp incidence-only oscillation window for exponential-transmission SIR

## Finding

In the closed deterministic SIR model with externally prescribed transmission \(\beta(t)=\beta_0e^{rt}\), \(0<r<\gamma\), the onset of repeated incidence peaks occurs strictly below the onset of repeated infectious-prevalence peaks. The additional threshold is explicit; in the resulting nonempty window, incidence has infinitely many strict interior maxima and minima while prevalence strictly decreases.

Write \(a=\gamma-r\), \(X=\beta S/N\), \(Y=\beta I/N\), and let \(h=\Phi(X(0),Y(0))\), where
\[
\Phi(X,Y)=X-a-a\log(X/a)+Y-r-r\log(Y/r).
\]
Set
\[
x_* =\frac{3a+r+\sqrt{a^2+6ar+r^2}}4,\qquad y_*=x_*-a,\qquad
h_{\rm inc}=\Phi(x_*,y_*),\qquad h_{\rm prev}=r-a\log(\gamma/a).
\]
Then \(0<h_{\rm inc}<h_{\rm prev}\). For each of incidence and prevalence, its own threshold has the following meaning: below threshold the derivative is negative; at equality the observable is still strictly decreasing, with one isolated horizontal tangency **per orbit cycle**; above threshold there is one strict local maximum phase and one strict local minimum phase per cycle. Thus the incidence-only window is \(h_{\rm inc}<h\le h_{\rm prev}\). In all cases with \(h>0\), corresponding values one scaled period \(P(h)\) apart are multiplied by \(e^{-rP(h)}\).

## Assumptions and scope

The equations are \(\dot S=-c\), \(\dot I=c-\gamma I\), \(\dot R=\gamma I\), with \(c(t)=\beta(t)S(t)I(t)/N\) the instantaneous incidence. Assume \(\beta_0,N>0\), \(S_0,I_0>0\), \(R_0=N-S_0-I_0\ge0\). The classification is on \([0,\infty)\); peak statements concern interior times \(t>0\). A count of phases per cycle is a count modulo the period of \((X,Y)\), not a count in an open interval that might omit an event at its endpoints. Strict decrease refers to values at any two distinct ordered times, so isolated zeros of the derivative are allowed.

## Proof

Differentiating the scaled coordinates gives \(\dot X=X(r-Y)\), \(\dot Y=Y(X-a)\), with the first integral \(\Phi\) since
\[
\dot\Phi=(X-a)(r-Y)+(Y-r)(X-a)=0.
\]
The Hessian is \(\operatorname{diag}(a/X^2,r/Y^2)\). The energy is proper in the positive quadrant, with its only minimum at \((a,r)\) of value zero. Each \(h>0\) level is the smooth boundary of a compact strictly convex sublevel set, enclosing the center. It is a single closed curve, and the vector field is nowhere zero on it, so it is traversed periodically. At \(h=0\) the scaled coordinates are constant. The physical quantities satisfy \(I=(N/\beta_0)e^{-rt}Y\) and \(c=(N/\beta_0)e^{-rt}XY\); these identities give the damping factor and show that both decrease at the center.

The logarithmic incidence derivative is \(r-Y+X-\gamma=X-a-Y\). On its zero ray set \(Y=x-a\) with \(x>a\). The restricted energy \(\psi(x)=\Phi(x,x-a)\) diverges at both ends and satisfies
\[
\psi'(x)=2-\frac a x-\frac r{x-a},\qquad
\psi''(x)=\frac a{x^2}+\frac r{(x-a)^2}>0.
\]
The minimizer is the unique root above \(a\) of \(2x^2-(3a+r)x+a^2=0\), namely \(x_*\). Its minimum \(h_{\rm inc}\) is positive because the center is not on the ray. Below this minimum the sublevel set lies strictly on the center side, where \(X-a-Y<0\). At equality it touches the ray at only one point, with the same strict sign elsewhere, so incidence decreases strictly. Above equality the level intersects the ray twice, transversally, as the two roots of \(\psi(x)=h\) are simple. The incidence derivative changes sign at each crossing, yielding the two claimed extrema phases.

The logarithmic prevalence derivative is \(X-\gamma\). The minimum of \(\Phi(\gamma,Y)\) is attained uniquely at \(Y=r\) and equals \(h_{\rm prev}=\Phi(\gamma,r)\). Below threshold there is no intersection with the vertical line and the derivative stays negative. At threshold the single contact leaves it negative except at the tangent phase. Above threshold there are two transverse intersections, again giving one extremum of each kind per cycle. Finally, \((\gamma,r)\) lies on the incidence ray, but \(\psi'(\gamma)=r/(a+r)>0\), so \(h_{\rm inc}<h_{\rm prev}\). Any positive energy can be realized in the physical model: take a point \((X_0,Y_0)\) on the level, choose \(\beta_0\ge X_0+Y_0\), and set \(S_0=NX_0/\beta_0\), \(I_0=NY_0/\beta_0\). Then \(R_0\ge0\), and the closed SIR equations preserve positivity and total population.

## Exact witness and reproducibility

Take \(N=1\), \(r=1\), \(\gamma=2\), \(\beta_0=4\), and \((S_0,I_0,R_0)=(19/40,1/4,11/40)\). Then \((X_0,Y_0)=(19/10,1)\) and \(h=9/10-\log(19/10)<1-\log 2=h_{\rm prev}\), by monotonicity of \(x-1-\log x\) for \(x>1\). The point \((17/10,7/10)\) lies on the incidence ray and has energy \(2/5-\log(119/100)\). This energy is strictly below \(h\), since \(190/119<13/8<e^{1/2}\). Thus \(h_{\rm inc}<h<h_{\rm prev}\) without a numerical sign test. The supplementary `verify.py` documents the symbolic identities and sample integrations; sampled dynamics cannot establish the all-time or all-parameter classification.

## Relationship to prior work and limitations

The Resultary record [1] already gives the same Lotka–Volterra dynamics, the exact prevalence threshold, geometric damping, and incidence peaks in the supercritical prevalence regime. In its notation \((Q,P)=(X/\gamma,Y/r)\), the energy \(H\) differs from \(\Phi\) by a constant, and \(H(1,1)=\gamma+r\) corresponds to \(\Phi(\gamma,r)=h_{\rm prev}\). The distinct contribution here is the sharp incidence threshold and the strict incidence-only window, not the prevalence criterion or geometric wave train. A later indexed Resultary record [2] gives the equivalent separate thresholds: its growth rate \(a\) is this note’s \(r\), its \(b\) is this note’s \(a\), and its positive minimizing ordinate \(h_c\) is \(y_*\).

General incidence and prevalence peak conditions under time-varying transmission are treated by Rabajante [3]. Those local derivative conditions are not by themselves the global incidence classification. The CoSIR preprint [4] concerns a feedback policy rather than an externally fixed exponential transmission function. Classical Lotka–Volterra periodicity is not new here. Because the prescribed transmission is unbounded and the oscillations shrink geometrically, the model does not predict infinitely many detectable waves or imply any statistical identifiability result.

## References

1. *A sharp infinite-wave threshold for an exponentially forced SIR model*, Resultary, October 13, 2026. https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-a-sharp-infinite-wave-threshold-for-an-exponentially-forced-sir--9a40b59e84d7
2. *Exact geometric wave trains under monotone exponential transmission in a closed SIR model*, Resultary, November 8, 2026. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-geometric-wave-trains-under-monotone-exponential-transmiss--ce053672f1d8
3. J. F. Rabajante, *How Simple Models Can Reproduce Multiple Epidemic Waves: Peak Topology, Minimal Dynamic Complexity, and Inference for Time-Varying Transmission*, arXiv:2610.05556, https://arxiv.org/abs/2610.05556.
4. H. Maheshwari, S. Shetty, N. Bannur, and S. Merugu, *CoSIR: Optimal control of SIR epidemic dynamics by mapping to Lotka-Volterra System*, medRxiv, doi:10.1101/2020.11.10.20211995.
