# Exact even-window cubic GCDs for Pell numbers

## Finding

Let \(P_0=0\), \(P_1=1\), \(P_{n+2}=2P_{n+1}+P_n\), and let \(Q_0=Q_1=1\), \(Q_{n+2}=2Q_{n+1}+Q_n\). For every integer \(m\ge 1\), define

\[
G(2m)=\gcd\left\{\sum_{j=1}^{2m}P_{n+j}^{3}:n\ge0\right\}.
\]

Then the exact formula is

\[
\boxed{G(2m)=\begin{cases}
Q_m/\gcd(Q_m,7), & m\ \text{odd},\\[3pt]
3^{\mathbf1_{4\mid m}}P_m/\gcd(P_m,7), & m\ \text{even}.
\end{cases}}
\]

In particular, there is a genuine exceptional divisor at \(7\) and an extra factor \(3\) precisely when \(4\mid m\).

## Assumptions and scope

All sequences above consist of integers with the given standard normalization; \(\gcd\) of an infinite set of positive integers means its positive generator as an ideal of \(\mathbb Z\). There are no constraints on the positive integer \(m\) beyond those stated, and no unproved asymptotic or finite-search assumption. Only even window lengths and Pell cubic powers are classified here.

## Proof

Write \(p=P_m\), \(q=Q_m\), and \(S_n=\sum_{j=1}^{2m}P_{n+j}^{3}\). The Pell addition and norm identities give

\[
q^2-2p^2=(-1)^m,\quad P_{2m}=2pq,\quad Q_{2m}=2q^2-(-1)^m,
\]
\[
P_{r+2m}-P_r=\begin{cases}2qP_{r+m},&m\ \text{odd},\\2pQ_{r+m},&m\ \text{even}.\end{cases}
\]

**A finite upper bound from shifted differences.** The identity \(8P_r^3=P_{3r}-3(-1)^rP_r\) shows that the sequence \((S_n)\) satisfies the reversible integer recurrence

\[
S_{n+4}-12S_{n+3}-30S_{n+2}+12S_{n+1}+S_n=0.
\]

Indeed, the component sequences have characteristic polynomials \(t^2-14t-1\) and \(t^2+2t-1\). The coefficient of \(S_n\) is \(1\), so the GCD of the nonnegative-index windows also divides \(S_0-S_{-1}=P_{2m}^3\), where \(S_{-1}=\sum_{j=0}^{2m-1}P_j^3\). It further divides \(S_1-S_0=P_{2m+1}^3-1\). With \(X=P_{2m+1}\), put \(T=q\) if \(m\) is odd and \(T=p\) if \(m\) is even. Dividing these two differences by \(2T\) yields

\[
(H_0,H_1)=\begin{cases}
(4p^3q^2,\ P_{m+1}(X^2+X+1)),&m\ \text{odd},\\
(4p^2q^3,\ Q_{m+1}(X^2+X+1)),&m\ \text{even}.
\end{cases}
\]

We claim \(\gcd(H_0,H_1)\) has no odd prime divisor when \(m\) is odd, and is exactly \(3^{\mathbf1_{4\mid m}}\) when \(m\) is even. To check this, use \(\gcd(p,q)=1\) and \(X=2pq+2q^2-(-1)^m\). At an odd prime \(\ell\mid p\), we have \(X\equiv-1\) and \(P_{m+1}\equiv q\) for odd \(m\); for even \(m\), \(X\equiv1\) and \(Q_{m+1}\equiv q\), giving \(H_1\equiv3q\pmod\ell\). At an odd prime \(\ell\mid q\), the roles reverse: for odd \(m\), \(X\equiv1\) and \(P_{m+1}\equiv p\), giving \(H_1\equiv3p\); for even \(m\), \(X\equiv-1\) and \(Q_{m+1}\equiv2p\). In the odd case, \(3\nmid q\) by \(q^2-2p^2=-1\), and \(3\nmid p\) for odd \(m\), so no odd prime divides both. In the even case, the only possibility is \(\ell=3\mid p\), equivalently \(4\mid m\) by Pell recurrence modulo \(3\). Then \(X\equiv1\pmod3\), and \(X^2+X+1\equiv3\pmod9\), while \(3\nmid Q_{m+1}\), proving \(\nu_3(H_1)=1\). Furthermore \(H_1\) is odd in the even case. Therefore

\[
G(2m)\mid\begin{cases}2q,&m\ \text{odd},\\2p\,3^{\mathbf1_{4\mid m}},&m\ \text{even}.\end{cases}
\]

For odd \(m\), precisely \(m\) of the \(2m\) Pell terms are odd, so \(S_0\) is odd. The factor \(2\) may therefore be removed. For even \(m\), we next establish that \(\nu_2(S_0)=\nu_2(p)\), removing the excess factor \(2\) there as well.

**A closed initial-window identity.** The cubic identity above and summation of a recurrence \(A_{r+2}=aA_{r+1}+A_r\), via \(\sum_{r=1}^{N}A_r=(A_{N+1}+A_N-A_1-A_0)/a\), give

