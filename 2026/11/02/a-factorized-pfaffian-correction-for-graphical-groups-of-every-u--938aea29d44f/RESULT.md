# A factorized Pfaffian correction for graphical groups of every unicyclic graph

## Finding

Let \(G=(V,E)\) be a finite connected simple unicyclic graph with \(n=|V|\) and unique cycle \(C\) of length \(\ell\ge 3\). For a spanning edge support \(S\subseteq E\), let \(\nu(S)\) be the largest matching size in \((V,S)\), and put
\[
H_G(w,z)=\sum_{S\subseteq E}w^{|S|}z^{\nu(S)}.
\]
Deleting the cycle **edges** partitions \(G\) into rooted trees \(T_v\), one for each \(v\in V(C)\). Write \(\nu_v(S)\) for the matching number of the supported rooted tree \((V(T_v),S)\), and \(\nu_v^0(S)\) for that of the same graph with its root \(v\) deleted. Define the root-unsaturated support polynomial
\[
Q_v(w,z)=\sum_{\substack{S\subseteq E(T_v)\\\nu_v(S)=\nu_v^0(S)}}w^{|S|}z^{\nu_v^0(S)}.
\]
For every prime power \(q\), let \(B_G(y)\) be the alternating weighted adjacency matrix, with independent edge weights \(y\in\mathbb F_q^E\). Its complete half-rank enumerator is
\[
R_G(q,z)=\sum_{y\in\mathbb F_q^E}z^{\operatorname{rank}B_G(y)/2}.
\]
**Theorem.** For every such graph and every prime power,
\[
\boxed{R_G(q,z)=H_G(q-1,z)\qquad(\ell\text{ odd}),}
\]
whereas for even \(\ell\),
\[
\boxed{R_G(q,z)=H_G(q-1,z)
 +(q-1)^{\ell-1}z^{\ell/2-1}(1-z)
 \prod_{v\in V(C)}Q_v(q-1,z).}
\]
In particular, every rank-stratum count is a polynomial in \(q\), with an explicit correction that factors over the trees attached to the unique cycle. For every **odd** prime power \(q\), the number of irreducible complex characters of the graphical group \(\mathbf G_G(\mathbb F_q)\) of degree \(q^j\) is
\[
\boxed{\operatorname{ch}(G,j;q)=q^{n-2j}[z^j]R_G(q,z).}
\]
The rank-enumerator identity itself is valid in characteristic two.

The correction also has a direct pointwise description. If the nonzero-weight support is missing a cycle edge, or the unique cycle is odd, the alternating matrix has rank exactly twice the support matching number. If the complete cycle has even length, a rank drop of precisely two occurs **only** when every attached supported rooted tree has a maximum matching leaving its cycle root unmatched, and the two alternating products of nonzero cycle weights cancel. When the rooted condition holds, exactly one out of every \(q-1\) nonzero cycle-weight choices cancels.

## Assumptions and scope

The graph is undirected, finite, connected, simple, and has exactly one cycle, of length at least three. There are no loops or parallel edges. A root-unsaturated support means \(\nu_v(S)=\nu_v^0(S)\); the equality does not mean that every maximum matching leaves the root unmatched, only that at least one does. The counting variable \(z\) marks half the matrix rank; \(w\) marks included (nonzero) support edges. The empty support has matching number zero, and a rooted tree with no edges contributes \(Q_v=1\).

The finite-field rank statement covers every prime power. The character statement uses the established odd-characteristic graphical-group character-rank correspondence, so no characteristic-two character formula is asserted here. The theorem enumerates ordinary irreducible characters by degree, not conjugacy classes by size.

## Proof

**1. Rank and perfect matchings.** For an alternating matrix over any field, its rank is twice the largest integer \(r\) for which some principal Pfaffian of order \(2r\) is nonzero (the alternating principal-minor rank criterion). A principal Pfaffian is a signed sum of products of edge weights indexed by perfect matchings of the supported graph induced on its chosen vertices. Its half-rank is therefore at most \(\nu(S)\).

Two distinct perfect matchings on the same vertex set have a nonempty symmetric difference consisting of even cycles. Since a unicyclic graph has only one cycle, a supported induced subgraph has at most two perfect matchings; if there are two, the unique cycle must be even, fully present, and their symmetric difference is precisely its edges. In particular, every perfect matching on an induced forest is unique. If the supported graph has no full even cycle, a maximum matching gives a nonzero principal Pfaffian (one nonzero monomial), so the rank equals \(2\nu(S)\).

