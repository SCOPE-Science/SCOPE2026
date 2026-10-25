# Four-dimensional stellahedral gamma minima and exact incidence defects

## Finding
For every four-dimensional convex polytope \(P\), let \(F_P(x)\) denote the **right augmented Eulerian Chow polynomial of its face lattice**. Equivalently, by the stellahedral-transform theorem of Faustini, Ferroni, and Piazza [1], \(F_P(x)\) is the toric \(h\)-polynomial of the stellahedral transform of that face lattice. Write
\[
F_P(x)=(1+x)^5\Gamma_P\!\left(\frac{x}{(1+x)^2}\right),\qquad
\Gamma_P(t)=1+\gamma_1(P)t+\gamma_2(P)t^2.
\]
Let \(v,e,r,s\) be, respectively, the numbers of vertices, edges, two-dimensional faces, and facets of \(P\). Let \(m\) be the number of incident pairs \((E,Q)\), where \(E\) is an edge and \(Q\) a two-dimensional face containing it. Introduce the five nonnegative incidence defects
\[
U=v-5,\quad W=s-5,\quad D=e-2v,\quad
K=m-3e,\quad X=m-3r.
\]
Then the **exact identities**
\[
\boxed{\gamma_1(P)=26+4U+2D+3W},
\qquad
\boxed{3\bigl(\gamma_2(P)-43\bigr)=12W+27D+4K+17X}
\]
hold for every such \(P\). In particular,
\[
\Gamma_P(t)\succeq 1+26t+43t^2
\]
coefficientwise, and **equality in either nonconstant coefficient holds if and only if \(P\) is a four-simplex**. Thus the four-dimensional case of the simplex-minimality conjecture stated in [1] holds, with an explicit incidence-based gap formula.

## Assumptions and scope
\(P\) is an arbitrary full-dimensional convex polytope in an affine four-dimensional real space, with no simplicity, simpliciality, rationality, or symmetry assumptions. The integer \(m\) counts *edge/two-face incidences*, not vertex/two-face incidences. Every two-face is a polygon. All \(f\)-counts and incidences count closed faces once; an edge contained in several two-faces contributes once for each pair. The polynomial \(F_P\) is the right (not the ordinary or the \(Z\)-) augmented Eulerian Chow polynomial, with the normalization in [1, Proposition 6.3].

## Proof
**1. The rank-five \(cd\)-index.** For the face lattice of a four-polytope, the degree-four \(cd\)-index in the usual convention is
\[
\Phi_P(c,d)=c^4+(s-2)c^2d+(r-s)cdc+(v-2)dc^2
 +(m-e-r-v-s+4)d^2.\tag{1}
\]
To verify (1) directly, expand \(c=a+b\), \(d=ab+ba\) and compare against the flag \(h\)-vector of the face lattice. The coefficients of the words \(aaab\), \(baaa\), \(aabb\), and \(abba\) yield successively \(s-2\), \(v-2\), \(r-s\), and \(m-e-r-v-s+4\). For \(aabb\), use that each two-face lies in precisely two facets; for \(abba\), its underlying flag count is \(m\). The other flag coefficients follow from the Eulerian Dehn–Sommerville equations, equivalently from the existence and uniqueness of the \(cd\)-index. In particular, Euler's relation is
\[
v-e+r-s=0.\tag{2}
\]

**2. Universal gamma contribution.** Proposition 6.3 of [1] gives the gamma contributions of the five degree-four \(cd\)-monomials as
\[
\begin{array}{c|ccccc}
\text{monomial}&c^4&c^2d&cdc&dc^2&d^2\\\hline
\text{gamma contribution}&1+t-t^2&3t+t^2&2t+2t^2&2t+t^2&7t^2.
\end{array}\tag{3}
\]
For completeness, these evaluations follow from that proposition's formula: write a monomial as \(c^{k_0}dc^{k_1}\cdots dc^{k_j}\); its gamma contribution is
\[
t^j\sum_{\ell=0}^j2^\ell\,s_{k_\ell}(t)
\prod_{h=\ell+1}^{j}T_{k_h+1}(t),
\]
where \(s_k(t)=1+t\sum_{i=0}^{k-1}T_{k-i}(t)\) and \(T_{2q+1}(t)=(-1)^qC_qt^q\), \(T_{2q}(t)=0\), with \(C_q\) the Catalan number. Inserting (1) into (3) gives
\[
\gamma_1(P)=3s+2e-9,
\qquad
\gamma_2(P)=7m-7e-5r-6v-8s+23.\tag{4}
\]
Equation (4) uses only (2) and exact integer arithmetic.

