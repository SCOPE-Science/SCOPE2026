# Exact optimal perfect-coalition partitions of a disjoint matching

## Finding
For every integer \(n\ge2\), let \(M_n=nK_2\) be the disjoint union of \(n\) **distinguishable** edges, whose \(2n\) endpoints are individually labeled. A perfect-coalition partition is a partition into nonempty classes in which each class either is a one-vertex dominating set or has another class with which it forms a perfect coalition (definitions below). Then the maximum number of classes is exactly four.

The number \(A_n\) of **unlabeled four-class partitions** attaining this maximum is
\[
\boxed{A_n=2^n\bigl(\tfrac14 S(n,2)+3S(n,3)+3S(n,4)\bigr),}
\]
where \(S(n,j)\) is a Stirling number of the second kind, with \(S(n,j)=0\) for \(j>n\).

The partner graph of every maximum partition is isomorphic to exactly one of \(C_4,P_4,2K_2\). The numbers with these three respective partner graphs are
\[
\boxed{A_n(C_4)=2^{n-2}S(n,2),\quad A_n(P_4)=3\cdot2^nS(n,3),\quad A_n(2K_2)=3\cdot2^nS(n,4).}
\]
In particular \(A_2=1\), \(A_3=30\), \(A_4=364\), and \(A_5=3480\). Every graph type listed above is realized for \(n\ge4\); at \(n=2\) only \(C_4\) occurs, and at \(n=3\) only \(C_4,P_4\) occur.

The structural upper bound and the abstract list of three possible optimal partner graphs can also be obtained from existing general results on transversal coalitions in two-uniform hypergraphs. The finding here is the **exact matching-specific realization criterion and complete enumerative refinement**, not a claim to have first identified those three possible partner graphs in general.

## Assumptions and scope
Graphs are finite, simple, and undirected. A subset \(D\) of vertices is *dominating* if every vertex outside \(D\) has a neighbor in \(D\), and *perfect dominating* if every vertex outside \(D\) has **exactly one** neighbor in \(D\). Two disjoint sets \(X,Y\) form a *perfect coalition* if neither alone dominates, each vertex outside \(X\) (respectively outside \(Y\)) has at most one neighbor inside \(X\) (respectively inside \(Y\)), and \(X\cup Y\) is perfect dominating. A perfect-coalition partition requires each class to have a coalition partner, except that a singleton dominating class is allowed by definition. The *partner graph* has one vertex per partition class and edges for perfect-coalition pairs.

All matching edges and their endpoints are labeled, while **partition classes themselves are unlabeled**. Since \(n\ge2\), \(M_n\) has no dominating singleton, so every class must have a partner. Every dominating subset of \(M_n\) is automatically perfect dominating, and every subset automatically satisfies the one-neighbor upper bound because the graph is one-regular.

## Proof
Let \(\pi\) be a perfect-coalition partition with \(k\) classes labeled temporarily by \([k]\). On these \(k\) labels, construct an *edge-type multigraph* \(Q\): each original matching edge whose endpoint class labels are \(a,b\) creates type \(\{a,b\}\), allowing a loop when \(a=b\). Repetitions are ignored when testing coverage. Since every class is nonempty, every label appears in at least one type. A label \(a\) individually dominates \(M_n\) if and only if it meets every original edge, equivalently if it occurs in every type of \(Q\). This is impossible for \(n\ge2\) in a valid partition.

A pair of distinct class labels \(\{a,b\}\) forms a perfect coalition **if and only if** it meets every type of \(Q\). Indeed, on a disjoint union of edges, domination is precisely the condition of meeting each edge; perfection and the separate upper-neighbor bounds are automatic. Write \(H\) for this exact coalition-partner graph. Thus every vertex of \(H\) has degree at least one, every edge of \(H\) meets every type of \(Q\), and conversely every original type (viewed as a set of one or two labels) is a vertex cover of \(H\).

**Bound \(k\le4\).** If \(Q\) contains a loop at label \(a\), every edge of \(H\) is incident with \(a\). As \(H\) has no isolated labels, it contains every edge \(ab\) with \(b\ne a\). Since \(a\) is not individually dominating, some original matching edge has two endpoint labels avoiding \(a\). Its at-most-two-element type must meet all \(k-1\) edges \(ab\), forcing \(k-1\le2\). Therefore \(k\le3\) in the loop case.

Otherwise \(Q\) is loopless. Its types cannot all share a vertex, since then that color class would dominate. For any family of ordinary edges with empty global intersection, either two edges are disjoint or the family contains all three edges of a triangle. In the former case, relabel these types \(12\) and \(34\): every edge of \(H\) must cross from \(\{1,2\}\) to \(\{3,4\}\). Hence it cannot meet labels outside those four, and the no-isolates condition yields \(k\le4\). In the latter case, every edge of \(H\) must contain two vertices of the triangle, so its no-isolates condition yields \(k\le3\). This proves \(k\le4\).

