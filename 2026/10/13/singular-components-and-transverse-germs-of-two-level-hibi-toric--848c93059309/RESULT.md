# Singular components and transverse germs of two-level Hibi toric varieties

## Finding

For integers \(a,b\ge1\), let \(P_{a,b}=A_a\oplus A_b\) be the ordinal sum of antichains: every one of the \(a\) first-level elements is below every one of the \(b\) second-level elements, with no relations within either level. Write \(X_{a,b}\) for the normal projective Hibi toric variety associated with the order-ideal lattice \(\mathcal I(P_{a,b})\) over \(\mathbb C\). It has dimension \(a+b\).

**Theorem.** The reduced singular locus has exactly the following irreducible components:

1. If \(a\ge2\), for each \(j\in\{1,\ldots,b\}\) a component \(B_j\cong (\mathbb P^1)^{b-1}\), of codimension \(a+1\).
2. If \(b\ge2\), for each \(i\in\{1,\ldots,a\}\) a component \(A_i\cong (\mathbb P^1)^{a-1}\), of codimension \(b+1\).
3. If \(a,b\ge2\), for each unordered pair \(\{i,i'\}\subset\{1,\ldots,a\}\) and unordered pair \(\{j,j'\}\subset\{1,\ldots,b\}\), one component \(J_{ii';jj'}\) of codimension three. It is the projective join of two disjoint-coordinate Segre varieties \((\mathbb P^1)^{a-2}\) and \((\mathbb P^1)^{b-2}\), hence has dimension \(a+b-3\).

At a general closed point of \(B_j\), the transverse analytic germ is the vertex of the affine Segre cone over \((\mathbb P^1)^a\), with multiplicity \(a!\). At a general point of \(A_i\), it is the analogous affine Segre cone over \((\mathbb P^1)^b\), with multiplicity \(b!\). At a general point of every \(J_{ii';jj'}\), the transverse analytic germ is the threefold ordinary node \(uv-wz=0\), of multiplicity two.

There are no other irreducible components. Thus
\[
\#\operatorname{Irr}\operatorname{Sing}(X_{a,b})_{\mathrm{red}}
=b\mathbf 1_{a\ge2}+a\mathbf 1_{b\ge2}+\binom a2\binom b2.
\]
The variety is smooth exactly for \(a=b=1\). If exactly one parameter is one and the other exceeds one, its singular locus consists of one point. If both parameters are at least two, its singular locus has codimension three. For example \(X_{2,2}\), a projective complete intersection of two quadrics, has exactly five singular lines.

## Assumptions and scope

All schemes are over \(\mathbb C\), all parameters \(a,b\) are positive integers, and singular locus means its underlying reduced closed subscheme. A *general point* means a closed point in a specified nonempty Zariski-open subset of a component, avoiding its intersections with the remaining components. A projective join includes both endpoint varieties. The Segre variety \((\mathbb P^1)^0\) means one point. This is an all-parameter classification, not merely a finite computational census.

Let \(C_m\subset\mathbb A^{2^m}\) denote the affine cone over the standard Segre embedding of \((\mathbb P^1)^m\), where \(m\ge1\). Its distinguished corner tensor coordinate is \(t\). For \(m\ge2\), \(C_m\) is smooth outside its vertex and singular at that vertex; \(C_1=\mathbb A^2\). The stated transverse germs are local analytic products with smooth factors; no assertion is made about embedded components or multiplicities of the global Jacobian singular scheme.

## Proof