\[
56S_0=\begin{cases}
q\bigl((4q^2+3)(P_{3m+3}+P_{3m})-21q\bigr),&m\ \text{odd},\\
p\bigl((4q^2-1)(Q_{3m+3}+Q_{3m})-42p\bigr),&m\ \text{even}.
\end{cases}
\tag{1}
\]

For transparency, the auxiliary sums are \(\sum_{r=1}^{2m}P_{3r}=(P_{6m+3}+P_{6m}-5)/14\) and \(\sum_{r=1}^{2m}(-1)^rP_r=(P_{2m+1}-P_{2m}-1)/2\); inserting the addition and triple-index identities gives (1).

If \(m\) is even, set \(B=(4q^2-1)(Q_{3m+3}+Q_{3m})-42p\). By the recurrence, \((P_0,\ldots,P_7)\bmod8=(0,1,2,5,4,5,6,1)\), and \((Q_0,\ldots,Q_7)\bmod16=(1,1,3,7,1,9,3,15)\), both with period \(8\) at these moduli. For \(m\equiv0,2,4,6\pmod8\), the pair \((p\bmod8,\ (Q_{3m+3}+Q_{3m})\bmod16)\) equals respectively \((0,8),(2,4),(4,0),(6,12)\). Since \(4q^2-1\equiv3\pmod{16}\), in each case \(B\equiv8\pmod{16}\). As \(\nu_2(56)=3\), (1) proves \(\nu_2(S_0)=\nu_2(p)\). Consequently

\[
G(2m)\mid\begin{cases}q,&m\ \text{odd},\\p\,3^{\mathbf1_{4\mid m}},&m\ \text{even}.\end{cases}
\tag{2}
\]

**Prime divisibility and the exceptional prime.** Every difference \(S_{n+1}-S_n\) is divisible by \(2q\) when \(m\) is odd and by \(2p\) when \(m\) is even, by the shifted Pell identity. If \(4\mid m\), then \(3\mid p\), the end Pell terms are congruent modulo \(3\), and \(a^2+ab+b^2\equiv0\pmod3\) when \(a\equiv b\pmod3\); therefore \(3p\mid S_{n+1}-S_n\) for every \(n\). Formula (1) proves that \(S_0\) contains the full prime-power factors of \(q\) (odd case) or of \(p\) (even case) at every prime other than \(2,7\). It also contributes one additional factor \(3\) when \(4\mid m\): indeed \(q^2=1+2p^2\) makes \(4q^2-1=3+8p^2\) divisible by \(3\). Thus the proposed divisor divides all \(S_n\), except that the valuation at \(7\) needs to be established precisely.

Suppose \(7\mid q\) with \(m\) odd. Then \(p^2\equiv4\pmod7\). Since \(Q_{m+1}=q+2p\), the triple-index identity \(P_{3r}=P_r(4Q_r^2-(-1)^r)\) gives \(P_{3m+3}\equiv0\pmod7\), while \(P_{3m}\equiv p\pmod7\). The odd-case bracket in (1) is therefore \(3p\not\equiv0\pmod7\). Hence \(\nu_7(S_0)=\nu_7(q)-1\). Similarly, for \(7\mid p\) with \(m\) even, \(q^2\equiv1\pmod7\). Using \(Q_{m+1}=q+2p\) and \(Q_{3r}=Q_r(4Q_r^2-3(-1)^r)\), we get \(Q_{3m+3}\equiv0\) and \(Q_{3m}\equiv q\pmod7\). The even-case bracket is \(3q\not\equiv0\pmod7\), giving \(\nu_7(S_0)=\nu_7(p)-1\). If \(7\) does not divide the relevant \(q\) or \(p\), no correction is needed. This proves the desired divisor divides all windows. Combining this with (2) proves equality.

## Verification

The included `verify_pell_cubic.py` computes the exact four-window GCD, the closed formula, both identities in (1), the integer-recurrence reversal identity, and the modulus-\(16\) valuation certificate for positive \(m\) in a reproducible finite range. Its successful output is evidence of finite checks, not a substitute for the proof above. Example values for \(m=1,2,3,4,5,6,8,12\) are \(1,2,1,36,41,10,1224,5940\).

## Relationship to prior work

Mbirika, Schrader and Spilker (2023) systematically calculate GCDs of consecutive terms in six Pell-related sequences and give partial *square*-window results; their Convention 1 provides the higher-power notation, but Sections 4–6 do not state cubic Pell-window GCDs. Mbirika and Spilker (2022) study squares of generalized Fibonacci sequences, not the present Pell cubic family. The present result solves all even cubic Pell-window lengths with explicitly explained prime corrections \(3\) and \(7\). No claim is made concerning odd window lengths or arbitrary linear recurrences.

## Limitations

Only the even-window Pell sequence with the stated normalization is covered. An independent mathematical review has not been performed. Unindexed literature or an implicit specialization of a more general recurrence theorem could affect publication priority.

## References

1. aBa Mbirika, Janee Schrader and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4; arXiv:2301.05758 (first posted 2023-01-13).
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269; arXiv:2204.12626 (2022-04-26).
