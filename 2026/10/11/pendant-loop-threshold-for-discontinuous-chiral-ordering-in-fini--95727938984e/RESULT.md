# Pendant-loop threshold for discontinuous chiral ordering in finite correspondences

## Finding
Fix an integer \(k\geq0\). On a directed three-cycle with all three core self-loops, attach \(k\) degree-one return branches to each core vertex, with an edge in each direction on each attachment. Put the oriented current observable \(\psi=+1\) on forward core edges, \(\psi=-1\) on backward core edges, and \(\psi=0\) otherwise. For inverse temperature \(\beta\geq0\), maximize the stationary Markov pressure
\[
\mathcal P_k(\beta)=\sup_{\mu Q=\mu}\left[h_\mu(Q)+\frac{\beta}{2}\left(\sum_{x,y}\mu(x)Q(x,y)\psi(x,y)\right)^2\right],
\]
where \(h_\mu(Q)=-\sum_{x,y}\mu(x)Q(x,y)\log Q(x,y)\), with \(0\log0=0\).

Set, for all real \(t\),
\[
C(t)=1+2\cosh t,\qquad S_k(t)=\sqrt{C(t)^2+4k},\qquad
\lambda_k(t)=\frac{C(t)+S_k(t)}2,
\]
\[
P_k(t)=\log\lambda_k(t),\qquad m_k(t)=P_k'(t)=\frac{2\sinh t}{S_k(t)}.
\]
Set \(b_k(t)=t/m_k(t)\) for \(t>0\), and \(\beta_c(k)=\sqrt{9+4k}/2\). The complete equilibrium classification is as follows.

**Continuous branch:** For \(k=0,1,2\), \(b_k\) increases strictly from \(\beta_c(k)\) to infinity. For \(0\leq\beta\leq\beta_c(k)\), the unique equilibrium pair is \((\mu_0,Q_0)\). For \(\beta>\beta_c(k)\), exactly two pairs \((\mu_{\pm t},Q_{\pm t})\) maximize pressure, where \(t>0\) is the unique solution of \(b_k(t)=\beta\). Their current vanishes continuously at the threshold, with
\[
|J|\sim\sqrt{\frac{48}{\sqrt{9+4k}(9-4k)}}\,\sqrt{\beta-\beta_c(k)}.
\]

**Discontinuous branch:** For every \(k\geq3\), there is exactly one minimizer \(t_*(k)>0\) of \(b_k\). There is exactly one number \(t_{\mathrm{co}}(k)>t_*(k)\) solving
\[
\log\frac{\lambda_k(t)}{\lambda_k(0)}=\frac{t\,m_k(t)}2.
\]
The nonzero local-maximizer branch appears at the spinodal \(\beta_s(k)=b_k(t_*(k))\); the **global** transition occurs at
\[
\beta_t(k)=b_k(t_{\mathrm{co}}(k)),\qquad
\beta_s(k)<\beta_t(k)<\beta_c(k).
\]
Below \(\beta_t(k)\) the zero-current pair is the unique equilibrium; at \(\beta_t(k)\) exactly three pairs (zero and two symmetry-related nonzero currents) are equilibria; above \(\beta_t(k)\) exactly the two ordered pairs are equilibria, with \(t>t_*(k)\) uniquely determined by \(b_k(t)=\beta\). The current jumps to \(m_k(t_{\mathrm{co}}(k))>0\), and \(\mathcal P_k\) has one-sided slopes \(0\) and \(m_k(t_{\mathrm{co}}(k))^2/2\). The zero-current state remains a strict local maximum at coexistence. The integer value \(k=3\) is the first discontinuous case.

