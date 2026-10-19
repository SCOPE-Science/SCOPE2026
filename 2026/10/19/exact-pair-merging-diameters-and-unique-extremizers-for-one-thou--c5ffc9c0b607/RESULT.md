# Exact pair-merging diameters and unique extremizers for one thousand Dżyga–Szykuła automata

## Finding
For every integer \(1\le k\le1000\), let \(A_k\) be the \(3k+6\)-state, two-letter automaton defined below. Let \(d_k(p,q)\) be the least length of a word mapping states \(q_p\) and \(q_q\) to the same state. Then every pair is mergeable, and its **exact pairwise merging diameter** is
\[
\max_{0\le p<q\le3k+5}d_k(p,q)=D(k):=
\begin{cases}
(5k^2+32k+47)/4,&k\text{ odd},\\
(5k^2+34k+44)/4,&k\text{ even}.
\end{cases}
\]
Moreover, the maximum is achieved by **exactly one unordered pair**:
\[
\{q_h,q_{h+1}\},\qquad h=\left\lfloor\frac{k+2}{2}\right\rfloor.
\]
At \(k=1000\), the automaton has \(3006\) states, the exact diameter is \(1{,}258{,}511\), and the unique maximizing pair is \(\{q_{501},q_{502}\}\).

This is a **finite, exhaustively certified theorem for \(k\le1000\)**, not a proof of the displayed formula or the unique-extremizer assertion for arbitrary \(k\). It verifies the diameter conjecture for an additional \(984\) parameters beyond the published proved range \(k\le16\).

## Assumptions and scope
The state set is \(Q_k=\{q_0,\ldots,q_{n-1}\}\), where \(n=3k+6\); letters \(a,b\) act as follows, with all indices zero-based. For \(i=0\), \(a(0)=0\) and \(b(0)=1\). For \(1\le i\le2k+3\), \(a(i)=i+1\) for odd \(i\), and \(a(i)=i-1\) for even \(i\); while \(b(i)=i-1\) for odd \(i\), and \(b(i)=i+1\) for even \(i\). At the junction \(i=2k+4\), \(a(i)=i+1\), \(b(i)=2\); at \(i=2k+5\), \(a(i)=3\), \(b(i)=i+1\). For \(2k+6\le i\le n-2\), \(a(i)=i+1\) when \(i\) is even and \(i-1\) otherwise; \(b(i)=i+1\) when \(i\) is odd and \(i-1\) otherwise. At the final index \(i=n-1\), if \(i\) is even then \(a(i)=i\), \(b(i)=i-1\); if odd then \(a(i)=i-1\), \(b(i)=i\). Empty index ranges are ignored. These are the figure-consistent completed transitions of the literature's \(A_k\) family, including the two boundary cases omitted from an early printed case distinction [1,2].

A word acts from left to right. For a distinct unordered pair \(\{p,q\}\), define \(d_k(p,q)\) as the minimum nonnegative word length resulting in equal state images, or infinity when no word merges it. The theorem is about **all** unordered pairs, not the shortest word merging a designated state with *some* other state; those are different invariants.

## Proof
For fixed \(k\), construct the finite directed *pair automaton* with vertices \(\{p,q\}\) for \(0\le p\le q<n\). Each letter \(c\in\{a,b\}\) gives an arc \(\{p,q\}\longrightarrow\{c(p),c(q)\}\). Every diagonal \(\{i,i\}\) is a collision terminal. A word merges a distinct pair precisely when its directed path reaches a diagonal; thus \(d_k(p,q)\) is the shortest path length to the set of diagonals.

Reverse every pair-automaton arc, and perform multi-source breadth-first search from all \(n\) diagonals at distance zero. Every arc has unit length, hence the first search label assigned to any unordered pair equals the exact shortest forward distance to a diagonal. This claim follows inductively on BFS levels: a path of length \(t\) ending at a diagonal is exactly a reversed path of length \(t\) from that diagonal, and BFS first visits vertices at their shortest reversed distance. The search has \(n(n+1)/2\) possible vertices and terminates after at most that many successful insertions.

The supplied implementation realizes each reversed arc **without approximations**: for each letter it builds inverse-image lists \(R_c(i)=\{p:c(p)=i\}\). When popping \(\{x,y\}\), for every \(p\in R_c(x)\) and \(q\in R_c(y)\), it inserts the unordered preimage \(\{p,q\}\), excluding duplicate and diagonal preimages where appropriate. Each inserted predecessor really maps to \(\{x,y\}\), and every such predecessor occurs in one of these inverse-image products (including the symmetric ordering where \(x\ne y\) when the successor is canonically ordered). Consequently the constructed reversed graph is exactly the reverse of the full unordered pair automaton.

