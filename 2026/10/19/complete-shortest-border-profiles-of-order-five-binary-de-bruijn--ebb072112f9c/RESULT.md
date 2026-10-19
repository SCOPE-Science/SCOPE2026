# Complete shortest-border profiles of order-five binary de Bruijn cycles

## Finding

Let \(B\) range over the binary de Bruijn cycles of order \(5\), identified up to rotation, and write \(N=32\). Each cycle contains all \(32\) five-bit words as distinct circular factors. For each of the \(32\) cuts \(c\), let \(b_B(c)=0\) when the associated linear rotation is unbordered, and otherwise let \(b_B(c)\) be the length of its shortest nonempty proper border. Define \(u_j(B)=|\{c:b_B(c)=j\}|\) for \(j\ge0\).

**Theorem (complete shortest-border census).** Every order-five cycle has \(u_1=16\), \(u_2=4\), and \(u_j=0\) for \(j\ge5\). The remaining triple \((u_0,u_3,u_4)\) takes precisely the seven values below. The second column is the exact number of cyclically inequivalent cycles with the indicated triple. The last two columns count orbits of those cycles under reversal and bit complementation, after rotation has been factored out.

| \((u_0,u_3,u_4)\) | Cycles | Orbits of size 2 | Orbits of size 4 |
|---|---:|---:|---:|
| \((8,4,0)\) | 48 | 4 | 10 |
| \((9,1,2)\) | 64 | 0 | 16 |
| \((9,2,1)\) | 256 | 4 | 62 |
| \((9,3,0)\) | 448 | 0 | 112 |
| \((10,0,2)\) | 48 | 4 | 10 |
| \((10,1,1)\) | 384 | 0 | 96 |
| \((10,2,0)\) | 800 | 20 | 190 |
| **Total** | **2048** | **32** | **496** |

In particular, the number of unbordered rotations is exactly \(8\), \(9\), or \(10\), occurring for \(48\), \(768\), or \(1232\) cycles, respectively. The mean number of unbordered rotations under the uniform measure on these \(2048\) cycles is \(613/64\), and its variance is \(1191/4096\). There are precisely \(528\) reversal–complement orbits.

## Assumptions and scope

A *binary de Bruijn cycle of order five* is a cyclic binary sequence \(B=B_0B_1\cdots B_{31}\) in which the factors \(B_iB_{i+1}\cdots B_{i+4}\), with indices taken modulo \(32\), range bijectively over \(\{0,1\}^5\). Its rotation at cut \(c\in\{0,\dots,31\}\) is the linear word \(B_cB_{c+1}\cdots B_{c+31}\). A *border* is a nonempty proper prefix identical to a suffix of the same length; overlapping prefix and suffix are allowed. Thus \(b_B(c)\) is zero for unbordered rotations and otherwise the minimum border length.

All numbers count binary labeled words; cycles are identified under rotation *only*. Reversal and complementation are used solely in the separate orbit refinement. The claim is an exhaustive finite statement for order \(5\), not a formula for higher orders. The type of shortest-border profile and its distribution are distinct from the previously studied unrestricted maximum of unbordered conjugates.

## Proof

**Structural restriction.** Suppose a rotation of \(B\) has a border of length \(k\) with \(5\le k<32\). Its first five letters agree with the first five letters of its length-\(k\) suffix. These are length-five circular factors of \(B\) starting at two different positions, since their starts differ by \(32-k\) modulo \(32\). This contradicts the de Bruijn property. Hence every nonzero shortest border length is at most four.

A cut has a length-one border exactly when the two letters immediately flanking the cut coincide. Each of `00` and `11` appears as a circular factor exactly \(2^{5-2}=8\) times, hence \(u_1=16\). A cut with shortest border two has, across the cut, one of the two squares `0101` and `1010`: the other binary squares of root length two, `0000` and `1111`, already give a border of length one. Each of `0101` and `1010` appears exactly \(2^{5-4}=2\) times, giving \(u_2=4\). Therefore \(u_0+u_3+u_4=12\) in every cycle.

**Exhaustive construction.** Consider the binary directed de Bruijn graph with sixteen four-bit vertices and thirty-two five-bit edges; the edge \(a_1a_2a_3a_4a_5\) goes from \(a_1a_2a_3a_4\) to \(a_2a_3a_4a_5\). An Euler circuit uses every five-bit edge exactly once and spells precisely one de Bruijn cycle. Fixing its unique edge `00000` as the first edge removes rotational duplication.

