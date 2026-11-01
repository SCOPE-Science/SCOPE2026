# The Coxeter independence complex realizes a twisted eight-point augmentation representation

## Finding
Let \(F\) be the Fano plane with point set \(\{1,\ldots,7\}\), written as the seven nonzero vectors of \(\mathbb F_2^3\). Its lines are the three-sets \(\{a,b,a\mathbin{\oplus}b\}\) for distinct nonzero vectors \(a,b\), with \(\oplus\) bitwise addition. Let \(G\) have the 28 non-line three-subsets as vertices, with an edge between two such triples precisely when they are disjoint. Thus \(G\) is the 28-vertex Coxeter graph. Put \(X=\operatorname{Ind}(G)\) and \(\Gamma=\operatorname{Aut}(G)\).

Let \(\mathcal S\) be the set of Sylow-seven subgroups of \(\Gamma\). There are exactly eight. Write
\[
U=\left\{\sum_{S\in\mathcal S}a_S[S]\in\mathbb Q[\mathcal S]:\sum_{S\in\mathcal S}a_S=0\right\},
\]
and let \(\varepsilon:\Gamma\to\{\pm1\}\) be the sign of the permutation of \(\mathcal S\) induced by conjugation.

**Theorem (complete symmetry character).** The only nonzero reduced rational homology of \(X\) is in degree six and, as a rational \(\Gamma\)-representation,
\[
\boxed{\widetilde H_6(X;\mathbb Q)\cong\varepsilon\otimes U.}
\]
This seven-dimensional representation is absolutely irreducible. Equivalently, for every \(g\in\Gamma\),
\[
\operatorname{tr}\left(g\mid\widetilde H_6(X;\mathbb Q)\right)
=\varepsilon(g)\bigl(|\mathcal S^g|-1\bigr).
\]
The ordinary homotopy type \(X\simeq\bigvee^7S^6\) was established previously and is not the new conclusion. The theorem identifies how the seven homology generators transform *jointly* under all 336 graph automorphisms.

**Consequences.** The 168-element kernel \(\Gamma^+=\ker\varepsilon\) still acts irreducibly on \(\widetilde H_6(X;\mathbb Q)\). Hence the reduced rational homology of both \(|X|/\Gamma\) and \(|X|/\Gamma^+\) vanishes in every degree. For a Sylow-seven subgroup \(C\le\Gamma\), the quotient \(|X|/C\) instead has a one-dimensional sixth reduced rational homology group, with all other reduced rational homology zero.

## Assumptions and scope
The Fano point labels are integers one through seven interpreted as nonzero three-bit vectors. All 28 graph vertices are indexed in ascending lexicographic order. The action is that of the **entire** ordinary graph automorphism group on the abstract independence complex, not just the 168-element Fano collineation subgroup. Integral homotopy is used only to independently establish the concentration and rank of rational homology. The representation and quotient assertions are over \(\mathbb Q\); no assertion about integral equivariant lattices or quotient homotopy types is made. The unrelated 30-vertex Tutte–Coxeter graph and reflection-group Coxeter complexes are not intended.

## Proof
**1. Reconstruction and independent homotopy certificate.** The seven Fano lines are exactly the unordered sets \(\{a,b,a\oplus b\}\) and the remaining three-subsets yield 28 vertices. Disjointness gives a cubic graph with 42 edges. Enumerate independent sets as bit masks by successively adjoining index \(v\) precisely to those existing masks containing no neighbor of \(v\). This constructs exactly 196,009 independent sets including the empty set, with 196,008 nonempty faces.

An exact acyclic discrete-Morse matching can be given without relying on a previous calculation. In the augmented face poset, process the vertices in the fixed order \((0,2,4,\ldots,26,1,3,\ldots,27)\). At vertex \(v\), pair all still-unpaired faces \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both remain unpaired. The 28 passes produce 98,001 matched pairs and leave exactly seven unpaired seven-element faces. Remove the pair containing the empty set, discard the empty set, and restore its singleton as critical. This gives 98,000 ordinary matching pairs, one critical vertex and seven critical six-simplices.

