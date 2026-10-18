# Exact optimal strong-odd-coloring counts for generalized windmill graphs

## Finding

Let \(r\ge 2\) and \(t\ge1\) be integers, and let \(W_{r,t}=K_1\vee(tK_r)\) denote the graph formed from \(t\) disjoint cliques of order \(r\) by joining every vertex to one common hub. A **strong odd coloring** is a proper vertex coloring in which, at each vertex, every color occurring in its open neighborhood occurs an odd number of times. Write \(\chi_{\mathrm{so}}(W_{r,t})\) for the minimum number of colors.

Define
\[
p(r,t)=\begin{cases}
r,&t\text{ odd},\\
2\left\lceil\dfrac{rt}{2(t-1)}\right\rceil,&t\text{ even}.
\end{cases}
\]
Then \(\chi_{\mathrm{so}}(W_{r,t})=p(r,t)+1\).

**New counting and structural assertion.** Every optimal coloring uses all \(p+1\) colors. After choosing the hub color, its restriction to each labeled clique is a permutation of an \(r\)-element subset \(S_i\) of the other \(p\) colors; the optimal colorings correspond exactly to ordered choices \(S_1,\ldots,S_t\) in which **each of the \(p\) colors belongs to an odd number of sets**. Consequently the exact number of optimal functions from the labeled vertex set to a fixed named palette of \(p+1\) colors is
\[
N_{r,t}=\frac{(p+1)(r!)^t}{2^p}\sum_{j=0}^{p}(-1)^j\binom pj
\left(\sum_{h=0}^{r}(-1)^h\binom jh\binom{p-j}{r-h}\right)^t,
\qquad p=p(r,t),
\]
where out-of-range binomial coefficients equal zero. In particular, if \(t\) is odd, then \(N_{r,t}=(r+1)(r!)^t\); if \(t=2\), then \(N_{r,2}=(2r+1)!\).

## Assumptions and scope

All graphs are finite and simple. Each of the \(t\) clique blocks and each vertex within a block is labeled; colors are also named, and two colorings related by permutation of colors or graph automorphism count as distinct functions. The count is for **exactly the minimum-size palette**, not for colorings with arbitrary surplus colors. The cases \(r=2\) (friendship graphs), odd and even \(t\), and \(t=1\) are included; no claim is made about arbitrary block graphs or unequal clique block sizes.

## Proof

**1. Reduction to a parity incidence system.** In any proper coloring, the hub has a color absent from every clique. Every clique contains \(r\) vertices mutually adjacent, so its colors are distinct. For any nonhub vertex, all its neighbors (the hub and the other \(r-1\) vertices of its own clique) have pairwise distinct colors; its strong-odd condition is therefore automatic. At the hub, the condition is exactly that every color appearing among the \(rt\) clique vertices appears an odd number of times. Let \(p\) denote their number of distinct colors. The chosen sets \(S_i\) have size \(r\), and all column multiplicities \(c_j=|\{i:j\in S_i\}|\) are odd.

**2. Minimum palette.** Necessarily \(p\ge r\). If \(t\) is odd, using the same \(r\) colors once per clique makes each color appear \(t\) times, so \(p=r\) is attained. If \(t\) is even, each positive odd multiplicity satisfies \(1\le c_j\le t-1\); hence \(rt=\sum_jc_j\le p(t-1)\). Since \(rt\) is even and the sum of \(p\) odd integers has parity \(p\), \(p\) must be even. Thus \(p\ge 2\lceil rt/(2(t-1))\rceil\).

To attain this value, set \(p=2\lceil rt/(2(t-1))\rceil\). It is even and satisfies \(p\le rt\le p(t-1)\). Begin with \(p\) odd multiplicities \(c_j=1\) and distribute the remaining even increment \(rt-p\) among them in steps of two, never exceeding \(t-1\). This is possible because \(0\le rt-p\le p(t-2)\), and the bounds are even. Now list color \(j\) consecutively \(c_j\) times in a word of length \(rt\). Assign consecutive positions of this word cyclically to clique blocks \(0,1,\ldots,t-1,0,1,\ldots\). Each block receives exactly \(r\) positions since the word has \(rt\) positions. Every color block has length \(c_j\le t-1\), so no single clique receives any color twice. This produces the requisite proper coloring and proves equality.

