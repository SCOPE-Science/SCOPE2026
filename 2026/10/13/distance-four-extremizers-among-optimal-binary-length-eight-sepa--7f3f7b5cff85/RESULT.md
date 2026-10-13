# Distance-four extremizers among optimal binary length-eight separating systems

## Finding
A binary \((2,1)\)-separating system is a set \(C\subseteq\{0,1\}^8\) such that for every three distinct words and every choice of one as the outsider, some coordinate has the other two words equal and the outsider different. Equivalently, \(C\) is a binary \(2\)-frameproof code, or a general-position set in the eight-dimensional hypercube.

The known maximum cardinality is \(10\). Among these maximum systems, the largest possible minimum Hamming distance is \(4\). Exactly \(1{,}182{,}720\) labeled unordered maximum systems have minimum distance \(4\). Under the full Hamming-isometry group \((C_2)^8\rtimes S_8\), of order \(10{,}321{,}920\), they split into exactly three orbits, with orbit sizes
\[
215{,}040,\qquad 322{,}560,\qquad 645{,}120,
\]
and corresponding stabilizer orders
\[
48,\qquad 32,\qquad 16.
\]
Representatives are the following ten-word sets:

```text
R1 = {00000000,00001111,00110011,00111100,01010101,01011010,10010110,10011001,11100001,11101110}
R2 = {00000000,00001111,00110011,00111100,01010101,01101010,10010110,10101001,11011000,11100100}
R3 = {00000000,00001111,00110011,00111100,01010101,01101010,10010110,10101001,11011000,11100111}
```

## Assumptions and scope
The ambient alphabet and coordinates are labeled. A labeled unordered system is therefore a ten-element subset of the fixed cube \(\{0,1\}^8\), not an ordered list of codewords. The equivalence group consists exactly of independent global bit translation by a word of \(\{0,1\}^8\) followed by a permutation of the eight coordinates. No complementations beyond those induced by translation and no nonlinear cube automorphisms are added; this is the full Hamming-isometry group of the binary cube.

The result refines the previously established equality \(m_2(8,2)=10\). It does not claim that the maximum cardinality \(10\) is new.

## Proof
For any ten binary words of length eight with minimum Hamming distance at least \(5\), the sum of all pairwise distances is at least \(45\cdot5=225\). In one coordinate, if \(s\) of the ten words contain a one, the contribution to that sum is \(s(10-s)\le25\). Hence all eight coordinates contribute at most \(8\cdot25=200\), a contradiction. Thus every ten-word system has minimum distance at most \(4\). Each displayed representative is directly checked to be separating and to have minimum distance \(4\), so the largest attainable minimum distance among maximum systems is exactly \(4\).

It remains to count and classify the distance-four equality cases. Translation by any binary word preserves both separation and Hamming distance. The exact search in `artifacts/verify.cpp` enumerates all ten-word separating systems of minimum distance at least \(4\) that contain `00000000`; it finds exactly \(46{,}200\). If \(N\) denotes the total number of labeled unordered such systems, translation transitivity on the \(256\) cube vertices gives the incidence identity
\[
10N=256\cdot46{,}200,
\]
so
\[
N=1{,}182{,}720.
\]

For each displayed representative, the same verifier enumerates all coordinate permutations and the only translations that can possibly stabilize a set. The stabilizer orders are \(48\), \(32\), and \(16\). Orbit-stabilizer therefore gives orbit sizes \(215{,}040\), \(322{,}560\), and \(645{,}120\). The multisets of per-codeword distance profiles distinguish the three representatives, so these orbits are disjoint. Their sizes sum to
\[
215{,}040+322{,}560+645{,}120=1{,}182{,}720=N,
\]
which proves that the three orbits exhaust every distance-four maximum system.

## Verification
`artifacts/verify.cpp` is a standalone C++17 program. It reconstructs the separation condition from the definition, performs the exhaustive search containing `00000000`, validates all three representatives, enumerates their stabilizers in the full binary Hamming-isometry group, checks the orbit sizes and their sum, and verifies that distance-profile invariants separate the three representatives. Its recorded output is in `artifacts/verification_output.txt`.

The known cardinality maximum \(10\) was independently checked against the complete normalized-pair proof and exact verifier published with the cited length-eight result: minimum distance \(1\) is impossible for a separating system with at least three words, minimum distance at least \(5\) is excluded by the same coordinate distance-sum bound for an eleven-word hypothetical code, and the remaining closest-pair distances \(2,3,4\) are exhausted after translation and coordinate-permutation normalization.

## Relationship to prior work
Randriambololona studies binary \((2,1)\)-separating systems asymptotically and gives the metric-convexity formulation, but does not classify finite length-eight extremizers. Korže and Vesel identify hypercube general-position sets with \((2,1)\)-separating systems and in 2023 report only a lower bound of \(10\) for the eight-cube. The later exact length-eight result establishes \(m_2(8,2)=10\) by a symmetry-complete finite proof. Its statement and verifier do not count the maximum systems, optimize their minimum distance, or classify the distance-four equality cases under Hamming isometries.

The present finding is therefore a structural refinement of a known exact extremal parameter: it identifies the most Hamming-separated maximum systems and gives their complete labeled census and natural-equivalence decomposition.

## Limitations
The equality census is computer-assisted, although finite and exhaustive after no heuristic pruning: every branch is accepted or rejected only by exact separation and distance tests. The orbit classification is for the full binary Hamming-isometry group stated above; it is not a classification under arbitrary permutations of the \(256\) cube vertices. No claim is made about all size-ten systems of smaller minimum distance.

Originality is supported by exact-parameter and alias searches plus inspection of the closest published exact result and the primary hypercube paper. An unindexed historical or private computational enumeration of the same equality subclass remains a residual risk. The earliest inspected source with an exact verified public-release day is the arXiv submission of Randriambololona on 2010-10-27; older foundational literature was encountered with journal-level dating only, so no earlier day was invented.

## References
1. H. Randriambololona, “\((2,1)\)-separating systems beyond the probabilistic bound,” arXiv:1010.5764v1, public release 2010-10-27; later *Israel Journal of Mathematics* 195 (2013), 171–186.
2. S. R. Blackburn, “Frameproof Codes,” *SIAM Journal on Discrete Mathematics* 16 (2003), 499–510, DOI:10.1137/S0895480101384633.
3. D. Korže and A. Vesel, “General Position Sets in Two Families of Cartesian Product Graphs,” *Mediterranean Journal of Mathematics* 20 (2023), article 203, DOI:10.1007/s00009-023-02416-z.
4. “Exact size of binary \((2,1)\)-separating systems of length eight,” published published-finding corpus record `2026/9/21/SCOPE-exact-length-eight-binary-21-separating-systems--bbbd20b813f0`.
