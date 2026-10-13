# The exact square-window GCD for Lucas-cobalancing numbers

## Finding
Let \(c_0=-1\), \(c_1=1\), and \(c_{n+2}=6c_{n+1}-c_n\) for \(n\ge0\). Let \(B_0=0\), \(B_1=1\), and \(B_{n+2}=6B_{n+1}-B_n\). For every positive integer \(k\), define
\[
H(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}c_{n+j}^{2}\right).
\]
Then
\[
\boxed{H(k)=\begin{cases}3\gcd(B_k,k),&k\equiv3\pmod6,\\\gcd(B_k,k),&k\not\equiv3\pmod6.\end{cases}}
\]
In particular, the additional factor three occurs at precisely the odd multiples of three. This establishes an exact formula for the Lucas-cobalancing square-window problem raised in Question 30 of Mbirika--Schrader--Spilker (2023).

## Assumptions and scope
Every index \(k\) is an arbitrary positive integer; \(n\) ranges over all nonnegative integers. The GCD of an infinite sequence of positive integers means its positive common divisor of largest magnitude. Let \(P_0=0,P_1=1\), \(Q_0=Q_1=1\), and \(P_{m+2}=2P_{m+1}+P_m\), \(Q_{m+2}=2Q_{m+1}+Q_m\). These are the Pell and associated Pell sequences. Their standard identities, derivable directly from the recurrences or Binet expressions, include
\[
c_j=Q_{2j-1}\ (j\ge1),\qquad B_j=P_jQ_j,\qquad Q_{2m}=2Q_m^2-(-1)^m,\qquad Q_{m+4}-Q_m=8P_{m+2}.
\]
No primality, asymptotic, or finite-index restriction is imposed.

## Proof
**1. An exact moving-window identity.** Put \(S_n=\sum_{j=1}^k c_{n+j}^2\). Since \(2Q_{2j-1}^2=Q_{4j-2}-1\), the elementary geometric sum for the Pell roots gives
\[
\sum_{j=1}^{k}Q_{4n+4j-2}=B_k Q_{4n+2k},
\]
and therefore
\[
2S_n=B_kQ_{4n+2k}-k.\tag{1}
\]
This may also be checked by the Binet formulas \(Q_m=(\gamma^m+\delta^m)/2\), \(P_m=(\gamma^m-\delta^m)/(2\sqrt2)\) with \(\gamma=1+\sqrt2\), \(\delta=1-\sqrt2\). Subtracting (1) at adjacent positions yields
\[
S_{n+1}-S_n=4B_kP_{4n+2k+2}.\tag{2}
\]

**2. Reduction of the infinite GCD.** The Pell sequence is a strong divisibility sequence:
\[
\gcd(P_r,P_s)=P_{\gcd(r,s)}\quad(r,s\ge1).
\]
Indeed \(P_{r+s}=P_rP_{s+1}+P_{r-1}P_s\), and consecutive Pell numbers are coprime, so the Euclidean algorithm applies to indices. Thus
\[
\gcd_{n\ge0}P_{4n+2k+2}=P_{\gcd(4,2k+2)}=
\begin{cases}2,&k\text{ even},\\12,&k\text{ odd}.\end{cases}
\]
The GCD of all window sums equals the GCD of the initial window and all adjacent differences. Hence (1)--(2) imply the *exact* finite reduction
\[
H(k)=\begin{cases}
\gcd\bigl((B_kQ_{2k}-k)/2,8B_k\bigr),&k\text{ even},\\
\gcd\bigl((B_kQ_{2k}-k)/2,48B_k\bigr),&k\text{ odd}.
\end{cases}\tag{3}
\]
No finite approximation of an infinite GCD is involved in this reduction.

