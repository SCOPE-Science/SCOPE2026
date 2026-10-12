# Exact five- and six-erasure ambiguity for a quinary strong-Pasch local-repair code

## Finding

For the explicit \([12,6,5]_5\) locally repairable code arising from the three strong-Pasch configurations of Fu and Shan over \(\mathbb F_5\), precisely **16 of the 792 five-coordinate erasure sets** and **181 of the 924 six-coordinate erasure sets** admit more than one completion. Every nonuniquely recoverable set of either size has a one-dimensional ambiguity space, so that a consistent received word has exactly five completions. The column matroid of the parity-check matrix has exactly 16 circuits of size five and 69 circuits of size six. Exactly 112 of the 181 failing six-sets contain one of the 16 five-circuits, while the remaining 69 are themselves circuits.

Equivalently, for uniformly sampled fixed-size erasures, the conditional unique-decoding failure probabilities are \(16/792=2/99\) at size five and \(181/924\) at size six. These are *erasure* ambiguity probabilities, not probabilities of an erroneous Hamming-metric decoding result.

## Assumptions and scope

All arithmetic is in \(\mathbb F_5\), and coordinates are labeled \(1,\ldots,12\). Partition these coordinates into three consecutive blocks of size four. Define triples of column vectors in \(\mathbb F_5^3\) by
\[
\begin{aligned}
 V_1&=((1,0,0),(0,1,0),(0,0,1)),\\
 V_m&=((1,m,-m),(m^2,m,-m^2),(m,-m,1)),\qquad m\in\{2,3\}.
\end{aligned}
\]
Let \(H\) be the \(6\times12\) matrix whose top three rows contain a separate all-one row for each four-coordinate block, and whose bottom three rows consist of the three blocks \((0,V_1)\), \((0,V_2)\), and \((0,V_3)\), with \(0\) the zero column. Thus the four columns in block \(i\) are precisely \((e_i,0)\), \((e_i,v_{i1})\), \((e_i,v_{i2})\), \((e_i,v_{i3})\), where \(e_i\) is a standard basis vector in \(\mathbb F_5^3\). Define
\[
 C=\{c\in\mathbb F_5^{12}:Hc^{\mathsf T}=0\}.
\]
The matrix is the \(q=5\), three-repair-group instance of the odd-characteristic family in Fu–Shan, Theorem 2. Its rank is six, so \(C\) has dimension six; its minimum nonzero Hamming weight is five. Each group has its own weight-four local parity equation, giving locality at most three.

For an erasure set \(E\subseteq\{1,\ldots,12\}\), let \(H_E\) be the submatrix containing precisely those columns. An erased word consistent with a codeword has \(5^{\nu(E)}\) completions, where \(\nu(E)=|E|-\operatorname{rank}_{\mathbb F_5}(H_E)\). A *circuit* is an inclusion-minimal dependent set of columns, equivalently a support of a nonzero codeword minimal under inclusion.

## Proof

**Ambiguity criterion.** If two codewords agree outside \(E\), their difference is a codeword supported within \(E\), i.e. a vector in \(\ker H_E\), extended by zeros. Rank-nullity gives the completion count. In particular every set of fewer than five columns is independent because the minimum codeword weight is five.

**Incidence characterization for five columns.** Each top parity equation forces the sum of the coefficients in each four-column group to vanish. Thus a minimal five-column dependence has a distribution of precisely two and three occupied columns in two distinct groups; no group can contain exactly one occupied column. Write the bottom three-column labels of group \(i\) as \(a_{i0}=0\), \(a_{i1}=v_{i1}\), \(a_{i2}=v_{i2}\), \(a_{i3}=v_{i3}\). Two selected columns indexed by \(u,v\) in group \(i\) contribute a nonzero multiple of \(a_{iu}-a_{iv}\). Three selected columns \(r,s,t\) in group \(j\) contribute a nonzero vector in the span of \(a_{jr}-a_{jt}\) and \(a_{js}-a_{jt}\). Since every three of the four affine points in a block are noncollinear, an incidence between the projective point \([a_{iu}-a_{iv}]\) and the line spanned by those two differences produces a dependence using *all five* coordinates (and conversely). The nonvanishing of its three coefficients follows from the fact that no two of the three affine points determine the same projective direction as the matched point from another strong-Pasch configuration. The six projective pair differences in one block and the corresponding six differences in any other block are disjoint, as may be checked in the stated finite field.

