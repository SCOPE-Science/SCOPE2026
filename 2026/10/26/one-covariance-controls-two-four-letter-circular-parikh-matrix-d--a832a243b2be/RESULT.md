# One covariance controls two four-letter circular Parikh-matrix defects

## Finding
Let \(\Sigma=\{a<b<c<d\}\). For a nonempty word \(w\), let \(P(w)\) be its ordinary \(5\times5\) Parikh matrix, and let \(M(w)\) be the mean of \(P\) over all rotations of \(w\). Let \(\overline M\) be the alternating-sign matrix defined below. For uniformly sampled rotations \(u\) of \(w\), put \(X=|u|_{ab}\) and \(Y=|u|_{cd}\), where vertical bars count scattered subsequences, and define \(\kappa(w)=\operatorname{Cov}(X,Y)\). If \(E\) is the \(5\times5\) matrix with its only nonzero entry \(E_{1,5}=1\), then for every integer \(p\ge1\),
\[
M(w^p)-M(w)^p=\binom p2\kappa(w)E,
\qquad
\overline{M(Rw)}-M(w)^{-1}=\kappa(w)E.
\]
Here \(Rw\) denotes reversal. Therefore the inverse/reversal identity holds if and only if the power identity holds for some (equivalently every) integer \(p\ge2\), precisely when \(\kappa(w)=0\). Both failures are rank at most one and confined to one entry.

For the natural full-support four-block family, let \(A,B,C,D\) be arbitrary positive integers, \(n=A+B+C+D\), and form a word from the four blocks \(a^A,b^B,c^C,d^D\), each used once in any of the six cyclic orders beginning with the \(a\)-block. Then
\[
\frac{4n^2\kappa(w)}{ABCD}=
\begin{cases}
-(A+B)(C+D),&\text{orders }abcd,\ adcb,\\
+(A+B)(C+D),&\text{orders }abdc,\ acdb,\\
(A-B)(C-D),&\text{orders }acbd,\ adbc.
\end{cases}
\]
Thus the circular inverse and power laws always fail in the four noninterlacing orders. In the two interlacing orders, both hold exactly when \(A=B\) or \(C=D\). In particular, for words with each of the four letters occurring once, the possible covariance values are \(-1/16,0,+1/16\), each attained by eight linear permutations; zero occurs exactly when the \(a,b\) pair and the \(c,d\) pair alternate around the circle.

## Assumptions and scope
Letters are totally ordered \(a<b<c<d\); \(w\in\Sigma^+\), and \(p\) is a positive integer. For a length-\(n\) word, rotation \(\rho_t(w)\) starts at position \(t\) (positions modulo \(n\)); repetitions among rotations are counted with their multiplicities, equivalent to uniformly averaging distinct rotations. The ordinary Parikh matrix has diagonal entries one and, for \(1\le i<j\le5\), entry \(P(w)_{i,j}\) equal to the number of scattered occurrences of the contiguous alphabet interval \(a_i\cdots a_{j-1}\), with \(a_1=a,\ldots,a_4=d\). Define
\[
M(w)=\frac1n\sum_{t=0}^{n-1}P(\rho_t(w)),\qquad
\overline M_{i,j}=(-1)^{j-i}M_{i,j},
\]
\[
\kappa(w)=\frac1n\sum_t X_tY_t-\left(\frac1n\sum_tX_t\right)\left(\frac1n\sum_tY_t\right),
\quad X_t=|\rho_t(w)|_{ab},\quad Y_t=|\rho_t(w)|_{cd}.
\]
All identities are exact rational identities and include nonprimitive words and words missing one or more alphabet letters.

## Proof
Let \(U_t=P(\rho_t(w))=I+N_t\) and \(\overline N=n^{-1}\sum_t N_t\). Since \(N_t\) is strictly upper triangular of size five, \(N_t^5=0\). Its four first-superdiagonal entries are the four symbol multiplicities in \(w\), hence independent of \(t\). Every entry of \(N_t^k\) for \(k\ge3\) is linear in the variable higher-superdiagonal entries, with constant coefficients: the only possibly variable three-step products in the top-right position are \((N_t)_{1,2}(N_t)_{2,3}(N_t)_{3,5}\), \((N_t)_{1,2}(N_t)_{2,4}(N_t)_{4,5}\), and \((N_t)_{1,3}(N_t)_{3,4}(N_t)_{4,5}\). Thus \(\mathbb E[N_t^k]=\overline N^k\) for \(k=3,4\).