**2. Which supports permit cancellation?** Suppose the unique cycle is even and fully contained in \(S\). Removing its edges yields rooted components \(T_v\). For a chosen support \(S_v=S\cap E(T_v)\), abbreviate \(a_v=\nu_v^0(S_v)\), \(b_v=\nu_v(S_v)\). Necessarily \(b_v\in\{a_v,a_v+1\}\). A matching that uses no cycle-to-tree edge has maximum size
\[
M_0=\ell/2+\sum_{v\in V(C)}a_v.
\]
If every \(b_v=a_v\), any matching using at least one cycle-to-tree edge occupies a cycle vertex and can use at most \(\ell/2-1\) cycle edges; it uses at most \(\sum_v a_v\) edges meeting the rooted trees, so it has size less than \(M_0\). Thus \(\nu(S)=M_0\), and **every** maximum matching splits into a perfect cycle matching and independent maximum matchings in the trees away from their roots.

Conversely, if \(b_v=a_v+1\) for some \(v\), a matching of the supported tree achieving \(b_v\) necessarily uses an edge from its root to the exterior. Combine it with maximum outside-tree matchings at all other roots and a maximum matching of the remaining cycle path \(C-v\). This produces a matching of size \(M_0\) using a cycle-to-tree edge. If \(\nu(S)>M_0\), any maximum matching must use a cycle-to-tree edge; if \(\nu(S)=M_0\), the displayed matching is itself such a maximum matching. Either way, at least one maximum matching uses a cycle-to-tree edge.

**3. Pfaffian of a maximal principal block.** If a maximum matching uses a cycle-to-tree edge, take precisely the endpoints of that matching. The induced graph has only that one perfect matching: a second one could differ only along the full cycle, impossible when a cycle vertex is matched outside. Its maximal principal Pfaffian is one nonzero monomial, so rank equals \(2\nu(S)\), irrespective of weight values.

It remains to consider supports with the entire even cycle present and \(b_v=a_v\) for every root. Every maximum matching uses all cycle vertices internally, while its outside-tree restriction is a maximum matching of a forest. For any chosen set of \(2\nu(S)\) vertices admitting a perfect matching, the forest outside the cycle has a **unique** perfect matching. Consequently every potentially nonzero maximal principal Pfaffian has the form
\[
\pm\left(\prod_{e\in M_{\rm out}}y_e\right)\Delta_C(y),
\qquad
\Delta_C(y)=\prod_{e\in M_{\rm odd}}y_e\ \pm\prod_{e\in M_{\rm even}}y_e,
\]
where \(M_{\rm odd}\) and \(M_{\rm even}\) are the two complementary perfect matchings of the even cycle, and the sign is fixed by the alternating matrix convention. Both products are nonzero and use disjoint cycle-edge sets. Therefore the rank is \(2\nu(S)\) precisely when \(\Delta_C(y)\ne0\).

For \(\Delta_C(y)=0\), all order-\(2\nu(S)\) principal Pfaffians vanish. Choose a maximum matching and remove one of its cycle edges. The remaining \(\nu(S)-1\) matching edges span fewer than all cycle vertices, so the induced support is a forest with a unique perfect matching. This gives a nonzero order-\(2\nu(S)-2\) principal Pfaffian. Hence cancellation lowers the rank **exactly** to \(2\nu(S)-2\), never further.

**4. Exact finite-field count and factorization.** Fix a support \(S\) satisfying the even-cycle/root-unsaturation criterion. There are \((q-1)^{|S|}\) edge assignments with that support. For every choice of all but one nonzero cycle edge weight, the equation \(\Delta_C(y)=0\) forces exactly one nonzero choice of the remaining cycle weight. Thus exactly \((q-1)^{|S|-1}\) assignments have the rank decreased by two.

Start with the support-matching enumerator \(H_G(q-1,z)\), which assigns every specialization of support \(S\) the provisional half-rank \(\nu(S)\). Each exceptional specialization must instead contribute \(z^{\nu(S)-1}\), producing a correction \((q-1)^{|S|-1}(z^{\nu(S)-1}-z^{\nu(S)})\). The exceptional supports are exactly those including the entire even cycle and having \(\nu_v(S_v)=\nu_v^0(S_v)\) independently at all roots. On these supports, \(\nu(S)=\ell/2+\sum_v\nu_v^0(S_v)\). Summing their corrections and separating the independent rooted-tree choices gives
\[
(q-1)^{\ell-1}z^{\ell/2-1}(1-z)\prod_v Q_v(q-1,z).
\]
For odd cycles there are no exceptional supports. This proves both displayed rank-enumerator formulas, including characteristic two, and immediately proves polynomiality in \(q\).

