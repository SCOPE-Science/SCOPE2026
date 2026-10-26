# The exact consecutive-square GCD for Lucas-balancing numbers

## Finding

Let the balancing numbers and Lucas-balancing numbers be given by
\[
B_0=0,\quad B_1=1,\quad B_{n+2}=6B_{n+1}-B_n,
\qquad
C_0=1,\quad C_1=3,\quad C_{n+2}=6C_{n+1}-C_n.
\]
For every integer \(k\ge1\), define
\[
S_n(k)=\sum_{i=1}^{k}C_{n+i}^{2},\qquad
G_C(k)=\gcd\{S_n(k):n\ge0\},
\]
where the infinite gcd means the unique nonnegative generator of the ideal of \(\mathbb Z\) spanned by the listed positive integers.

**Theorem.** For every \(k\ge1\),
\[
\boxed{G_C(k)=\gcd(k,B_k).}
\]
In particular this gives a closed formula for the Lucas-balancing case of the squared consecutive-sum GCD in Question 30 of Mbirika--Schrader--Spilker (2023).

## Assumptions and scope

The sequences have the initial values and recurrence above, with all indices nonnegative. The window length \(k\) is any positive integer; there are no coprimality or parity restrictions. The formula concerns squares of consecutive **Lucas-balancing** terms, not squares of balancing or cobalancing terms. Ordinary positive greatest common divisors are used.

## Proof

Put \(u=3+2\sqrt2\), so \(u^{-1}=3-2\sqrt2\). The Binet representations
\[
B_n=\frac{u^n-u^{-n}}{4\sqrt2},\qquad
C_n=\frac{u^n+u^{-n}}2
\]
follow from the initial values and common characteristic equation. They yield, for \(n\ge0\) and \(k\ge1\),
\[
C_j^2=\frac{C_{2j}+1}{2},\qquad
\sum_{i=1}^k C_{2(n+i)}=B_k C_{2n+k+1}.
\]
The second identity is the finite geometric sum, valid for both \(u\) and \(u^{-1}\). Hence
\[
\tag{1}2S_n(k)=k+B_k C_{2n+k+1}.
\]
Using \(C_{r+2}-C_r=16B_{r+1}\), equation (1) gives
\[
\tag{2}S_{n+1}(k)-S_n(k)=8B_k B_{2n+k+2}.
\]

The recurrence for \(B\) has determinant one, so \(\gcd(B_j,B_{j+1})=1\) for every \(j\ge0\). Furthermore,
\[
\gcd(B_j,B_{j+2})
=\gcd(B_j,6B_{j+1}-B_j)
=\gcd(B_j,6).
\]
The even-index subsequence and the odd-index subsequence each satisfy the unimodular recurrence \(X_{n+2}=34X_{n+1}-X_n\). Their respective entire gcds thus equal the gcds of their first two terms. Modulo \(6\), the original recurrence gives \(B_{2r}\equiv0\pmod6\) and \(B_{2r+1}\equiv(-1)^r\pmod6\). Therefore
\[
\tag{3}\gcd_{n\ge0}B_{2n+k+2}=
\begin{cases}1&k\text{ odd},\\6&k\text{ even}.\end{cases}
\]
Taking the gcd of \(S_0(k)\) and all successive differences in (2) proves
\[
\tag{4}G_C(k)=
\begin{cases}
\gcd(S_0(k),8B_k)&k\text{ odd},\\
\gcd(S_0(k),48B_k)&k\text{ even}.
\end{cases}
\]

**Odd windows.** Each \(C_j\) is odd (by its recurrence). When \(k\) is odd, \(S_0(k)\) is odd, as is \(B_k\). Thus the first case of (4) reduces to \(\gcd(S_0(k),B_k)\). Equation (1) at \(n=0\) says \(2S_0(k)=k+B_k C_{k+1}\). Since \(B_k\) is odd, the factor two is invertible modulo \(B_k\), and
\[
G_C(k)=\gcd(k,B_k).
\]

