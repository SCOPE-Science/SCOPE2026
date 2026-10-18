# Two-independence complexes of crown graphs and their full rational symmetry characters

## Finding
For each integer \(n\geq3\), let \(C_n\) be the **crown graph** with vertices \(a_i,b_i\), indexed by \(i\in\{0,\ldots,n-1\}\), and edges \(a_i b_j\) precisely when \(i\ne j\). Let \(X_n=\operatorname{Ind}_2(C_n)\) be the simplicial complex of vertex subsets whose induced connected components have at most two vertices. Then
\[
\boxed{X_n\simeq\bigvee^{\binom{n-1}{2}}S^2.}
\]
The equivalence is integral. Hence \(\widetilde H_2(X_n;\mathbb Z)\cong\mathbb Z^{\binom{n-1}{2}}\), with all other reduced integral homology groups zero, and \(\pi_1(X_n)=0\).

For the natural action of \(\operatorname{Aut}(C_n)\cong S_n\times C_2\), let \(V_n=\ker(\mathbb Q^n\xrightarrow{\mathrm{sum}}\mathbb Q)\), equipped with its standard permutation action of \(S_n\), and let \(\varepsilon\) denote the sign representation of the part-exchanging \(C_2\). Then the **rational**, not asserted integral, equivariant refinement is
\[
\boxed{\widetilde H_2(X_n;\mathbb Q)\cong (\bigwedge^2 V_n)\boxtimes\varepsilon.}
\]
Explicitly, for \(g=(\sigma,s)\), with \(s=0\) or \(1\), if \(f\) is the number of fixed points and \(t\) the number of 2-cycles of \(\sigma\), its homology character is
\[
\operatorname{tr}(g\mid\widetilde H_2)=(-1)^s\left(\frac{f^2-3f+2}{2}-t\right).
\]
The first cases \(n=3,4,5,6\) respectively have one, three, six, and ten 2-spheres. In particular, the eight-vertex cube is the \(n=4\) crown graph and has three 2-spheres in this **higher** independence complex.

## Assumptions and scope
All graphs are finite, simple, undirected. The parameter \(n\) ranges over every integer at least three, with all indices simultaneously permuted by \(S_n\), and global exchange \(a_i\leftrightarrow b_i\) generating \(C_2\). A face is an induced disjoint union of isolated vertices and isolated edges; for a bipartite graph this is equivalent to induced maximum degree at most one. Homotopy equivalence is non-equivariant; the equivariant statement is solely a rational homology representation isomorphism.

## Proof
**1. Exhaustive face description.** Write any face as \(A\sqcup B\), where \(A\subseteq\{a_i\}\) and \(B\subseteq\{b_i\}\). The degree of \(a_i\in A\) in the induced subgraph equals \(|B|-\mathbf1_{b_i\in B}\), and similarly the degree of \(b_j\in B\) equals \(|A|-\mathbf1_{a_j\in A}\). Each must be at most one. Therefore every pure \(A\)- or pure \(B\)-subset is a face. Every mixed face is exactly one of: \((|A|,|B|)=(1,1)\), unrestricted; \((2,1)\), where the sole \(B\)-index belongs to the \(A\)-index pair; \((1,2)\), symmetrically; or \((2,2)\), where the index pairs on both sides coincide. There are no larger mixed faces. Consequently the mixed-face counts in dimensions one, two, three are respectively \(n^2\), \(2n(n-1)\), and \(\binom n2\).

**2. Complete discrete-Morse matching.** Use all nonempty faces. Process the vertex pivots in the fixed order \(a_0,a_1,\ldots,a_{n-1},b_0\). At each stage, match every currently unpaired face \(F\) not containing the pivot with \(F\cup\{v\}\) if both remain unpaired; remove all these disjoint covering pairs. The empty face is never matched. The construction uses only incidences in the preceding exhaustive description.

Fix the selected \(B\)-subset. If it is empty, its nonempty \(A\)-fiber is the nonempty face poset of an \((n-1)\)-simplex: the \(a_0\) toggle removes every such face except \(\{a_0\}\). If \(B=\{b_j\}\), its allowed \(A\)-subsets are \(\varnothing\), all singletons, and pairs containing \(a_j\): this is a cone with apex \(a_j\). If \(B=\{b_i,b_j\}\), its allowed \(A\)-subsets are exactly all subsets of \(\{a_i,a_j\}\), again a cone. Within a fixed \(B\)-fiber, the first \(A\)-stage toggles are compatible with toggling the apex: a toggle by a vertex different from the apex pairs apex-containing and apex-avoiding faces in parallel, so the remaining fiber is still closed under the apex toggle. At the apex stage all remaining faces in either of these fibers are therefore paired. If \(|B|\geq3\), the sole allowed \(A\)-subset is empty, so the only faces left after all \(A\)-stages are \(\{a_0\}\) and pure \(B\)-faces of cardinality at least three.

The final \(b_0\)-toggle pairs every such pure \(B\)-face except the triples \(\{b_0,b_i,b_j\}\) with \(1\leq i<j<n\). Indeed, a face of size at least three lacking \(b_0\) is paired with its extension by \(b_0\), while a face containing \(b_0\) of size at least four is paired with its deletion of \(b_0\); for a triple containing \(b_0\), its deletion has cardinality two and was paired earlier. Exactly one critical zero-cell and \(\binom{n-1}{2}\) critical two-cells remain.

