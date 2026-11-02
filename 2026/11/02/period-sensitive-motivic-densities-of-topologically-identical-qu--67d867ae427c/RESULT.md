# Period-sensitive motivic densities of topologically identical quartic K3 cones

## Finding
For a smooth complex quartic surface \(S\subset\mathbb P^3\), let \(X_S\subset\mathbb A^4\) be its affine cone at the vertex \(o\). Put \(\mathbb L=[\mathbb A^1_{\mathbb C}]\) and
\[
\mathcal M_{\mathbb C}^{\mathbb Q}=\mathbb Q\otimes K_0(\operatorname{Var}_{\mathbb C})[\mathbb L^{-1},(1-\mathbb L^{-j})^{-1}:j\geq1].
\]
Let \(\Theta_S\in\mathcal M_{\mathbb C}^{\mathbb Q}\) be the dimension-three motivic local density defined by Forey and computed for isolated singularities by Ratajczak. Then
\[
\Theta_S=\frac{[S]}{1+\mathbb L+\mathbb L^2}.
\]
More importantly, **the following separation and variation statements hold**.

1. If \(\Theta_S=\Theta_T\), then \(H^2(S,\mathbb Q)\simeq H^2(T,\mathbb Q)\) as rational Hodge structures (without a claim that the isomorphism respects cup products or a polarization). In particular \(\rho(S)=\rho(T)\).
2. Among projective-equivalence classes of smooth quartics, each fiber of \(S\mapsto\Theta_S\) is at most countable. The image is uncountable.
3. All vertex germs \((X_S,o)\) are homeomorphic, are isolated dimension-three hypersurface singularities, and have Hilbert–Samuel multiplicity four. In particular the Fermat quartic with \(\rho=20\) and a very general quartic with \(\rho=1\) yield different motivic local densities despite this identical topological and multiplicity profile.

The formula for \(\Theta_S\) is a direct **application of the published general resolution formula**, not an independent new formula. The asserted contribution is its Hodge-theoretic separation and uncountable variation within one topological singularity type.

## Assumptions and scope
All geometry is over \(\mathbb C\). Quartic means an embedded smooth degree-four surface in \(\mathbb P^3\). Motivic densities are compared as elements of the stated rationalized localized Grothendieck ring, **not** after applying a numerical Euler or Hodge–Deligne polynomial. Here \(\rho(S)\) is the rank of the Néron–Severi group and the unpolarized rational Hodge structure is used. The projective-equivalence quotient is the quotient by \(\operatorname{PGL}_4(\mathbb C)\).

## Proof
**1. The cone and its resolution.** If \(F\) cuts out \(S\), its homogeneous gradient has no common zero outside the origin, since \(S\) is smooth; hence \(X_S=V(F)\) has one isolated singular point \(o\), dimension three and multiplicity four. Blow up \(o\). The resolution \(\pi:Y\to X_S\) is the total space of \(\mathcal O_S(-1)\) with zero section \(E\simeq S\). The exceptional divisor is smooth, irreducible and has multiplicity \(m_E=1\) in the pullback of the vertex maximal ideal. The Nash Gauss map extends to \(Y\): in local coordinates \((t,u,v)\) with cone map \(x_i=t\,s_i(u,v)\), the tangent three-plane away from \(t=0\) is spanned by \(s,s_u,s_v\), independent of \(t\). Thus the resolution factors through both the maximal-ideal blowup and the Nash modification, as required by Ratajczak's Theorem 1.2.

**2. Mather discrepancy and the density.** In the same chart the pullback of every ambient three-form minor of the differential has a factor \(t^2\), while smoothness of the projective embedding guarantees that one normalized minor is a local unit. Therefore the Mather Jacobian divisor has coefficient \(\widehat k_E=2\), so for \(d=3\) the source's exponent \(\alpha_E=\widehat k_E+1-dm_E=2+1-3=0\). With one exceptional divisor, Ratajczak's published formula gives
\[
\Theta_S=\frac{(\mathbb L-1)[E]}{\mathbb L^3-1}=\frac{[S]}{1+\mathbb L+\mathbb L^2}.
\]
The denominator is invertible in the specified localization since \(1+\mathbb L+\mathbb L^2=\mathbb L^2(1-\mathbb L^{-3})/(1-\mathbb L^{-1})\).

