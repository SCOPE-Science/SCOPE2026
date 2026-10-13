# Exact simultaneous reset thresholds for pairs of Černý automata through eleven states

## Finding

Let \(C_k\) be the standard \(k\)-state Černý deterministic automaton with common input alphabet \(\{a,b\}\), defined below. For every pair of integers \(2\le m<n\le11\), let \(L(m,n)\) denote the shortest length of a **single common reset word** for both automata. The following table determines all \(45\) values **exactly**, not as estimates. In each row the values are ordered by increasing \(m\).

| \(n\) | \(m\) in order | Exact \(L(m,n)\) in order |
|---:|:---|:---|
| 3 | 2 | 4 |
| 4 | 2, 3 | 9, 10 |
| 5 | 2, 3, 4 | 16, 17, 18 |
| 6 | 2, 3, 4, 5 | 25, 25, 27, 28 |
| 7 | 2, 3, 4, 5, 6 | 36, 37, 37, 39, 40 |
| 8 | 2, 3, 4, 5, 6, 7 | 49, 50, 49, 52, 53, 54 |
| 9 | 2, 3, 4, 5, 6, 7, 8 | 64, 64, 66, 66, 66, 69, 70 |
| 10 | 2, 3, 4, 5, 6, 7, 8, 9 | 81, 82, 83, 81, 84, 85, 87, 88 |
| 11 | 2, 3, 4, 5, 6, 7, 8, 9, 10 | 100, 101, 101, 103, 102, 104, 103, 107, 108 |

The additional common-control latency relative to resetting \(C_n\) alone is \(E(m,n)=L(m,n)-(n-1)^2\). Its complete spectrum is:

| \(n\) | Exact overheads for increasing \(m\) |
|---:|:---|
| 3 | 0 |
| 4 | 0, 1 |
| 5 | 0, 1, 2 |
| 6 | 0, 0, 2, 3 |
| 7 | 0, 1, 1, 3, 4 |
| 8 | 0, 1, 0, 3, 4, 5 |
| 9 | 0, 0, 2, 2, 2, 5, 6 |
| 10 | 0, 1, 2, 0, 3, 4, 6, 7 |
| 11 | 0, 1, 1, 3, 2, 4, 3, 7, 8 |

In this domain, \(\max_{2\le m<n} E(m,n)=n-3\), always attained at \(m=n-1\). In particular \(L(10,11)=108\), compared with the single-automaton optimum \(100\). The natural arithmetic zero-overhead cases \(m=2\) and \(m\mid n\) hold for **all** \(n>m\ge2\), not only the enumerated range; this statement follows directly from the classical shortest Černý reset construction and is background, not a separate novelty claim.

## Assumptions and scope

For each integer \(k\ge2\), \(C_k\) has state set \(Q_k=\{0,1,\ldots,k-1\}\). Letter \(a\) sends \(i\) to \(i+1\pmod k\); letter \(b\) fixes \(i<k-1\) and sends \(k-1\) to \(0\). A word \(w\in\{a,b\}^*\) **resets** \(C_k\) if \(Q_k\cdot w\) is a singleton. It is a **common reset word** for \(C_m,C_n\) if both images are singletons; the singleton targets need not be identified. A word's length counts the total input letters. All pairs are ordered by \(m<n\), and all claims of exact finite enumeration are restricted to \(2\le m<n\le11\).

The complete machine-readable list of the 45 thresholds, lexicographically earliest shortest witnessing words (\(a<b\)) and discovered-state counts is in `table.csv`. The witnesses are not asserted unique.

## Proof

**1. Product reduction.** For \(S\subseteq Q_m,T\subseteq Q_n\) and either input letter \(c\), \((S\times T)\cdot c=(S\cdot c)\times(T\cdot c)\). Induction gives the same identity for every word. Consequently a word resets the usual direct-product automaton \(C_m\times C_n\) if and only if it resets both factors. Equivalently \(w\in\operatorname{Syn}(C_m)\cap\operatorname{Syn}(C_n)\).