**3. Acyclicity and integral homotopy.** This sequential element matching is acyclic. For completeness, orient matched Hasse edges upward and all other covering edges downward. If a directed cycle existed, choose the earliest pivot stage represented by one of its upward matched edges. Along the cycle this pivot is added at least once; it cannot be removed: a downward edge deleting that pivot connects two faces both still unpaired before that earliest stage (because their cycle matching stages are no earlier), and hence those two faces would themselves have been matched by the pivot at that stage, contradicting downward orientation. Thus no directed cycle exists. The finite acyclic matching defines a Morse CW model with exactly one zero-cell and \(\binom{n-1}{2}\) two-cells and no other cells. Every attaching map of a two-cell into the unique zero-cell is constant, giving precisely the wedge of two-spheres claimed. This is an integral homotopy equivalence, not an inference from field homology.

**4. Full rational symmetry character.** The automorphism group for \(n\geq3\) is \(S_n\times C_2\), acting by simultaneous permutations of the index pairs and exchange of both sides. For a permutation \(\sigma\), put \(f=|\operatorname{Fix}(\sigma)|\) and let \(t\) be the number of its 2-cycles. The reduced simplicial Lefschetz number equals the trace on \(\widetilde H_2\), since all other reduced rational homology is zero. For \((\sigma,0)\), the two pure-part simplices contribute \(2\) to the unreduced alternating trace. Fixed mixed edges contribute \(-f^2\); fixed mixed triangles contribute \(+2f(f-1)\); fixed mixed tetrahedra contribute \(-\binom f2-t\), with positive orientation on both kinds of tetrahedral index orbits. Subtracting the augmentation trace \(1\) gives
\[
1-f^2+2f(f-1)-\binom f2-t=\frac{f^2-3f+2}{2}-t.
\]
For \((\sigma,1)\), no pure-part face is fixed, no mixed triangle is fixed, the fixed mixed edges are the \(f+2t\) ordered pairs whose indices are a fixed point or a transposition, with reversed orientation; the fixed mixed tetrahedra correspond to \(\binom f2+t\) invariant unordered index pairs, with positive orientation. Accounting for simplex dimension and subtracting augmentation yields
\[
(f+2t)-(\binom f2+t)-1=-\left(\frac{f^2-3f+2}{2}-t\right).
\]
Finally \(\chi_{V_n}(\sigma)=f-1\), while \(\chi_{V_n}(\sigma^2)=f+2t-1\). The exterior-square character identity gives \(\chi_{\wedge^2V_n}(\sigma)=((f-1)^2-(f+2t-1))/2\), which is the first formula. Rational representations of this finite group are determined by their character (equivalently after complexification), proving the stated isomorphism.

## Verification
The accompanying standalone Python program enumerates all vertex subsets from the original graph-edge definition, independently reconstructs the structural face list, checks every covering pair and acyclicity by complete topological sorting, and calculates mod-two boundary ranks. These tests pass for every \(3\leq n\leq8\), involving up to \(714\) faces and \(2608\) covering relations. Signed simplex-Lefschetz traces were independently compared with the character formula for **all** \(12+48+240+1440=1740\) automorphisms of the cases \(3\leq n\leq6\). These finite computations check the proof; the all-\(n\) theorem follows instead from Steps 1–4.

Run `python3 verify_crown.py` (Python standard library only) and compare its exact output to `verification_output.json`. No external input, hidden data or network access is needed.

## Relationship to prior work
Deshpande and Singh (arXiv:2001.05448, especially their Theorems 3.5 and 4.6) compute higher-independence homotopy types of complete multipartite graphs and cycles. The crown at \(n=3\) is a six-cycle, hence that boundary case is covered. For \(n\geq4\), the crown is not complete multipartite (its cross-part matched pairs are nonedges) and is not a cycle; it also is not in their fully whiskered, path, or perfect-tree families. Sawant (arXiv:2605.25150, first public May 24, 2026) proves vertex decomposability for trees, unlike these cyclic graphs. The chordal-graph results of Abdelmalek and coauthors do not apply: the crown has an induced six-cycle at \(n=3\) and induced four-cycles for \(n\geq4\). The forest-filtration treatment of other graph families in Carnero Bravo (arXiv:2307.13271) does not yield this exact crown classification. Thus the contribution is an all-parameter homotopy type together with a uniform **rational** symmetry module; the previously known six-cycle special case is not claimed as new.

## Limitations
This theorem covers only crown graphs with \(n\geq3\). Neither an equivariant homotopy equivalence nor an integral equivariant module decomposition is asserted. Finite checks do not constitute an infinite-parameter proof: that proof is the explicit acyclic matching and Lefschetz enumeration above. The relevant literature was compared by mathematical implication, but an unindexed equivalent publication cannot be excluded. No independent scientific audit has been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150 (first publicly posted 2026-05-24), https://arxiv.org/html/2605.25150v1.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first publicly posted 2020-01-15), https://arxiv.org/html/2001.05448v2.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (2021), https://arxiv.org/abs/2106.10863.
4. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (2023), https://arxiv.org/abs/2307.13271.
