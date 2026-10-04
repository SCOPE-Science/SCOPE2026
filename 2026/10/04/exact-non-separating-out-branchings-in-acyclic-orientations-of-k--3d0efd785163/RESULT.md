# Exact non-separating out-branchings in acyclic orientations of \(K_{3,n}\)
## Finding
For every integer \(n\ge4\), let \(D\) be an acyclic orientation of \(K_{3,n}\), with partite sets \(A\) and \(B\) of sizes \(3\) and \(n\). Form the canonical source-removal code by repeatedly deleting all current sources; it is an alternating sequence of nonempty \(A\)- and \(B\)-blocks. Then \(D\) has a non-separating out-branching if and only if the first block is a singleton and the block code is not one of \(A^1B^nA^2\), \(A^1B^1A^2B^{n-1}\), \(B^1A^3B^{n-1}\), or \(B^1A^1B^{n-1}A^2\). Here non-separating means that after deleting the out-branching arcs, the remaining underlying graph is connected.

## Assumptions and scope
All graphs are finite and simple. Let \(D\) be an acyclic orientation of \(K_{3,n}\), where \(n\ge4\), with partite sets \(A\) and \(B\), where \(|A|=3\) and \(|B|=n\). An out-branching is a spanning directed tree rooted at its unique indegree-zero vertex. It is non-separating here when deleting its arcs from \(D\) leaves a digraph whose underlying undirected graph is connected, matching the convention used in the initiating 2026 work.

Repeatedly remove all current sources of \(D\). For a complete bipartite graph, all current sources lie in one part, and after their deletion the next nonempty source set lies in the other part. Thus the process produces a canonical alternating block code. We write \(A^i\) or \(B^j\) for a block containing exactly \(i\) or \(j\) vertices. Every arc between two opposite-part blocks points from the earlier block to the later block.

The restriction \(n\ge4\) is structural, not computational. The underlying graphs \(K_{2,n}\) and \(K_{3,3}\) have fewer than \(2(|V|-1)\) edges, so they cannot contain two edge-disjoint spanning trees and hence cannot support an acyclic orientation with a non-separating out-branching. The family \(K_{3,n}\), \(n\ge4\), is therefore the first complete-bipartite family where the question is nontrivial.

## Proof
If the first source-removal block has size at least two, \(D\) has at least two sources, so it has no out-branching. Assume henceforth that the first block is a singleton.

First consider the four exceptional codes. For \(A^1B^nA^2\), every vertex of \(B\) has exactly one in-neighbour, namely the source in \(A\). Every out-branching must therefore use all \(n\) edges incident with that source, so deleting the branching isolates it. For \(A^1B^1A^2B^{n-1}\), let \(b\) be the singleton \(B\)-block. The edge from the source to \(b\) is forced, and both later \(A\)-vertices have \(b\) as their only earlier \(B\)-vertex. Hence all three edges incident with \(b\) are forced into every out-branching, so \(b\) is isolated after deletion. The arguments for \(B^1A^3B^{n-1}\) and \(B^1A^1B^{n-1}A^2\) are the same after interchanging the two parts: respectively the initial \(B\)-source or the singleton first \(A\)-block has every incident edge forced into the branching. Thus none of the four exceptional codes admits a non-separating out-branching.

It remains to construct a branching for every other singleton-first-block code. In every construction below, an arrow \(x\to y\) denotes the chosen parent arc of \(y\); all unspecified vertices in the relevant large part receive the parent indicated in the sentence. Since every chosen parent occurs in an earlier source-removal block, all listed edges are arcs of \(D\). Choosing one entering arc for every non-source vertex in an acyclic digraph yields an out-branching.

Suppose first that the source \(s\) lies in \(A\), and let the first \(B\)-block have size \(k\). If \(2\le k<n\), choose distinct \(b_1,b_2\) in that first block, write the other \(A\)-vertices in block order as \(a_1,a_2\), and choose a \(B\)-vertex \(c\) after the first block. Use \(b_1\to a_1\), \(b_2\to a_2\), \(a_1\to c\), and \(s\to b\) for every \(b\in B\setminus\{c\}\). In the complement, the edges \(sc\), \(ca_2\), \(b_1a_2\), and \(b_2a_1\) remain, while every other \(B\)-vertex retains edges to both \(a_1\) and \(a_2\). Hence the complement is connected.

If the source lies in \(A\) and \(k=1\), let \(b_0\) be the first \(B\)-vertex. Since the second exceptional code is excluded, the next \(A\)-block has size one; call its vertex \(a_1\), let \(c\) be a \(B\)-vertex occurring before the final \(A\)-vertex \(a_2\), and choose distinct \(d,e\in B\setminus\{b_0,c\}\), possible because \(n\ge4\). Use \(s\to b_0\), \(b_0\to a_1\), \(s\to c\), \(c\to a_2\), \(a_1\to d\), and \(s\to b\) for every remaining \(B\)-vertex. The complement contains the path \(s-d-a_2-e-a_1-c\) and also the edge \(a_2b_0\); every other \(B\)-vertex is adjacent there to both \(a_1\) and \(a_2\). Thus it is connected.

