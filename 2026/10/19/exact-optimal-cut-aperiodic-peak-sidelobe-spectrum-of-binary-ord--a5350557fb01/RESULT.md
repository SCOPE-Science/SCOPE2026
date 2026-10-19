# Exact optimal-cut aperiodic peak-sidelobe spectrum of binary order-five de Bruijn cycles

## Finding
Let \(B=(b_j)_{j\in\mathbb Z/32\mathbb Z}\) range over binary de Bruijn cycles of order five, counted up to cyclic rotation, with bit-to-sign encoding \(s_j=(-1)^{b_j}\). For a cut \(r\in\mathbb Z/32\mathbb Z\) and a lag \(1\le h\le31\), define the **aperiodic** autocorrelation of that cut by
\[
A_{B,r}(h)=\sum_{j=0}^{31-h}s_{r+j}s_{r+j+h},
\quad P_{B,r}=\max_{1\le h\le31}|A_{B,r}(h)|,
\quad P_*(B)=\min_{0\le r<32}P_{B,r}.
\]
All subscripts on \(s\) are reduced modulo \(32\). The complete spectrum of \(P_*\) over the \(2048\) distinct cycles is

| \(P_*\) | Number of cycles |
|---:|---:|
| 4 | 32 |
| 5 | 344 |
| 6 | 476 |
| 7 | 666 |
| 8 | 236 |
| 9 | 174 |
| 10 | 20 |
| 11 | 8 |
| 12 | 20 |
| 15 | 64 |
| 16 | 8 |

In particular, the sharp attainable minimum is \(4\), reached by \(32\) cycles, and the sharp attainable maximum of this optimized statistic is \(16\), reached by \(8\) cycles; neither \(13\) nor \(14\) occurs. The exact mean and variance under the uniform distribution on these \(2048\) cycles are
\[
\mathbb E P_* = \frac{3609}{512},\qquad
\operatorname{Var}(P_*)=\frac{1103247}{262144}.
\]
The \(32\) minimum-achieving cycles consist of \(8\) orbits of size \(4\) under reversal and binary complementation; the \(8\) maximum-achieving cycles comprise \(2\) such orbits. Among the \(32\) minima, \(24\) cycles have exactly one optimizing cut, while \(8\) have exactly two.

## Assumptions and scope
A binary de Bruijn cycle of order five is a cyclic binary sequence of length \(32\) in which each binary five-tuple occurs once as a cyclic consecutive window. Cycles differing only by rotation are identified. Reverse or complement images are counted as distinct unless they happen to be rotationally identical. **Aperiodic** means the sum at lag \(h\) contains \(32-h\) terms without wraparound in the cut linear word; only the base cyclic word is read modulo \(32\). Thus the cut is an optimization variable, not a quotient symmetry for aperiodic correlation.

## Proof
Represent a five-tuple by a directed edge in the binary de Bruijn graph whose vertices are the \(16\) four-bit words. Vertex \(v\) has exactly two outgoing directed edges, numbered \(2v\) and \(2v+1\), ending at \((2v+b)\bmod16\). Each cyclic order-five de Bruijn word is equivalent to an Eulerian circuit using all \(32\) edges exactly once. The edge numbered zero, corresponding to the unique five-tuple `00000`, fixes a unique starting point in each rotation class.

The standalone checker `VERIFY.py` implements two exhaustive descriptions of this same finite set.

**Edge-avoiding recursion:** Start with edge zero already used. From its terminal vertex zero, recursively append an unused outgoing edge until all \(32\) edges have been traversed and the walk closes at vertex zero. Conversely, every Eulerian circuit, uniquely anchored at edge zero, appears in this search: after any partial circuit, its next edge is one of the tested unused outgoing edges. The recursion produces exactly \(2048\) different anchored circuits.

**Local bijection enumeration:** At every vertex there are two incoming edges (numbered \(v\) and \(v+16\)) and two outgoing edges. An Eulerian circuit determines a bijection pairing each incoming edge to the next outgoing edge. There are precisely \(2\) such pairings per vertex, hence exactly \(2^{16}=65536\) possible global switch configurations. A configuration yields one Eulerian circuit if and only if its permutation of all \(32\) edges has a single orbit. Examining every configuration identifies exactly \(2048\) single-orbit cases, whose anchored bit words agree *setwise* with those produced by the recursion. The starting edge is unique, so neither enumeration double counts rotations.

