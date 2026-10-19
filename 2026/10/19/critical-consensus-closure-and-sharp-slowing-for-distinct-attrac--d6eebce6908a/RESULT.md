# Critical consensus closure and sharp slowing for distinct attraction–repulsion networks

## Finding
For the symmetric networked opinion dynamics of Boyce–Farina–McKerral–Shelyag–Zuparic, global consensus persists **at** the first loss of linear coercivity, even when the attraction and repulsion graphs are different. Suppose the critical signed Laplacian has exactly one additional zero eigenvalue beyond the translation mode. With the normalization below, all trajectories except those in an invariant, measure-zero strong-stable set obey the **sharp** vector limit
\[
\lim_{t\to\infty}\sqrt{t}\bigl(x(t)-\bar x\mathbf1\bigr)=\frac{s v}{\sqrt{2\kappa}},\qquad s\in\{-1,1\},
\]
where \(v\) is the unit critical eigenvector and \(\kappa\) is the strictly positive, explicitly weighted fourth-power edge energy. Exceptional trajectories converge exponentially. For the three-agent attractive path with one repulsive endpoint edge, the threshold is \(\alpha_*=1/2\), and the critical antisymmetric coordinate \(q=(x_1-x_3)/2\) satisfies the stronger exact asymptotic
\[
q(t)^{-2}=\frac{2t}{9}-\frac25\log t+C(q(0))+o(1)
\]
for every \(q(0)\ne0\). The logarithmic coefficient is independent of the initial state.

## Assumptions and scope
Let \(N\ge2\). The symmetric matrices \(A=(A_{ij})\) and \(R=(R_{ij})\) have nonnegative entries and zero diagonals. The positive-edge graph of \(A\) is connected, and \(R\) has at least one positive edge. For every \(\alpha>0\) and every \(x(0)\in\mathbb R^N\), consider
\[
\dot x_i=-\frac1N\left[\sum_{j=1}^N A_{ij}(x_i-x_j)-\sum_{j=1}^N R_{ij}\tanh\bigl(\alpha(x_i-x_j)\bigr)\right].\tag{1}
\]
Let \(L_A,L_R\) be the corresponding graph Laplacians and \(E=\{y:\mathbf1^Ty=0\}\). Define the strictly positive critical parameter by
\[
\alpha_*^{-1}=\max_{y\in E\setminus\{0\}}\frac{y^T L_R y}{y^T L_A y},\qquad H_*=L_A-\alpha_*L_R.
\]
The mean \(\bar x=N^{-1}\sum_i x_i(0)\) is conserved. The unconditional assertion is: **for every** initial state, consensus is globally asymptotically stable for every \(0<\alpha\le\alpha_*\), and it is unstable for \(\alpha>\alpha_*\).

For the sharper rate at \(\alpha=\alpha_*\), additionally suppose \(\ker(H_*)\cap E=\operatorname{span}\{v\}\) for a unit vector \(v\in E\). Define
\[
\kappa=\frac{\alpha_*^3}{3N}\sum_{1\le i<j\le N} R_{ij}(v_i-v_j)^4>0.\tag{2}
\]
For each fixed mean hyperplane, the exceptional set is the set of initial points whose orbits converge exponentially; it is the global strong-stable manifold of consensus, locally a smooth codimension-one submanifold of that hyperplane and globally of Lebesgue measure zero. Every other orbit obeys the limit in the Finding. The sign is determined by the asymptotic center direction; it is not generally just the sign of the initial projection onto \(v\).

The three-agent specialization takes \(A_{12}=A_{23}=1\), \(R_{13}=1\), all other off-diagonal weights zero except symmetric counterparts, and \(\alpha=1/2\). These are different graphs. Put
\[
q=(x_1-x_3)/2,\qquad p=(x_1+x_3-2x_2)/6.
\]
The constant \(C(q(0))\) in the Finding is finite and depends only on the initial nonzero \(q(0)\), not on \(p(0)\) or the conserved mean.

## Proof
**1. Positive critical parameter and global solutions.** Connectedness of \(A\) makes \(L_A\) positive definite on \(E\). Since \(R\) has a positive edge, the maximum defining \(\alpha_*^{-1}\) is finite and positive. Equation (1) is globally Lipschitz and conserves the sum of coordinates, so all solutions exist uniquely for every real time.