**3. Classification and enumeration.** All colorings at the minimum number \(p+1\) are precisely the parity-incidence systems from step 1: the reduction is necessary, and any such system with arbitrary ordering of the \(r\) colors inside each clique gives a strong odd coloring by the neighborhood argument.

For a fixed named palette \([p]\) of nonhub colors, denote by \(T_{r,t,p}\) the number of ordered \(t\)-tuples of \(r\)-subsets for which each color occurs an odd number of times. A product of parity-character indicators gives
\[
T_{r,t,p}=2^{-p}\sum_{A\subseteq[p]}(-1)^{|A|}
\left(\sum_{S\subseteq[p],\,|S|=r}(-1)^{|A\cap S|}\right)^t.
\]
If \(|A|=j\), the inner sum equals \(\sum_h(-1)^h\binom jh\binom{p-j}{r-h}\). Grouping by \(j\) yields the displayed finite-sum formula. Each choice of hub color has \(p+1\) options and each unordered clique color set has exactly \(r!\) orderings, independently in each of the \(t\) labeled cliques. Thus \(N_{r,t}=(p+1)(r!)^tT_{r,t,p}\).

For odd \(t\), the minimum \(p=r\) forces each clique to use all \(r\) colors, giving \(T_{r,t,r}=1\). When \(t=2\), the minimum \(p=2r\) forces each color to appear in exactly one clique; the two \(r\)-sets are complementary. There are \(\binom{2r}r\) ordered choices, giving \(N_{r,2}=(2r+1)!\). This completes the proof.

## Verification

The standalone program `verify_windmill.py` independently computes the minimum palette by an exhaustive XOR dynamic program over all \(r\)-subsets of every candidate palette (for the listed small ranges), computes the parity-character finite sum separately, and compares exact integer counts. It also explicitly constructs optimal colorings via the cyclic assignment and checks both properness and every vertex's neighborhood parity. The recorded output `verification_output.txt` reports 32 successful exact small profiles; these finite checks corroborate but do not replace the infinite proof.

## Relationship to prior work

Kwon and Park introduced the strong odd chromatic parameter (arXiv:2401.11653, originally posted 22 January 2024) and proved general sparse-graph bounds. Caro, Petruševski, Škrekovski, and Tuza (arXiv:2410.02336, originally posted 3 October 2024) established tree/unicyclic, planar, and graph-product results; their graph-product upper bounds do not specialize to a counting formula for the one-vertex join \(K_1\vee tK_r\). A subsequent paper of Pradhan, Sharma, and Verma (arXiv:2610.01441, first posted 1 October 2026) states in its accessible abstract that an optimal strong odd coloring of a general block graph can be computed in linear time. It is pertinent to the numerical chromatic-number component, but its accessible abstract does not enumerate all optimal named colorings. Its full text was unavailable for this comparison, and possible overlap remains a bibliographic risk. The distinctive assertion here is the complete structural and enumerative classification, not an algorithm for finding a single optimal coloring.

## Limitations

This is a theorem for equal-order clique blocks sharing exactly one hub. The counting formula is a finite character sum, not a simplified product in the even-block case. It counts named colors and labeled vertices; it does not classify orbits under automorphisms. The related 2026 block-graph paper could not be inspected in full; absence of a discovered enumeration is not a proof of priority. Independent review is not supplied. No computational experiment is asserted to prove the formula for all parameter values.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first public version 2024-01-22), https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (first public version 2024-10-03), https://arxiv.org/abs/2410.02336.
3. D. Pradhan, V. Sharma, and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441 (first public version 2026-10-01), https://arxiv.org/abs/2610.01441; full text not accessed.
