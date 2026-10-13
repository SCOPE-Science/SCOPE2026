# Bipartite band networks are exactly sign-gauge symmetric in multiband BCS linearization
## Finding
Consider the multiband BCS model of Henheik, Langmann, and Lauritsen with \(d\in\{1,2,3\}\), dispersion relations and interactions satisfying their Assumptions 1.1 and 1.2, and the scaled linearized operator
\[
H_T(\lambda,\kappa)=K_T+\lambda V^{\mathrm d}+\lambda\kappa V^{\mathrm{od}},
\qquad \lambda>0,\quad \kappa\in\mathbb R.
\]
Define the interaction graph \(G_V\) on the band set \(\{1,\ldots,n\}\) by joining distinct bands \(a\) and \(b\) exactly when \(V_{ab}\not\equiv0\).

If \(G_V\) is bipartite, then for every \(T>0\), \(\lambda>0\), and \(\kappa\in\mathbb R\),
\[
\operatorname{spec} H_T(\lambda,\kappa)
=
\operatorname{spec} H_T(\lambda,-\kappa).
\]
In particular, the source's critical temperature obeys the exact all-coupling symmetry
\[
T_c(\lambda,\kappa)=T_c(\lambda,-\kappa),
\]
and the two transition thresholds from its Proposition 1.4 satisfy
\[
\kappa_c^+=\kappa_c^-.
\]

There is also an exact converse at the level of bandwise phase gauges: a diagonal unitary acting only by constant phases on the band components can send \(V^{\mathrm{od}}\) to \(-V^{\mathrm{od}}\) if and only if \(G_V\) is bipartite. Thus an odd cycle is precisely the obstruction to this global sign gauge. This does not assert that every non-bipartite model has sign-dependent \(T_c\); accidental spectral symmetry can still occur.
## Assumptions and scope
The Hilbert space is \(\mathcal H=\bigoplus_{a=1}^n L^2(\mathbb R^d)\). The operator \(K_T\) and the intra-band interaction \(V^{\mathrm d}\) are diagonal in the band index, exactly as in the source. The off-diagonal interaction \(V^{\mathrm{od}}\) contains the blocks \(V_{ab}\) with \(a\ne b\), all scaled by the same real parameter \(\kappa\).

No connectivity assumption is needed: each connected component of \(G_V\) may be colored separately. Isolated bands are harmless. The theorem concerns the source's linearized critical-temperature criterion; no claim is made here about a different model in which independent edges carry unrelated coupling parameters.
## Proof
Assume \(G_V\) is bipartite, with a bipartition encoded by signs \(s_a\in\{-1,+1\}\) such that \(s_as_b=-1\) on every edge. Define the unitary \(U\) on \(\mathcal H\) by
\[
(U\psi)_a=s_a\psi_a.
\]
Because \(K_T\) and \(V^{\mathrm d}\) are band diagonal,
\[
UK_TU^*=K_T,
\qquad
UV^{\mathrm d}U^*=V^{\mathrm d}.
\]
For an off-diagonal block, conjugation contributes the scalar factor \(s_as_b\). Every nonzero off-diagonal block corresponds to an edge, so
\[
UV^{\mathrm{od}}U^*=-V^{\mathrm{od}}.
\]
Therefore
\[
UH_T(\lambda,\kappa)U^*
=H_T(\lambda,-\kappa).
\]
Unitary equivalence gives equality of the full spectra for every \(T\), \(\lambda\), and \(\kappa\).

The source defines
\[
T_c(\lambda,\kappa)
=
\inf\{T>0:H_T(\lambda,\kappa)\ge0\}.
\]
Since positivity is preserved by unitary conjugation, the defining sets of temperatures for \(\kappa\) and \(-\kappa\) coincide, proving exact evenness of \(T_c\). The equality \(\kappa_c^+=\kappa_c^-\) follows because Proposition 1.4 describes the equality region around \(\kappa=0\) by the interval \([-\kappa_c^-,\kappa_c^+]\), which must be symmetric when \(T_c\) is even.

For the gauge converse, suppose a bandwise diagonal phase unitary \(D=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_n})\) satisfies
\[
DV^{\mathrm{od}}D^*=-V^{\mathrm{od}}.
\]
On every edge \(\{a,b\}\), the nonzero block forces
\[
e^{i(\theta_a-\theta_b)}=-1.
\]
Hence adjacent vertices have phases differing by \(\pi\) modulo \(2\pi\). Multiplying these relations around a cycle shows that every cycle has even length. Thus \(G_V\) is bipartite. Conversely, a bipartition gives the sign unitary \(U\) constructed above. This proves the equivalence.
## Verification
The argument is exact and operator-theoretic. Its critical steps are: the source's band-diagonal structure of \(K_T\), the decomposition \(V=V^{\mathrm d}+\kappa V^{\mathrm{od}}\), the explicit critical-temperature definition through positivity, and the edgewise conjugation factor of the band-sign unitary. No finite experiment, numerical extrapolation, or unproved spectral approximation enters the proof.

The converse is only about this bandwise diagonal gauge. Non-bipartiteness proves that no such gauge flips all off-diagonal blocks simultaneously; it does not prove that \(T_c\) itself must distinguish the signs.
## Relationship to prior work
Henheik, Langmann, and Lauritsen prove that inter-band coupling cannot lower \(T_c\), allow different positive and negative threshold magnitudes in Proposition 1.4, and show weak-coupling linear or quadratic enhancement depending on degeneracy. They also note that for three or more equally strong bands the weak-coupling slope can generically depend on the sign of the inter-band coupling. Their paper does not formulate an interaction graph, a bipartiteness criterion, or an exact all-coupling unitary equivalence between \(\kappa\) and \(-\kappa\).

Yerin, Drechsler, and Fuchs show in a different three-band Ginzburg--Landau setting that the sign of inter-band coupling can affect \(T_c\), while in the two-band case it plays no role. The present theorem identifies the structural reason that survives for arbitrary numbers of bands in the source model: every bipartite interaction network, not only a two-band system, has exact sign-gauge symmetry. Their three-band examples with sign sensitivity contain the odd-cycle obstruction expected from this criterion.

Yang's earlier multiband BCS work proves, in a more restrictive isotropic constant-interaction setting, that \(T_c\) is controlled by the largest positive eigenvalue of the interaction matrix. Only an abstract/index record was available for inspection here; no statement of the present arbitrary-band bipartite gauge criterion was found there.
## Limitations
The theorem uses the source's single scalar \(\kappa\) multiplying all off-diagonal interaction blocks. It does not classify sign patterns when individual edges are scaled independently. It also does not claim a converse from non-bipartiteness to sign dependence of \(T_c\): an odd cycle is a necessary obstruction to this specific global sign gauge, not a sufficient mechanism for a measurable sign effect.

The result addresses the linearized operator that determines the critical temperature. No assertion is made about every nonlinear minimizer deep in the superconducting phase.
## References
1. J. Henheik, E. Langmann, and A. B. Lauritsen, *Multi-band superconductors have enhanced critical temperatures*, arXiv:2409.17297v1 (first public 2024-09-25), later published in *Annales Henri Poincare*, DOI 10.1007/s00023-026-01706-y.
2. Y. Yerin, S.-L. Drechsler, and G. Fuchs, *Ginzburg-Landau analysis of the critical temperature and the upper critical field for three-band superconductors*, arXiv:1306.6162.
3. Y. Yang, *Mathematical analysis of the multiband BCS gap equations in superconductivity*, *Physica D* 200 (2005), 60--74, DOI 10.1016/j.physd.2004.09.011.
