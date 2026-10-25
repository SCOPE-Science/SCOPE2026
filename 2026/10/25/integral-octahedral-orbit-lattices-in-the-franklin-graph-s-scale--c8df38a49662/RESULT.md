# Integral octahedral orbit lattices in the Franklin graph's scale-two Rips complex

## Finding
Let \(F\) be the twelve-vertex Franklin graph specified below, with shortest-path metric, and let
\[K=\operatorname{VR}_{\le2}(V(F),d_F).\]
Then \(H_2(K;\mathbb Z)\cong\mathbb Z^4\). Among the \(924\) six-vertex subsets, exactly \(20\) induce an octahedral two-sphere, and precisely these \(20\) subsets carry nonzero second homology on six vertices. All twenty sphere classes are primitive. Under the full \(48\)-element automorphism group of \(F\), the spheres split into orbits of sizes \(8\) and \(12\). The eight-orbit generates **all** integral second homology; the twelve-orbit generates a **primitive rank-three subgroup**, with quotient \(\mathbb Z\). In particular, the two geometrically natural orbits have different integral spanning power, despite every individual sphere being an essential minimum-support cycle.

## Assumptions and scope
Use vertex labels \(0,\dots,11\), with edges \(\{i,i+1\}\) modulo \(12\), together with \(\{i,i+5\}\) for even \(i\) and \(\{i,i-5\}\) for odd \(i\), interpreting labels modulo \(12\) and taking undirected distinct edges. This is the Franklin graph, isomorphic to the standard \(\operatorname{LCF}(12,[-5,-3,3,5]^3)\) model. Distances count graph edges, and a simplex of \(K\) is a vertex subset with **every** pair at distance at most \(2\). No claim is made about the geometric realization of a continuously sampled metric graph. All homology is ordinary simplicial homology with integral coefficients.

For a six-element set \(W\), call its induced Rips complex octahedral if the **nonedges** of its induced one-skeleton form exactly three disjoint pairs. Writing these pairs \((a_1,b_1),(a_2,b_2),(a_3,b_3)\) in increasing lexicographic order, orient its fundamental chain as the simplicial join \(([b_1]-[a_1])*([b_2]-[a_2])*([b_3]-[a_3])\), taking signs from the increasing global vertex order. Its class is \(z_W\).

## Proof
**1. Minimality and the twenty supports.** A flag complex with nonzero second homology over a field needs at least six vertices. Indeed, restrict to a vertex-minimal subcomplex with a nonzero class. The deletion–star Mayer–Vietoris sequence injects that class into first homology of each vertex link. A flag complex with nonzero first homology needs at least four vertices, with equality forcing an induced four-cycle. Each vertex also has at least one nonneighbor (otherwise the whole complex is a cone). Thus there are at least \(1+4+1=6\) vertices. In the equality case every vertex has one nonneighbor and a four-cycle link; the six-vertex one-skeleton is the octahedral graph \(K_{2,2,2}\). Integral torsion would also give nonzero homology over some prime field, so the same lower bound and equality classification apply to nonzero integral classes. For this particular graph an exhaustive, uniquely indexed check of all \(\binom{12}{6}=924\) sets finds exactly twenty nonedge-perfect-matchings. Their signed octahedral chains have zero boundary; step 3 below proves that every one maps to a nonzero primitive global class.

**2. The complete integral kernel.** Enumerating all cliques of the graph-distance-two graph produces the nonempty face vector
\[(c_0,c_1,c_2,c_3,c_4,c_5)=(12,48,76,45,12,2).\]
With increasing oriented vertices the second and third simplicial boundary maps have rank at least \(37\) and \(35\), respectively, modulo \(101\). The file `verify_franklin.py` deterministically chooses \(35\) third-boundary columns with indices
`[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,34,35,40,42,43]`
(in lexicographic tetrahedron order). It appends the signed sphere chains on supports
\[\begin{gathered}
(0,1,2,3,4,5),\quad(0,1,2,3,10,11),\\
(0,1,2,5,6,7),\quad(0,1,4,5,8,9).
\end{gathered}\]
These \(39\) integral two-cycles have a \(39\)-row minor of determinant \(-1\), with row indices listed in `verification_output.txt` and recomputed in the verifier. Every one of the \(45\) third-boundary columns is **exactly** an integral combination of the first \(35\), with zero coordinate in the last four cycle directions. Thus the third-boundary rank is exactly \(35\). The unit minor makes the \(39\)-generator subgroup primitive in the integral two-chain lattice, while the modular second-boundary lower bound implies that the full second-cycle lattice has rank at most \(76-37=39\). Hence the listed \(39\) cycles equal the whole integral kernel of the second boundary. Quotienting by the \(35\) independent third boundaries gives \(H_2(K;\mathbb Z)=\mathbb Z^4\) with the four displayed octahedral classes as an integral basis. No inference from modular rank alone is used to prove freeness or saturation.

