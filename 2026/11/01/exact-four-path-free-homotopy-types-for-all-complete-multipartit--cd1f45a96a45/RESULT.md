# Exact four-path-free homotopy types for all complete multipartite graphs

## Finding

For each integer \(r\ge2\) and any positive integers \(n_1,\ldots,n_r\), let \(G=K_{n_1,\ldots,n_r}\) be the complete multipartite graph with parts \(V_i\) of sizes \(n_i\). The four-path-free complex \(\operatorname{PF}_4(G)\) consists of all subsets \(\sigma\) of vertices for which the induced graph \(G[\sigma]\) does not contain a four-vertex path **as a subgraph** (not necessarily an induced path). Then

\[
\operatorname{PF}_4(G)\simeq\bigvee^{B}S^2,
\qquad B=\binom{N-1}{3}-\sum_{i=1}^{r}\left[\binom{n_i-1}{3}+(N-n_i)\binom{n_i-1}{2}\right],\quad N=\sum_{i=1}^r n_i.
\]

The convention is \(\binom ab=0\) when \(b<0\) or \(b>a\); a wedge of zero spheres is a point. In particular, all reduced integral homology vanishes outside degree two, and degree-two homology is free of rank \(B\). For three parts the rank simplifies to
\[
B=abc+ab+ac+bc-2(a+b+c)+2
\]
for \(G=K_{a,b,c}\). Thus \(\operatorname{PF}_4(K_{2,2,2})\simeq\bigvee^{10}S^2\) and \(\operatorname{PF}_4(K_{3,3,3})\simeq\bigvee^{38}S^2\).

## Assumptions and scope

The parts are disjoint and nonempty, and all cross-part edges, but no within-part edges, are present. The forbidden path has exactly four distinct vertices and three successive edges; additional chords are permitted. All assertions hold for every allowed part-size tuple, including singleton parts, and for both small and large total vertex counts. No shellability assumption is made.

## Proof

**1. Classify every face above dimension two.** All subsets of at most three vertices are faces. Let \(\sigma\) contain at least four vertices, and put \(a_i=|\sigma\cap V_i|\). It is a face if and only if there exists an index \(i\) such that \(|\sigma|-a_i\le1\). Indeed, such a set induces either an edgeless graph (zero vertices outside the part) or a star (one outside vertex), neither of which contains a four-vertex path. Conversely, if the vertices cannot all but one be placed in a single part, either there are two vertices in each of two distinct parts, two vertices in one part and one in each of two further parts, or vertices in four distinct parts. In these respective cases the induced graph contains a path with part patterns \(i,j,i,j\), \(i,j,i,k\), or \(i,j,k,l\). This exhausts the ways to select four vertices when no part contains all but at most one of the chosen vertices; hence the face characterization holds. For any face of size at least three satisfying the part condition, its **owner** \(i\) is unique: two distinct parts cannot each contain all but one vertex of a set of size at least three while also containing at least two vertices.

**2. Construct a complete acyclic matching above dimension two.** Choose one distinguished pivot vertex \(x_i\in V_i\) per part. For every face \(\sigma\) with \(|\sigma|\ge3\), owner \(i\), and \(x_i\notin\sigma\), match \(\sigma\) upward to \(\sigma\cup\{x_i\}\). Both are faces; adding a pivot in the owner part preserves the part condition. Any face with at least four vertices has a unique owner and is paired: it is the lower face if it omits the owner pivot, and it is the upper face otherwise (its lower partner removes that pivot and still has at least three vertices in the owner part or, at size four, at least two). Distinct matched pairs cannot overlap, since the owner remains unchanged on adding or removing its pivot.

To prove acyclicity, consider a Forman alternating gradient path at a fixed face dimension: a matched upward move \(\sigma\to\sigma\cup\{x_i\}\) must be followed, if the path continues, by removing a vertex other than \(x_i\) to obtain a different face \(\tau\) of the original dimension. This \(\tau\) retains the pivot \(x_i\). If its size is at least three, it is still owned by \(i\), because at least two owner vertices remain and at most one outside vertex exists. It therefore cannot be a lower member of any matched pair. In dimensions zero or one there are no matched lower faces either. Thus no fixed-dimensional alternating gradient path can continue to a second upward move. By the acyclic matching criterion, no closed gradient path exists, so this is an acyclic discrete Morse matching.

