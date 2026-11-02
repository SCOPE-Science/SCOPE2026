# A sharp global-attractor threshold for the two-cell sigmoid spiking map

## Finding
For the two-cell spiking map introduced by Buscarino, Famoso and Fortuna, the exact set of positive Euler steps admitting a compact global attractor is \(0<T\le2\), independently of the sigmoid gain \(\alpha>0\). The endpoint \(T=2\) is included even though the unsaturated linear part has multiplier \(-1\). If \(T>2\), every sufficiently remote initial state escapes at a uniform geometric rate, and no compact global attractor exists.

More precisely, put
\[
M=\begin{pmatrix}17/10&-1\\1&17/10\end{pmatrix},\qquad
b=\begin{pmatrix}-3/10\\3/10\end{pmatrix},\qquad
\Theta_\alpha(z)=\begin{pmatrix}\tanh(\alpha z_1)\\\tanh(\alpha z_2)\end{pmatrix},
\]
and consider \(F_{T,\alpha}(z)=(1-T)z+T(M\Theta_\alpha(z)+b)\) on \(\mathbb R^2\), with \(T,\alpha>0\). Define
\[
S=\frac{\sqrt2}{10}(\sqrt{389}+3),\qquad H=2S.
\]
Then the following are explicit compact absorbing, forward-invariant Euclidean balls:
\[
0<T<2:\quad \|z\|_2\le1+\frac{TS}{1-|1-T|},
\]
\[
T=2:\quad \|z\|_2\le R_\alpha,
\qquad R_\alpha=H+\frac58\left(H^2+\frac{68}{5e\alpha}+1\right).
\]
For \(T>2\), every initial state with \(\|z_0\|_2\ge 2TS/(T-2)\) satisfies
\[
\|F_{T,\alpha}^{n}(z_0)\|_2\ge (T/2)^n\|z_0\|_2\qquad(n\ge0).
\]
Consequently, compact global attraction and escape from a neighborhood of infinity meet at precisely \(T=2\).

## Assumptions and scope
All assertions concern the deterministic, real-plane map displayed above, with the exact coefficients fixed in the cited 2023 two-cell model. The parameter \(\alpha\) is any fixed positive real number; no upper bound on it is imposed. An absorbing set means one forward-invariant compact set eventually entered by every bounded set of initial conditions, uniformly over that bounded set. A compact global attractor is a compact invariant set attracting every bounded subset of \(\mathbb R^2\). The result does not claim that the global attractor consists of a single orbit, nor that it is chaotic. The sharp threshold is for these global properties, not the existence of smaller compact invariant sets at other steps.

## Proof
Write \(G_\alpha(z)=M\Theta_\alpha(z)+b\). The matrix identity \(M=(17/10)I+J\), with \(J\) skew-symmetric and \(J^\mathsf TJ=I\), gives \(\|M\|_2=\sqrt{389}/10\). As \(\|\Theta_\alpha(z)\|_2\le\sqrt2\) and \(\|b\|_2=3\sqrt2/10\), one has \(\|G_\alpha(z)\|_2\le S\) for all \(z\) and \(\alpha\).

If \(0<T<2\), put \(q=|1-T|<1\). The elementary estimate
\[
\|F_{T,\alpha}(z)\|_2\le q\|z\|_2+TS
\]
shows that the ball of radius \(1+TS/(1-q)\) is forward-invariant; iterating the same inequality proves that each bounded set enters it in finite time.

