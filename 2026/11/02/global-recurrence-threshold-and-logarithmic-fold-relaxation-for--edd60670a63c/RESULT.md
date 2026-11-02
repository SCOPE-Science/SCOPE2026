# Global recurrence threshold and logarithmic fold relaxation for generalized Hénon maps

## Finding
For every integer \(m\ge3\), every real \(a\), and every \(0<b<1\), consider the polynomial map
\[
F_{a,b}^{(m)}(x_1,\ldots,x_m)
=\bigl(a-x_{m-1}^{2}+b x_m,\ x_1,\ldots,x_{m-1}\bigr).
\]
Write \(c=(b-1)/2\), \(a_*=-c^2\), \(S=m-1+b\), and \(e=(1,\ldots,1)\). Then \(a_*\) is the **sharp global threshold for invariant probability measures and compact recurrent dynamics**, not merely for fixed points.

1. If \(a<a_*\), every orbit escapes every bounded set and obeys a linear-in-time norm lower bound. There is no invariant Borel probability measure, with no integrability assumption.
2. If \(a=a_*\), the sole invariant Borel probability measure is \(\delta_{ce}\). Every bounded forward orbit converges to \(ce\).
3. If \(a>a_*\), the two fixed-point atoms \(\delta_{r_\pm e}\), with \(r_\pm=c\pm\sqrt{a-a_*}\), exist.
4. At \(a=a_*\), every bounded forward orbit outside the (possibly global) strong-stable set of \(ce\) obeys, simultaneously for all \(j=1,\ldots,m\),
\[
(F_{a_*,b}^{(m)})^n(x)_j
=c+\frac{m-1+b}{n}
-\frac{(m-1)^2-b}{n^2}\log n
+O_{x,m,b}(n^{-2}).
\]
Orbits on the strong-stable set converge exponentially. The coefficient of the subleading logarithm is therefore explicit in all dimensions, and the expansion applies to all bounded initial conditions except the fast-relaxation set.

For a compactly supported invariant probability \(\mu\) at any \(a\), there is also the exact moment constraint
\[
\operatorname{Var}_{\mu}(x_1)
+\bigl(\mathbb E_{\mu}[x_1]-c\bigr)^2=a-a_*.
\]
The stationary moment constraint is stated as a useful consequence, *not* as an independent originality claim: an analogous identity is already available for the classical planar Hénon map.

## Assumptions and scope
The dimension \(m\) is any fixed integer at least three. The damping parameter is strictly between zero and one; endpoints are excluded because the critical linearization need not have the same primitive-stochastic spectral structure. All dynamics is on \(\mathbb R^m\), with exact real arithmetic. A bounded forward orbit means its entire forward sequence lies in some bounded subset. No moment hypothesis is imposed on invariant Borel probabilities in the recurrence statements; compact support or finite second moments is imposed only for the displayed moment identity. The asymptotic expansion is orbitwise, not uniform over all initial conditions. The strong-stable set consists of points whose forward trajectories converge exponentially to the critical fixed point; only those orbits are excluded from the algebraic law.

The model is documented in a source published on 16 May 2018 and belongs to discrete dynamical systems (MSC2020 37C75).

## Proof
### 1. A global exact coboundary
Define the linear functional
\[
L(x)=x_1+\cdots+x_{m-1}+b x_m.
\]
Direct substitution, with no approximation, yields
\[
\begin{aligned}
L(F_{a,b}^{(m)}x)-L(x)
&=a-x_{m-1}^{2}+(b-1)x_{m-1}\\
&=(a-a_*)-(x_{m-1}-c)^2.
\end{aligned}
\tag{1}
\]
If \(\delta=a_*-a>0\), iteration gives \(L(F^n x)\le L(x)-n\delta\). Since \(\|L\|_2=\sqrt{m-1+b^2}\), for sufficiently large \(n\),
\[
\|F^n x\|_2\ge
\frac{n\delta-L(x)}{\sqrt{m-1+b^2}}\longrightarrow\infty.
\]
Thus no forward orbit is bounded and no compact forward-invariant set exists below the threshold. For arbitrary invariant Borel probability \(\mu\), apply invariance to the bounded, strictly increasing test function \(h\circ L\), \(h(t)=\arctan t\). Equation (1) implies \(h(L(Fx))<h(L(x))\) at every point below the threshold, contradicting equality of their integrals. This does **not** require an expectation of \(L\).

