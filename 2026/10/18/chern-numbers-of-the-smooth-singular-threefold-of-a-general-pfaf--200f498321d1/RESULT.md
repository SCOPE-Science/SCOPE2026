# Chern numbers of the smooth singular threefold of a general Pfaffian quintic

## Finding
Let \(V\) be a complex vector space of dimension \(10\), and let \(L\subset\mathbb P(\bigwedge^2V^*)\cong\mathbb P^{44}\) be a general projective \(9\)-plane. The degree-five Pfaffian hypersurface \(P_L=\{[\omega]\in L:\operatorname{Pf}(\omega)=0\}\) has a smooth irreducible singular threefold \(S\). With \(H=\mathcal O_S(1)\), its canonical bundle and Chern numbers are
\[
K_S\simeq\mathcal O_S(5H),\qquad
\int_S H^3=330,\quad
\int_Sc_1(TS)H^2=-1650,\quad
\int_Sc_2(TS)H=7920,\quad
\int_Sc_3(TS)=-31350.
\]
Consequently \(K_S^3=41250\), the topological Euler characteristic is \(-31350\), and \(\chi(S,\mathcal O_S)=-1650\). The numerical Hilbert polynomial is
\[
\chi(S,\mathcal O_S(mH))=55m^3-\frac{825}{2}m^2+\frac{2695}{2}m-1650
\qquad(m\in\mathbb Z).
\]
The degree \(330\) is the established Harris--Tu formula specialized to this case; the claim here is the complete stated Chern-number calculation and the associated numerical invariants, not priority for the degree alone.

## Assumptions and scope
All geometry is over \(\mathbb C\). The projective plane \(L\) is general in the Grassmannian of projective \(9\)-planes in \(\mathbb P^{44}\); no assertion is made for a special matrix pencil. A point \([\omega]\) is regarded as a nonzero skew-symmetric form on \(V\) up to scalar. The singular locus is taken with its reduced structure, which equals its Jacobian scheme for general \(L\). The Chern classes are those of the tangent bundle of the smooth threefold \(S\), not those of the ambient singular eight-dimensional Pfaffian hypersurface.

## Proof
**1. Identify the singular locus.** The rank-at-most-six locus \(D_6\subset\mathbb P(\bigwedge^2V^*)\) of skew forms on \(V\) has codimension \(\binom{4}{2}=6\); its singular locus consists of the rank-at-most-four forms, of codimension \(\binom{6}{2}=15\). The rank-eight locus of the full Pfaffian hypersurface is smooth, and its transverse leading Pfaffian along rank six is the nondegenerate four-by-four skew Pfaffian \(z_{12}z_{34}-z_{13}z_{24}+z_{14}z_{23}\). Bertini and dimension counting show that \(S=L\cap D_6\) is a smooth irreducible projective threefold, that \(L\) misses rank-at-most-four forms, and that the restricted Pfaffian has no singularities outside \(S\). The transverse ordinary quadratic form also implies that the restricted Jacobian ideal is reduced along \(S\).

**2. A globally smooth incidence model.** On \(G=\operatorname{Gr}(4,V)\), let \(0\to U\to V\otimes\mathcal O_G\to Q\to0\), with \(\operatorname{rk}Q=6\). Put \(W=\bigwedge^2Q^*\), a rank-\(15\) bundle, and let \(Z=\mathbb P_G(W)\), the projective bundle of one-dimensional subspaces, with \(h=c_1(\mathcal O_Z(1))\). A point of \(Z\) consists of a four-dimensional subspace in the kernel of a nonzero alternating form. Thus its natural morphism to \(\mathbb P^{44}\) resolves \(D_6\) and is an isomorphism over the rank-six stratum. Since rank-at-most-four forms do not meet \(L\), its preimage \(\widetilde S\) is isomorphic to \(S\). Here \(\dim Z=24+14=38\), and \(\widetilde S\) is the transverse intersection of \(35\) general members of \(|h|\). Consequently
\[
c(TS)=\left.\frac{c(TZ)}{(1+h)^{35}}\right|_{\widetilde S},\qquad
\int_S c_i(TS)H^{3-i}=\int_Zc_i\!\left(\frac{TZ}{\mathcal O_Z(1)^{\oplus35}}\right)h^{38-i}
\quad(0\leq i\leq3).
\]
The right-hand side is a Chern-class expression for a *virtual* bundle and can be integrated on \(Z\); it does not require the general section \(\widetilde S\) to be torus-invariant.

