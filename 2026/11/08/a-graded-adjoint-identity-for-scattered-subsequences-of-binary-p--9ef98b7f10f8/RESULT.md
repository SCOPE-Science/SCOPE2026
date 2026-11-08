# A graded adjoint identity for scattered subsequences of binary palindromes

## Finding

Let \(u\) be any finite binary word, including the empty word, and let \(P_w(t)=\sum_{j\ge1}d_j(w)t^j\), where \(d_j(w)\) counts **distinct nonempty** length-\(j\) strings appearing as scattered subsequences of \(w\), rather than their embeddings. Define \(A_u(t)\) and \(B_u(t)\) to count distinct nonempty subsequences of \(u\) ending respectively in \(0\) and \(1\), by length; thus \(P_u=A_u+B_u\). Put \(v_u=(A_u,B_u,1)^{\mathsf T}\), and
\[
H(t)=\begin{pmatrix}t-1&t&t\\t&t-1&t\\t&t&0\end{pmatrix},\qquad
T_0(t)=\begin{pmatrix}t&t&t\\0&1&0\\0&0&1\end{pmatrix},\quad
T_1(t)=\begin{pmatrix}1&0&0\\t&t&t\\0&0&1\end{pmatrix}.
\]
Then the complete **length-graded** scattered-subsequence enumerators of every even or odd binary palindrome satisfy
\[
\boxed{\ tP_{u u^{\mathrm R}}(t)=v_u^{\mathsf T}H(t)v_u,\qquad
tP_{u c u^{\mathrm R}}(t)=v_u^{\mathsf T}H(t)T_c(t)v_u\ }
\]
for **each** \(c\in\{0,1\}\), with reversal \(u^{\mathrm R}\). Equivalently, the even transform is
\[
\boxed{\ tP_{u u^{\mathrm R}}=(t-1)(A_u^2+B_u^2)+2tA_uB_u+2t(A_u+B_u).\ }
\]
These are polynomial identities for every half-word, giving every distinct-subsequence length count from just the two ending-letter enumerators of the half-word. The two possible central letters are covered by the same adjoint form.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A scattered subsequence of \(w=w_1\cdots w_n\) is a string \(w_{i_1}\cdots w_{i_j}\) with strictly increasing indices; equal strings realized by different index tuples are counted only once. \(P_w\) excludes the empty word. The length-zero half-word and length-one palindromes are included. The indeterminate \(t\) is formal. The theorem makes no claim that the palindromic *subsequences* themselves are being counted: the host is palindromic, and the query subsequence is unrestricted.

## Proof

**1. Deterministic ending-letter recurrence.** For any prefix \(x\), let \(A_x\) and \(B_x\) be defined as above. On appending \(0\), every distinct old subsequence, including the empty string, yields exactly one distinct subsequence ending in \(0\), and every subsequence of \(x0\) ending in \(0\) has such a representation by the *last appended position*; therefore the new ending-\(0\) polynomial is \(t(1+A_x+B_x)\), while the ending-\(1\) polynomial is unchanged. The case of appended \(1\) is symmetric. Thus \(v_{x0}=T_0v_x\) and \(v_{x1}=T_1v_x\), with \(v_{\varepsilon}=(0,0,1)^{\mathsf T}\). These recurrences count distinct strings, not embeddings.

**2. Common adjoint form.** Direct multiplication gives
\[
T_i(t)^{\mathsf T}H(t)=H(t)T_i(t)\qquad(i=0,1),\qquad \det H(t)=2t^2.
\]
In the rational-function field \(\mathbb Q(t)\), \(H\) is invertible. If \(M(u)=T_{u_m}\cdots T_{u_1}\) for \(u=u_1\cdots u_m\), the common-adjoint identities yield
\[
M(u^{\mathrm R})=H^{-1}M(u)^{\mathsf T}H.
\]

**3. Reflection of the host.** With \(e_3=(0,0,1)^{\mathsf T}\), \(r=(1,1,0)^{\mathsf T}\), note \(He_3=tr\), \(v_u=M(u)e_3\), and \(P_w=r^{\mathsf T}M(w)e_3\). Therefore
\[
\begin{aligned}
tP_{uu^{\mathrm R}}
&=e_3^{\mathsf T}M(u)^{\mathsf T}H M(u)e_3=v_u^{\mathsf T}Hv_u,\\
tP_{ucu^{\mathrm R}}
&=e_3^{\mathsf T}M(u)^{\mathsf T}HT_cM(u)e_3=v_u^{\mathsf T}HT_cv_u.
\end{aligned}
\]
All expressions are identities of formal polynomials after multiplying by \(t\); no singular specialization at \(t=0\) was assumed. Expanding the first quadratic form gives the claimed scalar identity. This completes the proof for every half-length and both centers.

## Verification

The accompanying `verify_graded.py` independently computes the length profile by the standard whole-host ending-letter dynamic program, and also constructs explicit sets of distinct subsequences at small lengths. It checked all \(8{,}191\) binary half-words of lengths \(0\) through \(12\) in the even case, all \(16{,}382\) odd center choices, and \(381\) full-word subset enumerations; all compared coefficient by coefficient. It prints `VERIFY_OK`. For example, the even palindrome `0110` has profile \((2,4,3,1)\) in lengths \(1\) through \(4\). These finite tests corroborate; the matrix proof establishes all lengths.

## Relationship to prior work

Żak, *Finding binary words with a given number of subsequences* (first arXiv public date 2022-10-01, arXiv:2210.00342), studies the **ungraded total** and gives a concatenation theorem, Euclidean encoding, and alternating-word extremals. In particular, specializing the current even identity at \(t=1\) is compatible with that paper's bilinear total-count theorem; this specialization is NOT asserted to be new. The present result retains **all length coefficients**, with a common adjoint and a uniform middle-letter formula; these do not follow from an ungraded scalar count alone. Flaxman–Harrow–Sorkin (2004) maximizes the length-graded subsequence profile for unrestricted host words, but does not supply the reflected-half formula for palindromic hosts. Mahalingam–Pandoh (2021) studies **palindromic subsequence strings** of arbitrary hosts, a different counting observable. The matrix-adjoint identity is the contribution; the standard DP and ungraded Fibonacci extremals are credited prior background.

## Limitations

Only the binary alphabet is treated; no analogous adjoint identity is asserted for larger alphabets. The identity is a structural, exact all-length enumerator, not an independent novelty certificate; equivalent formulations in unindexed work remain possible. No claim of coefficientwise optimality for any palindrome family is made. The finite verifier is not a substitute for the proof, and there has been no independent expert audit.

## References

- R. Żak, *Finding binary words with a given number of subsequences*, arXiv:2210.00342 (initial public posting 2022-10-01). https://arxiv.org/abs/2210.00342
- A. Flaxman, A. W. Harrow, G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electron. J. Combin. 11 (2004), #R8. https://doi.org/10.37236/1761
- K. Mahalingam, P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729 (2021). https://arxiv.org/abs/2108.02729
