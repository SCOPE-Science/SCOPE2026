# An exact linear derangement-swap detour between inverse triangle products

## Finding

**Theorem.** For each integer \(k\ge 2\), set \(n=3k\), and let \(H_n\) be the crown graph obtained from the complete bipartite graph on two ordered copies of \([n]\) by deleting its \(n\) diagonal edges. Identify each perfect matching with a fixed-point-free permutation \(\pi\in S_n\) through the matched pairs \((i,\pi(i))\). Define

\[
\sigma_k=(1\ 2\ 3)(4\ 5\ 6)\cdots(3k-2\ 3k-1\ 3k),\qquad \tau_k=\sigma_k^{-1}.
\]

Two perfect matchings are adjacent when their symmetric difference is exactly one alternating four-cycle in \(H_n\), equivalently when their permutation words differ by one transposition that leaves both words fixed-point-free. The exact shortest-path distance is

\[
\boxed{d_{H_{3k}}(M_{\sigma_k},M_{\tau_k})=2k+2\lceil k/2\rceil
=\begin{cases}3k,&k\text{ even},\\3k+1,&k\text{ odd}.\end{cases}}
\]

The unrestricted transposition distance between the same endpoints is \(2k\). Thus forbidding fixed points forces exactly \(2\lceil k/2\rceil\) extra switches; this gap is unbounded and asymptotically linear in \(n\). At the boundary \(k=1\), the two inverse three-cycles are isolated vertices in the derangement-swap graph, so no finite distance exists.

## Assumptions and scope

The graph is simple and bipartite. A state is a **perfect** matching of \(H_n\), not an arbitrary matching. The only allowed move is the symmetric difference with an alternating four-cycle, so each intermediate state must remain a perfect matching of \(H_n\). In permutation coordinates a move swaps entries in positions \(i\ne j\). It is legal precisely when \(\pi(i)\ne j\) and \(\pi(j)\ne i\); these are exactly the two cross-edges not deleted from \(H_n\). All positions and values use \([n]=\{1,\dots,n\}\). The theorem assumes \(k\ge 2\); no assertion about arbitrary pairs of derangements or all reconfiguration distances is made.

## Proof

**Step 1: a cycle-splitting bound.** Fix the target \(\tau=\tau_k\). Given a current derangement \(\pi\), define its relative permutation \(R=\pi^{-1}\circ\tau\). A swap at positions \(i,j\) changes \(\pi\) to \(\pi'=\pi\circ(i\ j)\), hence \(R'=(i\ j)\circ R\). Left multiplication by a transposition either splits one cycle of \(R\) into two (increases its number of cycles by one) or merges two cycles (decreases it by one). Since \(\sigma_k\) has order three, initially \(R=\sigma_k^{-1}\tau_k=\sigma_k\), consisting of \(k\) separate three-cycles, whereas at the target \(R=\mathrm{id}\), which has \(3k\) cycles. If a legal path uses \(s\) splitting moves and \(m\) merging moves, then

\[
s-m=3k-k=2k,\qquad \text{length}=s+m=2k+2m.
\]

**Step 2: an unavoidable first merger for each block.** Let \(B_a=\{3a+1,3a+2,3a+3\}\) for \(0\le a<k\). Call \(B_a\) untouched until a swap uses a position in \(B_a\). Before its first use, \(\pi\) restricted to \(B_a\) is still the initial forward three-cycle, and \(\pi(B_a)=B_a\); the target \(\tau\) also preserves \(B_a\). Therefore the relative permutation \(R\) preserves \(B_a\), and its restriction there is a three-cycle, separate from all cycles supported outside \(B_a\).

The first swap touching \(B_a\) cannot use two positions of \(B_a\): exchanging any two images in a three-cycle creates a fixed point, making the swap illegal. Thus it must be a cross-block swap \((i\ j)\) with \(i\in B_a\) and \(j\notin B_a\). These two positions belong to different cycles of \(R\), so the swap is a **merger**. A single merger can make at most two previously untouched blocks touched. Since all \(k\) blocks must eventually be touched (the target reverses each three-cycle), it follows that

\[
m\ge\lceil k/2\rceil.
\]

Together with Step 1, every legal path has at least \(2k+2\lceil k/2\rceil\) switches.

**Step 3: matching constructions.** For two consecutive three-cycle blocks, translate the following ordered list of swaps to those six labels:

