# Exact partial-isomorphism extension spectrum of the seven-point AGL1(7) hypergraph

## Finding

Let \(M\) be the finite \(3\)-uniform hypergraph from Example 5.2 of Assari--Hosseinzadeh--Macpherson. Its vertex set is \(\mathbb F_7=\{0,1,2,3,4,5,6\}\), and its fourteen edges are
\[
013,026,023,045,015,046,124,235,346,156,134,245,356,126.
\]
The source obtains this edge set as one of the two \(\mathrm{AGL}_1(7)\)-orbits on triples and proves that the resulting hypergraph is set-homogeneous but not homogeneous.

The complete arity-by-arity extension spectrum is sharper:
\[
\boxed{M\text{ is }t\text{-homogeneous}\iff t\in\{1,2,5,6,7\}.}
\]
Moreover
\[
\boxed{\operatorname{Aut}(M)=\operatorname{AGL}_1(7),\qquad |\operatorname{Aut}(M)|=42.}
\]
At the two failing arities, the exact extension proportions are
\[
\begin{array}{c|c|c|c|c}
t&\text{induced type}&\#\text{ subsets}&|\operatorname{Aut}(M[U])|&\text{extendible fraction}\\ \hline
3&\text{edge}&14&6&1/2\\
3&\text{nonedge}&21&6&1/3\\
4&\text{one edge}&14&6&1/2\\
4&\text{two edges}&21&4&1/2
\end{array}
\]
Thus nonhomogeneity is not monotone in the size of the partial isomorphism: it occurs at sizes \(3\) and \(4\), but every isomorphism between induced \(5\)-sets or induced \(6\)-sets extends.

## Assumptions and scope

The statement concerns only the explicit seven-vertex hypergraph in Example 5.2, not the countably infinite hypergraphs \(M_3,M_4,M_6,N_3\) studied elsewhere in the same paper. Here \(t\)-homogeneous has the source's meaning: every isomorphism between induced substructures of size \(t\) extends to a global automorphism. The result is about induced subhypergraphs.

The primary source supplies the edge list, the \(\mathrm{AGL}_1(7)\)-orbit sizes on triples and four-sets, transitivity on five- and six-sets, and set-homogeneity. The equality \(\operatorname{Aut}(M)=\operatorname{AGL}_1(7)\) and the full extension spectrum are established here by exact finite analysis.

## Proof

Write \(G=\operatorname{AGL}_1(7)\), acting by \(x\mapsto ax+b\) with \(a\in\mathbb F_7^*\) and \(b\in\mathbb F_7\). The source gives \(|G|=42\), two triple orbits of sizes \(14\) and \(21\), two four-set orbits (their complements), and one orbit each on five- and six-sets. Every affine map preserves the displayed edge set, so \(G\leq\operatorname{Aut}(M)\). An exact check of all \(7!=5040\) permutations finds precisely these \(42\) edge-preserving permutations. Hence
\[
\operatorname{Aut}(M)=G.
\]
This finite equality is independently replayed in the verification section.

For a set-homogeneous structure, the source records the following criterion: a \(t\)-set-homogeneous structure is \(t\)-homogeneous exactly when, for every \(t\)-set \(U\), the permutation group induced on \(U\) by its setwise stabilizer is the full automorphism group of the induced structure \(M[U]\). We therefore only have to compare two small finite groups for each induced type.

For every \(|U|\ge2\), the pointwise stabilizer \(G_{(U)}\) is trivial, because an affine map is determined by the images of two distinct points. Consequently the induced stabilizer on \(U\) has order \(|G_U|=42/|U^G|\).

For triples, an edge orbit has size \(14\), so its induced stabilizer has order \(3\); a nonedge orbit has size \(21\), so its induced stabilizer has order \(2\). Every one-edge or zero-edge three-vertex hypergraph has automorphism group \(S_3\), of order \(6\). Therefore the proportions of extendible isomorphisms are respectively \(3/6=1/2\) and \(2/6=1/3\).

