# The genus-169 singular curve and Grassmannian resolution of a general Pfaffian quartic

## Finding
Let \(V\) be an eight-dimensional complex vector space and let \(\Lambda\cong\mathbb P^7\) be a general projective linear subspace of \(\mathbb P(\bigwedge^2V^*)\cong\mathbb P^{27}\). Let \(Y\subset\Lambda\) be the quartic hypersurface defined by the Pfaffian of the universal alternating form. Put \(D=\{[\omega]\in\Lambda:\operatorname{rank}\omega\le4\}\).

The singular scheme of \(Y\) is exactly \(D\), a smooth connected irreducible curve of degree \(84\) and genus \(169\). It has
\[
\omega_D\cong\mathcal O_D(4),\qquad
\chi(D,\mathcal O_D(m))=84m-168\quad(m\in\mathbb Z).
\]
At every closed point \(p\in D\), the completed analytic germ of \(Y\) is the product of a smooth curve germ and a five-dimensional ordinary quadratic cone:
\[
\widehat{\mathcal O}_{Y,p}\cong
\mathbb C[[t,z_1,z_2,z_3,z_4,z_5,z_6]]/
(z_1z_6-z_2z_5+z_3z_4).
\]
Let \(\mathcal K\) be the rank-four kernel bundle of the alternating form along \(D\). The blow-up \(\pi:\widetilde Y=\operatorname{Bl}_D Y\longrightarrow Y\) is smooth. Its exceptional divisor is the relative Klein quadric
\[
E\cong\operatorname{Gr}_D(2,\mathcal K^*),
\]
whose geometric fibers are smooth four-dimensional quadrics. Its two families of maximal projective planes do not get exchanged by monodromy: their parameter bundles are \(\mathbb P_D(\mathcal K)\) and \(\mathbb P_D(\mathcal K^*)\) (up to the projectivization convention). Finally,
\[
K_{\widetilde Y}=\pi^*K_Y+3E,
\qquad -K_Y\cong\mathcal O_Y(4).
\]
In particular the quartic has Gorenstein terminal singularities.

## Assumptions and scope
Everything is over \(\mathbb C\), and \(\Lambda\) is general in the Grassmannian of projective seven-planes in \(\mathbb P^{27}\). The statement is not asserted for special subspaces, where deeper rank drops or nontransverse intersections can occur. Write \(L=\mathcal O_D(1)\). The universal skew morphism on \(D\) is \(V\otimes\mathcal O_D\to V^*\otimes L\), and its kernel is \(\mathcal K\) of rank four.

## Proof
### 1. Smooth singular curve and its scheme structure
The universal projective rank-at-most-four alternating locus \(\Sigma_4\subset\mathbb P(\bigwedge^2V^*)\) is irreducible of codimension \(\binom{4}{2}=6\), smooth precisely on its rank-four stratum. Its smaller rank-at-most-two locus has codimension \(\binom{6}{2}=15\). A general \(\Lambda\cong\mathbb P^7\) avoids the latter and meets \(\Sigma_4\) transversely in a smooth curve. Repeated general hyperplane-section Bertini irreducibility gives that curve irreducible (and hence connected). The Pfaffian hypersurface has singular locus exactly \(\Sigma_4\) on the universal space. A general linear section meets the rank-six smooth stratum transversely, so no new singularities appear on \(Y\) there. Hence the underlying singular locus is \(D=\Lambda\cap\Sigma_4\). The local normal form in Step 3 shows its Jacobian scheme is reduced, which upgrades the equality to scheme-theoretic equality.

The Harris–Tu degree formula for the rank-at-most-four locus, as quoted in Bolognesi–Ciliberto–Verra, is
\[
\deg\Sigma_4=
\frac1{240}\binom83\binom92\cdot10=84.
\]
Linear section preserves degree, so \(\deg D=84\).

### 2. The canonical bundle and genus
On \(D\), let \(\mathcal Q=(V\otimes\mathcal O_D)/\mathcal K\). It is a rank-four bundle with a nondegenerate alternating form valued in \(L\). Its Pfaffian gives \(\det\mathcal Q\cong L^2\). Since the ambient rank-eight bundle is trivial,
\[
\det\mathcal K^*\cong\det\mathcal Q\cong L^2.
\]
At a rank-four point, first-order skew perturbations restricted to the four-dimensional kernel identify the normal space to \(\Sigma_4\) with \(\bigwedge^2\mathcal K^*\otimes L\). The transversality of \(\Lambda\) makes this also the normal bundle of \(D\) in \(\Lambda\):
\[
N_{D/\Lambda}\cong\bigwedge^2\mathcal K^*\otimes L.
\]
The bundle has rank six and determinant
\[
\det N_{D/\Lambda}\cong(\det\mathcal K^*)^3\otimes L^6
\cong L^{12}.
\]
Adjunction for the smooth codimension-six curve in \(\mathbb P^7\) gives
\[
\omega_D\cong(\omega_{\mathbb P^7}\otimes\det N_{D/\mathbb P^7})|_D
\cong L^{-8}\otimes L^{12}=L^4.
\]
Thus \(2g(D)-2=\deg\omega_D=4\cdot84=336\), giving \(g(D)=169\). Riemann–Roch on the connected smooth curve gives \(\chi(\mathcal O_D(m))=84m-168\) for every integer \(m\).

