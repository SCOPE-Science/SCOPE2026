# Bipartite mesh invariants and a sharp mixing floor for centered finite-volume transport

## Finding

**Theorem (common stationary subspace, mesh parity, and mixing floor).** Let \(G=(V,E)\) be any finite connected simple undirected graph with at least three vertices and no cut vertex (equivalently, 2-vertex-connected). Give each vertex a positive cell mass \(m_v\). Arbitrarily orient the edges. Let \(F=(F_e)_{e\in E}\) range over **all real algebraically divergence-free face fluxes**, meaning the signed sum of outgoing fluxes at every vertex vanishes. On every oriented edge \(e=(u,v)\) use the two-point centered tracer flux \(F_e(\theta_u+\theta_v)/2\), with the negative of this flux assigned at its receiving endpoint. Let \(D_F\) be the resulting cell-mass-scaled divergence operator. Then

\[
\bigcap_{\operatorname{div}F=0}\ker D_F=\begin{cases}
\operatorname{span}\{\mathbf1,\chi\},&G\text{ bipartite},\\
\operatorname{span}\{\mathbf1\},&G\text{ nonbipartite},
\end{cases}
\]
where \(\chi_v\in\{+1,-1\}\) is the bipartition sign. In particular, when \(G\) is bipartite, \(\chi\) and \(\mathbf1\) are stationary for **each individual** divergence-free face field, not just the intersection, and the signed checkerboard projection is unchanged under any time-dependent sequence of such fields and any positive Crank–Nicolson time steps.

For a connected bipartite graph, define the weighted inner product \(\langle x,y\rangle_m=\sum_v m_vx_vy_v\) and the mean-zero bipartition sign \(\chi_0=\chi-\langle\chi,\mathbf1\rangle_m\mathbf1/\langle\mathbf1,\mathbf1\rangle_m\). For any self-adjoint positive-definite discrete negative Laplacian \(L_h\) on the weighted mean-zero subspace, every mean-zero tracer, evolved using any time-varying centered divergence-free face fluxes by either the semidiscrete dynamics or Crank–Nicolson, obeys the **control-independent mix-norm bound**
\[
\|\theta(t)\|_{-1,h}^2:=\langle\theta(t),L_h^{-1}\theta(t)\rangle_m\ \geq\ \frac{|\langle\theta(0),\chi_0\rangle_m|^2}{\langle\chi_0,L_h\chi_0\rangle_m}.
\]
For a periodic uniform \(N_x\times N_y\) Cartesian mesh with \(N_x,N_y\ge4\), its face-adjacency graph is bipartite exactly when both side counts are even; in that case \(\chi_{ij}=(-1)^{i+j}\). For the standard five-point negative Laplacian with grid spacings \(h_x,h_y>0\), this sign has eigenvalue \(\lambda_\chi=4h_x^{-2}+4h_y^{-2}\). The bound is sharp **as an equality** for \(\theta(0)=c\chi\), since then \(\theta(t)=c\chi\) for all choices of fluxes and all times. On a bounded Cartesian mesh with impermeable outer faces and at least two cells in each direction the corresponding graph is bipartite regardless of side parity.

**Two-point uniqueness (classical energy mechanism, extended algebraic scope).** For any fixed divergence-free \(F\) and any linear, consistent conservative two-point edge rule \(F_e[\alpha_e\theta_u+(1-\alpha_e)\theta_v]\), conservation of \(\|\theta\|_m^2\) for **all initial states** requires \(\alpha_e=1/2\) on every edge with \(F_e\ne0\). Conversely, these equal weights make the transport generator weighted-skew-adjoint. Hence on bridgeless simple graphs, requiring exact conservation for every algebraically divergence-free face field uniquely selects the centered rule on every edge. This energy-uniqueness mechanism is well established in related finite-volume literature; the new assessed statement is the complete graph-dependent common stationary space and associated exact mix-norm control floor.

## Assumptions and scope

The graph is simple to ensure that each unordered edge corresponds to one independent monomial in the quadratic energy identity; it is 2-vertex-connected to ensure that any pair of neighbors of a vertex lie on a common cycle. The flux family is **all** divergence-free real face circulations on this graph. This is an algebraic face-control envelope and need not coincide with the trace space of any particular finite-dimensional smooth velocity-control basis. Regardless of restrictions on that basis, the bipartite fixed checkerboard remains invariant for the centered rule. Vertex masses are arbitrary positive numbers. The weighted Laplacian is any positive self-adjoint graph or mesh Laplacian with kernel constants; its inverse in the displayed bound is restricted to mean-zero states. A purely two-cell or multi-edge periodic discretization is excluded by the simple-graph hypothesis.

