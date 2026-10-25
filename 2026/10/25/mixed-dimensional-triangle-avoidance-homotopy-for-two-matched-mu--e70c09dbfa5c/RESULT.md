# Mixed-dimensional triangle-avoidance homotopy for two matched multipartite parts

## Finding
For integers \(k,l\ge2\) and \(s\ge0\), construct \(G_{k,l,s}\) on disjoint sets \(A,B,C\), with \(|A|=2k\), \(|B|=2l\), and \(|C|=s\). Partition \(A\) and \(B\) separately into \(k\) and \(l\) pairs. Make every pair of vertices belonging to different sets among \(A,B\) and the individual singleton parts \(\{c\}\) for \(c\in C\) adjacent; the only additional edges are the designated pair edges within \(A\) and \(B\). Let \(\mathsf{CF}_3(G)\) denote the simplicial complex of all vertex subsets inducing no triangle. Then the integral homotopy type is
\[
\mathsf{CF}_3(G_{k,l,s})\simeq S^{k+l-1}\vee\bigvee^{s+1}S^k\vee\bigvee^{s+1}S^l\vee\bigvee^{\binom{s+1}{2}}S^1.
\]
When \(k=l\), the two middle wedge terms give \(2(s+1)\) spheres of the same dimension. A zero-fold wedge denotes no summand. This formula holds without restrictions on the parity of \(s\) and is an integral statement about homotopy, not only a field-homology calculation.

## Assumptions and scope
All graphs are finite, simple, and undirected. The pairs internal to \(A\) and \(B\) form perfect matchings, and there are no other edges within either of these two parts. Every vertex in each part is adjacent to every vertex in any other part. Each member of \(C\) is a separate singleton part; hence \(C\) is a clique. The assertion concerns all integers \(k,l\ge2\) and \(s\ge0\) and only triangle-free *vertex-subset* complexes; it is not a theorem about ordinary edge matching complexes or cut complexes.

Let \(L_A\) and \(L_B\) be the independence complexes of the internal matching graphs on \(A\) and \(B\), respectively. These are the joins of \(k\), respectively \(l\), copies of \(S^0\), and therefore \(L_A\cong S^{k-1}\) and \(L_B\cong S^{l-1}\) as polyhedra. The notation \(\Delta(A)\) means the full simplex on \(A\); a join of complexes is denoted by \(*\).

## Proof
**Face classification.** A triangle-free face meeting both \(A\) and \(B\) cannot contain a matched edge entirely in either part: that edge and any vertex of the other part would form a triangle. Thus the part of the complex on \(A\cup B\) is exactly
\[
K_0=\Delta(A)\cup\Delta(B)\cup(L_A*L_B).
\]
A triangle-free face containing a vertex \(c\in C\) and at least one vertex of \(A\cup B\) can meet only one of \(A,B\), cannot contain a complete matching pair of that part, and cannot contain another vertex from \(C\). Faces contained in \(C\) have at most two vertices. Consequently the entire complex \(K\) is obtained from \(K_0\) by adjoining, for each \(c\in C\), the two cones \(c*L_A\) and \(c*L_B\), and finally each edge \(\{c,d\}\) between two distinct vertices of \(C\). There are no other faces.

**Initial two-part homotopy type.** Put \(J=L_A*L_B\). The join of the two cross-polytope boundaries is \(J\cong S^{k+l-1}\). Both inclusions \(L_A\hookrightarrow J\) and \(L_B\hookrightarrow J\) are null-homotopic: a fixed vertex in the opposite part cones either inclusion within \(J\). The three-piece union describing \(K_0\) attaches the contractible simplices \(\Delta(A)\) and \(\Delta(B)\) to \(J\) along \(L_A\) and \(L_B\), respectively. Since all inclusions are subcomplex cofibrations, homotopy invariance of the pushout replaces each contractible simplex by the cone on its attaching subcomplex. Attaching a cone along a null-homotopic map splits off the suspension of its source. Both attachments therefore split, giving
\[
K_0\simeq S^{k+l-1}\vee S^k\vee S^l.
\]
Here the second attachment remains null because its inclusion is already null within the unchanged subcomplex \(J\).

