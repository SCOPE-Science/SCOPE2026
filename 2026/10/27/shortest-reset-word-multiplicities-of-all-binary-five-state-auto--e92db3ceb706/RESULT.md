# Shortest-reset-word multiplicities of all binary five-state automata

## Finding

**Finite classification theorem.** Let \(Q=\{0,1,2,3,4\}\) and \(\Sigma=\{a,b\}\). Choose an ordered pair of arbitrary transition functions \(a,b:Q\to Q\), with all \(5^{10}=9,765,625\) pairs included. For any synchronizing automaton \(A\), let \(r(A)\) be the minimum length of a word \(w\in\Sigma^*\) with \(|Qw|=1\), and let \(c(A)\) count **distinct words** of length \(r(A)\) with this property. The letters are distinguished even if their actions coincide.

Exactly \(8,063,385\) automata synchronize, and exactly \(1,702,240\) do not. The following table gives the **complete** multiplicity spectrum: among synchronizing automata \(c(A)\) has precisely the fourteen listed values, with their displayed frequencies.

| Number of shortest reset words | Automata |
|---:|---:|
| 1 | 5,071,440 |
| 2 | 2,241,065 |
| 3 | 396,000 |
| 4 | 298,120 |
| 5 | 18,720 |
| 6 | 19,680 |
| 7 | 480 |
| 8 | 15,240 |
| 9 | 480 |
| 10 | 240 |
| 12 | 240 |
| 16 | 720 |
| 36 | 720 |
| 64 | 240 |

In particular, \(c(A)\le64\), and equality holds for exactly \(240\) ordered labeled binary automata. All such extremizers are in one orbit under permutation of the five state labels and interchange of the two alphabet letters. An explicit representative is

\[a=(2,3,1,0,0),\qquad b=(2,3,1,4,0),\]

where each tuple gives the images of states \(0,1,2,3,4\). This automaton has \(r(A)=13\), and all its \(64\) shortest reset words are described, with each \(x_i\) independently ranging over \(\{a,b\}\), by

\[w=a\,b\,x_1\,x_2\,a\,x_3\,b\,x_4\,a\,x_5\,x_6\,b\,a.\]

The number with exactly \(j\) occurrences of letter \(a\) is the coefficient of \(z^j\) in \(z^4(1+z)^6\). All such words reset to state \(0\).

The full distribution by minimum reset length is included below. In particular, \(5,071,440\) synchronizing automata admit exactly one shortest reset word; and the \(240\) automata whose threshold is \(16\) all have a unique shortest reset word, while maximum multiplicity occurs at threshold \(13\).

| Reset threshold | Automata | Exactly one shortest word | Total shortest words |
|---:|---:|---:|---:|
| 1 | 31,225 | 31,200 | 31,250 |
| 2 | 1,603,160 | 1,239,360 | 2,028,000 |
| 3 | 2,887,320 | 1,711,680 | 4,620,960 |
| 4 | 1,748,640 | 998,880 | 2,823,360 |
| 5 | 844,320 | 553,200 | 1,208,640 |
| 6 | 443,760 | 240,960 | 715,920 |
| 7 | 235,440 | 141,120 | 395,280 |
| 8 | 132,000 | 76,800 | 221,040 |
| 9 | 70,560 | 43,440 | 119,760 |
| 10 | 36,240 | 18,960 | 74,400 |
| 11 | 11,040 | 6,960 | 17,520 |
| 12 | 10,320 | 4,320 | 36,000 |
| 13 | 5,520 | 2,400 | 26,880 |
| 14 | 2,640 | 1,200 | 12,720 |
| 15 | 960 | 720 | 1,440 |
| 16 | 240 | 240 | 240 |

## Assumptions and scope

Every transition function is allowed: no reachability, minimality, strong connectivity, or distinctness of letters is imposed. Automata are labeled, alphabet letters ordered. A word is counted once as a sequence of letters; two words inducing the same state map are still distinct. For an automaton without a reset word, the multiplicity is undefined, and it contributes only to the nonsynchronizing total. The theorem is solely for \(5\) states and an alphabet of size \(2\).

## Proof

**1. Exhaustive, finite domain.** Encode each transformation \(t:Q\to Q\) by its five base-five digits \(t(0),\ldots,t(4)\) as an integer in \(\{0,\ldots,3124\}\). Nested loops over both integers therefore enumerate every ordered binary automaton exactly once.

