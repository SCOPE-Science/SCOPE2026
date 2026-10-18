# Antipodal first-source rigidity for optimal burning of even hypercubes through dimension fourteen

## Finding
For every even integer \(n\) satisfying \(2\le n\le14\), set \(k=n/2+1\). If \((x_1,\ldots,x_k)\) burns every vertex of the binary hypercube \(Q_n\) in \(k\) rounds, its first two sources necessarily are antipodal:
\[
d_H(x_1,x_2)=n.
\]
This proves the **first-two-sources assertion** of Conjecture 11 of Mitsche, Prałat and Roshanbin for all even dimensions through fourteen. The known optimal number of rounds is not part of the new claim.

A quantitative strengthening is obtained for dimension fourteen: if \(d_H(x_1,x_2)<14\), then for **every** choice of the third and fourth sources,
\[
\left|Q_{14}\setminus\bigcup_{i=1}^{4}B_{8-i}(x_i)\right|\ge650.
\]
The bound is sharp, with a witness whose vertices are encoded by integers \((0,4095,12415,16257)\) (binary digits in fourteen positions). The four remaining source-balls have total volume at most \(592\), so even optimal choices for them cannot finish the burn. The deficit is at least \(58\).

## Assumptions and scope
Vertices of \(Q_n\) are vectors in \(\{0,1\}^n\), adjacent when differing in exactly one coordinate. Write \(d_H\) for Hamming distance and \(B_r(x)=\{y:d_H(x,y)\le r\}\) for the closed Hamming ball. In ordinary graph burning, a single source is chosen in each round, and all previously burning vertices spread to neighbors in later rounds. A sequence burns the whole graph in \(k\) rounds exactly when
\[
\bigcup_{i=1}^{k}B_{k-i}(x_i)=\{0,1\}^n.
\]
Sources need not be distinct; allowing repeated or previously burned choices only strengthens the universal statement. Alon's 1992 result gives \(b(Q_n)=\lceil n/2\rceil+1\), so the length in the theorem is optimal. The paper's finite claim is confined to the specified even dimensions and does not settle arbitrary even dimension.

## Proof
**Small dimensions.** If \(n=2\), the first final-time ball of radius one excludes exactly the antipode, so the second singleton ball must be centered there. For \(n=4\), normalize \(x_1=0\). The first final-time ball of radius two misses exactly the five words of weights three and four. If \(x_2\) has weight below four, its radius-one ball meets these five words in at most two vertices. The third source has radius zero and contributes at most one further vertex, leaving at least two uncovered. Hence \(d_H(x_1,x_2)=4\).

**Exhaustive but symmetry-complete finite lemma.** Let \(n\in\{6,8,10,12,14\}\), and put \(k=n/2+1\). We prove that, for every ordered four-tuple \((x_1,x_2,x_3,x_4)\) with \(d_H(x_1,x_2)<n\), the complement of the four final-time balls of radii \(k-1,k-2,k-3,k-4\) has size at least the entry \(m_n\) below.

| \(n\) | Minimum uncovered \(m_n\) after first four final-time balls | Total volume of remaining balls | Symmetry classes checked |
|---:|---:|---:|---:|
| 6 | 5 | 0 | 1,632 |
| 8 | 16 | 1 | 6,270 |
| 10 | 53 | 12 | 19,162 |
| 12 | 185 | 93 | 49,933 |
| 14 | 650 | 592 | 115,600 |

Here a **symmetry class** is one orbit of ordered source quadruples under the full coordinate-permutation and bit-flip automorphism group of \(Q_n\). To see exhaustiveness, translate coordinates to take \(x_1=0\), and permute coordinates to make \(x_2\) the word with \(d\) initial ones, for \(0\le d<n\). Permutations preserving these two words make \(x_3\) have its ones in the initial \(a\) positions of the first block and initial \(b\) positions of the second, for \(0\le a\le d\) and \(0\le b\le n-d\). These choices partition coordinates into blocks of sizes \(a,d-a,b,n-d-b\). Finally permute within each block to bring the ones of \(x_4\) to initial positions, leaving exactly four integers with respective ranges \(0\ldots a\), \(0\ldots(d-a)\), \(0\ldots b\), \(0\ldots(n-d-b)\). Every ordered four-tuple is isometric to one and only one resulting block-size pattern, and every such pattern is enumerated by the supplied programs.

