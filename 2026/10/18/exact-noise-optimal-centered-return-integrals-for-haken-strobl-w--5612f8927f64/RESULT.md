# Exact noise-optimal centered return integrals for Haken–Strobl walks on complete bipartite graphs

## Finding

A complete bipartite graph has two vertex classes of sizes \(a,b\in\mathbb N\), with \(n=a+b\ge2\). A particle starts at a vertex \(0\) of the class of size \(a\). With adjacency Hamiltonian \(JA\), \(J>0\), and uniform Haken–Strobl site dephasing \(\gamma>0\), let \(p(t)=\rho_{00}(t)\). The signed centered integrated return
\[
T_{a,b}(\gamma,J)=\int_0^\infty\frac{np(t)-1}{n-1}\,dt
\]
is exactly
\[
\boxed{T_{a,b}=\frac{[n(n-1)-b]\gamma}{2bJ^2n(n-1)}+\frac{[n(n-1)(n-2)-bn^2+4b^2]}{2\gamma n(n-1)}.}
\]
With \(K=n(n-1)-b\) and \(R=n(n-1)(n-2)-bn^2+4b^2\), for \(n\ge3\) the unique global minimizer and minimum are
\[
\boxed{\gamma_*=J\sqrt{\frac{bR}{K}},\qquad T_*=\frac{\sqrt{KR/b}}{Jn(n-1)}.}
\]
For \(n=2\), \(T_{1,1}=\gamma/(4J^2)\), so there is no positive minimizer. For fixed \(a\) and \(b\to\infty\),
\[
\frac{\gamma_*}{J\sqrt b}\to\sqrt{a+1},\qquad J\sqrt b\,T_*\to\sqrt{a+1}.
\]
For any sequence with \(a/n\to\theta\in(0,1)\),
\[
\frac{\gamma_*}{Jn}\to\sqrt{\theta(1-\theta)},\qquad JT_*\to\sqrt{\frac{\theta}{1-\theta}}.
\]

## Assumptions and scope

The vertex basis is the canonical basis of \(\mathbb C^n\), \(A\) is the simple unweighted adjacency matrix of \(K_{a,b}\), \(H=JA\), and \(\hbar=1\). The dynamics is
\[
\dot\rho=-i[H,\rho]+\gamma\sum_{v=1}^{n}\left(P_v\rho P_v-\tfrac12\{P_v,\rho\}\right)
=-i[JA,\rho]+\gamma(\operatorname{diag}\rho-\rho),
\quad \rho(0)=P_0.
\]
Here \(P_v=|v\rangle\langle v|\). This dephasing normalization damps each off-diagonal entry at rate exactly \(\gamma\). The integral is a signed autocorrelation time normalized to have initial integrand one. More precisely, in the stationary state \(\pi=I/n\), the connected two-time occupation correlation \(C(t)=\operatorname{tr}[P_0e^{t\mathcal L}(P_0\pi)]-1/n^2\) obeys \(C(t)/C(0)=[np(t)-1]/(n-1)\). Thus the integral is the exact zero-frequency normalized equilibrium-occupation autocorrelation. It is not an absolute-distance integral, a first passage time, or an operational mixing time. The initial class is distinguished: exchanging \(a,b\) changes the initialization and can change the answer.

## Proof

**Strict equilibration.** The generator preserves trace and has fixed point \(I/n\). For any traceless eigenmatrix \(X\), the Hilbert–Schmidt inner product gives
\[
\operatorname{Re}\langle X,\mathcal L X\rangle=-\gamma\sum_{i\ne j}|X_{ij}|^2.
\]
If an eigenvalue had zero real part, its eigenmatrix would be diagonal. Its eigenvalue equation then forces its eigenvalue to be zero and forces \([A,X]=0\). Connectivity of \(K_{a,b}\) makes such a diagonal \(X\) scalar, contradicting tracelessness. Every eigenvalue on the finite-dimensional traceless subspace therefore has strictly negative real part, so convergence to \(I/n\) is exponential and all time integrals below converge absolutely.

**Symmetry reduction.** For \(a\ge2\), use the distinguished vertex \(0\), the other \(a-1\) vertices in its class, and the \(b\) opposite vertices. Permutation symmetry and the bipartite-real structure of the master equation imply that \(x=\rho_{00}\), \(y=\rho_{ii}\) for other first-class vertices, \(z=\rho_{jj}\) for second-class vertices, and within-class off-diagonals \(u=\rho_{0i}\), \(v=\rho_{ii'}\), \(w=\rho_{jj'}\) are real. Set \(\rho_{0j}=ip\) and \(\rho_{ij}=iq\) with real \(p,q\). The equations are
\[
\begin{aligned}
\dot x&=-2bJp,&\dot y&=-2bJq,&\dot z&=2J[p+(a-1)q],\\
\dot u&=-bJ(p+q)-\gamma u,&\dot v&=-2bJq-\gamma v,&\dot w&=2J[p+(a-1)q]-\gamma w,\\
\dot p&=J[x+(a-1)u-z-(b-1)w]-\gamma p,\\
\dot q&=J[u+y+(a-2)v-z-(b-1)w]-\gamma q.
\end{aligned}
\]
An off-diagonal orbit with fewer than two available vertices is absent, and its coefficient in these equations is zero. Initially \(x=1\), all other coordinates vanish. At equilibrium \(x=y=z=1/n\), all off-diagonals vanish.