The time-dependent system is \(\dot\theta=-D_{F(t)}\theta\), with piecewise continuous finite fluxes; the finite-step scheme with midpoint flux \(F^n\) and \(\tau_n>0\) solves \((I+\tau_nD_{F^n}/2)\theta^{n+1}=(I-\tau_nD_{F^n}/2)\theta^n\). Every such linear solve is invertible by weighted skew-adjointness.

## Proof

**1. Weighted energy identity and uniqueness.** Orient \(e=(u,v)\) outward at \(u\). By telescoping over cell masses, for an arbitrary tracer \(\theta\), the energy pairing is
\[
\langle\theta,D_F\theta\rangle_m
=\sum_{e=(u,v)}F_e(\theta_u-\theta_v)\bigl[\alpha_e\theta_u+(1-\alpha_e)\theta_v\bigr]
=\frac12\sum_{e=(u,v)}F_e(\theta_u^2-\theta_v^2)
+\sum_{e=(u,v)}F_e(\alpha_e-\tfrac12)(\theta_u-\theta_v)^2.
\]
The first sum vanishes because \(\operatorname{div}F=0\) at every vertex. If energy is conserved for every initial \(\theta\), the remaining quadratic polynomial is identically zero. Its coefficient of \(\theta_u\theta_v\) equals \(-2F_e(\alpha_e-1/2)\), and simple-graph adjacency makes that coefficient unique to \(e\). It follows that \(F_e(\alpha_e-1/2)=0\) on every edge. Conversely, central weights make the energy pairing zero for every \(\theta\), so polarization gives \(\langle x,D_Fy\rangle_m=-\langle D_Fx,y\rangle_m\). Every edge of a 2-vertex-connected graph is on a cycle and hence supports some divergence-free circulation; this proves the claimed all-flux uniqueness. Weighted skew-adjointness ensures that \(I+\tau D_F/2\) is invertible and that its Cayley transform preserves weighted \(L^2\) and weighted mass.

**2. Necessity of constant neighbor values.** Fix a vertex \(v\) and distinct neighbors \(u,w\). Since removing \(v\) leaves the graph connected, there is a simple path from \(u\) to \(w\) avoiding \(v\); joining it to \(u-v-w\) gives a simple cycle. Choose \(F\) to be a unit circulation around that cycle, zero off it. The central transport divergence at \(v\) is \((\theta_u-\theta_w)/(2m_v)\), up to orientation sign. Thus if \(D_F\theta=0\) for **every** divergence-free \(F\), necessarily \(\theta_u=\theta_w\) for any two neighbors of the same vertex. Equivalently, \(\theta\) is constant along every even-length walk in \(G\).

**3. Even-walk classes and sufficiency.** In a connected bipartite graph, every walk from one fixed vertex to another has parity prescribed by the bipartition. Any two vertices in the same bipartition class are joined by an even walk; the necessary condition in Step 2 makes \(\theta\) constant on each class, giving the stated two-dimensional space. In a connected graph containing an odd cycle, any pair of vertices can be joined by an even walk: insert a closed odd walk by traveling to an odd cycle and back if the chosen connecting walk is odd. Step 2 then forces \(\theta\) to be constant globally. Conversely \(D_F\mathbf1=0\) by divergence-free mass balance, while on a bipartite graph each edge has \(\chi_u+\chi_v=0\), so every individual face flux of \(\chi\) vanishes; hence \(D_F\chi=0\) even without divergence freedom. This proves the exact kernel intersection in both cases, without a genericity assumption on the flux coefficients.

**4. Irremovable mix-norm component.** Both \(\mathbf1\) and \(\chi\) are null vectors of every centered divergence-free \(D_F\). Since these operators are weighted-skew-adjoint, \(\langle\theta(t),\chi_0\rangle_m\) is constant in continuous time. For each Crank–Nicolson step, left-multiplying by \(\chi_0\) in the weighted inner product yields the identical invariance. Thus for any mean-zero state, by Cauchy–Schwarz applied to \(L_h^{-1/2}\theta\) and \(L_h^{1/2}\chi_0\),
\[
|\langle\theta,\chi_0\rangle_m|^2\le\langle\theta,L_h^{-1}\theta\rangle_m\langle\chi_0,L_h\chi_0\rangle_m.
\]
Insert the constant initial projection. Equality holds whenever \(\theta\) is proportional to \(L_h\chi_0\); the periodic Cartesian checkerboard example below simultaneously satisfies the stationary evolution, so its equality persists for any control schedule.