For either branch, writing \(\lambda=\lambda_k(t)\) and \(p=1/[3(1+k/\lambda^2)]\), the linear-pressure equilibrium pair is explicit: \(\mu_t(c_i)=p\), \(\mu_t(\ell_{i,j})=p/\lambda^2\), and
\[
Q_t(c_i,c_i)=\lambda^{-1},\quad Q_t(c_i,c_{i+1})=e^t/\lambda,\quad Q_t(c_i,c_{i-1})=e^{-t}/\lambda,\quad
Q_t(c_i,\ell_{i,j})=\lambda^{-2},\quad Q_t(\ell_{i,j},c_i)=1.
\]
Thus \(\mu_t=\mu_{-t}\) but \(J(\mu_t,Q_t)=-J(\mu_{-t},Q_{-t})=m_k(t)\) for \(t>0\): chiral ordering is invisible to single-coordinate stationary marginals.

## Assumptions and scope
The core indices are \(i\in\mathbb Z/3\mathbb Z\); leaf labels satisfy \(1\leq j\leq k\). When \(k=0\) there are no leaves. Core edges are precisely \((c_i,c_i)\), \((c_i,c_{i+1})\), and \((c_i,c_{i-1})\); leaf edges are precisely \((c_i,\ell_{i,j})\) and \((\ell_{i,j},c_i)\). Each edge has unit multiplicity. The graph is finite, strongly connected and aperiodic, hence its adjacency is primitive. All entropies use natural logarithms and all inverse temperatures are nonnegative. The maximum is over stationary probability kernels supported on these edges; the identical classification applies to nonlinear equilibrium pairs in the finite-state correspondence formalism of Tang--Yang--Li, by their finite-state variational theorem. No non-Markov assumption is needed: Markov replacement maximizes entropy for a specified stationary two-coordinate law.

