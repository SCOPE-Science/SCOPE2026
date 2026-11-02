# Complete cyclic \(b\)-symbol spectra of the binary Golay \([23,12,7]\) code

## Finding

Let \(C\) be the binary cyclic Golay code of length \(23\), generated over \(\mathbb F_2\) by
\[
g(x)=1+x^2+x^4+x^5+x^6+x^{10}+x^{11}.
\]
For \(1\le b\le23\), let \(A_j^{(b)}\) count codewords having exactly \(j\) nonzero consecutive cyclic windows of width \(b\). **The entire family of \(23\) distributions** \(\bigl(A_0^{(b)},\ldots,A_{23}^{(b)}\bigr)\) is determined by the exact integer table `B_SYMBOL_SPECTRA.csv` and by the independently checkable \(81\)-class run-partition census `ZERO_RUN_CENSUS.csv`.

In particular, the minimum nonzero read weights are
\[
d_1=7,\quad d_2=11,\quad d_3=13,\quad d_4=15,\quad
 d_b=b+11\quad(5\le b\le11),\quad d_b=23\quad(12\le b\le23).
\]
Their numbers of attaining words are respectively \(253\) at \(b=1\), \(115\) at \(b=2\), exactly \(23\) at each \(3\le b\le11\), and \(4095\) at each \(12\le b\le23\). For **every** \(3\le b\le11\), the set of minimizers is precisely the same \(23\)-word cyclic orbit of \(g(x)\). **Prior-coverage qualification.** The entire *minimum-distance profile* at widths \(1\) through \(11\) is already explicitly reported in Guan et al. [5, Example 4], whose reciprocal generator specifies the same cyclic code up to reversal. The stability theorem of Shi–Özbudak–Solé [6] covers the high-width stabilization. **Neither the distance values nor the elementary zero-run identity are claimed as new.** The new claim consists of the complete *multiplicity distributions* at the nontrivial widths, their joint \(81\)-class partition refinement, and the exact common minimizing orbit and multiplicities for widths \(3\) through \(11\).

## Assumptions and scope

