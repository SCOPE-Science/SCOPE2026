# Induced-matching and saturation spectra of the order-three projective-plane Levi graph

## Finding
Let \(\Pi=\mathrm{PG}(2,3)\), and let \(G\) be its bipartite point--line incidence (Levi) graph. Define \(J_G(z)=\sum_{M}z^{|M|}\), where the sum includes the empty matching and ranges over **induced** matchings \(M\subseteq E(G)\). Then
\[
J_G(z)=1+52z+702z^2+3276z^3+5031z^4+1404z^5+234z^6.
\]
There are exactly 10,700 induced matchings. Every induced matching of five flags extends to an induced matching of six flags in **exactly one way**. The inclusion-maximal induced matchings have only cardinalities four and six, with counts respectively 1,989 and 234; no maximal induced matching has cardinality five. The full incidence-graph automorphism group has order 11,232 and splits the 10,700 induced matchings into twelve orbits; its inclusion-maximal matchings form three orbits of sizes 117, 1,872 and 234 (the first two of cardinality four, the last of cardinality six).

## Assumptions and scope
Points of \(\Pi\) are the thirteen nonzero one-dimensional subspaces of \(\mathbf F_3^3\); lines are the thirteen zero sets of nonzero linear forms, each normalized by its first nonzero coordinate. The point indexed by vector \(v\) lies on the line indexed by vector \(w\) exactly when \(v\cdot w=0\) in \(\mathbf F_3\). Flags \((p,\ell)\) represent graph edges. A flag family is an induced matching precisely when its incidence matrix on the selected points and lines is the identity after corresponding row and column orderings: \(p_i\in\ell_j\) if and only if \(i=j\). This is the strong representative system (SRS) studied by Illés, Szőnyi and Wettl (1991); the terminology and its general bounds are not new. All counts here concern the specified order-three plane, not arbitrary projective planes or other graph classes.

## Proof
**Private-line counting identity.** For each point subset \(S\), put \(t_S(p)=|\{\ell:\ell\cap S=\{p\}\}|\) for \(p\in S\). A chosen matching with selected points exactly \(S\) must select for each \(p\in S\) a line meeting \(S\) only at \(p\). Conversely, independently choosing one of those lines for each \(p\) gives an induced matching, since these lines must be distinct and cannot contain another selected point. Therefore
\[
J_G(z)=\sum_{S\subseteq\Pi_{\rm points}}z^{|S|}\prod_{p\in S}t_S(p).
\]
The empty product is one. A finite exact evaluation of the thirteen-point sum requires only 8,192 subsets; no random sampling or numerical approximation is involved.

**Exhaustive incidence certificate.** The following is the complete list of *nonzero-weight* tangent profiles \((|S|;\text{sorted positive }t_S(p);\text{point-subset count})\), with the empty profile included: 

| Cardinality | Sorted tangent multiplicities | Number of point subsets |
|---:|:---|---:|
| 0 | empty | 1 |
| 1 | (4) | 13 |
| 2 | (3,3) | 78 |
| 3 | (3,3,3) | 52 |
| 3 | (2,2,2) | 234 |
| 4 | (3,3,3,3) | 13 |
| 4 | (1,2,2,2) | 468 |
| 4 | (1,1,1,1) | 234 |
| 5 | (1,1,1,1,2) | 702 |
| 6 | (1,1,1,1,1,1) | 234 |

Every other subset gives product zero. Multiplying each number of subsets by the product of its profile gives all coefficients of the displayed polynomial. The exact statement is finitely checkable by looping over the \(2^{13}\) subsets and evaluating all thirteen incidence-line intersections; the standalone `verify_geometry.py` implements precisely this check and asserts every coefficient.

**Saturation and completion.** Enumerate all 52 flags and form the 52-vertex conflict graph whose vertices are flags. Two flags conflict when they share an endpoint or when either selected point lies on the other selected line. Induced matchings of \(G\) are exactly independent sets in this conflict graph. For each independent set \(M\), its one-flag extension set consists of the conflict-graph vertices nonadjacent to every vertex of \(M\). `verify_geometry.py` checks this set directly for all 10,700 configurations and finds exactly 1,989 maximal four-flag matchings, 234 maximal six-flag matchings and no others. It additionally checks that all 1,404 five-flag matchings have exactly one extension; each of the 234 six-flag matchings has precisely six five-flag subfamilies, providing a second counting consistency check. Separately, `verify_independent.cpp` enumerates the independent sets via independent include/exclude recursion on *all 52 flag vertices*, independently recalculates the conflict predicate and confirms the same polynomial, maximality distribution and unique-extension property. These are finite exhaustive proofs for this fixed graph, not assertions about any infinite family.

