# A sharp six-to-seven placement switch in two-absorber quantum capture on triangular graphs

## Finding
For the triangular graph \(T_n=J(n,2)\) with \(n\ge5\), two equally strong absorbers capture exactly five coherent modes, regardless of whether their vertices intersect as two-element subsets (adjacent geometry, \(g=\mathrm a\)) or do not intersect (disjoint geometry, \(g=\mathrm d\)). Nonetheless the fastest *conditional* mean capture time changes its preferred geometry sharply with system size:
\[
T_{\mathrm a}^*<T_{\mathrm d}^*\quad(n=5,6),\qquad
T_{\mathrm d}^*<T_{\mathrm a}^*\quad(n\ge7).
\]
The unconditional eventual capture probability of an initially maximally mixed excitation is the same in both cases, namely \(5/\binom n2\). The mean time is conditioned on capture because the orthogonal dark subspace survives indefinitely.

Write \(T_g(\kappa)=\frac15\big(a_g(n)/\kappa+b_g(n)\kappa\big)\). All four coefficients are strictly positive, and are exactly
\[
\begin{aligned}
a_{\mathrm a}(n)&=\frac{3n^5-13n^4-35n^3+285n^2-536n+320}{4(n-3)^2(3n-8)},\\
b_{\mathrm a}(n)&=\frac{3n^3+59n^2-383n+545}{64(n-3)^2(3n-8)},\\
a_{\mathrm d}(n)&=\frac{(n-1)(n^4-5n^3+4n^2+16n-32)}{4(n-4)(n^2-5n+8)},\\
b_{\mathrm d}(n)&=\frac{n^3+12n^2-68n+64}{64(n-4)(n^2-5n+8)}.
\end{aligned}
\]
Each geometry has the *unique* loss-rate optimum
\[
\kappa_g^*=\sqrt{a_g(n)/b_g(n)},\qquad T_g^*=\frac25\sqrt{a_g(n)b_g(n)}.
\]
A stronger fixed-rate classification holds: adjacent is strictly faster for every \(\kappa>0\) at \(n=5\); disjoint is strictly faster for every \(\kappa>0\) at \(n\ge8\); at \(n=6\) and \(n=7\), adjacent is faster below a unique rate and disjoint above it, with the exact crossings \(\kappa^2=59392/293\) and \(\kappa^2=2500/51\), respectively. Equality holds at those two rates.

## Assumptions and scope
Let \(n\in\mathbb Z\), \(n\ge5\), and \(V=\{\{i,j\}:1\le i<j\le n\}\). The real symmetric adjacency \(A\) has \(A_{uv}=1\) precisely when distinct \(u,v\in V\) intersect. Hopping is one in the chosen energy and time units. For absorber vertices \(u\ne v\), let \(P_u=|u\rangle\langle u|\) and similarly \(P_v\). The no-jump generator is
\[
L=-\mathrm i A-\frac{\kappa}{2}(P_u+P_v),\qquad\kappa>0.
\]
The state before normalization after no jump is \(\rho_t=e^{Lt}\rho_0 e^{L^\dagger t}\), where \(\rho_0=I/\binom n2\). The absorption law is \(1-\lim_{t\to\infty}\operatorname{Tr}\rho_t\). Conditional mean time means \(\big(\int_0^\infty (\operatorname{Tr}\rho_t-\operatorname{Tr}\rho_\infty)\,dt\big)/P_{\mathrm{capture}}\), where the persistent dark component is subtracted. This convention makes the comparison meaningful even though most initial population is not captured.

## Proof
**1. Exact active spectrum.** The triangular graph is strongly regular. Its three distinct adjacency eigenvalues are
\[
E_0=2(n-2),\qquad E_1=n-4,\qquad E_2=-2.
\]
For each \(i\), the orthogonal spectral projector is the Lagrange polynomial \(Q_i=\prod_{j\ne i}(A-E_jI)/(E_i-E_j)\). In particular, its diagonal and off-diagonal entries follow from \((A^2)_{uu}=2(n-2)\), \((A^2)_{uv}=n-2\) for adjacent vertices and \((A^2)_{uv}=4\) for disjoint vertices.

