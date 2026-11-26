# Four-prime classification for Sándor’s displayed prime equation

## Finding
For distinct odd primes \(p<q<r<s\), put \(P=pqrs\) and \(F=(p-1)(q-1)(r-1)(s-1)\). Then
\[
P-2F=5\quad\Longleftrightarrow\quad(p,q,r,s)=(3,5,17,251).
\]
This classifies the four-prime case of the prime equation displayed in Sándor [1], considered as a separate Diophantine equation. Its solution does not solve the totient–divisor equation \(\varphi(4m)+d(4m)=m\) with \(m=2^4P\), where \(d\) counts positive divisors. The latter equation requires \(P-2F=7\), not \(5\).

## Proof
Since \(P-2F=5>0\),
\[
2(1-1/p)(1-1/q)(1-1/r)(1-1/s)<1.
\]
If \(p\ge5\) then the left hand side is at least \(2(4/5)(6/7)(10/11)(12/13)=5760/5005>1\). Thus \(p=3\). If then \(q\ge11\), the left hand side is at least \((4/3)(10/11)^3=4000/3993>1\). Hence \(q=5\) or \(7\). If \(q=7\), both \(P\) and \(2F=24(r-1)(s-1)\) are divisible by three, but five is not.

With \(q=5\), expansion gives
\[
(r-16)(s-16)=235.
\]
If both factors are negative their product is at most \(9\cdot5=45\), since \(5<r<s\) are odd primes. They cannot be zero or have opposite signs, so both are positive. The positive factor pairs of \(235=5\cdot47\) give \((r,s)=(17,251)\) or \((21,63)\). The latter is composite in both entries. Both entries of the former are prime and give \(P=64005\), \(F=32000\), verifying \(P-2F=5\).

Finally \(4m=2^6P\), so \(\varphi(4m)=32F\) and \(d(4m)=7\cdot 2^4\). Thus the totient–divisor equation is equivalent to \(P-2F=7\) in the specified family. At the solution to the displayed prime equation the corresponding \(m=1024080\) gives \(\varphi(4m)+d(4m)=1024112\), not \(m\).

## Verification and scope
`verify.py` checks the exact bounds, factor pairs, primality, and the arithmetic-function normalization. The inequalities and factorization prove exhaustiveness without a global prime cutoff. No claim about other prime supports, other powers of two, or infinitude is made.

## Relationship to prior work
Sándor [1, p. 136] displays the prime equation with right-hand side \(t+1\) for \(t\) odd prime factors, and in the four-prime instance exhibits \((3,5,17,251)\) after choosing the two smallest primes to be \(3,5\). The classification here proves those choices are forced. For the separate arithmetic-function equation with \(m=2^t\prod_i p_i\) and \(t\) distinct odd primes, the divisor count of \(4m\) is \((t+3)2^t\); the normalization yields a right-hand side of \(t+3\), not \(t+1\). The obstruction to solutions of that actual equation with four distinct odd prime factors and squarefree odd part is already given in [2].

## References
[1] J. Sándor, “On certain equations and inequalities involving the arithmetical functions \(\varphi(n)\) and \(d(n)\) – II,” *Notes on Number Theory and Discrete Mathematics* 29 (2023), 130–136, DOI 10.7546/nntdm.2023.29.1.130-136.

[2] [Squarefree odd-part obstruction for the totient–divisor quarter equation](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-squarefree-odd-part-obstruction-for-the-totient-divisor-quarter--13b58b41e74c), four-odd-prime case.
