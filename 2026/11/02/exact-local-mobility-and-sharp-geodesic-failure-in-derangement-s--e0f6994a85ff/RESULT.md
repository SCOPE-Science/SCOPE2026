# Exact local mobility and sharp geodesic failure in derangement switch graphs

## Finding
For an integer \(n\ge3\), let \(D_n\) be the set of fixed-point-free permutations of \([n]\). Form the graph \(X_n\) by joining two elements of \(D_n\) if their one-line notations differ by one swap of two positions. Equivalently, \(X_n\) is the four-cycle switch graph of perfect matchings of the crown graph \(K_{n,n}-M\). Let \(c_2(\pi)\) count the two-cycles in the disjoint-cycle decomposition of \(\pi\), and put \(b_n=\binom n2-n\).

**Theorem (a connected but non-geodesic switch family with exact degrees).** The graph \(X_3\) consists of two isolated vertices; \(X_n\) is connected for every \(n\ge4\). Its entire degree distribution is
\[
\deg_{X_n}(\pi)=b_n+c_2(\pi),\qquad
P_n(u):=\sum_{\pi\in D_n}u^{\deg_{X_n}(\pi)}
=u^{b_n}n![z^n]\frac{\exp(-z+(u-1)z^2/2)}{1-z}.
\]
If \(!n=|D_n|\) and \(!0=1\), then
\[
2|E(X_n)|=b_n\,!n+\binom n2\,!(n-2).
\]
When \(X_n\) is regarded as the induced subgraph of the full-transposition Cayley graph of \(S_n\), the inclusion is **isometric exactly for \(n=4\)** among connected members \(n\ge4\). For every \(n\ge5\), some two vertices have unrestricted transposition distance \(2\) but distance exactly \(4\) in \(X_n\). Every \(X_n\), \(n\ge3\), has no Hamiltonian path; the latter is a standard parity consequence included for context, not the principal novelty claim.

## Assumptions and scope
All permutations are bijections of the finite labelled set \([n]\). A graph edge means one legal exchange of exactly two one-line entries; self-loops and unsuccessful swaps are excluded. The unrestricted ambient transposition metric is the ordinary Cayley distance \(d_S(\pi,\sigma)=n-c(\sigma^{-1}\pi)\), where \(c\) counts all cycles including fixed points. Distances inside disconnected \(X_3\) are not compared with ambient distances. The coefficient notation \([z^n]\) is formal; all factorial expressions are exact integers. No claim is made that the maximal metric excess across all pairs has been determined for arbitrary \(n\).

## Proof
**Legal swaps and degrees.** A position swap \(i\leftrightarrow j\) creates a fixed point precisely when \(\pi(i)=j\) or \(\pi(j)=i\). There are \(n\) directed arcs in the cycle digraph of \(\pi\), and forgetting direction identifies two arcs as one forbidden unordered position pair precisely for each two-cycle. Thus exactly \(n-c_2(\pi)\) of the \(\binom n2\) swaps are illegal. This proves the degree formula.

**Complete degree law.** The exponential formula for permutations with no one-cycles and with each two-cycle marked by \(u\) gives
\[
\sum_{n\ge0}\frac{z^n}{n!}\sum_{\pi\in D_n}u^{c_2(\pi)}
=\exp\left(\frac{uz^2}{2}+\sum_{j\ge3}\frac{z^j}{j}\right)
=\frac{\exp(-z+(u-1)z^2/2)}{1-z}.
\]
Multiplying the degree enumerator at rank \(n\) by \(u^{b_n}\) proves the second formula. Double-counting (permutation, designated two-cycle) gives \(\sum_{\pi\in D_n}c_2(\pi)=\binom n2\,!(n-2)\), and the edge formula follows by the handshake lemma.

**Connectivity.** Swapping positions in one cycle of length \(k\ge4\) at cyclic separation two splits it into a two-cycle and a \((k-2)\)-cycle. All resulting cycles have length at least two, so the swap is legal. Swapping positions in different cycles joins them, again creating no fixed points. Repeating the first operation and joining pairs of three-cycles into six-cycles shows that every derangement is connected to a product of two-cycles if \(n\) is even, or to a product consisting of exactly one three-cycle and otherwise two-cycles if \(n\) is odd. The local graph \(X_4\) connects the three pairings of four labels, as can also be checked directly from its nine states. Thus all products of two-cycles are connected through four-label operations. The local graph \(X_5\) on 44 derangements is connected, by exhaustive generation of all 44 states and all allowed swaps using `verify_primary.py` and independently `verify_alt.cpp`; no probabilistic assumption is used. In odd order, applying this five-label connectivity on the unique three-cycle and any outside two-cycle permits replacement of any one label of the three-cycle by any label in an outside pair, with a new two-cycle on the remaining labels, and permits reversal of the three-cycle orientation. Such replacements connect all choices of three-cycle support because the graph of three-subsets under single-element exchange is connected. Four-label operations connect all pairings of the complement. Hence the odd-order normal forms are connected for all \(n\ge5\). The two three-cycles in \(D_3\) have no legal swaps, proving the exceptional case.