```text
(1,4) (1,2) (2,3) (3,6) (3,5) (3,4)
```

Starting with \((1\ 2\ 3)(4\ 5\ 6)\), this six-move sequence gives \((1\ 3\ 2)(4\ 6\ 5)\); after *each* move the permutation has no fixed point. For three consecutive blocks, the following ten-move sequence likewise reverses all three cycles while avoiding fixed points throughout:

```text
(1,4) (1,2) (1,7) (1,9) (1,8)
(1,7) (2,3) (3,6) (3,5) (3,4)
```

The legality and endpoints of both finite templates are checked explicitly by `verify_crown_geodesic.py`; they are also easily confirmed by hand. If \(k\) is even, partition the \(k\) blocks into \(k/2\) pairs and independently execute the six-move template on each pair, obtaining \(3k\) switches. If \(k\ge3\) is odd, execute the ten-move template on three blocks and pair the remaining \(k-3\) blocks, obtaining \(10+3(k-3)=3k+1\) switches. Since the templates use disjoint labels, performing them successively preserves their legality. These upper bounds coincide with Step 2. This proves the theorem.

**Boundary.** For \(k=1\), only two derangements of three letters exist. They are the two inverse three-cycles, each without legal transpositions, so they lie in different components. \(\square\)

## Verification

The standalone standard-library programs `verify_crown_geodesic.py` and `verify_crown_exhaustive.py` are included with this result. Run both as:

```sh
python verify_crown_geodesic.py
python verify_crown_exhaustive.py
```

The constructive checker applies the two universal local templates on disjoint blocks for every \(2\le k\le30\). It checks each intermediate permutation is a derangement, its endpoint is the inverse, and its relative-cycle merger/splitting totals attain the bound. The independent checker constructs crown perfect matchings directly, enumerates the graph exhaustively at sizes \(n=3,4,5,6,9\), and uses breadth-first search to certify distance \(6\) at \(n=6\) and \(10\) at \(n=9\); these graphs have respectively \(265\) and \(133496\) states. The small checks corroborate—but do not replace—the proof for every \(k\ge2\).

## Relationship to prior work

Diaconis, Graham and Holmes study permutations with forbidden positions and the switching Markov chain, including connectivity of the derangement-swap graph for \(n\ge4\) and failure at \(n=3\). Jain explicitly studies the same derangement-transposition graph under the name \(\alpha(n)\), obtaining degree and connectivity properties and a shortest spanning walk. Dyer, Jerrum and Müller analyze perfect-matching switch chains for graph families; their chordal-bipartite diameter bounds do not give this crown-graph pair distance. Sun and Wang study derangement polynomials and group actions, providing a dated combinatorial antecedent with classification \(05A15\), but not shortest switching distances. None of these inspected statements yields the present exact inverse-three-cycle distance or the unbounded difference from the ambient transposition metric. The identification of the state graph and its ordinary connectivity are prior art and are not novel claims here.

## Limitations

The formula applies specifically to the displayed inverse products of disjoint three-cycles, not to all pairs of permutations. It does not determine the diameter, distribution of distances, mixing time, or complexity of shortest paths in the entire derangement-swap graph. An exact equivalent formula may exist in less accessible or differently indexed literature; the bibliographic comparison is not a proof of originality. Exhaustive computation has been performed only at finite sizes; the arbitrary-size conclusion relies on the written proof and the fixed local templates. Independent external scientific validation has not been performed.

## References

1. P. Diaconis, R. Graham and S. P. Holmes, *Statistical Problems Involving Permutations with Restricted Positions*, full text at https://fanchung.ucsd.edu/ron/papers/01_07_permutations.pdf, especially the discussion of derangements and transposition connectivity on p. 17.
2. H. Sun and Y. Wang, *A Group Action on Derangements*, *Electronic Journal of Combinatorics* **21** (2014), P1.67. Published 2014-03-24; DOI https://doi.org/10.37236/3723. Primary classification on article: 05A15.
3. M. Dyer, M. Jerrum and H. Müller, *On the Switch Markov Chain for Perfect Matchings*, arXiv:1501.07725, https://arxiv.org/abs/1501.07725 (first posted 2015-01-30).
4. P. Jain, *Transpositions in Derangements* (2021), https://www.researchgate.net/publication/354533290_Transpositions_in_Derangements, DOI https://doi.org/10.13140/RG.2.2.35817.42088.
