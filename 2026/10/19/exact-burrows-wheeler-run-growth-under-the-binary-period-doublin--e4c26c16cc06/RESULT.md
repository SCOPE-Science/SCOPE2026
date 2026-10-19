# Exact Burrows–Wheeler run growth under the binary period-doubling substitution

## Finding

Let \(\theta\) be the binary morphism \(\theta(0)=01\), \(\theta(1)=00\), and let \(W_k=\theta^k(0)\). For a primitive finite word \(X\), \(\mathrm{BWT}(X)\) is the last column obtained by lexicographically sorting **all cyclic rotations** of \(X\), with \(0<1\); no terminal marker is appended. Let \(r(Y)\) count the maximal nonempty constant-letter runs in a **linear** word \(Y\). Then

\[
\boxed{r(\mathrm{BWT}(W_k))=2k-2\quad\text{for every integer }k\ge2.}
\]

A stronger transfer theorem is responsible for the exact formula. Suppose \(X\) is a primitive cyclic binary word containing no cyclic occurrence of \(11\). Partition \(B=\mathrm{BWT}(X)=B_0B_1\) after its first \(z=|X|_0\) positions, so that \(B_0\) collects rotations beginning in \(0\), and \(B_1\) collects those beginning in \(1\). Write \(o=|X|_1\), \(R\) for reversal, and \(\overline{Y}\) for bitwise complementation. Then \(\theta(X)\) is primitive and

\[
\boxed{\mathrm{BWT}(\theta(X))
=\overline{B_1^R}\,0^o\,\overline{B_0^R}\,0^z.}
\]

This is a word identity, not just an equality of run counts. It also applies to \(X=0\), with empty segments interpreted in the usual way.

## Assumptions and scope

A word \(X=x_0\cdots x_{n-1}\) is *primitive* when it is not a proper integral power. The cyclic rotation beginning at index \(i\) is \(x_ix_{i+1}\cdots x_{n-1}x_0\cdots x_{i-1}\), with subscripts interpreted modulo \(n\). The BWT used here sorts precisely these \(n\) rotations and records, in sorted order, the symbol at index \(i-1\). A cyclic occurrence of \(11\) includes a pair straddling the endpoint. We count linear BWT runs, not circular runs, and do not insert an end-of-text sentinel. The transfer identity is asserted only for primitive words with no cyclic \(11\); the run formula applies only to the period-doubling iterates \(W_k\).

## Proof

**Lemma 1: four blocks of sorted rotations.** Let \(X=x_0\cdots x_{n-1}\) be primitive and cyclically \(11\)-free. Set \(a_i=1-x_i\). The word \(Y=\theta(X)\) satisfies \(Y_{2i}=0\) and \(Y_{2i+1}=a_i\), with indices read cyclically. A rotation of \(Y\) is described by the symbol index \(i\) and one of the two starting parities: an even start \(E_i\) at \(2i\) or an odd start \(O_i\) at \(2i+1\).

These rotations fall into the following four lexicographically consecutive blocks, in the displayed order:

\[
\begin{array}{c|c|c}
\text{block}&\text{condition}&\text{initial symbols}\\\hline
E_i&x_i=1&0001\\
O_i&x_i=1&0010\\
E_i&x_i=0&01\\
O_i&x_i=0&10
\end{array}
\]

Indeed, \(x_i=1\) forces \(x_{i+1}=0\), since cyclic \(11\) is excluded; the four initial strings therefore separate the blocks. Within each block, the first position where two indexed input rotations differ is carried to the first differing *variable* position of the corresponding output rotations. This position contains the complement of the input symbol. Thus the within-block order is the **reverse lexicographic order** of the corresponding input rotations. Since \(X\) is primitive, its input rotations have no ties and the claimed comparison is strict. In particular all \(2n\) output rotations are distinct; hence \(\theta(X)\) is primitive.

**Lemma 2: transfer of the BWT last column.** The symbol preceding \(E_i\) is \(a_{i-1}=1-x_{i-1}\), whereas the symbol preceding \(O_i\) is \(0\). In the BWT of \(X\), its rotations beginning in \(0\) occur first and contribute \(B_0\); those beginning in \(1\) occur last and contribute \(B_1\). By Lemma 1, reversing the order of each relevant rotation block complements and reverses the corresponding source contribution at even starts, and yields only zeros at odd starts. In the four-block order, these contributions are \(\overline{B_1^R}\), \(0^o\), \(\overline{B_0^R}\), and \(0^z\), establishing the transfer identity.

**Lemma 3: primitive period-doubling iterates.** Every \(W_k\) is cyclically \(11\)-free: each image begins with \(0\); any \(1\) occurs only at the end of an image and is followed cyclically by the first \(0\) of the next image. For \(k\ge1\), the number \(o_k\) of ones in \(W_k\) satisfies \(o_0=0\) and \(o_{k+1}=2^k-o_k\), so \(o_k=(2^k-(-1)^k)/3\). The numerator, and hence \(o_k\), is odd. A binary word of length \(2^k\) that is a proper power would have repetition exponent at least \(2\), and in fact an even exponent; its number of ones would then be even. Therefore \(W_k\) is primitive. The singleton \(W_0=0\) is primitive as well.

