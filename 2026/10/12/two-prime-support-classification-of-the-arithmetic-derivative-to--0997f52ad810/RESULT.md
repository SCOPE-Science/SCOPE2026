# Two-prime-support classification of the arithmetic-derivative/totient equation

## Finding

Let \(D\) denote the arithmetic derivative, characterized by \(D(p)=1\) on primes and the Leibniz rule, and let \(\varphi\) be Euler's totient. For every integer \(n\ge2\) with \(\omega(n)\le2\),
\[
D(n)=\varphi(n)
\]
holds if and only if one of the following mutually exclusive alternatives occurs.

1. There is a prime \(p\) with
\[
n=p^{p-1}.
\]

2. There are odd primes \(p<q\) such that \(q\not\equiv1\pmod p\). If \(u\in\{2,\ldots,p-1\}\) is the unique integer satisfying
\[
uq\equiv1\pmod p,
\]
then
\[
n=p^a q^b,\qquad a=u-1,\qquad b=q-1-\frac{uq-1}p.
\]

Consequently, every admissible exact two-prime support \(\{p,q\}\) contains exactly one solution, while no support containing \(2\) contains a solution. The unique squarefree semiprime solution is
\[
15=3\cdot5.
\]
For each fixed odd prime \(p\), the prime number theorem in arithmetic progressions also gives
\[
\#\{q\le Q:q>p,\ q\text{ prime},\ q\not\equiv1\pmod p\}\sim\frac{p-2}{p-1}\operatorname{Li}(Q).
\]

## Assumptions and scope

Here \(\omega(n)\) is the number of distinct prime divisors. The theorem is an unbounded classification on the complete stratum \(\omega(n)\le2\); there is no upper bound on the primes or exponents. The asymptotic statement fixes \(p\) and lets \(Q\to\infty\).

For
\[
n=\prod_i p_i^{e_i},
\]
the standard exact formula for the arithmetic derivative is
\[
\frac{D(n)}n=\sum_i\frac{e_i}{p_i}.
\]

## Proof

For a prime power \(n=p^a\), the equality becomes
\[
\frac ap=\frac{p-1}p,
\]
so \(a=p-1\). This proves the first branch in both directions.

Now suppose \(n=p^a q^b\) with distinct primes \(p<q\) and \(a,b\ge1\). Dividing the equality by \(n\) gives
\[
\frac ap+\frac bq=\frac{(p-1)(q-1)}{pq},
\]
or equivalently
\[
aq+bp=(p-1)(q-1).
\]
Set \(A=a+1\) and \(B=b+1\). Then
\[
Aq+Bp=pq+1. \tag{1}
\]

If \(p=2\), equation (1) forces \(Aq\) to be odd, hence \(A\) is odd. Since \(A\ge2\), we have \(A\ge3\), and therefore \(Aq>2q+1\), contradicting (1). Thus every two-prime solution has odd \(p\) and \(q\).

Assume now that \(p\) is odd. Since \(B\ge2\), equation (1) yields
\[
Aq\le pq+1-2p<pq,
\]
so \(2\le A\le p-1\). Reducing (1) modulo \(p\) gives
\[
Aq\equiv1\pmod p.
\]
Hence \(q\not\equiv1\pmod p\), because the inverse residue \(A\) cannot be \(1\). Moreover, \(A\) is uniquely determined: it is the unique \(u\in\{2,\ldots,p-1\}\) satisfying \(uq\equiv1\pmod p\). Equation (1) then gives
\[
B=q-\frac{uq-1}p,
\]
and consequently
\[
a=u-1,\qquad b=q-1-\frac{uq-1}p.
\]

Conversely, suppose \(p<q\) are odd primes with \(q\not\equiv1\pmod p\), and choose \(u\) as above. Put
\[
k=\frac{uq-1}p.
\]
Because \(2\le u\le p-1\), one has \(1\le k<q\). If \(q-k=1\), then \(uq-1=p(q-1)\), so
\[
q(p-u)=p-1,
\]
which is impossible because \(q>p-1\) and \(p-u\ge1\). Thus \(B=q-k\ge2\), so both exponents \(a=u-1\) and \(b=B-1\) are positive. The definitions give (1), hence \(D(p^a q^b)=\varphi(p^a q^b)\). Uniqueness follows because \(u\) is the unique inverse residue in the permitted interval and then \(B\) is forced by (1).

For the squarefree subcase \(a=b=1\), the equation reduces to
\[
p+q=(p-1)(q-1),
\]
which is equivalent to
\[
(p-2)(q-2)=3.
\]
With primes \(p<q\), this forces \(p=3\), \(q=5\), hence \(n=15\).

Finally, for fixed odd \(p\), the only excluded nonzero residue class for \(q\bmod p\) is \(1\). The prime number theorem in arithmetic progressions gives equal asymptotic prime mass \(1/(p-1)\) to every nonzero residue class, proving the stated density.

## Verification

The bundled `verify.py` checks the classification independently on finite data. It verifies the prime-power formula for small primes, exhaustively compares the modular-inverse formula with direct positive-exponent solutions for all prime supports in a finite prime box, and confirms the initial numerical solutions. These computations are regression checks only; the proof above is the unbounded argument.

Representative solutions are
\[
2,\ 9,\ 15,\ 625,\ 1225,\ 3993,\ 117649.
\]
For example, the support \(\{5,7\}\) has inverse \(u=3\), giving \(a=b=2\) and \(n=1225\), while the support \(\{3,11\}\) gives \(a=1\), \(b=3\), and \(n=3993\).

## Relationship to prior work

Ufnarovski and Åhlander give the prime-factor formula for the arithmetic derivative and study several arithmetic differential equations, including \(D(n)=n\), but the inspected full text does not give the equation \(D(n)=\varphi(n)\) or a two-prime-support classification. Emmons and Xiao develop arithmetic derivatives and partial derivatives over broader local and global settings; their paper supplies the focal modern arithmetic-derivative context and likewise does not state this coincidence classification.

Published-finding searches for the exact equation, semiprime and two-prime-support variants, modular-inverse parametrizations, and neighboring arithmetic-derivative/totient equations found no statement implying the theorem. The nearest records concern a different gap \(D(n)-(n-\varphi(n))\), fixed-multiplier equations \(D(n)=kn\), and iterates of \(D\); none determines the present supports or exponents.

## Limitations

The theorem treats only \(\omega(n)\le2\). It makes no claim about solutions with three or more distinct prime factors. The density statement concerns admissible prime supports for fixed \(p\), not the counting function of the resulting integers \(p^a q^b\) by size. Novelty searches cannot rule out an obscure or unindexed equivalent observation.

## References

1. B. Emmons and X. Xiao, “A generalization of arithmetic derivative to \(p\)-adic fields and number fields,” *Notes on Number Theory and Discrete Mathematics* 30 (2024), 357–382. arXiv:2307.04912; DOI:10.7546/nntdm.2024.30.2.357-382.
2. V. Ufnarovski and B. Åhlander, “How to Differentiate a Number,” *Journal of Integer Sequences* 6 (2003), Article 03.3.4.