The orthonormal symmetric and antisymmetric absorber states \(v_\pm=(|u\rangle\pm|v\rangle)/\sqrt2\) are supported in independent invariant sectors. Their weights \(w_{i,\pm}=\|Q_i v_\pm\|^2=\langle u|Q_i|u\rangle\pm\langle u|Q_i|v\rangle\) are, for adjacent absorbers,
\[
\begin{array}{c|cc}
& w_{i,+}&w_{i,-}\\\hline
E_0&\frac4{n(n-1)}&0\\
E_1&\frac{3n-8}{n(n-2)}&\frac1{n-2}\\
E_2&\frac{(n-3)^2}{(n-2)(n-1)}&\frac{n-3}{n-2}
\end{array}
\]
and, for disjoint absorbers,
\[
\begin{array}{c|cc}
& w_{i,+}&w_{i,-}\\\hline
E_0&\frac4{n(n-1)}&0\\
E_1&\frac{2(n-4)}{n(n-2)}&\frac2{n-2}\\
E_2&\frac{n^2-5n+8}{(n-2)(n-1)}&\frac{n-4}{n-2}
\end{array}.
\]
All entries other than \(w_{0,-}\) are positive for \(n\ge5\), and each column sums to one. The symmetric sector has exactly three active energy directions and the antisymmetric sector exactly two. The remaining \(\binom n2-5\) dimensions are dark. On the active subspace no eigenstate is orthogonal to both absorbers, so finite-dimensional dissipative dynamics absorbs all active population for every \(\kappa>0\); thus the captured fraction is exactly \(5/\binom n2\).

**2. Rank-one integrated-survival identity.** Consider any diagonal Hermitian \(D=\operatorname{diag}(e_1,\ldots,e_r)\) with distinct real energies and normalized absorber vector with strictly positive spectral weights \(w_j\). Set \(G=-\mathrm iD-\kappa vv^\dagger/2\), and \(X=\int_0^\infty e^{Gt}e^{G^\dagger t}\,dt\). Then \(GX+XG^\dagger=-I\). Rephase the energy eigenvectors so \(v_j=\sqrt{w_j}\). The diagonal Lyapunov equations give \(\operatorname{Re}[(Xv)_j/v_j]=1/(\kappa w_j)\), and the off-diagonal equations yield
\[
z_j:=\operatorname{Im}[(Xv)_j/v_j]=\frac1{2w_j}\sum_{k\ne j}\frac{w_j+w_k}{e_j-e_k}.
\]
Substituting into the diagonal entries and symmetrizing gives the *exact* trace formula
\[
\operatorname{Tr}X=\frac1\kappa\sum_{j=1}^r\frac1{w_j}
+\frac\kappa4\sum_{j=1}^r\frac1{w_j}
\left(\sum_{k\ne j}\frac{w_j+w_k}{e_j-e_k}\right)^2.
\]
This follows algebraically from the Lyapunov equation and is not a fit to finite experiments. Its coefficients are positive when there are at least two coupled distinct energies.

**3. Exact lifetime and minimization.** Apply this identity separately in the \(+\) and \(-\) sectors, using the five nonzero weights above. The two absorber projectors restrict to independent rank-one projectors in those sectors. Substituting \(E_0,E_1,E_2\), simplifying rational functions, and summing the traces gives exactly the displayed \(a_g,b_g\). The maximally mixed state restricted to the five-dimensional active space is \(I_5/5\), hence the factor \(1/5\). Strict positivity makes \(a_g/\kappa+b_g\kappa\) strictly convex, with the unique optimizer and minimum stated above.