**Sharp isometric threshold.** At \(n=4\), the even derangements are the three double transpositions, and the odd derangements are the six four-cycles. Each four-cycle has exactly two neighbors among the three even states, and each even state has four neighbors. Two distinct four-cycles therefore share an even neighbor, and two distinct even states share an odd neighbor. Their constrained and ambient distances both equal two. An odd-even pair is either adjacent in both graphs (distance one) or at distance three in both (the ambient distance is odd and at most three, and the connected bipartite graph \(X_4\) has an alternating three-edge walk between such a pair). Thus \(X_4\) is isometric.

For \(n=5\), start at the derangement \(\pi=(12)(345)\) and end at \(\sigma=(12)(354)\). An exact four-swap path (using positions indexed from one) is
\[
(2,1,4,5,3)\xrightarrow{(1,3)}(4,1,2,5,3)
\xrightarrow{(1,5)}(3,1,2,5,4)
\xrightarrow{(1,4)}(5,1,2,3,4)
\xrightarrow{(1,3)}(2,1,5,3,4).
\]
For \(n=6\), use \(\pi=(123)(456)\) and \(\sigma=(132)(456)\) and the path
\[
(2,3,1,5,6,4)\xrightarrow{(1,4)}(5,3,1,2,6,4)
\xrightarrow{(1,2)}(3,5,1,2,6,4)
\xrightarrow{(2,3)}(3,1,5,2,6,4)
\xrightarrow{(3,4)}(3,1,2,5,6,4).
\]
All intermediate lists are derangements. Each endpoint pair differs by one reversed three-cycle, so ambient distance is two. Any expression of that relative three-cycle as two transpositions must use positions entirely within its three-letter support. The first such swap splits a three-cycle into a fixed point and a two-cycle, so no legal two-edge path exists. Both graphs are bipartite by sign, ruling out odd path lengths. The displayed paths therefore have constrained distance exactly four. For every \(n\ge7\), extend the five-letter pair by the same fixed-point-free permutation on the remaining \(n-5\ge2\) labels. The four-step witness remains valid, and the same two-step obstruction persists: a minimum-length ambient transposition factorization cannot involve letters outside the differing three-letter support. Therefore no connected member \(X_n\) for \(n\ge5\) is isometric.

**Parity obstruction (context).** Every switch reverses sign, while the determinant expansion of the off-diagonal all-ones matrix gives
\[
\sum_{\pi\in D_n}\operatorname{sgn}(\pi)=\det(J_n-I_n)=(-1)^{n-1}(n-1).
\]
A bipartite Hamiltonian path would alternate between parts whose sizes differ by at most one. Their actual imbalance is \(n-1\ge2\), so no Hamiltonian path exists. The classical parity observation is not presented as an independent novelty claim.

## Verification
`verify_primary.py` exhaustively enumerates \(D_n\) for \(3\le n\le8\), constructs each legal switch, and verifies connectivity, degrees, the labelled edge count, and an independently derived cycle-count coefficient formula. It tests all pairs for isometry at \(n=4\) and both explicit four-step exceptional pairs. `verify_alt.cpp` independently enumerates derangements through the next-permutation algorithm, constructs four-cycle switches by forbidden-diagonal tests, verifies degree counts from cycle decompositions, checks connectivity, and independently checks the same distance facts. Both implementations are standalone and require no network calls. Finite checks corroborate—but do not replace—the general algebraic and reduction arguments.

## Relationship to prior work
The perfect-matching switch Markov chain and its transposition interpretation were explicitly formulated by Diaconis, Graham and Holmes and studied in detail by Dyer, Jerrum and Müller (arXiv:1501.07725, first posted 2015-01-30); that paper establishes hereditary-class ergodicity criteria and some general diameter bounds, not the crown-family degree polynomial or its sharp isometry threshold. Baril and Vajnovszki (2004) construct Gray codes for derangements using transitions that may be a rotation or multiple transpositions, while Korsh and LaFollette (2004) allow a rotation of three elements. Those results are not transposition-only geodesics in \(X_n\). Mütze's 2023 survey explicitly distinguishes these operations. The complete transposition Cayley metric is classical and supplies the ambient comparison; its distance formula is not new. The general perfect-matching flip-graph results for complete bipartite graphs do not directly cover the crown graph, whose missing diagonal edges impose the essential restrictions.

## Limitations
The argument does not compute the full pair-distance distribution, precise diameter, worst-case metric distortion, mixing time, spectral gap, or shortest-path counts for arbitrary \(n\). The value claim concerns a natural transition family, its exact local mobility and a sharp geometric boundary; it does not assert that standard permutation-exponential-formula techniques or signed derangement enumerations are newly discovered. Literature overlap remains a risk, particularly in older matching-switch literature and unpublished derangement reconfiguration notes. Scientific originality has not been independently adjudicated.

## References
- M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725 (first public preprint 2015-01-30); subsequent J. ACM 64 (2017), article 12.
- J.-L. Baril and V. Vajnovszki, *Gray code for derangements*, Discrete Applied Mathematics 140 (2004), 207–221; doi:10.1016/j.dam.2003.06.002.
- J. F. Korsh and P. S. LaFollette, *Constant time generation of derangements*, Information Processing Letters 90 (2004), 181–186.
- T. Mütze, *Combinatorial Gray codes—an updated survey*, Electronic Journal of Combinatorics 30 (2023), #DS26.
