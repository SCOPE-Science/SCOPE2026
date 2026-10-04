# Two-point sequence \(b\)-spectrum of crown graphs
## Finding
Let \(n\ge 3\), and let \(\operatorname{Cr}_n\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\). Let \(S=(2,2,2,\ldots)\). Under the sequence \(b\)-coloring definition of Jakovac and Lang, the \(S\)-spectrum is exactly
\[
\operatorname{Spec}_S(\operatorname{Cr}_n)=\{2,n\}.
\]
More strongly, up to permutation of color names, there is exactly one realizing coloring with two colors, namely the bipartition coloring \(A\mid B\), and exactly one realizing coloring with \(n\) colors, namely the matched-pair coloring with color classes \(\{a_i,b_i\}\) for \(1\le i\le n\). There are no realizing colorings with any other number of colors. Consequently,
\[
\chi_S(\operatorname{Cr}_n)=2,\qquad \phi_S(\operatorname{Cr}_n)=n,
\]
and sequence \(b\)-spectra can have arbitrarily long internal gaps even on connected regular bipartite graphs.
## Assumptions and scope
Graphs are finite and simple. The crown graph is connected for \(n\ge3\) and is \((n-1)\)-regular. A proper coloring realizes the length-\(k\) prefix \((2,\ldots,2)\) when every one of its \(k\) color classes contains at least two color-dominating vertices, where a vertex is color-dominating when its closed neighborhood contains every color used by the coloring. The \(S\)-spectrum is the set of all such color counts \(k\).
## Proof
Every independent set in \(\operatorname{Cr}_n\) is of exactly one of the following forms: a subset of \(A\), a subset of \(B\), or one matched pair \(\{a_i,b_i\}\). Indeed, if an independent set contains vertices from both sides, a cross pair can be nonadjacent only when the indices agree, and no third vertex can be added without creating an edge.

Consider a proper coloring in which every color class contains at least two color-dominating vertices. Call a class \(A\)-pure if it is contained in \(A\), \(B\)-pure if it is contained in \(B\), and paired if it is some \(\{a_i,b_i\}\).

Suppose an \(A\)-pure class \(C\) exists and a paired class \(P_i=\{a_i,b_i\}\) also exists. The vertex \(a_i\) has no neighbor in \(C\), so \(a_i\) is not color-dominating. Thus \(P_i\) contains at most one color-dominating vertex, contradicting the requirement of two. Hence an \(A\)-pure class excludes every paired class. By symmetry, so does a \(B\)-pure class.

If no paired class occurs, all classes are pure. There cannot be two distinct \(A\)-pure classes, because no vertex of one is adjacent to any vertex of the other, so neither class could contain a color-dominating vertex. Thus there is exactly one \(A\)-pure class and, symmetrically, exactly one \(B\)-pure class. Since all vertices must be colored, these classes are precisely \(A\) and \(B\), giving exactly two colors. Every vertex is color-dominating in this coloring, so the prefix \((2,2)\) is realized.

If a paired class occurs, the preceding paragraph shows that no pure class can occur. Therefore every class is a matched pair. Covering all \(2n\) vertices then forces exactly the \(n\) classes \(\{a_i,b_i\}\). In this coloring, for every \(j\ne i\), the vertex \(a_i\) sees color \(j\) through \(b_j\), and \(b_i\) sees color \(j\) through \(a_j\); each also sees its own color in its closed neighborhood. Hence both vertices of every class are color-dominating, so the length-\(n\) prefix is realized.

These two cases exhaust all proper colorings satisfying the two-CDV requirement, proving that the spectrum is exactly \(\{2,n\}\) and that the two realizing colorings are unique up to color permutation.
## Verification
The accompanying `verify.py` reconstructs \(\operatorname{Cr}_n\) from its adjacency rule, enumerates every set partition of the vertex set for \(3\le n\le5\), filters the partitions by properness, computes color-dominating vertices directly from closed neighborhoods, and records the color counts for which every class has at least two such vertices. It checks both the spectrum and the claimed uniqueness/type of the realizing partitions. The exhaustive replay reports 120318 set partitions, 4520 proper partitions, and exactly six realizing partitions across \(n=3,4,5\), two for each value of \(n\).

This finite enumeration is a stress test only. The theorem for all \(n\ge3\) is established by the structural proof above.
## Relationship to prior work
Jakovac and Lang introduced sequence \(b\)-colorings and the associated \(S\)-spectrum. Their paper studies cycles, regular graphs under girth hypotheses, and the sequence \((2,1,1,\ldots)\), and explicitly asks which sets of positive integers can occur as \(S\)-spectra. The inspected full text contains no occurrence of “crown” or “multipartite.” The present result supplies an explicit infinite family with a two-point spectrum \(\{2,n\}\), so the missing interval between the minimum and maximum can grow without bound.

Classical \(b\)-spectrum work concerns the weaker condition of at least one color-dominating vertex per color class. That theory does not imply the two-CDV spectrum determined here. Searches for crown-graph \(b\)-coloring and \(b\)-spectrum results located work on related graphs and classical \(b\)-coloring, but no statement giving this sequence spectrum.
## Limitations
The result concerns only the constant sequence \(S=(2,2,2,\ldots)\) and crown graphs \(\operatorname{Cr}_n\). It does not classify spectra for other sequences or for arbitrary bipartite graphs. The literature search cannot exclude an unindexed or differently phrased crown-graph result that explicitly tracks multiple color-dominating vertices per color class, although no such source was located and the sequence framework itself is recent.
## References
1. Marko Jakovac and Michael S. Lang, “Sequence b-colorings in graphs,” arXiv:2609.08484v1, 2026.
2. Allen Ibiapina and Ana Silva, “b-continuity and Partial Grundy Coloring of graphs with large girth,” arXiv:1908.00674, 2019.
