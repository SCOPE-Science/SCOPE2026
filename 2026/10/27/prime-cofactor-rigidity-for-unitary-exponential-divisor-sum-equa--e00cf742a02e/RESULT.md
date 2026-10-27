# Prime-cofactor rigidity for unitary–exponential divisor-sum equality on squarefree squares

## Finding
For every squarefree integer \(m\ge2\) and every prime \(q\nmid m\),
\[
\sigma^*(qm^2)=\sigma^{(e)}(qm^2)
\quad\Longleftrightarrow\quad
(m,q)\in\{(2,5),(3,5)\}.
\]
Here \(\sigma^*\) is the sum of unitary divisors and \(\sigma^{(e)}\) is the sum of exponential divisors. In particular, if \(m\) has two or more distinct prime factors, **no choice of a prime cofactor** gives equality. Both one-repeated-prime solutions \(20\) and \(45\) were known; the uniform exclusion for arbitrarily many squared prime factors is the structural contribution.

## Assumptions and scope
A divisor \(d\mid n\) is *unitary* when \(\gcd(d,n/d)=1\). An exponential divisor of \(n=\prod p^{a_p}\) is \(\prod p^{b_p}\) with \(b_p\mid a_p\) and each \(b_p\ge1\). Consequently both divisor sums are multiplicative, with prime-power values
\[
\sigma^*(p^a)=p^a+1,
\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
The theorem quantifies over every squarefree \(m\ge2\) and every prime \(q\) not dividing \(m\). It does not concern a nonsquarefree \(m\), a composite cofactor, or general equality solutions.

## Proof
Write \(m=p_1\cdots p_k\) with distinct primes and \(k\ge1\). Set
\[
U=\prod_{p\mid m}(p^2+1),\qquad
E=\prod_{p\mid m}p(p+1).
\]
Multiplicativity gives
\[
\sigma^*(qm^2)=(q+1)U,
\qquad\sigma^{(e)}(qm^2)=qE.\tag{1}
\]
Every factor \(p(p+1)/(p^2+1)=1+(p-1)/(p^2+1)\) is strictly larger than one.

**One prime factor.** When \(k=1\), write \(m=p\). Equation (1) reduces to
\[
q(p-1)=p^2+1,
\quad\text{so}\quad
q=p+1+\frac{2}{p-1}.
\]
Since \(q\) is an integer, \(p-1\) divides \(2\); hence \(p=2\) or \(p=3\), and in both cases \(q=5\). Both satisfy the original identities, and \(q\ne p\).

**At least two prime factors.** Suppose \(k\ge2\), and equality holds. Divide (1) by \(qU\):
\[
1+\frac1q=\prod_{p\mid m}\left(1+\frac{p-1}{p^2+1}\right).
\]
For *each* prime \(p\mid m\), the remaining product has at least one factor strictly greater than one. It follows that
\[
\frac1q>\frac{p-1}{p^2+1},
\qquad
q<p+1+\frac2{p-1}.\tag{2}
\]
Write \(r\) for the least prime factor of \(m\). There are three cases.

**Case \(r\ge5\).** By (2), \(q<r+2\). As \(r\) is an odd prime, \(r+1\) is not prime, and \(q\ne r\); thus \(q<r\). In particular \(p\nmid(q+1)\) for every \(p\mid m\), since \(q+1<r\le p\). Reduce (1) modulo such a \(p\). Since \(p\mid E\) and \(p\nmid(q+1)\), one has \(p\mid U\). But \(p^2+1\equiv1\pmod p\), so a *different* prime \(t\mid m\) must satisfy \(t^2\equiv-1\pmod p\). Euler's criterion (or the order-four condition) forces \(p\equiv1\pmod4\). This holds for every \(p\mid m\). Therefore each \(p^2+1\) has \(2\)-adic valuation one, as does each \(p(p+1)\). Thus \(\nu_2(U)=\nu_2(E)=k\). Equation (1) now gives \(\nu_2(q+1)=\nu_2(q)\), which is impossible for consecutive integers.

**Case \(r=3\).** Equation (2) yields \(q<5\); since \(q\ne3\), the cofactor must be \(q=2\). All other primes \(p\mid m\) are \(>3\), so \(p\nmid(q+1)=3\). Reducing (1) modulo each such \(p\) again gives \(p\mid U\) and \(p\equiv1\pmod4\). In the product \(U\), the prime \(3\) contributes \(3^2+1=10\) with \(\nu_2=1\); each other prime contributes \(\nu_2=1\). Hence \(\nu_2(U)=k\). In the product \(E\), the prime \(3\) contributes \(3(3+1)=12\) with \(\nu_2=2\); each other prime contributes \(\nu_2=1\). Hence \(\nu_2(E)=k+1\). But (1) would read \(3U=2E\), with unequal valuations \(k\) and \(k+2\), a contradiction.

**Case \(r=2\).** Equation (2) yields \(q<5\); since \(q\ne2\), necessarily \(q=3\). Because \(q\nmid m\), every other \(p\mid m\) is at least \(5\), and \(p\nmid(q+1)=4\). Reduction of (1) modulo \(p\) gives \(p\mid U\), forcing \(p\equiv1\pmod4\). At \(p=2\), the contribution to \(U\) is \(5\) with \(\nu_2=0\), and to \(E\) is \(6\) with \(\nu_2=1\). All remaining prime factors contribute valuation one in each product. Thus \(\nu_2(U)=k-1\) and \(\nu_2(E)=k\). Equation (1) reads \(4U=3E\), with valuations \(k+1\) and \(k\), again a contradiction.

All possibilities for \(k\ge2\) are excluded. Together with the verified \(k=1\) cases, this proves the biconditional. \(\square\)

## Verification
The complete proof is the argument above, which quantifies over arbitrary squarefree \(m\) and arbitrary prime cofactors and contains no computational cutoff. For an independent finite check of the local divisor definitions and the boundary, run the standalone standard-library script with `python verify.py`. It enumerates every squarefree \(m\) from \(2\) to \(300\), and every prime cofactor \(q\le101\) with \(q\nmid m\), by **directly summing the unitary and exponential divisors** rather than using the product equations. It finds exactly \((m,q)=(2,5),(3,5)\) among \(4441\) tested pairs, including \(2855\) pairs with at least two squared prime supports. This finite verification is corroborative, not a proof of the unrestricted claim.

## Relationship to prior work
Trudgian's 2013 preprint, *The sum of the unitary divisor function*, raises the infinitude question for \(\sigma^*(n)=\sigma^{(e)}(n)\) and exhibits the known examples including \(20\), \(45\) and \(6615\). OEIS A236474 tabulates known equality numbers. A published exponent-layer classification covers the distinct **two-prime** family \(p^a q\) for \(2\le a\le49\), and hence already covers the two positive solutions in the present theorem; it does not rule out arbitrarily many squared prime factors. Lelechenko's study of exponential divisors concerns related arithmetic functions and mean behavior, not this uniform exclusion. The new statement isolates an infinite, varying-prime-support family and proves the negative classification at all support sizes beyond one.

## Limitations
The theorem does not classify general integers with exponent patterns other than \(1\) and \(2\). The known equality \(6615=3^3\cdot5\cdot7^2\) shows that an exponent \(3\) allows three-prime-support equality, so the exponent boundary is meaningful. Searches and document comparisons cannot establish global publication priority; unindexed equivalent work and a partially accessible 2014 conference abstract on related equality counts remain residual literature risks. No assertion about the full set of equality integers or its infinitude follows.

## References
- Tim Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, initially posted December 17, 2013; *Publications de l'Institut Mathématique* 97(111) (2015), 175–180. https://arxiv.org/abs/1312.4615
- Andrew V. Lelechenko, *Exponential and infinitary divisors*, arXiv:1405.7597. https://arxiv.org/abs/1405.7597
- OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*. https://oeis.org/A236474
- *The first 49 exponent layers of the unitary–exponential divisor-sum equality*, published mathematical result (2026), RESULT.md. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-first-49-exponent-layers-of-the-unitary-exponential-divisor--59314f8e910e
