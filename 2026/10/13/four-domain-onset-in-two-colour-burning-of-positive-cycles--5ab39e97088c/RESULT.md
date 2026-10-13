# Four-domain onset in two-colour burning of positive cycles
## Finding
Let \(C_n\), for each integer \(n\geq3\), carry the all-positive signature and the two-colour spread-before-ignition dynamics defined below. The complete terminal-word codes through the first occurrence of four sign boundaries are as follows.

- At \(n=3\), exactly the two constant sign words are reachable.
- At \(n=4\), exactly ten words are reachable: the two constant words and the eight words with a unique vertex of the minority colour.
- For every integer \(5\leq n\leq9\), precisely the two constant words and all \(n(n-1)\) words with exactly two cyclic sign boundaries are reachable. Thus the code cardinality is \(n(n-1)+2\).
- At \(n=10\), exactly 172 words are reachable: two with no boundaries, all 90 with two boundaries, and exactly 80 with four boundaries. The latter 80 split into four classes of 20, with cyclic run-length representatives \((1,2,2,5)\), \((1,5,2,2)\), \((1,2,4,3)\), and \((1,3,4,2)\). Run lengths are considered up to cyclic rotation of the four runs, not reflection.

**Sharp infinite threshold.** Every terminal word for \(3\leq n\leq9\) has at most two cyclic sign boundaries. For each integer \(n\geq10\), some reachable terminal word has at least four cyclic sign boundaries. Thus ten is the exact first cycle order permitting four boundaries.

The exact Hamming covering radius \(\rho_n\) of the reachable code for \(3\leq n\leq10\) is
\[
(\rho_3,\rho_4,\ldots,\rho_{10})=(1,1,1,2,2,3,3,4).
\]
By the previously established switching/covering-radius correspondence [1, Proposition 2.9 and Remark 2.10], the minimum two-colour plurality over all *balanced signatures* of \(C_n\) at these orders is \(n-\rho_n\). In particular, the radius at order ten is four, whereas the corresponding positive path radius is three by [1, Remark 3.5].

## Assumptions and scope
All graphs are finite, simple, undirected, with labeled vertices \(\{0,\ldots,n-1\}\) and edges between consecutive residues modulo \(n\). All edges have sign \(+1\). At the start all vertices have state zero. In each round **first** every unburned vertex changes simultaneously to the sign of the sum of its two previously burned neighbours, with sign of zero interpreted as zero. Previously nonzero states never change. **Then**, if any vertex remains unburned, exactly one such vertex is ignited in a freely chosen state \(+1\) or \(-1\). A terminal word is a fully nonzero state at the first terminal round; both signs are distinguished, as are labeled vertices. This is the signed-burning process of [1, Definition 2.1] specialized to positive cycles.

For a terminal word \(w\in\{-1,+1\}^n\), its cyclic boundary count is
\[
b(w)=\sum_{i=0}^{n-1}{\bf1}\{w_i\ne w_{i+1\bmod n}\}.
\]
A four-boundary word has four alternating monochromatic runs. Its cyclic run-length type is the lexicographically smallest cyclic rotation of the four positive run lengths. The code \(\mathcal R_n\) consists of all reachable terminal words and has covering radius
\[
\rho_n=\max_{u\in\{-1,+1\}^n}\min_{w\in\mathcal R_n}d_H(u,w).
\]
No assertion of an exact code or radius is made for \(n\geq11\); the infinite-order assertion concerns only the existence of at least four boundaries. No claim is made for unbalanced signatures.

## Proof
**Exhaustive finite-state lemma.** For any fixed \(n\), let \(s\in\{-1,0,+1\}^n\). Define its simultaneous spread \(F(s)\) coordinatewise: if \(s_i\ne0\), preserve it; otherwise set
\[
F(s)_i=\operatorname{sgn}(s_{i-1\bmod n}+s_{i+1\bmod n}),\qquad\operatorname{sgn}(0)=0.
\]
If \(F(s)\) is terminal, it is the unique one-round successor. Otherwise the one-round successors are the states obtained from \(F(s)\) by changing **exactly one** zero to either sign. Start with the all-zero state and take the directed reachability closure under this successor relation, collecting all terminal states. This procedure enumerates precisely the reachable terminal code: every legal round is one listed transition, and each listed transition is realizable by a legal ignition. Every transition from a nonterminal state increases the number of nonzero coordinates by at least one; therefore all paths end after at most \(n\) ignitions. There are at most \(3^n\) states, and exhaustive closure is both terminating and complete.

**Finite computations, fully specified.** The accompanying `verify_burning_cycles.py` implements the above closure with breadth-first search over sign tuples; `verify_burning_cycles_independent.py` separately implements the same recursion using integer ternary encodings and memoized depth-first search. The independent `crosscheck_burning_cycles.py` compares the **entire labeled terminal-word sets**, not just aggregate counts, for each order \(3\) through \(10\). All comparisons match. The primary program counts cyclic boundaries, tabulates canonical run types, and enumerates every one of the \(2^n\) binary target words to compute exact Hamming-distance distributions. These exhaustive finite checks yield:

| \(n\) | \(|\mathcal R_n|\) | number by boundary count \(0,2,4\) | \(\rho_n\) | counts of target words at distance \(0,1,\ldots,\rho_n\) |
|---:|---:|---|---:|---|
| 3 | 2 | 2,0,0 | 1 | 2,6 |
| 4 | 10 | 2,8,0 | 1 | 10,6 |
| 5 | 22 | 2,20,0 | 1 | 22,10 |
| 6 | 32 | 2,30,0 | 2 | 32,30,2 |
| 7 | 44 | 2,42,0 | 2 | 44,70,14 |
| 8 | 58 | 2,56,0 | 3 | 58,136,60,2 |
| 9 | 74 | 2,72,0 | 3 | 74,234,186,18 |
| 10 | 172 | 2,90,80 | 4 | 172,490,310,50,2 |

The count of all labeled words with exactly two cyclic boundaries is \(n(n-1)\): choose an ordered pair of distinct boundary edges and one of the two possible signs on a reference interval, then account for double counting the unordered boundary pair. Consequently the computed counts \(n(n-1)\) at orders five through ten together with the boundary restriction prove equality with **all** such words. At order four, the eight two-boundary words are exactly the eight with a singleton minority run, as confirmed by direct enumeration. At order ten the four run types stated in the finding each occur 20 times and exhaust the 80 four-boundary outputs. No word of six or more boundaries appears by the complete finite-state census.

**Infinite-order construction and sharpness.** For every \(n\geq10\), in four consecutive rounds ignite vertices
\[
0,\quad2,\quad4,\quad6
\]
with respective signs \(-1,+1,-1,+1\). These ignitions are legal. Before round two, vertex two is distance two from the sole source at vertex zero and is not reached by the one intervening spread. Before round three, vertex four is distance at least two from source two and at least four from source zero; neither fire has had enough spreads. Before round four, vertex six has respective cycle distances at least four, four and two from the earlier sources at vertices zero, two and four, while those sources have respectively had only three, two and one spread opportunities. Here the distance from zero to six is \(\min\{6,n-6\}\geq4\), exactly where the hypothesis \(n\geq10\) is used. Therefore vertex six is also still unburned at its ignition step.

All four ignited signs persist in every completion. Going cyclically through the four disjoint arcs between their positions, the endpoint signs alternate, so each arc contains at least one edge with opposite terminal signs. The four arcs are edge-disjoint, hence the terminal word has **at least four** sign boundaries. Every partial state admits a completion because each remaining round ignites another unburned vertex. For \(3\leq n\leq9\), the complete finite-state census above shows no word with four boundaries. The threshold is therefore exact.

**Covering-radius consequence.** Given the exact terminal-code sets, the exhaustive \(2^n\)-target Hamming counts in the table establish \(\rho_n\) exactly. The conversion to minimum plurality among balanced signatures is an application of [1, Proposition 2.9 and Remark 2.10], not a new general switching theorem. Its path comparison uses the path formula already proved in [1, Remark 3.5].

## Verification
Extract the standalone Python files and corresponding `*_output.txt` files from the package into one directory. With Python 3.10 or newer and no external packages, execute:

```sh
python verify_burning_cycles.py
python verify_burning_cycles_independent.py
python crosscheck_burning_cycles.py
```

The three programs reproduce `bfs_output.txt`, `dfs_output.txt`, and `crosscheck_output.txt`. The primary enumeration explores, at \(n=10\), precisely 1553 distinct end-of-round ternary states and 3880 successor transitions; the depth-first implementation visits 1553 distinct states. The finite proof depends on the proved completeness of the transition relation and on actually executing the programs; the output logs by themselves are not proofs. The non-finite existence assertion is established by the explicit four-source argument rather than by testing larger orders.

## Relationship to prior work
Fallat, Gupta, Khodamoradi and Zilles [1] introduce this exact two-colour signed-burning dynamics, define its reachable terminal-word code, prove switching equivariance, and relate the minimum plurality over a switching class to Hamming covering radius. Their Section 3 computes results for signed **paths**; these general results do not count terminal words on **cycles**, determine the four-boundary onset, identify the 80 ten-vertex four-run words, or supply the cycle radius table. Their path covering-radius formula is expressly acknowledged and used for comparison. Conventional unsigned graph-burning parameters and standard graph colorings do not contain terminal *two-colour* code data. Related semantic searches of published mathematical findings showed no statement implying the present cycle-specific finite classification or sharp onset; this is evidence of a gap, not a proof of uniqueness.

## Limitations
The exact code and covering radius are proved only for cycle orders three through ten; for every larger order the theorem proves existence of a four-boundary terminal word but makes no complete classification, optimal boundary-count claim, or covering-radius claim. Only the all-positive cycle signature is directly enumerated. The balanced-signature plurality corollary relies on the switching result of [1]; arbitrary unbalanced signatures are not covered. The finite checks are exhaustive only for the explicitly listed sizes and depend on the readable standalone algorithms; their reachability-completeness lemma supplies the mathematical bridge from finite search to a valid finite theorem. The originality comparison cannot exclude unidentified equivalent classifications.

## References
[1] S. Fallat, H. Gupta, K. Khodamoradi, and S. Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1, first posted October 1, 2026; especially Definition 2.1, Proposition 2.9, Remark 2.10, Section 3 and Remark 3.5. https://arxiv.org/html/2610.02506v1
