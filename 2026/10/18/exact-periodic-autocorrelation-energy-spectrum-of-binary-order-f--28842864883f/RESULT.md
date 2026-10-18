# Exact periodic autocorrelation-energy spectrum of binary order-five de Bruijn cycles

## Finding

Let \(B=(b_0,\ldots,b_{31})\) be a binary cyclic de Bruijn word of order five: every binary word of length five occurs exactly once among its 32 cyclic factors. Identify words differing only by rotation, but **not** by reversal or bit complementation. Define \(s_j=(-1)^{b_j}\), with subscripts modulo 32, and define its signed periodic autocorrelations and total nonzero-shift energy by
\[
R_B(t)=\sum_{j=0}^{31}s_js_{j+t},\qquad
E(B)=\sum_{t=1}^{31}R_B(t)^2.
\]
There are exactly 2,048 such cycles. Their complete energy distribution \(H(e)=\#\{B:E(B)=e\}\) is:

| \(e\) | \(H(e)\) | \(e\) | \(H(e)\) | \(e\) | \(H(e)\) |
|---:|---:|---:|---:|---:|---:|
| 192 | 12 | 224 | 12 | 256 | 12 |
| 288 | 12 | 320 | 44 | 352 | 32 |
| 384 | 96 | 416 | 72 | 448 | 100 |
| 480 | 72 | 512 | 136 | 544 | 132 |
| 576 | 112 | 608 | 66 | 640 | 146 |
| 672 | 126 | 704 | 104 | 736 | 52 |
| 768 | 74 | 800 | 74 | 832 | 76 |
| 864 | 52 | 896 | 66 | 928 | 40 |
| 960 | 18 | 992 | 30 | 1024 | 26 |
| 1056 | 8 | 1088 | 32 | 1120 | 38 |
| 1152 | 16 | 1184 | 20 | 1216 | 18 |
| 1248 | 10 | 1280 | 20 | 1312 | 20 |
| 1344 | 12 | 1408 | 2 | 1440 | 8 |
| 1472 | 4 | 1504 | 8 | 1600 | 8 |
| 1632 | 4 | 1664 | 10 | 1696 | 8 |
| 1888 | 4 | 1952 | 4 | | |

Thus exactly 47 energy values occur, with sharp bounds
\[
192\le E(B)\le1952.
\]
The minimum is attained by 12 cycles (three four-element orbits under reversal and complementation); the maximum is attained by four cycles forming one such orbit. All energies are divisible by 32. Exactly nine multiples of 32 between the extrema do not occur: \(1376,1536,1568,1728,1760,1792,1824,1856,1920\).

For the uniform distribution on the 2,048 rotational classes,
\[
\mathbb E E=\frac{2813}{4},\qquad
\operatorname{Var}(E)=\frac{1336631}{16}.
\]
Equivalently, the precisely defined periodic main-peak-to-total-sidelobe ratio \(1024/E(B)\) ranges from \(32/61\) to \(16/3\). These are **periodic** correlations, not aperiodic correlations.

## Assumptions and scope

The alphabet consists of two labeled symbols, 0 and 1. The order is exactly five, and word length is exactly 32. A cyclic factor may wrap around the end of a displayed linear representative. Rotations are identified, whereas reversals and complementation are not identified for the principal count. Energy includes all shifts from 1 through 31, counted with both symmetric shifts \(t\) and \(32-t\). Integer arithmetic is exact throughout.

## Proof

**Exhaustive finite parametrization.** Use the binary de Bruijn digraph with 16 vertices indexed by the four-bit integers \(v=0,\ldots,15\) and 32 directed edges indexed by five-bit integers \(e=0,\ldots,31\). Edge \(e\) goes from its four-bit prefix to its four-bit suffix. At vertex \(v\), its incoming edges are exactly \(v\) and \(v+16\), and its outgoing edges are exactly \(2v\) and \(2v+1\). A cyclic Euler tour induces a bijection matching the two incoming edges to the two outgoing edges at every vertex. Each vertex has precisely two such bijections, so all Euler tours appear among the \(2^{16}=65{,}536\) simultaneous local pairings.

For a pairing, let \(T\) send each incoming edge to the outgoing edge paired with it. The map \(T\) is a permutation of the 32 edges. It is one 32-cycle precisely when the pairing yields a cyclic Euler tour. Every de Bruijn cycle has exactly one such local pairing: the unique occurrence of each length-five factor identifies the outgoing edge that follows it. Conversely a 32-cycle of edges produces a de Bruijn word by reading the first bit of each edge. Anchoring the tour at the unique all-zero edge fixes rotation. Therefore accepted masks correspond **bijectively** to de Bruijn cycles; there is neither omission nor rotation multiplicity. The number of accepted masks is 2,048, agreeing with the classical total \(2^{2^{4}-5}\).

**Exact histogram and extremes.** The included standalone `CHECKER.py` iterates all 65,536 masks. At each vertex the switch bit chooses one of the two bijections; it traces the permutation from the all-zero edge and accepts precisely those masks whose trace visits all 32 edges and returns to that edge. It constructs each accepted binary word and evaluates the 31 correlations by their defining 32-term sums, without floating point. Integer tallying gives exactly the displayed 47-row histogram, its minimum and maximum, and the counts of their witnesses. This is an exhaustive finite proof because the preceding bijection proves that its search domain contains every eligible object.

A second, independent enumeration enumerates all 32-edge trails of the same overlap graph using recursive edge-avoidance backtracking, starting at the all-zero edge and accepting only tours returning to the starting vertex. This does **not** use the local pairing masks. It generates the identical set of 2,048 cycle representatives and the identical histogram. Its membership test separately verifies all 32 cyclic five-bit factors are different. The checker asserts exact equality of the two generated sets, not just their cardinalities.

**Moments and symmetry.** Direct exact sums from the histogram give
\[
\sum_e H(e)=2048,\qquad
\sum_e eH(e)=1{,}440{,}256,\qquad
\sum_e e^2H(e)=2048\cdot578{,}100.
\]
Dividing by 2,048 proves the mean and variance. Rotation, reversal and complementation preserve all squared periodic correlations, so grouping the minimizers and maximizers by these operations is valid. The checker constructs these orbits explicitly: the 12 minimizers form three orbits of four, and the four maximizers form one orbit of four.

**Divisibility and spectral interpretation.** Binary periodic autocorrelations at length 32 satisfy \(R_B(t)=R_B(32-t)\). For every shift \(t\), the number of positions where \(b_j\ne b_{j+t}\) is even (the numbers of zero-to-one and one-to-zero changes match), whence \(4\mid R_B(t)\). Moreover, \(R_B(16)=32-4h\), where \(h\) is the number of unequal antipodal pairs among the 16 pairs. As the de Bruijn word contains 16 ones, the equality \(16=2a+h\) for the number \(a\) of pairs of two ones implies \(h\) is even, so \(8\mid R_B(16)\). Hence
\[
E(B)=2\sum_{t=1}^{15}R_B(t)^2+R_B(16)^2
\]
is divisible by 32. The de Bruijn property additionally forces \(R_B(t)=0\) for \(1\le t\le4\), since all length-five patterns occur uniformly. Finally, writing \(\widehat{s}(k)=\sum_{j=0}^{31}s_j\exp(-2\pi i kj/32)\), discrete Parseval gives
\[
E(B)=\frac1{32}\sum_{k=0}^{31}|\widehat{s}(k)|^4-1024.
\]
Thus the histogram is equivalently the full cyclic fourth Fourier-moment spectrum for this natural finite class.

## Verification

Run `python3 CHECKER.py` with Python 3 and no third-party packages. The checker tests the complete 65,536-mask enumeration against an independent recursive Euler-tour enumeration, the exact histogram, the sharp extremal multiplicities, all four symmetry-orbit facts, the two exact moments, and the low-shift identities. It also reproduces, to three reported decimal places, the three average normalized root-mean-square (RMS) sidelobe statistics and the two size thresholds published in Table 3 of Spinsante--Andrenacci--Gambi (2011). These external agreements test normalization independently of the histogram.

## Relationship to prior work

The de Bruijn/overlap-graph correspondence is classical. Gabrić and Sawada (2018, first posted March 23) study constructive universal cycles; their methods do not determine squared periodic correlation distributions. Mandal and Gong (2020) investigate correlation-friendly filtered de Bruijn generators, a different output ensemble. The closest statistical predecessor is Spinsante, Andrenacci and Gambi (2011): their Section on correlation properties and Table 3 examine **all 2,048 order-five cycles**, and report the 12 cycles with maximum absolute nonzero-shift correlation at most four, the 784 with threshold at most eight, and three rounded *averages* of normalized RMS sidelobes. These facts are explicitly acknowledged; the present finding is **not** claiming the existence of these subsets, the first use of an RMS metric, or the first generation of all 2,048 cycles. Its additional information is the full exact 47-value *individual-energy histogram*, the maximum-energy class, exact moments and orbit classification; three aggregate RMS averages and two peak-cutoff counts do not imply that histogram. Fujisaki and Nabeshima (2011) provide lower bounds and experimental worst/second-worst **individual correlation values**, not the sum-of-squares distribution. Spinsante, Warty and Gambi (2013, Section 4 and Figure 6) display overlaid correlation traces for all 2,048 cycles, but do not tabulate their individual energies or the histogram: a family of plotted traces is not an exact multiplicity table.

## Limitations

The result is finite and restricted to order five, not a theorem about all orders. The exhaustive programs prove the finite classification through independently complete graph traversals, not by numerical sampling or probabilistic extrapolation. There is no claim of performance superiority for physical channels: correlation energy is a mathematically motivated proxy. Published material might contain equivalent specialized data under a different normalization, so historical originality carries a residual literature risk. No independent mathematical audit has been performed.

## References

1. D. Gabrić and J. Sawada, *Constructing de Bruijn sequences by concatenating smaller universal cycles*, arXiv:1803.09009, first public version March 23, 2018; doi:10.1016/j.tcs.2018.06.039.
2. K. Mandal and G. Gong, *On ideal \(t\)-tuple distribution of orthogonal functions in filtering de Bruijn generators*, *Advances in Mathematics of Communications* 16 (2022), 597--619, first online December 15, 2020, doi:10.3934/amc.2020125.
3. S. Spinsante, S. Andrenacci and E. Gambi, *Binary De Bruijn sequences for DS-CDMA systems: analysis and results*, *EURASIP Journal on Wireless Communications and Networking* (2011), article 4, doi:10.1186/1687-1499-2011-4 (particularly Table 3).
4. H. Fujisaki and Y. Nabeshima, *On auto-correlation values of de Bruijn sequences*, *Nonlinear Theory and Its Applications, IEICE* 2 (2011), 400--408, doi:10.1587/nolta.2.400 (particularly Tables I--II).
5. S. Spinsante, C. Warty and E. Gambi, *DS-SS with de Bruijn sequences for secure Inter Satellite Links*, 2013 IEEE Aerospace Conference, doi:10.1109/AERO.2013.6496833 (particularly Figure 6).