**3. Cancellation under the full Hodge realization.** Suppose \(\Theta_S=\Theta_T\). Multiplication by the invertible class \([\mathbb P^2]\) gives \([S]=[T]\) in \(\mathcal M_{\mathbb C}^{\mathbb Q}\). Apply the alternating rational mixed-Hodge-structure realization \(\chi_{\mathrm{Hdg}}\), taking \(\mathbb L\) to the Tate class. This extends to the localization. A smooth quartic is a K3 surface, with cohomology only in even degrees, so
\[
\chi_{\mathrm{Hdg}}([S]-[T])=[H^2(S,\mathbb Q)]-[H^2(T,\mathbb Q)].
\]
This equality holds in the localized Grothendieck group of rational mixed Hodge structures. Localization does **not** discard a nonzero finite-weight Grothendieck class: tensoring by \(\mathbb Q(-1)\) shifts weights upward by two, hence is invertible; for any \(j\geq1\), multiplication by \(1-[\mathbb Q(j)]\) is injective, because the smallest weight of a nonzero finite-support virtual class produces a unique strictly smaller weight after multiplying by \(-[\mathbb Q(j)]\). Repeating this for finitely many factors proves injectivity of the localization. Finally the integral Grothendieck group is torsion-free: its finite weight-graded pieces are sums of Grothendieck groups of semisimple categories of polarizable pure rational Hodge structures. Therefore rationalizing also loses no class. We conclude
\[
[H^2(S,\mathbb Q)]=[H^2(T,\mathbb Q)]
\]
*before localization*. Semisimplicity of polarizable pure weight-two rational Hodge structures upgrades equality of classes to a Hodge isomorphism. The Lefschetz \((1,1)\) theorem then gives \(\rho(S)=\rho(T)\).

**4. Countability of fibers.** The smooth-quartic moduli space has complex dimension nineteen; its period map is locally injective by the polarized K3 local Torelli theorem. Fix the rational Hodge structure of a quartic \(S\). Under markings of the fixed rational vector space \(\Lambda_{\mathbb Q}\simeq\mathbb Q^{22}\), Hodge isomorphism forces the period line \(H^{2,0}\) to lie in an orbit under the countable group \(\operatorname{GL}_{22}(\mathbb Q)\). In the marked polarized period space each such line has at most countably many preimages: local injectivity makes each fixed-period fiber discrete in a second-countable analytic space. Accounting for the countably many integral markings leaves a countable union of countable sets. Since equal density forces Hodge isomorphism, each density fiber is at most countable. A positive-dimensional complex moduli space has uncountably many points, so the density image is uncountable.

**5. Fixed topology.** The space of smooth quartics is the connected complement of the discriminant in the projective space of quartic equations. Any path of smooth quartics gives an Ehresmann locally trivial family of compact embedded surfaces with their hyperplane classes and associated unit-circle bundles of \(\mathcal O_S(-1)\). The link of \((X_S,o)\) is exactly this circle bundle, and its cone is homeomorphic to the singular germ. Consequently all these germs are homeomorphic. The classical calculation \(\rho=20\) for the Fermat quartic versus \(\rho=1\) for a very general quartic gives the claimed explicit rank obstruction.

## Verification
The proof uses exact normalizations, the published Mather-discrepancy resolution formula, the semisimplicity and finite-weight structure of rational Hodge theory, local Torelli, and smooth proper isotopy. A direct chart calculation gives \(m_E=1\), \(\widehat k_E=2\), and \(\alpha_E=0\); the localization cancellation uses a finite minimal-weight argument rather than numerical Hodge polynomials. No finite experiment is claimed to prove the uncountability assertion, and no independent mathematical audit has been performed.

## Relationship to prior work
Ratajczak, *Motivic local density of isolated singularities of algebraic varieties*, arXiv:2610.32416v1, Theorem 1.2, already supplies the **general formula** from which the displayed cone density is specialized; that specialization alone is not asserted to be original. Forey's *Motivic local density*, arXiv:1512.00420, establishes the underlying local-density framework and tangent-cone principle. Huybrechts, *Lectures on K3 surfaces*, supplies the local period theorem and the Picard-rank examples. The additional combination proved here is that the fully motivic density, unlike the ordinary multiplicity or topological germ, has uncountably many values on this fixed-topology family. This is a priority-sensitive consequence of known general frameworks and could be implicit in broader motivic or Hodge-theoretic literature.

## Limitations
The separation is one-directional: no converse is proved, and the recovered Hodge isomorphism is not asserted to preserve the polarization or intersection form. The density can distinguish quartics of different rational Hodge structures but does not classify analytic isomorphism types. The argument applies to smooth quartic cones over \(\mathbb C\), not arbitrary nonhomogeneous deformations, positive characteristic, or numerical realizations such as the Euler characteristic (which erase the asserted variation). Final historical priority and independent mathematical validation remain open.

## References
1. S. Ratajczak, *Motivic local density of isolated singularities of algebraic varieties*, arXiv:2610.32416v1, first posted 2026-10-23; Theorem 1.2 and Sections 2, 4–5.
2. A. Forey, *Motivic local density*, arXiv:1512.00420, introductory definition and the tangent-cone theorem.
3. D. Huybrechts, *Lectures on K3 surfaces*, author-hosted draft (2015), Chapters 1, 5–7, 17; local Torelli, quartic moduli, and Picard ranks of the Fermat and very general quartics.