**Cones over the two parts.** In \(K_0\), both inclusions of \(L_A\) and \(L_B\) are null-homotopic because they each bound the full simplex on the corresponding part. For a new vertex \(c\), the intersection of \((c*L_A)\cup(c*L_B)\) with the previously assembled complex is the *disjoint* union \(L_A\sqcup L_B\). The two cones have the same apex and their union is the cone \(c*(L_A\sqcup L_B)\). The attachment map of this disjoint union is null-homotopic, since each component is null-homotopic separately. Both spheres \(L_A,L_B\) are nonempty and path-connected, because \(k,l\ge2\). For a path-connected target \(X\), coning off a disjoint union of two path-connected spaces by a null-homotopic map gives
\[
X\cup_{L_A\sqcup L_B}C(L_A\sqcup L_B)\simeq X\vee\Sigma L_A\vee\Sigma L_B\vee S^1.
\]
This standard splitting follows by replacing the attaching map with a constant map to a chosen point and using a path connecting the two component basepoints; equivalently, the reduced suspension of a disconnected union has one extra circle. The null-homotopies remain valid as additional cones are adjoined because \(\Delta(A),\Delta(B)\) remain subcomplexes. Thus adding all \(s\) external vertices produces \(s\) additional copies each of \(S^k,S^l,S^1\), in addition to the three summands of \(K_0\).

**Edges among external vertices.** At this stage all external vertices lie in the same connected component as \(K_0\). Every edge joining two of them is attached along its two endpoints, without any higher simplex containing that edge: such a simplex would already contain a triangle. Attaching an interval to an existing path-connected CW complex at its endpoints adds a wedge summand \(S^1\). There are exactly \(\binom s2\) such edges. The total number of circle summands is \(s+\binom s2=\binom{s+1}2\), while the higher summands are unchanged, proving the displayed equivalence. All homotopy pushout and cell-attachment arguments are integral and valid for every stated parameter.

## Verification
The accompanying self-contained Python program `verify.py` directly builds graph edges and the complete list of triangular forbidden triples, enumerates *all* nonempty admissible vertex subsets for each tested parameter set, constructs the complete simplicial boundary matrices over \(\mathbb F_2\) using bitset columns, and computes their ranks by exact elimination. It verifies that the full mod-two reduced Betti vectors agree with the theorem for 14 parameter configurations with \(k,l\in\{2,3\}\), \(0\le s\le3\), and at most 13 vertices. The run processed a total of 4,855 nonempty faces and returned `VERIFY_OK`. This finite verification is supplemental: the proof of the infinite integral homotopy statement is the decomposition above, not the enumeration.

Reproduce in Python 3 with `python verify.py`; there are no third-party dependencies. The exact recorded terminal output is included as `verification_output.txt`.

## Relationship to prior work
Ghosh and Selvaraja's 2026 treatment introduces and studies \(t\)-clique-free complexes, emphasizing shellability and clique attachments for particular chordal graph classes; its inspected theorems do not classify homotopy for the two-matched-part nonchordal graphs here. A previously available general formula for triangle-free complexes of \(K_m\vee H\) assumes that \(H\) is *triangle-free*; it does not imply the present result, because the two matched parts with all cross edges already contain triangles. The extra sphere \(S^{k+l-1}\) records that previously excluded interaction. Standard results on joins, simplicial mapping cones, and homotopy pushouts are used in the proof, but the displayed family classification is not a rephrasing of their general qualitative statements. Terminology such as "matching complex" and "three-cut complex" refers to different complexes and does not furnish an equivalent calculation.

## Limitations
No result is asserted for arbitrary internal graphs in place of the two perfect matchings, for three or more internally matched parts, or for \(t\)-clique-free complexes with \(t\ne3\). This is not a claim of uniqueness among all published results: indexing gaps or unexamined literature could contain earlier equivalent statements. The executable check computes mod-two homology for small instances, not integral homotopy of the entire infinite family. The integral conclusion rests on the given geometric argument.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623 (first public version 2026-02-10), https://arxiv.org/abs/2602.09623.
2. A. Hatcher, *Algebraic Topology*, 2002, sections on homotopy pushouts, cofibrations, and CW complexes, https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