At each four-bit vertex, an Euler circuit pairs the two incoming edges (`0v`, `1v`) bijectively with its two outgoing edges (`v0`, `v1`). There are exactly two such pairings per vertex. Every possible circuit therefore induces one of \(2^{16}=65536\) completely specified local-pairing assignments. Conversely, a local-pairing assignment defines a permutation of the thirty-two edges; it represents one Euler circuit precisely when this permutation is a single cycle. This is an *exhaustive* characterization, not a probabilistic search. The accompanying `verify.py` enumerates all assignments and retains exactly \(2048\) single-cycle permutations.

**Independent finite enumeration and certificate.** Independently, `verify.py` depth-first enumerates all Euler circuits beginning with edge `00000`, making one independent choice among unused outgoing edges at each step. The resulting normalized sets are identical, both containing \(2048\) cycles. For each cycle the program evaluates all thirty-two rotations in two ways: full prefix/suffix equality for every proper border length and, independently, equality of the two length-\(k\) circular blocks centered at the cut for each \(1\le k\le4\). The preceding structural restriction makes the second check complete. The two algorithms agree on every cut. Accumulating each \((u_0,u_3,u_4)\) produces precisely the seven rows of the table.

Finally, reverse and bit-complement each normalized cycle, re-normalizing the four images by the unique `00000` factor. These operations generate a group of order at most four on rotation classes and preserve every count \(u_j\). Partitioning all \(2048\) classes into the resulting orbits gives the two orbit columns, with no excluded or repeated cycles. Summing rows by \(u_0\) gives \(48,768,1232\). Exact rational arithmetic gives the stated mean and variance.

## Verification

Run `python3 verify.py` using only the Python standard library. It asserts equality of the two independent complete sets, checks all five-bit cyclic factors of every generated word, compares independent shortest-border and centered-square calculations at all \(65536\) cuts, verifies each of the seven exact frequencies, and validates both symmetry-orbit totals and their cellwise multiplicities. The file `spectrum.csv` records the seven rows separately. Every assertion passes on the supplied verifier; the full count is a finite exhaustive computation with a mathematical completeness argument. No partial sampling or timeout is used as evidence.

## Relationship to prior work

Harju and Nowotka's *Border correlation of binary words* introduced systematic study of bordered and unbordered conjugates, including bounds for arbitrary binary words. Blanchet-Sadri, Clader, and Simpson's *Border Correlations of Partial Words* studies refined shortest-border correlations and suggests studying the population distribution of correlations. Holub and Müller's *Fully bordered words* (arXiv:1504.02222, first public version 2015-04-09) characterizes the opposite extreme, words with exactly two unbordered conjugates. Clokie, Gabric, and Shallit's *Circularly squarefree words and unbordered conjugates: a new approach* (arXiv:1904.08187, 2019-04-17) investigates global extrema and possible numbers of unbordered conjugates for general words. None of the inspected material supplies the restriction to *de Bruijn order-five* words with its seven shortest-border profiles and exact frequencies. These results give definitions and broader bounds, not the present census.

## Limitations

This result concerns order five only. It does not imply a spectrum for larger de Bruijn orders, nor an enumeration of all cyclic border-correlation strings themselves (as opposed to their shortest-border count profiles). The completely published 2004 version of Harju and Nowotka's directly relevant article was not accessible in full in this review; its abstract and later papers describing its principal results were inspected. The possibility of unindexed or inaccessible earlier equivalent enumerations remains a historical-priority risk. The computational proof is reproducible and complete on the specified finite domain; a general-order classification remains open.

## References

1. Š. Holub and M. Müller, *Fully bordered words*, arXiv:1504.02222 (publicly posted 2015-04-09), https://arxiv.org/abs/1504.02222.
2. T. Clokie, D. Gabric, and J. Shallit, *Circularly squarefree words and unbordered conjugates: a new approach*, arXiv:1904.08187 (2019-04-17), https://arxiv.org/abs/1904.08187.
3. F. Blanchet-Sadri, E. Clader, and O. Simpson, *Border Correlations of Partial Words*, manuscript dated 2008-07-15, later published in *Theory of Computing Systems* 47 (2010), 179–195. https://www.researchgate.net/publication/220544393_Border_Correlations_of_Partial_Words.
4. T. Harju and D. Nowotka, *Border correlation of binary words*, *Journal of Combinatorial Theory, Series A* 108 (2004), 331–341, https://doi.org/10.1016/j.jcta.2004.07.009. Earlier technical report dated August 2003.
5. OEIS A321162, *Maximum number of unbordered conjugates for a binary word of length n*, https://oeis.org/A321162; a different unrestricted invariant.
