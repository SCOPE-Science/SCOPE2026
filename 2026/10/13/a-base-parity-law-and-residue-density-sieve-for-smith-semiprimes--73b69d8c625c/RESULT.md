# A base-parity law and residue-density sieve for Smith semiprimes
## Finding
Fix an integer base \(B\ge2\). Let \(s_B(n)\) denote the sum of the base-\(B\) digits of \(n\). A composite integer is a base-\(B\) Smith number when
\[
s_B(n)=\sum_{p^e\parallel n}e\,s_B(p).
\]
Let \(M_B(x)\) count such numbers \(n\le x\) with
\[
\Omega(n)=2.
\]

There is an exact parity dichotomy for odd bases. In base \(3\) there are no Smith semiprimes at all. For every odd base
\[
B\ge5,
\]
the only Smith semiprime is
\[
4=2^2.
\]

For even bases there is a universal residue-density sieve. Put
\[
m=B-1
\]
and, for odd \(m>1\), define
\[
A_m=\{r\pmod m:\gcd(r,m)=\gcd(r-1,m)=1\}.
\]
Set \(|A_1|=1\). If a Smith semiprime is squarefree,
\[
n=pq,
\qquad p<q,
\]
then necessarily
\[
(p-1)(q-1)\equiv1\pmod m.
\]
Consequently its ordered residue pair has the form
\[
\left(r,1+(r-1)^{-1}\right)\pmod m,
\qquad r\in A_m.
\]

Let \(C_B(x)\) count all semiprimes \(n\le x\), with prime factors counted with multiplicity, that satisfy this necessary congruence. Then for every even \(B\),
\[
C_B(x)\sim c_B\frac{x\log\log x}{\log x},
\]
where
\[
c_B=\frac{|A_m|}{\varphi(m)^2}
=\prod_{\ell^a\parallel m}
\frac{\ell-2}{\ell^{a-1}(\ell-1)^2}.
\]
For \(B=2\), the product is empty and \(c_2=1\).

Since the total number \(S_2(x)\) of semiprimes with \(\Omega(n)=2\) satisfies
\[
S_2(x)\sim\frac{x\log\log x}{\log x},
\]
every even-base Smith-semiprime counting function obeys
\[
\limsup_{x\to\infty}\frac{M_B(x)}{S_2(x)}\le c_B.
\]
In decimal,
\[
c_{10}=\frac1{12},
\]
and the only compatible distinct-prime residue pairs modulo \(9\) are
\[
(2,2),\qquad(5,8),\qquad(8,5).
\]

## Assumptions and scope
A semiprime here means an integer with exactly two prime factors counted with multiplicity, so both \(pq\) with distinct primes and prime squares \(p^2\) are included.

The asymptotic constant \(c_B\) measures the density of the universal congruence-compatible superset, not the actual density of Smith semiprimes. The theorem therefore provides an explicit upper-density sieve in even bases, not an asymptotic formula for \(M_B(x)\).

The odd-base statement is exact and includes prime squares. The even-base residue parametrization is stated for distinct primes; prime squares contribute only
\[
O\!\left(\frac{\sqrt x}{\log x}\right)
\]
to \(C_B(x)\), so they do not affect its main term.

## Proof
For every integer \(t\), the base-\(B\) digit sum satisfies
\[
s_B(t)\equiv t\pmod{B-1}.
\]
If \(n=pq\) is a Smith semiprime, with \(p,q\) prime and not necessarily distinct, then
\[
s_B(pq)=s_B(p)+s_B(q).
\]
Reducing modulo
\[
m=B-1
\]
gives
\[
pq\equiv p+q\pmod m,
\]
or equivalently
\[
(p-1)(q-1)\equiv1\pmod m. \tag{1}
\]

