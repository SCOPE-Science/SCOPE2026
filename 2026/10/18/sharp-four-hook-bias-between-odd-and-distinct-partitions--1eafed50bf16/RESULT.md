# Sharp four-hook bias between odd and distinct partitions

## Finding
For every integer \(n\ge0\), write \(a_4(n)\) for the sum of the numbers of four-hooks over all partitions of \(n\) into odd parts, and \(b_4(n)\) for the analogous sum over partitions into distinct parts. Then
\[
a_4(n)-b_4(n)\ge0\quad(n\ne8),\qquad a_4(8)-b_4(8)=-1.
\]
Thus the sharp least terminal threshold in the hook-bias conjecture is \(N_4=8\): the inequality holds for every \(n>8\), but fails at \(n=8\). The argument is uniform for all integers, not an extrapolation from a finite check.

## Assumptions and scope
A partition \(\lambda=(\lambda_1,\ldots,\lambda_\ell)\) is a nonincreasing finite sequence of positive integers. The hook length at cell \((i,j)\) of its Ferrers diagram is \(\lambda_i-j+1+|\{r>i:\lambda_r\ge j\}|\). A four-hook is one whose hook length is four. The empty partition at \(n=0\) contributes zero. Define \(q(n)\) to be the number of partitions of \(n\) into distinct parts, with \(q(0)=1\) and \(q(n)=0\) for \(n<0\); put \(Q(q)=\prod_{j\ge1}(1+q^j)\) as a formal power series (here the same italic \(q\) denotes the series variable). All statements are about formal coefficients over the integers. No asymptotic assumptions are made.

## Proof
**1. Exact four-hook generating function.** Specializing the already published all-hook generating-function identity of Craig, Dawsey and Han [2, Theorem 2.1] at hook length four, and summing its finite geometric series, gives
\[
\sum_{n\ge0}(a_4(n)-b_4(n))q^n
=\frac{q^7(1-q)R(q)Q(q)}{(1-q^6)(1-q^8)},
\]
where
\[
R(q)=1-q+q^2+q^3+2q^4+2q^7+2q^8+q^9-q^{10}.
\]
For reproducibility, the corresponding two normalized rational factors are
\[
\frac{\sum a_4(n)q^n}{Q(q)}=\frac{q^4}{1-q^8}+q^4(1+q^2)\left(\frac1{1-q^4}-\frac q{1-q^6}\right)+\frac{q^9}{1-q^6}+q^5\left(\frac1{1-q^2}-\frac{q^3}{1-q^4}\right)
\]
and
\[
\frac{\sum b_4(n)q^n}{Q(q)}=\frac{q^4(2+2q+3q^2+2q^3+2q^4+2q^5)}{(1-q)(1+q)^2(1+q^2)(1-q+q^2)(1+q+q^2)}.
\]
The displayed difference identity is obtained by taking a common denominator. The all-hook identity is used as a known lemma, not claimed as new.

**2. A monotone auxiliary sequence.** Put
\[
H(q)=\frac{Q(q)}{(1-q^6)(1-q^8)},\qquad K(q)=(1-q)H(q)=\sum_{n\ge0}K_nq^n,
\]
and set \(K_n=0\) for \(n<0\). Since \(q(n)\) is nondecreasing (add a part of size one under the odd-parts interpretation), the coefficients of \((1-q)Q(q)\) are nonnegative. Multiplication by \((1-q^6)^{-1}(1-q^8)^{-1}\) proves \(K_n\ge0\) for all integers \(n\).