**Even windows, odd prime divisors.** Suppose \(k\) is even. At any odd prime \(\ell\ne3\), the factor \(48\) is a unit, and the same identity \(2S_0(k)=k+B_kC_{k+1}\) proves
\[
\nu_\ell(G_C(k))=\min\{\nu_\ell(k),\nu_\ell(B_k)\}.
\]
For \(\ell=3\), the recurrence modulo \(3\) shows \(3\mid B_j\) if \(j\) is even, and \(3\mid C_j\) if \(j\) is odd. The Binet identity
\[
B_{3j}=B_j(4C_j^2-1)
\]
shows that if \(j\) is even, then \(\nu_3(B_{3j})\ge\nu_3(B_j)+1\), since \(C_j\equiv\pm1\pmod3\). Writing the even index as \(k=2m3^t\) with \(3\nmid m\), induction from \(3\mid B_{2m}\) gives \(\nu_3(B_k)\ge t+1\). Because \(k+1\) is odd, \(3\mid C_{k+1}\); hence equation (1) gives \(\nu_3(S_0(k))=t=\nu_3(k)\). Consequently
\[
\nu_3(G_C(k))=t=\min\{\nu_3(k),\nu_3(B_k)\}.
\]

**Even windows, the prime two.** Write \(k=2^a m\), where \(a\ge1\) and \(m\) is odd. The doubling identity \(B_{2j}=2B_jC_j\) and the easily verified congruences
\[
B_j\equiv j\pmod4,\qquad C_j\equiv(-1)^j\pmod4
\]
give
\[
\frac{B_k}{2^a}=B_m\prod_{r=0}^{a-1}C_{2^rm}\equiv-m\pmod4.
\]
Every factor \(C_j\) is odd, so \(\nu_2(B_k)=a\). As \(k+1\) is odd, \(C_{k+1}\equiv-1\pmod4\); equation (1) gives
\[
\frac{2S_0(k)}{2^a}
=m+\frac{B_k}{2^a}C_{k+1}
\equiv 2m\pmod4.
\]
Thus \(\nu_2(S_0(k))=a\). Since \(\nu_2(48B_k)=a+4\), the second case of (4) gives \(\nu_2(G_C(k))=a\), exactly the two-adic valuation of \(\gcd(k,B_k)\).

Every prime valuation of the two positive integers now agrees. This proves the theorem for all \(k\ge1\). \(\square\)

## Verification

Run the included standalone Python 3 file `verify.py` without external dependencies. It reconstructs both recurrences, checks the Binet-free identities and direct sliding-window gcds for every \(1\le k\le250\) and \(0\le n\le18\), and checks the claimed formula. These tests confirm many finite cases, while the proof above establishes the universal statement.

## Relationship to prior work

Mbirika, Schrader and Spilker (2023), arXiv:2301.05758, Question 30, explicitly ask for closed forms for gcds of consecutive **squares** of the six number sequences and leave the Lucas-balancing-square case without a closed formula. The same article determines corresponding gcds for unsquared terms; that statement does not cover squares. Mbirika and Spilker (2022), arXiv:2204.12626, treat squares of generalized Fibonacci sequences satisfying a different recurrence. Komatsu and Panda (2016), arXiv:1608.05918, derive balancing-number sum identities, not this infinite gcd. The present formula resolves one explicitly identified case of the 2023 question. The publication literature may contain unindexed or implicit equivalent derivations; the originality comparison is not a claim of certified publication priority.

## Limitations

No formula is asserted here for the other three unknown squared-sum gcd cases listed in Question 30. This is a self-reviewed result, not an independently audited or published theorem; originality assessment is limited to the sources and searches documented in the companion review.

## References

1. aBa Mbirika, Janee Schrader and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of \(k\) consecutive Pell, balancing, and related numbers*, Journal of Integer Sequences **26** (2023), Article 23.6.4; arXiv:2301.05758v1 (first public date 2023-01-13), Question 30.
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (2022).
3. Takao Komatsu and Gopal Krishna Panda, *On several kinds of sums of balancing numbers*, arXiv:1608.05918 (2016).
4. OEIS A001109 (balancing numbers) and A001541 (Lucas-balancing numbers).
