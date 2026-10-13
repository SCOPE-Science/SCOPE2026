# Total outer-independent coalition number of noncomplete multipartite graphs with at least three parts
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge 3\), and assume at least one part has size at least \(2\). Then
\[
C_t^{oi}(G)=3.
\]
Here a total outer-independent dominating set (TOIDS) is a total dominating set whose complement is independent; two disjoint non-TOIDS sets form a TOI-coalition when their union is a TOIDS; and \(C_t^{oi}(G)\) is the largest number of blocks in a partition in which every block has a TOI-coalition partner.

## Assumptions and scope
The graph is finite, simple, and complete multipartite, with partite classes \(V_1,\ldots,V_r\), \(r\ge3\). The noncomplete hypothesis means \(n_i=|V_i|\ge2\) for at least one index. The argument is uniform in all part sizes. The already-known complete-graph case is deliberately excluded from the stated finding.

## Proof
First characterize the TOIDS sets. For \(r\ge3\), a set \(D\subseteq V(G)\) is a TOIDS if and only if \(V(G)\setminus D\) is contained in one partite class. The forward implication follows because the complement of a TOIDS is independent, while every independent set of a complete multipartite graph lies in a single part. Conversely, if the complement lies in one part, then \(D\) contains every vertex of the other \(r-1\) parts. Hence \(D\) meets at least two parts, so every vertex, including each vertex of \(D\), has a neighbor in \(D\); thus \(D\) is total dominating, and its complement is independent.

For the lower bound, choose vertices \(y\in V_1\) and \(z\in V_2\) from distinct parts, and put \(Y=\{y\}\), \(Z=\{z\}\), and \(X=V(G)\setminus\{y,z\}\). Neither singleton is total dominating. Also \(X\) is not a TOIDS because its complement \(\{y,z\}\) meets two parts and is therefore not independent. But \(X\cup Y=V(G)\setminus\{z\}\) and \(X\cup Z=V(G)\setminus\{y\}\) are TOIDS by the characterization. Thus \(\{X,Y,Z\}\) is a TOI-coalition partition, so \(C_t^{oi}(G)\ge3\).

For the upper bound, suppose a TOI-coalition partition \(\Psi\) has at least four blocks. Choose coalition partners \(A,B\in\Psi\). Since \(A\cup B\) is a TOIDS, every block outside \(A\) and \(B\) lies in a single part \(P\). Let \(C\) be one of these remaining blocks and choose a coalition partner of \(C\).

If \(C\) partners \(A\), then the complement of \(A\cup C\) contains \(B\) and at least one other remaining block contained in \(P\). Independence of that complement forces \(B\subseteq P\). Consequently the complement of \(A\) is contained in \(P\), so the characterization makes \(A\) itself a TOIDS, contradicting the definition of a coalition block. The same argument excludes \(B\) as the partner of \(C\).

Therefore \(C\) must partner another remaining block \(E\subseteq P\). If there are exactly two remaining blocks, then \(C\cup E\subseteq P\), which cannot be total dominating because vertices of \(P\) have no neighbors inside \(P\). If there are at least three remaining blocks, choose a third one \(F\subseteq P\). Since \(C\cup E\) is a TOIDS, its independent complement contains \(A\), \(B\), and \(F\); the presence of \(F\subseteq P\) forces \(A\cup B\subseteq P\), contradicting that \(A\cup B\) is total dominating. Hence four or more blocks are impossible, and \(C_t^{oi}(G)=3\).

## Verification
The proof above is symbolic and applies to arbitrary part sizes. As a finite stress test, the accompanying `verify.py` independently reconstructs the definitions, enumerates all set partitions for every noncomplete complete-multipartite part-size profile of total order at most \(8\) with at least three parts, and verifies that the maximum coalition-partition size is \(3\). It also checks the TOIDS characterization on every vertex subset for those profiles. These finite computations corroborate but do not replace the infinite proof.

## Relationship to prior work
Buntina and Golmohammadi introduced TOI-coalitions and \(C_t^{oi}\) in arXiv:2607.23623v1. Their exact-values section gives \(C_t^{oi}(K_n)=3\) and \(C_t^{oi}(K_{r,s})=s+1\) for \(r\le s\), together with path and cycle values. The inspected preprint does not state a complete-multipartite theorem. The present result covers the missing noncomplete complete-multipartite regime with at least three parts and shows a sharp structural collapse to the constant value \(3\), in contrast to the growing bipartite value.

## Limitations
The theorem does not reclassify complete bipartite graphs, which are covered in the initiating paper, and it excludes complete graphs from the new claim because their value \(3\) is already known there. The literature search found no equivalent complete-multipartite TOI-coalition theorem, but a poorly indexed result under different terminology remains a residual originality risk. No claim of independent audit is made.

## References
[1] O. Buntina and H. Golmohammadi, “Total outer-independent coalition in graphs,” arXiv:2607.23623v1, first public 2026-07-26.
[2] M. Krzywkowski, “An upper bound on the total outer-independent domination number of a tree,” *Opuscula Mathematica* 32 (2012), 153–158.
