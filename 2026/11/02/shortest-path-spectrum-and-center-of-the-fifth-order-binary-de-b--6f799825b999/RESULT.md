# Shortest-path spectrum and center of the fifth-order binary de Bruijn cross-join graph

## Finding

For the graph whose vertices are all rotation-equivalence classes of binary de Bruijn sequences of order \(5\), and whose edges are legal cross-join transformations, the graph has \(2048\) vertices, radius \(5\), diameter \(7\), and exactly \(48\) centers. The exact numbers of unordered pairs at respective distances \(1,2,3,4,5,6,7\) are

\[
(38704,305376,758800,710976,254800,27104,368).
\]

The eccentricity spectrum, written as \((\text{eccentricity},\text{number of sequences})\), is \((5,48),(6,1264),(7,736)\). Every one of the \(736\) sequences of eccentricity \(7\) has exactly one opposite sequence at distance \(7\), yielding precisely \(368\) unordered diametral pairs. In particular, the center and diameter distinguish meaningful configurations even though the graph is connected.

This claim is restricted to the order-five *metric census*. Connectivity, the underlying cross-join technique, and the related Hamming-distance descent are credited to earlier work, rather than claimed as new.

## Assumptions and scope

A binary de Bruijn sequence of order \(5\) is a cyclic binary word of length \(32\) in which every binary five-block occurs exactly once. Cyclic rotations represent one configuration; complementation or reversal is **not** quotiented out. Model a configuration as the unique Hamiltonian directed cycle in the binary de Bruijn digraph on states \(\{0,1,\ldots,31\}\) rooted for encoding at state \(0\).

Let \(z=v\bmod 16\). For a Boolean table \(f:\{0,\ldots,15\}\to\{0,1\}\), define its permutation candidate on these states by

\[
T_f(v)=2z+\left(\lfloor v/16\rfloor\oplus f(z)\right),
\]

where \(\oplus\) is XOR. Write the table as an integer mask \(F=\sum_{z=0}^{15} 2^z f(z)\), solely for reproducible encoding. A mask is admitted if and only if iterating \(T_f\) from \(0\) visits all \(32\) states and returns to \(0\) without repetition. There are exactly \(2048\) such masks.

A legal cross-join toggles the table at two **distinct** suffix positions, thus replacing \(F\) by \(F\oplus 2^i\oplus2^j\), for \(0\le i<j\le15\), *provided that both tables produce full cycles*. This coincides with switching successors at two pairs of conjugate states in the classical cross-join definition. The graph is undirected and simple, and its distance counts the minimum number of those legal moves. The present census involves no arbitrary restriction of allowable pairs.

## Proof

**1. Exhaustive state description.** At each suffix \(z\), the two states \(z\) and \(z+16\) must have complementary outgoing last bits. Otherwise their out-neighbors would coincide, precluding a Hamiltonian cycle. Hence every Hamiltonian cycle has one and only one table \(f\) in the stated form. Conversely, a table with one full orbit is a de Bruijn cycle. Testing each of the \(65536\) masks for a single \(32\)-state orbit therefore enumerates the entire domain with no isomorphism quotient. The exhaustive verifier finds exactly \(2048\) valid masks.