There are six unordered pairs per source block and four unordered triples per target block. Compute their point-on-line incidences by reducing each pair difference to its first nonzero entry and testing its dot product against the cross product of the two triple differences. For ordered source/target blocks \((i,j)\) with \(i\ne j\), the six incidence counts in zero-based group order are
\[
 (N_{01},N_{02},N_{10},N_{12},N_{20},N_{21})=(3,3,3,2,3,2).
\]
Therefore there are exactly \(3+3+3+2+3+2=16\) distinct five-circuits, yielding exactly sixteen failing five-erasure sets. Every such dependency is unique up to scale because every four-column subset is independent.

**Exact six-column boundary.** The enclosed `artifacts/circuits.json` gives a complete coordinate list of the sixteen five-circuits and the sixty-nine six-circuits, using one-based indices. The standalone `verify.py` builds \(H\) directly from the above triples and, over all \(\binom{12}{6}=924\) six-subsets, computes \(\operatorname{rank}(H_E)\) by exact modular row reduction. The resulting rank-deficiency histogram is
\[
 \#\{E:|E|=6,\nu(E)=0\}=743,\qquad
 \#\{E:|E|=6,\nu(E)=1\}=181;
\]
no six-subset has larger deficiency. Independently, direct enumeration of all \(5^6\) codewords identifies the same 69 inclusion-minimal six-support sets and the same 16 five-support sets, with four nonzero scalar multiples for each support. Thus this is an exhaustive finite computation, rather than a sampled calculation.

Every pair of distinct five-circuits intersects in at most three coordinates, again exactly checked from their complete lists. Consequently their extensions by one coordinate are all distinct, giving \(16(12-5)=112\) dependent six-subsets. The 69 six-circuits contain no five-circuit, and the exhaustive rank histogram gives precisely \(112+69=181\) six-erasure failures. Their deficiencies are all one, proving the claimed completion multiplicity.

## Verification

Run `python3 verify.py` with the companion `artifacts/circuits.json` in the same extracted directory. The standard-library-only checker reconstructs the parity-check matrix, obtains a six-row basis of the kernel, and enumerates all \(15{,}625\) codewords. It checks the complete Hamming-weight distribution
\[
 (A_0,A_5,A_6,A_7,A_8,A_9,A_{10},A_{11},A_{12})
 =(1,64,276,748,2060,3800,4460,3084,1132),
\]
with all other weights absent. It then checks the independent projective incidence calculation, the complete circuit manifest and all \(792+924\) rank tests, including that no failed set has deficiency above one. Successful replay prints `VERIFY_OK`. The weight enumerator is supporting evidence for the one erasure-spectrum finding, not a separate claim about an unproved general family.

## Relationship to prior work

Fu and Shan, *Geometric construction of k-optimal locally repairable codes* (arXiv:2605.31214v1, 29 May 2026), introduce strong-Pasch configurations and construct odd-characteristic \((4l,3l-3,5;3)\) codes with disjoint repair groups. In particular they establish the existence of this \([12,6,5]_5\) construction and its minimum distance. The new issue addressed here is *how many* erasure patterns of sizes five and six fail, together with their circuit decomposition and ambiguity dimension. Neither existence nor distance five is claimed as new. Earlier parity-check constructions of local-repair codes are background rather than purportedly excluded cases of the same finite incidence problem.

## Limitations

The enumerations and counts apply to the specified three-group code over \(\mathbb F_5\) with the stated column normalization and not automatically to other choices of strong-Pasch configurations, larger fields, larger codes, or errors rather than erasures. The finite rank computations establish no asymptotic formula. The literature search cannot exclude unindexed earlier presentations or independently computed equivalent matroid data. No independent mathematical audit has yet been performed.

## References

1. Yi Fu and Xiuling Shan, *Geometric construction of k-optimal locally repairable codes*, arXiv:2605.31214v1, first public 2026-05-29, https://arxiv.org/abs/2605.31214.
2. Jie Hao, Shu-Tao Xia, Kenneth W. Shum, Bin Chen, Fang-Wei Fu, Yi-Xian Yang, *Bounds and Constructions of Locally Repairable Codes: Parity-check Matrix Approach*, arXiv:1601.05595, 2016, https://arxiv.org/abs/1601.05595.
3. Fang et al., *Perfect LRCs and k-optimal LRCs*, Designs, Codes and Cryptography 91 (2023), 1209–1232.