## Proof
**1. Perron--Frobenius reduction.** Give an edge \((x,y)\) weight \(A(x,y)e^{t\psi(x,y)}\). Rotating the three core vertices and permuting their equal leaves preserves this matrix. Its positive Perron eigenvector therefore has a common core entry \(u\) and common leaf entry \(v\). The eigen-equations are \(\lambda u=C(t)u+kv\) and \(\lambda v=u\), so \(\lambda^2-C(t)\lambda-k=0\) and the largest positive root is precisely \(\lambda_k(t)\). The left positive eigenvector has the same classwise values, because incoming core and leaf weighted sums obey the same equations. The Doob transform gives the displayed \(\mu_t\) and \(Q_t\). Their rows sum to one by \(C/\lambda+k/\lambda^2=1\), and \(\mu_tQ_t=\mu_t\). Differentiating \(\log\lambda_k(t)\) gives \(m_k(t)\); strict monotonicity follows from the identity
\[
m_k'(t)=\frac{2[2\cosh^2t+(5+4k)\cosh t+2]}{S_k(t)^3}>0.
\]
In particular, \(m_k\) is an odd analytic bijection from \(\mathbb R\) to \((-1,1)\), with \(m_k'(0)=2/\sqrt{9+4k}\).

**2. One-dimensional constrained entropy.** For every stationary pair with circulation \(m\in(-1,1)\), the Perron--Frobenius Gibbs inequality gives \(h_\mu(Q)+tm\leq P_k(t)\), and equality occurs only at \((\mu_t,Q_t)\). This follows directly by integrating the nonnegative relative entropy of each row against the Doob kernel; the logarithm of its eigenvector telescopes under stationarity. For each interior \(m\), choose the unique \(t\) with \(P_k'(t)=m\). The maximal entropy at fixed circulation is therefore
\[
s_k(m)=P_k(t)-tm,\qquad s_k'(m)=-t.
\]
At \(m=\pm1\), only the oriented deterministic core cycle is possible and \(s_k(\pm1)=0\). For finite \(\beta\), neither boundary is a global maximizer, since \(s_k'(m)\to\mp\infty\) as \(m\to\pm1\). Hence the global maximum is among interior critical points of \(s_k(m)+\beta m^2/2\), obeying \(t=\beta m_k(t)\). On the positive half-axis its derivative is
\[
\frac{d}{dm}\left(s_k(m)+\frac\beta2m^2\right)=m\bigl(\beta-b_k(t(m))\bigr).
\]
The negative half-axis is symmetric and \(m=0\) is always critical.

**3. An exact monotonicity dichotomy.** Define \(D(t)=t\cosh t-\sinh t>0\) for \(t>0\). Differentiating \(b_k(t)=tS_k(t)/(2\sinh t)\) shows that its derivative has the sign of
\[
F_k(t)=2tC(t)\sinh^2t-D(t)[C(t)^2+4k].
\]
At the real reference parameter \(k=9/4\), an exact hyperbolic-identity calculation gives
\[
F_{9/4}(t)=\sinh3t+2\sinh2t+11\sinh t
-t(\cosh2t+14\cosh t+3).
\]
Writing Taylor coefficients with the same positive denominators,
\[
F_{9/4}(t)=\sum_{n\geq1}\frac{a_nt^{2n+1}}{(2n+1)!},\quad
D(t)=\sum_{n\geq1}\frac{2n\,t^{2n+1}}{(2n+1)!},\quad
a_n=3\cdot9^n+(3-2n)4^n-28n-3.
\]
Here \(a_1=0\), and \(a_n/(2n)\) is strictly increasing, since
\[
n a_{n+1}-(n+1)a_n
=3\bigl[(8n-1)9^n-(2n^2-n+1)4^n+1\bigr]>0.
\]
Indeed \((9/4)^n\geq n\) for all positive integers \(n\), while \((8n-1)n-(2n^2-n+1)=6n^2-1>0\). The elementary ratio-of-power-series lemma (compare paired cross terms in the derivative of the quotient) implies \(F_{9/4}(t)/D(t)\) is strictly increasing for positive \(t\), from \(0\) to infinity; the latter limit also follows from \(F_{9/4}(t)\sim e^{3t}/2\) and \(D(t)\sim(t-1)e^t/2\). Since
\[
\frac{F_k(t)}{D(t)}=\frac{F_{9/4}(t)}{D(t)}+9-4k,
\]
for integer \(k=0,1,2\) it is everywhere positive, whereas for each integer \(k\geq3\) it has exactly one positive zero, negative before and positive afterwards. Consequently \(b_k\) is strictly increasing for \(k\leq2\), and decreases then increases, with exactly one minimum \(t_*(k)>0\), for \(k\geq3\). Moreover \(b_k(t)\to\infty\) as \(t\to\infty\), and \(b_k(0+)=\beta_c(k)\).

**4. Global phase selection.** For \(k\leq2\), the sign rule in Step 2 yields the unique zero maximizer at and below \(\beta_c(k)\) and one positive plus one negative global maximizer above it. The expansion
\[
P_k(t)=P_k(0)+\frac{t^2}{\sqrt{9+4k}}+
\frac{4k-9}{12(9+4k)^{3/2}}t^4+O(t^6)
\]
proves the displayed square-root onset. For \(k\geq3\), the stationary upper (positive) nonzero branch lies at \(t>t_*(k)\), while the smaller nonzero stationary point, if present, is a local minimum. At any nonzero critical point (where \(\beta=b_k(t)\)), its value relative to the zero phase is
\[
G_k(t)=P_k(t)-P_k(0)-\frac{t\,m_k(t)}2.
\]
One has \(G_k(0)=0\) and \(G_k'(t)=\tfrac12 m_k(t)^2b_k'(t)\), so \(G_k\) decreases strictly until \(t_*(k)\), then increases strictly to infinity. There is therefore exactly one positive zero \(t_{\mathrm{co}}(k)>t_*(k)\), and this global-value comparison gives the claimed one/three/two count of maximizing pairs. Since \(P_k^{(4)}(0)=2(4k-9)/(9+4k)^{3/2}>0\) when \(k\geq3\), the derivative of the reduced objective at \(\beta=\beta_c(k)\) is strictly positive for sufficiently small positive \(m\). Thus the nonzero branch beats zero already for some \(\beta<\beta_c(k)\), establishing the strict upper inequality \(\beta_t(k)<\beta_c(k)\); the strict lower inequality is forced by \(t_{\mathrm{co}}(k)>t_*(k)\) and monotonicity on the upper branch. The pressure is a maximum of the constant zero-phase value and the ordered analytic branch, so its slope jumps from \(0\) to \(m_k(t_{\mathrm{co}})^2/2\). At coexistence \(\beta_t<\beta_c\), the zero phase is still a strict local maximum. The equal-marginal, opposite-current statement follows from the explicit Doob formulas and evenness of \(\lambda_k(t)\).

## Verification
Every step above is analytic. Direct expansion of the explicit Perron root checks \(P_k''(0)=2/\sqrt{9+4k}\) and \(P_k^{(4)}(0)=2(4k-9)/(9+4k)^{3/2}\). Symbolic hyperbolic simplification checks the reference identity for \(F_{9/4}\) and its Taylor coefficients. For the first discontinuous graph \(k=3\), scalar root-finding (an illustration, not proof) gives approximately \(t_*=0.80015730\), \(\beta_s=2.27460002\), \(t_{\mathrm{co}}=0.98874517\), \(\beta_t=2.27861888\), \(\beta_c=2.29128785\), and coexistence current \(0.43392301\). The proof, not this finite-precision calculation, establishes uniqueness, global maximality and the all-integer classification.

## Relationship to prior work
Tang, Yang and Li (2026), especially Sections 6 and 7, prove the general nonlinear correspondence variational and Legendre frameworks, and describe two-state correlation phases, a three-state occupation-based Potts first-order transition, and a one-forbidden-edge three-state continuous transition with exponent \(1/4\). The present family retains a **single scalar, antisymmetric edge-current observable** while changing only the number of reversible pendant excursions; it determines the exact graph-decoration threshold \(k=3\), a unique coexistence equation for all \(k\geq3\), and opposite-current phases with equal one-coordinate marginals. Those specific claims are not consequences of the example statements just cited. Buzzi, Kloeckner and Leplaideur (2023), Section 5, establish general nonlinear thermodynamics, Curie--Weiss examples and an asymmetric three-letter metastable example with a different observable and graph. Bru, de Siqueira Pedra and Lopes (2025), Section 4, treat full two-symbol shift examples and quadratic self-consistency. Kucherenko (2024) provides a rotation-theoretic framework but no corresponding decoration-dependent spectral phase classification. These broad formalisms support the method, rather than supply the particular transition threshold and explicit equilibrium census.

## Limitations
The theorem concerns exactly this primitive family: a looped three-cycle with \(k\) reversible pendant leaves at each core, unit edge multiplicities, and the specified scalar quadratic energy. It does not claim universality for arbitrary primitive graphs, nonquadratic or multi-observable energies, external chiral fields, kinetic transition rates, or fluctuating nonequilibrium entropy production. The transition inverse temperatures for \(k\geq3\) are uniquely characterized transcendental numbers, not elementary closed forms. The proof establishes the phase diagram without claims of more general universality or of a formal-machine certificate.

## References
1. D. Tang, R. Yang and Z. Li, *Nonlinear thermodynamic formalism for correspondences*, arXiv:2609.25915v1 (2026), especially Sections 6 and 7. https://arxiv.org/html/2609.25915v1
2. J. Buzzi, B. Kloeckner and R. Leplaideur, *Nonlinear thermodynamical formalism*, Annales Henri Lebesgue 6 (2023), 1429--1477, arXiv:2002.00576. https://arxiv.org/pdf/2002.00576
3. J.-B. Bru, W. de Siqueira Pedra and A. O. Lopes, *Nonlinear Thermodynamic Formalism: Mean-field Phase Transitions, Large Deviations and Bogoliubov's Variational Principle*, arXiv:2511.06975v1 (2025), especially Section 4. https://arxiv.org/html/2511.06975v1
4. T. Kucherenko, *Nonlinear thermodynamic formalism through the lens of rotation theory*, Discrete and Continuous Dynamical Systems 44 (2024), 3760--3773. https://tamara.ccny.cuny.edu/publications/Nonlinear%20Thermodynamic%20Formalism.pdf
