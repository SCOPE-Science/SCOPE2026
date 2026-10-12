# Sharp nonunimodality threshold for maximal consecutive-321 Lehmer codes

## Finding
For every integer \(n\ge2\), let \(M_n\) be the set of maximal elements, under coordinatewise comparison, among Lehmer codes of permutations avoiding the **consecutive** pattern \(321\). Write
\[
\delta(p)=\binom{n}{2}-\sum_{i=1}^n p_i,
\qquad F_n(q)=\sum_{p\in M_n}q^{\delta(p)}.
\]
The complete coefficient sequence of \(F_n(q)\), in increasing powers of \(q\) (including any initial zeros), is unimodal **if and only if**
\[
\boxed{2\le n\le10\quad\text{or}\quad n=12.}
\]
Thus the first failure is \(n=11\), unimodality returns at \(n=12\), and every length \(n\ge13\) fails.

An exact coefficient formula, used in the proof, is as follows. For integers \(n\ge2\) and \(d\), put
\[
u=n-2-d,\qquad e\in\{0,1,2\},\ e\equiv2d-n+2\pmod3,
\qquad v=(2d-n+2-e)/3.
\]
Then
\[
[q^d]F_n(q)=
\begin{cases}
\displaystyle\binom{2}{e}\binom{u+v}{v},&u\ge0,\ v\ge0,\\
0,&\text{otherwise}.
\end{cases}
\]
Equivalently, as a formal power series in \(x\),
\[
\sum_{n\ge2}F_n(q)x^n=\frac{(x+qx^2)^2}{1-qx^2-q^3x^3}.
\]
The block encoding used to derive this generating function was established in the cited primary paper. The **newly assessed assertion** is the precise all-length unimodality/nonunimodality threshold, including the isolated restoration at length twelve.

## Assumptions and scope
A Lehmer code is a vector \(p=(p_1,\ldots,p_n)\) with \(0\le p_i\le n-i\); the associated permutation \(\pi\) has \(p_i=|\{j>i:\pi_j<\pi_i\}|\). The forbidden pattern is three **adjacent positions** satisfying \(\pi_i>\pi_{i+1}>\pi_{i+2}\), not classical (nonconsecutive) pattern avoidance. Codes are partially ordered componentwise. *Maximal* means having no strictly larger code in this restricted poset, and does not mean maximum inversion weight. The coefficient sequence is unimodal if there is an index through which it is weakly nondecreasing and after which it is weakly nonincreasing; zeros before the minimum defect are allowed. No statement is made for the empty or one-letter permutation.

## Proof
**Published structural input.** Lemma 4.4 of Beveridge, Hu and Liu [1, pp. 13--14] proves that maximal codes correspond bijectively to block lengths
\[
(b_1,b_2,\ldots,b_s),\qquad s\ge2,
\]
whose first and last terms belong to \(\{1,2\}\), every interior term belongs to \(\{2,3\}\), and whose sum is \(n\). The exceptional small lengths \(n=2,3\) are included in this description. Each block of length \(b\) contributes \(\binom b2\) to the defect; this block-defect identity is also explicitly proved in [1, pp. 16--17]. In particular, **neither structural input is claimed as new here**.

Set \(e=(b_1-1)+(b_s-1)\in\{0,1,2\}\), let \(u\) be the number of interior blocks of length two, and let \(v\) be the number of interior blocks of length three. The length and defect satisfy exactly
\[
n=2+e+2u+3v,\qquad d=e+u+3v.
\]
Solving gives \(u=n-2-d\) and \(e+3v=2d-n+2\). Since \(e\) must lie in \(\{0,1,2\}\), it is uniquely determined by reduction modulo three; then \(v\) is uniquely determined. If \(u,v\ge0\), there are \(\binom2e\) choices of the two endpoint lengths and \(\binom{u+v}{v}\) arrangements of the interior blocks. Otherwise there are none. This proves the coefficient formula. Multiplying the two endpoint weights \(x+qx^2\) and summing any ordered sequence of interior block weights \(qx^2\) and \(q^3x^3\) proves the rational generating function.

It remains to classify unimodality for every length. **Odd lengths:** write \(n=2r+1\) with \(r\ge5\), and let \(c_d=[q^d]F_n(q)\). Three *consecutive* coefficients, at defects \(r+1,r+2,r+3\), are
\[
(c_{r+1},c_{r+2},c_{r+3})
=(r-1,\ r-2,\ (r-2)(r-3)).
\]
For \(r\ge5\), the middle entry is strictly smaller than both neighbors. A nonnegative unimodal sequence cannot have a strict interior valley; hence every odd \(n\ge11\) fails unimodality.

