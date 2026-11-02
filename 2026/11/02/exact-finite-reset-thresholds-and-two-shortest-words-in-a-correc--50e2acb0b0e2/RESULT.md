# Exact finite reset thresholds and two shortest words in a corrected Figure 3 automaton family

## Finding
For each integer \(3\le p\le15\), the corrected Figure 3 binary automaton \(A_p\) of Wang [1] has reset threshold
\[\operatorname{rt}(A_p)=3p^2+4p-1.\]
There are **exactly two** shortest reset words, namely
\[(ba)^p(ab)^{p-1}\,v\,(ba)^{p-2}\left(\prod_{j=2p-2}^{p}\bigl(a(ba)^j\bigr)\right)(ab)^p,\quad v\in\{aaaa,abba\},\]
The product is read in descending order, with \(j=2p-2,2p-3,\ldots,p\). Both words send all states to \(q_2\). The case \(v=aaaa\) is the explicit reset construction already established in [1]; the exact minimality for the thirteen parameter values and the complete two-word classification are the contributions here.

## Assumptions and scope
For integer \(p\ge3\), the state set is \(Q_p=\{q_0,\ldots,q_{3p-1}\}\), with alphabet \(\{a,b\}\). We use the **corrected** transition definition from Section 2 of [1], not the incomplete original diagram of [2]. In integer-index notation, initialize both transitions as the identity; letter \(a\) swaps \((2j-1,2j)\) for \(1\le j\le p-1\), then sends \(2p-1\mapsto2p\), \(2p\mapsto2p+1\), and \(2p+1\mapsto3\), and on indices \(2p+2,\ldots,3p-1\) swaps consecutive pairs beginning at \(2p+2\). Letter \(b\) swaps \((2j,2j+1)\) for \(0\le j\le p-1\), sends \(2p\mapsto2\), and swaps consecutive pairs among indices \(2p+1,\ldots,3p-1\) beginning at \(2p+1\). Any unmatched endpoint is fixed. Word actions read from left to right. The *reset threshold* is the minimum number of letters in a word whose image of the complete state set is a singleton. Distinct words are distinct strings over the fixed ordered alphabet; no identification under letter exchange or state relabeling occurs. Scope is **exactly** the finite range \(3\le p\le15\).

## Proof
Write \(\delta_x(S)=\{\delta_x(q):q\in S\}\) for \(x\in\{a,b\}\). Construct the directed *power automaton* with vertices nonempty subsets of \(Q_p\) and exactly two labeled edges \(S\to\delta_a(S)\) and \(S\to\delta_b(S)\). Every word corresponds to one labeled path from \(Q_p\); reset words correspond exactly to paths ending at a singleton. Breadth-first search therefore establishes the exact shortest reset length once the **entire** reachable breadth-first layer preceding the first singleton is processed. For each reached subset \(S\), store its minimum distance \(d(S)\) and the exact integer number \(c(S)\) of labeled paths of that distance. Initialize \(d(Q_p)=0,c(Q_p)=1\); for an edge \(S\xrightarrow{x}T\) with \(d(T)=d(S)+1\), add \(c(S)\) to \(c(T)\). The recurrence counts both letter choices separately even if they have the same subset image. Summing \(c(T)\) over all singleton targets at the first singleton depth gives exactly the total number of shortest words; prior levels have none. This is a complete finite-graph exhaustion, not a sample of words.

The standalone `forward_bfs.py` implements that recurrence. The independently written `reverse_bfs.cpp` instead starts from *all* singleton subsets, applies each letter's complete inverse-image map on subsets, and breadth-first searches toward \(Q_p\). The reverse-graph path count similarly equals the number of shortest reset strings. Its transition definition, direction of search, and graph construction are independent. Both exact enumerations return shortest length \(3p^2+4p-1\) and count two at every \(p\in\{3,\ldots,15\}\). Complete breadth-first searches visited the numbers of distinct subsets in the table below; all transitions and counting are deterministic integers.

For identification of the two words, `witness_checks.py` constructs the two strings in the displayed formula and checks directly from the supplied transition tables that both images are \(\{q_2\}\) with the listed length, for all thirteen values of \(p\). These words differ because `aaaa` and `abba` differ; since the exhaustive count is exactly two, they are the *entire* shortest-word set.

## Verification
| \(p\) | States | Shortest length | Forward subsets | Reverse subsets | Shortest words |
|---:|---:|---:|---:|---:|---:|
| 3 | 9 | 38 | 199 | 254 | 2 |
| 4 | 12 | 63 | 597 | 760 | 2 |
| 5 | 15 | 94 | 1,587 | 2,007 | 2 |
| 6 | 18 | 131 | 3,951 | 4,992 | 2 |
| 7 | 21 | 174 | 9,454 | 11,899 | 2 |
| 8 | 24 | 223 | 21,998 | 27,680 | 2 |
| 9 | 27 | 278 | 50,157 | 63,045 | 2 |
| 10 | 30 | 339 | 112,623 | 141,334 | 2 |
| 11 | 33 | 406 | 249,841 | 312,180 | 2 |
| 12 | 36 | 479 | 548,848 | 681,585 | 2 |
| 13 | 39 | 558 | 1,196,017 | 1,472,173 | 2 |
| 14 | 42 | 643 | 2,588,662 | 3,154,095 | 2 |
| 15 | 45 | 734 | 5,570,552 | 6,704,609 | 2 |

The machine-readable record `counts.csv` contains the same values. Reproduce the forward search with `python3 forward_bfs.py 15`, the reverse search with `g++ -O3 -std=c++17 reverse_bfs.cpp -o reverse_bfs && ./reverse_bfs 3 15`, and the explicit image checks with `python3 witness_checks.py`. The attached `verification_output.txt` records the completed runs. For \(p=15\), the two exact subset searches respectively reached \(5,570,552\) and \(6,704,609\) subsets. Neither search uses randomized sampling or partial-depth extrapolation.

## Relationship to prior work
Wang [1], arXiv version posted October 5, 2026, proves the specified-state compress-with-another threshold \(\mu(q_0)=4p\) for all \(p\ge3\) and establishes the **upper bound** \(\operatorname{rt}(A_p)\le3p^2+4p-1\) using one explicit reset word. It does **not** claim that this reset word is shortest, nor enumerate the shortest reset words. Szykuła [2] states the earlier related conjecture about a specified-state collision, not the complete reset threshold. The result here is a *finite exact sharpness/census theorem*, not an all-parameter sharpening of [1]. Other independent proofs of the distinct specified-state collision property have been announced; they are not assumed to settle shortest reset-word multiplicities.

## Limitations
The assertion covers \(3\le p\le15\) only; extending it to every \(p\ge3\) is unproved. Finite exhaustive searches do not give an infinite-parameter lower bound. State-label and transition conventions matter; this result cannot be transferred automatically to the earlier incomplete illustration. Published and unpublished equivalent enumerations may exist; independent priority audit has not occurred.

## References
[1] Q. Wang, *The compress-with-another threshold of Szykuła's Figure 3 family*, arXiv:2610.07044v1 (first publicly posted October 5, 2026), Sections 2, 4 and 5, https://arxiv.org/abs/2610.07044.

[2] M. Szykuła, *Synchronizing Automata: Open Problems*, EPTCS 451 (2026), 33–47; arXiv:2608.24245v1, Figure 3 and Conjecture 8, https://arxiv.org/abs/2608.24245.
