# A three-support obstruction for the unitary divisor-sum minus-one equation

## Finding
Let \(\sigma^*(N)\) denote the sum of the unitary divisors of \(N\), and let \(\omega(N)\) be the number of distinct prime divisors. For positive integers \(N\ge2\) and \(M\ge1\),
\[
\sigma^*(N)=MN-1,\qquad \omega(N)\le3
\]
holds if and only if
\[
(N,M)=(2,2).
\]
Equivalently, every solution other than \(N=2\) must have at least four distinct prime factors.

## Assumptions and scope
If
\[
N=\prod_{i=1}^r p_i^{e_i},
\]
with distinct primes \(p_i\), then
\[
\sigma^*(N)=\prod_{i=1}^r \left(p_i^{e_i}+1\right).
\]
Write \(A_i=p_i^{e_i}\), so the \(A_i\) are pairwise coprime prime powers. The theorem concerns only the support range \(r=\omega(N)\le3\); it makes no assertion about existence or nonexistence for \(r\ge4\).

## Proof
Since every factor \(A_i+1\) exceeds \(A_i\), one has \(\sigma^*(N)>N\), so the equation forces \(M\ge2\).

If \(r=1\), then \(\sigma^*(N)=N+1\). Hence
\[
N+1=MN-1
\]
gives
\[
(M-1)N=2.
\]
With \(N\ge2\), this yields exactly \(N=2\) and \(M=2\).

Suppose \(r=2\). Write \(N=AB\) with pairwise coprime prime powers \(2\le A<B\). Then \(B\ge3\), and
\[
\frac{\sigma^*(N)}{N}
=
\left(1+\frac1A\right)\left(1+\frac1B\right)
\le
\frac32\cdot\frac43=2.
\]
But
\[
\frac{\sigma^*(N)}{N}=M-\frac1N,
\]
so \(M=2\). Expanding \((A+1)(B+1)=2AB-1\) gives
\[
(A-1)(B-1)=3.
\]
The only positive factorization would give \(\{A,B\}=\{2,4\}\), contradicting pairwise coprimality. Thus there is no two-support solution.

Suppose \(r=3\). Write \(N=ABC\) with pairwise coprime prime powers \(A<B<C\). The three smallest possible pairwise coprime prime powers are \(2,3,5\), so
\[
\frac{\sigma^*(N)}N
=
\left(1+\frac1A\right)\left(1+\frac1B\right)\left(1+\frac1C\right)
\le
\frac32\cdot\frac43\cdot\frac65
=
\frac{12}{5}.
\]
Also \(N\ge30\). If \(M\ge3\), then
\[
\frac{\sigma^*(N)}N=M-\frac1N\ge3-\frac1{30}>\frac{12}{5},
\]
a contradiction. Hence \(M=2\), and expansion gives
\[
C(AB-A-B-1)=AB+A+B+2. \tag{1}
\]

If \(A=2\), then \(B=3\) makes the left coefficient of \(C\) in (1) zero, which is impossible. For \(B>3\),
\[
C=\frac{3B+4}{B-3}=3+\frac{13}{B-3}.
\]
Thus \(B-3\) is a positive divisor of \(13\), so \(B\in\{4,16\}\), neither coprime to \(A=2\).

If \(A=3\), then
\[
C=\frac{4B+5}{2B-4}=2+\frac{13}{2(B-2)}.
\]
The positive even denominator \(2(B-2)\) cannot divide \(13\), so this case is impossible.

Finally assume \(A\ge4\), hence \(B\ge5\). To have \(C\ge B\), equation (1) would require
\[
B(AB-A-B-1)\le AB+A+B+2.
\]
The difference between the left and right sides is
\[
D(A,B)=AB^2-2AB-B^2-2B-A-2.
\]
At \((A,B)=(4,5)\), \(D(4,5)=19>0\). Moreover,
\[
D(A+1,B)-D(A,B)=B^2-2B-1>0
\]
for \(B\ge5\), and
\[
D(A,B+1)-D(A,B)=2AB-A-2B-3>0
\]
for \(A\ge4\), \(B\ge5\). Hence \(D(A,B)>0\) throughout this region, forcing \(C<B\), contrary to the ordering. No three-support solution exists.

Combining the three cases proves the classification.

## Verification
The accompanying checker evaluates \(\sigma^*(N)\) exactly for every \(2\le N\le200000\) with \(\omega(N)\le3\) and verifies that the only instance for which
\[
N\mid \sigma^*(N)+1
\]
is \(N=2\), giving \(M=2\). This finite computation is regression evidence only; the proof above is unbounded and does not depend on the cutoff.

## Relationship to prior work
Yamada's 2023 paper treats equations involving \(\sigma^*(N)=MN\pm1\) and proves quantitative upper bounds for \(M\). Its introduction records Subbarao's plus-sign result that a solution of \(\sigma^*(N)=MN+1\) with \(M>1\) has at least \(16\) distinct prime factors. Yamada's logarithmic bound in terms of the number of singly occurring prime factors assumes at least four such factors; it does not give the exact minus-sign classification for total support at most three.

Subbarao's 1998 paper was inspected in full text. It formulates and studies the plus-sign congruence \(\sigma^*(N)\equiv1\pmod N\), including the \(16\)-prime lower bound for the plus-sign equation, but the inspected text does not state the minus-sign theorem above. Hasanalizade's 2023 paper likewise concerns only \(\sigma^*(N)=1+MN\).

## Limitations
The theorem does not classify solutions with \(\omega(N)\ge4\), and it does not prove that any nontrivial minus-sign solution exists. The literature comparison is strongest for the full texts and indexed records inspected; older or poorly indexed work on unitary Lehmer analogues remains a residual bibliographic risk.

## References
1. T. Yamada, *On Lehmer's problem and related problems*, arXiv:2303.16853v1, first submitted 2023-03-29, primary MSC 11A25.
2. M. V. Subbarao, *A companion to a Lehmer problem*, Publicationes Mathematicae Debrecen 52 (1998), 683--698.
3. E. Hasanalizade, *On the equation \(\sigma^*(n)=1+Mn\)*, Integers 23 (2023), A31.
