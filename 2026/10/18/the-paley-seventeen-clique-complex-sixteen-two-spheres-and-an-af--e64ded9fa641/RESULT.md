# The Paley-seventeen clique complex: sixteen two-spheres and an affine homology module

## Finding
Let \(P_{17}\) be the Paley graph on \(\mathbb F_{17}\), in which distinct \(u,v\) are adjacent exactly when \(v-u\) is a nonzero square. Write \(K=\operatorname{Cl}(P_{17})\) for its flag (clique) complex, and let
\[
A=\{x\mapsto ax+b:\ a\in(\mathbb F_{17}^{\times})^2,\ b\in\mathbb F_{17}\}
\]
be its natural affine automorphism group, of order \(136\). Then:

1. **Integral homotopy type.** There is a (nonequivariant) homotopy equivalence
   \[
   K\simeq\bigvee^{16}S^2.
   \]
2. **Complete affine rational representation.** As \(\mathbb Q[A]\)-modules,
   \[
   \widetilde H_2(K;\mathbb Q)\cong
   \mathbb Q[\mathbb F_{17}]/\mathbb Q\mathbf 1,
   \]
   the sixteen-dimensional augmentation representation of the affine action on seventeen vertices. Its character is \(16\) on the identity, \(-1\) on each nonidentity translation, and \(0\) on every affine transformation with nontrivial multiplier.
3. **Every affine-subgroup geometric quotient.** Let \(T=\{x\mapsto x+b:b\in\mathbb F_{17}\}\). For every subgroup \(H\le A\), the only potentially nonzero reduced rational homology group of \(|K|/H\) is degree two, and
   \[
   \dim_{\mathbb Q}\widetilde H_2(|K|/H;\mathbb Q)
   =\begin{cases}
     16/|H|,&H\cap T=\{1\},\\
     0,&H\cap T\ne\{1\}.
   \end{cases}
   \]
   In particular, a quotient is rationally acyclic if and only if its subgroup contains a nonidentity translation; the translation-free subgroup orders are \(1,2,4,8\), yielding ranks \(16,8,4,2\), respectively.

## Assumptions and scope
The graph has exactly the labeled vertex set \(\{0,1,\ldots,16\}\), with arithmetic modulo \(17\). The nonzero quadratic residues are
\[
Q=\{1,2,4,8,9,13,15,16\}.
\]
There are no additional edges, simplex identifications or coefficient twists. Homotopy means ordinary topological homotopy of the geometric realization. The affine statement concerns rational singular homology; no integral identification of the affine lattice and no equivariant wedge decomposition is asserted. In the quotient formula \(H\) is *any* subgroup of the specified order-\(136\) affine group; geometric, not fixed-vertex, quotients are used.

## Proof
**1. The entire flag complex has dimension two.** Each graph vertex has eight neighbors, giving \(68\) graph edges. The affine group is edge-transitive: translating the first endpoint to zero and multiplying a quadratic-residue difference by its inverse takes any edge to \(\{0,1\}\). This edge has precisely the three common neighbors \(2,9,16\), so there are \(68\) triangles. The graph induced on the eight neighbors \(Q\) of zero has the twelve edges
\[
\{1,2\},\{1,9\},\{1,16\},\{2,4\},\{2,15\},\{4,8\},\{4,13\},\{8,9\},\{8,16\},\{9,13\},\{13,15\},\{15,16\}.
\]
It is the three-dimensional cube graph and hence triangle-free. Translation symmetry shows that no vertex belongs to a four-clique; consequently there are no four-cliques. Thus \(K\) has exactly \(17\) vertices, \(68\) edges, \(68\) triangles and no higher-dimensional faces.

**2. Exact acyclic Morse certificate.** Root a spanning tree of the one-skeleton at zero and choose its breadth-first parents by increasing vertex labels. Match each nonroot vertex to its parent edge (sixteen pairs). Initially declare the sixteen tree edges resolved. Repeatedly choose the lexicographically first triangle with *exactly one unresolved edge*, pair it with that edge, and declare the edge resolved. The fully specified deterministic procedure terminates with all remaining \(52\) edges paired to \(52\) distinct triangles. Its explicit parent map and triangle pair list are contained in `paley17_matching_certificate.json`.

The supplied independent verifier reconstructs the simplicial complex directly from quadratic residues; checks both members of every pair, face containment, uniqueness and exhaustiveness; constructs the complete directed Hasse graph (\(340\) face-cover relations, orienting matched relations upward and others downward); and performs a complete directed-acyclicity test. The only unmatched simplices are one vertex and sixteen triangles. The acyclic-matching theorem for finite simplicial complexes therefore produces a CW model with one zero-cell, no one-cells and sixteen two-cells. Every attaching map has target a point, so the CW model is precisely \(\bigvee^{16}S^2\). This proves the integral homotopy equivalence, including the absence of hidden fundamental-group or torsion obstructions.