For each of these \(2048\) cycles, enumerate each of the \(32\) cuts and each of the \(31\) positive lags; evaluate the finite integer sum in the definition of \(A_{B,r}(h)\), maximize absolute value over lags, then minimize over cuts. This yields the displayed histogram, whose multiplicities sum to \(2048\). A second implementation of the same scalar invariant instead counts disagreements between the two length-\((32-h)\) aligned substrings and uses
\[
A_{B,r}(h)=(32-h)-2\,\#\{0\le j<32-h:b_{r+j}\ne b_{r+j+h}\}.
\]
The signed-sum and mismatch-count implementations independently give the same histogram. Every arithmetic operation is over exact integers. The displayed mean, variance, cut-multiplicities, and symmetry-orbit counts follow by direct exact summation and orbit enumeration over these exhaustive records.

An additional check connects the aperiodic and periodic normalizations. Defining the cyclic correlation \(R_B(h)=\sum_{j=0}^{31}s_j s_{j+h}\), for every cut and positive lag one has
\[
A_{B,r}(h)+A_{B,r}(32-h)=R_B(h).
\]
This follows by partitioning the \(32\) cyclic summands into the first \(32-h\) and remaining \(h\). The checker verifies this identity for every cycle and lag, independently guarding against a periodic-versus-aperiodic convention mismatch.

## Verification
Save the included standalone `VERIFY.py` alongside this file and execute `python3 VERIFY.py` using Python 3 with no third-party dependencies. Its exhaustive assertions verify \(65536\) switch configurations, \(2048\) identical canonical circuits from two generation procedures, all \(11\) exact histogram entries, the mismatch-count cross-check, the cyclic/aperiodic identity, and the extremal symmetry classes. A successful execution prints `PHASE_APERIODIC_PSL_DB5_PASS` and the complete table, exact moments, representatives, and optimizing-cut counts. Explicit canonical representatives attaining \(4\) and \(16\) are respectively `00000100011001010110111010011111` and `00000100011010111001010011111011` (each begins at the unique `00000` window).

## Relationship to prior work
Spinsante, Andrenacci, and Gambi (2011) enumerated all \(2048\) binary order-five de Bruijn cycles and studied their **periodic** correlation sidelobes; for example, their reported \(12\)-cycle selection at periodic sidelobe level \(4\) addresses a different function. Their periodic profile and summary statistics do not determine the distribution of the minimum **aperiodic** peak over the \(32\) cuts. Katz and van der Linden (2021) rigorously studied the aperiodic peak-sidelobe level of Golay–Rudin–Shapiro sequences, a different structured word family; their estimates neither supply the complete de Bruijn order-five population nor optimize circular cuts. Gabrić and Sawada (2018) develop de Bruijn construction, without the stated cut-optimized correlation spectrum. A previously obtained periodic-correlation-energy distribution for these same cycles is also a different statistic: a sum of squared periodic sidelobes is not the minimum over cuts of the maximum absolute aperiodic sidelobe.

## Limitations
This is an exact finite classification at binary order five only. No formula is claimed for higher order, other alphabet sizes, other correlation normalizations, or physical channel performance. The proof is a reproducible exhaustive combinatorial computation: its scope is the proved completeness of both finite generators and the exact evaluation of all candidates, not an experimental extrapolation. Literature comparison cannot exclude an equivalent computation in literature not recovered by the present search. Independent validation has not been performed.

## References
- D. J. Katz and C. M. van der Linden, *Peak Sidelobe Level and Peak Crosscorrelation of Golay–Rudin–Shapiro Sequences*, arXiv:2108.07318 (first publicly posted 2021-08-16). https://arxiv.org/abs/2108.07318
- S. Spinsante, S. Andrenacci, and E. Gambi, *Binary De Bruijn sequences for DS-CDMA systems: analysis and results*, EURASIP Journal on Wireless Communications and Networking (2011), article 4. https://doi.org/10.1186/1687-1499-2011-4
- D. Gabrić and J. Sawada, *Constructing de Bruijn sequences by concatenating smaller universal cycles*, arXiv:1803.09009 (first publicly posted 2018-03-23). https://arxiv.org/abs/1803.09009
- D. Dmitriev and J. Jedwab, *Bounds on the growth rate of the peak sidelobe level of binary sequences*, Advances in Mathematics of Communications 1 (2007), 461–475. https://doi.org/10.3934/amc.2007.1.461