**4. Sharp change of optimum.** The common denominator of \(a_{\mathrm a}b_{\mathrm a}-a_{\mathrm d}b_{\mathrm d}\), after reduction, is
\[
256(n-4)^2(n-3)^4(3n-8)^2(n^2-5n+8)^2>0.
\]
Its numerator \(P(n)\) has the following coefficients when expanded in nonnegative powers of \(n-7\), in ascending order:
\[
(8223720192,32857173120,54887442496,52894431360,33445509260,14804489932,4747654751,1120678088,195073053,24746906,2223113,133732,4815,78).
\]
Every coefficient is positive. Thus \(P(n)>0\) for every \(n\ge7\). Direct exact evaluation shows \(P(5)<0\) and \(P(6)<0\), which proves the claimed switch, since \(T_g^*\) is strictly increasing with \(a_gb_g\). For fixed \(\kappa\), the difference has sign \(\operatorname{sgn}[(a_{\mathrm a}-a_{\mathrm d})/\kappa+(b_{\mathrm a}-b_{\mathrm d})\kappa]\). Exact factorization and positive coefficients after the shift \(n\mapsto n+8\) show both differences are positive for all \(n\ge8\); at \(n=5\) they are both negative; at \(n=6,7\), the first is negative and the second positive. Solving the unique linear equation in \(\kappa^2\) yields the stated crossings.

## Verification
The bundled `check_triangular.py` reconstructs \(T_n\) from two-element subsets, checks exact spectral weights and four rational coefficients with symbolic arithmetic, and proves the all-size placement inequality using a positive shifted polynomial. As an independent finite-graph cross-check, it builds the actual adjacency matrices for \(n=5,6,7,8,9\), extracts each five-dimensional Krylov space from the two original site vectors, and solves 30 independent continuous-time Lyapunov equations at three positive loss rates. The resulting lifetime traces match the closed formulas. Run `python check_triangular.py` after installing packages from `requirements.txt`. The machine-readable `PLACEMENT_CERTIFICATE.json` records the inequality certificate.

## Relationship to prior work
Varbanov, Krovi and Brun (2008) study continuous quantum-walk hitting times and their dependence on measurement rate, using a Poisson measurement model rather than the present no-jump local-loss generator. Novo and collaborators (first posted 2014) establish invariant-subspace methods and coherent transport efficiency for local absorption, including an illustrative optimum on a small graph. Lugão, Portugal, Sabri and Tanaka (first posted 2022) analyze *two marked vertices in general Johnson graphs* under a Hermitian search Hamiltonian and a coherent uniform initial state; their projector machinery and the distinction between marked-vertex distances are highly relevant, but their algorithmic search running time and large-size success probability are different observables from the present conditional absorbing lifetime. The prior general machinery and five-dimensional spectral reduction are not claimed as new. The assessed contribution is the exact finite-size lifetime functions and the sharp placement switch in optimized dissipative capture.

## Limitations
Only integer \(n\ge5\), uniform unit hopping, two equal positive local decay rates, and an initially maximally mixed single-excitation state are covered. The mean time is conditional on capture: the unconditional expected time to absorb all initial population is infinite because a dark subspace remains. Different site-dependent loss rates, dephasing, disorder, interactions, alternate initial ensembles, and experimental device performance are outside the result. Historical priority has not received an independent audit; in particular the general Johnson two-marked-vertex literature is extensive.

## References
- M. Varbanov, H. Krovi, T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (first posted 24 March 2008). https://arxiv.org/abs/0803.3446
- L. Novo, S. Chakraborty, M. Mohseni, H. Neven, Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (first posted 22 December 2014). https://arxiv.org/abs/1412.7209
- P. H. G. Lugão, R. Portugal, M. Sabri, H. Tanaka, *Multimarked Spatial Search by Continuous-Time Quantum Walk*, arXiv:2203.14384 (first posted 27 March 2022). https://arxiv.org/abs/2203.14384