**Lemma 4: exact run recursion.** Put \(B^{(k)}=\mathrm{BWT}(W_k)=B^{(k)}_0B^{(k)}_1\), partitioned by the initial rotation symbol as in Lemma 2. If \(z_{k-1}=|W_{k-1}|_0\), then every \(B^{(k)}_1\) is \(0^{z_{k-1}}\). This follows from the final block of the transfer identity. For \(k\ge2\), since \(z_{k-2}=o_{k-1}\), the first three transfer blocks yield

\[
B^{(k)}_0=1^{o_{k-1}}0^{o_{k-1}}
\overline{(B^{(k-1)}_0)^R}.
\]

Directly, \(W_2=0100\) and \(B^{(2)}=1000\), so \(r(B^{(2)})=2\), and \(B^{(2)}_0=100\) begins in \(1\) and ends in \(0\). Inductively \(B^{(k-1)}_0\) begins in \(1\) and ends in \(0\). Its complemented reversal also begins in \(1\) and ends in \(0\), and preserves the number of runs. The newly prepended blocks \(1^{o_{k-1}}0^{o_{k-1}}\) therefore increase the number of runs by exactly two. The final suffix \(B^{(k)}_1\) consists of zeros and merges with the ending zero of \(B^{(k)}_0\), so

\[
r(B^{(k)})=r(B^{(k-1)})+2\qquad(k\ge3).
\]

Together with \(r(B^{(2)})=2\), induction yields \(r(B^{(k)})=2k-2\) for all \(k\ge2\), as required.

## Verification

The standalone file `verify_bwt.py` contains an explicit sorting implementation and an independent cyclic suffix-array doubling algorithm. It checks the transfer identity for every primitive cyclically \(11\)-free word of lengths \(1\) through \(10\) (282 input words). It independently reconstructs and compares BWT columns for \(W_k\), \(1\le k\le9\), using both algorithms, and verifies the exact transfer formula and run count through \(k=14\) (length \(16384\)). Run the checker with standard Python 3 using `python verify_bwt.py`. Its expected last line starts `VERIFY_OK`. These are finite reproducibility tests; the unbounded theorem is proved by the four lemmas above.

## Relationship to prior work

Currie, Rampersad, Saari and Zamboni [1] characterized lexicographically extremal **infinite** words for the period-doubling subshift, using the same substitution; their result does not sort finite cyclic rotations or count BWT runs. Brlek, Frosini, Mancini, Pergola and Rinaldi [2] gave exact BWT analyses for Thue–Morse, generalized Fibonacci and related composed morphisms, not this substitution. Frosini, Mancini, Rinaldi, Romana and Sciortino [3] established logarithmic upper bounds for BWT runs in binary purely morphic words, but those bounds do not determine the exact constant, offset or explicit last-column recurrence here. Fici, Romana, Sciortino and Urbina [4] studied BWT sensitivity of the period-doubling morphism on general inputs, including inputs where the run increment is arbitrarily large; their theorems concern different input families and do not imply the present exact iteration formula. The BWT transfer identity on the restricted cyclically \(11\)-free class directly explains the special behavior.

## Limitations

The theorem uses the cyclic-rotation BWT without a terminal marker. A sentinel-based transform has different sorting and run counts. The equality \(2k-2\) is not asserted for arbitrary starting words or other substitutions. The reference comparison supports originality relative to the inspected literature but cannot exclude all unindexed equivalent presentations. No independent scientific audit has been performed.

## References

1. J. D. Currie, N. Rampersad, K. Saari and L. Q. Zamboni, *Extremal words in morphic subshifts*, arXiv:1301.4972, first posted 2013-01-21. https://arxiv.org/abs/1301.4972
2. S. Brlek, A. Frosini, I. Mancini, E. Pergola and S. Rinaldi, *Burrows–Wheeler Transform of Words Defined by Morphisms*, IWOCA 2019, DOI:10.1007/978-3-030-25005-8_32. https://flore.unifi.it/retrieve/e398c380-dd2e-179a-e053-3705fe0a4cff/BWT-morphism_%20Last.pdf
3. A. Frosini, I. Mancini, S. Rinaldi, G. Romana and M. Sciortino, *Logarithmic Equal-Letter Runs for BWT of Purely Morphic Words*, arXiv:2202.02609, 2022. https://arxiv.org/abs/2202.02609
4. G. Fici, G. Romana, M. Sciortino and C. Urbina, *On the Impact of Morphisms on BWT-Runs*, CPM 2023, DOI:10.4230/LIPIcs.CPM.2023.10. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2023.10