Every unpaired face has cardinality at most three; discrete Morse theory gives a CW homotopy model of dimension at most two. Independently, because the original complex contains every three-vertex subset, it contains the full two-skeleton of the simplex on \(N\) vertices. For \(N\ge3\), every edge loop is filled by triangles, so the original complex is simply connected. For \(N=2\) it is a segment and is contractible. Consequently the two-dimensional CW model is simply connected. Its second homology is free abelian and it has no positive-dimensional homology except possibly in degree two. By Hurewicz, representatives of a basis of its second integral homology induce a homology equivalence from a wedge of two-spheres; the simply connected homological Whitehead theorem makes this a homotopy equivalence.

**3. Count the two-spheres.** All \(N\) vertices and all \(\binom N2\) edges are critical; all triangles are initially present. The matched lower triangles have owner \(i\) and omit \(x_i\). They have either three vertices in \(V_i\setminus\{x_i\}\), giving \(\binom{n_i-1}{3}\) choices, or two there and one outside \(V_i\), giving \((N-n_i)\binom{n_i-1}{2}\) choices. No such triangle is counted twice because the owner is unique. Thus the number \(c_2\) of critical two-cells is
\[
c_2=\binom N3-\sum_i\left[\binom{n_i-1}{3}+(N-n_i)\binom{n_i-1}{2}\right].
\]
The reduced Euler characteristic of the Morse CW model, equal to the rank of its second homology since it is simply connected and two-dimensional, is \(N-\binom N2+c_2-1\). The identity \(N-\binom N2+\binom N3-1=\binom{N-1}{3}\) yields the asserted \(B\). This also proves \(B\ge0\) without relying on the appearance of the formula.

## Verification

The supplied standalone `check_pf4.py` independently constructs forbidden paths by enumerating permutations of four vertices, enumerates all faces, constructs and checks the full directed Hasse matching for cycles, compares the exact Euler characteristic and critical-cell count, and computes all simplicial-chain mod-two Betti numbers. Run `python check_pf4.py` with standard Python 3. For 14 parameter tuples, including \((3,3,3)\), all checks pass. These finite tests corroborate the exact all-parameter proof; they are not an exhaustive proof for unbounded part sizes.

## Relationship to prior work

Deshpande, Goyal, and Sawant [1] prove the homotopy type for complete **bipartite** graphs for all path parameters (Theorem 4.3), and for complete multipartite graphs at the **three-vertex** path parameter (Theorem 4.5). Their Conjecture 4.7 proposes sphere-wedge types for arbitrary path parameter, and Question 4.8 asks for multiplicities. The present result resolves the four-vertex case for **all** multipartite part counts and sizes; the two-part specialization is previously known and is not offered as a novel result. Their non-sequential Cohen–Macaulay theorem includes \(K_{3,3,3}\) at this path parameter, so the new classification is not merely a consequence of shellability. The higher-independence complexes in Deshpande–Singh [2] are different at the four-vertex path parameter: for example, a three-leaf star is permitted in the path-free complex but not in the three-independence complex. Taylan's graph-devoid-complex methods [3] concern principally different graph families.

## Limitations

The theorem concerns exactly four-vertex *subgraph* paths in complete multipartite graphs and determines ordinary homotopy types, not equivariant actions or all larger forbidden path lengths. It relies on standard discrete Morse and Whitehead theorems. No claim of priority beyond the directly compared literature is made, and independent mathematical validation has not been performed.

## References

[1] P. Deshpande, S. Goyal, R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358v1 (first public 2026-07-06), especially Theorems 3.10, 4.3, 4.5, Conjecture 4.7 and Question 4.8. https://arxiv.org/html/2607.05358v1

[2] P. Deshpande, A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, Theorem 3.5. https://arxiv.org/abs/2001.05448

[3] E. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1. https://arxiv.org/abs/1501.06754