**3. An affine-equivariant midpoint correspondence.** As \(2\in Q\), every edge \(\{u,v\}\) determines a triangle
\[
\Phi(\{u,v\})=\{u,v,(u+v)/2\}.
\]
A three-element subset of \(\mathbb F_{17}\) cannot have two different members serving as the midpoint of the other two: two such equations would force three times the difference of two distinct vertices to vanish. Since \(17\ne3\), this is impossible. The midpoint map is therefore injective, and the matching face counts of \(68\) edges and \(68\) triangles make it a bijection. It commutes with every affine transformation.

The only nonidentity element stabilizing the unoriented base edge \(\{0,1\}\) is \(x\mapsto1-x\). It reverses orientation on that edge; on the corresponding triangle \(\{0,1,9\}\), it exchanges the endpoints and fixes the midpoint, again reversing orientation. Because the edge and triangle sets are each one transitive affine orbit with the same signed stabilizer action, their oriented rational chain permutation modules are isomorphic:
\[
C_1(K;\mathbb Q)\cong C_2(K;\mathbb Q)
\quad\text{as }\mathbb Q[A]\text{-modules}.
\]
Taking the alternating sum in the representation ring and using the already-proved homology concentration gives
\[
[\widetilde H_2(K;\mathbb Q)]
=[C_0(K;\mathbb Q)]-[\mathbf1].
\]
Maschke semisimplicity identifies the actual rational module with the quotient of the vertex permutation module by its constant line. This establishes the asserted complete character without relying on finite character fitting.

**4. All subgroup quotients.** After barycentric subdivision, the finite action is cellular without inversions. Over \(\mathbb Q\), averaging over a finite group is exact, so
\[
\widetilde H_j(|K|/H;\mathbb Q)
\cong\widetilde H_j(K;\mathbb Q)^H.
\]
An affine permutation of seventeen vertices fixes all \(17\) vertices at the identity, none for a nonzero translation, and exactly one whenever its multiplier is not one. Consequently the augmentation character takes values \(16,-1,0\) in those three cases. By character averaging, if \(H\cap T=\{1\}\), its fixed dimension is \(16/|H|\); otherwise, since the prime-order group \(T\) is contained in \(H\), the sum of the seventeen translation character values is zero, and all remaining character values also vanish. Every subgroup avoiding \(T\) injects into \(A/T\cong C_8\), so its order divides eight. The quotient formula follows.

## Verification
The package includes `paley17_matching_certificate.json`, `paley17_verifier.py` and `paley17_verifier_output.txt`. From a directory containing these files, run:

```
python3 paley17_verifier.py paley17_matching_certificate.json
```

The verifier uses only the Python standard library. It reconstructs all \(153\) nonempty simplices, checks the full \(68\)-pair acyclic matching and its \(340\) cover relations, verifies the midpoint bijection and its affine equivariance for all \(136\) affine maps, and independently computes signed fixed-simplex Lefschetz traces for every affine element. The recorded execution ends with `PASS`. The output does not replace the proofs of the Morse and rational-transfer theorems; it certifies their finite input data.

## Relationship to prior work
Cioabă and Mim (arXiv:2606.27328, first public version June 25, 2026) study first homology of clique complexes of strongly regular graphs. Their conference-graph vanishing theorem applies to sufficiently large graphs (they give a threshold of \(256\) vertices), whereas the Paley graph considered here has \(17\) vertices. Their results do not give this exact homotopy type, affine representation or orbit-space homology.

The Paley graph \(P_{17}\) is a classical extremal \(K_4\)-free and co-\(K_4\)-free Ramsey graph, and its degree, clique counts and automorphism group are standard graph data. Those facts are inputs, not claimed discoveries. In particular, mere knowledge of the face vector \((17,68,68)\) and Euler characteristic \(17\) does not imply simple connectivity or a sphere-wedge homotopy type. As \(P_{17}\) is self-complementary, its independence complex is isomorphic to this clique complex, so that synonymous formulation is included in the originality comparison. The separately studied Lovász neighborhood complex of this same graph is a different simplicial complex and its homotopy type does not imply the present theorem.

## Limitations
This is a theorem for the single natural seventeen-vertex Ramsey witness, not an all-orders Paley theorem. The resulting wedge equivalence is nonequivariant; the representation identification is rational only. The quotient result is confined to reduced rational homology, not fundamental groups, integral homology, stable homotopy or equivariant homotopy types. Completeness of literature indexing is not asserted; an equivalent unindexed computation remains possible.

## References
1. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (first submitted 2026-06-25), especially Section 6 on conference graphs. https://arxiv.org/abs/2606.27328
2. E. W. Weisstein, *Paley Graph*, MathWorld, Paley graph definition, symmetry information and the seventeen-vertex Ramsey example. https://mathworld.wolfram.com/PaleyGraph.html
3. R. Forman, *A User's Guide to Discrete Morse Theory*, Séminaire Lotharingien de Combinatoire 48 (2002), Article B48c; standard acyclic-matching theorem.