**5. Characters.** For odd \(q\), the established graphical-group rank formula (O'Brien–Voll, as used by Rossmann) identifies the number of degree-\(q^j\) ordinary irreducible characters with \(q^{n-2j}\) times the number of alternating commutator-matrix specializations of rank \(2j\). The matrix here is exactly \(B_G(y)\). Applying the already proved rank enumerator yields the character formula. The degree-squared identity follows automatically:
\[
\sum_j\operatorname{ch}(G,j;q)q^{2j}
=q^n\sum_j[z^j]R_G(q,z)=q^{n+|E|}=q^{2n}=|\mathbf G_G(\mathbb F_q)|.
\]

## Verification

The standalone, standard-library-only `verify.py` implements independent support-matching, rooted-factorization, and direct finite-field skew-matrix-rank computations. For ten distinct connected unicyclic graph configurations, including both cycle parities and pendant trees of varying shapes, it enumerates all edge assignments over \(\mathbb F_2\) and \(\mathbb F_3\). For **20 exhaustive graph-field cases**, the direct matrix-rank histogram, the support/Pfaffian exceptional-support formula, and the independently assembled rooted-product correction agree coefficient by coefficient. It checks that each histogram sums to the expected number of weight assignments, and returns `VERIFY_OK`.

For a four-cycle with a two-edge pendant path, \(n=6\), the exceptional factor is
\[
Q_0(w,z)=1+(w+w^2)z,
\qquad Q_v(w,z)=1\ (v\ne0).
\]
Over \(\mathbb F_3\), the rank-specialization vector is \((1,56,384,288)\) for half-ranks \(0,1,2,3\), respectively. The corresponding irreducible-character multiplicities in degrees \(1,3,9,27\) are \((729,4536,3456,288)\); their degree-squared sum is \(3^{12}\), the group order.

These finite checks are diagnostic, not a proof of the all-graph theorem. The proof is the Pfaffian-matching argument above.

## Relationship to prior work

Rossmann (first public version 12 July 2021, arXiv:2107.05564), Question 1.10, asks for the irreducible-character degree numbers of graphical groups over finite fields. His rank-specialization framework and the O'Brien–Voll character formula are used here, not claimed as new.

The 2014 paper of Li and Yu, *The skew-rank of oriented graphs* (arXiv:1404.7230), Theorems 4.2 and 4.5, is an especially close structural predecessor: it classifies the skew rank of unicyclic graphs when each present edge has weight \(\pm1\) over the reals. In contrast, the present theorem counts **every assignment of arbitrary finite-field weights, including zeros and every characteristic**, resolves the exact cancellation fraction, produces a factorized correction over all rooted attachments, and translates it to the complete graphical-group character-degree distribution. A weighted finite-field restatement without this enumeration would not be the present claim.

Previously published full rank-enumerator formulas for graphical groups cover trees and bare cycles, and a separate cone extension. The tree formula has no cycle cancellation, the bare-cycle formula has no attached rooted trees, and coning does not yield a general unicyclic graph. Their exact scientific implications were compared; the factorized full-unicyclic formula is not among their stated consequences. These sources remain important ingredients and close overlap risks, not novelty certifications.

## Limitations

The result applies to connected simple graphs with exactly one cycle, not arbitrary cactus or multicyclic graphs. The formula is exact but may require exponentially many supports; no general polynomial-time evaluation is claimed. The character formula is restricted to odd characteristic, whereas the rank count itself is valid over every finite field. The Li–Yu fixed-weight rank classification predates this result and is explicitly acknowledged. Publication priority is best knowledge after targeted searches and inspected sources, not a theorem of uniqueness; a broader unpublished or differently titled finite-field Pfaffian enumeration might imply the formula. Independent mathematical audit is not supplied.

## References

1. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1, 12 July 2021; *Bull. Lond. Math. Soc.* 54 (2022), 1923–1943, DOI 10.1112/blms.12665.
2. E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*, arXiv:1203.3050; *Trans. Amer. Math. Soc.* 367 (2015), 7775–7796, DOI 10.1090/tran/6276.
3. X. Li and G. Yu, *The skew-rank of oriented graphs*, arXiv:1404.7230v1, 29 April 2014, especially Theorems 4.2 and 4.5.
4. *Tree graphical groups have matching-support character polynomials*, public result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65 .
5. *Cycle graphical groups have an explicit character-degree enumerator*, public result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e .
6. *Coning recurrence for character degrees of graphical groups*, public result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-coning-recurrence-for-character-degrees-of-graphical-groups--732adc755a75 .
