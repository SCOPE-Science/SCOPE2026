# The unique Don-bound obstruction and shortest-reaching-word spectrum at eight states

## Finding

Let \(Q=\{0,1,\ldots,7\}\) and let a **binary completely reachable automaton** be a deterministic complete automaton over two letters for which every nonempty state subset is the image of \(Q\) under some word. Write \(d(S)\) for the minimum length of a word mapping \(Q\) exactly onto \(S\). An **exception** is a nonempty proper set \(S\) with \(d(S)>8(8-|S|)\).

Every eight-state binary completely reachable automaton containing an exception has **exactly one exceptional subset**. It has cardinality \(6\), is the complement of an antipodal state pair, and has \(d(S)=17\). Fix the cyclic letter as \(a:i\mapsto i+1\pmod8\), and write \(b\) for the necessarily rank-seven letter. Among the \(1{,}093{,}632\) completely reachable normalized maps, exactly \(544\) have such an exception. The exact distribution of the **number of distinct shortest reaching words** for the unique exceptional subset is

| Shortest reaching words | Normalized maps | Classes under cyclic relabeling |
| ---: | ---: | ---: |
| \(2\) | \(384\) | \(48\) |
| \(3\) | \(96\) | \(12\) |
| \(4\) | \(32\) | \(4\) |
| \(5\) | \(32\) | \(4\) |
| **Total** | **\(544\)** | **\(68\)** |

The \(68\) total is already known from Zhu's census and is reproduced here for control; **the contribution is the unique-per-automaton obstruction and optimal-word multiplicity partition**, not the historical total \(68\).

## Assumptions and scope

All words are ordinary words over the two *distinguished* letters, not words modulo letter relations. Their action is read left-to-right. Distinct shortest words are counted individually even when their induced transformations agree. Normalization uses a relabeling that sends the unique cyclic letter to \(a:i\mapsto i+1\pmod8\); cyclic translations are the remaining label symmetries. Binary completely reachable automata have a cyclic letter, as established in the existing literature; the other letter must have rank seven because some seven-state subset must be a first rank-loss image. Thus the normalized class reduces to permutations of six outputs and one duplicate output. The theorem is only about eight states and exactly two letters.

## Proof

**1. Exhaustive normal form.** By the cited circularity theorem, fix the cyclic letter \(a\). The other letter \(b\) has exactly one pair of colliding domain states, exactly one excluded output, and exactly one duplicated output; its remaining six domain states map bijectively to the six other output states. Conversely every rank-seven map is uniquely specified by these data. Therefore the number of candidates is
\[
\binom82\cdot8\cdot7\cdot6!=1{,}128{,}960.
\]
Automata with other-letter rank below seven cannot be completely reachable, since no word can have rank seven. The normalization has no missing cases.

**2. Exact shortest-image paths.** Represent every subset by an eight-bit mask. The action of \(a\) rotates the mask; that of \(b\) is the bitwise image under its transition table. Starting from the full mask \(255\), breadth-first search over the \(255\) nonempty masks computes all finite distances \(d(S)\). Each edge corresponds to appending exactly one alphabet letter, so breadth-first distances equal word lengths without approximation. An automaton is completely reachable exactly when all \(255\) masks are visited. Among the enumerated \(1{,}128{,}960\) rank-seven maps, the exact number passing this test is \(1{,}093{,}632\).

**3. All exceptional subsets.** For each completely reachable map, compare each \(d(S)\) with \(8(8-|S|)\). The complete census finds \(544\) maps with at least one violation and \(0\) violations at subset sizes different from six. Each of the \(544\) maps has exactly one violating six-element subset, at distance exactly \(17\). The only target masks are \(119,187,221,238\), each for exactly \(136\) maps; each mask omits a pair differing by four modulo eight. In every exceptional map, the excluded and duplicated output states of \(b\) likewise differ by four. Because all rank-seven maps are enumerated, these are finite exhaustive statements, not extrapolations.

