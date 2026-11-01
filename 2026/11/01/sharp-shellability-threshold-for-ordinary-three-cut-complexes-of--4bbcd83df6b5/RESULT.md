# Sharp shellability threshold for ordinary three-cut complexes of fourth-power cycles

## Finding
For every integer \(n\ge3\), let \(C_n^4\) be the fourth power of the cycle on \(\mathbb Z/n\mathbb Z\), with adjacency at cyclic distance at most four. Let \(\Delta_3(C_n^4)\) be the *ordinary* three-cut complex, whose facets are complements of three-vertex subsets inducing a disconnected subgraph. Then

\[
\boxed{\begin{array}{ll}
3\le n\le10 &: \Delta_3(C_n^4)\text{ is void},\\
11\le n\le16 &: \Delta_3(C_n^4)\text{ is nonvoid and nonshellable},\\
n\ge17 &: \Delta_3(C_n^4)\text{ is shellable}.
\end{array}}
\]

For all \(n\ge17\), its integral homotopy type is
\[
\boxed{\Delta_3(C_n^4)\simeq
\bigvee^{(n^2-17n+2)/2} S^{n-4}.}
\]
The **new finite step** is an explicit complete shelling for each of the four missing boundary cases \(n=17,18,19,20\). The infinite tail \(n\ge21\) is from Chauhan--Shukla (2026). The lower-range mod-two homology obstructions are independently reconstructed here; corresponding nonequivariant homology ranks appeared in Chauhan--Shukla--Vinayak (2024/2025).

## Assumptions and scope
Vertices are exactly \(\{0,\ldots,n-1\}\), with cyclic distance \(\min(|a-b|,n-|a-b|)\). The graph is simple. For any unordered triple \(T\), its complement \(F_T=V\setminus T\) is a facet precisely when \(G[T]\) is disconnected; every nonvoid complex is pure of dimension \(n-4\). Shellability means an ordering of its facets in which each new facet meets the union of the previous facets in a pure codimension-one subcomplex. The homology obstruction uses reduced homology with coefficients in \(\mathbb F_2\).

## Proof
**The void range.** For \(n\le9\), the fourth power of the cycle is complete, so no triple induces a disconnected subgraph. At \(n=10\), every vertex has exactly one nonneighbor (its antipode). A disconnected triple must contain an isolated vertex with two nonneighbors; this is impossible. Therefore the three-cut complex is void for \(3\le n\le10\).

**The nonshellable range.** For \(11\le n\le16\), exhaustive exact binary boundary reductions give the following nonzero *reduced* mod-two Betti numbers (all other reduced Betti numbers vanish):

| \(n\) | Facets | Degree \(d\) | \(\dim\widetilde H_d(-;\mathbb F_2)\) | Top simplex dimension |
|---:|---:|---:|---:|---:|
| 11 | 11 | 3 | 1 | 7 |
| 12 | 36 | 6 | 6 | 8 |
| 13 | 78 | 7 | 40 | 9 |
| 14 | 140 | 8 | 15 | 10 |
| 15 | 215 | 9 | 1 | 11 |
| 16 | 304 | 11 | 3 | 12 |

The included checker enumerates **all** \(\binom n3\) triples, builds every face of every complement facet, and computes every simplicial boundary rank over \(\mathbb F_2\) by exact integer-bit Gaussian elimination. Thus each asserted nonzero class is a finite, exhaustive computation, not a sample. A nonvoid pure shellable complex has reduced field homology only in its top dimension. Each displayed lower-dimensional group therefore obstructs shellability.

