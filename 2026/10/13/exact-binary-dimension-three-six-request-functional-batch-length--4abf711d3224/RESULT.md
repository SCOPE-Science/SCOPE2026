# Exact binary dimension-three six-request functional batch length

## Finding
For dimension \(3\) over \(\mathbb F_2\) and six simultaneous requests, the exact optimal lengths of a functional batch code, an all-symbol batch code, and an all-symbol PIR code coincide:
\[
\operatorname{FB}(3,6,2)=\operatorname{ASB}(3,6,2)=\operatorname{ASP}(3,6,2)=11.
\]
A single binary generator attains all three bounds and supplies disjoint recovery sets with at most three accessed coordinates per request. The equality for functional batch codes concerns **arbitrary mixtures of six linear-functional requests**, not just six copies of one request.

## Assumptions and scope
Use the conventions of Boruchovsky–Gruica–Niemann–Yaakobi: a full-rank \(3\)-by-\(n\) binary generator \(G\) serves \(v_1,\ldots,v_6\) if six pairwise disjoint subsets of column indices each span their designated vector. A functional batch code serves all vectors in \(\mathbb F_2^3\); all-symbol batch serves all six-request multisets of its stored columns; all-symbol PIR serves six copies of each stored column. Each coordinate stores one binary linear functional. Permutations of the requested vectors are immaterial.

Identify the nonzero binary columns with their integers \(1,\ldots,7\), where \(1=(1,0,0)^\mathsf T\), \(2=(0,1,0)^\mathsf T\), \(4=(0,0,1)^\mathsf T\) and the label is the coordinate-bit sum. Take the length-\(11\) generator with columns, in order:

`1,2,3,4,5,6,7,1,2,4,7`

Equivalently the matrix is
\[
G=\begin{pmatrix}
1&0&1&0&1&0&1&1&0&0&1\\
0&1&1&0&0&1&1&0&1&0&1\\
0&0&0&1&1&1&1&0&0&1&1
\end{pmatrix}.
\]
Its first, second and fourth columns form an identity basis, so it has dimension three. The last four columns are the affine plane \(\{1,2,4,7\}\) of nonzero column types.

## Proof
**Lower bound.** For any dimension-three generator satisfying six-request all-symbol PIR, every nonzero message \(u\) produces a nonzero binary word \(uG\). Choose any stored column \(g_j\) with \(u g_j=1\), which exists by full row rank. In each of the six disjoint recovery sets for \(g_j\), at least one coordinate has \(u g_i=1\), since otherwise the linear span of that set would be annihilated by \(u\). Hence every nonzero codeword has Hamming weight at least six. The binary Griesmer bound for a dimension-three code gives
\[
 n\ge d+\left\lceil\frac d2\right\rceil+\left\lceil\frac d4\right\rceil\ge6+3+2=11.
\]
For completeness, the Griesmer step follows by puncturing a minimum-weight word of weight \(d\), leaving a dimension-two code of length \(n-d\) and minimum distance at least \(\lceil d/2\rceil\): the puncturing kernel consists only of zero and the chosen minimum-weight word, since a second independent word supported on the same \(d\) positions would produce two disjoint nonzero words of weight at least \(d\) each. For any other codeword, that word and its sum with the minimum word both have weight at least \(d\), so its number of nonzero coordinates outside the minimum word's support is at least \(\lceil d/2\rceil\). Applying the same argument to dimension two yields the displayed inequality. Thus \(\operatorname{ASP}(3,6,2)\ge11\); stronger batch models have the same lower bound.

**Upper bound.** The attached `certificates.tsv` is a complete finite constructive proof that the displayed \(G\) serves every possible six-request multiset of nonzero vectors. There are exactly
\[
\binom{7+6-1}{6}=924
\]
such multisets. Each data line names the sorted six requested vectors and gives six comma-separated lists of one-based column indices, separated by vertical bars. Each list is nonempty, contains at most three indices, and spans its corresponding requested vector. The six index sets on each line are disjoint. The standalone standard-library checker `verify.py` independently validates every incidence, all 924 distinct request patterns and rank three. Its exact result is `VERIFY_OK` with 3,798 singleton, 1,669 two-coordinate and 77 three-coordinate recovery sets across the certificate. Because every nonzero vector appears as a column of \(G\), this verifies six-functional batch service, not merely all-symbol batch service. Zero-vector requests are also serviceable: replace each zero request by any fixed nonzero vector when looking up the certificate; its recovered set spans zero as well. Therefore \(\operatorname{FB}(3,6,2)\le11\). The inclusions functional batch \(\Rightarrow\) all-symbol batch \(\Rightarrow\) all-symbol PIR finish the proof.

## Verification
Extract both `certificates.tsv` and `verify.py` unchanged into one directory and run `python3 verify.py`. The program uses only the Python standard library, regenerates all \(924\) request multisets, checks all six pairwise-disjoint recovery sets against the actual matrix, verifies that each target lies in its recovery-set span and calculates the seven nonzero codeword weights. Its observed output begins `VERIFY_OK 924/924 recovery lists; rank=3; minimum distance=6` and reports block sizes. This finite exhaustive verification is the complete upper-bound certificate for the fixed matrix, not an extrapolation to untested lengths or fields. The lower bound is the general proof above.

## Relationship to prior work
Zhang–Etzion–Yaakobi (arXiv:1901.01605, numerical table of functional PIR lengths) already give the optimal six-request **functional PIR** length \(\operatorname{FP}(3,6,2)=11\). That weaker repeated-request optimum and the Griesmer obstruction are not new. Boruchovsky–Gruica–Niemann–Yaakobi (arXiv:2601.04041) introduce and study all-symbol PIR and all-symbol batch codes, with their specific exact dimension-three results concentrating on fewer requests and their general bounds not establishing six-request mixed-service optimality. Kılıç–Ravagnani–Salizzoni (arXiv:2508.02586) establish exact two-dimensional functional-batch lengths and special binary families, without an inspected theorem settling the six-request dimension-three functional-batch value. Oksner and coauthors (arXiv:2601.12302) study locality-constrained functional batch codes and bounds; the material inspected does not subsume this all-six-multisets certificate. The added claim is the existence of a length-eleven generator serving all six arbitrary requests, implying equality of the three stronger optimal lengths above.

## Limitations
The proof concerns only dimension three over the binary field at exactly six requests. It does not assert minimum length for larger dimensions, other fields or larger numbers of requests, nor classify all optimal generators. Earlier unindexed exact functional-batch constructions remain an originality risk. The numerical certificate is finite but exhaustive for the stated domain; an external independent audit has not been performed.

## References
- Y. Zhang, T. Etzion, E. Yaakobi, *Bounds on the Length of Functional PIR and Batch Codes*, arXiv:1901.01605, https://arxiv.org/abs/1901.01605.
- A. Boruchovsky, A. Gruica, J. Niemann, E. Yaakobi, *Serving Every Symbol: All-Symbol PIR and Batch Codes*, arXiv:2601.04041, https://arxiv.org/abs/2601.04041 (first submitted January 7, 2026).
- A. B. Kılıç, A. Ravagnani, F. Salizzoni, *The Length of Functional Batch and PIR Codes*, arXiv:2508.02586, https://arxiv.org/abs/2508.02586.
- *On the Minimum Length of Functional Batch Codes with Small Recovery Sets*, arXiv:2601.12302, https://arxiv.org/abs/2601.12302.
