# Palindromic-span spectrum and reversal-symmetry orbits of binary order-five de Bruijn cycles

## Finding

Let \(B\) be a binary cyclic de Bruijn word of order \(5\), meaning a length-\(32\) cyclic word in which each of the \(32\) binary length-\(5\) words occurs exactly once. Identify words differing by cyclic rotation, but **not** by complementation or reversal. Define \(L(B)\) as the greatest length of a contiguous palindrome appearing anywhere in the bi-infinite periodic extension of \(B\). The complete distribution is:

| \(L(B)\) | Cycles | Orbits of size \(2\) | Orbits of size \(4\) |
| ---: | ---: | ---: | ---: |
| 7 | 200 | 14 | 43 |
| 8 | 192 | 4 | 46 |
| 9 | 856 | 6 | 211 |
| 10 | 128 | 0 | 32 |
| 11 | 392 | 6 | 95 |
| 12 | 32 | 0 | 8 |
| 13 | 200 | 2 | 49 |
| 15 | 48 | 0 | 12 |
| **Total** | **2048** | **32** | **496** |

The orbits are under the actions of binary complementation and reversal on rotation classes. No other values of \(L(B)\) or orbit sizes occur. In particular, the sharp minimum and maximum are \(7\) and \(15\). Two example anchored representatives attaining those extremes are `00000100011010011101100101011111` and `00000100011010011111001010111011`, respectively.

## Assumptions and scope

All indices in a cycle are taken modulo \(32\). A cyclic palindrome of length \(\ell\) is a word \(B_i B_{i+1}\cdots B_{i+\ell-1}\) equal to its reversal. The represented cycle is uniquely rooted for enumeration by the beginning of its unique occurrence of `00000`. The rotation class retains both its complemented and reversed partners as distinct cycles unless they are related by rotation. This statement is specific to a binary alphabet and de Bruijn order \(5\); it makes no assertion for larger orders.

## Proof

**1. An exhaustive, duplication-free parameterization.** Write a length-\(5\) state as \(au\), with \(a\in\{0,1\}\) and \(u\in\{0,1\}^4\). Its successor in the cyclic list of length-\(5\) windows has the form \(ub\), where \(b\) is the newly appended symbol. Since the windows of a de Bruijn cycle contain all states and each successor must occur once, the two states \(0u\) and \(1u\) must receive different appended bits. Therefore there is a unique Boolean function \(h:\{0,1\}^4\to\{0,1\}\) such that their appended bits are \(h(u)\) and \(1-h(u)\), respectively. Conversely, for every such \(h\), the map

\[
T_h(au)=u\bigl(a\mathbin{\oplus}h(u)\bigr)
\]

permutes the \(32\) states. Its orbit from `00000` defines a de Bruijn cycle precisely when the orbit has all \(32\) states and returns to `00000`. Exactly one Boolean function corresponds to each rooted de Bruijn cycle. There are exactly \(2^{16}=65536\) Boolean functions to test; no candidate or rotation class is excluded by this parameterization.

**2. Exact enumeration and palindrome computation.** For each of the \(65536\) functions, the standalone program `pal_cycle_fsr.cpp` checks the orbit and, when it is a full \(32\)-cycle, constructs its unique rooted output word. For each \(\ell\in\{1,\ldots,32\}\) and cyclic start \(i\in\{0,\ldots,31\}\), it compares opposite positions of the corresponding factor to test whether the factor is a palindrome. It finds exactly \(2048\) accepted cycles and the eight frequency bins in the table. The independent program `pal_cycle_dfs.py` instead depth-first enumerates edge-simple Euler circuits in the order-\(5\) de Bruijn graph, anchored at `00000`, and obtains the identical bins. The underlying state and edge invariants establish exhaustive mathematical coverage, rather than a sample-based inference.

