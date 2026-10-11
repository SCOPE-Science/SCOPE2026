# Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition

## Finding

For every integer \(m\ge 4\), the ordinary Lovász open-neighborhood complex of the prism over the complete graph, \(G_m=K_m\square K_2\), has the homotopy type

\[
\mathcal N(G_m)\simeq\bigvee^{2}S^{m-2}\vee\bigvee^{m^2-3m+1}S^2.
\]

Here the wedge multiplicities are nonnegative integers. For \(m=4\), both displayed sphere dimensions coincide and the result is \(\bigvee^7 S^2\). For \(m\ge5\), the reduced integral homology is free, of rank \(m^2-3m+1\) in degree \(2\) and of rank \(2\) in degree \(m-2\), and vanishes elsewhere. The entire complex is simply connected. It is pure of dimension \(m-1\) and **not shellable** for every \(m\ge4\).

## Assumptions and scope

A finite simple graph's *open-neighborhood complex* \(\mathcal N(G)\) consists of all subsets of vertices contained in some open graph neighborhood \(N_G(v)=\{w:\{v,w\}\in E(G)\}\). Let \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_m\}\). The graph \(G_m\) has a clique on \(A\), a clique on \(B\), and precisely the cross-layer edges \(\{a_i,b_i\}\) for \(1\le i\le m\). All assertions refer to its ordinary open neighborhoods, not closed neighborhoods; geometric realization is implicit in statements of homotopy type. The parameter range is exactly \(m\in\mathbb Z\), \(m\ge4\).

## Proof

**Step 1 (maximal faces).** From the graph definition,
\[
N(a_i)=(A\setminus\{a_i\})\cup\{b_i\},\qquad
N(b_i)=(B\setminus\{b_i\})\cup\{a_i\}.
\]
Each has \(m\) vertices; these \(2m\) distinct neighborhoods are the facets. Put \(X_A=\bigcup_{i=1}^m\Delta[N(a_i)]\) and \(X_B=\bigcup_{i=1}^m\Delta[N(b_i)]\), where \(\Delta[S]\) is the full simplex on \(S\). Then \(\mathcal N(G_m)=X_A\cup X_B\).

**Step 2 (the two spheres).** Inside \(X_A\), the vertex \(b_i\) occurs in exactly one maximal simplex, \(\Delta[N(a_i)]\), with its link the entire simplex \(\Delta[A\setminus\{a_i\}]\). Elementary simplicial collapses therefore remove every face involving \(b_i\), leaving the face \(A\setminus\{a_i\}\); operations for different \(i\) cannot interfere because their removed faces contain different \(b_i\). After all \(m\) removals, precisely the boundary of the \((m-1)\)-simplex on \(A\) remains. Thus \(X_A\searrow\partial\Delta(A)\cong S^{m-2}\). Symmetrically \(X_B\searrow\partial\Delta(B)\cong S^{m-2}\). As \(m\ge4\), both spaces are simply connected.

**Step 3 (the intersection).** Every simplex of \(X_A\) contains at most one \(B\)-vertex, and every simplex of \(X_B\) contains at most one \(A\)-vertex. Every same-layer edge belongs to exactly one of the two complexes, so \(I=X_A\cap X_B\) is at most one-dimensional. Its vertices are all of \(A\sqcup B\). A cross edge \(\{a_i,b_j\}\) lies in \(X_A\) precisely when \(i\ne j\), and then also lies in \(X_B\) (using the neighborhood of \(b_i\)). Hence
\[
I\cong K_{m,m}\setminus\{\{a_i,b_i\}:1\le i\le m\},
\]
the crown graph. For \(m\ge4\), it is connected, has \(2m\) vertices and \(m(m-1)\) edges, and consequently has cycle rank
\[
\beta_1(I)=m(m-1)-2m+1=m^2-3m+1.
\]
It follows that \(I\simeq\bigvee^{m^2-3m+1}S^1\).

**Step 4 (homotopy pushout).** The inclusions \(I\hookrightarrow X_A\) and \(I\hookrightarrow X_B\) are cofibrations of simplicial subcomplexes. Both maps are null-homotopic: \(I\) is a connected graph and the targets \(X_A\) and \(X_B\) are simply connected. Their pushout is therefore homotopy equivalent to the homotopy pushout of two constant maps from \(I\), which is \(X_A\vee X_B\vee\Sigma I\) (based wedge, with \(I\) connected). Substituting Steps 2 and 3 gives the displayed formula. This is a uniform proof for all \(m\ge4\), not an extrapolation from enumerated cases.

**Step 5 (purity and shellability).** All \(2m\) neighborhoods of Step 1 are distinct facets of size \(m\), so the complex is pure of dimension \(m-1\). The reduced degree-\(2\) integral homology is nonzero, because \(m^2-3m+1>0\) in the stated range. Since \(2<m-1\), the complex cannot be pure shellable: a pure shellable complex is homotopy equivalent to a wedge of spheres only in its top dimension (or is contractible). This proves non-shellability.

## Verification

The standalone finite checker `verify.py` reconstructs the graph adjacency, enumerates all neighborhood faces, and verifies the decomposition \(X_A\cup X_B\) and intersection edge set. It calculates the full reduced simplicial Betti vector over \(\mathbb F_2\) by exact binary boundary-matrix elimination for all \(4\le m\le8\), as well as reduced Euler characteristics. The outputs give \(7\) degree-\(2\) classes for \(m=4\); degree-\(2\)/high-degree ranks \((11,2)\), \((19,2)\), \((29,2)\), \((41,2)\) for \(m=5,6,7,8\). The checker reports `VERIFY_OK`. These finite checks corroborate but do not replace the proof in Steps 1–5. To reproduce, run `python3 verify.py` with the standard Python library.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue classify **cut complexes** \(\Delta_k(G_m)\) for this same clique-prism graph, with \(\Delta_k(G_m)\simeq\bigvee^{\binom{m-1}{k-1}}S^{2m-k-2}\) for \(2\le k\le m\) (their Theorem 7.18). A cut complex is not the open-neighborhood complex, and this result does not determine the displayed mixed-dimensional wedge. Adams, Shukla and Singh compute **closed-neighborhood/Čech** complexes for hypercube graphs and explicitly distinguish these from Lovász open neighborhoods (their Section 4). Matsushita (Example 3.5) classifies the **closed** neighborhood complex of \(K_m\square K_2\) as \(\bigvee^{(m-1)^2}S^2\); this is not equivalent to the present open-neighborhood result, which already has different degree-\(2\) rank for \(m=4\), and has higher-dimensional homology for \(m\ge5\). Shukla's open-neighborhood classifications treat maximum-degree-at-most-three graphs or four-regular circulants, not an unbounded family of clique prisms. No covering open-neighborhood classification was identified in the inspected sources.

## Limitations

The theorem concerns only the ordinary open-neighborhood complex of \(K_m\square K_2\) for \(m\ge4\); it makes no claim for \(m\le3\), for other Cartesian factors, for closed neighborhoods, or for stronger equivariant structures. Searches cannot exclude an unindexed equivalent published theorem. The finite checker tests only \(4\le m\le8\); the infinite assertion rests on the complete homotopy-pushout argument, and no independent audit has been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), Definition 7.16 and Theorem 7.18. https://arxiv.org/html/2304.13675v2
2. H. Adams, S. Shukla, and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first public 2022-12-12), Section 4 and Theorem 4.1. https://arxiv.org/html/2212.05871v2
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first public 2018-02-13), Theorems 2.1–2.6. https://arxiv.org/html/1802.04526v2
4. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (first public 2025-11-16), Example 3.5. https://arxiv.org/html/2511.12608v2
