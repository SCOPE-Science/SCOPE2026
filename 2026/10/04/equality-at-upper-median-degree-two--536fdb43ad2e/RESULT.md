# Equality at upper median degree two
## Finding
Let \(G\) be a finite connected simple graph of order \(n\), let \(\gamma_2(G)\) denote the minimum size of a set \(D\subseteq V(G)\) such that every vertex outside \(D\) has at least two neighbors in \(D\), and write the degree sequence as \(d_1\le\cdots\le d_n\). Define the upper median degree by \(m(G)=d_{\lfloor n/2\rfloor+1}\).

Assume \(m(G)=2\). Then
\[
\gamma_2(G)=n-m(G)+1=n-1
\]
if and only if \(G\) is one of the following five isomorphism types: \(P_4\), or a triangle \(K_3\) with \(k\) pendant vertices, all adjacent to the same triangle vertex, where \(0\le k\le3\).

Thus the newly proved upper-median bound is rigid in its first nontrivial median layer: equality at \(m(G)=2\) forces \(n\le6\).

## Assumptions and scope
Graphs are finite, simple, and connected. The definition of 2-domination is the open-neighborhood definition: vertices belonging to the dominating set impose no condition on themselves. The theorem concerns exactly the layer \(m(G)=2\); it does not classify equality for other upper median degrees.

For the proof, put
\[
H=\{v\in V(G): d_G(v)\ge2\}.
\]
Because \(m(G)=2\), the set \(H\) is nonempty and in fact has at least \(\lceil n/2\rceil\) vertices.

## Proof
We first prove a structural lemma that does not use the median hypothesis.

**Lemma.** If a finite simple graph \(G\) has at least one vertex of degree at least two, then \(\gamma_2(G)=n-1\) if and only if \(H\) induces a clique and at most one vertex of \(H\) has degree at least three.

Choose a vertex \(x\) of degree at least two. Then \(V(G)\setminus\{x\}\) is 2-dominating, so \(\gamma_2(G)\le n-1\).

For distinct vertices \(x,y\), the set \(V(G)\setminus\{x,y\}\) is 2-dominating exactly under the following condition. If \(xy\notin E(G)\), then each omitted vertex retains all of its neighbors in the selected set, so both \(d_G(x)\ge2\) and \(d_G(y)\ge2\) are necessary and sufficient. If \(xy\in E(G)\), each omitted vertex loses the other omitted vertex as a selected neighbor, so both \(d_G(x)\ge3\) and \(d_G(y)\ge3\) are necessary and sufficient.

Consequently a 2-dominating set of size \(n-2\) exists if and only if either two vertices of \(H\) are nonadjacent, or two adjacent vertices both have degree at least three. Therefore no such set exists exactly when \(H\) is a clique and at most one of its vertices has degree at least three. Since a set of size \(n-1\) already exists, this proves the lemma.

Now assume \(m(G)=2\) and equality in the upper-median bound. Then \(\gamma_2(G)=n-1\), so the lemma applies. Because \(H\) is a clique and at most one of its vertices has degree at least three, \(|H|\le3\): if \(|H|\ge4\), every vertex of the clique \(G[H]\) already has at least three neighbors in \(H\). On the other hand, \(m(G)=2\) implies \(|H|\ge\lceil n/2\rceil\). Hence \(n\le6\).

Connectivity implies that every vertex outside \(H\) is a leaf. We now distinguish \(|H|\).

If \(|H|=1\), the graph is a star with at least two leaves. Its upper median degree is one, contradicting \(m(G)=2\).

If \(|H|=2\), the two vertices of \(H\) are adjacent. Each must have at least one leaf neighbor in order to have degree at least two, and at most one may have more than one leaf neighbor. Write the two leaf counts as \(1\) and \(k\) with \(k\ge1\). If \(k\ge2\), there are \(k+1\) leaves among \(k+3\) vertices, so the upper median degree is one. Thus \(k=1\), giving exactly \(P_4\).

If \(|H|=3\), then \(G[H]\cong K_3\). Since at most one vertex of \(H\) can have degree at least three, all leaves are adjacent to a single triangle vertex. Let their number be \(k\ge0\). The degree multiset is
\[
\underbrace{1,\ldots,1}_{k\text{ times}},2,2,k+2.
\]
Its upper median is two exactly for \(0\le k\le3\). This yields the four triangle-with-leaves graphs in the statement.

Conversely, direct application of the lemma shows that \(P_4\) and each of the four listed triangle-with-leaves graphs has \(\gamma_2(G)=n-1\); the displayed degree multisets show \(m(G)=2\). Therefore each attains \(\gamma_2(G)=n-m(G)+1\), completing the classification.

## Verification
The proof above is analytic and covers all finite connected simple graphs with \(m(G)=2\). A standalone verifier in `artifacts/verify.py` independently enumerates every labeled simple graph of orders two through six, filters the connected graphs, computes \(\gamma_2\) directly by subset search, computes the upper median degree directly from the degree sequence, and checks both the structural lemma and the five-type classification. It does not use the proof's classification to compute \(\gamma_2\).

A replay produced:

`ALL CHECKS PASSED; graph_masks=33866; connected_graphs=27475; structural_checks=27475; m2_graphs=8595; m2_equalities=115; max_order=6`

The number \(115\) counts labeled equality graphs; the verifier separately checks that their degree/isomorphism signatures reduce to the five types stated above. The computation is a finite stress test, not the reason the theorem holds for all orders; the analytic proof supplies the order bound \(n\le6\).

## Relationship to prior work
Jun Qing proved in 2026 that every nonempty finite simple graph satisfies
\[
\gamma_2(G)\le n-m(G)+1.
\]
The same paper notes sharpness for every order using complete graphs \(K_n\), for which \(m(K_n)=n-1\), but it does not give an equality classification or discuss the layer \(m(G)=2\).

The 2010 paper of DeLaViña, Larson, Pepper, and Waller introduced the upper-median conjecture and established several earlier 2-domination bounds, including partial results for bipartite graphs. Those statements do not classify equality when the upper median degree is two. Earlier literature on 2-domination contains many bounds and comparisons with other domination parameters, but the targeted searches described in `AUDIT.json` did not locate the structural criterion \(\gamma_2(G)=n-1\) used here or the resulting five-type upper-median equality classification.

## Limitations
The theorem is restricted to connected graphs with upper median degree exactly two. It makes no claim about equality for \(m(G)\ne2\), and it does not claim a complete classification of graphs with a prescribed 2-domination number outside the near-full value \(n-1\). Literature search cannot prove absence from all publications; the residual risk is that an older domination paper states an equivalent \(\gamma_2(G)=n-1\) characterization under different terminology.

## References
1. Jun Qing, *The 2-Domination Number and the Upper Median Degree: A Proof of Graffiti.pc Conjecture 387*, arXiv:2607.27246v1, first public 2026-07-28, primary MSC 05C69.
2. E. DeLaViña, C. E. Larson, R. Pepper, and B. Waller, *Graffiti.pc on the 2-domination number of a graph*, Congressus Numerantium 203 (2010), 15–32.
3. F. Bonomo, B. Brešar, L. N. Grippo, M. Milanič, and M. D. Safe, *Domination parameters with number 2: Interrelations and algorithmic consequences*, Discrete Applied Mathematics, DOI 10.1016/j.dam.2017.08.017.