**2. Metric reduction.** For two valid tables \(f,g\), write \(h=\#\{z:f(z)\ne g(z)\}\). Each legal move toggles exactly two positions, so any path has length at least \(h/2\). The number \(h\) is even: all valid one-cycle permutations have the same parity, while toggling one table bit exchanges the images of two states and changes parity. To establish the matching upper bound, fix a disagreeing suffix \(i\). The single image transposition at \(i\) splits the one-cycle \(T_f\) into two disjoint directed cycles. Some other disagreeing suffix \(j\) must have its two conjugate states in different split cycles: otherwise all other differing image swaps preserve each of those two vertex sets, contradicting that their combined result \(T_g\) is a single cycle. Switching at \(j\) merges the two cycles, producing another valid table that agrees with \(g\) at both \(i\) and \(j\). Induct on \(h/2\). Therefore

\[
d(f,g)=\tfrac12\#\{z:f(z)\ne g(z)\}=\tfrac12\operatorname{wt}(F\oplus G).
\]

The constructive descent belongs to the established cross-join theory [1,2]; here it permits an independent and exhaustive metric census, not a new general theorem.

**3. Exhaustive finite census.** Generate the ordered list \(\mathcal F\) of the \(2048\) valid feedback masks by the complete orbit test in Step 1. For each of the \(\binom{2048}{2}=2096128\) unordered pairs, evaluate the exact integer \(\tfrac12\operatorname{wt}(F\oplus G)\). The resulting seven-class distribution is

\[
(38704,305376,758800,710976,254800,27104,368).
\]

For each \(F\), take the maximum over all \(G\in\mathcal F\). The resulting eccentricity distribution is exactly \((5:48,6:1264,7:736)\), proving the radius, diameter, and center count. The two fixed table bits at suffixes \(0\) and \(15\) are both \(1\) for every valid table; therefore at distance \(7\), two valid tables must differ at *all* remaining \(14\) suffixes, so the only possible partner is \(G=F\oplus\texttt{0x7ffe}\). A complete membership check finds exactly \(736\) masks with that partner, and hence \(368\) pairs.

**4. Independent graph computation.** Separately enumerate the \(2048\) directed Hamiltonian cycles with a depth-first search rooted at zero, rather than enumerate feedback masks. Determine adjacency directly from whether two conjugate-state chords interlace around the cycle. This creates \(38704\) edges. Breadth-first searches from **all** \(2048\) roots produce the same seven distance counts and the same \(48\)-center/\(7\)-diameter results. The two representations are independent finite constructions of the objects and operations, and the explicit BFS additionally verifies that the Hamming metric is not merely a lower bound.

## Verification

Run `python3 verify_truth_table.py` and `python3 verify_hamiltonian_cycles.py` with Python 3.8 or later. These standalone standard-library scripts implement, respectively, exhaustive truth-table orbit testing plus pairwise distance descent, and an independent Hamiltonian-cycle enumeration plus chord-interlacement adjacency and all-root BFS. Both must terminate with four printed `PASS` lines and no assertion failure. There are no external datasets, random seeds, heuristic cutoffs, or omitted states.

The first program examines exactly \(65536\) Boolean feedback tables. The second independently explores exactly \(92636\) depth-first recursion nodes. The eight success markers, including `RADIUS5_CENTER48_DIAMETER7_ANTIPODE_PAIRS368_PASS` and `INDEPENDENT_RADIUS5_CENTER48_DIAMETER7_PASS`, are reproducible within the two included scripts; the proof rests on the enumerations and the justified graph constructions rather than on printed logs alone.

## Relationship to prior work

Mykkeltveit and Szmidt [1] explain cross-joining through nonlinear feedback shift registers and give the fundamental connectivity/descent framework. Alhakim [2] studies the cross-join graph, proves connectedness and Hamiltonicity, and publishes a degree-frequency table for this exact fifth-order family. Therefore the existence of a path, the general Hamming descent, the graph size, and the degree distribution or aggregate edge count are **not** asserted to be new. The new restricted claim is the *complete shortest-path spectrum*, its radius and diameter, its \(48\) centers, and the exact \(368\) diametral pairs. The cross-join method for multicycles [3] concerns a broader object and likewise does not supply this distance census.

## Limitations

The statement concerns binary order \(5\) with cyclic rotations identified and all named suffix positions retained; it is not a formula for general order or for nonbinary or multi-de Bruijn sequences. The all-pairs metric formula has a literature antecedent in cross-join connectivity arguments; the original contribution claimed is its exact finite metric census and its extremal structure at order five. The calculation is exhaustive in its stated finite domain; it neither proves that no historic table contains an equivalent census nor represents independent scholarly verification.

## References

[1] Johannes Mykkeltveit and Janusz Szmidt, *On cross joining de Bruijn sequences*, Cryptology ePrint Archive 2013/760, https://eprint.iacr.org/2013/760 (record received 2013-11-21).

[2] Abbas Alhakim, *Hamiltonicity of the Cross-Join Graph of de Bruijn Sequences*, arXiv:1805.12059 (submitted 2018-05-30), https://arxiv.org/abs/1805.12059.

[3] Abbas Alhakim and Janusz Szmidt, *Multi de Bruijn Sequences and the Cross-Join Method*, Mathematics **11** (2023), 1262, https://doi.org/10.3390/math11051262.
