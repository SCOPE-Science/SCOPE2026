# Orientable total-domination spectrum of cycle bouquets
## Finding
For integers \(t\ge 2\) and \(\ell_1,\ldots,\ell_t\ge3\), let \(B=\bigvee_{i=1}^{t} C_{\ell_i}\) be the simple graph formed by identifying one vertex of each of \(t\) otherwise vertex-disjoint cycles to a single common vertex \(c\). Put \(\beta=\sum_{i=1}^{t}(\ell_i-3)\). A valid orientation \(D\) of \(B\) has indegree at least one at every vertex. Write \(\gamma_t(D)\) for the minimum size of a vertex set \(S\) supplying an in-neighbor in \(S\) to *every* vertex, including vertices of \(S\). Orientations of the fixed graph are counted as assignments of directions to its distinct edges, not modulo graph automorphisms.

**Theorem.** The complete distribution of these orientation minima is the polynomial
\[
 Z_B(z)=\sum_{D\text{ valid}}z^{\gamma_t(D)}
 =z^{\beta+2}\left(\prod_{i=1}^{t}(\ell_i-1+2z)-\prod_{i=1}^{t}(\ell_i-1)\right).
\]
In particular, the lower and upper orientable total domination numbers are
\[
 \operatorname{dom}_t(B)=\beta+3,\qquad
 \operatorname{DOM}_t(B)=\beta+t+2.
\]
Every integer in this interval is attained, with its exact number of realizing valid orientations given by the corresponding coefficient of \(Z_B(z)\). The total number of valid orientations is \(\prod_i(\ell_i+1)-\prod_i(\ell_i-1)\).

## Assumptions and scope
All graphs are finite, undirected, simple, and fixed with distinguished vertex sets. A cycle petal has length \(\ell_i\ge3\), and different petals share only the common hub \(c\); there are no edges joining their nonhub vertices. No loops, parallel edges, or directed two-cycles are allowed. Orientations are valid only if every vertex has an in-neighbor. The number \(\gamma_t(D)\) uses open in-neighborhood total domination and is not the ordinary domination number, which exempts vertices inside a dominating set. The polynomial counts valid orientations rather than sets or isomorphism classes.

## Proof
Write one petal cyclically as \(v_0=c,v_1,\ldots,v_{\ell-1},v_\ell=c\). For the edge \(v_jv_{j+1}\), let its sign be \(+\) when directed from \(v_j\) to \(v_{j+1}\), and \(-\) otherwise. At the nonhub vertex \(v_j\) with \(1\le j\le\ell-1\), indegree zero occurs exactly when the two consecutive signs are \((- ,+)\). Hence the sign word cannot contain a transition from \(-\) to \(+\). It follows that every locally admissible orientation is exactly one of the following:

* either of the two directed cycles (the all-\(+\) or all-\(-\) word); or
* one of the \(\ell-1\) words consisting of \(p\) plus signs followed by \(\ell-p\) minus signs, where \(1\le p\le\ell-1\). In this second type, the hub is the unique source and \(v_p\) is the unique sink.

Call the first type *cyclic* and the second type *outward*. Each petal offers two cyclic and \(\ell-1\) outward orientations. A globally valid orientation must contain at least one cyclic petal, since the hub has an incoming arc precisely from cyclic petals. Conversely, once every nonhub vertex has indegree at least one and at least one petal is cyclic, all vertices have positive indegree. Thus validity is equivalent to making such local choices with at least one cyclic choice.

Fix a valid orientation. Every nonhub vertex on an outward petal lies on one of two directed paths from the hub to the sink. The hub belongs to every total dominating set: on each petal at least one neighbor of \(c\) has \(c\) as its unique in-neighbor. On an outward petal of length \(\ell\), if one path from \(c\) to the sink has length one, the opposite directed path forces exactly \(\ell-3\) additional nonhub vertices into any total dominating set; the sink is already dominated by \(c\). If both paths have length at least two, every nonhub vertex other than the sink and the two first neighbors of \(c\) has a unique in-neighbor, forcing altogether \(\ell-4\) predecessor vertices, while the sink requires one additional predecessor on either path. Therefore in both cases the exact minimum nonhub contribution is \(\ell-3\). These choices dominate all nonhub vertices of the petal, and no outward petal supplies an in-neighbor to the hub.

