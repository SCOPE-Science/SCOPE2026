# The full rational homology character of the Pappus independence complex

## Finding
Let \(P\) denote the Pappus graph, \(G=\operatorname{Aut}(P)\), and \(X=\operatorname{Ind}(P)\). The 216-element automorphism group acts on \(\widetilde H_4(X;\mathbb Q)\), and **the following table determines its entire character**, including all 13 conjugacy classes (two of which share a displayed row). Cycle types refer to permutations of the 18 graph vertices. The centralizer size is needed only to distinguish the two fixed-point-free order-three types.

| Vertex cycle type of \(g\) | \(|C_G(g)|\) when needed | Number | \(\operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))\) |
|:---|:---:|---:|---:|
| \(1^{18}\) | — | 1 | 10 |
| \(2^6 1^6\) | — | 9 | −2 |
| \(2^7 1^4\) | — | 18 | 2 |
| \(2^9\) | — | 18 | 0 |
| \(3^5 1^3\) | — | 12 | 1 |
| \(3^6\) | 18 | 12 | −2 |
| \(3^6\) | 108 | 2 | 1 |
| \(4^3 2^3\) | — | 18 | 2 |
| \(6^2 3 2 1\) | — | 36 | −1 |
| \(6^2 3^2\) | — | 18 | 1 |
| \(6^3\) | — | 36 | 0 |
| \(12\,6\) | — | 36 | −1 |

This character has squared norm \(\langle\chi,\chi\rangle_G=2\), and its invariant subspaces have dimensions
\[
\dim\widetilde H_4(X;\mathbb Q)^G=0,\qquad
\dim\widetilde H_4(X;\mathbb Q)^{G^+}=0,
\]
where \(G^+\) is the index-two subgroup preserving each class of the bipartition. Therefore both \(|X|/G\) and \(|X|/G^+\) have vanishing reduced rational homology. All other reduced rational homology of \(X\) vanishes.

The two types of automorphisms with vertex cycle profile \(3^6\) have **identical edge cycle profile \(3^9\)**, but opposite-sign fourth-homology traces \(-2\) and \(1\). Thus neither the vertex nor the edge permutation cycle type determines the homology character by itself.

## Assumptions and scope
The finite simple graph has labeled vertices \(0,\ldots,17\). Its edges comprise the Hamiltonian cycle \(\{i,i+1\bmod18}\}\) together with the chords \(\{i,i+a_i\bmod18}\}\), where \((a_0,\ldots,a_{17})\) repeats \((5,7,-7,7,-7,-5)\) three times. The resulting graph is cubic with 27 edges. An independent set is a subset containing no graph edge; the nonempty independent sets are precisely the simplices of \(X\). Every automorphism of \(P\) acts simplicially on \(X\). The displayed action and homology calculations use rational coefficients; the equivariant integral lattice is not classified.

For an automorphism \(g\), \(C_G(g)=\{h\in G: hg=gh\}\) is its centralizer. The full character is a complete isomorphism invariant of the semisimple rational representation, independently of a particular irreducible labeling.

## Proof
**Homology concentration.** The supplied standalone verifier generates all nonempty independent sets directly from the LCF graph. Its simplex counts in degrees zero through eight are
\[
(18,126,438,801,756,348,90,18,2).
\]
It constructs 1,293 disjoint Forman matching pairs by sequential vertex toggles in the explicit order
\[
(4,7,16,15,12,2,14,13,6,10,5,8,11,1,17,9,3,0).
\]
Each pair is checked as a genuine facet/cofacet pair. Reversing the matched arrows and directing all other arrows downwards, an exhaustive topological sort visits every one of the 2,597 nonempty faces and checks all 11,430 Hasse incidences. Therefore the matching is acyclic. Its unmatched faces consist of exactly one vertex and ten four-simplices, with no cells in consecutive positive dimensions. The associated CW complex is a wedge of ten four-spheres, and so \(\widetilde H_i(X;\mathbb Z)\) is zero except for \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{10}\). This nonequivariant homotopy description is a premise of the character calculation, **not its novelty claim**.

**Automorphisms.** Breadth-first search reconstructs the complete shortest-path distance matrix. Exhaustive injective backtracking preserving that matrix generates 216 permutations; each is then separately checked to preserve every graph edge. Conversely every graph automorphism preserves the distances, so this search is exhaustive. Conjugation by each of the 216 permutations partitions this set into exactly 13 conjugacy classes. Each element is classified by its vertex cycle type; for the shared \(3^6\) type a direct centralizer count is performed, producing sizes 18 and 108.