**Group-orbit certificate.** Coordinate swaps, a 3-cycle, an elementary shear, and the diagonal transformation with first entry two generate all 5,616 projective linear collineations of \(\mathrm{PG}(2,3)\). Together with the dot-product polarity swapping points and lines, they generate the full order-11,232 incidence-graph automorphism group. The fundamental theorem of projective geometry ensures that all incidence-preserving automorphisms arise in this way (no nontrivial field automorphism exists over \(\mathbf F_3\)). The same standalone verifier constructs and checks the 5,616 collineations, applies the five flag permutations to all matchings, computes twelve complete disjoint orbits and checks the embedded `orbit_classes.csv` representatives and cardinalities. The three maximal orbit sizes stated above follow from this exhaustive certificate.

**Size ceiling.** For completeness, let \(B\) be the thirteen-by-thirteen point--line incidence matrix. The projective-plane identity \(BB^\mathsf T=3I+\mathbf1\mathbf1^\mathsf T\) gives singular values four on constants and \(\sqrt3\) on their orthogonal complements. Any induced matching of size \(k\) yields \(k\) incidences between its selected \(k\) points and \(k\) lines, so
\[
k\ge\frac{4k^2}{13}-\sqrt3\left(k-\frac{k^2}{13}\right).
\]
For \(k>0\), this forces \(k\le13(1+\sqrt3)/(4+\sqrt3)<7\), agreeing with the finite census. This bound alone does not establish the enumerator or the unique-extension claim.

## Verification
From one directory containing the three companion files, run `python3 verify_geometry.py`; then compile and run `c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. The Python verifier recomputes and checks `orbit_classes.csv`, the tangent profiles, the complete polynomial, unique five-flag extensions, maximal configurations, the automorphism generators and twelve orbit certificates. The independent C++ verifier generates all 52 flags anew, uses independent-set branching rather than point-subset products, and checks every coefficient and maximality/extension claim. Both are standalone, require no nonstandard Python packages, and have been run with successful assertions. The CSV uses zero-based indices in lexicographically ordered normalized projective vectors. Output logs are not substituted for code or independent mathematical reasoning; all computations are embodied in complete source files.

## Relationship to prior work
Illés, Szőnyi and Wettl (1991) introduce precisely these strong representative systems, prove general bounds on maximal size, and classify a structural condition for maximal systems of the smallest possible size (their Proposition 2.3). Thus the notion, general size bounds, and line-or-pencil characterization of maximal four-flag systems are **prior work**, not new contributions. Kiss, Marcugini and Pambianco (2008) classify semioval sizes and equivalence classes in \(\mathrm{PG}(2,3)\); this establishes related optimal tangent geometry, not an enumeration of all strong representative systems or their one-flag extension multiplicities. Mengyán (2008) studies partitions of flags into strong representative systems for non-prime plane orders, not the individual-system census at the prime order three. The accessible abstract shows that focus; the publisher PDF was not accessible for full inspection. Kanj, Pelsmajer, Schaefer and Xia (2008) study induced matchings and their general extremal algorithms on several graph classes, not this complete finite-plane polynomial. The new assertion is the complete induced-matching census *together with* the five-flag unique-completion and saturation spectra, after crediting these prior structural statements. No claim of globally established publication priority or independent external confirmation is made.

## Limitations
The result is restricted to the 26-vertex order-three Levi graph. The group computation and finite census rely on complete verifiers, rather than a closed-form classification valid for arbitrary field order. Earlier small-order flag enumerations or tables may exist outside indexed sources; lack of a matching literature hit does not establish priority. In particular, the previously published four-flag maximality criterion already constrains the reported four-flag counts. The completion and orbit counts have only been checked for the specified plane.

## References
1. T. Illés, T. Szőnyi, F. Wettl, "Blocking sets and maximal strong representative systems in finite projective planes," *Mitt. Math. Sem. Giessen* 201 (1991), 97–107; public text: https://www.researchgate.net/publication/255720223_Blocking_sets_and_maximal_strong_representative_systems_in_finite_projective_planes.
2. G. Kiss, S. Marcugini, F. Pambianco, "Semiovals in projective planes of small order," *ACCT2008* (June 16–22, 2008), 151–154; full public text: https://www.researchgate.net/publication/228983042_Semiovals_in_projective_planes_of_small_order.
3. C. Mengyán, "Partitioning the flags of PG(2,q) into strong representative systems," *Contributions to Discrete Mathematics* 3(1) (2008), published 2008-02-06; https://doi.org/10.55016/ojs/cdm.v3i1.61981.
4. I. Kanj, M. J. Pelsmajer, M. Schaefer, G. Xia, "On the Induced Matching Problem," *STACS 2008*, 397–408, public 2008-02-06; https://doi.org/10.4230/LIPIcs.STACS.2008.1361.