**3. All sphere classes and their two symmetry orbits.** The verifier solves each of the twenty signed sphere chains in this integral basis, using the determinant-one minor and checking the complete \(76\)-coordinate chain equality, not merely a truncated minor. All twenty coordinates are primitive (their entries have greatest common divisor one). The graph automorphism enumeration has exactly \(48\) elements. Its action on six-subsets gives the orbit of size \(8\), represented by \((0,1,2,3,4,5)\), and the orbit of size \(12\), represented by \((0,1,2,5,6,7)\). The integral coordinate matrices for the two orbits have nonzero Smith factors respectively
\[(1,1,1,1)\qquad\text{and}\qquad(1,1,1).\]
The first orbit therefore spans all \(\mathbb Z^4\); the second is a primitive rank-three sublattice. In the four-cycle basis of step 2, the primitive functional
\[\phi(c_1,c_2,c_3,c_4)=-c_1-c_2+c_4\]
annihilates all twelve classes from the second orbit, while its value on each of the eight classes from the first orbit is \(+1\) or \(-1\). This proves the asserted quotient and the geometric orbit distinction.

## Verification
Run `python verify_franklin.py` after installing dependencies from `requirements.txt`. The checker reconstructs graph distances and all clique faces, checks the oriented boundary-of-boundary identity, modular boundary ranks, a genuine integral unit minor, exact integral expansions of **all** third boundaries and **all** octahedral cycles, full orbit enumeration and Smith forms, and all induced mod-two second homology groups on at most six vertices. The successful run is recorded in `verification_output.txt`. The finite enumeration is exhaustive because all \(2^{12}\) subsets and all simplices have canonical finite encodings; it does **not** purport to establish a general infinite-family theorem.

## Relationship to prior work
Adamaszek and Adams, *The Vietoris–Rips complexes of a circle* (arXiv:1503.03669, first public version 2015-03-12), develop circle/cyclic-graph Rips homotopy theory and the convention used here, but their theorems concern circle samples and cyclic graphs, not the Franklin graph's scale-two octahedral orbit lattices. Their later paper *On Vietoris–Rips complexes of hypercube graphs* (arXiv:2103.01040) treats binary hypercube graphs, not this twelve-vertex graph. Publicly indexed results on the Franklin graph's **matching complex** concern a different simplicial complex on its eighteen edges. Results on scale-two Rips complexes of other twelve-vertex graphs do not imply an integral octahedral orbit decomposition for \(F\). The observed equality \(\operatorname{VR}_{\le2}(F)=\operatorname{Ind}(H)\), where \(H\) is the distance-three graph and \(H\cong F\), is accounted for explicitly; the independence-complex reformulation is not ignored in the comparison.

## Limitations
This is a specific finite twelve-point metric computation with exact mathematical certificates, not a claim about larger graph families or higher homotopy groups. Its full homotopy type is not asserted. Exhaustive searches and available primary comparisons cannot exclude equivalent unpublished, unindexed, or inaccessible results. The main contribution is the **sharp integral geometric generator-orbit distinction**, rather than the standalone rank of second homology.

## References
1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, initial public submission 2015-03-12; https://arxiv.org/abs/1503.03669 .
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040; https://arxiv.org/abs/2103.01040 .
3. Standard Franklin graph labels (LCF notation), Maple GraphTheory SpecialGraphs documentation; https://de.maplesoft.com/support/help/maple/view.aspx?path=GraphTheory%2FSpecialGraphs%2FLCFGraph .