**Character calculation.** For each \(g\), the signed fixed-face Lefschetz formula is
\[
\operatorname{tr}\bigl(g\mid\widetilde H_4(X;\mathbb Q)\bigr)
=-1+\sum_{\substack{\emptyset\ne S\subseteq V(P)\\ S\ \mathrm{independent},\ gS=S}}(-1)^{|S|-1}\operatorname{sgn}(g|_S).
\]
This equals the reduced alternating trace of the augmented simplicial chain complex because reduced homology is confined to degree four. A **second independent implementation** enumerates the vertex orbits of \(g\), discards orbits containing an internal edge, forms the conflict graph on the remaining orbits, and returns the negative of its independence polynomial evaluated at \(-1\). The equality follows because an invariant face is exactly an independent union of vertex orbits, and its alternating signed contribution is \((-1)^{k-1}\) when it comprises \(k\) orbits. Both algorithms agree on every one of the 216 permutations, giving the displayed table. The exceptional order-three types have \(3^9\) edge cycles in both cases, verified by an independent action on the 27 edges.

**Representation consequences.** The character's squared norm is computed exactly as \(216^{-1}\sum_{g\in G}\chi(g)^2=2\). Its trivial-isotypic multiplicity in any subgroup \(H\) is \(|H|^{-1}\sum_{g\in H}\chi(g)\). The calculated sums are zero for the full group and for the 108 bipartition-preserving automorphisms. Over characteristic zero, finite-group coinvariants agree in homology with invariants, so the corresponding topological quotients have trivial reduced rational homology.

## Verification
Run `python3 verify_pappus_full.py` with the Python 3 standard library. It prints the exhaustive graph counts, the Forman-matching acyclicity certificate summary, all character table rows, the conjugacy-class check, and the subgroup invariant counts. The full 216-element signed fixed-face algorithm and the independent orbit-conflict algorithm agree entrywise; the case \(g(i)=i+6\bmod18\) has trace \(-2\), matching the narrower preexisting cyclic calculation. A successful recorded run is included as `verification_output.txt`. The proof is finite and exhaustive for precisely this graph; no extrapolation from finite sampling is used.

## Relationship to prior work
Barmak's *Star clusters in independence complexes of graphs* (2010 public preprint, sections 1–4) gives structural homotopy methods for triangle-free graph independence complexes, but its suspension theorems do not determine any Pappus automorphism representation. Przytycki and Silvero (2016 public preprint, sections 2 and 6) examine suspension and wedge properties of independence complexes of circle graphs rather than this exact action. Tsukuda (2017) establishes a nonequivariant relation between incidence-graph independence complexes and Alexander duality; the accessible abstract does not establish an automorphism character. The previously published **Pappus order-three symmetry** calculation determines only the subgroup generated by the period-six translation (character \((10,-2,-2)\) on three elements), explicitly leaving the full automorphism action unclassified. That cyclic restriction follows from the present table but does not imply it: in particular it cannot distinguish the 13 conjugacy classes or determine the full-group and index-two quotient homology. This comparison concerns implications of the stated theorems, not merely the absence of matching titles.

## Limitations
The result is an exact finite-graph calculation and does not classify an infinite family, integral equivariant lattices, or homotopy types of the quotients. Publication priority is subject to the risk of an unindexed equivalent calculation. The inspected 2017 incidence-graph article was available by abstract rather than its full text, and hence has not been globally ruled out, although its stated theorem concerns nonequivariant homotopy equivalence. The 12 displayed character rows combine two distinct conjugacy classes with the same value and graph cycle profile; the verifier checks all 13 classes individually.

## References
1. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public 2010-07-02), especially §§1–4. https://arxiv.org/html/1007.0418v1
2. Jozef H. Przytycki and Marithania Silvero, *Homotopy type of circle graphs complexes motivated by extreme Khovanov homology*, arXiv:1608.03002v1 (first public 2016-08-09), especially §§2 and 6. https://arxiv.org/html/1608.03002v1
3. Shuichi Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46. https://cdm.ucalgary.ca/article/view/62277
4. *Order-three symmetry on Pappus independence homology*, published mathematical record; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31
5. *Pappus Graph*, Wolfram MathWorld, graph identification and LCF notation. https://mathworld.wolfram.com/PappusGraph.html
