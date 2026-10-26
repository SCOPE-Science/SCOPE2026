# Complete reaching-diameter spectrum of binary five-state completely reachable automata

## Finding

Consider ordered binary transition tables on \(Q=\{0,1,2,3,4\}\), counted with the two letters distinguished and the states labeled. For any nonempty \(S\subseteq Q\), let \(d(S)\) be the least nonnegative length of a word \(w\) satisfying \(Qw=S\), with \(d(S)=\infty\) when none exists. An automaton is *completely reachable* when all \(31\) nonempty subsets are reachable. For such an automaton its **reaching diameter** is \(R=\max_{\varnothing\neq S\subseteq Q}d(S)\).

Of the \(5^{10}=9,765,625\) ordered binary automata, exactly \(57,600\) are completely reachable. The complete reaching-diameter distribution is:

| Reaching diameter \(R\) | Labeled automata | Classes up to relabeling and letter exchange |
| ---: | ---: | ---: |
| 7 | 1,440 | 6 |
| 8 | 4,800 | 20 |
| 9 | 9,360 | 39 |
| 10 | 8,400 | 35 |
| 11 | 11,760 | 49 |
| 12 | 8,160 | 34 |
| 13 | 4,800 | 20 |
| 14 | 4,800 | 20 |
| 15 | 1,200 | 5 |
| 16 | 1,200 | 5 |
| 17 | 960 | 4 |
| 18 | 480 | 2 |
| 20 | 240 | 1 |
| **Total** | **57,600** | **240** |

The range is exactly \(\{7,8,\ldots,18,20\}\): there is a **gap at \(19\)**. Exactly \(240\) labeled automata attain the maximum \(20\), and all are isomorphic, allowing interchange of input letters, to
\[
a=(1,2,3,4,0),\qquad b=(0,1,2,3,0).
\]
For this representative, the maximum of \(d(S)\) over subsets of cardinality \(k=1,2,3,4\) is, respectively, \(20,15,10,5\). An explicit word of length \(20\) mapping the full set to singleton \(\{4\}\) is `baaaabaaaabaaaabaaaa`, confirming the sharp maximum when paired with the exhaustion certificate.

## Assumptions and scope

Transition maps are total deterministic functions \(Q\to Q\); two distinct input symbols may induce any maps, including coincident maps. An isomorphism may permute the five states and swap the two letters. The cardinality-specific extremal statements are maxima over all completely reachable binary five-state automata and all target subsets of that size. No claim about more states or alphabets is made.

## Proof

**Normal form and counting.** For \(n\ge3\), complete reachability of a binary automaton requires a rank-\(n-1\) letter and a full cyclic permutation letter (Casas--Volkov and Hoffmann, references below). The defect-one rank is \(4\) when \(n=5\). Conversely, if \(a\) acts as a five-cycle and \(b\) has rank \(4\), then the omitted output state and the duplicated output state of \(b\) are distinct. Their nonzero cyclic distance is coprime to \(5\), so Don's coprime circular criterion ensures every nonempty subset is reachable. There are \(4!=24\) five-cycles on \(Q\) and \(5\binom52 4!=1200\) rank-\(4\) maps. Either letter may be the cycle. Therefore \(2\cdot24\cdot1200=57,600\) automata are completely reachable.

**Exhaustive distance certificate.** Encode \(S\subseteq Q\) as \(\sum_{{q\in S}}2^q\), and encode each map as its five values in base \(5\). For all \(3125^2\) ordered transition pairs, compute subset images and breadth-first search on the directed graph with vertices the \(31\) nonempty subsets, beginning at mask \(31\). A vertex's first-discovery distance is exactly \(d(S)\): each edge appends one letter, so breadth-first search cannot overestimate a shortest path, and every word traces a path. Classify a pair as completely reachable precisely when all \(31\) vertices are discovered; in that case tally the largest finite distance. The exact histogram printed by `census.cpp` is the displayed distribution, including \(R=19:0\), and its independent normalized re-enumeration is checked by `verify_canonical.py`.

**No overcount of isomorphism types.** Up to conjugation each five-cycle is \(a(i)=i+1\pmod5\), leaving its centralizer, the \(5\) cyclic shifts, acting on \(b\). Each rank-\(4\) map has a unique omitted output state. Any shift commuting with it must fix that state, and only the identity shift does so. Consequently each normalized class contains exactly \(5\) rank-\(4\) maps, giving \(1200/5=240\) classes. In the full labeled class, swapping letters is the only extra option, and each orbit has size \(5!\cdot2=240\). The second certificate explicitly computes the canonical representative of every rotation orbit. Its histogram has one diameter-\(20\) class, exactly \(b=(0,1,2,3,0)\), demonstrating extremal uniqueness.

**Sharp diameter and subset-size maxima.** The breadth-first exploration simultaneously records the largest \(d(S)\) among sets of each size. The resulting maxima over all \(57,600\) completely reachable automata are \(20,15,10,5\) for subset sizes \(1,2,3,4\); the canonical check verifies the same maxima over all \(1200\) normalized maps. The displayed Černý-type representative reaches all four bounds. Since the two enumerations are independently coded, the agreement supplies a cross-check of map enumeration, subset actions, and breadth-first distance calculations.

## Verification

With a C++17 compiler (GNU extensions accepted for `census.cpp`) and Python 3.10 or later, run `g++ -std=c++17 -O3 census.cpp -o census && ./census` and `python3 verify_canonical.py`. The C++ code checks all \(9,765,625\) transition pairs. The Python code, which independently constructs subset transitions using set-frontier breadth-first search, checks all \(1200\) normalized rank-\(4\) maps, plus their cyclic conjugacy classes. The Python script asserts the exact normalized histogram, complete reachability, one extremal class, and subset-size maxima, then prints `VERIFY_OK`. The checks are entirely finite; nothing is extrapolated beyond the specified five-state binary domain.

## Relationship to prior work

Szykuła's August 2026 survey motivates the study of sharp and statistical synchronization phenomena. Complete reachability and reaching thresholds were developed by Ferens and Szykuła, and a characterization of binary complete reachability appears in Casas and Volkov. Don's coprime-distance criterion already proves reachability, with the upper bound \(5(5-|S|)\), for every normalized map in this census; the sharp \(20\) attainable by the Černý family is therefore **not independently new**. Zhu's study of Don's conjecture tabulates the number of eight-state (and larger) violation classes but does not determine this five-state full reaching-diameter spectrum. The present contribution is the complete **distribution, exclusion of \(19\), and uniqueness of the extremal isomorphism type**. Previously established reachability and upper-bound claims are credited rather than claimed as new.

## Limitations

This is an exact finite census, not a general formula for arbitrary state counts. The structural reduction uses known results, and the new distribution and uniqueness statements depend on reproducible finite computation. Equivalent unpublished or unindexed enumerations remain possible; the cited primary works and relevant indexed mathematical records did not establish the same histogram or imply the \(19\)-gap. No independent external audit is asserted.

## References

1. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first posted 25 August 2026.
2. D. Casas and M. V. Volkov, *Binary completely reachable automata*, arXiv:2205.09404 (2022), Sections 2--3.
3. R. Ferens and M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956 (2022), Sections 1--2.
4. Y. Zhu, *Around Don's conjecture for binary completely reachable automata*, arXiv:2402.19089 (2024), Sections 1 and 4.
5. S. Hoffmann, *State Complexity of the Set of Synchronizing Words for Circular Automata and Automata over Binary Alphabets*, arXiv:2011.14404 (2020), Sections 2--3 (including the statement of Don's criterion).
