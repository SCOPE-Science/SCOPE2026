# Geodesic and triangle fingerprints of strongly nonlinear quantum walks

## Finding
For a finite connected simple graph and a localized initial state, the large attractive Kerr coefficient has a graph-structural dynamical signature, not merely a localization bound. The order of each remote amplitude identifies its shortest-path distance, its leading coefficient counts geodesics, and the first correction to total leakage identifies the number of triangles through the starting vertex. The same theorem proves that the sharp worst-time leakage has leading coefficient four times the starting degree.

For the evolution defined below, write \(d(o,v)\) for graph distance, \(N(o,v)\) for the number of geodesics from \(o\) to \(v\), \(d_o\) for the starting degree, and \(T_o\) for the number of triangles containing \(o\). For each integer \(h\ge 1\), set
\[
R_h(s)=e^{is}-\sum_{k=0}^{h-1}\frac{(is)^k}{k!}.
\]
Then, for each fixed \(S>0\) and every \(v\ne o\) at distance \(h\), uniformly for \(0\le s\le S\),
\[
\psi_v(s/g)=g^{-h}N(o,v)R_h(s)+O_{G,S}(g^{-h-1}). \tag{1}
\]
Consequently the leading rescaled occupation is \(N(o,v)^2|R_h(s)|^2\), whenever \(R_h(s)\ne0\). Moreover,
\[
1-|\psi_o(s/g)|^2=\frac{4d_o\sin^2(s/2)}{g^2}
+\frac{4T_o\,[2(1-\cos s)-s\sin s]}{g^3}
+O_{G,S}(g^{-4}). \tag{2}
\]
In particular,
\[
\lim_{g\to\infty}g^3\left(1-|\psi_o(\pi/g)|^2-\frac{4d_o}{g^2}\right)=16T_o. \tag{3}
\]
The uniform-in-time leading worst-case occupation loss satisfies
\[
\lim_{g\to\infty}g^2\sup_{t\ge0}\bigl(1-|\psi_o(t)|^2\bigr)=4d_o. \tag{4}
\]

## Assumptions and scope
Let \(G=(V,E)\) be any finite connected simple undirected unweighted graph with \(|V|\ge2\), adjacency matrix \(A\), and distinguished root \(o\). Let \(g>0\) be the Kerr coupling. The deterministic cubic nonlinear Schrödinger evolution is
\[
i\frac{d}{dt}\psi_v(t)=-\sum_{u\sim v}\psi_u(t)-g|\psi_v(t)|^2\psi_v(t),
\qquad \psi_v(0)=\mathbf 1_{\{v=o\}}.
\]
This normalization makes hopping amplitudes unity, total mass one, and the initial energy \(-g/2\). The asymptotics hold as \(g\to\infty\) on compact rescaled-time intervals \(s=gt\), with \(G\) fixed. The constant in the local \(O\)-terms may depend on the graph and on \(S\), and the bounds are uniform across finitely many vertices. The supremum in (4), unlike (1)–(3), ranges over all physical times \(t\ge0\).

## Proof
**Mass and energy.** The finite-dimensional polynomial flow preserves \(\sum_v|\psi_v|^2=1\), and its conserved Hamiltonian is
\[
H(\psi)=-\langle\psi,A\psi\rangle-\frac g2\sum_v|\psi_v|^4=-\frac g2.
\]
The vector field has no finite-time escape because the mass-one sphere is compact, so all-time solutions exist.

**Geodesic expansion.** Substitute \(s=gt\), \(\epsilon=1/g\). Then
\[
\frac{d\psi_v}{ds}=i\epsilon\sum_{u\sim v}\psi_u+i|\psi_v|^2\psi_v.
\]
At \(\epsilon=0\), the unique solution is \(\psi_o(s)=e^{is}\) and \(\psi_v(s)=0\) for \(v\ne o\). The finite-dimensional polynomial real vector field permits a Taylor expansion in \(\epsilon\), uniform on each compact real \(s\)-interval. Differentiate this flow successively at \(\epsilon=0\): because a hopping factor contributes one power of \(\epsilon\), the coefficient of \(\epsilon^k\) at a vertex more than \(k\) edges from \(o\) is zero. At any vertex of distance \(h\), cubic on-site contributions first occur in degree at least \(3h>h\) and thus do not affect the leading coefficient. The leading coefficients \(C_v(s)\) obey
\[
C_o(s)=e^{is},\qquad
C_v'(s)=i\sum_{u\sim v:\ d(o,u)=h-1}C_u(s),\quad C_v(0)=0
\]
for \(d(o,v)=h\ge1\). The geodesic counts obey the same predecessor recursion, and \(R_1'(s)=ie^{is}\), \(R_h'(s)=iR_{h-1}(s)\) for \(h\ge2\). Hence \(C_v=N(o,v)R_h\), proving (1). It also gives \(g^{2h}|\psi_v(s/g)|^2=N(o,v)^2|R_h(s)|^2+O_{G,S}(g^{-1})\).

