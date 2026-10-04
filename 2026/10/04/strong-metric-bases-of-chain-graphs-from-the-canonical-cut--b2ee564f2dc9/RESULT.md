# Strong metric bases of chain graphs from the canonical cut
## Finding
Let \(G\) be a finite connected chain graph. Write its canonical nonempty open-neighborhood twin classes as
\[
A_1,\ldots,A_p,B_1,\ldots,B_p,
\]
with adjacency normalized by \(A_i\sim B_j\) exactly when \(j\le i\). Put \(\alpha_i=|A_i|\), \(\beta_i=|B_i|\), and \(N=|V(G)|\).

If \(G\cong K_2\), then \(\operatorname{sdim}(G)=1\) and the two singleton sets are the two strong metric bases. Otherwise, the strong resolving graph \(G_{SR}\) has exactly the following edges: every pair of distinct vertices within one canonical class \(A_i\) or \(B_i\), and every cross pair \(a\in A_i\), \(b\in B_j\) with \(j>i\). It has no other edges.

The maximum independent sets of \(G_{SR}\) are exactly the sets obtained by choosing, for one unique cut index \(t\in\{1,\ldots,p\}\), one vertex from each of
\[
B_1,\ldots,B_t,A_t,\ldots,A_p.
\]
Thus every such independent set has size \(p+1\), and every strong metric basis is its complement. Hence
\[
\operatorname{sdim}(G)=N-p-1
\]
and the number of strong metric bases equals
\[
\sum_{t=1}^p
\left(\prod_{j=1}^t\beta_j\right)
\left(\prod_{i=t}^p\alpha_i\right).
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A chain graph is a bipartite graph whose neighborhoods on either side are linearly ordered by inclusion; after coalescing equal open neighborhoods, the canonical classes above are nonempty and unique up to reversing the two sides and their order. A vertex \(u\) is maximally distant from \(v\) when every neighbor \(w\) of \(u\) satisfies \(d(w,v)\le d(u,v)\); two vertices are mutually maximally distant when each is maximally distant from the other. The strong resolving graph joins precisely mutually maximally distant pairs. The standard vertex-cover characterization of strong metric dimension is used.

The displayed formula is for all connected chain graphs except that \(K_2\) is stated separately. In particular, for \(p=1\) and \(G\not\cong K_2\), it specializes to the known scalar complete-bipartite value \(N-2\), while additionally counting all minimum bases.

## Proof
First determine the mutually maximally distant pairs.

Two distinct vertices in the same canonical class are at distance \(2\) and have identical open neighborhoods. Every neighbor of either vertex is adjacent to the other, so the pair is mutually maximally distant. Hence each \(A_i\) and each \(B_i\) induces a clique in \(G_{SR}\).

Now take two vertices from different \(A\)-classes, say \(a_i\in A_i\) and \(a_k\in A_k\) with \(i<k\). Their distance is \(2\). Any vertex of the nonempty class \(B_k\) is adjacent to \(a_k\), while it is nonadjacent to \(a_i\) and has distance \(3\) from \(a_i\). Thus \(a_k\) is not maximally distant from \(a_i\). The symmetric argument applies to two different \(B\)-classes. Therefore there are no strong-resolving-graph edges between distinct classes on the same bipartition side.

For a cross pair \(a_i\in A_i\), \(b_j\in B_j\) with \(j>i\), the two vertices are nonadjacent and have distance \(3\). Every neighbor of \(a_i\) lies in some \(B_h\) with \(h\le i\) and is at distance \(2\) from \(b_j\); every neighbor of \(b_j\) lies in some \(A_k\) with \(k\ge j\) and is at distance \(2\) from \(a_i\). Hence the pair is mutually maximally distant, giving every cross edge with \(j>i\).

For an adjacent cross pair, \(j\le i\), the distance is \(1\). Unless the graph is exactly \(K_2\), at least one endpoint has another neighbor, and that other neighbor is at distance \(2\) from the opposite endpoint. Thus the adjacent pair is not mutually maximally distant. In \(K_2\) the unique edge is mutually maximally distant, which explains the exceptional case.

Assume now \(G\not\cong K_2\). Since each canonical class is a clique in \(G_{SR}\), an independent set uses at most one vertex from each class. If it uses both sides, let \(q\) be the largest selected \(B\)-index and \(r\) the smallest selected \(A\)-index. The cross-edge rule forces \(q\le r\). Therefore its size is at most
\[
q+(p-r+1)\le p+1.
\]
If it uses only one side, its size is at most \(p\). Equality \(p+1\) is possible exactly when \(q=r=t\), every class \(B_1,\ldots,B_t\) contributes one selected vertex, and every class \(A_t,\ldots,A_p\) contributes one selected vertex. This proves both the maximum-independent-set classification and its count
\[
\sum_{t=1}^p
\left(\prod_{j=1}^t\beta_j\right)
\left(\prod_{i=t}^p\alpha_i\right).
\]

For every connected graph, a strong metric basis is a minimum vertex cover of its strong resolving graph. The complement of a minimum vertex cover is a maximum independent set, so \(\operatorname{sdim}(G)=N-(p+1)=N-p-1\), and complements of the maximum independent sets above are exactly all strong metric bases.

## Verification
The accompanying `verify.py` constructs every canonical positive chain-graph profile through order \(9\). It computes all-pairs graph distances, recomputes mutually maximally distant pairs directly from the definition, and compares them with the claimed strong-resolving-graph structure. It then enumerates vertex subsets, tests the literal strong-resolution condition for every unordered vertex pair, rules out all sets smaller than the claimed optimum, and checks both the minimum size and the exact number of bases.

A replay of the packaged verifier gives:

`VERIFY_OK profiles=255 subset_checks=70490 mmd_checks=7423 basis_checks=2829 max_order=9`

The finite census is a check of the proof, not a substitute for the argument for arbitrary class sizes.

## Relationship to prior work
Oellermann and Peters-Fransen introduced the strong-dimension framework and its reduction to vertex cover in the strong resolving graph. Kratica, Kovačević-Vujčić, Čangalović, and Mladenović survey that reduction and the then-known exact graph classes. May and Oellermann give an efficient method for the broader class of distance-hereditary graphs; this is algorithmic broader coverage, but it does not state the chain-graph closed formula or enumerate all minimum bases. Kuziak, Yero, and Rodríguez-Velázquez use the mutually-maximally-distant strong resolving graph in exact work on rooted products; their accepted author version was posted online on 30 June 2015, which supplies the exact public-source date used here and lists primary MSC 05C12.

The chain-graph paper of Bhat, Hanif, and Sudhakara treats ordinary metric dimension and restricted threshold dimension. Its full public PDF was inspected at the abstract/MSC page and at its concluding theorem/conclusion; those passages concern ordinary metric dimension, not strong metric dimension. The present statement is not inferred from title mismatch: its implication was also compared against the broader distance-hereditary algorithm and the general strong-resolving-graph theorem. The complete-bipartite scalar case is prior-covered and is not claimed as new.

## Limitations
The theorem concerns strong metric dimension and its minimum bases, not all strong resolving sets and not fractional, partition, local, or mixed metric variants. The proof assumes connected chain graphs and uses the canonical nonempty twin-class decomposition. The literature search did not locate a chain/Ferrers-specific prior statement with the same formula or basis classification, but weakly indexed older literature under alternative names such as Ferrers or difference graphs remains a residual bibliographic risk. The full text of the foundational 2007 article was not available from the inspected public endpoint; its vertex-cover theorem was checked in the full-text 2014 survey instead.

## References
1. O. R. Oellermann and J. Peters-Fransen, “The strong metric dimension of graphs and digraphs,” *Discrete Applied Mathematics* 155 (2007), 356–364. DOI: 10.1016/j.dam.2006.06.009.
2. J. Kratica, V. Kovačević-Vujčić, M. Čangalović, and N. Mladenović, “Strong metric dimension: A survey,” *Yugoslav Journal of Operations Research* 24 (2014), 187–198. DOI: 10.2298/YJOR130520042K.
3. T. R. May and O. R. Oellermann, “The Strong Dimension of Distance-Hereditary Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 76 (2011), 59–73.
4. D. Kuziak, I. G. Yero, and J. A. Rodríguez-Velázquez, “Strong metric dimension of rooted product graphs,” *International Journal of Computer Mathematics* 93 (2016), 1265–1280. DOI: 10.1080/00207160.2015.1061656.
5. K. Arathi Bhat, S. Hanif, and G. Sudhakara, “Metric dimension and its variations of chain graphs,” *Proceedings of the Jangjeon Mathematical Society* 24 (2021), 309–321. DOI: 10.17777/pjms2021.24.3.309.
