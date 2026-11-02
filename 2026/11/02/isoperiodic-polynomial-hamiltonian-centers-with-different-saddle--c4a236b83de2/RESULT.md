# Isoperiodic polynomial Hamiltonian centers with different saddle counts and limiting time measures

## Finding
Let \(p\ge4\) be even, \(q>p\) be integral, and \(a>0\). For each \(k\in\{1,\ldots,q\}\) with \(q-k\) even, consider the polynomial Hamiltonian
\[
H_k(x,y)=\frac{(x^2+y^2)^{p/2}}p+a(x^2+y^2)^{(q-k)/2}\operatorname{Re}(x+iy)^k
\]
and its physical-time Hamiltonian flow \(\dot x=\partial_yH_k\), \(\dot y=-\partial_xH_k\). Put \(d=q-p\), \(r_c=(aq)^{-1/d}\), and \(E_c=dr_c^p/(pq)\). All of these systems have a center at the origin and regular inner energy ovals for \(0<E<E_c\). Their enclosed area \(A_k(E)\) and physical period \(T_k(E)\) are **exactly independent of** \(k\), throughout this entire energy interval. Nevertheless, the full systems have exactly \(k\) nonzero equilibrium saddles, and their normalized physical-time measures on the inner ovals obey
\[
\mu_{k,E}\ \Longrightarrow\ \frac1k\sum_{j=0}^{k-1}\delta_{r_c\exp(i(2j+1)\pi/k)}\qquad(E\uparrow E_c).
\]
Moreover, for every admissible \(k\),
\[
T_k(E)=\sqrt{\frac qd}\,r_c^{2-p}\log\!\frac{E_c}{E_c-E}+O(1)\qquad(E\uparrow E_c).
\]
For the concrete quintic polynomial family \(p=4,q=5\), the three cases \(k=1,3,5\) thus share exactly the same nonconstant period-energy function while approaching time measures supported on one, three, or five distinct saddles, respectively. The global flows cannot be topologically conjugate, because their numbers of equilibria differ.

## Assumptions and scope
The phase space is \(\mathbb R^2\) with its standard symplectic area and physical Hamiltonian time. The integers \(p,q,k\), real number \(a\), and energy \(E\) satisfy the quantified restrictions above. In polar coordinates \((r,\theta)\),
\[
H_k(r,\theta)=\frac{r^p}{p}+ar^q\cos(k\theta).
\]
For each \(E\in(0,E_c)\), the **inner oval** means the simple closed level curve \(r=r_{k,E}(\theta)\) with \(0<r_{k,E}(\theta)<r_c\); this is not a claim about all outer components of the same energy level. The orbit probability \(\mu_{k,E}\) is the pushforward of normalized Lebesgue time on one period of that oval. Weak convergence means convergence against every bounded continuous function on the plane.

## Proof
**Inner ovals and equilibria.** For \(0<r<r_c\),
\[
\partial_rH_k=r^{p-1}(1+aqr^d\cos(k\theta))\ge r^{p-1}(1-aqr^d)>0.
\]
Also \(H_k(r_c,\theta)\ge r_c^p/p-ar_c^q=E_c\). Hence for every angle and \(0<E<E_c\) there is exactly one radial solution between zero and \(r_c\), smooth in the angle. It is a regular star-shaped oval. Away from the origin, a critical point must satisfy \(\partial_\theta H_k=-ak r^q\sin(k\theta)=0\) and \(\partial_rH_k=0\). The latter is possible only when \(\cos(k\theta)=-1\), with \(r=r_c\), yielding precisely \(k\) nonzero critical points at the angles stated. At each such point, the radial and angular quadratic forms have opposite signs, so it is a nondegenerate saddle. The origin is an isolated strict minimum.