**3. Odd-prime valuations.** At any odd prime \(\ell\ne3\), the second argument in (3) has valuation \(\nu_\ell(B_k)\), and reduction of its first argument modulo powers of \(\ell\) dividing \(B_k\) gives \(-k/2\). Therefore
\[
\nu_\ell(H(k))=\min\{\nu_\ell(B_k),\nu_\ell(k)\}\qquad(\ell\ne2,3).
\]
If \(k\) is even, the coefficient in (3) is \(8B_k\), so the same statement also holds for \(\ell=3\). If \(k\) is odd, then \(3\nmid B_k\), because \(B_{m+2}\equiv-B_m\pmod3\) and \(B_0=0,B_1=1\). Also \(3\mid Q_{2k}\): the odd-indexed \(Q_k\) are units modulo three, and \(Q_{2k}=2Q_k^2+1\equiv0\pmod3\). Thus \(S_0\equiv-k/2\pmod3\), while the second argument in (3) has precisely one factor of three. Accordingly \(\nu_3(H(k))=1\) exactly when the odd \(k\) is divisible by three, and is zero otherwise.

**4. The prime two.** For odd \(k\), every \(c_j\) is odd, so \(S_0\) is odd; also \(B_k\) is odd, and the required two-adic valuation is zero. Suppose \(k=2^t u\) with \(t\ge1\) and \(u\) odd. The duplication identity \(P_{2m}=2P_mQ_m\) and oddness of every \(Q_m\) show \(\nu_2(P_k)=t\); hence \(\nu_2(B_k)=t\). To locate \(S_0\) precisely, use the recurrence modulo four:
\[
P_u\equiv1,\quad Q_u\equiv u,\quad Q_{2u}\equiv3,\quad Q_{2^j u}\equiv1\ (j\ge2)\pmod4.
\]
Iterating duplication shows
\[
\frac{P_k}{2^t}\equiv\begin{cases}u,&t=1,\\3u,&t\ge2\end{cases}\pmod4,
\qquad Q_k\equiv\begin{cases}3,&t=1,\\1,&t\ge2\end{cases}\pmod4.
\]
Consequently \(B_k/2^t\equiv3u\pmod4\), and \(Q_{2k}\equiv1\pmod4\). It follows that
\[
\frac{B_kQ_{2k}-k}{2^t}\equiv2u\pmod4,
\]
so \(\nu_2(S_0)=t\). Since \(\nu_2(8B_k)=t+3\), formula (3) gives \(\nu_2(H(k))=t=\nu_2(\gcd(B_k,k))\). All prime valuations now agree with the asserted formula. \(\square\)

## Verification
The accompanying standalone `verify.py` uses exact arbitrary-precision integer arithmetic. It independently constructs both recurrences, compares the formula with the GCD of the first 25 square-windows for every \(1\le k\le320\), checks 8,000 individual window-sum identities, checks 12,100 Pell strong-divisibility pairs, and tests the even-index two-adic unit congruence for 160 indices. The saved actual output appears in `verification_output.txt`. These finite checks do not prove the unrestricted statement; its proof is the preceding identities and valuation argument.

## Relationship to prior work
Mbirika, Schrader and Spilker (2023), Question 30, asks for formulas for the GCDs of consecutive squared balancing, Lucas-balancing, cobalancing and Lucas-cobalancing numbers. They give numerical evidence that the Lucas-balancing and Lucas-cobalancing squared-window GCDs agree except at window lengths congruent to three modulo six, when the Lucas-cobalancing value is triple. The theorem proves the precise Lucas-cobalancing formula directly and establishes the exceptional factor by a prime-three valuation argument. Their Partial Result 29 treats squared Pell and associated Pell numbers, not this odd-index associated-Pell subsequence. Mbirika and Spilker (2022) treat generalized Fibonacci sequences with recurrence \(G_{n+2}=G_{n+1}+G_n\), not the recurrence here. The present formula does not rely on a conjectured comparison to another squared-window sequence.

## Limitations
The formula still involves \(\gcd(B_k,k)\), whose further structural classification is a separate question (Question 31 in the 2023 paper). The theorem does not determine the squared cobalancing (without Lucas prefix) GCD, and it does not imply formulas for higher powers. Bibliographic searches cannot rule out unindexed equivalent results.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of \(k\) Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4, arXiv:2301.05758v1 (first public 2023-01-13), especially Definition 7, Convention 1, Section 6.1, Question 30 and Question 31. https://arxiv.org/abs/2301.05758
2. aBa Mbirika and Jürgen Spilker, *GCD of Sums of \(k\) Consecutive Squares of Generalized Fibonacci Numbers*, Fibonacci Quarterly 60 (2022), 255–269, arXiv:2204.12626v1 (first public 2022-04-26). https://arxiv.org/abs/2204.12626