**5. Cartesian parity and sharp example.** The periodic Cartesian dual graph is the Cartesian product of the cycles \(C_{N_x}\) and \(C_{N_y}\). An odd side cycle makes the product nonbipartite; when both are even, sign alternation around each side is consistent and gives a bipartition. The standard five-point negative Laplacian applied to \(\chi_{ij}=(-1)^{i+j}\) gives \((4/h_x^2+4/h_y^2)\chi_{ij}\). Equal cell masses make \(\chi\) mean-zero. For \(\theta(0)=c\chi\), every centered face tracer average is zero, so the solution and every numerical iterate remain \(c\chi\). Its squared inverse-Laplacian norm is exactly \(c^2\langle\chi,\chi\rangle_m/(4/h_x^2+4/h_y^2)\), equal to the bound. For a bounded rectangular grid, ordinary integer parity \(i+j\bmod2\) always defines the bipartition.

## Verification

The included `checker.py` uses only the Python 3 standard library and exact rational arithmetic (`fractions.Fraction`). Running `python checker.py` confirms the predicted common-kernel dimension on nine 2-vertex-connected examples, independently enumerates each graph's divergence-free flow basis and transports, checks weighted-energy cancellations and individual bipartite face cancellation, and verifies the periodic \(4\times6\) grid's exact top checkerboard eigenvalue \(208\) for spacings \(h_x=1/4,h_y=1/6\). These are finite regression checks; the five-step argument above is the proof for all admissible graphs, masses, flux histories and timesteps.

## Relationship to prior work

Hu–Li–Zhang–Zuazua (2026), §§2–3, define a centered face flux for incompressible finite-volume mixing control, combine it with Crank–Nicolson, and prove discrete mass and \(L^2\) preservation. Their Remark 2.3 already warns of grid-scale oscillations; it does not classify the intersection of all control generators' kernels or give a sharp control-independent inverse-Laplacian floor. Coppola–Veldman (2022), §5.2, already derive equal-weight interpolation as the unique energy-preserving three-point rule and discuss odd-even decoupling in collocated pressure discretizations; the flux-energy uniqueness above is explicitly *not* claimed as independently new. Classical signless-Laplacian graph theory already characterizes the zero eigenvalue by graph bipartiteness; it does not by itself calculate the common invariant space of all divergence-free two-point transport operators. The assessed conjunction classifies arbitrary 2-vertex-connected graph envelopes and translates the exact invariant into a sharp obstacle for a mixing optimization objective.

## Limitations

No assertion is made that the continuous passive scalar problem has an invariant checkerboard, or that smooth/resolved test data in Hu et al. have a substantial checkerboard projection. The inverse-Laplacian floor may be small at fine resolution because the obstruction is high-frequency. The nonbipartite conclusion only says that there is no **common pointwise-stationary direction other than constants across all algebraic fluxes**; it does not imply controllability, uniform mixing, or convergence of any particular control algorithm. Real physical velocity-control families can be smaller and have more common invariants. Other stencils, upwind fluxes, nonexact divergence, multi-edge graphs, and nonconforming face coupling lie outside the theorem. Priority risk remains for older graph-advection treatments phrased through signless incidence and cycle spaces.

## References

1. W. Hu, Z. Li, Y. Zhang, E. Zuazua, *A Structure-Preserving Numerical Scheme for Optimal Control and Design of Mixing in Incompressible Flows*, arXiv:2601.06294, first posted 2026-01-09, particularly equations (2.6)–(2.9), Theorem 3.1, Lemma 3.2 and Remark 2.3. https://arxiv.org/abs/2601.06294
2. G. Coppola, A. E. P. Veldman, *Global and local conservation of mass, momentum and kinetic energy in the simulation of compressible flow*, arXiv:2208.14067 (2022), particularly §5.2 and the discussion of collocated odd-even decoupling. https://arxiv.org/abs/2208.14067
3. D. Cvetković, P. Rowlinson, S. Simić, *Signless Laplacians of Finite Graphs*, survey, especially the characterization of zero signless-Laplacian eigenvalues for connected bipartite graphs. https://turing.mi.sanu.ac.rs/projects/signless_L_reportJan28.pdf