**3. Canonical bundle.** Write \(g=c_1(\det U^*)\) on \(G\). One has \(K_G=-10g\) and \(c_1(W)=-5g\). The relative tangent Euler sequence of \(Z=\mathbb P_G(W)\) gives \(K_Z=-5g-15h\), hence adjunction yields
\[
K_S=(-5g+20h)|_{\widetilde S}.
\]
Over \(S\), the induced rank-six alternating form on \(Q\) is nondegenerate and has values in \(\mathcal O_S(1)\). Its Pfaffian trivializes \(\det(Q^*)\otimes\mathcal O_S(3)\), so \(\det Q\simeq\mathcal O_S(3)\). Since \(\det Q=\det U^*\), \(g|_S=3H\). It follows that \(K_S\simeq\mathcal O_S(5H)\).

**4. Exact Chern integrations.** Act on \(V\) by a diagonal torus with pairwise independent characters \(w_1,\ldots,w_{10}\). The fixed points of \(Z\) correspond to a four-element index set \(I\subset\{1,\ldots,10\}\) and a two-element set \(R\) in the complement \(J\); there are \(\binom{10}{4}\binom62=3150\) such points. Let \(h_R=\sum_{r\in R}w_r\) and let \(\mathcal T_{I,R}\) be the multiset of \(38\) tangent weights
\[
\{w_j-w_i:i\in I,\ j\in J\}\;\sqcup\;
\{h_R-w_a-w_b:\{a,b\}\subset J,\ \{a,b\}\ne R\}.
\]
For \(0\leq e\leq3\), equivariant localization gives the finite, exact formula
\[
\int_Sc_e(TS)H^{3-e}=
\sum_{\substack{|I|=4\\R\subset J,\ |R|=2}}
\frac{h_R^{38-e}}{\prod_{\tau\in\mathcal T_{I,R}}\tau}
[z^e]\frac{\prod_{\tau\in\mathcal T_{I,R}}(1+\tau z)}{(1+h_Rz)^{35}}.
\]
The enclosed `verify.py` evaluates this expression in exact rational arithmetic twice, at \(w_i=2^{i-1}\) and \(w_i=3^{i-1}\). Both evaluations return the ordered values \((330,-1650,7920,-31350)\). Nonzero tangent denominators are checked for every term. The computation is exhaustive over all \(3150\) fixed points, not a sampling or extrapolation.

**5. Derived invariants.** The equalities \(K_S^3=125H^3=41250\) and \(\chi_{\mathrm{top}}(S)=\int_Sc_3(TS)=-31350\) follow. Hirzebruch--Riemann--Roch gives \(\chi(\mathcal O_S)=\frac1{24}\int_Sc_1(TS)c_2(TS)=-1650\) and the stated Hilbert polynomial. Notice that no determination of the full Betti numbers or Picard lattice is required.

## Verification
Run `python3 verify.py` with Python 3's standard library. It independently reproduces all four integral values for two unrelated diagonal torus weight systems, checks the canonical-class numerical consequence, and tests the neighboring size-eight case: a general Pfaffian quartic singular curve of degree \(84\) satisfies \(\int c_1(T)=-336\), hence genus \(169\). This is a cross-check rather than an ingredient in the proof of the size-ten result. The supplied localization formula plus the fixed-point list is an exact finite computation of the universal intersection numbers.

## Relationship to prior work
Bolognesi, Ciliberto and Verra (arXiv:2610.11925v1, 8 October 2026) study the same general Pfaffian hypersurfaces and give their rationality and related line congruences. They quote the Harris--Tu formula for the degree of the rank-drop locus; at \(n=9\), it already gives \(330\). The inspected paper does not compute the canonical bundle and threefold Chern-number table or its Euler characteristic. Harris and Tu (1984) provide classical rank-drop degree formulas, and standard skew-determinantal and equivariant-intersection theory supplies methods underlying the present derivation. A related computation in dimension eight yields the genus-\(169\) singular curve of a Pfaffian quartic, a different-dimensional locus whose answer does not determine the threefold invariants. Universal degeneracy-class techniques may make these numerical values derivable; the contribution is the complete exact specialization and its geometric interpretation, rather than a new general localization theorem.

## Limitations
Only general complex projective \(9\)-planes are covered. No smoothness or Chern-number assertions are made for nongeneric intersections containing forms of rank at most four. This finding does not give the full Hodge diamond, Picard group, singularity scheme of nongeneral Pfaffian hypersurfaces, or any independent priority certification. The degree is not claimed as new. Published universal rank-locus formulas could indirectly imply parts of the computation; this remains a residual literature risk.

## References
1. M. Bolognesi, C. Ciliberto and A. Verra, *On Calabi--Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1 (8 October 2026), https://arxiv.org/html/2610.11925v1.
2. J. Harris and L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, Topology **23** (1984), 71--84, DOI:10.1016/0040-9383(84)90026-0.
3. T. Józefiak, A. Lascoux and P. Pragacz, *Classes of determinantal varieties associated with symmetric and skew-symmetric matrices*, Izvestiya AN SSSR Ser. Mat. **45** (1981), 662--673.
4. M. F. Atiyah and R. Bott, *The moment map and equivariant cohomology*, Topology **23** (1984), 1--28.