Now suppose that the source \(s\) lies in \(B\). If the first \(A\)-block has size two, call its vertices \(a_0,a_1\), let \(b_1\) be the first later \(B\)-vertex, let \(a_2\) be the remaining \(A\)-vertex, and choose distinct \(d,e\in B\setminus\{s,b_1\}\). Use \(s\to a_0\), \(s\to a_1\), \(a_0\to b_1\), \(b_1\to a_2\), \(a_1\to d\), and \(a_0\to b\) for every other non-source \(B\)-vertex. The complement contains \(sa_2\), \(a_2d\), \(da_0\), \(a_2e\), \(ea_1\), and \(a_1b_1\), and every further \(B\)-vertex retains edges to \(a_1\) and \(a_2\). Hence it is connected.

Finally suppose that the source lies in \(B\) and the first \(A\)-block is the singleton \(a_0\). Let \(b_1\) be a vertex of the next \(B\)-block. Because the fourth exceptional code is excluded, some later \(A\)-vertex \(a_1\) occurs before all non-source \(B\)-vertices have been removed; choose a \(B\)-vertex \(c\) after \(a_1\), let \(a_2\) be the third \(A\)-vertex, and choose \(e\in B\setminus\{s,b_1,c\}\). Use \(s\to a_0\), \(b_1\to a_1\), \(s\to a_2\), \(a_1\to c\), and \(a_0\to b\) for every non-source \(B\)-vertex other than \(c\). The complement contains the path \(s-a_1-e-a_2-c-a_0\) and the edge \(b_1a_2\); every other \(B\)-vertex retains edges to \(a_1\) and \(a_2\). Hence it is connected.

These four constructive cases exhaust all nonexceptional singleton-first-block codes, proving the equivalence.

## Verification
The standalone verifier `verify_k3n.py` reconstructs every block word with three \(A\)-vertices. It checks the explicit proof constructions for all words with \(4\le n\le30\), totaling 9,792 positive cases. Independently, for every word with \(4\le n\le7\), it enumerates every possible choice of one earlier opposite-part parent for each non-source vertex and directly tests connectivity after deleting the resulting out-branching. Across 295 words, the exhaustive result agrees exactly with the four-pattern classification. The replay output is stored in `VERIFY.out`.

The finite checks are not the proof for unbounded \(n\); the proof above is. Their role is to test the case split, edge directions, and complement-connectivity assertions on all small canonical orientations and many larger constructions.

## Relationship to prior work
Bang-Jensen and Yeo introduced the present acyclic orientation-completion direction and proved that, for an already acyclic digraph, existence of a non-separating out-branching is decidable in polynomial time by matroid intersection. They also observed that an undirected graph has some acyclic orientation with such a branching exactly when it has two edge-disjoint spanning trees, and they posed the mixed-graph completion problem. Their theorem is algorithmic and does not give the exact orientation-by-orientation classification above for \(K_{3,n}\).

Carballosa, Reyes, and Khera give the canonical source-removal encoding for acyclic orientations of complete multipartite graphs and enumerate orientations having a directed spanning tree, equivalently a unique source. Their full text does not impose connectivity after deleting the spanning tree. The present result uses that encoding but adds the non-separating condition and identifies exactly four obstruction codes in the first nontrivial complete-bipartite family.

Earlier work of Bang-Jensen, Bessy, and Yeo studies non-separating structures in highly connected digraphs of independence number two. Its hypotheses and connectivity setting do not imply this acyclic \(K_{3,n}\) classification; for \(n\ge4\), the independence number of \(K_{3,n}\) is \(n\), and a nontrivial acyclic digraph is not strongly connected.

## Limitations
The theorem classifies only acyclic orientations of \(K_{3,n}\) for \(n\ge4\). It does not classify \(K_{m,n}\) for \(m\ge4\), mixed partial orientations, or non-acyclic digraphs. The verifier is finite and does not certify the infinite quantifier; the explicit proof supplies that step. No claim is made about the number of distinct non-separating out-branchings inside a positive orientation.

## References
1. J. Bang-Jensen and A. Yeo, *Acyclic orientations of mixed graphs*, arXiv:2609.32403v1, first public 2026-09-26.
2. W. Carballosa, F. A. Reyes, and J. Khera, *Encoding and enumerating acyclic orientations of graphs*, Utilitas Mathematica 125 (2025), 21–41; arXiv:2303.09021v2.
3. J. Bang-Jensen, S. Bessy, and A. Yeo, *Non-separating spanning trees and out-branchings in digraphs of independence number 2*, Graphs and Combinatorics 38 (2022), Article 187; arXiv:2007.02834v1.
