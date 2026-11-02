# Complete reset-threshold spectrum for eight-state circular defect-one automata

## Finding

Let \(Q=\mathbb{Z}/8\mathbb{Z}\). Fix \(a(i)=i+1\pmod 8\), and let \(b:Q\to Q\) range over all maps of rank exactly seven. The reset threshold \(\tau(b)\) is the length of a shortest word over \(\{a,b\}\) mapping all eight states to a singleton; put \(\tau(b)=0\) if no such word exists. We count pairs \((a,b)\) up to state relabelings that retain this fixed \(a\), i.e., cyclic rotations of state labels. Every such orbit has exactly one representative for which \(b(Q)=\{1,2,3,4,5,6,7\}\).

**Exact complete spectrum.** Write \(H(t)\) for the number of normalized representatives with \(\tau(b)=t\). The following is the full nonzero support of \(H\), with zero values at all other arguments. The table is also supplied as `spectrum.csv`.

| Reset threshold | Cyclic-rotation classes |
|---:|---:|
| 0 | 1,856 |
| 7 | 5,040 |
| 8 | 1,587 |
| 9 | 4,613 |
| 10 | 7,401 |
| 11 | 9,777 |
| 12 | 11,183 |
| 13 | 15,688 |
| 14 | 13,690 |
| 15 | 13,831 |
| 16 | 11,868 |
| 17 | 10,663 |
| 18 | 10,041 |
| 19 | 7,989 |
| 20 | 5,152 |
| 21 | 3,356 |
| 22 | 1,855 |
| 23 | 1,450 |
| 24 | 1,346 |
| 25 | 1,087 |
| 26 | 807 |
| 27 | 507 |
| 28 | 249 |
| 29 | 57 |
| 30 | 13 |
| 31 | 8 |
| 32 | 1 |
| 34 | 1 |
| 37 | 1 |
| 43 | 1 |
| 44 | 1 |
| 49 | 1 |

Thus there are exactly \(141120\) classes, of which \(139264\) are synchronizing and \(1856\) are not. There are \(31\) distinct positive threshold values. Among synchronizing classes the exact mean threshold is \(2063331/139264\), and exactly three classes have threshold at least \(40\), one each at \(43,44,49\). These three normalized maps (with outputs listed for inputs \(0,1,\ldots,7\)) are `12345671`, `22345671`, and `11234567`, respectively. More high-threshold representative tuples appear in `rare_witnesses.csv`.

The complete histogram, not the classical bound \(49\), is the claim evaluated for originality. A non-synchronization count and its congruence explanation accompany the classification; the general congruence-to-synchronization principle is previously known and is not claimed as a new theorem.

## Assumptions and scope

All states are labeled before quotienting, both transition functions are total, and exactly two distinct input letters are used. The first is the fixed directed eight-cycle. The second is **any** rank-seven transformation, not just a simple idempotent or a Černý-family transformation. Relabelings are precisely those commuting with \(a\), namely the eight rotations. Letter exchange is not an equivalence because the designated cycle letter is fixed. The value zero denotes nonsynchronizability, not a zero-length resetting word. Normalized maps are represented by eight output digits from \(1\) through \(7\) in input order.

## Proof

**1. Exhaustive parameterization without duplication.** Every rank-seven transformation omits exactly one output state. Conjugating by a unique power of the eight-cycle moves that state to \(0\). A normalized map has a unique output \(d\in\{1,\ldots,7\}\) with two preimages, a unique unordered pair of preimage positions, and a bijection of the other six input positions to the six remaining outputs. The number is exactly

\[
7\binom{8}{2}6!=141120.
\]

These data uniquely specify the map. Its omitted output makes every normalized cyclic-conjugacy class singleton within the normalized parameterization; hence there is no unaccounted symmetry division.

**2. Exact finite-state reset test.** Encode a subset \(S\subseteq Q\) by the eight-bit mask \(M(S)=\sum_{i\in S}2^i\). Define the two subset transitions

\[
A(S)=\{i+1\bmod8:i\in S\},\qquad B(S)=\{b(i):i\in S\}.
\]

Breadth-first search starting at \(Q\) and following both transitions visits every reachable subset (there are only \(255\) possible nonempty states). Its first singleton is reached after exactly \(\tau(b)\) transitions, by the defining invariant of breadth-first search; if none occurs, no reset word exists. `verify.cpp` visits all \(141120\) maps in the bijective parameterization and counts the threshold of each. It asserts the total, congruence counts and key boundary values, and prints the entire histogram. Its transition map uses the low-set-bit recurrence, with the cycle image computed by an eight-bit rotation.