### 3. Uniform formal normal form
At an arbitrary rank-four point, the \(8\times8\) skew matrix has an invertible \(4\times4\) alternating block. Congruence by invertible block matrices reduces it in the completed local ring to an invertible skew block plus its \(4\times4\) skew Schur complement \(S\). The Pfaffian is a unit times \(\operatorname{Pf}(S)\). Because the intersection with \(\Sigma_4\) is transverse, the six independent entries of \(S\) form formal transverse local coordinates \(z_1,\dots,z_6\); choose a seventh coordinate \(t\) along \(D\). The Pfaffian of a general \(4\times4\) alternating matrix is \(z_1z_6-z_2z_5+z_3z_4\). Absorb the unit by an invertible formal change. Its transverse Hessian has rank six. Its Jacobian ideal is exactly \((z_1,\ldots,z_6)\), proving the claimed analytic germ and the reduced singular scheme at every point of \(D\).

### 4. Blow-up and exceptional Grassmannian
The normal cone of \(D\) in \(Y\) is cut out inside \(N_{D/\Lambda}\) by the nondegenerate fiberwise Pfaffian quadratic form. Therefore the exceptional divisor of the blow-up is its relative projectivized zero locus. Under \(N_{D/\Lambda}\cong\bigwedge^2\mathcal K^*\otimes L\), this is precisely the Plücker relative Grassmannian \(\operatorname{Gr}_D(2,\mathcal K^*)\). It is a smooth quadric-fourfold fibration, with the two maximal-plane rulings parametrized by lines and hyperplanes in the rank-four kernel bundle. The local normal form makes the strict transform of the quadratic cone under blowing up its vertex smooth. Consequently \(\widetilde Y\) is smooth globally.

The blow-up of \(\mathbb P^7\) along its smooth codimension-six center has ambient canonical discrepancy five, and \(Y\) has multiplicity two along \(D\). Adjunction to the strict transform therefore gives \(K_{\widetilde Y}=\pi^*K_Y+(5-2)E\). Meanwhile hypersurface adjunction gives \(K_Y\cong\mathcal O_Y(-4)\). A resolution with smooth exceptional divisor and positive discrepancy three proves that these hypersurface singularities are terminal; hypersurface adjunction also makes them Gorenstein.

## Verification
The accompanying standalone `verify.py` uses exact symbolic arithmetic to check the quadratic Pfaffian identity for a block-diagonal rank-four \(8\times8\) alternating matrix, rank six and nonzero determinant of its transverse Hessian, the degree formula, the adjunction exponent, the genus, and the discrepancy. It returns `VERIFY_OK`. These finite algebraic checks corroborate the proof but do not prove the general transversality statement; that follows from the universal rank stratification and Bertini.

## Relationship to prior work
Bolognesi–Ciliberto–Verra (arXiv:2610.11925v1, 8 October 2026), Section 1, introduce this general Pfaffian hypersurface and cite the Harris–Tu formula for the *degree* of the rank-four singular stratum, and establish rationality of the hypersurface. The present statement instead determines the smooth singular curve's canonical sheaf and genus, its scheme-theoretic and transverse singularity structure, and the blow-up geometry with discrepancy. The degree 84 is used as published input, not presented as a new calculation.

Harris–Tu (1984) supplies the general skew-determinantal degree formula used here. Their original full text was not retrievable during this comparison; an implicit broader formula for these specific geometric conclusions remains a priority risk. Benedetti and collaborators, *The Coble quadric* (2024), investigate different special Pfaffian loci on \(\operatorname{Gr}(2,8)\), not the general linear Pfaffian quartic's rank-four curve in \(\mathbb P^7\). Standard Pfaffian normal forms and adjunction supply proof ingredients; no new general theorem about arbitrary skew determinantal loci is claimed.

## Limitations
The claim requires a general linear system and complex characteristic zero. The degree of \(D\) was known. The canonical and blow-up conclusions are new specializations of standard degeneracy-locus mechanisms, so unlocated literature deriving them for the same family remains a specific originality risk. No cohomology ring, Hodge numbers of the resolution, arbitrary special-section classification, or uniqueness/novelty certification is claimed.

## References
1. M. Bolognesi, C. Ciliberto and A. Verra, *On Calabi–Yau varieties that are linear sections of Grassmannians of lines*, arXiv:2610.11925v1, 8 October 2026, Sections 1.1–1.3 and 2–3. https://arxiv.org/abs/2610.11925
2. J. Harris and L. W. Tu, *On symmetric and skew-symmetric determinantal varieties*, Topology 23 (1984), 71–84, Proposition 12(c), DOI:10.1016/0040-9383(84)90026-0 (degree formula as quoted in Reference 1; original full text not independently inspected).
3. V. Benedetti et al., *The Coble quadric*, Forum of Mathematics, Sigma 12 (2024), especially introduction and Sections 4–5 (related but distinct relative Pfaffian geometry).