**Four boundary shellings.** Fix \(n\in\{17,18,19,20\}\). Every line of `cert_p4_n17.json`, `cert_p4_n18.json`, `cert_p4_n19.json`, or `cert_p4_n20.json`, respectively, is represented by one entry of the `triples` array, ordered as a proposed shelling of the *complement* facets. For a current missing triple \(T\), let \(\mathcal P\) be the earlier triples and set
\[
R(T)=\{x\in V\setminus T: \exists W\in\mathcal P\text{ with }W\setminus T=\{x\}\}.
\]
For every earlier triple \(U\), the standard pure-shelling facet-intersection criterion is equivalent to
\[
R(T)\cap(U\setminus T)\ne\varnothing.
\]
Indeed \(F_T\setminus F_U=U\setminus T\); an earlier facet \(F_W\) meets \(F_T\) along a ridge exactly when \(W\setminus T\) consists of one vertex, and \(F_T\cap F_U\subseteq F_T\cap F_W\) exactly when that vertex lies in \(U\setminus T\). Thus the preceding condition simultaneously checks every earlier facet intersection.

The verifier independently enumerates the entire disconnected-triple set using graph reachability; it checks that each proposed ordering has *each facet once*, then checks the displayed criterion at every step. Its results are

| \(n\) | Total facets, all checked | Spanning facets | Dimension |
|---:|---:|---:|---:|
| 17 | 408 | 1 | 13 |
| 18 | 528 | 10 | 14 |
| 19 | 665 | 20 | 15 |
| 20 | 820 | 31 | 16 |

A shellable pure complex is homotopy equivalent to a wedge of top-dimensional spheres, one for each spanning facet (the first facet contributes no sphere). For these four orders, a spanning facet occurs exactly when \(R(T)=V\setminus T\); the verifier counts them exhaustively. The four homotopy types therefore have respectively \(1,10,20,31\) spheres of dimensions \(13,14,15,16\).

**The infinite tail.** Theorem 1.4 of Chauhan--Shukla [1] proves shellability of \(\Delta_3(C_n^p)\) for every \(p\ge2\) and \(n\ge6p-3\), with \(\binom{n-2p}{2}-(2p^2+p-1)\) top spheres. Specializing to \(p=4\) covers every \(n\ge21\) with \(\binom{n-8}{2}-35=(n^2-17n+2)/2\) spheres. This agrees exactly with the four certified boundary counts and completes the classification.

## Verification
Place `verify.py` beside the four JSON certificate files and execute `python3 verify.py` using Python 3.8 or later. It uses only the standard library and exact integer arithmetic. It checks the empty range, all six mod-two boundary calculations, complete facet coverage and every shelling intersection for all four boundary orders, and their spanning-facet counts. The general \(n\ge21\) step invokes [1] as a published theorem; the finite checker does not purport to reprove it.

## Relationship to prior work
Chauhan--Shukla--Vinayak [2, Conjecture 4.2] conjectured a sharp transition at \(n=4p+1\) for ordinary three-cut complexes of powered cycles, and their Table 2 includes nonequivariant homology computations for the fourth-power cases. Those data **do not establish shellability**. Chauhan--Shukla [1, Theorem 1.4] subsequently proved shellability only for \(n\ge6p-3\); at \(p=4\) this begins at \(n=21\). The four new explicit shellings close precisely the remaining interval \(17\le n\le20\), and therefore prove the fourth-power case of the threshold conjecture. No newness is claimed for the previously published Betti-number table, for the already known infinite tail, or for the previously settled third-power case.

## Limitations
The result proves the sharp threshold for the **fourth** power only; it makes no claim for higher powers or for cut size other than three. Exact mod-two calculations establish non-shellability below threshold but not integral homotopy types there. The computational certificates are exhaustive for their stated finite ranges, not evidence for arbitrary parameters. Equivalent unindexed or unpublished shelling orders cannot be ruled out by the literature comparisons.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, first public 2026-03-24. Theorem 1.4 and Section 4. https://arxiv.org/abs/2603.23155
2. P. Chauhan, S. Shukla, and K. Vinayak, *Shellability of 3-cut complexes of squared cycle graphs*, arXiv:2406.01979, first public 2024-06-04. Table 2 and Conjecture 4.2. https://arxiv.org/abs/2406.01979
