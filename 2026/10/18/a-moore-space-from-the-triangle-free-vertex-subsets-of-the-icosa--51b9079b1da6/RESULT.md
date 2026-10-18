# A Moore space from the triangle-free vertex subsets of the icosahedral graph

## Finding
Let \(I\) be the graph of the regular icosahedron, with twelve vertices and thirty edges. Let \(\operatorname{CF}_3(I)\) be the simplicial complex whose faces are those vertex subsets \(W\subseteq V(I)\) for which the induced graph \(I[W]\) has no three-clique. Then
\[
\operatorname{CF}_3(I)\simeq M(\mathbb Z/2,4)
:=S^4\cup_{\deg(2)}e^5
\simeq\Sigma^3\mathbb{RP}^2.
\]
In particular, its sole nonzero reduced integral homology group is \(\widetilde H_4(\operatorname{CF}_3(I);\mathbb Z)\cong\mathbb Z/2\). The complex is neither a wedge of spheres nor shellable. The integral torsion is essential: all reduced rational homology vanishes.

## Assumptions and scope
The convention for \(\operatorname{CF}_3\) forbids *all* triangles (three-cliques) among the chosen vertices, rather than forbidding connected three-vertex sets, independent triples, or matching edges. It is a downward-closed simplicial complex. We fix a labeling of the icosahedral graph with vertex set \(\{0,1,\ldots,11\}\), specified exactly by the thirty undirected edges in `ico_cf3_verify.py`. This labeling is solely for reproducibility; the conclusion is invariant under graph isomorphism. Every vertex has five neighbors, each inducing a five-cycle, so the graph is the standard icosahedral graph. Its complete set of forbidden three-faces consists of its twenty triangular faces.

There are precisely \(1,048\) faces including the empty simplex, with nonempty face vector in dimensions zero through five
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,200,345,312,112).
\]
All counts below are exhaustive finite counts; no asymptotic or probabilistic inference is involved.

## Proof
For a face \(F\), encode its vertices in a twelve-bit mask. Generate every mask and retain it precisely when it contains none of the twenty forbidden triangles. This gives the full complex and the face vector above, not a selected subcomplex.

Construct a partial matching on the augmented face poset, starting with all \(1,048\) masks. In the order
\[
5,8,7,9,2,4,3,11,1,10,6,0,
\]
visit each pivot \(v\). Among faces still unpaired at that stage, pair each \(F\) not containing \(v\) with \(F\cup\{v\}\) when both are still available, then permanently remove that pair. The checker constructs all \(523\) pairs, checks that each pair is a genuine face-cover relation, and enumerates the entire directed Hasse graph obtained by reversing its matched cover arrows. A topological sort visits all \(1,048\) vertices of this directed graph. Therefore the matching is acyclic (Forman's condition), not merely maximal. The only two unpaired masks are \(213\), a four-simplex, and \(3147\), a five-simplex. The empty face is paired with the singleton \(\{5\}\); deleting that augmented pair supplies one unmatched vertex in the ordinary face-poset matching. Thus a CW model of the complex has precisely one cell each in dimensions \(0\), \(4\), and \(5\).

It remains essential to compute the integral attachment, rather than infer it from finite-field ranks. Orient each simplex by increasing vertex label. Let \(c_4\) denote the critical four-simplex (mask \(213\)). For every four-simplex \(F\), define its reduction coefficient \(R(F)\) by recursive integer elimination along the acyclic matching: \(R(c_4)=1\); \(R(F)=0\) if \(F\) is neither critical nor the lower member of a four-to-five matching pair; and, when \((F,B)\) is such a pair,
\[
R(F)=-\frac{1}{[B:F]}
\sum_{F'\subset B,\,\dim F'=4,\,F'\ne F}[B:F']R(F'),
\]
where \([B:F]\in\{+1,-1\}\) is the ordinary signed simplicial incidence. Acyclicity ensures this recursion terminates, and each division is exact because the pivot incidence is a unit. For the critical five-simplex \(c_5\) (mask \(3147\)), the complete integer computation returns
\[
\sum_{F\subset c_5,\,\dim F=4}[c_5:F]R(F)=-2.
\]
The checker implements this recurrence and confirms the value exactly. It is the signed algebraic discrete-Morse boundary from the unique five-cell to the unique four-cell, so the cellular attaching degree has absolute value two.

The four-skeleton of the resulting CW model consists of a single four-sphere with a disjoint zero-cell identified as its base point. The five-cell is attached by a map \(S^4\to S^4\) of degree \(\pm2\). Since \(\pi_4(S^4)\cong\mathbb Z\) classifies these maps by degree, the homotopy type is the four-dimensional mod-two Moore space \(M(\mathbb Z/2,4)\). Its reduced homology follows from the chain complex \(0\to\mathbb Z\xrightarrow{\pm2}\mathbb Z\to0\). Its reduced integral torsion precludes any wedge-of-spheres type, and the pure complex cannot be shellable, since pure shellable complexes have torsion-free integral homology.

## Verification
Run `python3 ico_cf3_verify.py` using Python 3 and its standard library; the script is embedded with this result. It reconstructs the graph, all twenty triangle constraints, the complete complex, every matching cover, the directed matching Hasse diagram, the exact signed Morse coefficient, and all full simplicial boundary maps over both \(\mathbb F_2\) and \(\mathbb F_3\). The expected output begins `PASS: 20 triangles`, continues `PASS: 523 acyclic pairs`, and ends `Moore homotopy M(Z/2,4)`. The independent finite-field consistency checks give reduced Betti numbers one in degrees four and five over \(\mathbb F_2\), and no nonzero reduced Betti numbers over \(\mathbb F_3\). Finite-field evidence alone would not prove the integral attaching degree; the exact signed recurrence above provides that proof.

## Relationship to prior work
Ghosh and Selvaraja [1] introduce and study higher clique-free complexes of graphs, focusing on shellability criteria under graph-theoretic hypotheses; their structural results do not classify the triangle-free vertex-set complex of the nonchordal icosahedral graph. Their earlier paper [2] concerns higher independence complexes, defined by bounds on sizes of induced connected components rather than the absence of three-cliques, so these constructions are different. Cut-complex results on the icosahedral graph also concern another simplicial object: its ordinary three-cut complex is built from complements of *disconnected* three-element subsets, not the triangle-avoiding subsets considered here.

There is a useful precise duality: the Alexander dual of \(\operatorname{CF}_3(I)\) is the **total three-cut complex of the complement graph** \(\overline I\), because the minimal nonfaces of the former are exactly triangles of \(I\), equivalently independent three-element sets of \(\overline I\). This explains the appropriate alternative description without confusing it with the ordinary three-cut complex of \(I\). The classification above is not a consequence of a homotopy classification of that different ordinary cut complex.

## Limitations
This theorem concerns the finite twelve-vertex icosahedral graph and the parameter-three clique-free construction only. It does not classify general triangulation graphs, all Platonic graphs, larger clique-free parameters, or equivariant homology. The exact finite matching is a computer-assisted exhaustive proof with a standalone checker, not a closed symbolic formula. Published and indexed-source comparisons cannot exclude every unindexed or inaccessible equivalent proof; the claim of literature noncoverage is restricted to sources inspected. Independent scientific validation has not been performed.

## References
[1] Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623, first posted 2026-02-10.

[2] Arka Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, first posted 2025-05-10.

[3] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (2023); see also *Total Cut Complexes of Graphs*, arXiv:2209.13503 (2022).
