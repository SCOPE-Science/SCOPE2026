# Complete two-prime-support classification of Sándor's fifth harmonic quotient

## Finding
For every positive integer \(n\) with \(\omega(n)\le2\), the fifth quotient
\[
H_5(n)=\frac{n2^{\omega(n)}}{\sigma^{**}(n)}
\]
is an integer **if and only if** \(n\in\{1,6,45\}\). Both prime exponents, when present, are unrestricted. The three values of the quotient are respectively \(1,2,3\).

## Assumptions and scope
The function \(\omega(n)\) is the number of distinct prime divisors, with \(\omega(1)=0\). The multiplicative function \(\sigma^{**}\) is the sum of the bi-unitary divisors. Its exact prime-power formulas, for every prime \(p\) and integer \(a\ge1\), are
\[
\sigma^{**}(p^a)=\begin{cases}
\displaystyle\sum_{j=0}^{a}p^j,&a\text{ odd},\\[2pt]
\displaystyle\sum_{j=0}^{2m}p^j-p^m
=\frac{p^m-1}{p-1}(p^{m+1}+1),&a=2m.
\end{cases}
\]
Write \(F_p(a)=\sigma^{**}(p^a)\). In all cases \(p^a<F_p(a)<p^{a+1}/(p-1)\), using the complete geometric sum as a strict upper bound (the case \(a=1\) also satisfies the strict bound). For an odd prime \(p\), the number \(F_p(a)\) is even and coprime to \(p\); for \(p=2\), it is odd.

## Proof
**Zero or one prime support.** For \(n=1\), the quotient equals \(1\). If \(n=p^a\), then \(p^a<F_p(a)<2p^a\), so \(1<H_5(p^a)<2\), excluding integrality.

**Two odd prime supports.** Let \(n=p^a q^b\) with odd primes \(p<q\). Put \(A=F_p(a)\) and \(B=F_q(b)\). Integrality means \(AB\mid 4p^a q^b\). Both \(A\) and \(B\) are even and coprime to their base primes. Consequently both have \(2\)-adic valuation exactly \(1\), and their only possible odd prime factors are respectively \(q\) and \(p\). Thus
\[
A=2q^v,\qquad B=2p^u,\qquad 0\le v\le b,\quad0\le u\le a.
\]
The quotient is the odd integer \(p^{a-u}q^{b-v}\), strictly below \(4\). It cannot be \(1\), since \(AB<4p^a q^b\); hence it is \(3\). Thus \(p=3\), \(u=a-1\), \(v=b\), and \(F_3(a)=2q^b\) has \(2\)-adic valuation \(1\).

If \(a\) is odd, then \(F_3(a)=1+3+\cdots+3^a\) is divisible by \(4\), because the terms pair as \(3^{2j}(1+3)\). Write \(a=2m\). If \(m\) is even, both \((3^m-1)/2\) and \(3^{m+1}+1\) are even, again giving divisibility by \(4\). Therefore \(m\) is odd. Put
\[
U=\frac{3^m-1}{2},\qquad V=\frac{3^{m+1}+1}{2}.
\]
Then \(U,V\) are odd, \(F_3(2m)=2UV\), and \(V-3U=2\); therefore \(\gcd(U,V)=1\). As \(UV=q^b\) and \(V>1\), one has \(U=1\), whence \(m=1\), \(a=2\), and \(q^b=5\). This gives \(n=45\).

**Even integers with two prime supports.** Write \(n=2^a q^b\) with odd prime \(q\) and positive \(a,b\). Since \(F_2(a)\) is odd and coprime to \(2\), while \(F_q(b)\) is even and coprime to \(q\), the divisibility
\[
F_2(a)F_q(b)\mid2^{a+2}q^b
\]
forces \(F_2(a)=q^j\) for some \(1\le j\le b\), and \(F_q(b)\) to be a power of \(2\).