**2. Strict dissipation at the boundary.** Write \(y=x-\bar x\mathbf1\) and \(\Delta_{ij}=y_i-y_j\). Symmetry yields the exact identity
\[
\frac N2\frac{d}{dt}\|y\|_2^2=-y^T(L_A-\alpha L_R)y-\sum_{i<j}R_{ij}\bigl[\alpha\Delta_{ij}^2-\Delta_{ij}\tanh(\alpha\Delta_{ij})\bigr].\tag{3}
\]
For \(0<\alpha\le\alpha_*\), the first term on the right is nonpositive because \(L_A-\alpha L_R\succeq0\) on \(E\). Every bracket is nonnegative and is **strictly** positive if its edge has \(R_{ij}>0\) and \(\Delta_{ij}\ne0\), since \(z\tanh(\alpha z)<\alpha z^2\) for nonzero real \(z\). If equality holds in (3), then \(y\in\ker(L_A-\alpha L_R)\cap E\) and all repulsion-edge differences vanish. Consequently \(L_Ry=0\), whence \(L_Ay=0\), and connectedness forces \(y=0\). Thus the squared-distance Lyapunov function is strictly decreasing off consensus, trajectories are bounded, and the compact-sublevel LaSalle argument proves global convergence to consensus. The strict inequality for \(\alpha<\alpha_*\) even gives exponential convergence. For \(\alpha>\alpha_*\), the symmetric linearization \(-(L_A-\alpha L_R)/N\) has a positive eigenvalue on \(E\); hence consensus is unstable.

**3. Exact cubic coefficient and exceptional trajectories.** At \(\alpha=\alpha_*\), Taylor's formula in the finite-dimensional phase space \(E\) gives
\[
\dot y=-\frac{H_*}{N}y-\frac{\alpha_*^3}{3N}\sum_{i<j}R_{ij}(y_i-y_j)^3(e_i-e_j)+O(\|y\|^5).\tag{4}
\]
The complement \(E\cap v^\perp\) has strictly negative linear spectrum. A smooth one-dimensional local center manifold can therefore be parameterized by \(y=av+h(a)\), where \(h(a)\in E\cap v^\perp\), \(h(a)=O(a^3)\), and the equation is odd under \(y\mapsto-y\). Taking the scalar product of (4) with \(v\) gives
\[
\dot a=-\kappa a^3+O(a^5).\tag{5}
\]
If \(\kappa=0\), then all repulsion-edge differences \(v_i-v_j\) vanish. This gives \(L_Rv=0\) and, since \(H_*v=0\), also \(L_Av=0\), contrary to \(v\in E\) and \(\|v\|=1\). Therefore \(\kappa>0\).

The standard local strong-stable foliation of a normally stable one-dimensional center manifold provides an exponentially shadowing center trajectory for each sufficiently small state. Its center amplitude is either zero, in which case the original orbit is exponentially decaying and belongs to the local strong-stable manifold, or nonzero. In the latter case (5) gives eventual constant sign and
\[
\frac{d}{dt}\bigl[a(t)^{-2}\bigr]=2\kappa+O(a(t)^2),\qquad a(t)^{-2}\sim2\kappa t.
\]
The complementary component is \(O(a^3)\) plus an exponentially decaying correction, hence the vector limit follows. Every orbit reaches this neighborhood by step 2. The global exceptional set is a countable union of inverse-time images of a local codimension-one strong-stable manifold, hence is invariant and Lebesgue-null on the fixed-mean hyperplane. Every point in it converges exponentially. No claim of one common sign for all initial conditions is made.

**4. Exact three-agent reduction and first logarithmic correction.** For the specified three-agent graphs,
\[
H_*=\begin{pmatrix}1/2&-1&1/2\\-1&2&-1\\1/2&-1&1/2\end{pmatrix},
\quad \operatorname{spec}(H_*)=\{0,0,3\},\quad v=(1,0,-1)/\sqrt2,\quad\kappa=1/18.
\]
Writing \(x=\bar x\mathbf1+(q+p,-2p,-q+p)\) yields the **exact** independent equations
\[
\dot p=-p,\qquad \dot q=-\frac{q-\tanh q}{3}.\tag{6}
\]
If \(q(0)=0\), then \(q\equiv0\) and \(p(t)=p(0)e^{-t}\), the exceptional strong-stable set. If \(q(0)\ne0\), the sign of \(q\) is preserved and \(|q|\searrow0\). With \(U(t)=q(t)^{-2}\), the exact scalar differential equation gives
\[
\dot U=\frac23\frac{q-\tanh q}{q^3}=\frac29-\frac4{45U}+O(U^{-2}).\tag{7}
\]
First \(U(t)/t\to2/9\) and then integration of (7) shows \(U(t)=2t/9-(2/5)\log t+O(1)\). Substituting this estimate back into (7) makes the remainder after removing \(2/9-2/(5t)\) integrable (bounded by a constant times \((\log t)/t^2\)), yielding the finite constant \(C(q(0))\) and the claimed \(o(1)\). In particular \(\lim_{t\to\infty}\sqrt t\,q(t)=\operatorname{sgn}(q(0))\,3/\sqrt2\). This also independently confirms the general coefficient in (2).