For completeness, acyclicity is checked over the *entire* ordinary face poset: orient unmatched codimension-one incidences upward and matched incidences downward. There are precisely 1,319,724 incidences. An exact Kahn topological sort traverses all of them and removes all 196,008 nonempty faces, so the oriented Hasse diagram has no directed cycle. Forman's theorem therefore gives a CW model with one zero-cell and seven six-cells, with no intermediate cells. All attaching maps are null since the five-skeleton is a point. Hence \(X\simeq\bigvee^7S^6\), in particular \(\widetilde H_j(X;\mathbb Q)=0\) for \(j\ne6\) and \(\dim\widetilde H_6=7\).

**2. A fixed-orbit Lefschetz formula.** Fix any \(g\in\Gamma\). Its cycles on the 28 vertices define possible blocks for a \(g\)-invariant independent set. Discard every cycle that contains an edge of \(G\), then form a graph \(H_g\) on the remaining cycles, joining two distinct cycles if some vertex of one is adjacent in \(G\) to some vertex of the other. The fixed independent sets of \(G\) are exactly unions of independent vertex sets of \(H_g\).

If \(q\) permissible cycles together contain \(s\) original vertices, the orientation sign of \(g\) on the associated simplex is \((-1)^{s-q}\). Its contribution to the reduced alternating chain trace is therefore \((-1)^{s-1+s-q}=(-1)^{q+1}\). Including the reduced empty-face contribution \(-1\), the reduced Lefschetz number is
\[
\widetilde L(g)=-I_{H_g}(-1),\qquad
I_{H_g}(t)=\sum_{T\ \mathrm{independent\ in}\ H_g} t^{|T|}.
\]
Because the reduced homology is concentrated in **even** degree six, \(\widetilde L(g)\) equals the desired sixth-homology trace. The value \(I_{H_g}(-1)\) is obtained exactly by the deletion–closed-neighborhood recurrence \(I_H(-1)=I_{H-v}(-1)-I_{H-N[v]}(-1)\), with \(I_{\varnothing}(-1)=1\).

**3. Full automorphism enumeration and identification.** Backtracking over the images of a chosen vertex and its three neighbors, with every adjacency and nonadjacency preserved, enumerates all 336 distinct permutations of the graph vertices. No candidates are sampled or excluded by a heuristic bound: every automorphism has one of these initial assignments, and the subsequent search enumerates all compatible completions.

Exactly 48 elements have order seven. Their generated subgroups form eight distinct Sylow-seven subgroups. Conjugating these eight subgroups gives an eight-point action; its sign is \(\varepsilon\). The exact fixed-orbit calculation of Step 2 and the independent eight-point permutation calculation agree for **every** automorphism. The complete summary, grouping indistinguishable order-seven classes, is:

| Element order | \(\varepsilon(g)\) | \(|\mathcal S^g|\) | \(\operatorname{tr}(g\mid\widetilde H_6)\) | Number of elements |
|---:|---:|---:|---:|---:|
| 1 | +1 | 8 | 7 | 1 |
| 2 | +1 | 0 | -1 | 21 |
| 2 | -1 | 2 | -1 | 28 |
| 3 | +1 | 2 | 1 | 56 |
| 4 | +1 | 0 | -1 | 42 |
| 6 | -1 | 2 | -1 | 56 |
| 7 | +1 | 1 | 0 | 48 |
| 8 | -1 | 0 | 1 | 84 |

The character on the eight-point permutation module is \(g\mapsto|\mathcal S^g|\); hence that on \(\varepsilon\otimes U\) is \(g\mapsto\varepsilon(g)(|\mathcal S^g|-1)\). The table proves equality with the computed homology character. Maschke's theorem and character uniqueness in characteristic zero give the asserted rational representation isomorphism.