For each pattern, the first program explicitly forms the four Boolean-ball bitsets and counts the zeros of their union exactly. A second program independently counts uncovered words using eight coordinate patterns for the triples of bits in \((x_2,x_3,x_4)\): if a pattern occurs \(g\) times, a word having \(j\) ones in those positions contributes \(\binom gj\) possibilities. Summing products of these binomial factors subject to all four strict distance inequalities returns the same minimum and class count for every value of \(d\) in every tested dimension. Both are integer-exact finite calculations, not random experiments or extrapolations.

**Comparison with remaining sources.** For each dimension, the remaining \(k-4\) sources have radii \(k-5,k-6,\ldots,0\), and therefore cover at most
\[
M_n=\sum_{r=0}^{k-5}\sum_{j=0}^{r}\binom nj
\]
additional vertices. For the five dimensions these capacities are respectively \(0,1,12,93,592\), strictly less than \(m_n\). Thus a source pair that is not antipodal cannot be extended to a covering sequence in \(k\) rounds. Together with the small cases this proves the theorem.

For sharpness at \(n=14\), the explicit quadruple of integer-coded vertices \((0,4095,12415,16257)\) has second-source weight twelve and has exactly \(650\) uncovered vertices after its first four final-time balls. The universal orbit-enumeration lower bound therefore is attained.

## Verification
The accompanying complete, stand-alone C++17 programs `certificate_bitset.cpp` and `certificate_binomial.cpp` enumerate all relevant source-quadruple classes in even dimensions six through fourteen. They use no external dependencies. The first is a direct Hamming-ball bitset calculation; the second is an independent multinomial distance count. Their recorded outputs are `certificate_bitset_output.txt` and `certificate_binomial_output.txt`. For reproduction, compile each source with a C++17 compiler and run its binary with each of the five even dimensions as a single command-line argument. The complete per-distance minima and orbit counts agree between programs; the first program additionally verifies that the minimum always exceeds the capacity of later source balls. The small-dimensional cases were proved directly above. A separate direct integer-word check confirmed the sharp fourteen-dimensional witness.

## Relationship to prior work
Alon [1] proves the exact optimal transmission/burning time on hypercubes and gives an antipodal-source construction, but neither the necessity of antipodal first sources nor this finite extremal four-ball certificate follows from the quoted theorem. Mitsche, Prałat and Roshanbin [2, Section 3.3, Conjecture 11] explicitly formulate the antipodality of the first two sources in any optimal burning sequence for every even-dimensional hypercube as a conjecture. The present theorem establishes that particular conjectured assertion in the specified finite range, and not the general conjecture. The general graph-burning ball characterization is classical [3]. A published study of four-round burning in a different fixed-diagonal graph family [4] uses related ball-cover methods but is not a hypercube result and does not imply this claim.

## Limitations
No statement is established for even dimensions sixteen and above, nor for the more general uniqueness or structure of all subsequent burning sources. The sharp \(650\) uncovered-vertex bound concerns only the first four final-time balls, not an asserted universal lower bound on all partial process states. The conclusion was checked with exhaustive finite programs and not an independent external audit. Full text of the 2018 publisher article could not be retrieved; its publicly indexed Section 3.3 and exact Conjecture 11 statement were inspected. Unindexed equivalent computations and later papers remain possible originality risks.

## References
[1] N. Alon, "Transmitting in the n-dimensional cube," *Discrete Applied Mathematics* 37/38 (1992), 9–11, DOI 10.1016/0166-218X(92)90121-P. Open full text: https://web.math.princeton.edu/~nalon/PDFS/Publications2/Transmitting%20in%20the%20n-dimensional%20cube.pdf .

[2] D. Mitsche, P. Prałat and E. Roshanbin, "Burning number of graph products," *Theoretical Computer Science* 746 (2018), 124–135, DOI 10.1016/j.tcs.2018.06.036. Indexed Section 3.3 and Conjecture 11: https://doi.org/10.1016/j.tcs.2018.06.036 .

[3] A. Bonato, J. Janssen and E. Roshanbin, "How to burn a graph," *Internet Mathematics* 12 (2016), arXiv:1507.06524, https://arxiv.org/abs/1507.06524 .

[4] "Four-round burning cutoff for \(H(n,5)\)," publicly indexed research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-round-burning-cutoff-for-h-n-5--c67e002b03db .