At \(a=a_*\), (1) says \(L(Fx)\le L(x)\), with equality exactly when \(x_{m-1}=c\). For a bounded forward orbit, the nonnegative series \(\sum_{n\ge0}(x_{n,m-1}-c)^2\) telescopes and converges, because \(L(x_n)\) is bounded below. Therefore \(x_{n,m-1}\to c\). The shift equations \(x_{n+1,j+1}=x_{n,j}\) propagate the convergence to each coordinate, proving \(F^n x\to ce\).

For an invariant Borel probability at criticality, the bounded monotone test \(h\circ L\) again forces equality in (1) almost surely; hence \(x_{m-1}=c\) almost surely. All coordinate marginals agree under invariance, by the shift equations, so all coordinates are \(c\) almost surely. Hence \(\mu=\delta_{ce}\). For \(a>a_*\), the fixed-point equation is \((r-c)^2=a-a_*\), supplying the two stated fixed-point measures.

### 2. Spectral structure of the critical fixed point
Center coordinates at \(ce\): let \(u=x-ce\). At \(a=a_*\), the centered map is
\[
u\mapsto P u-e_1 u_{m-1}^2,
\quad
P u=((1-b)u_{m-1}+b u_m,u_1,\ldots,u_{m-1}),
\]
where \(e_1=(1,0,\ldots,0)\). The matrix \(P\) has nonnegative entries, each row sums to one, and its directed graph has two directed cycles of lengths \(m-1\) and \(m\) with strictly positive weights (because \(0<b<1\)). Their lengths are coprime. Thus \(P\) is primitive; Perron–Frobenius theory gives a simple eigenvalue 1 and all other eigenvalues of modulus strictly less than 1. The normalized Perron vectors are
\[
P e=e,\qquad
p^T P=p^T,\qquad
p=\frac1S(1,\ldots,1,b),\qquad p^T e=1.
\]
The local center manifold is one-dimensional, with a codimension-one exponentially contracting strong-stable foliation. Standard center-manifold and stable-tracking theorems apply because the map is polynomial and its remaining multipliers lie strictly inside the unit disk.