On a cyclic petal, choose a direction and list its vertices so that \(c\to v_1\to\cdots\to v_{\ell-1}\to c\). The unique-in-neighbor conditions for \(v_2,\ldots,v_{\ell-1}\) force the \(\ell-2\) nonhub vertices \(v_1,\ldots,v_{\ell-2}\). They, with \(c\), dominate all nonhub vertices of this petal. The remaining vertex \(v_{\ell-1}\) is its sole in-neighbor of the hub. To dominate the hub, at least one such terminal vertex from *some* cyclic petal must additionally be selected; any one suffices. Terminal vertices are distinct from all the forced vertices.

Consequently, if exactly \(k\ge1\) petals are cyclic, then the exact minimum is
\[
 1+\sum_{i\text{ outward}}(\ell_i-3)
 +\sum_{i\text{ cyclic}}(\ell_i-2)+1
 =\beta+k+2.
\]
The first \(1\) accounts for the forced hub, the last for an in-neighbor of that hub, and all local contributions can be attained simultaneously because the petals meet only at \(c\).

Attach weight \(2z\) to each cyclic petal and weight \(\ell_i-1\) to each outward petal. Choosing a nonempty collection of cyclic petals produces the weighted product \(\prod_i(\ell_i-1+2z)-\prod_i(\ell_i-1)\). Multiplying by \(z^{\beta+2}\) proves the full enumerator. All coefficients for \(z^{\beta+2+k}\), \(1\le k\le t\), are positive, which proves both extrema and complete intermediate realization. Setting \(z=1\) counts valid orientations.

## Verification
Run `python verify_orientable_total_cycle_bouquets.py` using Python 3 and only its standard library. The program independently enumerates each orientation of several small fixed cycle bouquets, tests the positive-indegree condition directly, enumerates all vertex subsets in increasing size, and checks total domination with bitwise in-neighborhood coverage. It compares the resulting exact orientation-by-minimum distribution with the polynomial prediction. Cases include length sequences `(3,)`, `(4,)`, `(3,3)`, `(3,4)`, `(4,4)`, `(3,5)`, `(3,3,3)`, and `(3,4,5)`. The last case checks all \(2^{12}=4096\) directed edge assignments on a ten-vertex graph. The stored output ends in `VERIFY_OK`. The symbolic proof, not finite enumeration, establishes the claim for all permitted lengths and numbers of petals.

## Relationship to prior work
Hansen, Lai, and Yue established the orientable *open* domination concept and several foundational bounds in 1999, under equivalent in-neighborhood terminology. They give examples such as a fan graph but not, in the inspected material, the orientation-distribution polynomial for bouquets of cycles. Anderson, Dravec, Johnston, and Kuenzel (first preprint 27 November 2023) use the same invariant as *orientable total domination*, determine it on unicyclic graphs and complete bipartite graphs, and pose the general intermediate-value realization question. A bouquet with at least two cycle petals is not unicyclic, and the formula above supplies every intermediate value together with its multiplicity. Blázsik and Nagy (first preprint 7 November 2024) classify graphs with upper orientable total domination number one below the order. That theorem covers scalar extremal consequences for two-petal bouquets, since then \(\operatorname{DOM}_t(B)=|V(B)|-1\); it does not state the full polynomial or the result for arbitrary numbers of petals.

## Limitations
The result covers only bouquets in which all cycle petals share exactly one common vertex; it is not a claim about arbitrary cactus graphs, arbitrary orientations with sources, or automorphism-orbit enumeration. Minimum total dominating sets themselves are not counted. The two-petal upper extremum and the one-petal cycle boundary connect to earlier results, and no novelty is claimed for those scalar special cases in isolation. Published-source searches and inspected primary texts cannot establish absolute uniqueness; earlier implicit block-decomposition arguments and incompletely inspected legacy texts remain possible overlap risks. No independent audit has been performed.

## References
1. S. E. Anderson, T. Dravec, D. Johnston, and K. Kuenzel, *Orientable total domination in graphs*, arXiv:2311.16307v1, posted 27 November 2023, https://arxiv.org/abs/2311.16307.
2. L. Hansen, Y.-L. Lai, and B. Q. Yue, *Orientable open domination of graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **29** (1999), 159–181, https://combinatorialpress.com/article/jcmcc/Volume%20029/vol-029-paper%2013.pdf.
3. Z. L. Blázsik and L. V. Nagy, *Characterization of graphs with orientable total domination number equal to \(|V|-1\)*, arXiv:2411.04560v1, posted 7 November 2024, https://arxiv.org/abs/2411.04560.
