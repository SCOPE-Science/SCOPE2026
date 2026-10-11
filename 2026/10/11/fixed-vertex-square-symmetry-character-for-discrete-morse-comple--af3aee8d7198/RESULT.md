# Fixed-vertex-square symmetry character for discrete Morse complexes of cones over trees

## Finding
Let \(T\) be any finite simple tree with \(n\ge 2\) vertices. Form the graph \(G\) by adjoining one hub \(h\) joined to every vertex of \(T\), and regard \(G\) strictly as a **one-dimensional** simplicial complex (the graph's triangles are *not* filled). The ordinary discrete-Morse complex \(\mathcal M(G)\) has vertices the incident vertex–edge pairs of \(G\), with simplices corresponding to acyclic partial discrete gradient matchings.

Let \(\Gamma=\operatorname{Aut}(T)\) act on \(G\) fixing \(h\). For every \(g\in\Gamma\), write \(f(g)=|\{v\in V(T):gv=v\}|\) and \(\epsilon(g)=\operatorname{sgn}_{V(T)}(g)\). Then

\[
\mathcal M(G)\simeq\bigvee^{n^2}S^{n-1},\qquad
\operatorname{tr}\!\left(g\mid \widetilde H_{n-1}(\mathcal M(G);\mathbb Q)\right)=\epsilon(g)f(g)^2.
\]

Equivalently, if \(U=\mathbb Q[V(T)]\) is the rational permutation representation on the vertices and \(\epsilon\) is their permutation-sign character, then
\[
\widetilde H_{n-1}(\mathcal M(G);\mathbb Q)\cong \epsilon\otimes (U\otimes U)
\]
as rational \(\Gamma\)-representations (an abstract, not a claimed canonical, isomorphism). The **representation character**, rather than merely the previously accessible shellability/homotopy conclusion, is the central result.

## Assumptions and scope
The tree \(T\) is finite, undirected, loopless, connected and has no parallel edges. Its order is \(n\ge2\), with no restriction on degree, diameter or automorphism group. All directed arcs below refer to possible discrete vertex–edge matchings on the bidirected underlying graph, not extra edges of \(G\). A matching at a vertex is represented by an outgoing arrow along its matched edge. A valid Morse matching has at most one outgoing arrow at any vertex and no directed cycle. This convention is isomorphic, by arrow reversal, to the customary directed-forest complex with at most one incoming arrow. Only rational equivariant representation is claimed, while the homotopy statement is integral.

## Proof
**1. Dimension and concentration.** An acyclic directed partial map on \(V(G)\) can have at most \(n\) arrows, since at least one vertex is unmatched. Conversely a spanning tree directed toward \(h\) has \(n\) arrows. After reversing arrows, the bidirected graph has a complete source \(h\). The complete-source shellability theorem for complexes of directed trees (Kozlov; see the explicit theorem and generating-facet discussion in Jojić [2]) implies this complex is pure shellable of dimension \(n-1\). Therefore it is a wedge of \((n-1)\)-spheres, possibly zero in number, and its reduced homology is concentrated in degree \(n-1\), with no torsion.

**2. An equivariant signed forest sum.** Fix \(g\in\Gamma\). A simplex stabilized setwise by \(g\) is a union of complete cyclic \(g\)-orbits of arc-vertices. A selected arc orbit of length \(\ell\) gives \(\ell\) simplicial vertices; in the alternating simplicial trace its ordering sign is \((-1)^{\ell-1}\) and the extra face-size factor is \((-1)^\ell\). Their product is \(-1\). Include the empty simplex in the augmented chain complex. If \(S(g)\) is the sum over invariant acyclic arrow configurations of \((-1)\) to the number of selected arc orbits, then the augmented Hopf–Lefschetz formula, together with step 1, gives
\[
\chi(g)=\operatorname{tr}(g\mid\widetilde H_{n-1})=(-1)^nS(g).
\]

**3. Orbit determinant.** Form a finite directed multigraph \(D_g\) whose vertices are the cyclic orbits of \(g\) on \(V(G)\). For each orbit \(A\), choose a representative \(u\). A directed edge \(A\to B\) is assigned for each neighbor \(w\) of \(u\) in orbit \(B\) for which \(g^{|A|}w=w\), provided \(A\ne B\). Such a choice uniquely extends to an equivariant assignment of one outgoing arrow at every vertex of \(A\). Same-orbit assignments necessarily form a directed cycle, hence are excluded. Each equivariant acyclic matching corresponds to an acyclic partial choice of one outgoing edge from each selected vertex of \(D_g\). With \(L_g\) the outdegree Laplacian (including edge multiplicities), the elementary row expansion
\[
\det(I-L_g)=\sum_{F\text{ acyclic partial choices}}(-1)^{|\operatorname{dom}F|}=S(g)
\]
follows by choosing either the identity row or minus one incidence row for each vertex: an acyclic choice makes those rows triangular with determinant one; a directed cycle makes them linearly dependent. This identity includes the empty choice.

**4. Fixed vertices.** The fixed vertices of a tree automorphism either form a nonempty connected induced subtree \(F\) of order \(f\), or there are no fixed vertices and the automorphism interchanges the endpoints of a central edge. If \(f>0\), the vertex orbits consisting of fixed points (including \(h\)) give exactly the cone graph \(K_1+F\). They cannot map equivariantly to moving orbits; hence \(I-L_g\) is block triangular. The fixed block is
\[
\begin{pmatrix}1-f&\mathbf1^{\mathsf T}\\\mathbf1&-L_F\end{pmatrix}.
\]
The tree matrix-tree theorem says every principal cofactor of \(L_F\) is one, so \(\operatorname{adj}(L_F)=\mathbf1\mathbf1^{\mathsf T}\). Expansion along the hub block gives determinant \((-1)^ff^2\), including \(f=1\).

**5. Moving vertices.** Let \(b\) be the number of nonfixed vertex orbits in \(T\). Every such orbit has exactly one equivariant arrow toward the hub, so subtracting its outdegree Laplacian cancels the \(1\) on its diagonal in \(I-L_g\). The remaining moving block is minus the Dirichlet outdegree Laplacian of the rooted orbit tree \(T/\langle g\rangle\) outside \(F\). Each moving orbit has a unique parent orbit toward \(F\), and this parent arrow is equivariant. Any permitted other edges lead away from \(F\) along the quotient tree. By the directed matrix-tree expansion, the only directed forest from every moving orbit to the deleted fixed subtree takes all parent arrows; its weight is one. Thus the moving-block determinant is \((-1)^b\). Consequently
\[
S(g)=(-1)^{f+b}f^2 \quad (f>0).
\]
If \(f=0\), the unique central edge inverted by \(g\) becomes a self-orbit edge and is excluded. The moving block after hub cancellation has zero row sums, hence determinant zero; therefore \(S(g)=0\). These statements also hold when some moving orbits have different lengths: the orbit construction permits only well-defined equivariant arrows, and each parent arrow is always well-defined.

**6. Character and multiplicity.** The permutation sign of \(g\) on the \(n\) tree vertices is \((-1)^{n-(f+b)}\), since \(f+b\) is the number of all its vertex cycles. Combining steps 2–5 yields
\[
\chi(g)=(-1)^n(-1)^{f+b}f^2=\epsilon(g)f^2,
\]
with the same formula if \(f=0\). At \(g=1\), the trace is \(n^2\), giving the number of top spheres. Finally the permutation character of \(U\) is \(f(g)\), so the character of \(\epsilon\otimes U\otimes U\) is exactly \(\epsilon(g)f(g)^2\). Characters determine rational representations of finite groups up to isomorphism, proving the asserted module classification.

## Verification
Run `python verify_cone_tree.py` with standard Python 3. The verifier constructs every unlabelled simple tree with two through seven vertices using Prüfer sequences and canonical rooted-tree codes, enumerates every automorphism, and independently evaluates the signed invariant-forest sum by enumerating all equivariant partial arrow choices. It checks the character formula on **24 tree isomorphism types and 967 automorphisms**. It also independently constructs complete simplicial complexes and checks their mod-two augmented boundary ranks for the four tree types on at most four vertices. Successful execution reports `VERIFY_OK trees=24 automorphisms=967 homology_cases=4`. This is finite corroboration; the unlimited-order theorem follows from the proof, not from extrapolating the tests.

## Relationship to prior work
Donovan and Scoville [1] define graph Morse complexes and analyze several graph families, including trees and extended stars; their results motivate asking for an equivariant calculation beyond ordinary Betti numbers. Kozlov's complete-source result, in the inspectable presentation and further shellability treatment of Jojić [2], already supplies the essential shellability/homology-concentration input and is **not** claimed as new. Engström [3] studies directed-tree complexes and shellability for acyclic digraphs. The new part is the explicit signed orbit-forest determinant and its closed character formula for all tree automorphisms. The star-tree specialization \(T=K_{1,k}\) with \(k\ge2\) reproduces the narrower triangular-book character \(\operatorname{sgn}(\sigma)(1+f_\sigma)^2\) for page permutations \(\sigma\); that already-obtained special case is not itself claimed as new. These established structural theorems do not themselves state that character, although their stronger descriptions of generating facets are an important potential route to an equivalent formula.

## Limitations
The module statement is over \(\mathbb Q\), not a canonical integral module identification. The homotopy classification uses the cited complete-source shellability theorem, not a newly supplied shelling. No assertion covers cones over graphs containing cycles, graphs regarded as filled two-dimensional clique complexes, or automorphisms moving the hub. No claim of novelty certification is made: a previously unlocated equivalent equivariant computation could exist, especially in the broader Kozlov/Jojić directed-tree literature; the older Kozlov source itself was not fully inspected during this comparison. The computational checks are finite corroboration only, not an infinite proof or independent audit.

## References
[1] C. Donovan and N. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, initial public version 27 July 2022; primary MSC 57Q70.

[2] D. Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475 (2011), Filomat 27 (2013), 1551–1559; see the complete-source shelling and generating-facet results. Also credits D. Kozlov, *Complexes of directed trees*, J. Combin. Theory Ser. A 88 (1999), 112–122.

[3] A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148 (2005).