**Integrate the generator.** Denote integrals of the centered coordinates by uppercase letters \(X,Y,Z,U,V,W,P,Q\). Integrating the three population equations from time zero to infinity gives
\[
P=\frac{n-1}{2bJn},\qquad Q=-\frac1{2bJn},
\]
and integrating the off-diagonal equations gives
\[
U=-\frac{n-2}{2\gamma n},\qquad V=W=\frac1{\gamma n}
\]
for existing orbits. The two imaginary-coherence equations yield
\[
X-Z=\frac{\gamma(n-1)}{2bJ^2n}+\frac{(a-1)(n-2)+2(b-1)}{2\gamma n},
\]
\[
Y-Z=-\frac{\gamma}{2bJ^2n}+\frac{3b-a}{2\gamma n}.
\]
Using the trace constraint \(X+(a-1)Y+bZ=0\), solve
\[
X=\frac{(n-1)(X-Z)-(a-1)(Y-Z)}{n}.
\]
The centered integral is \(nX/(n-1)\). Simplification gives the asserted exact expression. For \(a=1\), use only the existing variables \(x,z,w,p\), with equations \(\dot x=-2bJp\), \(\dot z=2Jp\), \(\dot w=2Jp-\gamma w\), and \(\dot p=J[x-z-(b-1)w]-\gamma p\). Their integrated equations give directly
\[
T_{1,b}=\frac{\gamma}{2J^2(b+1)}+\frac{b-1}{\gamma(b+1)},
\]
which agrees with the general formula, including \(b=1\).

**Sharp optimum and limits.** For \(n\ge3\), \(K=a(n-1)+b(n-2)>0\). An expansion of the other coefficient gives
\[
R=(a+1)b^2+(2a^2-6a+2)b+a(a-1)(a-2).
\]
For \(a=1\), it equals \(2b(b-1)\), positive because \(n\ge3\) entails \(b\ge2\). For \(a=2\), it equals \(b(3b-2)>0\). For \(a\ge3\) every displayed coefficient is nonnegative and the leading one positive. Thus \(T=c_1\gamma+c_2/\gamma\) with both coefficients positive, proving strict convexity and the unique minimizer above by differentiating. For \(n=2\), \(R=0\). The limits follow by dividing \(K,R\) by their respective leading powers: when \(a\) is fixed and \(b\to\infty\), \(K\sim b^2\), \(R\sim(a+1)b^2\); when \(a/n\to\theta\), \(b/n\to1-\theta\), \(K\sim n^2\), \(R\sim\theta n^3\). Substitution proves both pairs of asymptotics.

## Verification

The standalone file `verify.py` independently constructs the full \(n^2\)-dimensional Lindblad generator, solves the zero-frequency resolvent on the traceless sector, and checks the returned integral against the closed form for a grid of graph sizes and positive rates. It also checks the integrated symmetry equations in exact rational arithmetic and tests the optimizer against nearby rates. Execute `python verify.py` after installing packages from `requirements.txt`. This is finite corroboration, not a substitute for the spectral and algebraic proof.

## Relationship to prior work

The open 2022 study by Bressanini, Benedetti and Paris analyzes Haken–Strobl classicalization and noise-induced localization, principally with graph-Laplacian Hamiltonians and quantum–classical distances. The 2025 preprint of Adithya L J et al. compares network topologies, including stars and complete graphs, under several noise models, but studies node occupancies, coherence, fidelity, entropy, and dynamical distances rather than this complete-bipartite signed return resolvent. Neither inspected manuscript gives this two-part, all-size exact integral and its optimization. Earlier quantum-transport work by Razzoli, Bordone, and Paris considers coherent Hamiltonian transport and terminal trapping, not the present dephasing functional. Novo and coauthors construct effective adjacency Hamiltonians on complete bipartite graphs by Floquet engineering; their coherent construction motivates the graph family but does not address Haken–Strobl noise or centered-return optimization.

This comparison is substantive: a graph-Laplacian Hamiltonian \(D-A\) is not a scalar shift of adjacency on an unbalanced complete bipartite graph; its diagonal degree potential changes the dynamics. For a balanced biclique it *is* a scalar shift of negative adjacency, but the inspected prior observable is still different. General finite-dimensional Lindblad resolvent methods are known and not asserted as new. The potentially original content is the exact biclique reduction, the all-size noise optimum, and the distinct balanced versus fixed-part scaling limits.

## Limitations

The result is restricted to uniform adjacency hopping, site-basis pure dephasing at the specified rate normalization, and an initially localized vertex. It is not a mixing-time optimum, an absolute-value integrated distance, or a theorem about spectral gaps. It does not automatically extend to arbitrary graph Laplacians, inhomogeneous hopping, dephasing of different strengths, finite observation windows, or coherent initial superpositions. The main theorem follows from elementary finite-dimensional reduction; an unindexed or implicit earlier evaluation cannot be categorically excluded.

## References

1. Adithya L J, J. Nokkala, J. Piilo, C. Meena, *Stability of Continuous Time Quantum Walks in Complex Networks*, arXiv:2507.17880 (first posted 2025-07-23), https://arxiv.org/abs/2507.17880.
2. G. Bressanini, C. Benedetti, M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, *Quantum Information Processing* 21, 317 (2022), https://doi.org/10.1007/s11128-022-03647-x, arXiv:2204.01836.
3. L. Razzoli, I. Bordone, M. G. A. Paris, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, *Entropy* 23, 85 (2021), https://doi.org/10.3390/e23010085.
4. L. Novo et al., *Floquet engineering of continuous-time quantum walks: towards the simulation of complex and next-to-nearest-neighbor couplings*, *Physical Review A* 103, 042219 (2021), https://doi.org/10.1103/PhysRevA.103.042219, arXiv:2012.00448.
