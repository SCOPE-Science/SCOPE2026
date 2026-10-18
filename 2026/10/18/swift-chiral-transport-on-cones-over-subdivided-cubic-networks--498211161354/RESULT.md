# Swift chiral transport on cones over subdivided cubic networks

## Finding

Let \(G\) be any finite, connected, simple, \(3\)-regular graph. Form its **one-subdivision** \(S(G)\) by replacing each edge \(e=uv\) with \(u-x_e-v\), and then form the cone \(C(G)\) by joining an apex \(o\) to every vertex of \(S(G)\). Write
\[
N=|V(S(G))|=|V(G)|+|E(G)|=\frac{5}{2}|V(G)|.
\]
A *chiral adjacency Hamiltonian* means a zero-diagonal Hermitian matrix \(H\) supported exactly on the edges of \(C(G)\), with every nonzero entry of modulus one and opposite orientations complex-conjugate. Starting from the apex, call the dynamics **swift** if
\[
\left|\langle o|e^{-itH}|o\rangle\right|^2
   =\cos^2(\sqrt N\,t)\quad\text{for every real }t.
\]

**Theorem.** A swift chiral adjacency Hamiltonian on \(C(G)\) exists **if and only if \(G\) is bipartite**. In that case one can arrange, at the quantum-speed-limit time \(t_*=\pi/(2\sqrt N)\),
\[
\left|\langle v|e^{-it_*H}|o\rangle\right|^2=\frac1N
\quad(v\in V(S(G))),\qquad
\left|\langle o|e^{-it_*H}|o\rangle\right|^2=0.
\]