**Equal areas and periods.** By polar integration,
\[
A_k(E)=\frac12\int_0^{2\pi}r_{k,E}(\theta)^2\,d\theta.
\]
The radial equation depends on \(\theta\) only through \(\cos(k\theta)\). Since integer multiplication of the angular coordinate preserves normalized circle measure, its angular integral is the same for every admissible \(k\). Differentiation under the integral is valid for \(E<E_c\); the Hamiltonian coarea identity \(T_k(E)=A_k'(E)\) follows directly from \(dt=r\,d\theta/(\partial_rH_k)\) (with orientation disregarded). Thus both \(A_k\) and \(T_k\) are exactly common functions of energy, with no time reparametrization.

**Saddle asymptotics.** Fix a saddle angle \(\theta_j=(2j+1)\pi/k\), and write \(\xi=r-r_c\), \(\phi=\theta-\theta_j\), \(\varepsilon=E_c-E\). Taylor expansion gives
\[
H_k=E_c-\frac{d r_c^{p-2}}2\xi^2+\frac{k^2r_c^p}{2q}\phi^2+O((|\xi|+|\phi|)^3).
\]
On the inner oval, solving for the negative radial displacement gives, locally and uniformly for small \(\varepsilon>0\),
\[
-\xi=\frac{\sqrt{2\varepsilon+(k^2r_c^p/q)\phi^2}}{\sqrt{d r_c^{p-2}}}+O(\varepsilon+\phi^2).
\]
Consequently the physical-time element \(r\,d\theta/\partial_r H_k\) differs by a uniformly bounded integrand from
\[
\frac{r_c\,d\phi}{\sqrt{d r_c^{p-2}}\sqrt{2\varepsilon+(k^2r_c^p/q)\phi^2}}.
\]
The integral over a fixed small symmetric saddle-angle neighborhood is therefore
\[
\frac1k\sqrt{\frac qd}\,r_c^{2-p}\log\!\frac1\varepsilon+O(1).
\]
The time contribution outside the \(k\) saddle neighborhoods remains uniformly bounded because the limiting radial derivative is positive there. Summing gives the stated logarithmic law, absorbing the fixed energy unit into \(O(1)\).

**Weak limiting measures.** The Hamiltonian and its inner oval are invariant under angle rotation by \(2\pi/k\), so the time spent near the \(k\) saddles is identical. Each neighborhood contributes a logarithmically diverging time, while the complement contributes bounded time. As the neighborhoods shrink, every continuous test function on them approaches its value at the corresponding saddle. Taking first \(E\uparrow E_c\), then the neighborhood radius to zero, yields the equal-weight atomic weak limit. Different values of \(k\) have distinct numbers of isolated equilibria and hence cannot have globally topologically conjugate flows.

## Verification
The proof above is analytic and covers all allowed integer degrees and all \(a>0\). A standalone checker verifies polynomial-coordinate identities at integer test points for \(p=4,q=5\), confirms the rational Lagrange-inversion coefficients in the common area expansion, and tests angular moment invariance; its finite tests are not substitutes for the proof. For reproducibility, set \(s=(pE)^{1/p}\), \(z=(pa)^2s^{2d}\), \(\alpha=d/p\), \(\beta=2/p\). The common action has the locally convergent series
\[
A(E)=\pi s^2\left(1+\sum_{j\ge1}\frac{\binom{2j}{j}}{4^j}\frac\beta{2j}\frac{(\beta+1+2j\alpha)_{2j-1}}{(2j-1)!}z^j\right),
\]
obtained by Lagrange inversion. It provides an independent local computation of the \(k\)-independent area. No infinite identity is inferred from a finite checker run.

## Relationship to prior work
Gasull's 2020 survey (Problem 12) asks about critical periods for Hamiltonians that are sums of two homogeneous or quasi-homogeneous terms. Álvarez--Gasull--Prohens (2017) and Zhuang--Liu (2023) investigate the critical-point count for the period; the later abstract explicitly reports a positive resolution of that count problem. **No claim of priority is made for one-critical-period or monotonicity facts.** The result here instead compares different polynomial angular harmonics at the same degrees: exact isoperiodicity and equal areas alongside different saddle counts, different weak endpoint time measures, and a frequency-independent logarithmic coefficient. These conclusions do not follow merely from a bound on the number of critical periods. Complete earlier literature comparison remains a publication-priority limitation.

## Limitations
Only the star-shaped inner ovals below \(E_c\) are covered. The exact common period is expressed via an integral (and a local power series), not asserted to have an elementary closed form. The outside-of-oval dynamics need not agree across different harmonics. The finite checker provides supplementary arithmetic evidence, not a global proof. The 2023 paper's complete publisher full text was not accessible during source comparison; its abstract and publicly visible introduction were reviewed. Independent expert audit and exhaustive literature-priority assessment have not been performed.

## References
1. A. Gasull, *Some open problems in low dimensional dynamical systems* (public preprint, 2020-12-04), arXiv:2012.02524, https://arxiv.org/abs/2012.02524 .
2. M. Álvarez, A. Gasull, and A. Prohens, *Global behaviour of the period function of the sum of two quasi-homogeneous vector fields*, Journal of Mathematical Analysis and Applications (2017), DOI:10.1016/j.jmaa.2016.12.077 .
3. J. Zhuang and J. Liu, *Critical Periods of the Sum of Two Quasi-Homogeneous Hamiltonian Vector Fields*, Qualitative Theory of Dynamical Systems (2023), DOI:10.1007/s12346-023-00786-z .
