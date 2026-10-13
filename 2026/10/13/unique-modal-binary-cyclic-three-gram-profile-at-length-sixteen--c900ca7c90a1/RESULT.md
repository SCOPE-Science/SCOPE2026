# Unique modal binary cyclic three-gram profile at length sixteen

## Finding
For a binary word \(w=(w_0,\ldots,w_{15})\) with indexed coordinates, define its **cyclic three-gram profile** \(P(w)=(p_{000},p_{001},\ldots,p_{111})\) by counting the triple \((w_i,w_{i+1},w_{i+2})\) at each \(i\in\{0,\ldots,15\}\), with indices modulo \(16\). For each attainable profile \(p\), its **fiber** comprises all distinct indexed binary words \(w\) satisfying \(P(w)=p\). Rotations are **not** identified.

**Theorem.** Among all binary cyclic three-gram profiles at length \(16\), the largest fiber has size \(1296\). The maximizing profile is unique: it is \((2,2,2,2,2,2,2,2)\), corresponding to twice-each-three-gram coverage. Exactly \(271\) profiles occur, and the unique second-largest fiber has size \(1280\), at profile \((1,2,3,2,2,3,2,1)\). Both vectors use lexicographic triple order \(000,001,010,011,100,101,110,111\).

The value \(1296\) for the twice-each-three-gram fiber itself follows from earlier multi-de Bruijn enumeration. What is established here is its **unique global maximizing property**, including comparison with every nonuniform profile and the strict gap to the runner-up.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the word length is exactly \(16\), and all \(16\) starting locations are observed with wraparound. Profiles retain the *multiplicities* of all eight triples. Two words differing only by a nontrivial rotation count as distinct if their indexed bit arrays differ. No assertion is made for longer words, other alphabets, or noncyclic substrings.

The smallest full-coverage case provides a useful boundary comparison: at length \(8\), the uniform profile \((1,1,1,1,1,1,1,1)\) has fiber size \(16\), whereas the unique modal profile \((0,1,2,1,1,2,1,0)\) has fiber size \(24\). Thus uniformity is *not* a universal consequence of profile balancing at the first full-coverage length.

## Proof
Form the directed binary order-two de Bruijn graph whose vertices are \(00,01,10,11\). An edge labeled by triple \(uvw\) goes from \(uv\) to \(vw\). Every cyclic word corresponds to a length-\(16\) closed edge walk and conversely. In the order \(000,001,010,011,100,101,110,111\), write the edge multiplicities as \((a,b,c,d,e,f,g,h)\). Flow conservation at all vertices gives
\[
e=b,\qquad g=d,\qquad f=c+d-b,
\]
while the total-length equation is
\[
a+b+2c+3d+h=16.
\]
All multiplicities must be nonnegative integers. The set of positive-multiplicity edges of a closed walk must form one strongly connected component, disregarding vertices of degree zero.

When \(b,d>0\), all four vertices lie in that component, and the number of directed spanning in-arborescences rooted at \(00\) is \(t=b\,d\,(c+d)\): the edge from \(10\) to \(00\) can be chosen in \(b\) ways, the edge from \(11\) to \(10\) in \(d\) ways, and the edge leaving \(01\) in \(c+d\) ways. Denote the outdegrees by \(r_{00}=a+b\), \(r_{01}=c+d\), \(r_{10}=b+f=c+d\), and \(r_{11}=d+h\). The directed BEST formula, after identifying identical copies of each labeled triple, gives the number of indexed cyclic words with this exact profile:
\[
F(a,b,c,d)=\frac{16\,t\,\prod_{v}(r_v-1)!}{a!\,(b!)^2\,c!\,(d!)^2\,f!\,h!}.
\]
Here all four outdegrees are positive. To see the indexed factor \(16\), for any specified initial vertex, the last-exit arborescence construction counts Eulerian walks in which the initial edge is distinguished. Summing over initial vertices counts the \(16\) possible labeled starting locations. The product of factorials in the denominator identifies permutations of identical edge copies. The number of rooted in-arborescences is independent of the root in an Eulerian strongly connected digraph, so the factor \(t\) may be taken at \(00\).