**3. Nonnegative defect decomposition.** A four-polytope has at least five vertices and five facets, hence \(U,W\ge0\). Every vertex has at least four incident edges, so \(2e\ge4v\), giving \(D\ge0\). Each edge has a two-dimensional polygon as its face-link and therefore belongs to at least three two-faces: \(m\ge3e\), giving \(K\ge0\). Finally, each two-face is a polygon with at least three edges, so \(m\ge3r\), giving \(X\ge0\). Substitution of these definitions into (4), using (2), proves both boxed identities.

**4. Sharpness and equality.** For a four-simplex, \((v,e,r,s,m)=(5,10,10,5,30)\), so all five defects vanish and \(\Gamma_P(t)=1+26t+43t^2\). Conversely, \(\gamma_1(P)=26\) forces \(U=0\) from its positive defect decomposition, hence \(P\) has exactly five vertices and is a simplex. Similarly, \(\gamma_2(P)=43\) forces \(W=0\) from the second decomposition, hence \(P\) has exactly five facets and is a simplex. This also proves that every nonsimplex has both inequalities strict. \(\square\)

## Verification
The accompanying standalone `verify.py` uses integer-only computations. It independently enumerates faces from facet intersections for eight specified four-polytopes; computes all sixteen flag \(h\)-coefficients; compares them to the \(cd\)-index expansion in (1); evaluates the five universal gamma terms directly from [1, Proposition 6.3]; and compares all resulting coefficients and nonnegative defects. The examples are a four-simplex, four-cube, four-cross-polytope, three products of simplices, and pyramids over the three-cube and three-octahedron. The program prints `EXACT_OK basis=5 convex_4_polytopes=8` on success. These finite tests check formulas and implementation but do not establish the universal theorem; the preceding argument proves it for all four-polytopes.

## Relationship to prior work
Faustini, Ferroni, and Piazza [1] introduced the stellahedral transform, identified its toric \(h\)-polynomial with the right augmented Chow polynomial, and proved gamma-positivity for all polytopal face lattices. They expressly **conjectured** coefficientwise gamma minimality at the simplex without stating or proving the present four-dimensional defect identities or equality classification. Their universal gamma evaluation (Proposition 6.3) is an essential cited premise, not a new theorem here. Ferroni, Matherne, and Vecchi [2] developed Chow functions and augmented variants, but their relevant sections do not give this explicit four-dimensional minimization and stability result. The \(cd\)-index itself and the relevant flag identities are established background.

## Limitations
The theorem is specific to four-dimensional convex polytopes; it does not resolve the higher-dimensional simplex-minimality conjecture. It concerns the **right** augmented Eulerian Chow polynomial and its toric-stellahedral interpretation, not an arbitrary Chow, Ehrhart, or \(Z\)-polynomial. The originality comparison establishes no exhaustive historical priority; older or differently indexed equivalent specializations may exist. The proof depends on the universal \(cd\)-to-gamma evaluation in [1], while the new incidence reductions and sharp equality are proved here. Independent scientific validation has not been performed.

## References
[1] T. Faustini, L. Ferroni, and L. Piazza, *Stellahedral Geometry of Partially Ordered Sets*, arXiv:2609.22078, first public version 18 September 2026; version 2, 28 September 2026, especially Theorems 1.4 and 1.6, Conjecture following Theorem 1.6, and Proposition 6.3. https://arxiv.org/abs/2609.22078

[2] L. Ferroni, J. P. Matherne, and L. Vecchi, *Chow Functions for Partially Ordered Sets*, arXiv:2411.04070, first public version 6 November 2024, version 3 of May 2026, especially Sections 3.5 and 5. https://arxiv.org/abs/2411.04070