All polynomial operations are over \(\mathbb F_2\). Coordinates of \(c(x)=\sum_{i=0}^{22}c_i x^i\) are \(c_0,\ldots,c_{22}\), with indices read modulo \(23\). The code is the exact set
\[
C=\{m(x)g(x):m\in\mathbb F_2[x],\ \deg m<12\},
\]
which has \(4096\) elements: \(g\) has degree \(11\), divides \(x^{23}+1\), and multiplication by \(g\) is injective for these message degrees. For every integer \(1\le b\le23\), define
\[
w_b(c)=\#\{i\in\mathbb Z/23\mathbb Z:(c_i,c_{i+1},\ldots,c_{i+b-1})\ne(0,\ldots,0)\}.
\]
Thus \(A_j^{(b)}=\#\{c\in C:w_b(c)=j\}\). The orientation and cyclic coordinate order are fixed; arbitrary coordinate permutations are not included.

A *cyclic maximal zero-run* of a nonconstant binary word is a maximal nonempty cyclic arc of consecutive zeros, with its length recorded. We sort the lengths in nonincreasing order to define a zero-run partition \(\lambda(c)\). The two constant words are recorded separately as `ALL_ZERO` and `ALL_ONE`.

## Proof

**Complete enumeration of the code.** The twelve polynomials \(x^j g(x)\), \(0\le j<12\), have distinct leading degrees \(11+j\), so they are linearly independent. Hence the loop over all \(0\le m<2^{12}\) in `GENERATE.py` visits every one of the \(4096\) words in \(C\) exactly once. Since \(\deg(mg)\le22\), no modular reduction is needed. The exact arithmetic is XOR of integer bit vectors; no approximation or probabilistic sampling occurs.

**Run-to-window identity.** For any nonconstant \(c\), a zero-run of length \(r\) contains exactly \(\max(r-b+1,0)\) starts of all-zero cyclic windows of width \(b\). Such starts belong to disjoint runs. Consequently
\[
w_b(c)=23-\sum_{r\in\lambda(c)}\max(r-b+1,0).
\]
For the zero and all-one words the weights are \(0\) and \(23\), respectively. Thus, writing \(N_\lambda=\#\{c\in C:\lambda(c)=\lambda\}\), the exact finite summation
\[
A_j^{(b)}=\mathbf1_{j=0}+\mathbf1_{j=23}
 +\sum_{\lambda\ \mathrm{nonconstant}}N_\lambda\,
 \mathbf1_{\,j=23-\sum_{r\in\lambda}\max(r-b+1,0)}
\]
computes each of the \(24\) coefficients for every \(b\). The first CSV enumerates **all 81 nonempty partition categories**, with the two constants included; the second is the resulting complete \(23\)-row spectrum table. Every row sums to \(4096\). This constitutes a finite exhaustive proof because all message integers are traversed, not an extrapolation from examples.

**Distance and common-minimizer claims.** Inspection of all coefficients of the complete generated table, performed independently by `VERIFY.py`, gives the displayed distances and multiplicities. For each \(3\le b\le11\), the independently enumerated minimizing words equal exactly
\[
\{x^j g(x)\bmod (x^{23}+1):0\le j<23\}.
\]
The \(23\) rotations are distinct, and every one occurs in \(C\). The previously tabulated minimum *values* alone do not determine that this entire minimizing set is a single orbit, rather than several orbits, or determine any of the other spectrum coefficients. For \(12\le b\le23\), a nonzero codeword cannot contain \(12\) consecutive zeros: cyclically rotate such an arc to the first twelve positions. In the resulting message-times-generator polynomial, the coefficient at each degree from \(0\) through \(11\) successively forces its corresponding message coefficient to be zero, because the constant term of \(g\) equals \(1\). The word must be zero, a contradiction. Therefore every nonzero codeword has all \(23\) cyclic windows nonzero when \(b\ge12\).

## Verification

The distributable package contains `GENERATE.py`, `VERIFY.py`, `ZERO_RUN_CENSUS.csv`, and `B_SYMBOL_SPECTRA.csv`. From one directory containing all four files, run `python3 GENERATE.py` followed by `python3 VERIFY.py`. The former builds the two exact CSV tables by message-wise polynomial multiplication and a cyclic-zero-run identity. The latter independently constructs each codeword using systematic polynomial division (rather than the generator's XOR-message loop), computes every cyclic window directly (rather than relying on the run identity), and compares every coefficient and every partition count with the CSV files.

The second verifier additionally tests the generator divisibility, all \(4096\) distinct words, the classical Hamming weight enumerator
\[
1+253z^7+506z^8+1288z^{11}+1288z^{12}+506z^{15}+253z^{16}+z^{23},
\]
the \(178\) nonconstant cyclic orbits, every listed minimum and multiplicity, and the exact common minimizing orbit. Its expected terminal output is `VERIFY_OK: 4096 codewords, 81 zero-run classes, all 23 read lengths`. The reported computations were performed from the supplied standalone files using Python's standard library; there are no external dependencies.

## Relationship to prior work

The standard cyclic generator and ordinary Hamming parameters of the binary Golay code are established in GUAVA [1]. Chee et al. [2] establish Singleton-type bounds and MDS existence for symbol-pair read channels, without giving a Golay spectrum. Yaakobi, Bruck and Siegel [3] establish general pair-distance lower bounds and constructions, including \(d_2\ge d_1+\lceil d_1/2\rceil\), which covers the lower bound \(11\) for this code. Vega [4] computes complete \(b\)-symbol distributions for specified **irreducible** one- and two-weight cyclic-code families; the binary Golay code instead has a reducible parity-check polynomial and seven distinct nonzero Hamming weights.

**Crucially, Guan, Luo, Luo, Fei and Wang [5, Example 4] explicitly state the binary Golay minimum \(b\)-read distance hierarchy** \((7,11,13,15,16,17,18,19,20,21,22)\) for widths \(1\) through \(11\). Their generator is \(x^{11}g(1/x)\), the reciprocal of the present standard generator, so their code is its coordinate reversal and has the **same entire cyclic read spectra**. Accordingly, none of those minimum *values* is claimed new here. Their stated hierarchy and cyclic repetition constructions do not tabulate the coefficient multiplicities at each read weight, the \(81\) zero-run classes, or the unique minimizing orbit across widths \(3\) through \(11\). Shi, Özbudak and Solé [6] establish the general stabilization of cyclic \(b\)-symbol enumerators for \(b\) at least code dimension, so the stabilization for \(12\le b\le23\) is also not novel. Panraksa [7] gives a related cyclic zero-run/gap and minimizer-orbit treatment for the **ternary length-11 Golay code**, not the binary length-23 code; the zero-run identity itself is classical and not claimed as an original lemma.

The contribution is therefore the exact all-weight, nontrivial-width finite classification of the binary cyclic Golay code and its codeword multiplicities, not the known distance hierarchy, stabilization principle, or run identity. Targeted comparisons found no prior complete coefficient table for widths \(2\) through \(11\) or the common-minimizer claim, but incomplete indexing and archival coverage remain residual risks.

## Limitations

The classification applies only to the binary cyclic Golay code of length \(23\) under its specified cyclic coordinate order, for all integer widths \(1\le b\le23\). It does not cover the extended length-\(24\) Golay code, arbitrary permutations of coordinates, arbitrary other codes, or a claimed general formula for other lengths. The enumerated finite case is proved exhaustively, not by an infinite-length theorem. The previously published minimum-distance hierarchy, wide-window stabilization and general run identity are explicitly excluded from claims of novelty. An independently conducted scientific review and definitive archival-priority certification have not been performed.

## References

1. GUAVA/GAP documentation, *Generating Codes*, §5.4, binary Golay code and its generator polynomial: https://web.mit.edu/sage/export/guava-3.5/htm/chap5.html
2. Y. M. Chee, L. Ji, H. M. Kiah, C. Wang, J. Yin, *Maximum Distance Separable Codes for Symbol-Pair Read Channels*, first public arXiv record dated 2012-11-07: https://arxiv.org/abs/1211.1728
3. E. Yaakobi, J. Bruck, P. H. Siegel, *Constructions and Decoding of Cyclic Codes over b-Symbol Read Channels*, IEEE Trans. Inform. Theory 62 (2016), DOI:10.1109/TIT.2016.2522434; lawful full text: https://cmrr-star.ucsd.edu/static/pubs/Constructions_TI.pdf
4. G. Vega, *The b-symbol weight distributions of all semiprimitive irreducible cyclic codes*, Designs, Codes and Cryptography 91 (2023), DOI:10.1007/s10623-023-01193-w: https://link.springer.com/article/10.1007/s10623-023-01193-w
5. C. Guan, G. Luo, L. Luo, Y. Fei, H. Wang, *Generalized Repetition Codes and Their Application to HARQ*, arXiv:2511.15207 (first posted 2025-11-19), Example 4: https://arxiv.org/abs/2511.15207
6. M. Shi, F. Özbudak, P. Solé, *Geometric Approach to b-Symbol Hamming Weights of Cyclic Codes*, IEEE Trans. Inform. Theory 67 (2021), DOI:10.1109/TIT.2021.3069772: https://doi.org/10.1109/TIT.2021.3069772
7. C. Panraksa, *On the Cyclic Symbol-Pair and b-Symbol Distance of the Ternary [11,6,5] Golay Code*, Far East J. Math. Sci. 143 (2026), DOI:10.17654/0972087126158: https://doi.org/10.17654/0972087126158
