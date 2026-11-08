# A factor-four rare-winding singularity for geodesically reset Brownian motion on a ring

## Finding

A Brownian particle that occasionally returns along the shortest arc of a ring has a singular high-current winding law. Every arbitrarily small **positive** Poisson return rate cuts the leading large-deviation cost of extremely fast signed rotations to one quarter of the cost without returns. This is a statement about the distribution of rare trajectories, not about a fourfold increase of the ordinary small-fluctuation diffusivity.

Fix a circumference \(L>0\), diffusivity \(D>0\), and reset rate \(r\geq0\). Let \(W_t\) count signed completed turns, as defined below. Its scaled cumulant generating function \(\Lambda_r(k)\) is the unique nonnegative solution of

\[
\cosh k\,H_r(\Lambda_r(k))=1,\qquad
H_r(s)=\frac{r\cosh z+s}{r\cosh z+s\cosh(2z)},\quad
z=\frac L2\sqrt{\frac{r+s}{D}}.
\]

At \(r=0\), define \(H_0(s)=\operatorname{sech}(L\sqrt{s/D})\), including \(H_0(0)=1\). For positive \(r\),

\[
\Lambda_r(k)=\frac{4D}{L^2}\left(|k|-2\log|k|+\log\frac{rL^2}{8D}+o(1)\right)^2-r
\quad (|k|\to\infty).
\]

Consequently, for the good large-deviation rate function of net turns per unit time,

\[
I_r(j)\sim\frac{L^2j^2}{16D}\quad (|j|\to\infty,\ r>0),
\qquad I_0(j)=\frac{L^2j^2}{4D}.
\]

In particular, the limits of \(\Lambda_r(k)/k^2\) at \(r\downarrow0\) and \(|k|\to\infty\) do not commute. The factor four arises because a reset can complete a turn after Brownian travel through only half the circumference.

## Assumptions and scope

The ring has circumference \(L\), its marked start is angle zero, and Brownian motion has generator \(D\partial_{xx}\) (thus free displacement variance \(2Dt\)). The Poisson clock has constant rate \(r\), independent of Brownian motion. A reset returns the physical particle instantaneously along the shortest arc to the marked start. A turn is counted when the trajectory completes a full signed circuit, including a crossing of the lifted completion line induced by the reset arc. A reset at the antipode has two equal shortest choices, but this occurs with probability zero.

For a single turn, use a lifted coordinate \(x\in(-L,L)\), started at zero. Brownian arrival at \(\pm L\) completes a signed turn. At a reset, when \(|x|<L/2\) no turn is completed and \(x\) returns to zero; when \(L/2<|x|<L\), the shortest return arc ends the excursion at \(\operatorname{sgn}(x)L\) and completes one turn. Recenter at zero after each turn. Thus the intercompletion durations are independent copies of a strictly positive random variable \(\tau\); the signs are independent fair marks, also independent of durations, by reflection symmetry. Count only *completed* turns, not the fractional position during the last unfinished excursion.

All limits \(t\to\infty\) are at fixed physical parameters; rare-current asymptotics hold for each fixed \(r>0\). The result makes no claim about delayed finite-speed return arcs, biased Brownian drift, state-dependent reset clocks, or arbitrary reset-time laws.

## Proof