We next prove \(K_n-K_{n-1}\ge0\) for \(n\ge11\). Put
\[
E(q)=(1-q)^2Q(q)=\sum_{n\ge0}e_nq^n.
\]
The established convexity theorem for distinct-part partitions [3] gives \(e_n=q(n)-2q(n-1)+q(n-2)\ge0\) for \(n\ge5\). Direct values from \(q(0),\ldots,q(12)\) show \(e_0=e_3=e_5=e_9=e_{12}=1\), \(e_1=e_4=-1\), and \(e_2=0\). Moreover
\[
K_n-K_{n-1}=[q^n]\frac{E(q)}{(1-q^6)(1-q^8)}=\sum_{a,b\ge0}e_{n-6a-8b}.
\]
We construct an injection from every negative summand with \(n\ge11\) to a distinct positive unit summand in the same total degree. A negative \(e_1\) at indices \((a,b)\) with \(b\ge1\) is paired with \(e_9\) at \((a,b-1)\); if instead \(b=0\) and \(a\ge2\), it is paired with \(e_5\) at \((a-2,1)\). A negative \(e_4\) with \(b\ge1\) is paired with \(e_{12}\) at \((a,b-1)\); if \(b=0\) and \(a\ge2\), it is paired with \(e_0\) at \((a-2,2)\). Every match preserves the total degree, and targets are distinct since they have different base indices. The unmatched negative cases occur only at total degrees \(1,4,7,10\). Thus all summands at degrees \(n\ge11\) pair off nonnegatively, proving the asserted eventual monotonicity of \(K_n\).

**3. Coefficient positivity and the sharp exception.** Write \(m=n-7\). Expanding \(R\) in the exact generating function yields
\[
\begin{aligned}
a_4(n)-b_4(n)={}&(K_m-K_{m-1})+K_{m-2}+K_{m-3}+2K_{m-4}\\
&+2K_{m-7}+2K_{m-8}+(K_{m-9}-K_{m-10}).
\end{aligned}
\]
For \(n\ge27\), both bracketed differences have indices at least \(11\), hence are nonnegative by Step 2; all other terms are nonnegative. For the remaining \(0\le n\le26\), the exact coefficient values, computed from the displayed generating series, are
\[
(0,0,0,0,0,0,0,1,-1,1,2,1,2,2,4,6,7,7,11,13,17,22,27,31,40,48,57).
\]
Only the coefficient at \(n=8\) is negative, and it equals \(-1\). This proves the theorem.

## Verification
A standalone checker in `artifacts/verify.py` performs symbolic rational-function reduction of the four-hook specialization to the displayed rational identity; independently enumerates odd and distinct partitions through \(n=26\) and computes each hook directly; evaluates \(q(n)\), the auxiliary coefficients, and the matching targets; and checks the stated finite table. Exact integer arithmetic is used throughout. The finite calculations verify the boundary and formula; the general inequality rests on the proof in Step 2.

## Relationship to prior work
Ballantine, Burson, Craig, Folsom and Wen [1, Conjecture 1.7 and Figure 2] predicted \(N_4=8\) but proved the hook inequalities only at lengths two and three. Craig, Dawsey and Han [2, Theorems 1.2 and 2.1] proved eventual hook bias at every fixed length, but explicitly stated that their proof is noneffective and determines no optimal threshold. This result uses their known generating function and the known convexity of the distinct partition function [3] to settle the exact four-hook endpoint. It neither claims the existing generating-function identity nor the convexity theorem as new.

## Limitations
No sharp threshold for hook lengths other than four is established here. The proof supplies nonnegativity, not a separately justified universal strict-positivity statement for all larger \(n\). The theoretical comparison is bounded to the inspected primary literature and mathematical findings records; independent external audit is not performed.

## References
[1] C. Ballantine, H. Burson, W. Craig, A. Folsom and B. Wen, *Hook Length Biases and General Linear Partition Inequalities*, arXiv:2303.16512, publicly submitted March 29, 2023.

[2] W. Craig, M. L. Dawsey and G.-N. Han, *Inequalities and Asymptotics for Hook Numbers in Restricted Partitions*, arXiv:2311.15013, publicly submitted November 25, 2023; see Theorem 2.1 and Remark 1.3.

[3] *Partition of an Integer into Distinct Bounded Parts: Identities and Bounds*, INTEGERS 12 (2012), article A8, Section 3 (convexity of the distinct-part partition function).
