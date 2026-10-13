# Sharp shortest-edge perturbation radius for quantum-graph spanning-tree recovery

## Finding

Let \(G\) be a finite connected simple graph on \(n\ge3\) vertices and \(m\) edges. Give each edge \(e\) a positive length \(L_e\), put \(\ell=\min_e L_e\) and \(\beta=m-n+1\), and let \(\mathcal L_\Gamma\) be the Kirchhoff--Neumann metric-graph Laplacian. Define the Harrison--Weyand reconstruction statistic
\[
Q_\Gamma=\frac{\prod_{v\in V(G)}d_v}{m\,2^m\ell^{\beta+1}}\det{}'(\mathcal L_\Gamma),
\]
where \(\det{}'\) is the zeta-regularized spectral determinant with the zero eigenvalue omitted. Let \(\tau(G)\) denote the number of spanning trees. The integer determined by rounding \(Q_\Gamma\) is exactly \(\tau(G)\) throughout the following **sharp universal radius**.

For \(n\ge3\) put \(M_n=\binom n2\), \(b_n=M_n-n+1\), and
\[
F_n(u)=\frac{n^{n-3}}{M_n}\,u^{b_n-1}(2u+n-2)(1+(M_n-1)u),\qquad u\ge1.
\]
There is a unique \(u_n>1\) for which \(F_n(u_n)=n^{n-2}+\tfrac12\). Set \(\rho_n=u_n-1\). For every such \(G\) and every assignment satisfying
\[
\ell\le L_e<\ell(1+\rho_n)\quad\text{for every edge }e,
\]
\(Q_\Gamma\) has \(\tau(G)\) as its unique nearest integer. The constant \(\rho_n\) is optimal **uniformly over all connected simple graphs with \(n\) vertices**: for every \(r>\rho_n\), the complete graph on \(n\) vertices with one edge of length \(\ell\) and all other edges of equal length strictly between \(\ell u_n\) and \(\ell(1+r)\) has \(Q_\Gamma>\tau(G)+\tfrac12\).

The same proof gives an exact graph-specific cutoff. If \(a_e\) is the number of spanning trees containing the edge \(e\), and \(p_G=\max_e a_e/\tau(G)\), then for \(u>1\) and \(\ell\le L_e<\ell u\),
\[
0\le Q_\Gamma-\tau(G)<\tau(G)\left[\frac{1+(m-1)u}{m}\,u^{\beta-1}(1-p_G+p_Gu)-1\right].
\]
Its right-hand side is continuous and strictly increasing from zero to infinity, so setting it equal to \(\tfrac12\) gives the optimal admissible radius for the fixed topology. In particular, \(\rho_3=(\sqrt{42}-6)/4\) and \(\rho_n\sim n^{-n}\) as \(n\to\infty\). The special connected two-vertex graph has a single edge, and choosing \(\ell\) as its actual length gives \(Q_\Gamma=\tau(G)=1\) identically; it has no finite cutoff.

## Assumptions and scope

Graphs are finite, simple, undirected and connected. Vertex matching conditions are standard continuity and Kirchhoff flux conservation. All edge lengths are strictly positive. The short edge of length \(\ell\) really exists; the normalization is **not** an arbitrary lower length bound. The degree product, edge number, and minimum edge length are assumed available when evaluating the displayed statistic. The theorem is a sharp bound for that particular normalized spectral statistic, not a claim that the abstract spectrum alone always determines the graph's degrees or number of vertices.

## Proof

**1. Exact cotree identity.** Let \(\mathcal T(G)\) be the set of spanning trees and set \(x_e=L_e/\ell\) and \(\overline x=m^{-1}\sum_e x_e\). The Friedlander determinant formula stated as equation (40) in Harrison--Weyand [1] gives
\[
\det{}'(\mathcal L_\Gamma)=\frac{2^m(\sum_e L_e)}{n}\frac{\prod_e L_e}{\prod_vd_v}\det{}'(R),
\]
where \(R\) is the weighted discrete Laplacian with conductances \(1/L_e\). Kirchhoff's weighted matrix-tree identity gives
\[
\det{}'(R)=n\sum_{T\in\mathcal T(G)}\prod_{e\in T}L_e^{-1}.
\]
Every spanning tree has \(n-1\) edges and thus its complement has exactly \(\beta\) edges. Substitution, with no approximation, yields
\[
\boxed{Q_\Gamma=\overline x\sum_{T\in\mathcal T(G)}\prod_{e\notin T}x_e.}\tag{1}
\]
This formula proves \(Q_\Gamma\ge\tau(G)\), since every factor is at least one.

**2. Sharp fixed-topology bound.** Fix an edge \(e_0\) with \(x_{e_0}=1\). Expression (1) is coordinatewise nondecreasing in every other \(x_e\ge1\). For a fixed cap \(u>1\), its maximal value on the closed box is attained at \(x_e=u\) for all \(e\ne e_0\). Trees containing \(e_0\) leave \(\beta\) long edges in their complement; trees not containing \(e_0\) leave \(\beta-1\) long edges. Thus the extremal value equals
\[
\frac{1+(m-1)u}{m}\bigl(a_{e_0}u^\beta+(\tau(G)-a_{e_0})u^{\beta-1}\bigr).
\]
The coefficient of \(a_{e_0}\) is positive for \(u>1\), so maximizing over the choice of shortest edge selects \(p_G=\max_{e_0}a_{e_0}/\tau(G)\). Because actual edge lengths are strictly below the cap, the displayed upper bound is strict for \(n\ge3\). Its value at \(u=1\) is \(\tau(G)\), and it tends strictly increasingly to infinity as \(u\to\infty\). This proves the exact fixed-topology radius.

**3. Complete graph maximizes the rounding error.** Write the contribution of a spanning tree in (1) minus one as \(\overline x\prod_{e\notin T}x_e-1\ge0\). Add a previously absent edge of normalized length \(u\ge\max_e x_e\). For each old spanning tree, the complement product gains the factor \(u\), and the average length does not decrease. Every newly admitted spanning tree adds a nonnegative contribution. Therefore \(Q_\Gamma-\tau(G)\) cannot decrease under edge addition. Add all missing edges, retaining a chosen shortest edge at one and assigning all new edges the length \(u\); then increase all other existing lengths to \(u\). Hence the maximal rounding error among all connected simple graphs on \(n\) vertices occurs on \(K_n\) with exactly one edge of normalized length one and all other edges of length \(u\).

**4. Exact complete-graph extremum.** By Cayley's formula \(\tau(K_n)=n^{n-2}\). Each of its \(M_n\) edges belongs to the same number of spanning trees, namely
\[
a_e=\frac{n-1}{M_n}\tau(K_n)=2n^{n-3}.
\]
The count of spanning trees omitting that edge is \((n-2)n^{n-3}\). Inserting these two counts in step 2 produces precisely \(F_n(u)\). Every factor in \(F_n(u)\) is positive and increasing on \(u\ge1\), and \(F_n(1)=n^{n-2}\). Thus \(F_n(u_n)=n^{n-2}+\tfrac12\) has exactly one root \(u_n>1\). The upper comparison proves success whenever the length ratio is smaller than \(u_n\); choosing complete graphs with ratios just above \(u_n\) proves optimality. The normalized minimum really remains attained in these counterexamples.

**5. Examples and asymptotics.** For \(n=3\), \(F_3(u)=(2u+1)^2/3\), giving \(\rho_3=(\sqrt{42}-6)/4\). For \(n=4\), \(F_4(u)=\frac43u^2(u+1)(1+5u)\). The derivative at one is
\[
F_n'(1)=n^{n-2}\left(b_n+\frac2n-\frac1{M_n}\right).
\]
For fixed bounded \(c>0\), a Taylor expansion at \(u=1+c n^{-n}\), with its remainder bounded by a constant times \(n^{n-2}M_n^2n^{-2n}=O(n^{2-n})\), gives \(F_n(1+c n^{-n})-n^{n-2}\to c/2\). Monotonicity then implies \(n^n\rho_n\to1\).

## Verification

Run `python3 verify.py` with Python 3, using no third-party packages. It computes exact rational spanning-tree sums, weighted Laplacian cofactors and shortest-edge extremal formulas on all connected simple graphs with at most four vertices, and checks the complete-graph formula for three through five vertices. Expected output begins with `VERIFY_OK`. These finite checks do not replace the all-graph proof above. The exact source normalization was read from [1, equation (40)], and the later one-edge perturbation discussion was compared in [2, Section 5 and Appendix A].

## Relationship to prior work

Harrison and Weyand [1, Theorem 2] proved recovery by rounding under a much smaller sufficient edge-length window and explicitly described that bound as suboptimal. Their determinant identity is a premise here, not a novelty claim. Their follow-up [2, Section 5] computed first-order perturbations of **one** edge for selected graph families and suggested a larger window of order \(\ell n^{-n}\); it did not prove an optimal all-topology, simultaneous-edge window. The theorem above establishes an exact worst-case radius, a complete-graph extremizer, and an exact refinement controlled by spanning-tree edge-inclusion counts. The source formula and the weighted matrix-tree theorem are acknowledged known ingredients; the derived sharp extremal radius and its graph-specific form are the mathematical contribution considered here.

## Limitations

The theorem does not establish a new spectral-determinant formula, recover degrees from spectral data, address mean-normalized or two-sided perturbations, or handle non-Kirchhoff couplings, multigraphs, or an unnormalized fixed reference length that is not the actual shortest edge. The threshold is worst-case and generally conservative for sparse graphs; the graph-specific radius is better when the topology and spanning-tree edge-inclusion counts are available. A publication under alternative terminology for sharp determinant-rounding radii cannot be excluded solely by text searches.

## References

[1] J. Harrison and T. Weyand, *Can One Hear the Spanning Trees of a Quantum Graph?*, arXiv:2209.01284, first public version 2022-09-02, v2 (2023), Sections 5--7 and equation (40). https://arxiv.org/abs/2209.01284

[2] J. Harrison and T. Weyand, *Spectral Determinants of Almost Equilateral Quantum Graphs*, arXiv:2406.17965, first public version 2024-06-25, v3 (2025), Sections 3--5 and Appendix A. https://arxiv.org/abs/2406.17965

[3] L. Friedlander, *Determinant of the Schrödinger operator on a metric graph*, in *Quantum Graphs and Their Applications*, Contemp. Math. 415 (2006), 151--160; determinant identity attributed in [1, Theorem 4].