We first prove the local lemma that **for odd \(q\), a power of \(2\) of the form \(F_q(b)\) requires \(b=1\)**. If \(b=2h-1\ge3\), then
\[
F_q(b)=(q+1)S_h,\qquad S_h=1+q^2+\cdots+q^{2(h-1)}.
\]
Because \(q^2\equiv1\pmod8\), splitting the sum when \(h\) is even shows \(\nu_2(S_{2h})=\nu_2(S_h)+1\), while \(S_h\) is odd for odd \(h\). Thus \(\nu_2(S_h)=\nu_2(h)\). Since \(S_h>h\ge2^{\nu_2(h)}\), it is not a power of \(2\). If \(b=2h\) and \(h\) is odd, then \(F_q(b)=[(q^h-1)/(q-1)](q^{h+1}+1)\), where the second factor is \(2\pmod8\) and exceeds \(2\); thus the product is not a power of \(2\). If \(h\) is even, the factor \(q^{h+1}+1\) contains the odd factor \(q^h-q^{h-1}+\cdots-q+1>1\), and the same conclusion follows. This proves the local lemma.

Therefore \(b=1\), so \(F_q(1)=q+1\) is a power of \(2\), and \(F_2(a)=q\). The bounds
\[
2^a<F_2(a)\le2^{a+1}-1
\]
show that the only power of \(2\) in the interval \((2^a+1,2^{a+1}]\) is \(2^{a+1}\). Hence \(q=2^{a+1}-1\) and \(F_2(a)=2^{a+1}-1\). The last equality forces \(a\) to be odd, because for even \(a\) the bi-unitary formula subtracts \(2^{a/2}\). Thus \(a+1\ge2\) is even. Primality of \(2^{a+1}-1\) requires \(a+1\) to be prime (since a composite exponent produces a geometric factorization); therefore \(a+1=2\), giving \(a=1\), \(q=3\), \(n=6\).

Finally \(\sigma^{**}(6)=3\cdot4=12\), \(H_5(6)=2\); \(\sigma^{**}(45)=10\cdot6=60\), \(H_5(45)=3\). All listed integers qualify and no others do.

## Verification
The standalone `verify_h5.py` computes the multiplicative bi-unitary divisor sum by exact integer arithmetic, performs a separate smallest-prime-factor enumeration of all \(n\le10^6\) with \(\omega(n)\le2\), and checks odd-prime exponent obstructions up to exponent \(100\) for twelve odd primes. Run `python3 verify_h5.py`. The output is

`VERIFY_OK limit=1000000 support_hist=[1, 78734, 288726] qualifying=[1, 6, 45] odd_prime_exponent_tests=1188`

The bound is computational only; the proof above establishes the theorem for all positive integers.

## Relationship to prior work
Sándor introduced \(H_5\) in 2011 and proved that its integrality implies bi-unitary harmonicity; he also linked \(H_5\) to the unitary harmonic quotient when all prime exponents are at most \(2\). His remark identifies \(45\) for the restricted form \(p^2q\), but does not classify arbitrary exponents of two primes. Wall's 1983 work considers the **different** unitary harmonic quotient and lists \(6,45\) among its two-support examples. That different condition does not imply the present theorem: \(H_5(270)=3\) is an integer, although the unitary harmonic quotient of \(270\) is \(30/7\). Manea–Minculete (2016) study the usual bi-unitary harmonic quotient for several special factorization patterns, but not the unrestricted \(H_5\) two-prime class. A related published result excludes bi-unitary harmonic numbers of the form \(p^3q^{2^{t+1}}\); it does not cover arbitrary exponents or the \(H_5\) quotient.

## Limitations
This classification concerns \(H_5\) only, not every form of harmonicity, and only integers with at most two distinct prime factors. It does not classify values with three or more prime supports; in fact \(270\) has three supports and integral \(H_5\). Earlier unindexed or inaccessible proofs of the identical classification cannot be excluded solely by literature searches. The finite verifier is corroborative, not an infinite proof.

## References
1. J. Sándor, “On bi-unitary harmonic numbers,” arXiv:1105.0294v1, first posted 2 May 2011. https://arxiv.org/abs/1105.0294
2. C. R. Wall, “Unitary harmonic numbers,” *Fibonacci Quarterly* 21 (1983), 18–25. https://www.fq.math.ca/Scanned/21-1/wall.pdf
3. A. Manea and N. Minculete, “Types of integer harmonic numbers (II),” *Bull. Transilvania Univ. Brașov*, Series III, 9(58) (2016), 67–82. https://webbut.unitbv.ro/index.php/Series_III/article/download/1820/1566/3270
4. OEIS A286325, “Bi-unitary harmonic numbers.” https://oeis.org/A286325