The attached `pair_census.cpp` is a complete finite certificate checker for the parameter interval. It reconstructs every transition from the explicit definition, initializes **all** diagonal targets, visits their full reverse-reachable set, rejects any unvisited off-diagonal pair, and tests every one of the \(\binom{n}{2}\) off-diagonal distances against the candidate diameter. It records the maximizing pair and its multiplicity and aborts unless the diameter is \(D(k)\), the maximizing pair has indices \(h,h+1\), and its multiplicity is one. Its successful run for **every** \(k=1,\ldots,1000\), with one row for every integer, is embedded as `pair_census.tsv`.

The full sweep computes exact distances for \(1{,}510{,}524{,}000\) distinct unordered pairs across the thousand automata, with \(1{,}512{,}031{,}500\) pair states including diagonals. Each parameter is checked against its own complete state space, with no sampling and no extrapolation between parameters. This finite exhaustion proves the statement for the declared interval.

## Verification
Build and run the verifier using a C++17 compiler: `c++ -O3 -std=c++17 -Wall -Wextra -pedantic pair_census.cpp -o pair_census` followed by `./pair_census 1000 > pair_census.tsv`. The attached complete tab-separated output includes columns for \(k\), \(n\), diameter, maximizing pair, multiplicity, and completeness of pair merging. There are \(1000\) result rows and one header row, with SHA-256 `f88e9f5eb6626e581f2ffb6d19660280904394a77ad6bd590d8c8db8b81c2128` for the recorded output.

Two complementary, independently written checks reduce the risk of a mistaken inverse-edge implementation. `crosscheck_small.py` explicitly creates *every* pair-automaton arc and its reverse adjacency lists for \(1\le k\le40\), computing exact BFS distances and the entire maximizing-pair set independently of the main checker. `crosscheck_forward.cpp` independently runs **forward** BFS from the declared farthest pair for ten cases, including \(k=1000\), and verifies that its shortest collision word length equals the claimed diameter. The recorded outputs in `verification_output.txt` were reproduced with these standalone sources. The forward checks substantiate the extremal lower bound, while the main reverse BFS certifies the entire upper bound and uniqueness.

## Relationship to prior work
Szykuła's 2026 survey [1] introduces the \(3k+6\)-state construction as an open-problem example, focusing on the distinguished-state compression threshold, not the all-pairs diameter. An independent 2026 paper [2, §8, Theorem 8.1] proves exactly the displayed piecewise diameter formula for \(1\le k\le16\), reports unformalized computation for \(17\le k\le30\), and poses the **all-\(k\)** equality as Conjecture 8.2. The present finite theorem establishes the conjectured values exhaustively through \(k=1000\) and additionally gives a unique maximizing pair for every value in that interval. The unique-extremizer statement is not made in the inspected relevant theorem or conjecture. Neither a proposed general formula nor a computation without a proof-level finite certificate establishes values beyond its proved range.

The 2018 thesis originally credited with introducing the construction was not accessible for complete inspection. Relevant searchable mathematical research records and available earlier local claims revealed no equivalent or stronger all-pairs result for this interval; such negative searches cannot establish exhaustive historical priority.

## Limitations
All conclusions are confined to the one thousand explicitly specified automata. The checksum and recorded output alone are not substitutes for reading or rerunning the exhaustive verifier. This is a machine-assisted exact finite proof whose reliability depends on the supplied C++17 source, correct compilation/execution and the explicit inverse-graph argument. An arbitrary-\(k\) proof, a closed formula for all pair distances, and independent scientific validation remain open or unperformed here. The inaccessible originating thesis and unindexed equivalent computations are residual originality risks.

## References
[1] Marek Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245v1 (first posted 2026-08-25), §2.3, Figure 3. https://arxiv.org/abs/2608.24245

[2] *The compress-with-another threshold of the series* \(A_k\)*: an upper bound* \(4n/3\) *for every* \(k\)*, exact values to* \(n=186\)*, and a one-letter correction*, 2026, §§2, 8, Theorem 8.1 and Conjecture 8.2. https://ideosphere.ai/papers/cwa-series-v1.pdf