**Even lengths:** write \(n=2r\) with \(r\ge7\). At defects \(r+2,r+3,r+4\), the formula gives
\[
(c_{r+2},c_{r+3},c_{r+4})
=\left(\binom{r-2}{2},\ \binom{r-3}{2},\ 2\binom{r-3}{3}\right).
\]
The first exceeds the middle. The third exceeds the middle because
\[
\frac{2\binom{r-3}{3}}{\binom{r-3}{2}}=\frac{2(r-5)}3>1\quad(r\ge7).
\]
Therefore every even \(n\ge14\) fails unimodality.

The remaining cases are precisely \(n=2,3,\ldots,10,12\). Their nonzero coefficient sequences, in ascending defect order, obtained directly from the exact binomial formula, are:

| \(n\) | Nonzero coefficients |
| --- | --- |
| 2 | 1 |
| 3 | 2 |
| 4 | 1, 1 |
| 5 | 2, 1 |
| 6 | 1, 1, 2 |
| 7 | 2, 2, 1 |
| 8 | 1, 1, 4, 1 |
| 9 | 2, 3, 2, 2 |
| 10 | 1, 1, 6, 3, 1 |
| 12 | 1, 1, 8, 6, 3, 2 |

Each row is unimodal, establishing the asserted if-and-only-if classification. For comparison, the row at \(n=11\) is \((2,4,3,6,1)\), displaying the first strict valley. This finishes the proof.

## Verification
The included standard-library program `artifacts/verify.py` can be executed by `python3 artifacts/verify.py` after extracting the files. It independently enumerates all Lehmer codes for \(2\le n\le9\), decodes the actual permutations, tests consecutive-pattern avoidance, and uses a multidimensional upper-zeta transform to determine maximal elements under componentwise order. It compares the resulting exact weight histograms against the derived binomial formula. A separate block-composition generator checks lengths through \(28\); the coefficient and unimodality classification is checked for every length through \(120\). The stored output is in `artifacts/verify_output.txt`. The universal conclusion follows from the preceding algebra, not from bounded numerical testing.

## Relationship to prior work
Beveridge--Hu--Liu [1] introduced these code posets, proved the maximal-code block characterization (Lemma 4.4), obtained Padovan total counts (Theorem 1.4), and derived the block formula for defect while determining maximum inversion weights (Theorem 1.5). These are **prior results**, not claimed as contributions. The present threshold uses that encoding to ask a different enumerative question: whether the *entire inversion-rank profile of maximal elements* is unimodal, as opposed to its total size or extremal rank. The explicit coefficient formula is supplied as a bridge from [1], not as an independently original structural classification.

Beveridge--Hu--Liu [2] studies different, partially adjacent patterns and their associated Fibonacci maximal codes. Neither its patterns nor its scalar enumerations imply the sharp consecutive-321 unimodality threshold without an additional pattern-specific argument. Targeted searches for rank polynomial, inversion defect distribution, and equivalent reversed inversion profiles did not identify a published all-length threshold. A search's failure is not proof of global originality.

## Limitations
The result concerns maximal elements of the **coordinatewise Lehmer-code poset**, not all consecutive-321-avoiding permutations and not merely maximum-weight codes. It establishes unimodality only, not real-rootedness or any general zero-location property. Its new step is an algebraic consequence of the previously published maximal-code structure, not an independent proof of that classification. An unindexed earlier treatment of the same rank-profile threshold could limit originality; independent audit has not been performed.

## References
[1] A. Beveridge, Y. Hu and Y. Liu, *Maximal Lehmer Codes for Permutations with Classical and Consecutive 321-Avoidance*, arXiv:2609.33137v1 (first public 2026-09-27), especially Lemma 4.4 and Theorems 1.4--1.5; https://arxiv.org/pdf/2609.33137v1.

[2] A. Beveridge, Y. Hu and Y. Liu, *Lehmer Codes and the Reverse-Complement Mapping from (32-1)-Avoiding Permutations to (3-21)-Avoiding Permutations*, arXiv:2607.26900 (2026); https://arxiv.org/abs/2607.26900.