**The first motif correction.** Since \(A_{oo}=0\), the coefficient of \(\epsilon\) at the root vanishes. The nonlinear response of an off-root site first occurs at cubic order in its amplitude. Therefore, for every neighbor \(v\sim o\), the first two coefficients are
\[
\psi_v(s/g)=\epsilon R_1(s)+\epsilon^2(A^2)_{vo}R_2(s)+O_{G,S}(\epsilon^3).
\]
Every vertex at distance at least two contributes only \(O(\epsilon^4)\) to off-root occupation. Summing neighbor probabilities and using mass conservation yields
\[
1-|\psi_o|^2=\epsilon^2d_o|R_1(s)|^2
+2\epsilon^3\operatorname{Re}(\overline{R_1(s)}R_2(s))
\sum_{v\sim o}(A^2)_{vo}+O_{G,S}(\epsilon^4).
\]
Each triangle at \(o\) generates two closed length-three walks, so \(\sum_{v\sim o}(A^2)_{vo}=(A^3)_{oo}=2T_o\). Finally \(|R_1(s)|^2=2(1-\cos s)\) and \(\operatorname{Re}(\overline{R_1}R_2)=2(1-\cos s)-s\sin s\), proving (2). Evaluating at \(s=\pi\) proves (3).

**Global sharpness.** Let \(q(t)=\sum_{v\ne o}|\psi_v(t)|^2\) and \(B\) be the adjacency matrix on \(V\setminus\{o\}\), with \(M=\|B\|_{\mathrm{op}}\). Energy conservation gives
\[
\langle\psi,A\psi\rangle=\frac g2\bigl(1-\sum_v|\psi_v|^4\bigr),
\qquad
 gq(1-q)\le2\sqrt{d_oq(1-q)}+Mq.
\]
The second inequality uses \(\sum_v|\psi_v|^4\le(1-q)^2+q^2\), Cauchy–Schwarz for the root-to-neighbor cross term, and \(\langle\psi_{\ne o},B\psi_{\ne o}\rangle\le Mq\). At \(q=1/2\) the same energy identity would require \(\langle\psi,A\psi\rangle\ge g/4\), which is impossible if \(g>4\|A\|_{\mathrm{op}}\). Because \(q(0)=0\) and \(q\) is continuous, \(q(t)<1/2\) for every time when \(g>4\|A\|_{\mathrm{op}}\).

For \(q\le1/2\), the displayed inequality implies the uniform estimate \(q\le8d_o/(g-2M)^2\) whenever \(g>2M\) (the case \(q=0\) is trivial). Thus \(q=O_G(g^{-2})\) at all times. Dividing that inequality by \(\sqrt{q(1-q)}\) now yields
\[
g\sqrt{q(1-q)}\le2\sqrt{d_o}+M\sqrt{q/(1-q)}
=2\sqrt{d_o}+O_G(g^{-1}),
\]
whence \(\limsup_{g\to\infty}g^2\sup_{t\ge0}q(t)\le4d_o\). At \(t=\pi/g\), formula (2) supplies the reverse \(\liminf\ge4d_o\). This proves (4).

## Verification
The included Python 3 standard-library verifier independently integrates the original finite graph equations (after time rescaling) with a fourth-order Runge–Kutta method. It checks mass, conserved energy, geodesic amplitude limits, leading leakage and the triangle-sensitive next-order coefficient for five distinct graph examples at three couplings. Its **117 finite numerical assertions passed**. These are reproducibility checks, not an exhaustive or infinite proof. The proof above provides the uniform asymptotics and exact global conclusion.

To reproduce, run `python3 verify_strong_kerr.py` using Python 3. No external packages, data, network or environment variables are needed.

## Relationship to prior work
Shi and Wong (2026) investigate self-trapping bounds for nonlinear walks on paths and cycles; their conserved-energy bound already implies an upper bound consistent with the leading \(4d_o/g^2\) order in those graph families. Neither their localization bound nor their definitions are claimed as new here. The present theorem supplies the matching all-time sharp coefficient for an arbitrary finite graph and, separately, the time-resolved geodesic count and triangle corrections (1)–(3). Perakis and Tsironis (2009) study nonlinear network self-trapping numerically in graph ensembles. Bustamante and Molina (2000) identify coordination effects in lattice self-trapping thresholds. The exact dimer dynamics of Kenkre and Campbell (1986) cover the two-vertex special case. These works motivate the structural question but the inspected material did not establish the entire graph-distance and motif asymptotic package.

## Limitations
The graph is fixed while \(g\) grows; error estimates are not uniform over growing graph families or times \(s\) that diverge with \(g\). The first nontrivial motif correction concerns root triangles only and does not classify higher-order cycles. Equation (4) gives the leading maximum leakage but does not classify all times of maximum leakage. The leading upper bound overlaps consequences of conserved-energy prior work, and generic high-coupling perturbative theory could contain an implicit version of the geodesic expansion. The derivation is mathematical, not a claim of experimental realization or independent certification.

## References
1. Y. Shi and T. G. Wong, *Self-Trapping Bounds for Continuous-Time Nonlinear Quantum Walks on Path and Cycle Graphs*, arXiv:2605.20464, version 1 publicly posted 2026-05-19, version 2 read for comparison, https://arxiv.org/abs/2605.20464.
2. F. Perakis and G. P. Tsironis, *Discrete nonlinear Schrödinger equation dynamics in complex networks*, arXiv:0909.3172, https://arxiv.org/abs/0909.3172.
3. C. A. Bustamante and M. I. Molina, *Universal features of self-trapping in nonlinear tight-binding lattices*, Physical Review B 62, 15287 (2000), DOI:10.1103/PhysRevB.62.15287.
4. V. M. Kenkre and D. K. Campbell, *Self-trapping on a dimer: Time-dependent solutions of a discrete nonlinear Schrödinger equation*, Physical Review B 34, 4959(R) (1986), DOI:10.1103/PhysRevB.34.4959 (abstract consulted).