**3. Completeness of the length cutoff.** It remains to ensure that no palindrome longer than a period was overlooked. A palindrome of length \(14\) or \(17\) can occur in a de Bruijn cycle only if its length-\(5\) subwords form a nonrepeating directed trail in the order-\(5\) de Bruijn graph that can be completed to an Euler circuit. Such a completion exists exactly when the unused directed edges, whose degrees automatically have the two appropriate trail endpoints, have weakly connected nonisolated support including those endpoints (or have no unused edges and coincident endpoints). The standalone `pal_euler_n5.py` tests this condition on every binary palindrome of lengths \(14\), \(15\), \(16\), and \(17\), yielding respectively \(0\), \(6\), \(0\), and \(0\) extendible candidates. Hence no even palindrome of length at least \(14\), and no odd palindrome of length at least \(17\), can appear. Thus \(L(B)\le15\) for every cycle, and checking through length \(32\) is more than sufficient. Independently, every cycle has the unique `00000` preceded and followed by `1`; otherwise `00000` would repeat. The factor `1000001` is therefore present, giving \(L(B)\ge7\). The first and last table rows, each positive, show both bounds sharp.

**4. Symmetry-orbit counts.** Complementation and reversal commute and preserve \(L(B)\), and hence act on the \(2048\) rotation classes. The independent `pal_cycle_orbits.py` traverses all accepted Boolean feedback functions, normalizes cyclic rotations lexicographically, and partitions the classes into their orbits under the four group actions. It computes the displayed two- and four-element orbit counts. In every row, twice the size-two count plus four times the size-four count equals the corresponding cycle total. The totals are \(32\) orbits of size two and \(496\) of size four, accounting for all \(2048\) cycles.

## Verification

The package contains four standalone reproducibility artifacts: `pal_cycle_dfs.py`, `pal_cycle_fsr.cpp`, `pal_euler_n5.py`, and `pal_cycle_orbits.py`. They need Python 3 standard libraries and a C++17 compiler, respectively. Run `python3 pal_cycle_dfs.py`, `g++ -std=c++17 -O2 pal_cycle_fsr.cpp -o pal_cycle_fsr && ./pal_cycle_fsr`, `python3 pal_euler_n5.py`, and `python3 pal_cycle_orbits.py`. Their exact expected histograms and orbit counts are provided above and in `VERIFICATION.md`. Distinct data structures are used for the two exhaustive primary counts. An exhaustive finite proof is obtained because their loops cover a mathematically complete finite parameter space; the independence of the implementations is a useful cross-check, not a substitute for completeness arguments.

## Relationship to prior work

Gabrić and Sawada's 2024 work on orientable sequences treats the stronger *exclusion* of an order-length palindromic window and reversal pairs, and develops efficient constructions and upper bounds for the lengths of the resulting words. A full binary de Bruijn cycle necessarily contains all length-\(5\) palindromes, so that construction problem does not imply the present distribution of its longest palindromic window. Chang and Wang's 2024 study analyzes complement/reversal-symmetric de Bruijn sequences and their numbers and linear complexity, but not their maximum palindrome spans. Burris, Motta, and Shipman's 2016 unoriented variation studies reversal classes of fixed-length windows and Eulerian structures rather than the maximum length of a palindrome in each standard de Bruijn cycle. These sources motivate the invariant without yielding the eight-bin spectrum or its symmetry-orbit refinement in the material inspected.

## Limitations

The exact census is restricted to binary order \(5\) and to rotations as the primary equality relation. The counts are rigorous finite statements contingent on the explicit finite parameterization and executable enumerators, not asymptotic statements. They do not establish a formula for other orders. The 2024 reversal literature and related references do not exclude the possibility of an independently derived or unindexed table elsewhere; independent scholarly priority review has not been performed.

## References

1. D. Gabrić and J. Sawada, *Efficient Construction of Long Orientable Sequences*, 35th Annual Symposium on Combinatorial Pattern Matching, LIPIcs 296 (2024), Article 15. DOI: 10.4230/LIPIcs.CPM.2024.15. Earliest preprint arXiv:2401.14341, January 25, 2024. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2024.15
2. Z. Chang and Q. Wang, *Efficient generation of odd order de Bruijn sequence with the same complement and reverse sequences*, arXiv:2408.01794 (August 3, 2024). https://arxiv.org/abs/2408.01794
3. C. S. Burris, F. C. Motta, and P. D. Shipman, *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480 (August 30, 2016). https://arxiv.org/abs/1608.08480
