# A unique growth-rate reversal between local and rare long-distance dispersal

## Finding
Consider two symmetric probability kernels on the integer line: \(K_0=(\delta_{-1}+\delta_{1})/2\), and \(K_q=(1-q)\delta_0+(q/2)(\delta_{-2}+\delta_2)\) with \(0<q\le1\). Let \(R>1\) be the low-density reproductive multiplier and define the rightward linear-determinacy speed functional
\[
c_K(R)=\inf_{t>0}\frac{\log R+\log M_K(t)}{t},\qquad M_K(t)=\sum_{j\in\mathbb Z}K(j)e^{tj}.
\]
The **complete ranking theorem** is:

1. If \(1/4\le q\le1\), then \(c_{K_q}(R)>c_{K_0}(R)\) for every \(R>1\).
2. If \(0<q<1/4\), there exists a **unique** \(R_*(q)>1\) such that \(c_{K_q}(R)<c_{K_0}(R)\) for \(1<R<R_*(q)\), the two speeds are equal at \(R=R_*(q)\), and \(c_{K_q}(R)>c_{K_0}(R)\) for \(R>R_*(q)\).
3. Define \(I_q(v)=\sup_{t\ge0}\{tv-\log[1-q+q\cosh(2t)]\}\) for \(0\le v\le1\), and \(I_0(v)=\tfrac{1+v}{2}\log(1+v)+\tfrac{1-v}{2}\log(1-v)\), with the continuous endpoint convention. There is an exact secondary threshold \(q_c=0.145200330326435\ldots\), specified below, separating an interior speed crossing from a crossing after \(K_0\) has reached its maximal step speed. If \(0<q<q_c\), then \(\log R_*(q)=I_q(1)>\log2\) and the common speed is \(1\). If \(q=q_c\), then \(R_*(q)=2\) and the common speed is \(1\). If \(q_c<q<1/4\), the common speed is the unique \(v_*(q)\in(0,1)\) with \(I_q(v_*)=I_0(v_*)\), and \(\log R_*(q)=I_0(v_*)\).

The threshold \(q_c\) is exactly \(2z_c^2/[(z_c^2+3)(z_c^2-1)]\), where \(z_c>1\) is the unique such root of \(z^3-4z^2+3z-4=0\). For \(0<q\le q_c\), put
\[
y_q=\frac{1-q+\sqrt{(1-q)^2+3q^2}}{q}.
\]
Then an explicit switching formula is \(R_*(q)=y_q^{3/2}/[q(y_q^2-1)]\). In particular, for \(q=1/8\), \(y_q=7+2\sqrt{13}\) and \(R_*(1/8)=2.13271041141225\ldots\). The corresponding common spreading speed is exactly \(1\).

## Assumptions and scope
The setting is one-dimensional discrete space with generations indexed by nonnegative integers. Kernel atoms are normalized and symmetric, distances \(1\) and \(2\) are in common lattice units, the same reproduction factor \(R>1\) is used with both kernels, and the functional above is defined for every such \(q,R\). This is a theorem about the **linear-determinacy speed functional**, not a new existence theorem for all nonlinear traveling waves. Where monotone, linearly determinate population models justify identifying this functional with a biological invasion speed, the result compares their predicted leading-edge velocities. It does not assert such identification without model assumptions.

## Proof
Write \(L=\log R>0\), \(\phi_0(t)=\log\cosh t\), and \(\phi_q(t)=\log(1-q+q\cosh2t)=\log(1+2q\sinh^2t)\). The elementary factorization
\[
M_q(t)-M_0(t)=(\cosh t-1)\bigl(2q(\cosh t+1)-1\bigr)
\]
shows \(M_q(t)>M_0(t)\) for all \(t>0\) when \(q\ge1/4\). Since the minimum for either speed occurs at a finite positive tilt unless its bounded-jump endpoint is attained, and the endpoint speed of \(K_q\) is \(2\) rather than \(1\), this yields the strict ranking in part 1.