**4. Word multiplicity.** Let \(c(Q)=1\). After determining all distances, propagate counts along exactly those labeled subset edges satisfying \(d(T)=d(S)+1\), using \(c(T)\mathrel{+}=c(S)\) for each letter separately. Every shortest reaching word has a unique penultimate prefix and final letter, so induction on distance shows \(c(S)\) is precisely the number of shortest reaching words. The histogram over the \(544\) exceptional targets is \(384,96,32,32\) at multiplicities \(2,3,4,5\), respectively. An independently implemented wavefront recurrence reproduces the histogram. An independent Python breadth-first count verifies the \(68\) class representatives.

**5. Label quotient.** Because the cyclic letter is uniquely distinguished by its permutation rank, normalization permits only cyclic rotations of the eight labels (and renaming the alphabet to restore the cyclic-letter convention). The \(544\) exceptional maps partition into \(68\) rotation orbits of size eight. Dividing the four normalized counts by eight yields \(48,12,4,4\). Independent orbit generation from the generated representative list confirms the orbit size and the counts directly.

For an explicit multiplicity-five example, take \(b=(6,2,4,3,5,3,1,0)\), meaning \(b(i)\) is the displayed coordinate. Its unique exceptional six-element subset has bitmask \(187\), shortest reaching length \(17\), and precisely five shortest reaching words. One of them is `baaaaaaabaaaabaaa`.

## Verification

The included `reach_census.cpp` enumerates all rank-seven second-letter maps from integer encodings and computes exact forward subset distances. The separately written `independent_waves.cpp` enumerates maps by collision pair, excluded output, duplicated output, and bijection, while counting shortest paths via a distance-wavefront recurrence. `violation8.cpp` extracts all \(68\) cyclic representatives; `orbit_check.py` independently generates rotation orbits and recalculates shortest reaching-word multiplicities. The exact representative list is `violation8.txt`. Compile the C++ programs using a standards-compliant C++17 compiler and run with argument `8` for `reach_census.cpp`; run `orbit_check.py` with `violation8.txt` in the working directory. Text/JSON outputs from the actual executions are embedded. Independently implemented enumerators agree on \(1{,}128{,}960\) maps, \(1{,}093{,}632\) completely reachable maps, \(544\) exceptional maps, the absence of violations at other subset sizes, and the four shortest-word multiplicities. Exhaustiveness comes from the proven normal form and traversal of all maps; running an illustrative case alone would not prove it.

## Relationship to prior work

Zhu (2024) disproved Don's reachability conjecture for binary completely reachable automata and reported **\(68\)** nonisomorphic eight-state counterexamples, as well as an explicit obstruction. That paper establishes the pre-existing extremal context but does not give the above optimal-reaching-word multiplicity census or the uniqueness of the exceptional subset in each eight-state counterexample. Szykuła (2026) provides the recent study of synchronization invariants and motivation for exact finite profiles. A related research record on two-defect reachability in cyclic defect-one automata already characterizes where some codimension-two reachability bounds may fail; it does not state the above cardinalities of distinct optimal reaching words. The new result is not the known \(68\)-class total, nor the general possibility of antipodal obstructions.

## Limitations

The proof is an exhaustive, independently reproduced finite classification, not a uniform theorem for all state counts. It applies to binary completely reachable deterministic automata on exactly eight states. A 2024 census already gives the total \(68\) exceptional isomorphism classes; novelty is restricted to the uniqueness and shortest-reaching-word multiplicity stratification. The associated research-record full text on two-defect reachability was not accessible here; an unindexed equivalent enumeration remains a priority risk. The checks are not an independent external audit or formal machine proof.

## References

- M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first public 2026-08-25. https://arxiv.org/abs/2608.24245
- Y. Zhu, *Around Don's conjecture for binary completely reachable automata*, arXiv:2402.19089, first public 2024-02-29, especially Section 4 and Table 1. https://arxiv.org/abs/2402.19089
- *Two-defect reachability in cyclic defect-one automata*, research-record abstract, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-defect-reachability-in-cyclic-defect-one-automata--3d0ad329ab1e. Only its indexed abstract was consulted; its full text was not examined.
