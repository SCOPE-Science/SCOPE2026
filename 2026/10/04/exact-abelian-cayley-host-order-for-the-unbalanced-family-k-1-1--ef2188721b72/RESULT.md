# Exact abelian Cayley host order for the unbalanced family \(K_{1,1,n}\)
## Finding
For every integer \(n\ge2\),
\[
\eta(K_{1,1,n})=3n.
\]
Here \(\eta(G)\) is the least order of a finite abelian group \(\Gamma\) for which \(G\) occurs as an induced subgraph of a Cayley graph of \(\Gamma\). Thus the complete-multipartite upper construction of order \(3n\) is optimal on this entire unbalanced family. In particular, the previously highlighted unresolved example \(K_{1,1,5}\) has \(\eta(K_{1,1,5})=15\).

## Assumptions and scope
Graphs are finite, simple, and undirected. Cayley graphs are taken over finite abelian groups with a symmetric connection set not containing the identity. The statement concerns the complete tripartite graph having part sizes \(1,1,n\), with \(n\ge2\).

For an injective labeling \(f:V(G)\to\Gamma\), write \(D_E\) for the set of signed differences arising from edges and \(D_{\overline E}\) for the signed differences arising from nonedges. The exact induced-embedding criterion is
\[
D_E\cap D_{\overline E}=\varnothing.
\]

## Proof
Let an induced embedding of \(K_{1,1,n}\) into a Cayley graph of a finite abelian group \(\Gamma\) be given. Translate the labeling so that one singleton part is labeled \(0\). Let \(z\ne0\) be the label of the other singleton, and let \(A\subseteq\Gamma\) be the set of labels of the \(n\)-vertex part. Then \(|A|=n\), \(0\notin A\), and \(z\notin A\).

Consider
\[
A-A,\qquad -A,\qquad z-A.
\]
The set \(A-A\) has at least \(n\) elements, since for any fixed \(a_0\in A\) the translate \(A-a_0\) is an \(n\)-element subset of \(A-A\). The other two sets each have exactly \(n\) elements.

These three sets are pairwise disjoint. First, every element of \(-A\) is a difference across an edge from \(0\) to the large part, whereas every nonzero element of \(A-A\) that arises from two distinct labels is a nonedge difference. Since \(0\notin-A\), the induced-embedding criterion gives
\[
(A-A)\cap(-A)=\varnothing.
\]
Likewise, every element of \(z-A\) is an edge difference from the other singleton to the large part; because \(0\notin z-A\),
\[
(A-A)\cap(z-A)=\varnothing.
\]
Finally, if \(-a=z-b\) for some \(a,b\in A\), then \(z=b-a\). Since \(z\ne0\), this makes the edge difference between the two singleton vertices simultaneously a nonedge difference between two distinct vertices of the large part, again contradicting the induced-embedding criterion. Hence
\[
(-A)\cap(z-A)=\varnothing.
\]
Therefore
\[
|\Gamma|\ge |A-A|+|-A|+|z-A|\ge3n.
\]

For the reverse inequality, take \(\Gamma=\mathbb Z_3\times\mathbb Z_n\) and
\[
S=\{(i,j)\in\Gamma:i\ne0\}.
\]
The Cayley graph \(\operatorname{Cay}(\Gamma,S)\) is \(K_{n,n,n}\), with the three parts given by the first coordinate. Choosing \((0,0)\), \((1,0)\), and all \((2,j)\) for \(j\in\mathbb Z_n\) induces \(K_{1,1,n}\). Thus \(\eta(K_{1,1,n})\le3n\), completing the proof.

## Verification
The proof is purely finite and analytic. A standalone checker additionally exhausts all finite abelian group types of every order below \(3n\) for \(2\le n\le5\), after translating one singleton label to the identity, and finds no induced embedding. It also verifies the explicit \(\mathbb Z_3\times\mathbb Z_n\) construction and the three-set disjointness certificate for \(2\le n\le50\). The finite computation is a stress test only; it is not used to justify the universal quantifier. Replay output: `ALL CHECKS PASSED; exhaustive_n=2..5; host_types=30; normalized_label_candidates=26938; constructions_n=2..50`.

## Relationship to prior work
Fokam Souop and Bitjoka introduced \(\eta\) as an individual-graph invariant and proved the exact difference-set criterion used above. Their complete-multipartite discussion gives only the general upper bound
\[
\eta(K_{a_1,\ldots,a_k})\le k\max_i a_i,
\]
explicitly states that unbalanced complete multipartite graphs are unresolved, and singles out \(K_{1,1,5}\): their local lower floor is \(10\), while the multipartite construction has order \(15\). The present argument supplies a genuinely multi-neighborhood lower obstruction and closes that example together with the full family \(K_{1,1,n}\).

The older representation-number theory for complete multipartite graphs concerns a stricter invariant: the host is forced to be cyclic and the connection set is forced to be the units. Its conclusions therefore do not determine \(\eta\), where both restrictions are removed.

## Limitations
The three-disjoint-set argument uses the two singleton parts essentially. It does not determine \(\eta\) for arbitrary unbalanced complete multipartite graphs, and no claim is made for other part-size patterns. Search-based noncoverage is not treated as a proof of novelty; the strongest evidence is that the initiating \(\eta\)-paper itself identifies this exact multipartite regime, including \(K_{1,1,5}\), as open. Older induced-Cayley literature may contain differently phrased special cases not recovered by the searches performed.

## References
1. Rigobert Fokam Souop and Laurent Bitjoka, “Induced Embeddings of Graphs into Abelian Cayley Graphs,” arXiv:2609.01486, first public 2026-09-01.
2. László Babai and Vera T. Sós, “Sidon sets in groups and induced subgraphs of Cayley graphs,” European Journal of Combinatorics 6 (1985), 101–114.
3. Reza Akhtar, Anthony B. Evans, and Dan Pritikin, “Representation numbers of complete multipartite graphs,” Discrete Mathematics 312 (2012), 1158–1165, doi:10.1016/j.disc.2011.12.003.