There is also a complete description of all phase assignments. Gauge-fix the apex bonds to \(H_{ov}=1\). For a bipartition \(V(G)=U\sqcup W\), let \(\omega=e^{2\pi i/3}\), and let \(c:E(G)\to\{0,1,2\}\) be any proper \(3\)-edge-colouring. Every swift Hamiltonian in this apex gauge is uniquely obtained from some \(\zeta\in\mathbb T\) and \(c\) by
\[
H_{u,x_e}=\zeta\omega^{c(e)}\quad(u\in U),\qquad
H_{w,x_e}=-\zeta\omega^{c(e)}\quad(w\in W),
\]
with opposite entries conjugated, and no other base edges. Two pairs \((\zeta,c)\) describe the same phase assignment precisely when they differ by a simultaneous cyclic rotation of the three colours and the inverse cube-root rotation of \(\zeta\). In particular, before any further physical gauge quotient, the solution space is a disjoint union of \(\#\operatorname{Col}_3(G)/3\) circles.

## Assumptions and scope

All graphs are finite, simple, connected, and undirected before assigning complex phases. The original graph \(G\) has degree exactly three at every vertex; inserted midpoint vertices in \(S(G)\) have degree two. All cone and subdivision edge strengths have modulus exactly one. On-site potentials are identically zero. The Hamiltonian is not a combinatorial Laplacian, and the theorem does not allow freely tuned diagonal entries. The apex gauge fixes phases on edges incident to \(o\); it does not discard physical edge-phase solutions because diagonal-unitary switching preserves transition probabilities.

The class is a natural chiral quantum-transport design problem: subdividing bonds introduces physical intermediate nodes, and the question is whether phase-only controls can still produce the fastest apex departure and exact simultaneous equal-population arrival on the intermediate network.

## Proof

**1. A short-time rigidity identity.** A diagonal-unitary gauge change makes all apex bonds have phase \(1\). Order \(o\) first and the \(N\) base vertices after it, so
\[
H=\begin{pmatrix}0&\mathbf1^{\mathsf T}\\\mathbf1&B\end{pmatrix},
\qquad B=B^*,\quad B_{vv}=0.
\]
The first two nontrivial even apex moments are
\[
(H^2)_{oo}=N,\qquad
(H^4)_{oo}=\|H^2e_o\|_2^2=N^2+\|B\mathbf1\|_2^2.
\]
Taylor expansion of the survival amplitude, including its possibly nonzero cubic imaginary term, therefore gives the probability identity
\[
|\langle o|e^{-itH}|o\rangle|^2
=1-Nt^2+\left(\frac{N^2}{3}
       +\frac{\|B\mathbf1\|_2^2}{12}\right)t^4+O(t^6).
\]
The target \(\cos^2(\sqrt N\,t)\) has fourth coefficient \(N^2/3\), so swift evolution **requires** \(B\mathbf1=0\). Conversely, if \(B\mathbf1=0\), the two-dimensional span of \(e_o\) and \((0,\mathbf1/\sqrt N)\) is invariant, and the restriction of \(H\) is \(\begin{psmallmatrix}0&\sqrt N\\\sqrt N&0\end{psmallmatrix}\). Consequently
\[
e^{-itH}e_o=\cos(\sqrt N\,t)e_o
-i\sin(\sqrt N\,t)(0,\mathbf1/\sqrt N),
\]
which proves both the swift law and the asserted exactly uniform base probabilities at \(t_*\). Thus the problem is **equivalent** to classifying the supported unit-gain matrices \(B\) satisfying \(B\mathbf1=0\).

**2. Local three-phase rigidity.** For every original vertex \(u\) and incident original edge \(e\), write \(z_{u,e}=B_{u,x_e}\in\mathbb T\). The zero-row condition at \(x_e\) is
\[
\overline{z_{u,e}}+\overline{z_{v,e}}=0,
\qquad\text{hence}\qquad z_{v,e}=-z_{u,e}.
\]
At each original cubic vertex \(u\), the three numbers \(z_{u,e}\) have modulus one and sum zero. Such a triple is necessarily, in some order,
\[
\zeta_u,\qquad\zeta_u\omega,\qquad\zeta_u\omega^2.
\]
Indeed, if unit vectors \(a,b,c\) sum to zero, then \(|a+b|=|c|=1\), whence \(2+2\operatorname{Re}(a\overline b)=1\); the pairwise angular separations are \(2\pi/3\). Let \(\mu_3=\{1,\omega,\omega^2\}\), and call \(\zeta_u\mu_3\) the local phase coset.

**3. Odd cycles are forbidden.** Along every original edge \(uv\), the endpoint equation in Step 2 forces
\[
\zeta_v\mu_3=-\zeta_u\mu_3.
\]
Traversing an original cycle of length \(\ell\) yields \(\zeta_u\mu_3=(-1)^\ell\zeta_u\mu_3\). For odd \(\ell\) this would require \(-1\in\mu_3\), which is false. Hence a swift assignment forces \(G\) to have no odd cycle and therefore to be bipartite.

**4. Construction on every bipartite cubic graph.** Write \(G=(U,W,E)\). A cubic bipartite graph admits a proper \(3\)-edge-colouring: for any \(X\subseteq U\), counting the three edges at each vertex shows \(3|X|\le3|N_G(X)|\). Hall's condition supplies a perfect matching. Removing it leaves a \(2\)-regular bipartite graph, a disjoint union of even cycles, whose edges alternate between two further colours. Use these three colours in the formula of the Finding, with any \(\zeta\in\mathbb T\). At each cubic vertex the incident phases sum to \(\pm\zeta(1+\omega+\omega^2)=0\); each midpoint sees two opposite phases, and its row also sums to zero. Thus \(B\mathbf1=0\), and Step 1 supplies swift dynamics.

**5. Exhaustiveness of the phase parameters.** Given any solution, Step 3 and connectedness imply a *single* coset \(\zeta\mu_3\) at all vertices of \(U\), and \(-\zeta\mu_3\) at all vertices of \(W\). At every vertex the three incident labels occur once each; these labels therefore define a proper \(3\)-edge-colouring \(c\) of \(G\). Conversely Step 4 realizes each such \((\zeta,c)\). Two representations coincide exactly when \(\zeta' /\zeta\in\mu_3\) and the colours shift by the inverse common residue. The action of \(\mu_3\) on labelled colourings is free, establishing the asserted circle count.

## Verification

The accompanying dependency-free `verify_swift_subdiv.py` constructs five connected cubic examples: \(K_4\), \(K_{3,3}\), the three-cube \(Q_3\), the triangular prism, and the Petersen graph. Exact pair-of-integers arithmetic in \(\mathbb Z[\omega]\) checks row-sum cancellation for every labelled \(3\)-edge-colouring of \(K_{3,3}\) and \(Q_3\), respectively \(12\) and \(24\) assignments. A separate direct integer walk count verifies the fourth moment in each example. A truncated independent matrix-exponential Taylor computation verifies zero apex probability and equal base probabilities at \(t_*\) for one construction on each bipartite example, with maximum entrywise probability error below \(2\times10^{-12}\). Reproduce using `python3 verify_swift_subdiv.py`.

These examples corroborate the formulas but cannot prove the unrestricted equivalence. The proof is the all-graph argument above.

## Relationship to prior work

Frigerio and Paris introduced swift chiral walks and the reduction to zero-row-sum chiral adjacency matrices (arXiv:2207.05168, Secs. 3–4). They established swift-phase constructions for even-degree graphs and an exact perfect-matching criterion for cubic graphs, and identified the broader nonregular classification as open. The one-subdivision \(S(G)\) is nonregular, with degrees two and three; their existence results do not decide its phase configurations. Their general cone criterion supplies context, while the bipartiteness obstruction, the converse construction, and the complete circle parametrization here use the original edge-midpoint constraints. The new conclusion does not follow by applying their cubic theorem to \(G\): even a nonbipartite \(3\)-edge-colourable graph such as \(K_4\) fails after subdivision.

The quantum-walk framework of Coutinho et al., *Irrational quantum walks* (arXiv:2208.08971; primary MSC 81P68), develops exact spectral and mixing methods for integral Hamiltonians. Its statements do not themselves give phase-only swift attainability on these complex-weighted cones. Belardo and Brunetti study a separate \(-2\)-eigenvalue problem for line graphs of complex unit-gain graphs; its public abstract does not resolve the phase-design equivalence here, although that literature remains a source of potential broader spectral overlap.

## Limitations

The classification concerns only connected simple cubic original graphs, each original edge subdivided exactly once, zero diagonal, and all edge magnitudes one. It does not classify other subdivision lengths, arbitrary graph degrees, freely variable on-site potentials, or generic weighted quantum walks. The raw circle classification is in the fixed apex gauge, before any quotient by additional physical equivalences. No assertion about *every* possible way to attain an isolated orthogonality event without the full swift time profile is needed. Searches of the available research index and accessible papers cannot establish universal publication priority; broader unit-gain graph results could conceal an equivalent formulation.

## References

1. M. Frigerio and M. G. A. Paris, *Swift chiral quantum walks*, arXiv:2207.05168 (first public 11 July 2022), Linear Algebra and its Applications **673** (2023), 28–45. https://arxiv.org/abs/2207.05168
2. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971 (first public 18 August 2022), SIAM Journal on Applied Algebra and Geometry **7** (2023). https://arxiv.org/abs/2208.08971
3. F. Belardo and M. Brunetti, *Line graphs of complex unit gain graphs with least eigenvalue \(-2\)*, Electronic Journal of Linear Algebra **37** (2021). https://doi.org/10.13001/ela.2021.5249