For completeness, the other connected supports are enumerated separately. When \(b=0,d>0\), connectivity forces \(a=0\); \(f=c+d\), and the three-vertex in-arborescence count is \(t=d(c+d)\). When \(d=0,b>0\), connectivity forces \(h=0\); \(f=c-b\ge0\), and \(t=bc\). The same BEST formula applies after removing vertices of degree zero, with the corresponding factorials. When \(b=d=0\), the only connected possibilities are an all-zero word, an all-one word, and (because the length is even) the two alternating words. In the last case the in-arborescence count is \(8\), so the BEST formula gives \(2\); each constant profile has fiber size \(1\).

The exact remaining calculation is finite and exhaustive. In the four-vertex case enumerate every positive \(b,d\), every \(c\ge0\) with \(f=c+d-b\ge0\), and every \(a\) between zero and \(16-b-2c-3d\), setting \(h=16-b-2c-3d-a\). In the two three-vertex cases enumerate their remaining nonnegative \(c\) and loop multiplicity. This enumerates precisely \(226\) four-vertex profiles, \(21\) profiles with the \(00\) vertex absent, \(21\) with \(11\) absent, and three final profiles, totaling \(271\). Computing each fiber by the displayed factorial/arborescence expression gives exactly one profile of size \(1296\), the all-twos profile; the largest value among all other profiles is \(1280\), uniquely at \((1,2,3,2,2,3,2,1)\).

For an explicit spot evaluation, the all-twos profile has four vertices each of outdegree \(4\) and arborescence count \(16\). Its fiber is therefore
\[
\frac{16\cdot16\cdot(3!)^4}{(2!)^8}=1296.
\]
The runner-up has arborescence count \(20\), outdegrees \((3,5,5,3)\), and the formula gives \(1280\). The complete \(271\)-row finite computation is given in `profile_census.csv` and in the independently executable `verify_euler.py`. Since all supports have been covered, no unexamined profile can exceed the reported maximum. This proves the theorem.

## Verification
From the directory containing the supplied files, execute `python3 verify_euler.py` and `python3 verify_direct.py`. Both use only the Python standard library and compare their complete profile-to-fiber map with `profile_census.csv`. The first reconstructs the entire \(271\)-profile census using flow constraints, support classification, integer factorials and arborescences; the second independently visits all \(2^{16}=65536\) indexed binary words and counts their profiles directly. The total of all profile fibers equals \(65536\), and the programs verify both unique highest ranks. The direct enumerator also checks the length-eight boundary example.

## Relationship to prior work
Jacquet, Knessl and Szpankowski study the **number of distinct cyclic Markov types**, not the maximum cardinality of a fixed type for order-two binary transitions at a prescribed length. Kiah, Puleo and Milenkovic investigate de Bruijn sequence profiles and coding with distinct profiles, but their reported theorems do not identify the largest fiber of this cyclic length-sixteen three-gram observation. Tesler's multi-de Bruijn formula already gives the **size of the uniform fiber** (\(1296\)) but does not compare that fiber to nonuniform profiles. Alhakim and Szmidt construct and connect uniform-multiplicity multi-de Bruijn cycles; the same fixed-length global comparison is not among their stated results. Distinguishing cyclic indexed arrays from cycles identified under rotation is necessary when comparing these works.

## Limitations
This is an exact **finite-length** global maximum, not an asymptotic theorem and not an all-length extremal classification. The fact that the uniform count itself was known is not presented as a new theorem. Nonuniform profiles are compared by a finite, fully enumerated certificate, rather than a general analytic inequality. Inaccessible or unindexed historical enumerations might have tabulated the modal value without explicitly identifying the same invariant; independent external validation has not been performed.

## References
1. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58 (2012), 4261–4272; author full text: https://www.cs.purdue.edu/homes/spa/papers/it12-types.pdf .
2. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Storage Channels*, first arXiv submission 2014-10-31, arXiv:1410.8837; and *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (2015).
3. G. Tesler, *Multi de Bruijn Sequences*, Journal of Combinatorics 8 (2017), 439–474; arXiv:1708.03654, especially the formula for linearized cyclic multi-de Bruijn sequences.
4. A. Alhakim and J. Szmidt, *Multi de Bruijn Sequences and the Cross-Join Method*, Mathematics 11 (2023), article 1262, DOI:10.3390/math11051262.
