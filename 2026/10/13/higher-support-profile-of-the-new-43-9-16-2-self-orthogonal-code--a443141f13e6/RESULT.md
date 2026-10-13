# Higher-support profile of the new \([43,9,16]_2\) self-orthogonal code
## Finding

Lim, An, and Kim list a new optimal binary self-orthogonal code with parameters
\[
[43,9,16]_2
\]
as the first entry of their Table 2. Using the exact generator matrix supplied in their companion data, its generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9)
=(16,24,29,33,36,38,40,42,43).
\]

The number of \(r\)-dimensional subcodes attaining \(d_r\) is, in the same order,
\[
(24,20,4,9,28,8,7,43,1).
\]
Thus, for example, exactly four three-dimensional subcodes have support \(29\), and exactly seven seven-dimensional subcodes have support \(40\).

The code is also projective. Its 43 generator columns are all nonzero and pairwise distinct. Exactly seven unordered column triples are linearly dependent, at one-based coordinate sets
\[
\{6,20,35\},\ \{11,24,41\},\ \{12,31,36\},\ \{13,31,41\},
\]
\[
\{14,31,35\},\ \{15,27,36\},\ \{34,41,43\}.
\]
Consequently
\[
d(C^\perp)=3
\]
and \(C^\perp\) contains exactly seven words of weight \(3\).

## Assumptions and scope

The claim concerns the specific \(9\times43\) binary generator matrix in the authors' companion file for the block labeled
`source=[34,9,13]_2 best_so=[43,9,16]_2 ... experiment_id=1`.
No equivalence-class uniqueness beyond that published witness is asserted.

For an \(r\)-dimensional subcode \(D\le C\), its support is the union of the supports of its words, and
\[
d_r(C)=\min_{\dim D=r}|\operatorname{Supp}(D)|.
\]
The code is binary, so a nonzero column already represents its unique projective point.

## Proof

The supplied matrix has rank \(9\). Direct multiplication over \(\mathbb F_2\) gives
\[
GG^{\mathsf T}=0,
\]
which independently confirms the stated self-orthogonality. Exhausting its \(2^9=512\) words gives
\[
\begin{aligned}
W_C(z)={}&1+24z^{16}+95z^{18}+123z^{20}+107z^{22}\\
&+91z^{24}+45z^{26}+17z^{28}+9z^{30}.
\end{aligned}
\]
In particular the published minimum distance \(16\) is reproduced.

Every \(r\)-dimensional subcode of \(C\) is the image of a unique \(r\)-dimensional subspace of \(\mathbb F_2^9\), because the generator map has full rank. The verifier enumerates every such message subspace exactly once by reduced-row-echelon representatives. The numbers examined for \(r=1,\ldots,9\) are
\[
511,\ 43435,\ 788035,\ 3309747,\ 3309747,\ 788035,\ 43435,\ 511,\ 1.
\]
For each basis, bitwise union of the basis-codeword supports equals the support of the entire subcode. Taking the minimum in each exhaustive support histogram yields
\[
(16,24,29,33,36,38,40,42,43),
\]
and reading the frequency at each minimum yields
\[
(24,20,4,9,28,8,7,43,1).
\]
The complete histograms are stored in `artifacts/certificate.json` and checked by the verifier.

For the dual statement, no generator column is zero, so \(C^\perp\) has no word of weight \(1\). No two columns coincide, so it has no word of weight \(2\). Exhausting all \(\binom{43}{3}\) triples finds precisely the seven dependent triples displayed above. Over \(\mathbb F_2\), each dependent triple gives one weight-\(3\) dual word, proving the claimed minimum distance and multiplicity.

## Verification

`artifacts/verify.c` is a standalone exact checker using only the C standard library. It embeds the published generator matrix, reconstructs all 512 codewords, checks rank and self-orthogonality, enumerates every subspace of \(\mathbb F_2^9\) in reduced row-echelon form, and verifies the complete support histograms in `artifacts/certificate.json` against hard-coded expected counts.

It separately checks that the 43 columns are nonzero and distinct and exhausts all triples to recover exactly the seven dependent coordinate sets above. A successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article introduces the code as one of 66 new optimal self-orthogonal codes found by a constraint-preserving genetic algorithm. Table 2 reports only \([n,k]\), minimum distance, and permutation-automorphism-group order; for this entry those data are \([43,9]\), \(16\), and \(1\). The authors make the resulting generator matrices publicly available in their companion repository.

The full primary text contains no generalized-Hamming-weight or weight-hierarchy statement, and the companion generator file supplies the matrix but no higher-support census. Focused searches using the exact parameters, the exact hierarchy, minimum-support-subcode terminology, and the dual weight-\(3\) layer did not locate an earlier same-object result.

Generalized Hamming weights are classical invariants, but knowing that a code is optimal, self-orthogonal, and has minimum distance \(16\) does not determine \(d_2,\ldots,d_9\), their extremal-subcode multiplicities, or the weight-\(3\) layer of the dual. Those quantities require incidence information from the actual generator columns.

## Limitations

The result is a finite exact analysis of one newly published optimal code. It does not claim a formula for all 66 optimal codes in the source or for arbitrary self-orthogonal embeddings.

The source reports permutation-automorphism-group order \(1\), but no new automorphism claim is made here.

An unindexed computation could contain the same higher-support profile; the originality conclusion is limited to the primary text, its companion data, and the focused literature and research-record searches described in the review.

## References

1. Haeun Lim, Junmin An, and Jon-Lark Kim, *Constraint-Preserving Genetic Algorithms for Embedding Linear Codes into Self-Orthogonal Codes*, arXiv:2609.02135v1, 2026.
2. Haeun Lim, companion repository *Self-orthogonal-and-LCD-embedding-using-genetic-algorithm-and-greedy-search*, file `SO_Genetic algorithm_generator matrix.txt`, blob SHA `346878eeefdb465e7d79e43d4fa3c34e3ad24570`.
3. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