**1. A two-cone presentation.** Every order ideal is either a subset of the first antichain, or the complete first antichain together with a subset of the second. The two Boolean sublattices share exactly the complete first-level ideal. Hibi's straightening relations for incomparable ideals therefore split into the Boolean relations within the two sublattices; no incomparable pair uses one ideal strictly from each of them. A Boolean Hibi ring on \(m\) elements is the homogeneous coordinate ring of the affine Segre cone \(C_m\), with \(2^m\) tensor coordinates. Identifying the unique shared variable gives, scheme-theoretically,
\[
\operatorname{Spec}R(P_{a,b})\ \cong\ C_a\times_{\mathbb A^1_t}C_b.
\]
Here on each factor \(t=\prod_{i=1}^m u_i\) in its rank-one tensor parametrization \(\bigotimes_i(u_i,v_i)\); choosing opposite Boolean orientations on the two sublattices merely relabels the coordinates. The common grading scales all tensor coordinates simultaneously, so \(X_{a,b}=\operatorname{Proj}R(P_{a,b})\) is the quotient of the nonzero affine cone by scalar multiplication. The Hibi normal-domain theorem ensures no extraneous components are introduced in the fiber product. As \(\dim C_m=m+1\), the total affine cone has dimension \(a+b+1\).

**2. The differential of the corner coordinate.** At any nonzero rank-one tensor of \(C_m\), the cone is smooth. On a local product chart the corner function is a unit times the product of the \(u_i\)'s, multiplied by the local scale coordinate. If the corner coordinate vanishes, its differential is nonzero exactly when *one* \(u_i\) vanishes; it vanishes exactly when *at least two* of them vanish. If the corner coordinate is nonzero, its derivative along the scalar direction is nonzero. This follows from the ordinary product rule and is unaffected by choosing a different trivializing tensor chart.

**3. Singularity criterion.** If both tensors are nonzero, the fiber product is a hypersurface inside the product of two smooth cones. Its defining function is \(t(x)-t(y)\). The Jacobian criterion and step 2 show that the point is singular precisely when at least two distinguished \(u\)-factors vanish on *each* side. When the first tensor is zero and the second nonzero, the fiber-product equation still has nonzero differential with respect to the shared coordinate in the first ambient tensor space. The tangent space therefore has dimension \(2^a+b\), whereas the expected dimension is \(a+b+1\); this point is singular exactly when \(2^a>a+1\), that is, \(a\ge2\). The symmetric argument applies when only the second tensor is zero. The total zero tensor is discarded by \(\operatorname{Proj}\). This exhausts the singular points.

**4. Components and their geometry.** In the first-zero locus the remaining tensor has corner coordinate zero. The divisor \(t=0\) on the nonzero Segre cone has exactly \(b\) irreducible pieces, obtained by setting a specified \(u_j=0\); their projectivizations are the Segre varieties \((\mathbb P^1)^{b-1}\). They contribute the \(B_j\)'s when \(a\ge2\), with dimension \(b-1\). Similarly the second-zero locus contributes \(a\) Segre components \(A_i\) when \(b\ge2\), of dimension \(a-1\).

With both tensors nonzero, the singularity criterion prescribes a pair of vanishing \(u\)'s on each side. For each choice of two indices on each side, the corresponding closed locus is the projective join of the indicated two Segre faces. This follows because the common tensor corner coordinate is identically zero on both faces, so their nonzero coordinates may be scaled independently and jointly projectivized. Its dimension is \((a-2)+(b-2)+1=a+b-3\). The open subset with both tensors nonzero and *exactly* the chosen vanishing factors is nonempty and irreducible. Its closure is \(J_{ii';jj'}\).

These components are pairwise distinct: a general point of a boundary component has one entire tensor equal to zero and exactly one vanishing factor on the other side, whereas a general point of a mixed join has both tensors nonzero and exactly the indicated two vanishing factors on each side. This also proves no listed component is contained in another. Since step 3 exhausts the singular points, the list is complete and the stated counts and codimensions follow.

**5. Transverse germs.** At a general point of \(B_j\), the second tensor is smooth and \(dt\ne0\), so the fiber-product equation eliminates one smooth coordinate on that factor. After quotienting by scalar multiplication, a neighborhood is analytically \(C_a\times\mathbb A^{b-1}\) near the zero section. The transverse singularity is therefore the vertex of \(C_a\). Its Hilbert-Samuel multiplicity is the Segre degree \(a!\), since \(\deg((\mathbb P^1)^a,\mathcal O(1,\ldots,1))=a!\). Similarly \(A_i\) has transverse germ \(C_b\) and multiplicity \(b!\).