**2. Exact forward recurrence.** Represent each nonempty subset of \(Q\) by a five-bit mask. For every transformation \(t\) and subset mask \(S\), compute the image \(t(S)\) by bitwise union of the one-point images. The transition graph has \(31\) nonempty subset vertices, with two directed labeled edges out of every vertex. Initialize breadth-first search at \(Q\) with distance zero and path count one. For each nonfinal subset \(S\) at distance \(d\), and each letter \(t\in\{a,b\}\), the recurrence adds its path count to that of \(t(S)\) if \(t(S)\) is first reached at \(d+1\), or again reached at the same shortest distance. If the image is a singleton, count the edge as a candidate final edge at length \(d+1\); stop after the first singleton level. Because breadth-first search processes vertices by increasing distance, path counts accumulate all and only labeled shortest paths. A labeled path from \(Q\) corresponds bijectively to a word; hence the accumulated singleton counts are exactly \(c(A)\), and the first singleton level is \(r(A)\). Exhausting the graph without a singleton is equivalent to nonsynchronizability.

**3. Independent inverse recurrence.** Independently precompute \(t^{-1}(S)\) for every transformation and every subset. Reverse breadth-first search starts at all five singleton masks, with one path for each singleton; traverse preimage edges, accumulating shortest path counts. The first arrival at \(Q\) records exactly the shortest reset words because each reset word has a unique final state and therefore a unique starting singleton in the reverse enumeration. A count of length \(d\) in either recurrence agrees with the forward recurrence, and its full distribution and multiplicity histogram agree independently over every one of the \(5^{10}\) automata. Both algorithms are supplied as complete standard C++ source code and executed by `verify.py`. The exact integer arrays in the tables are the outputs of these exhaustively defined recurrences. No statistical inference or randomized search occurs.

**4. Extremal orbit and explicit language.** The forward enumeration gives maximum \(64\) and exactly \(240\) extremizers. The witness automaton above has exactly the six-choice family displayed in the finding and no reset word of length below \(13\), as checked by directly evaluating all binary words through length \(13\) on its five states (\(16,382\) words in total). Conjugating both transitions by all \(120\) state permutations and optionally interchanging the two letters yields \(240\) distinct automata. Conjugation and letter interchange preserve \(c(A)\), hence all \(240\) are extremizers. Since exhaustive enumeration found only \(240\), there are no others. Thus the extremal isomorphism orbit is unique.

## Verification

The included `count.cpp` implements forward subset-image breadth-first counting, and `count_reverse.cpp` independently implements inverse-subset breadth-first counting. Run `python3 verify.py` on a system with Python 3 and a C++17 compiler. The verifier builds and runs both complete censuses, compares their whole reset-length and multiplicity tables, checks all cardinality identities, enumerates the witness words through length \(13\), matches all six independent choices, and verifies the symmetry orbit cardinality \(240\). See `COUNTS.json` for the exact numeric data.

## Relationship to prior work

The 2026 survey by Szykuła emphasizes reset thresholds and their distribution in automata, rather than the multiplicity of different shortest reset words for every small binary automaton. Kisielewicz, Kowalski and Szykuła (2013/2015) describe algorithms that find shortest reset words and estimate their length in random automata; their numerical experiment measures lengths rather than the exact five-state **word multiplicity** histogram or its extremal orbit. Their later small-automata studies concern length bounds and slow-reset classes. These results motivate exact counting of *all* optimal words but do not imply the histogram: two automata can have the same shortest reset length and different numbers of minimizers. The supplied census distinguishes these.

## Limitations

The enumeration is complete only for ordered binary five-state transition tables. It does not prove a formula for other state counts, alphabets or restricted classes. All numbers are exact, but exhaustive finite computations rely on the reproducibility of the two included implementations and independent witness checks; the inclusion of source code permits replication but is not an independent external mathematical audit. The novelty comparison is limited to accessible indexed primary literature; an unindexed earlier identical census cannot be ruled out.

## References

1. Marek Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first publicly posted 25 August 2026. https://arxiv.org/abs/2608.24245
2. Andrzej Kisielewicz, Jakub Kowalski and Marek Szykuła, *Computing the shortest reset words of synchronizing automata*, *Journal of Combinatorial Optimization* **29** (2015), 88–124, first published online 17 November 2013, doi:10.1007/s10878-013-9682-0. https://link.springer.com/article/10.1007/s10878-013-9682-0
3. Andrzej Kisielewicz, Jakub Kowalski and Marek Szykuła, *Experiments with Synchronizing Automata*, arXiv:1607.04025, 2016. https://arxiv.org/html/1607.04025v1
4. Jakub Kowalski and Marek Szykuła, *The Černý conjecture for small automata: experimental report*, arXiv:1301.2092, 2013. https://arxiv.org/abs/1301.2092