### 3. Cubic center reduction in a canonical coordinate
Choose the center coordinate \(z=p^T u=L(u)/S\), and parametrize the center manifold as
\[
u=z e+Qz^2+O(z^3),\qquad p^TQ=0.
\]
The quadratic invariance equation is
\[
(P-I)Q=e_1-\frac1S e.
\]
Its unique solution in \(p^TQ=0\), indexed by \(1\le j\le m\), is
\[
Q_j=\frac{j-1}{S}
-\frac{(m-1)\bigl((m-2)/2+b\bigr)}{S^2}.
\]
In particular
\[
Q_{m-1}=\frac{(m-1)(m-2)/2-b}{S^2}=:\frac H{S^2}.
\]
The centered form of (1) is the **exact** scalar identity \(z'=z-u_{m-1}^2/S\). Hence on the center manifold,
\[
z'=z-\frac{z^2}{S}-\frac{2H}{S^3}z^3+O(z^4).
\tag{2}
\]
These coefficients depend only on the original equations and the specified linear coordinate; no ambiguous rescaling of the center variable is involved.

### 4. Parabolic iteration and its logarithmic correction
Equation (2) has the form \(z'=z-\alpha z^2+\beta z^3+O(z^4)\), with \(\alpha=1/S>0\) and \(\beta=-2H/S^3\). Every sufficiently small positive center coordinate stays positive and decreases to zero. Negative nonzero center coordinates are repelled from a small neighborhood under forward iteration. For the positive orbit, elementary comparison gives \(z_n\sim S/n\). Expanding the reciprocal yields
\[
\frac1{z_{n+1}}-\frac1{z_n}
=\frac1S+\frac{S+2H}{S^3}z_n+O(z_n^2).
\]
Since \(z_n=S/n+O((\log n)/n^2)\), summation gives
\[
\frac1{z_n}=\frac nS+\frac{S+2H}{S^2}\log n+C+o(1),
\]
where \(C\) depends on the orbit. Inversion gives
\[
z_n=\frac Sn-\frac{S+2H}{n^2}\log n+O(n^{-2}).
\]
The identity \(S+2H=(m-1)^2-b\) proves the advertised coefficient. Because every physical component of the center graph is \(c+z+O(z^2)\), the same \(n^{-1}\) and \((\log n)/n^2\) coefficients hold in every coordinate.

Every bounded critical forward orbit converges to \(ce\) by Step 1. Once in the local neighborhood, center-manifold stable tracking supplies a center orbit with exponentially small coordinate error. An orbit whose center projection is identically zero is in the local strong-stable leaf and converges exponentially; if it is not, its center projection must lie on the attracting positive branch, since a negative center orbit cannot converge to zero in forward time. Exponential tracking is negligible compared with the stated polynomial remainder. This completes the law for all bounded non-strong-stable forward orbits.

### 5. Stationary moment consequence
For an invariant measure with finite second moments, integrating (1) is legitimate. Since all coordinate marginals agree by the shift equations, \(\mathbb E[(x_{m-1}-c)^2]=\mathbb E[(x_1-c)^2]\). Therefore
\[
\mathbb E[(x_1-c)^2]=a-a_*
\]
and variance decomposition gives the displayed moment constraint. This observation is ancillary to the recurrence and relaxation theorem.

## Verification
The included `verify_generalized_henon.py` checks the exact polynomial coboundary, Perron projection, quadratic center-graph coefficients, and the simplification of the logarithmic coefficient using rational arithmetic for \(3\le m\le20\) and four rational damping values. It separately iterates representative critical trajectories at \(m=3,4,5\) for 80,000 steps and compares numerical estimates of the logarithmic coefficient against the theorem. The program completed successfully. Rational calculations check identities over sampled dimensions and parameters, while the proof above establishes them symbolically for **all** \(m\ge3\), \(0<b<1\). Finite orbit experiments are diagnostic, not an infinite-time argument. The key global recurrence claims follow directly from (1).

## Relationship to prior work
Zheng, Wang, Li and Wang (2018) explicitly define this arbitrary-dimensional family and analyze the three-dimensional map, including the fixed-point discriminant and its local fold bifurcation. Their full openly accessible article, including the fold center-manifold section and conclusions, was inspected. The threshold \(a_*\) for **fixed-point existence and local fold bifurcation** is prior work. Their displayed fold reduction gives the leading quadratic center coefficient in dimension three; it does not provide the global all-orbit/all-probability threshold or the dimension-uniform logarithmic subleading critical law.

Richter (2002) studies the same higher-dimensional family and provides an important precursor. Its abstract and accessible preview were examined, but a complete lawful copy was unavailable at review time. Consequently, an equivalent dynamical statement within its inaccessible portions is a residual novelty risk; it is not counted as negative coverage based on a snippet.

A published result on the classical **two-dimensional** Hénon map (“Exact stationary fixed-point parabola and strip crossing for the Hénon map,” 2026) already gives an invariant-measure moment parabola in the planar setting. The present moment identity is acknowledged as an analogous extension, not counted as independent novelty. It does not imply a global escape threshold or dimension-uniform logarithmic relaxation coefficient for the specific \(m\ge3\) delay map. Other searched critical-relaxation results concerned distinct continuous-time Sprott systems, while semi-parabolic complex Hénon results concern different two-dimensional holomorphic families. No inspected result implied the combined new statement.

## Limitations
The theorem is confined to real \(m\ge3\) and \(0<b<1\). It does not classify unbounded critical trajectories, attractors above the fold, or the behavior when \(b\le0\) or \(b\ge1\). The asymptotic constants hidden in \(O_{x,m,b}(n^{-2})\) depend on the initial condition. Some critical trajectories converge exponentially and have a different leading law. An inaccessible complete 2002 precursor is a residual publication-priority risk; unindexed results may also exist.

## References
1. J. Zheng, Z. Wang, Y. Li and J. Wang, “Bifurcations and chaos in a three-dimensional generalized Hénon map,” *Advances in Difference Equations* 2018, article 185, published 16 May 2018, DOI: 10.1186/s13662-018-1622-y.
2. H. Richter, “The generalized Hénon maps: Examples for higher-dimensional chaos,” *International Journal of Bifurcation and Chaos* 12 (2002), 1371–1384, DOI: 10.1142/S0218127402005121.
3. “Exact stationary fixed-point parabola and strip crossing for the Hénon map,” published mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-stationary-fixed-point-parabola-and-strip-crossing-for-the--ace815aa3687.
4. Standard Perron–Frobenius theory, one-dimensional center-manifold theory, and stable-foliation tracking for smooth maps, used with the explicit spectral hypotheses proved in the text.