For \(0<q<1/4\), the tilted means \(v_i(t)=\phi_i'(t)\) satisfy
\[
v_0(t)=\tanh t,\quad
v_q(t)=\frac{4q\sinh t\cosh t}{1+2q\sinh^2t},\quad
\frac{v_q(t)}{v_0(t)}=\frac{4q(1+\sinh^2t)}{1+2q\sinh^2t}.
\]
The last ratio increases strictly from \(4q<1\) to \(2>1\), crossing one at \(\sinh^2t=(1-4q)/(2q)\). Both tilted means increase strictly from zero to their respective maximal jump lengths. Let \(t_i(v)\) be their inverse tilts for \(0<v<1\). Then \(t_q(v)-t_0(v)\) is positive below one velocity \(v_c\in(0,1)\) and negative above it.

The Legendre rate functions obey \(I_i'(v)=t_i(v)\) for \(0<v<1\). Consequently \(J(v)=I_q(v)-I_0(v)\) increases strictly on \((0,v_c)\), decreases strictly on \((v_c,1)\), and satisfies \(J(0)=0\). In particular \(J(v)>0\) near zero and there can be **at most one positive zero** in \((0,1]\). This is the key global uniqueness lemma.

For a bounded symmetric kernel with maximal positive jump \(a\), strictly convex log moment-generating function \(\phi\), and right-tail mass \(p_a>0\), the speed satisfies \(c(e^L)=I^{-1}(L)\) on \(0<L<-\log p_a\), and \(c(e^L)=a\) thereafter. This follows by differentiating \((L+\phi(t))/t\): its finite minimizer obeys \(L=t\phi'(t)-\phi(t)=I(\phi'(t))\); above the endpoint rate, the infimum is approached as \(t\to\infty\). Here the two endpoints are \(I_0(1)=\log2\) and \(I_q(2)=\log(2/q)\).

Thus a positive zero of \(J\) in \((0,1)\) gives exactly one growth-rate crossing while both speeds are below one. If \(J(1)\ge0\), the second speed is strictly smaller until the first has saturated at \(1\), after which the second speed increases through \(1\) exactly once at \(L=I_q(1)\). The equality case occurs at \(L=\log2\). The low-growth ordering is also consistent with \(c_{K_q}/c_{K_0}\to2\sqrt q<1\) as \(L\downarrow0\); at large growth, the speeds approach \(2\) and \(1\), respectively.

To classify the endpoint comparison, \(I_q(1)\) is strictly decreasing with \(q\), since \(\partial_q\phi_q(t)>0\) for positive tilts. It diverges as \(q\downarrow0\) and lies below \(\log2\) at \(q=1/4\), so equality occurs at exactly one \(q_c\). At the maximizing tilt for \(I_q(1)\), let \(y=e^{2t}>1\). The tilted-mean equation is \(qy^2-2(1-q)y-3q=0\), giving \(y=y_q\), while \(I_q(1)=\log[y_q^{3/2}/(q(y_q^2-1))]\). Imposing \(I_q(1)=\log2\), with \(z=\sqrt y\), yields \(z^3-4z^2+3z-4=0\) and the stated formula for \(q_c\). This cubic has exactly one root \(z>1\): it is negative at \(1\) and at its only local minimum on that half-line, then increases to infinity. All claims follow.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3.9 or newer; there are no third-party dependencies. The program checks the MGF factorization on 2,000 reproducible parameter pairs, performs 6,000 direct minimization-versus-threshold comparisons, and checks the two critical branches, numerical root, and support-saturation cases. It prints \(q_c\approx0.145200330326436\), \(R_*(1/8)\approx2.132710411412251\), and \(R_*(1/5)\approx1.449099457773091\). These finite checks supplement, but do not establish, the universal analytical proof.

## Relationship to prior work
Kot, Lewis and van den Driessche (1996) introduce the integrodifference invasion-speed formulation via kernel moment-generating functions and explicitly observe that different **continuous** dispersal kernels can exchange invasion-speed ranking as reproductive rate changes. Their printed analytical development and Drosophila illustrations do not supply the exact nearest-neighbor versus stationary/long-jump lattice comparison, single-crossing proof, or the secondary \(q_c\) boundary claimed here. Hsu and Zhao (2008) establish linear determinacy and traveling-wave results in broad function-kernel settings; their main integral assumptions concern Lebesgue densities rather than the atomic lattice kernels here. The general speed formula itself, low-growth variance behavior, and the qualitative possibility of reversal are not claimed as new. The contribution is the complete exact two-parameter ranking, its single-switch rigidity, and the distinction between an interior and a post-saturation switch.

## Limitations
The kernels are idealized three-/two-atom probability laws, not fitted dispersal data. The conclusion concerns identical reproductive multipliers with no density dependence in the speed functional itself. Nonlinear fronts, density-dependent dispersal, stochastic finite-population effects, nonuniform environments, and continuous kernels are not classified. Literature overlap is assessed on the inspected accessible materials; the possibility that a broader large-deviation comparison theorem implies this particular phase diagram is a remaining historical-priority risk.

## References
Kot, M., Lewis, M. A., and van den Driessche, P. (1996), “Dispersal Data and the Spread of Invading Organisms,” *Ecology* 77:2027–2042. DOI: 10.2307/2265698. First published 1996-10-01.

Hsu, S.-B., and Zhao, X.-Q. (2008), “Spreading Speeds and Traveling Waves for Nonmonotone Integrodifference Equations,” *SIAM Journal on Mathematical Analysis* 40:776–789. DOI: 10.1137/070703016.
