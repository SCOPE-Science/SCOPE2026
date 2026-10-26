# Exact least descent thresholds for factoradic digit-power maps

## Finding
For each integer \(r\ge2\), the factoradic digit-power map has an *exact* universal strict-descent cutoff. Define
\[
 j_r=\min\{j\ge2:j!>j^{r-1}\},\qquad
 P_r=\sum_{i=1}^{j_r-1}(i^r-i\,i!),
\]
\[
 a_r=\max\{a\in\{0,\ldots,j_r\}:P_r+a^r-a\,j_r!\ge0\}.
\]
The exact least nonnegative integer \(C_r\) for which \(S_{r,!}(n)<n\) for **all** integers \(n\ge C_r\) is
\[
 \boxed{C_r=(a_r+1)j_r!}.
\]
It is sharp at its immediate predecessor: \(S_{r,!}(C_r-1)\ge C_r-1\). In particular, the exact cutoffs for \(r=2,3,4,5,6,7,8,9\) are respectively \(6,24,720,10080,362880,7257600,159667200,6227020800\). The earlier general cutoff \((j_r+1)!\) is sharp for some exponents but not for others.

## Assumptions and scope
For any \(n\in\mathbb Z_{\ge0}\), use its unique factorial-base expansion \(n=\sum_{i\ge1}d_i i!\) with \(d_i\in\{0,\ldots,i\}\) and only finitely many nonzero digits, and put \(S_{r,!}(n)=\sum_{i\ge1}d_i^r\). The theorem holds for every **integer** exponent \(r\ge2\) and every nonnegative integer input. The number \(j_r\) exists because factorial growth eventually exceeds fixed power growth. The set defining \(a_r\) is nonempty because \(a=0\) is admissible: \(P_r\ge0\).

## Proof
Write \(j=j_r\). By the minimality of \(j\), for every \(1\le i<j\) one has \(i!\le i^{r-1}\), so \(i^r-i\,i!\ge0\). For the digit contribution \(f_i(t)=t^r-i!\,t\) on the real interval \([0,i]\), convexity for \(r\ge2\) gives
\[
 \max_{0\le t\le i}f_i(t)=\max\{f_i(0),f_i(i)\}=i^r-i\,i!.
\]
Thus for every nonnegative integer \(n<(j+1)!\), writing its \(j\)-th factorial digit as \(a\in\{0,\ldots,j\}\) gives
\[
 S_{r,!}(n)-n=\sum_{i=1}^{j}\bigl(d_i^r-i!\,d_i\bigr)
 \le P_r+a^r-a\,j!.
\]
This upper bound is **attained within each block of numbers whose \(j\)-th digit is \(a\)**: take all lower digits maximal, \(d_i=i\) for \(1\le i<j\), giving the number
\[
 n_a=a\,j!+\sum_{i=1}^{j-1}i\,i!=(a+1)j!-1.
\]
Consequently \(S_{r,!}(n_a)-n_a=P_r+a^r-a\,j!\). By definition of \(a_r\), every integer \(n\) with \((a_r+1)j!\le n<(j+1)!\) has top digit \(a>a_r\) and therefore \(S_{r,!}(n)-n<0\); for \(a_r=j\), this interval is empty.

For all \(n\ge(j+1)!\), the established all-exponent strict-descent theorem of Sánchez Garza and Treviño (2021, Theorem 1) gives \(S_{r,!}(n)<n\). Together these prove strict descent for every \(n\ge (a_r+1)j!\). Conversely, the exact block-end witness \(n_{a_r}=(a_r+1)j!-1\) satisfies \(S_{r,!}(n_{a_r})-n_{a_r}=P_r+a_r^r-a_rj!\ge0\). No smaller cutoff works; the stated value is exact. \(\square\)

## Verification
`verify.py` provides an independent factorial-digit evaluator, recomputes \(j_r,P_r,a_r,C_r\) for \(2\le r\le40\), and checks exact endpoint identities. It also exhaustively scans every integer below the published bound \((j_r+1)!\) for \(2\le r\le6\), independently recovering the last nondecreasing input. These finite checks are supplementary: the all-exponent statement depends on the preceding proof and the explicitly cited published high-range bound, not on extrapolation. Expected initial cutoffs are \(6,24,720,10080,362880\).

## Relationship to prior work
Carlson, Goedhart, and Harris, *Sequences of consecutive factoradic happy numbers*, arXiv:1912.02044v1 (2019), defined these maps and derived an eventually-decreasing bound for exponents in a finite range (Theorem 3 in the arXiv HTML; the journal theorem numbering differs). Sánchez Garza and Treviño, *On a Sequence Related to the Factoradic Representation of an Integer*, Journal of Integer Sequences 24 (2021), Article 21.8.5, Theorem 1, extended the uniform sufficient bound \((j_r+1)!\) to **all** positive exponents. Their theorem does not identify the least cutoff. The new argument optimizes the lower digits at each top-digit block endpoint and supplies a sharp witness for every exponent, obtaining the exact least cutoff. For example, at \(r=3\) the previously sufficient cutoff is \(120\), whereas the exact cutoff is \(24\). The reported first-occurrence sequence \(j_r\) (OEIS A230319) contains only the index, not this sharp descent invariant.

## Limitations
This exact cutoff concerns the **one-step** inequality \(S_{r,!}(n)<n\), not the classification of attracting cycles, fixed points, or happy numbers. The mathematical proof invokes the published all-exponent bound for inputs at least \((j_r+1)!\), while proving the sharp subthreshold refinement from first principles. Priority beyond the primary works inspected is not certified; an unindexed equivalent result could exist.

## References
1. J. Carlson, E. G. Goedhart, and P. E. Harris, *Sequences of consecutive factoradic happy numbers*, arXiv:1912.02044v1 (first posted 2019-12-04), https://arxiv.org/html/1912.02044v1.
2. M. Sánchez Garza and E. Treviño, *On a Sequence Related to the Factoradic Representation of an Integer*, *Journal of Integer Sequences* 24 (2021), Article 21.8.5, Theorem 1, https://cs.uwaterloo.ca/journals/JIS/VOL24/Trevino/trevino6.pdf.
3. OEIS A230319, factorial-versus-power crossing index, https://oeis.org/A230319.
