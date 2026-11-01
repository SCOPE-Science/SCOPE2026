# Three six-spheres and an irreducible full-symmetry module in the Möbius–Kantor two-independence complex

## Finding
Let \(M=GP(8,3)\) be the Möbius–Kantor graph with vertices \(u_i,v_i\), where indices belong to \(\mathbb Z/8\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\) for every index \(i\). The first higher-independence complex \(X=\operatorname{Ind}_2(M)\) has the exact integral homotopy type
\[
X\simeq S^6\vee S^6\vee S^6.
\]
Under its full automorphism group \(G=\operatorname{Aut}(M)\), of order \(96\), its only nonzero reduced rational homology is the absolutely irreducible three-dimensional module \(\widetilde H_6(X;\mathbb Q)\). The kernel of this action is the central involution \(z(u_i)=u_{i+4}\), \(z(v_i)=v_{i+4}\).

For a permutation \(g\) of the sixteen vertices, let \(\mathcal O(g)\) be the set of its vertex cycles. The full character is given for every \(g\in G\) by the finite, unambiguous formula
\[
\chi(g)=-1+\sum_{\substack{\varnothing\ne J\subseteq\mathcal O(g)\\\bigcup J\in X}}(-1)^{|J|+1}.
\]
The union in the condition is the union of vertices in the chosen cycles. This formula specifies values even when two automorphisms share a vertex cycle type but have different homological traces. No nonzero rational class is fixed by all of \(G\); hence \(\widetilde H_*(X/G;\mathbb Q)=0\).

## Assumptions and scope
A face of \(X\) is a vertex subset \(S\subseteq V(M)\) for which every connected component of the induced graph \(M[S]\) contains at most two vertices. Equivalently, every vertex of \(M[S]\) has induced degree at most one. The dimension of a nonempty face is its cardinality minus one. Faces are oriented in increasing vertex order, with \(u_0,\ldots,u_7\) numbered \(0,\ldots,7\) and \(v_0,\ldots,v_7\) numbered \(8,\ldots,15\). All topological homotopy and integral homology assertions concern the geometric realization of this finite abstract simplicial complex; no assertion is made for other generalized Petersen graphs.

## Proof
**Complete finite construction.** Enumerating the subsets of the sixteen vertices and retaining exactly those of induced maximum degree at most one gives \(6812\) nonempty faces, with face vector by dimension \(0\) through \(7\)
\[
(16,120,512,1324,2064,1840,816,120).
\]
The verifier independently checks the component-size definition against the induced-degree predicate on all \(65536\) vertex subsets.

**Acyclic Morse matching.** Starting with every face, including the empty face, process the vertices in the displayed order. At stage \(i\), pair every still-unpaired face not containing vertex \(i\) with its union with \(\{i\}\), whenever that union is also still unpaired. Break the unique pair involving the empty face, giving one critical vertex. Exactly \(3400\) nonempty pairs remain; the critical cells consist of one vertex, one four-cell, four five-cells, and six six-cells. The eleven positive-dimensional critical face bitmasks are, grouped by dimension:

- Dimension four: `818`.
- Dimension five: `8916, 10898, 17304, 17714`.
- Dimension six: `15048, 18344, 21924, 23714, 43684, 58008`.

The complete directed Hasse diagram has \(6812\) vertices and \(35104\) incidences. Every unmatched incidence is oriented downward and every matched incidence upward. An exhaustive topological sort visits all \(6812\) vertices, proving there is no directed cycle. Forman's discrete Morse theorem therefore produces a CW complex with precisely the listed critical cells.

**Integral attaching degrees.** In the listed critical-cell orders, the integer Morse boundary from degree five to degree four is
\[
\partial^{\mathrm M}_5=\begin{pmatrix}-1&0&-1&-1\end{pmatrix}.
\]
The degree-six to degree-five boundary is
\[
\partial^{\mathrm M}_6=\begin{pmatrix}
-1&0&0&0&1&-1\\
-1&0&-1&-1&1&0\\
0&1&0&0&0&1\\
1&-1&0&0&-1&0
\end{pmatrix}.
\]
These are obtained by the complete signed gradient-path formula: each matched lower face is replaced by the negative of the other oriented boundary faces of its paired upper face, divided by the unit incidence coefficient, iterated to critical faces. The verified determinantal divisors are \((1)\) for \(\partial^{\mathrm M}_5\) and \((1,1,1,0)\) for \(\partial^{\mathrm M}_6\); also \(\partial^{\mathrm M}_5\partial^{\mathrm M}_6=0\). Thus the nonzero Smith invariants are a single unit in degree five and three units in degree six, with \(\widetilde H_6(X;\mathbb Z)\cong\mathbb Z^3\) and all other reduced integral homology zero.

