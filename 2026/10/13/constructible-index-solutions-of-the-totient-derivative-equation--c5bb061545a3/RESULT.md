# Constructible-index solutions of the totient-derivative equation

## Finding
Let \(\varphi\) denote Euler's totient function and let \(D\) be the arithmetic derivative, characterized by \(D(1)=0\), \(D(p)=1\) for every prime \(p\), and \(D(uv)=uD(v)+vD(u)\). For **every positive integer** \(n\) whose totient \(\varphi(n)\) is a power of \(2\), including \(2^0=1\),
\[
D(\varphi(n))=n\quad\Longleftrightarrow\quad n\in\{32,80,192\}.
\]
The corresponding totients are \(\varphi(32)=16\), \(\varphi(80)=32\), and \(\varphi(192)=64\). For \(n\ge3\), the classical Gauss--Wantzel criterion identifies power-of-two totients exactly with straightedge-and-compass constructibility of a regular \(n\)-gon; hence these are exactly the constructible polygon indices that satisfy the stated arithmetic-derivative equation.

## Assumptions and scope
All integers \(n\) are positive. A power of \(2\) means \(2^e\) for an integer \(e\ge0\). The theorem does **not** classify all positive integers satisfying \(D(\varphi(n))=n\). It uses no assumption about whether further Fermat primes exist. The proof is unconditional and covers arbitrarily large \(n\) and arbitrarily large exponents.

## Proof
If \(\varphi(n)=1\), then \(n\in\{1,2\}\) and \(D(\varphi(n))=D(1)=0\ne n\). Thus suppose \(\varphi(n)=2^e\) with \(e\ge1\). The Leibniz rule gives
\[
D(2^e)=e2^{e-1},\qquad
D(\varphi(n))=n\ \Longrightarrow\ e=\frac{2n}{\varphi(n)}.
\tag{1}
\]

Every odd prime divisor \(p\) of \(n\) must occur to exponent one: if \(p^b\Vert n\) with \(b\ge2\), the odd factor \(p\) divides \(\varphi(n)\), contrary to its being a power of \(2\). Moreover \(p-1\) must be a power of \(2\), say \(p-1=2^t\). Since \(p=2^t+1\) is prime, \(t\) itself must be a power of \(2\): otherwise write \(t=uv\) with odd \(v>1\), so \(2^u+1\) is a nontrivial divisor of \(2^{uv}+1\). Thus each odd prime factor is a Fermat prime \(p_j=2^{2^j}+1\), \(j\ge0\).

Consequently \(n=2^a\prod_{j\in J}(2^{2^j}+1)\) for an integer \(a\ge0\) and a finite set \(J\) of distinct nonnegative indices whose Fermat numbers are prime. Put
\[
T=\sum_{j\in J}2^j,\qquad P=\prod_{j\in J}(2^{2^j}+1).
\]
Here \(P\) is odd and \(T\ge0\). When \(a=0\), we have \(n=P\), \(\varphi(n)=2^T\), and equation (1) becomes \(T=2^{1-T}P\). Since \(T\) is an integer and \(P\) is odd, \(T\le1\). The case \(T=0\) gives \(n=1\), previously excluded. The only possibility \(T=1\) is \(P=3\), giving \(1=3\), a contradiction. Hence every solution is even.

For \(a\ge1\), multiplicativity gives
\[
\varphi(n)=2^{a-1+T},\qquad e=a-1+T,\qquad
\frac{2n}{\varphi(n)}=2^{2-T}P.
\]
As \(e\) is an integer and \(P\) is odd, (1) forces \(T\le2\). Because \(T\) is a sum of **distinct** powers \(2^j\), there are just three possibilities:

- \(T=0\): \(J=\varnothing\), \(P=1\), and \(a-1=4\), yielding \(n=2^5=32\).
- \(T=1\): \(J=\{0\}\), \(P=3\), and \(a=6\), yielding \(n=2^6\cdot3=192\).
- \(T=2\): \(J=\{1\}\), \(P=5\), and \(a+1=5\), yielding \(n=2^4\cdot5=80\).

These candidates all satisfy the original equality, not merely its necessary condition:
\[
D(\varphi(32))=D(16)=4\cdot8=32,\quad
D(\varphi(80))=D(32)=5\cdot16=80,\quad
D(\varphi(192))=D(64)=6\cdot32=192.
\]
This proves the equivalence for every positive integer in the stated domain. In particular, no unknown Fermat prime of index \(j\ge2\) can yield an additional solution.

## Verification
The accompanying standalone `verify_totient_dyadic.py` uses exact integer totient and smallest-prime-factor sieves to check every \(1\le n\le10^6\) with \(\varphi(n)\) a power of \(2\). The command `python verify_totient_dyadic.py` produced:

`VERIFY_OK limit=1000000 prime_power_totient_candidates=208 solutions=[32, 80, 192] near_exceptions=[31,81,112,176,244]`

The finite computation checks the first million inputs only; the unrestricted theorem follows from the proof above, not from this bound. The five near-exceptions satisfy \(D(\varphi(n))=n\) but have totients with an odd prime factor, confirming the importance of the stated domain.

## Relationship to prior work
OEIS A248815, first authored October 15, 2014, records the unrestricted equation \(n=D(\varphi(n))\) and explicitly lists \(32,80,192\), alongside nonconstructible indices. Its entry and finite table do not assert completeness of the intersection with dyadic-totient integers. The standard prime-factor characterization of dyadic totients (in terms of distinct Fermat primes) is classical; the result here is the **complete intersection**, obtained by the integral-exponent obstruction \(T\le2\). Kovič (2012) treats arithmetic derivatives and antiderivatives more broadly, not this restricted composite equation in the inspected material. No indexed equivalence or stronger result was located in the named searches; that absence is not a proof of novelty.

## Limitations
No statement is made about \(D(\varphi(n))=n\) when \(\varphi(n)\) has an odd prime factor, nor about the distribution of solutions to that unrestricted equation. The proof uses the established classification of the odd prime divisors of numbers with power-of-two totient, and proves the needed factorization argument directly. Unindexed previous elementary observations could overlap the restricted classification; independent scholarly assessment has not been performed.

## References
1. OEIS Foundation, **A248815**, *Numbers equal to the arithmetic derivative of their Euler totient function*, original entry Paolo P. Lava, October 15, 2014. https://oeis.org/A248815
2. Jurij Kovič, *The Arithmetic Derivative and Antiderivative*, Journal of Integer Sequences **15** (2012), Article 12.3.8. https://cs.uwaterloo.ca/journals/JIS/VOL15/Kovic/kovic4.pdf
3. Classical Fermat-prime factorization and Gauss--Wantzel constructibility criterion, with an accessible exposition of the factorization at https://www.physicsforums.com/threads/proof-about-itex-phi-n-itex-being-a-power-of-2.691973/ (May 15, 2013). The factorization required here is reproved above.
