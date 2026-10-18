# Complete bipartite structure of minimum circular attractors in the first twelve finite Fibonacci words

## Finding
For \(m=1,2,\ldots,12\) let \(F_0=0\), \(F_1=01\), and \(F_m=F_{m-1}F_{m-2}\). Let \(G_m\) have as vertices the zero-based positions of \(F_m\). Two distinct positions are adjacent precisely when together they form a circular string attractor: for **each** nonempty circular factor of length at most \(|F_m|\), some occurrence of that factor intersects at least one chosen position.

**Finite classification (all indicated twelve cases):** \(G_m\) is the disjoint union of isolated vertices with
\[
K_{2^{\lfloor m/2\rfloor},\;2^{\lfloor(m-1)/2\rfloor}}.
\]
Consequently the exact minimum size of a circular attractor is two, and the number of minimum-size attractors is \(2^{m-1}\). Furthermore, when all position pairs are filtered by the requirement for lengths \(1,2,\ldots,|F_m|\) in that order, for \(m\ge2\) a strict decrease occurs at exactly the lengths \(|F_0|,|F_1|,\ldots,|F_{m-2}|\). There are no such strict decreases for \(m=1\).

## Assumptions and scope
All positions are zero-based and interpreted modulo the length \(N=|F_m|\). For \(1\le \ell\le N\), a circular occurrence starting at \(s\in\{0,\ldots,N-1\}\) is the length-\(\ell\) substring of the periodic extension \(F_mF_m\) beginning at \(s\). It covers precisely the positions \((s+t)\bmod N\) with \(0\le t<\ell\). A two-position set is an attractor if, for every distinct factor \(u\) of each such length, **at least one** of its occurrences covers at least one position in the set. A factor appearing at several start positions requires only one intersecting occurrence.

The theorem is a finite classification for \(m\le12\); it is not an asserted induction over all Fibonacci indices. All twelve lengths, all position pairs, all circular start positions and all admissible factor lengths are covered without sampling or probabilistic assumptions. The symbols \(0\) and \(1\) both occur in every word under consideration, so one position never suffices.

## Proof
This finite proof is an exhaustive enumeration with a small, standalone checker (see `checker.py`). Its correctness is reduced to the following bit-set invariant, which can be inspected directly in the embedded program.

Fix a word \(w\) of length \(N\) and a factor length \(\ell\). Enumerate the distinct circular factors of that length, giving each a unique integer \(j\in\{0,\ldots,r-1\}\). For each position \(p\), form the integer mask \(M_{\ell,p}\) whose \(j\)-th bit is set exactly when **at least one** occurrence of the \(j\)-th factor covers \(p\). The checker forms these masks by looping over all \(N\) start positions, identifying the factor in the periodic extension, and setting its bit at every one of the \(\ell\) covered positions modulo \(N\). Every occurrence and every covered position is visited exactly once in its associated loop. Therefore, for any unordered pair of distinct positions \(\{p,q\}\), every length-\(\ell\) factor has an occurrence crossing \(p\) or \(q\) if and only if
\[
M_{\ell,p}\mathbin{|}M_{\ell,q}=2^r-1,
\]
where the vertical bar denotes bitwise OR. This equivalence is exact, including multiply occurring factors and factors wrapping around the circular boundary.

The checker begins with **all** \(\binom N2\) possible pairs and, for each \(\ell=1,\ldots,N\), discards precisely the pairs failing the preceding equality. Thus its final edge set is **exactly** the edge set of \(G_m\). It records each factor length at which this set shrinks; these are the only critical lengths. The program independently computes all connected components and bipartite vertex classes by breadth-first search, checks every edge crosses classes, and compares the complete edge set with their Cartesian product. These equalities prove the claimed complete bipartite structure, not merely its edge count. It checks both partition sizes implicitly from their product and explicitly through the displayed complete output, and checks the closed-form \(2^{m-1}\) edge count for each index. The two bipartition classes consist of positions with opposite symbols. Hence a one-position attractor cannot exist (both symbols occur as length-one factors), and each enumerated pair is minimal.

Every critical length is checked against the exact list \(|F_0|,\ldots,|F_{m-2}|\) for each \(m\ge2\), rather than inferred from a plot. The complete program is short and uses only Python's standard library. It terminates after at most \(\sum_{m=1}^{12}\sum_{\ell=1}^{|F_m|}(\ell |F_m|+|F_m|^2)\) elementary position and mask operations, a finite bound determined by the displayed loops.

## Verification
The executable `checker.py` prints one result line per \(m\), including exact circular factor totals, surviving pairs, two bipartite part sizes, the exact critical-length list, and the first sixteen hexadecimal characters of the SHA-256 digest of the ordered surviving-edge list. The complete actual output is embedded in `checker-output.txt`.

| \(m\) | \(|F_m|\) | Distinct length-tagged circular factors | Minimum pairs | Bipartite parts |
|---:|---:|---:|---:|---:|
|1|2|4|1|1 and 1|
|2|3|8|2|2 and 1|
|3|5|19|4|2 and 2|
|4|8|43|8|4 and 2|
|5|13|103|16|4 and 4|
|6|21|251|32|8 and 4|
|7|34|628|64|8 and 8|
|8|55|1594|128|16 and 8|
|9|89|4093|256|16 and 16|
|10|144|10583|512|32 and 16|
|11|233|27493|1024|32 and 32|
|12|377|71629|2048|64 and 32|

For the largest case the certificate gives the full two sets of active zero-based positions, containing 64 and 32 positions respectively. Their Cartesian product is exactly the 2,048-edge minimum-attractor graph; all other 281 positions are isolated. To replay: `python3 checker.py` (Python 3.9+). It must end with `ALL FINITE ENUMERATIONS PASS`. No third-party libraries or input datasets are needed.

## Relationship to prior work
The standard circular-attractor decision/optimization framework is developed by Giuseppe Romana in *An Algorithmic View on Circular String Attractors* (2023). That article describes algorithms and includes an illustrative Fibonacci example, but the inspected exposition does not enumerate all minimum circular-attractor pairs for the first twelve Fibonacci words, determine their complete bipartite compatibility graphs, or identify the complete sequence of critical constraint lengths. The 2026 study *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words* by Banbara and collaborators counts **linear** Fibonacci attractors; its treatment of linear positions is not a covering theorem about circular factors and circular position pairs. Earlier Christoffel/Sturmian studies supply contextual factor-complexity results, not the stated circular minimum-pair classification. An equivalent hidden tabulation, particularly within a computational appendix, remains a priority risk.

## Limitations
The classification is completely finite: it stops at the twelfth Fibonacci index and length 377. The observed power-of-two count, complete bipartite shape and Fibonacci-critical lengths are not asserted to persist at higher indices. The result is not a proof of uniqueness of a general closed form over all indices. The proof relies on reproducible full finite enumeration and does not contain a human-only analytic derivation of the observed structure. Publication priority is not independently certified. The finite checker is supplied for complete replay and inspection; its successful execution is not a substitute for scrutiny of its bitset invariant.

## References
1. Giuseppe Romana, *An Algorithmic View on Circular String Attractors*, ICTCS 2023. https://ceur-ws.org/Vol-3587/9885.pdf
2. M. Banbara and collaborators, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, first arXiv public version February 18, 2026, arXiv:2602.16152; CPM 2026. https://arxiv.org/abs/2602.16152
3. Carey and Clampitt, *Partitioned Factors in Christoffel and Sturmian Words*, 2018. https://arxiv.org/abs/1804.08724