Suppose first that \(B\) is odd, so \(m\) is even. If \(p\ne q\), then modulo \(2\) the left side of (1) is \(0\): either both primes are odd, or one is \(2\) and the other is odd. This contradicts (1). If \(p=q\) is odd, the same parity contradiction applies. Hence the only possible prime square is \(p=q=2\), giving \(n=4\). In base \(3\),
\[
s_3(4)=s_3(11_3)=2
\]
while
\[
2s_3(2)=4,
\]
so \(4\) is not Smith. For every odd \(B\ge5\), the integers \(2\) and \(4\) are single base-\(B\) digits, and therefore
\[
s_B(4)=4=2s_B(2).
\]
Thus \(4\) is the unique Smith semiprime in every odd base \(B\ge5\).

Now let \(B\) be even, so \(m\) is odd. Consider distinct primes \(p<q\) satisfying (1). No prime divisor \(\ell\mid m\) can equal \(p\) or \(q\): if, say, \(p=\ell\), then reducing (1) modulo \(\ell\) forces \(q\equiv0\pmod\ell\), hence \(q=\ell\), contrary to distinctness. Thus \(p\) and \(q\) are units modulo \(m\). Equation (1) also shows that both \(p-1\) and \(q-1\) are units modulo \(m\).

Write
\[
r\equiv p\pmod m.
\]
Then \(r\in A_m\), and (1) determines \(q\) uniquely by
\[
q\equiv T(r):=1+(r-1)^{-1}\pmod m. \tag{2}
\]
Conversely, if \(r\in A_m\), then \(T(r)\) is also a unit modulo \(m\), \(T(r)-1\) is a unit, and (2) satisfies (1). Moreover
\[
T(T(r))=r,
\]
so this parametrizes exactly the congruence-compatible ordered residue pairs.

By the Chinese remainder theorem, if
\[
m=\prod_{\ell^a\parallel m}\ell^a,
\]
then the number of residues that are units and are not \(1\) modulo \(\ell\) is
\[
\ell^{a-1}(\ell-2)
\]
for each prime power. Therefore
\[
|A_m|=
\prod_{\ell^a\parallel m}\ell^{a-1}(\ell-2). \tag{3}
\]

It remains to count prime pairs in a fixed compatible residue pair. Fix reduced residues \(r,s\pmod m\), and let \(N_{r,s}(x)\) count products \(pq\le x\) with
\[
p<q,
\qquad p\equiv r\pmod m,
\qquad q\equiv s\pmod m.
\]
Then
\[
N_{r,s}(x)=
\sum_{\substack{p\le\sqrt x\\p\equiv r\, (\mathrm{mod}\,m)}}
\left(
\pi(x/p;m,s)-\pi(p;m,s)
\right). \tag{4}
\]

For fixed \(m\), the prime number theorem in arithmetic progressions and Mertens' theorem for primes in arithmetic progressions imply
\[
N_{r,s}(x)
\sim
\frac{x\log\log x}{\varphi(m)^2\log x}. \tag{5}
\]
For completeness, one can obtain the leading coefficient directly from (4): take
\[
Y=x^{1/\sqrt{\log\log x}}.
\]
For \(p\le Y\), the prime number theorem in arithmetic progressions is uniform over the relevant arguments and gives
\[
\pi(x/p;m,s)
=(1+o(1))\frac{x}{\varphi(m)p\log x}.
\]
Meanwhile
\[
\sum_{\substack{p\le Y\\p\equiv r\, (\mathrm{mod}\,m)}}\frac1p
\sim\frac{\log\log x}{\varphi(m)}.
\]
The range \(Y<p\le\sqrt x\) is
\[
o\!\left(\frac{x\log\log x}{\log x}\right)
\]
by Brun--Titchmarsh and the corresponding reciprocal-prime estimate, while the subtraction term in (4) is
\[
O\!\left(\frac{x}{(\log x)^2}\right).
\]
This proves (5).

There are exactly \(|A_m|\) compatible ordered residue pairs, so summing (5) over them gives
\[
C_B(x)
\sim
\frac{|A_m|}{\varphi(m)^2}
\frac{x\log\log x}{\log x}.
\]
Compatible prime squares contribute only lower order. Combining (3) with
\[
\varphi(m)=
\prod_{\ell^a\parallel m}\ell^{a-1}(\ell-1)
\]
yields the displayed Euler product for \(c_B\).