The character inner product with itself is exactly
\[
\frac{1}{336}\left(1\cdot49+21+28+56+42+56+48\cdot0+84\right)=1.
\]
It is consequently irreducible over \(\mathbb C\), and thus absolutely irreducible over \(\mathbb Q\). Restricting to the 168 even-sign elements gives inner product \((49+21+56+42)/168=1\), proving the claim for \(\Gamma^+\).

**4. Quotient rational homology.** For any finite simplicial group action, barycentric subdivision removes inversions and rational averaging identifies the rational homology of the ordinary quotient with the invariant subspace of the original rational homology. The full character average and the \(\Gamma^+\) average are both zero. For a Sylow-seven subgroup \(C\), the identity has trace seven and every other element has trace zero, so \(\dim\widetilde H_6(X;\mathbb Q)^C=(7+6\cdot0)/7=1\). The remaining reduced rational homology groups vanish before taking invariants and therefore after quotienting.

## Verification
The standalone pure-Python file `verify_coxeter_symmetry.py` reconstructs the graph and all faces without external graph libraries, constructs the independent parity-first matching, checks all 1,319,724 oriented incidences and performs the complete topological sort. It then independently exhausts all automorphisms, constructs all eight Sylow-seven subgroups, computes every Lefschetz trace by exact finite deletion recurrence, checks the signed Sylow permutation formula on all 336 elements, and independently re-evaluates oriented fixed faces for eight representative types. Run `python3 verify_coxeter_symmetry.py` in a directory containing this file. The recorded successful output is supplied in `verification_output.txt`; its final marker is `COXETER_SYMMETRY_VERIFY_OK`.

## Relationship to prior work
Barmak's 2010 triangle-free suspension theorem applies to the Coxeter graph but does not identify its homology representation. Dejter's 2010 Coxeter/Klein-graph study establishes structural graph geometry and group relationships, not the representation on an independence complex. Feng and Wang's 2024 Kneser computation treats the complete 35-vertex \(KG(7,3)\), whereas the Coxeter graph is the proper induced 28-vertex subgraph obtained by deleting the seven Fano-line vertices. Their table and Fano-supported six-dimensional cycles do not compute the symmetry of the deleted-vertex complex.

A separately published 2026 calculation of **the same Coxeter independence complex** establishes its ordinary homotopy type \(\bigvee^7 S^6\), which is explicitly excluded from novelty here. Its result does not determine the full 336-element homology character, irreducibility, the Sylow-seven twisted augmentation identification or rational quotient ranks. Known abstract character theory of \(\mathrm{PGL}(2,7)\) likewise does not establish that this particular topological homology representation is the indicated character.

## Limitations
The claim is about one canonical finite graph and rational homology with its full graph-automorphism action. The self-contained exact enumeration supplies a finite proof, not a uniform result for larger graphs. No integral equivariant-module classification, equivariant homotopy equivalence, integral quotient homology or quotient fundamental-group classification is claimed. The closest indexed literature and exact same-object earlier result have been compared, but an equivalent unindexed character calculation cannot be categorically ruled out. No independent external mathematical audit has been performed.

## References
[1] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public 2010-07-02), Theorems 3.4–3.5, https://arxiv.org/pdf/1007.0418.

[2] I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960 (first public 2010-02-09; later versions 2012), Section 3 and graph automorphisms, https://arxiv.org/pdf/1002.1960.

[3] Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1 (first public 2024-04-16), Table 1 and Theorem 8, https://arxiv.org/pdf/2404.10566.

[4] *The Coxeter graph independence complex is \(\bigvee^{7}S^{6}\)*, published mathematical finding, 2026-10-11, identifier `2026/10/11/SCOPE-the-coxeter-graph-independence-complex-is-bigvee-7-s-6--8a1bdfa47e09` (prior nonequivariant result).

[5] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic discrete-Morse theorem).