**2. Finite exhaustive certificate.** Define the finite directed graph \(G_{m,n}\) whose vertices are all pairs of nonempty subsets \((S,T)\) of \(Q_m,Q_n\). Its initial vertex is \((Q_m,Q_n)\). For each vertex and \(c\in\{a,b\}\), include the edge \((S,T)\to(S\cdot c,T\cdot c)\). The goal vertices are exactly those with \(|S|=|T|=1\). The graph has at most \((2^m-1)(2^n-1)\) vertices, so this is a finite **complete** state space. Any path of length \(\ell\) corresponds to a word of length \(\ell\), and conversely. Therefore the graph distance to a goal is **exactly** \(L(m,n)\). Ordinary breadth-first search, exploring `a` then `b` and recording each first-visit predecessor, visits all reachable vertices at smaller distances before dequeuing a goal. It supplies both an optimal witness and a proof that no shorter word exists. The Python implementation uses tuple-keyed subset bitmasks; the C++ implementation uses a single encoded integer per pair and computes each bit transition explicitly. Each independently performs all \(45\) exact graph searches and verifies every reconstructed witness by replay against each original automaton.

**3. Exhaustiveness and equality of outputs.** The programs iterate every \(n=3,\ldots,11\) and every \(m=2,\ldots,n-1\), exactly \(\sum_{n=3}^{11}(n-2)=45\) pairs. The two generated CSV tables agree field by field on `m,n,length,word,visited_before_goal`; the included `table.csv` is the Python output and can be compared to the C++ output. Its 45 length entries yield the claimed table and overheads. The CSV discovered-state column records how many vertices were first discovered when the initial shortest-goal search terminated; the claim of minimality follows from BFS search order, not from that column alone.

**4. Finite consequences and an all-size baseline.** Direct subtraction of \((n-1)^2\) for each of the \(45\) verified entries gives the overhead table and, for each \(n\le11\), maximum \(n-3\) at \(m=n-1\). For the all-size baseline, the classical shortest Černý word \(W_n=b(a^{n-1}b)^{n-2}\) has length \((n-1)^2\). If \(m\mid n\), its action on \(C_m\) is \(b(a^{m-1}b)^{n-2}\), which includes the standard reset word \(W_m\) as a prefix; hence \(W_n\) resets both, and no common word can be shorter than the known optimum for \(C_n\). For \(m=2\), the letter \(b\) already resets \(C_2\), and \(W_n\) begins with \(b\).

## Verification

The self-contained executable scripts are `verify_python.py` (Python 3.9+) and `verify_cpp.cpp` (C++17). In a directory containing them and `table.csv`, run `python3 verify_python.py`, then `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp`. The scripts produce `table_python.csv` and `table_cpp.csv`, respectively. Compare parsed CSV records (they may use different newline conventions) to `table.csv`: all \(45\) rows and full shortest witnesses must match. Both implementations replay every word on the full initial state set of each automaton, and assert singleton images. Neither relies on an external solver, unpublished table, or heuristic search. The largest explored instance is \((m,n)=(10,11)\); the C++ program allocates at most \(2^{m+n}\) parent slots, which is finite and feasible here.

## Relationship to prior work

Černý's classical example establishes the separate reset threshold \((n-1)^2\). Kisielewicz–Kowalski–Szykuła develop single-automaton shortest-word search algorithms [1] and census experiments [4]; these do not give the shortest **intersection** word for two differently sized automata. Maslennikova [3] explicitly relates intersections of synchronizing languages to direct products and studies a decision/complexity question about language equality; the reduction is used here, but no table for \(C_m,C_n\) is reported in the examined relevant sections. Gusev [2] studies random-input coalescence of two *states of one* Černý automaton; that is a different pair problem. None of these inspected primary results supplies the 45-entry exact simultaneous-threshold spectrum or its finite overhead classification. An earlier unindexed computation under equivalent terminology cannot be ruled out.

## Limitations

Exact enumeration establishes the displayed table only for \(2\le m<n\le11\). The observed consecutive-size equality \(L(n-1,n)=(n-1)^2+n-3\) is **not** proved beyond this range. The graph search is finite and complete but is not a succinct symbolic formula for arbitrary pairs; memory growth precludes unqualified large-size extrapolation. Secondary references or unpublished code may already tabulate related values; bibliographic noncoverage is not a proof of uniqueness. Independent mathematical audit has not been performed.

## References

1. A. Kisielewicz, J. Kowalski, M. Szykuła, *A Fast Algorithm Finding the Shortest Reset Words* (2012), arXiv:1203.2822, https://arxiv.org/pdf/1203.2822.
2. V. V. Gusev, *Synchronizing automata with random inputs* (2014), arXiv:1404.6731, https://arxiv.org/pdf/1404.6731.
3. M. Maslennikova, *Complexity of checking whether two automata are synchronized by the same language* (2014), arXiv:1405.3576, https://arxiv.org/pdf/1405.3576.
4. A. Kisielewicz, J. Kowalski, M. Szykuła, *Experiments with Synchronizing Automata* (2016), arXiv:1607.04025, https://arxiv.org/pdf/1607.04025.