For \(k=2\), all entries likewise average linearly except the top-right one:
\[
(N_t^2)_{1,5}=(N_t)_{1,2}(N_t)_{2,5}+(N_t)_{1,3}(N_t)_{3,5}+(N_t)_{1,4}(N_t)_{4,5}.
\]
The first and third terms consist of one fixed symbol count times one varying scattered-subword count; the middle term is \(X_tY_t\). Consequently
\[
\mathbb E[N_t^2]-\overline N^2=\kappa(w)E.
\]
The standard Parikh map is multiplicative: \(P(u^p)=P(u)^p\). Rotations of \(w^p\) are repeated rotations of \(w\) raised to the \(p\)-th power. Hence \(M(w^p)=\mathbb E[(I+N_t)^p]\), while \(M(w)^p=(I+\overline N)^p\). The finite binomial expansions, together with the preceding identities, give exactly \(\binom p2\kappa(w)E\).

For linear words, the reversal formula is \(\overline{P(Ru)}=P(u)^{-1}\). Reversal permutes the cyclic rotations, so \(\overline{M(Rw)}=\mathbb E[(I+N_t)^{-1}]\). Expanding the inverse as \(I-N_t+N_t^2-N_t^3+N_t^4\) and comparing it with the inverse of \(I+\overline N\) leaves exactly the same \(\kappa(w)E\). Since \(\binom p2>0\) for every integer \(p\ge2\), the zero-defect equivalences follow.

For completeness, the block formulas can be verified by splitting the rotation cut into four blocks and summing the resulting arithmetic progressions. In the order \(a^Ab^Bc^Cd^D\), one finds
\[
\mathbb E X=\frac{AB}{n}\left(\frac{A+B}{2}+C+D\right),\quad
\mathbb E Y=\frac{CD}{n}\left(A+B+\frac{C+D}{2}\right),\quad
\mathbb E[XY]=\frac{ABCD}{2}.
\]
Their covariance is \(-ABCD(A+B)(C+D)/(4n^2)\). In the order \(a^Ac^Cb^Bd^D\), the corresponding three expressions are
\[
\mathbb E X=\frac{AB}{n}\left(\frac{A+B}{2}+D\right),\quad
\mathbb E Y=\frac{CD}{n}\left(A+\frac{C+D}{2}\right),\quad
\mathbb E[XY]=\frac{ABCD(A+D)}{2n}.
\]
After expansion, \(4n^2\kappa/(ABCD)=(A-B)(C-D)\). Swapping the labels \(a,b\) changes \(X\) to \(AB-X\) and reverses the sign of covariance; swapping \(c,d\) changes \(Y\) to \(CD-Y\) and likewise reverses its sign. Applying these swaps and cyclically reselecting the first block supplies the four remaining orders and their displayed coefficients. The vanishing and permutation classifications follow because all four block lengths are positive.

## Verification
The standalone Python 3 checker `checker.py` constructs Parikh matrices through the append-letter scattered-subsequence recurrence. Using exact rational arithmetic, it independently checks both matrix defect identities for powers \(p=2,3,5\) against all \(4^1+\cdots+4^5\) words, additional fixed-seed samples of lengths six through fifteen, and all twenty-four four-letter permutations. It checks the factorized block covariance formula for six orders and all positive block lengths from one to three. Its successful output is:

`CIRCULAR_PARIKH_COVARIANCE_PASS words=1548 lengths=1..15 powers=2,3,5 permutation_signs=8,8,8 blocks=486`

The all-length statement is proved algebraically above; finite checks do not replace that proof.

## Relationship to prior work
Poovanandran, Simpson and Teh introduced the rotation-average circular Parikh matrix and showed the reversal/inverse and power identities through ternary alphabets, while giving the four-letter word `abcd` as a counterexample [1, §4, Remark 4.10]. They did not state the common four-letter covariance defect, its equivalence of the two failures, or the factorized, exhaustive four-block zero-defect classification. Atanasiu, Poovanandran and Teh supplied general formulas for powers of *linear* Parikh matrices [2, §3]. Those formulas are used as background, but do not themselves describe circular averaging, the common inverse defect, or the sign/vanishing classification for circular four-block words. The present result is a precise extension at the alphabet threshold identified in [1].

## Limitations
The central one-entry covariance law is specific to the four-letter alphabet; with five or more alphabet letters, products of multiple fluctuating scattered-subword counts enter other matrix coordinates. The block sign/vanishing table requires exactly four nonempty monochromatic blocks, one of each letter. The arbitrary-word criterion remains the covariance condition, not a local forbidden-pattern characterization. Unindexed equivalent treatments of the four-letter case cannot be excluded without independent literature review.

## References
[1] G. Poovanandran, J. Simpson, W. C. Teh, *Counting Subwords in Circular Words and Their Parikh Matrices*, arXiv:2110.14858v1, first posted 2021-10-28, https://arxiv.org/abs/2110.14858 (especially §4).

[2] A. Atanasiu, G. Poovanandran, W. C. Teh, *Parikh Matrices for Powers of Words*, arXiv:1808.04102v1, first posted 2018-08-13, https://arxiv.org/abs/1808.04102 (especially §3).