**Classification at equality.** For \(k=4\), there are no loops. The above argument gives two disjoint types, relabeled \(12\) and \(34\). The only possible other types are among the four crossing edges \(13,14,23,24\). Each label must belong to a two-element vertex cover of \(Q\), because it must have a coalition partner. With no additional crossing type, \(Q=2K_2\). With one, \(Q=P_4\). With two *disjoint* crossing types, \(Q=C_4\). With two crossing types sharing a vertex, the resulting graph has a triangle with a pendant edge: the pendant tip does not belong to any two-element cover. With three crossings, at least two labels fail to belong to any two-element cover; with four, no two-element cover exists. Hence the only possible \(Q\)-types are \(2K_2,P_4,C_4\). Directly listing their two-element vertex covers shows that the corresponding partner graphs \(H\) are respectively \(C_4,P_4,2K_2\); every label occurs in a partner edge. Conversely any assignment of matching edges whose type support is exactly one of these three graphs gives a valid four-class partition.

**Enumeration.** Fix four temporary class names. There are exactly \(3\) named realizations of \(2K_2\), \(12\) named realizations of \(P_4\), and \(3\) named realizations of \(C_4\) on the four labels. For a particular type graph with \(r\) distinct edges, assigning the \(n\) distinguishable original matching edges onto all \(r\) edge types gives \(r!S(n,r)\) possibilities. Orienting each original edge's two named endpoints independently gives \(2^n\) possibilities. Every resulting color class occurs, and each unlabeled four-class partition has exactly \(4!\) class-namings. Therefore the three counts, indexed by the *partner graphs*, are
\[
\begin{aligned}
A_n(C_4)&=\frac{3\cdot 2!\cdot2^n S(n,2)}{4!}=2^{n-2}S(n,2),\\
A_n(P_4)&=\frac{12\cdot3!\cdot2^n S(n,3)}{4!}=3\cdot2^nS(n,3),\\
A_n(2K_2)&=\frac{3\cdot4!\cdot2^n S(n,4)}{4!}=3\cdot2^nS(n,4).
\end{aligned}
\]
Their sum is the displayed \(A_n\). Four classes are attainable for every \(n\ge2\): use exactly two disjoint edge types, both at least once. Thus the maximum class count is four, completing the proof.

## Verification
`verify.py` enumerates all unlabeled vertex partitions directly from restricted-growth strings on \(2n\) labeled vertices, evaluates the **original** domination, one-neighbor and perfect-coalition conditions from the graph's adjacency masks, and classifies the partner graphs by degree sequences. It does not use the edge-type characterization to decide validity. Tests for \(n=2,3,4,5\) give the optimum counts \(1,30,364,3480\), and match each of the three exact type formulas. Execute `python3 verify.py`. The finite test is supplementary; the unlimited-\(n\) assertion follows from the proof.

## Relationship to prior work
The perfect-coalition definition and 2024 introduction come from Mojdeh and Samadzadeh, *Perfect coalition in graphs* (arXiv:2409.10185, first posted 2024-09-16; MSC 05C69). This source discusses bounds and selected disconnected extremal graphs, rather than the number of optimum partitions of \(nK_2\). Ordinary coalition partitions date to Haynes and collaborators' 2020 introduction; on one-regular graphs the ordinary and perfect definitions coincide, so the claimed count must be distinguished from both literatures. Bakhshesh, Henning and Pradhan (arXiv:2111.08945) analyze coalition numbers of trees and certain maximum-order cases, not the present full matching census.

Blázsik, *General sharp upper bounds on the transversal coalition number* (DOI:10.1016/j.dam.2025.08.019), supplies general two-uniform transversal bounds and the already-known three **possible** four-vertex optimal coalition-graph types \(C_4,P_4,2K_2\). We do not claim those universal types or the scalar four-block ceiling as original. In the matching family, the exact type supports, Stirling-number coefficients, separate realization counts, and all-\(n\) enumeration are more specific than those general statements. A full bibliographic search cannot guarantee first priority; overlapping unindexed or inaccessible enumeration results remain possible.

## Limitations
The result is solely about full disjoint matchings with individually distinguishable edges and endpoints and **unlabeled partition classes**. It does not enumerate partitions into fewer than four classes, disconnected graphs with other components, or matchings considered modulo graph automorphisms. No independent external audit has been performed. Computations check only finite small instances; the infinite theorem requires the given proof.

## References
- D. A. Mojdeh and M. R. Samadzadeh, *Perfect coalition in graphs*, arXiv:2409.10185, first posted 2024-09-16, https://arxiv.org/abs/2409.10185 .
- T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae and R. Mohan, *Introduction to coalitions in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 653–659, https://doi.org/10.1080/09728600.2020.1832874 .
- D. Bakhshesh, M. A. Henning and D. Pradhan, *On the coalition number of trees*, arXiv:2111.08945, https://arxiv.org/abs/2111.08945 .
- Z. L. Blázsik, *General sharp upper bounds on the transversal coalition number*, Discrete Applied Mathematics 378 (2026), 384–391, https://doi.org/10.1016/j.dam.2025.08.019 .