## Verification
Run `python CHECK.py` in the same directory. It checks exact three- and four-node path Laplacians, critical spectra and eigenvectors (including the four-node coefficient \(\kappa=1/100\)), the fourth-power coefficient \(\kappa=1/18\), the odd hyperbolic-tangent expansion through seventh order, the two reduced equations, and the analytically predicted \(-2/5\) logarithmic coefficient. Numerical integration over increasing horizons tests the independently derived leading asymptotic and convergence of the logarithmically renormalized remainder. These numerical checks support, but do not replace, the analytical proof. No finite computation purports to verify the general infinite-time theorem exhaustively.

## Relationship to prior work
Boyce et al., arXiv:2512.05725 (first made public 2025-12-05), introduce equation (1). Their Theorem 1 proves global consensus when the signed Laplacian is strictly positive on the mean-zero hyperplane and instability when it has a negative direction. Their Section 3.2 treats the special case of identical attraction and repulsion networks at equality; their Appendix C already identifies the \(\alpha_*=1/2\) threshold for the three-node path with endpoint repulsion. **Those model, spectral, and threshold facts are not claimed as new here.** The additions are the general **distinct-topology semidefinite-boundary** global theorem, the generic sharp vector decay with its explicit quartic graph coefficient and exceptional strong-stable set, and the three-node logarithmic correction.

Homs-Dones, Devriendt and Lambiotte (arXiv:2008.12022) give a broad framework for nonlinear odd edge couplings, graph-based equilibria, and linear stability; Devriendt and Lambiotte (arXiv:2002.08408) study a polynomial consensus–dissensus model and effective resistance. Neither inspected source provides the critical asymptotics of (1). Zelazo and Bürger (arXiv:1408.2187) cover signed-Laplacian definiteness and effective-resistance stability, which are treated as prior tools, not claimed contributions.

## Limitations
The sharp nonexceptional vector rate requires a **simple** nontranslation zero eigenvalue of \(H_*\); for higher-dimensional critical null spaces this result proves global convergence but makes no universal direction or coefficient assertion. The model is deterministic, uses symmetric and nonnegative edge weights and an undirected connected attraction graph, and presumes the original hyperbolic-tangent interaction law. Numerical examples do not establish the theorem by themselves. The literature comparison covers accessible sources and indexed records, not every unindexed manuscript; broader nonlinear-gradient theory can recover aspects of the center-manifold mechanism without giving this network-specific formula. These are mathematical statements about a stylized opinion model, not empirical statements about people.

## References
1. J. Boyce, M. Farina, J. McKerral, S. Shelyag and M. Zuparic, *Opinion dynamics modelling: distinct attraction and repulsion topologies highlight quantitative effects of trolling*, arXiv:2512.05725 (first public 2025-12-05), https://arxiv.org/abs/2512.05725; *Journal of Nonlinear Science* 36, article 112 (2026), https://doi.org/10.1007/s00332-026-10333-0.
2. M. Homs-Dones, K. Devriendt and R. Lambiotte, *Nonlinear consensus on networks: equilibria, effective resistance and trees of motifs*, arXiv:2008.12022; *SIAM J. Appl. Dyn. Syst.* 20 (2021), https://doi.org/10.1137/20M1376844.
3. K. Devriendt and R. Lambiotte, *Nonlinear network dynamics with consensus–dissensus bifurcation*, arXiv:2002.08408; *Journal of Nonlinear Science* 31, article 18 (2021), https://doi.org/10.1007/s00332-020-09674-1.
4. D. Zelazo and M. Bürger, *On the definiteness of the weighted Laplacian and its connection to effective resistance*, arXiv:1408.2187 (2014), https://arxiv.org/abs/1408.2187.
5. J. Carr, *Applications of Centre Manifold Theory*, Springer (1981), standard center-manifold and stable-foliation methods.