**Homotopy upgrade.** The Morse CW complex has no positive cells below dimension four. Its degree-five attaching maps to the unique four-sphere are classified by their integer degrees. The primitive unit in \(\partial^{\mathrm M}_5\) allows cancellation of one four-cell against one five-cell (after a change of five-cell basis). The resulting CW complex has three five-cells and six six-cells. Its six-cell attaching maps are classified by \(\pi_5(\bigvee^3S^5)\cong\mathbb Z^3\), with no Whitehead-product ambiguity in this dimension. The three unit Smith factors of the remaining degree-six attaching matrix cancel all three five-cells against three six-cells. The remaining three six-cells attach to the basepoint, proving \(X\simeq\bigvee^3 S^6\).

**Automorphism character.** Exhaustive adjacency-preserving backtracking gives exactly \(96\) permutations of the sixteen vertices. On each invariant oriented simplex, the signed simplicial Lefschetz contribution is \((-1)^{\dim\sigma}\) times the sign of the induced vertex permutation. If an invariant simplex is a union of \(k\) vertex cycles, this sign equals \((-1)^{k+1}\). Subtracting the empty-face contribution gives the displayed reduced Lefschetz formula. Since reduced rational homology is concentrated in even degree six, this Lefschetz number equals \(\chi(g)\).

For transparency, the pairs (vertex-cycle type, trace) and their multiplicities among the \(96\) automorphisms are:

| Vertex-cycle type | Trace | Count |
|---|---:|---:|
| \(1^{16}\) | 3 | 1 |
| \(1^4 2^6\) | -1 | 12 |
| \(1^4 3^4\) | 0 | 8 |
| \(2^8\) | 1 | 18 |
| \(2^8\) | 3 | 1 |
| \(2^2 6^2\) | 0 | 8 |
| \(4^4\) | -3 | 2 |
| \(4^4\) | -1 | 6 |
| \(4\,12\) | 0 | 16 |
| \(8^2\) | -1 | 12 |
| \(8^2\) | 1 | 12 |

The verifier computes each trace in two independent ways: cycle-union enumeration and direct fixed-face signed permutations. The results agree on all \(96\) elements. They satisfy \(\sum_{g\in G}\chi(g)^2=96\), so the character has inner product one with itself and is irreducible over \(\mathbb C\), hence absolutely irreducible over \(\mathbb Q\). Exactly two elements have trace three: the identity and the simultaneous half-rotation \(z\). An average-invariant positive-definite inner product makes every finite-order matrix orthogonal, so trace three forces the identity action. The representation kernel is precisely \(\{1,z\}\), and the verified character sum \(\sum_{g\in G}\chi(g)=0\) rules out invariant rational homology. After barycentric subdivision the finite group action is admissible; rational averaging identifies quotient homology with invariants. Therefore the quotient is rationally acyclic.

## Verification
Run `python3 verify_mk.py` using Python 3 and only its standard library. The exact output is included in `verify_mk.out`. The code checks the graph and face constructions in two ways; the entire matching's acyclicity; signed Morse matrices and all determinantal divisors; independent original-boundary ranks over \(\mathbb F_2\); exhaustive automorphisms; signed Lefschetz calculations by two methods; character norm and kernel. These checks constitute an executable finite proof certificate for the computations; the topological inferences also use the stated mathematical theorems.

## Relationship to prior work
Salvetti's foundational work introduced generalized independence complexes in relation to Artin groups. Deshpande and Singh's homotopy classification treats complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees. Deshpande, Shukla, and Singh establish general connectivity estimates and a sphere-wedge theorem for chordal graphs. The Möbius–Kantor graph is cubic, has girth six, and is neither chordal nor one of those classified families. Their published statements do not imply its exact integral homotopy type or the three-dimensional character of all graph automorphisms.

Earlier computations on the same graph's **ordinary** independence complex and matching complex are about distinct simplicial complexes; neither is a special-case proof of this result. The explicit representation theorem is not implied by knowing the rank of integral homology. Searches for generalized Petersen graph aliases and higher-independence statements identified no covering published calculation. This is a best-knowledge originality comparison, not a proof of publication priority.

## Limitations
The result concerns this one sixteen-vertex graph and the parameter two. It does not classify higher parameters, other generalized Petersen graphs, integral representation lattices, or the integral homology or homotopy type of the symmetry quotient. The 2016 foundational chapter was available in abstract and bibliographic form but not in full; a requested institutional copy could not be accessed. Equivalent unindexed work remains possible. The computation is independently reproducible from the supplied code but has not received an independent mathematical audit.

## References
1. M. Salvetti, *Some Combinatorial Constructions and Relations with Artin Groups*, Springer INdAM Series, DOI: 10.1007/978-3-319-20155-9_22 (public bibliographic date 2016-01-25).
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first posted 2020-01-15).
3. P. Deshpande, S. Shukla, and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775 (first posted 2020-01-19).
4. G. Paolini and M. Salvetti, *Weighted sheaves and homology of Artin groups*, Algebraic & Geometric Topology 18 (2018), 3943–4000, DOI: 10.2140/agt.2018.18.3943.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
6. H. S. M. Coxeter, *Self-dual configurations and regular graphs*, Bulletin of the American Mathematical Society 56 (1950), 413–455.