Finally, Landau's semiprime asymptotic gives
\[
S_2(x)\sim\frac{x\log\log x}{\log x}.
\]
Every Smith semiprime lies in the congruence-compatible set, so the upper-density conclusion follows.

For \(B=10\), one has \(m=9\),
\[
A_9=\{2,5,8\},
\]
and (2) gives precisely
\[
(2,2),(5,8),(8,5).
\]
Thus
\[
c_{10}=\frac{3}{\varphi(9)^2}=\frac{3}{36}=\frac1{12}.
\]

## Verification
The accompanying checker enumerates every semiprime through \(500000\) and verifies the Smith condition directly in bases \(2\) through \(20\). It confirms that base \(3\) has no Smith semiprime in this range and that every tested odd base \(B\ge5\) has only \(4\), exactly as the proof requires.

For every even base through \(40\), the checker independently constructs \(A_{B-1}\), verifies the involution \(T\), verifies the Chinese-remainder product formula for \(|A_{B-1}|\), and checks that every enumerated distinct-prime Smith semiprime lies in one of the predicted residue pairs.

It also reports finite congruence-compatible proportions for several even bases. These approach the constants \(c_B\), but the finite values are not used as evidence for the infinite asymptotic.

## Relationship to prior work
Smith numbers were introduced in the decimal setting and have a substantial construction literature. Witno's complete 2013 paper constructs infinite families of decimal Smith numbers using generalized repunit patterns. Its full text works in decimal representation and contains no occurrence of “semiprime”. A closely related 2014 paper, whose primary classification is \(11A63\), continues the repunit construction program and likewise contains no semiprime result.

The exact decimal semiprime sequence is recorded as OEIS A098837. Later digital-root work gives the decimal necessary pattern: a two-prime Smith number has digital root \(4\), with prime-factor digital roots of type \((2,2)\) or \((5,8)\). This is exactly the decimal specialization of the congruence-compatible pairs above and is treated here as prior coverage, not as a new decimal observation.

OEIS A279314 records the broader congruence
\[
n\equiv\sum p_i\pmod9
\]
for decimal Smith numbers and explicitly notes the analogous modulus \(B-1\) for Smith numbers in base \(B\). Thus the elementary digit-sum congruence itself is also prior coverage.

The new content is the consequence of that congruence on the complete semiprime layer across all bases: the exact odd-base classification, the involutive residue parametrization for even bases, and the explicit prime-pair asymptotic density \(c_B\). The inspected construction papers, exact sequence entries, and digital-root sources do not state that base-parity law or the residue-density theorem.

## Limitations
For even bases, the theorem gives the density of a necessary congruence-compatible superset. It does not prove that Smith semiprimes themselves have density \(c_B\), positive density, or zero density inside the semiprimes.

The full text of the 2024 digital-root article was not openly available in the inspected source. Its later book treatment and longstanding public Smith-number material explicitly state the decimal two-factor digital-root restriction, so no originality claim is made for the decimal residue pattern.

The earliest exact public date verified among the inspected Smith-number sources is 25 March 2013 for Witno's *Journal of Integer Sequences* article. Earlier foundational papers are historically prior but were available here only with year-level bibliographic dates, so no exact calendar day was invented for them.

## References
1. A. Witno, “A Family of Sequences Generating Smith Numbers”, *Journal of Integer Sequences* 16 (2013), Article 13.4.6; published 25 March 2013.
2. A. Witno, “Multiples of repunits as sum of powers of ten”, *Arab Journal of Mathematical Sciences* 20 (2014), 246–249, DOI 10.1016/j.ajmsc.2013.09.001; 2010 MSC \(11A63\).
3. OEIS Foundation, A098837, “Smith semiprimes”.
4. OEIS Foundation, A279314, composite integers satisfying the Smith digit-sum congruence modulo \(9\), with the stated base-\(B\) generalization.
5. S. S. Gupta, “Digital root analysis of Smith numbers”, *The Mathematical Gazette* 108 (2024), 124–130, DOI 10.1017/mag.2024.21.
