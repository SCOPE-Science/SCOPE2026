# Directional underdispersion and exact body-diagonal rays in cubic lattice quantum graphs
## Finding
Consider the free standard-Kirchhoff metric graph on the cubic lattice \(\ell\mathbb Z^\nu\), where \(\nu\ge2\) and every edge has length \(\ell>0\). For quasi-momentum \(p\in[-\pi/\ell,\pi/\ell]^\nu\), let \(E_\ell(p)\) denote the principal Bloch-band energy of the rescaled operator \(\nu H_\ell\). Then
\[
E_\ell(p)=\frac{\nu}{\ell^2}\arccos^2\!\left(\frac1\nu\sum_{j=1}^\nu\cos(\ell p_j)\right)
\le \lvert p\rvert_2^2.
\]
Equality holds if and only if
\[
\lvert p_1\rvert=\lvert p_2\rvert=\cdots=\lvert p_\nu\rvert.
\]
Thus the principal metric-graph band is globally underdispersive relative to the continuum Laplacian, except on the body-diagonal rays where it agrees with continuum dispersion exactly at every mesh size. For each fixed \(p\),
\[
E_\ell(p)=\lvert p\rvert_2^2-\frac{\nu\ell^2}{12}\operatorname{Var}_{1\le j\le\nu}(p_j^2)+O(\ell^4)
\qquad(\ell\to0).
\]
In dimension two this becomes
\[
E_\ell(p_1,p_2)=p_1^2+p_2^2-\frac{\ell^2}{24}(p_1^2-p_2^2)^2+O(\ell^4).
\]

## Assumptions and scope
The graph is the equilateral cubic metric graph with standard Kirchhoff conditions and no edge or vertex potential. The Bloch parameter is restricted to the first Brillouin zone, and the energy is restricted to the principal branch, characterized by \(0\le \ell\sqrt{E_\ell(p)/\nu}\le\pi\). The continuum comparator is the free symbol \(\lvert p\rvert_2^2\). The statement includes Brillouin-zone boundary points by continuity.

## Proof
Write \(q_j=\ell p_j\in[-\pi,\pi]\), and let \(k\ge0\) be the principal metric-graph wave number. The standard Bloch reduction for the cubic Kirchhoff lattice gives
\[
\cos(k\ell)=\frac1\nu\sum_{j=1}^\nu\cos q_j,
\qquad 0\le k\ell\le\pi,
\]
so \(E_\ell(p)=\nu k^2\).

Set \(t_j=q_j^2\in[0,\pi^2]\) and define \(g(t)=\cos\sqrt t\). For \(t=r^2\) with \(0<r\le\pi\),
\[
g''(t)=\frac{\sin r-r\cos r}{4r^3}.
\]
If \(h(r)=\sin r-r\cos r\), then \(h(0)=0\) and \(h'(r)=r\sin r>0\) for \(0<r<\pi\). Moreover \(g''(0)=1/12\) by continuity. Hence \(g\) is strictly convex on \([0,\pi^2]\).

Jensen's inequality therefore gives
\[
\frac1\nu\sum_{j=1}^\nu\cos q_j
=\frac1\nu\sum_{j=1}^\nu g(t_j)
\ge g\!\left(\frac1\nu\sum_{j=1}^\nu t_j\right)
=\cos\!\left(\sqrt{\frac1\nu\sum_{j=1}^\nu q_j^2}\right).
\]
Both angles belong to \([0,\pi]\), where cosine is decreasing, so
\[
k\ell\le\sqrt{\frac1\nu\sum_{j=1}^\nu q_j^2}.
\]
Multiplying by \(\nu/\ell^2\) yields \(E_\ell(p)\le\lvert p\rvert_2^2\). Strict convexity makes Jensen equality equivalent to \(t_1=\cdots=t_\nu\), which is exactly \(\lvert p_1\rvert=\cdots=\lvert p_\nu\rvert\). This also proves exact continuum dispersion on every body diagonal, not merely asymptotic agreement.

For the small-mesh expansion, define
\[
m_2=\frac1\nu\sum_{j=1}^\nu p_j^2,
\qquad
m_4=\frac1\nu\sum_{j=1}^\nu p_j^4.
\]
Then
\[
\frac1\nu\sum_{j=1}^\nu\cos(\ell p_j)
=1-\frac{\ell^2m_2}{2}+\frac{\ell^4m_4}{24}+O(\ell^6).
\]
Writing \((k\ell)^2=\ell^2m_2+\ell^4b+O(\ell^6)\) and matching the cosine expansion gives
\[
b=\frac{m_2^2-m_4}{12}
=-\frac1{12}\operatorname{Var}_{1\le j\le\nu}(p_j^2).
\]
Since \(E_\ell(p)=\nu k^2\), the stated quartic correction follows.

## Verification
The inequality proof is analytic on the entire first Brillouin zone and does not rely on sampling. A standalone checker evaluates the exact principal-band formula in dimensions two through six, checks the global sign on structured test grids, confirms exact body-diagonal agreement to floating-point precision, and checks the \(\ell^2\) coefficient against the variance formula for representative non-diagonal momenta. Those finite checks are corroborative only; strict convexity and Jensen's inequality are the proof.

## Relationship to prior work
Exner, Nakamura, and Tadano prove norm-resolvent convergence of lattice quantum-graph Hamiltonians to continuum Schrödinger operators, establishing the relevant continuum-limit setting. Holden and Vasil write the exact square-lattice dispersion relation and record only the lowest-order continuum approximation \(2k^2=k_x^2+k_y^2+O(\ell^2)\). The present statement extracts a global one-sided comparison, its exact equality locus, and the leading anisotropic correction. Nakamura and Tadano prove a continuum limit for discrete square-lattice Schrödinger operators; that finite-difference model is distinct from the metric-graph dispersion considered here.

## Limitations
The result concerns only the free equilateral standard-Kirchhoff cubic lattice and its principal Bloch branch. It does not address higher branches, the Dirichlet flat bands, nonzero edge or vertex potentials, magnetic phases, unequal edge lengths, or nonlinear dispersion. The literature comparison found no equivalent statement in the inspected sources, but an unindexed equivalent observation under numerical-dispersion terminology remains possible.

## References
1. P. Exner, S. Nakamura, and Y. Tadano, *Continuum limit of the lattice quantum graph Hamiltonian*, arXiv:2202.06586v1; Letters in Mathematical Physics 112 (2022), Article 83.
2. S. Holden and G. Vasil, *A continuum limit for the Laplace operator on metric graphs*, arXiv:2301.07086v1.
3. S. Nakamura and Y. Tadano, *On a continuum limit of discrete Schrödinger operators on square lattices*, Journal of Spectral Theory 11 (2021), DOI:10.4171/JST/343.
