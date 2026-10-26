# The exact minimum maximal total-visibility census in the eight-cube

## Finding

Let \(Q_8\) have vertex set \(\{0,1\}^8\), with adjacent words differing in exactly one coordinate. A set \(X\) is *total mutual-visible* when for every ordered pair \(u,v\) of cube vertices, some shortest \(u,v\)-path has all internal vertices outside \(X\). It is *maximal* when no vertex can be added while preserving that property. The lower total mutual-visibility number is the smallest size of such an inclusion-maximal set.

**Theorem.** The lower total mutual-visibility number is
\[
\mu_{\mathrm t}^{-}(Q_8)=16.
\]
There are exactly **5,189,648,486,400** distinct labeled inclusion-maximal total mutual-visibility sets of this minimum size. Equivalently, each of the even- and odd-parity halves of the cube admits exactly **2,278,080** inclusion-maximal distance-two-avoiding eight-subsets; a minimum total mutual-visibility set is an independent choice of one from each half.

## Assumptions and scope

All graphs are finite, simple, and labeled by the binary coordinates. Distance is ordinary Hamming distance \(d_H\). Let \(E\) be the 128 even-weight words and \(O\) the 128 odd-weight words. The *halved cube* \(H_8\) has vertex set \(E\), with adjacency exactly when \(d_H=2\); its odd translate is isomorphic. For a graph \(H\), an independent dominating set is an independent set that dominates every vertex, equivalently an inclusion-maximal independent set. The theorem is restricted to dimension eight and does not claim a formula in general dimension.

## Proof

**Step 1 (reduction).** Bujtás, Klavžar and Tian (2023, Theorem 6) prove for every Hamming graph that \(X\) is a total mutual-visibility set if and only if it contains no pair at Hamming distance two. In \(Q_8\), every distance-two pair lies within the same parity class. Thus total mutual-visibility sets are exactly independent sets of the disjoint union of the two distance-two graphs on \(E\) and \(O\). Such a set is inclusion-maximal if and only if both restrictions are independent dominating sets. Therefore the lower number is twice \(i(H_8)\), and the number of smallest maximal sets is the square of the number of minimum independent dominating sets of \(H_8\).

**Step 2 (complete finite certificate for one parity).** Binary XOR translations by even words act transitively on \(E\), preserving distance and independent domination. Consequently every nonempty independent dominating set of \(H_8\) can be translated to a set containing the word \(0\). The embedded file `enumerate.cpp` uses this normalization to test *every* unordered set \(\{0,v_2,\ldots,v_k\}\) whose nonzero words are taken in strictly increasing integer order and whose pairwise distances are at least four. The 128 even words are enumerated in increasing integer order. For each selected word \(v\), a two-word 128-bit mask stores exactly the even words at distances zero or two from \(v\). The bitwise union of all these masks is all ones if and only if the selected set dominates \(H_8\). No candidates are skipped: the recursion tries every larger index, rejecting only pairs at distance two (equivalently, accepting Hamming distances four, six or eight).

The verified leaf counts, indexed by the total set size \(k\), are:

| \(k\) | Independent anchored candidates | Independently dominating anchored candidates |
|---:|---:|---:|
| 5 | 611,100 | 0 |
| 6 | 2,984,625 | 0 |
| 7 | 7,490,595 | 0 |
| 8 | 9,234,285 | 142,380 |

Every closed neighborhood has \(1+\binom82=29\) vertices. Thus a dominating set cannot have at most four vertices, because \(4\cdot29<128\). The exhaustive rows exclude sizes five, six and seven, and the positive eight row establishes \(i(H_8)=8\). Independently, an explicit witness is the even-weight code
\[
\{0,15,51,60,85,154,225,238\},
\]
where integers encode eight-bit words. The file `verify.py` checks directly that its pairwise distances are at least four and that it covers all 128 even words at radius two.

**Step 3 (unanchoring and two parities).** Let \(a=142,380\) count eight-element independent dominating sets containing zero. Each of the 128 vertices belongs to exactly \(a\) such sets, by even XOR transitivity. Double-counting incidences between vertices and all eight-element independent dominating sets yields exactly \(128a/8=2,278,080\) sets in one parity. The odd parity graph is an isomorphic translate. Hence a smallest maximal total mutual-visibility set has eight vertices in each parity and is counted by
\[
(2,278,080)^2=5,189,648,486,400.
\]
This proves both assertions.

## Verification

Compile and run `enumerate.cpp` with a standard C++17 compiler, for example `g++ -std=c++17 -O2 -Wall -Wextra -pedantic enumerate.cpp -o enumerate && ./enumerate`. It performs a complete finite search, asserts the exact candidate and domination counts for each \(k\in\{5,6,7,8\}\), and prints `VERIFY_OK`. Its distance-six auxiliary profile reports three degree-component profiles of the anchored eight-sets, with frequencies 80,640, 11,340, and 50,400, summing to 142,380. These are profile types, not a claimed graph-isomorphism classification. Run `python3 verify.py` to independently check the explicit 16-point total-visibility witness against all pairs of cube vertices by breadth-first search and to check inclusion-maximality. Both programs are self-contained; their exact source bytes accompany this manuscript.

## Relationship to prior work

Brešar and Yero (2023) introduce the *lower* total mutual-visibility number and explicitly pose its determination on hypercubes in Problem 1. Bujtás, Klavžar and Tian (2023) provide the distance-two characterization used in Step 1, but not this dimension-eight minimal-maximal census. Korže and Vesel (2024) compute the *upper* total mutual-visibility number for small hypercubes; their table gives \(\mu_{\mathrm t}(Q_8)=32\), an extremal maximum, not the lower number 16. Independent domination of \(H_8\) is stronger than ordinary domination: the published ordinary domination number of the eight-halved cube is seven, with 71,680 ordinary minimum dominating sets in OEIS A323447 (2025 extension). Neither ordinary-domination datum determines the independent-domination minimum or its census. The usual covering-code benchmark \(K(8,2)=12\) covers *all* 256 words with radius-two balls and does not imply the same-parity independent-domination statement.

## Limitations

This is an exact **finite** dimension-eight result, with a fully specified exhaustive-search certificate, not a symbolic formula for arbitrary hypercube dimension. The proof of its count depends on faithful implementation and execution of the supplied enumeration; the separately programmed shortest-path witness check is not itself a proof of the counting exhaustiveness. Indexed and accessible primary papers and numerical tables were compared, but an unindexed prior census of independent dominating sets of the halved eight-cube might still exist. No independent external scientific audit is claimed.

## References

1. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951 (first posted 2023-07-06), especially Problem 1. https://arxiv.org/abs/2307.02951
2. C. Bujtás, S. Klavžar and J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168 (first posted 2023-07-11), especially Theorem 6. https://arxiv.org/abs/2307.05168
3. D. Korže and A. Vesel, *Variety of mutual-visibility problems in hypercubes*, arXiv:2405.05650 (first posted 2024-05-09), especially the hypercube total-visibility values. https://arxiv.org/abs/2405.05650
4. OEIS A323447, *Number of minimum dominating sets in the n-halved cube graph* (eight-dimensional term extended 2025-03-23). https://oeis.org/A323447
5. U. Blass and S. Litsyn, *The smallest covering code of length 8 and radius 2 has 12 words*, Ars Combinatoria **52** (1999), 309–318. https://combinatorialpress.com/ars-articles/volume-052-ars-articles/the-smallest-covering-code-of-length-8-and-radius-2-has-12-words/