At a general point of \(J_{ii';jj'}\), after trivializing all nonvanishing tensor factors, the first corner coordinate equals a unit times \(u_i u_{i'}\), and the second equals a unit times \(u_j u_{j'}\). All other coordinates are smooth parameters; absorbing the units into variables gives the transverse local equation \(u_i u_{i'}-u_j u_{j'}=0\), an ordinary threefold node. This proves the full generic local-model assertions.

## Verification

A standalone exact checker `hibi_bipartite_checker.py` and its deterministic output `hibi_bipartite_checks.json` are included. The checker constructs *all* Boolean straightening quadrics for the two sublattices (with the common variable identified), forms their Jacobian matrices, and compares rank with the singularity criterion at a finite set of rank-one tensor representatives and zero-tensor boundary representatives. It tested \(1,815\) nonzero representatives across the nine parameter pairs \((1,1),(1,2),(1,3),(2,2),(2,3),(3,2),(3,3),(2,4),(4,2)\), using both moduli \(1000003\) and \(1000033\), with no disagreement. Run `python3 hibi_bipartite_checker.py` to regenerate the JSON and compare it with `hibi_bipartite_checks.json`. The calculations are finite consistency checks, **not** a proof of completeness for arbitrary parameters, and are not an independent review.

## Relationship to prior work

Hibi's quadratic straightening presentation and the normality of Hibi rings, used in step 1, are established. Wagner (1996, Theorem 2.3 and Section 3) gives a general singular-orbit criterion and associated-graded local-ring approach for all projective Hibi varieties. Lakshmibai–Mukherjee (2007, Theorem 6.9) gives an affine Hibi singular-locus criterion. Gonciulea–Lakshmibai (1997, Theorem 12.3) treats specific ladder-determinantal Hibi families; Friedl (2015) computes global class and Picard groups of projective Hibi varieties. These general/specialized results are premises and comparison points, not claimed as new. The mathematical claim here is the explicit *complete* irreducible-component decomposition and closed count for this two-level complete-comparability family, together with the generic Segre-cone and nodal transverse analytic germs. Universal orbit criteria require a nontrivial specialization to recover these component formulas and do not themselves state the asserted generic analytic types. No independence or exhaustive literature novelty certification is claimed.

## Limitations

The proof works over \(\mathbb C\); no claim is made about arbitrary positive-characteristic analytic singularity types. Singular loci are classified as reduced sets of irreducible subvarieties, not as full nonreduced Jacobian schemes. The stated generic analytic models need not describe intersections or special points on components. General published orbit and cotangent-space criteria might furnish another derivation of these specialized formulas; despite direct comparison of relevant texts, independently locating every equivalent formulation is not guaranteed. The checker tests finitely many representative points, not all points of those varieties or the infinite family.

## References

- T. Hibi, *Distributive lattices, affine semigroup rings and algebras with straightening laws*, in **Commutative Algebra and Combinatorics**, Advanced Studies in Pure Mathematics 11 (1987), 93–109.
- D. G. Wagner, *Singularities of Toric Varieties Associated with Finite Distributive Lattices*, **Journal of Algebraic Combinatorics** 5 (1996), 149–165, DOI 10.1023/A:1022469218716; full text available at https://scispace.com/pdf/singularities-of-toric-varieties-associated-with-finite-3okhe4d63h.pdf.
- N. Gonciulea and V. Lakshmibai, *Schubert varieties, toric varieties and ladder determinantal varieties*, **Annales de l'Institut Fourier** 47 (1997), 1013–1064, DOI 10.5802/aif.1590; full text https://www.numdam.org/article/AIF_1997__47_4_1013_0.pdf.
- V. Lakshmibai and H. Mukherjee, *Singular Loci of Hibi Toric Varieties*, arXiv:0706.2686v1 (first posted 18 June 2007), https://arxiv.org/pdf/0706.2686.
- T. Friedl, *Divisors on Projective Hibi Varieties*, arXiv:1506.02407v1 (first posted 8 June 2015), https://arxiv.org/pdf/1506.02407.