For four-sets, the one-edge orbit has size \(14\) and the two-edge orbit has size \(21\). A one-edge four-vertex hypergraph has automorphism group \(S_3\) on its edge while fixing the isolated point, so has order \(6\). In the two-edge type the two triples share a two-point intersection; one may independently swap the shared pair and the two private vertices, giving automorphism group of order \(4\). The stabilizer images have orders \(3\) and \(2\), respectively. Hence both types have extension fraction \(1/2\).

There is one five-set orbit and one six-set orbit. Thus their stabilizers have orders \(42/21=2\) and \(42/7=6\). For the representative five-set \(\{0,1,2,3,4\}\), whose edges are \(013,023,124,134\), direct inspection gives exactly two induced automorphisms: the identity and \((0\ 4)(1\ 3)\). For the representative six-set \(\{0,1,2,3,4,5\}\), direct inspection gives exactly six induced automorphisms. Hence in both arities the stabilizer image is already the entire induced automorphism group, so every isomorphism extends.

At arity \(2\), sharp two-transitivity of \(\mathrm{AGL}_1(7)\) extends every isomorphism of two-point induced structures; arity \(1\) follows from transitivity. At arity \(7\), an isomorphism \(M\to M\) is itself a global automorphism. This proves the stated spectrum.

For a direct global census, there are exactly \(8912\) isomorphisms between equal-size induced subhypergraphs, of which \(5090\) extend. Broken down by induced type, the exact pairs (all isomorphisms, extendible isomorphisms) are
\[
\begin{array}{c|c|r|r}
t&\text{type}&\text{all}&\text{extendible}\\ \hline
0&\text{unique}&1&1\\
1&\text{unique}&49&49\\
2&\text{unique}&882&882\\
3&\text{edge}&1176&588\\
3&\text{nonedge}&2646&882\\
4&\text{one edge}&1176&588\\
4&\text{two edges}&1764&882\\
5&\text{unique}&882&882\\
6&\text{unique}&294&294\\
7&\text{unique}&42&42.
\end{array}
\]

## Verification

The exact replay enumerates all \(42\) affine maps, all \(5040\) permutations of the seven vertices, every induced subset, and every bijection between equal-size subsets. It checks edge preservation, identifies all partial isomorphisms, tests extension against the recovered global automorphism group, and reproduces every entry of the table above. The replay terminates with

`VERIFY_OK 154786 exact assertions`

and reports `TOTAL_PARTIAL_ISOMORPHISMS 8912` and `TOTAL_EXTENDIBLE 5090`.

## Relationship to prior work

Assari--Hosseinzadeh--Macpherson construct this exact seven-vertex hypergraph and prove it is set-homogeneous but not homogeneous. They state the two triple orbits, the two four-set orbits, and transitivity on five- and six-sets. Their proof of nonhomogeneity uses the classification of finite homogeneous \(3\)-hypergraphs: the example does not occur in that classification. The paper also states the stabilizer criterion for \(t\)-homogeneity.

The result here resolves the finer question left open by that qualitative nonhomogeneity statement: at exactly which substructure sizes does extension fail, and by how much? The answer is the nonconsecutive spectrum \(1,2,5,6,7\), with exact extension fractions at the two bad sizes. Targeted searches for the finite example under `AGL1(7)`, `AGL_1(7)`, set-homogeneity, partial-isomorphism extension, and \(t\)-homogeneity located the primary paper but no previously stated extension-spectrum table or the claim that failure occurs exactly at \(3\) and \(4\).

## Limitations

The originality claim is deliberately narrow. The underlying seven-point hypergraph, its set-homogeneity, its orbit decomposition, and its qualitative failure of homogeneity are published results. The new contribution is the exact extension spectrum, the identification of the full automorphism group from the explicit edge set, and the extension proportions. Because the derivation is short once the finite example is isolated, an uncatalogued folklore calculation remains the main originality risk.

No independent audit has been performed. The computational verification is exhaustive for this finite object, but the literature search cannot exclude every unpublished calculation.

## References

1. Amir Assari, Narges Hosseinzadeh, Dugald Macpherson, “Set-homogeneous hypergraphs,” *Journal of the London Mathematical Society* 108 (2023), 1852–1885. arXiv:2202.09613. DOI: 10.1112/jlms.12796.