**1. Laplace transform of a completed turn.** For \(s\geq0\), set \(u_s(x)=\mathbb E_x[e^{-s\tau}]\). Let \(b=\sqrt{(r+s)/D}\), \(h=L/2\). By first-step conditioning on the Brownian generator and the exponential clock, \(u_s\) is even, is continuously differentiable at \(h\), satisfies \(u_s(L)=1\), \(u_s'(0)=0\), and obeys

\[
\begin{aligned}
D u_s''-(r+s)u_s+r u_s(0)&=0&&(0<x<h),\\
D u_s''-(r+s)u_s+r&=0&&(h<x<L).
\end{aligned}
\]

The first forcing term corresponds to safe resetting and restarting from zero; the second to immediate completion in the outer half. On \([0,h]\), the unique even solution has the form

\[
u_s(x)=\frac{u_s(0)}{r+s}\bigl(r+s\cosh(bx)\bigr).
\]

On \([h,L]\), the solution has the form

\[
u_s(x)=\frac{r+s\cosh(b(L-x))}{r+s}+C\sinh(b(L-x)).
\]

Matching the value and derivative at \(h\) gives

\[
H_r(s):=u_s(0)=\frac{r\cosh(bh)+s}{r\cosh(bh)+s\cosh(2bh)}.
\]

For \(r=0\), the standard exit-time boundary-value problem directly gives \(H_0(s)=\operatorname{sech}(L\sqrt{s/D})\). In all cases \(H_r(0)=1\), \(H_r(s)\downarrow0\), and \(H_r'(s)<0\) for \(s>0\), as it is the Laplace transform of a nondegenerate positive duration. Its mean is finite: for \(r>0\), writing \(z_0=\frac L2\sqrt{r/D}\),

\[
\mathbb E\tau=-H_r'(0)=\frac{2\sinh^2 z_0}{r\cosh z_0},
\]

whose continuous \(r\downarrow0\) limit is \(L^2/(2D)\).

**2. Regeneration and scaled cumulants.** Reflection of the entire trajectory preserves \(\tau\) and exchanges winding signs. Hence \(\tau\) is independent of each fair sign \(\xi\in\{-1,+1\}\). After completion, the Markov and Poisson memoryless properties restart the same experiment. Let \(M_k(t)=\mathbb E[e^{kW_t}]\), and \(F\) denote the law of \(\tau\). Conditioning on the first completion gives the exact renewal equation

\[
M_k(t)=\Pr(\tau>t)+\cosh k\int_{(0,t]}M_k(t-v)\,F(dv).
\]

For each \(k\ne0\), there is a unique \(\Lambda_r(k)>0\) such that \(H_r(\Lambda_r(k))\cosh k=1\). Multiplication of the renewal equation by \(e^{-\Lambda_r(k)t}\) makes its renewal kernel a nonarithmetic probability measure with finite positive mean. The elementary nonlattice key renewal theorem then gives \(M_k(t)e^{-\Lambda_r(k)t}\to c_k\in(0,\infty)\). At \(k=0\), \(M_0(t)=1\) and \(\Lambda_r(0)=0\). Therefore the claimed scaled cumulant limit exists for every real \(k\).

Implicit differentiation and the finite positive duration mean make \(\Lambda_r\) smooth for all \(k\); it is even and convex. Its derivatives tend to \(\pm\infty\) at the two ends (established in step 3). The Gärtner–Ellis theorem, together with exponential tightness supplied by finiteness of all exponential moment limits, yields an LDP for \(W_t/t\) with the good rate \(I_r(j)=\sup_k\{kj-\Lambda_r(k)\}\).

**3. The high-current regime.** For \(r=0\), the equation reduces to \(\cosh(L\sqrt{\Lambda_0(k)/D})=\cosh k\), so \(\Lambda_0(k)=Dk^2/L^2\). For fixed \(r>0\) and \(s\to\infty\), the exact transform satisfies

\[
H_r(s)=\frac rs\exp\left[-\frac L2\sqrt{\frac{s+r}{D}}\right](1+o(1)).
\]

Indeed, in its numerator \(r\cosh z\) dominates \(s\), whereas in its denominator \(s\cosh(2z)\) dominates \(r\cosh z\). Thus, with \(K=|k|\to\infty\) and \(a=4D/L^2\),

\[
\sqrt{\frac{\Lambda_r(k)+r}{a}}+\log\frac{\Lambda_r(k)}r
=K-\log2+o(1).
\]

The equality first gives \(\Lambda_r(k)/(aK^2)\to1\). Substitution into the logarithm then yields

\[
\sqrt{\frac{\Lambda_r(k)+r}{a}}
=K-2\log K+\log\frac{r}{2a}+o(1),
\]

which proves the stated sharp cumulant expansion. Convexity and quadratic growth imply \(\Lambda_r'(k)\sim2ak\), so the derivative range is the full real line. Legendre duality (or quadratic sandwich bounds) now gives \(I_r(j)\sim j^2/(4a)=L^2j^2/(16D)\). For \(r=0\), direct duality gives \(I_0(j)=L^2j^2/(4D)\).

**4. Singular zero-rate limit.** At each fixed \(s>0\), \(H_r(s)\to H_0(s)\) as \(r\downarrow0\). Strict monotonicity of \(H_r\) in \(s\), and continuity at \(s=0\), imply \(\Lambda_r(k)\to\Lambda_0(k)\) for each fixed \(k\). But the leading coefficient at fixed positive \(r\) is \(4D/L^2\), not \(D/L^2\). Hence the rare-current and vanishing-reset limits cannot be interchanged.

## Verification

The standalone script `CHECK.py` uses only Python's standard library. It tests the exact transform against an independently discretized piecewise backward boundary-value problem, checks the renewal-pole equation and the free-ring limit, and compares numerical roots with the large-tilt expansion. Execute `python CHECK.py` from the extracted directory. The finite diagnostics do not certify an asymptotic identity or replace the proof above.

## Relationship to prior work

Grange's ring-resetting study established the geometric first-turn mechanism and its mean first-completion time, and discussed long-time mean total turns and net-turn variance. Kundu, Comtet and Majumdar developed winding large deviations **without resets**. Tucci, Gambassi, Gupta and Roldán studied the protocol dependence of stationary resetting currents on a ring. Den Hollander, Majumdar, Meylahn and Touchette gave general large-deviation machinery for time-additive functionals of Brownian motion under resets. The result here concerns a different, topological completed-turn observable and isolates the explicit positive-reset, large-tilt asymptotic and its noncommuting limit; the general renewal strategy and known no-reset law are not claimed as new.

## Limitations

The leading factor of four is a rare-event statement for each fixed nonzero reset rate. The logarithmic correction prevents an exact quadratic formula at finite tilt, and the ordinary variance can behave differently. Full text of the closest Grange ring paper could not be accessed during the literature comparison; its abstract and first-page publisher preview were inspected. This leaves a nontrivial publication-priority risk for any related higher-cumulant calculation in its later sections. General theoretical frameworks for resetting large deviations are credited. No independent validation or peer review is claimed.

## References

1. P. Grange, *Winding number of a Brownian particle on a ring under stochastic resetting*, arXiv:2111.15241 (first posted 2021-11-30); *J. Phys. A* **55** (2022) 155003. https://arxiv.org/abs/2111.15241
2. A. Kundu, A. Comtet and S. N. Majumdar, *Winding statistics of a Brownian particle on a ring*, *J. Phys. A* **47** (2014) 385001. https://doi.org/10.1088/1751-8113/47/38/385001
3. G. Tucci, A. Gambassi, S. Gupta and É. Roldán, *Controlling particle currents with evaporation and resetting from an interval*, *Phys. Rev. Research* **2** (2020) 043138. https://doi.org/10.1103/PhysRevResearch.2.043138
4. F. den Hollander, S. N. Majumdar, J. M. Meylahn and H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, *J. Phys. A* **52** (2019) 175001. https://doi.org/10.1088/1751-8121/ab0efd