The endpoint requires a different argument. For every \(u\ge0\),
\[
u(1-\tanh u)=\frac{2u}{e^{2u}+1}\le2ue^{-2u}\le e^{-1}.
\]
Therefore \(z_i\tanh(\alpha z_i)\ge|z_i|-1/(e\alpha)\) for \(i=1,2\). The off-diagonal and forcing terms satisfy
\[
-z_1\tanh(\alpha z_2)+z_2\tanh(\alpha z_1)+b\cdot z
\ge-\frac{13}{10}(|z_1|+|z_2|).
\]
It follows, exactly, that
\[
z\cdot G_\alpha(z)\ge\frac25(|z_1|+|z_2|)-\frac{17}{5e\alpha}.
\]
At \(T=2\), write \(F_{2,\alpha}(z)=-z+2G_\alpha(z)\). With \(r=\|z\|_2\), the squared radial defect obeys
\[
\|F_{2,\alpha}(z)\|_2^2-r^2
=-4z\cdot G_\alpha(z)+4\|G_\alpha(z)\|_2^2
\le-\frac85r+\frac{68}{5e\alpha}+H^2.
\]
Let \(\rho_\alpha=\frac58(H^2+68/(5e\alpha)+1)\). Whenever \(r\ge\rho_\alpha\), the squared radius decreases by at least one. If \(r<\rho_\alpha\), the triangle inequality gives \(\|F_{2,\alpha}(z)\|_2\le r+H\le\rho_\alpha+H\). Hence the closed radius-\(R_\alpha=\rho_\alpha+H\) ball is forward-invariant; every trajectory outside it enters after finitely many steps, and the bound on the entry time is uniform for bounded sets of starts.

A continuous map on \(\mathbb R^2\) with a forward-invariant compact absorbing ball \(K\) has a compact global attractor \(\mathcal A=\bigcap_{n\ge0}F^n(K)\). Indeed the nonempty nested compact sets converge to their intersection in one-sided Hausdorff distance; continuity gives \(F(\mathcal A)=\mathcal A\); and absorption transports attraction from \(K\) to every bounded set.

Finally, if \(T>2\), the reverse triangle inequality yields
\[
\|F_{T,\alpha}(z)\|_2\ge(T-1)\|z\|_2-TS.
\]
For \(r\ge2TS/(T-2)\), the right side is at least \((T/2)r\). This inequality propagates because \(T/2>1\), proving the asserted geometric escape for every point outside that explicit ball. Its existence rules out attraction of all bounded sets by a compact set, proving sharpness.

## Verification
The standalone standard-library program `check_bounds.py` performs exact-rational checks on the coefficient identities and the coercivity margin \(2/5\), then runs reproducible finite diagnostics for all three step regimes. It passed 1,050 deterministic assertions. The global and infinite statements are established by the preceding inequalities; the finite numerical diagnostics serve only as consistency checks.

## Relationship to prior work
Buscarino, Famoso and Fortuna [1] introduce exactly this sigmoid Euler map and study equilibria, bifurcation diagrams, spikes, noise and bounded numerical attractors, including parameter examples with \(T=2.3\). Their full open-access article does not provide the global absorbing-set frontier or the noncontracting endpoint proof. In particular, their observations of bounded attractors for \(T>2\) are consistent with the theorem: the theorem excludes *global* attraction there but permits coexistence with local bounded invariant sets. Classical discrete neural-network stability studies [2,3] give results for other network models and often address fixed-point attraction or gain constraints, not this exact large-state boundedness threshold with the critical endpoint. The general reverse-triangle argument explains the supercritical escape; the model-specific coercivity inequality is required for the included endpoint.

## Limitations
The absorbing radii are explicit sufficient bounds, not claimed optimal. The theorem does not classify the attractors, their invariant measures, the extent of their basins or their local bifurcations. Compact invariant sets can persist for \(T>2\). All claims concern ideal real arithmetic and deterministic dynamics, not finite-word hardware clipping or a stochastic perturbation. Generic prior results on ultimate boundedness might cover some general ingredients even if no source proving this exact full threshold was identified; the publication-priority comparison is limited to the inspected sources.

## References
[1] A. Buscarino, C. Famoso, L. Fortuna, *Bifurcations in a new two-cell spiking map: a numerical and experimental study*, Nonlinear Dynamics 111 (2023), 20361–20375. DOI: 10.1007/s11071-023-08897-7. Open full text: https://link.springer.com/article/10.1007/s11071-023-08897-7 (published 2023-09-27).

[2] C. M. Marcus, R. M. Westervelt, *Dynamics of iterated-map neural networks*, Physical Review A 40 (1989), 501. DOI: 10.1103/PhysRevA.40.501 (abstract consulted).

[3] B. Cessac, *Absolute stability criterion for discrete time neural networks*, Journal of Physics A 27 (1994), L927. DOI: 10.1088/0305-4470/27/24/004 (abstract consulted).