The independent **enumeration-method cross-check** `crosscheck.cpp` instead iterates over all \(8^8=16777216\) base-eight output arrays, retains exactly those having image mask `254`, and executes a separately written breadth-first search that applies the letters by scanning all eight input positions for each subset. It counts \(141120\) retained maps and reproduces every histogram coefficient of `spectrum.csv`. Both methods enumerate the *entire* finite space, rather than a sample or a truncated search.

**3. Independent check of the zero class.** Any congruence preserved by the full eight-cycle is a partition into residue classes modulo a divisor of eight. The nontrivial possibilities are precisely modulo two and modulo four. Because \(b\) has rank seven, any induced map on one of these quotients, if well defined, is automatically a permutation; hence this congruence cannot be synchronized. The normalized numbers of \(b\) preserving the modulo-two and modulo-four congruences are, respectively,

\[
2\cdot4!\cdot(3\cdot\binom{4}{2}\cdot2!)=1728,
\qquad 4!\cdot(2!)^3=192.
\]

Their intersection has \(2(2!)^2\cdot(2!)^3=64\) maps. Inclusion-exclusion gives \(1728+192-64=1856\) provably nonsynchronizing maps. Independently, both exhaustive subset searches find *exactly* \(1856\) nonsynchronizing maps, so these congruences explain all zero-threshold cases. This last completeness observation is also consistent with Volkov's published theorem that a primitive automaton with a defect-one letter synchronizes; it is not asserted as historically new.

**4. Labeled interpretation.** Each normalized map has eight distinct state-rotation relabelings, since any relabeling fixing the omitted state must be the identity. Therefore the distribution for maps with the same fixed labeled cycle, **without** quotienting by state rotations, is \(8H(t)\) for every \(t\). In total, there are \(1128960\) labeled rank-seven maps, \(14848\) nonsynchronizing and \(1114112\) synchronizing.

## Verification

Compile and execute from the directory containing the included standalone files:

```sh
c++ -std=c++17 -O2 verify.cpp -o verify
./verify > verify_output.txt
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck > crosscheck_output.txt
```

The expected respective terminal markers are `VERIFY_OK` and `CROSSCHECK_OK`. Both programs print a `threshold,classes` table matching all \(32\) rows of `spectrum.csv`. The first also prints the congruence counts and representative high-threshold tuples. The complete runs were executed and the spectra compared coefficient by coefficient before this result was recorded. Details and limitations appear in `VERIFICATION.md`.

## Relationship to prior work

Černý's example and the known circular-automaton upper bound already provide the extremal value \(49\) for eight states. Trahtman's experimental work gives the largest noncritical binary eight-state reset threshold as \(44\), and studies extremal small automata, not the histogram here. De Bondt, Don and Zantema explicitly list threshold frequencies for automata of at most six states and discuss larger critical cases, but do not supply the present all-rank-seven, fixed-eight-cycle coefficient table. Don establishes sufficient structural synchronization criteria for circular automata. Volkov's later general result proves primitivity implies synchronization in the presence of a defect-one letter and thus conceptually covers the nonsynchronizing congruence test; **the zero-class criterion alone is not a novelty claim**. Kisielewicz, Kowalski and Szykuła give general shortest-reset-word algorithms and sampled distributions for larger automata, but not this exhaustive conditional eight-state spectrum. The precise count at each positive threshold is not logically implied by any of these results.

## Limitations

This is a finite exact classification, not an all-state-number theorem. It assumes a distinguished forward eight-cycle, a second letter of rank precisely seven, and the stated rotation equivalence. It does not give shortest reset words for each class in the table, enumerate arbitrary pairs of transformations, or determine random-automaton asymptotics. The scientific verification is self-review, not independent external mathematical validation. An unpublished or unindexed historical computer-generated table could contain the coefficients and remains a priority risk; checking named published articles cannot certify historical uniqueness.

## References

- A. N. Trahtman, *An efficient algorithm finds noticeable trends and examples concerning the Černý conjecture*, MFCS 2006; open preprint https://arxiv.org/abs/0709.1197 (first posted 2007-09-08).
- A. Kisielewicz, J. Kowalski, and M. Szykuła, *Computing the shortest reset words of synchronizing automata*, Journal of Combinatorial Optimization, online 2013-11-17; https://doi.org/10.1007/s10878-013-9682-0.
- H. Don, *The Černý conjecture and 1-contracting automata*, open preprint first posted 2015-07-22; https://arxiv.org/abs/1507.06070.
- A. Kisielewicz, J. Kowalski, and M. Szykuła, *Experiments with Synchronizing Automata*, open preprint first posted 2016-07-14; https://arxiv.org/abs/1607.04025.
- M. de Bondt, H. Don, and H. Zantema, *Slowly synchronizing automata with fixed alphabet size*, open preprint first posted 2016-09-22; https://arxiv.org/abs/1609.06853.
- M. V. Volkov, *Synchronization of primitive automata*, open preprint first posted 2023-06-23; https://arxiv.org/abs/2306.13317.
