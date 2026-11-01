# A uniform dyadic valuation law for recursive divisor counts with one repeated prime

## Finding

Let \(\kappa_0(1)=1\), and for each integer \(n\ge2\) define
\[\kappa_0(n)=1+\sum_{d\mid n,\ d<n}\kappa_0(d).\]
For every integer \(r\ge1\), every \(k\ge0\), and pairwise distinct primes \(p,q_1,\ldots,q_k\), set \(N=p^r\prod_{i=1}^kq_i\). Then
\[
\nu_2(\kappa_0(N))=
\begin{cases}
r,&k=0,\
r+\nu_2(r+2),&k=1,\
r,&k\ge2\text{ and }r\text{ odd},\
r+1,&k\ge2\text{ and }r\text{ even}.
\end{cases}
\]
In particular, after two distinct squarefree cofactor primes have been added, further primes do not change the valuation. At one cofactor prime, even \(r\) can exhibit arbitrarily large additional valuation: take \(r=2^h-2\) for \(h\ge2\).

## Assumptions and scope

All primes are positive rational primes and pairwise distinct. Valuations apply to positive integers. The empty product for \(k=0\) is one. The result concerns exactly the exponent vectors with at most one prime whose exponent can exceed one; it makes no claim about exponent vectors with two repeated primes.

## Proof

The recursive identity implies the formal Dirichlet-series identity
\[\sum_{n\ge1}\frac{\kappa_0(n)}{n^s}=\frac{\zeta(s)}{2-\zeta(s)}.\]
This identity is interpreted coefficientwise, so it does not require analytic convergence. Replace the Euler factor of \(p\) by \((1-x)^{-1}\), and those of the \(k\) other *labelled* distinct primes by \(\prod_{i=1}^k(1-y_i)^{-1}\). Extracting coefficients linear in each \(y_i\) is equivalent to taking the \(k\)-th exponential coefficient after substituting \(y_i\) collectively by an exponential variable \(t\):
\[
G_r(t)=\sum_{k\ge0}\kappa_0(p^r q_1\cdots q_k)\frac{t^k}{k!}
=[x^r]\frac{e^t}{2(1-x)-e^t}
=\frac{2^r e^t}{(2-e^t)^{r+1}}.
\]
Here the notation in the left sum denotes the common value determined by the exponent vector, independent of which distinct primes are chosen. The derivation is a labelled-variable coefficient extraction: the coefficient of \(y_1\cdots y_k\) in a series depending only on \(\prod_i(1-y_i)^{-1}\) agrees with \(k![t^k]\) under the substitution of that product by \(e^t\).

Set \(u=e^t-1\). Then
\[2^{-r}G_r(t)=(1+u)(1-u)^{-r-1}=1+\sum_{j\ge1}c_{r,j}u^j,\]
where \(c_{r,j}=\binom{r+j}{j}+\binom{r+j-1}{j-1}\). The first coefficients are
\[c_{r,1}=r+2,\qquad 2!c_{r,2}=(r+1)(r+4),\qquad3!c_{r,3}=(r+1)(r+2)(r+6).\]
Writing \(S(k,j)\) for the Stirling number of the second kind, the identity is \(k![t^k](e^t-1)^j=j!S(k,j)\),
\[
2^{-r}\kappa_0(N)=\sum_{j=0}^k c_{r,j}j!S(k,j).
\]
For \(k=0\) this sum is one. For \(k=1\) it is \(r+2\). If \(k\ge2\) and \(r\) is odd, the \(j=1\) summand \(r+2\) is odd and every \(j\ge2\) summand is even, giving valuation \(r\).

Finally suppose \(k\ge2\) and \(r\) even. Terms with \(j\ge4\) are multiples of four because \(4!\mid j!\). The \(j=3\) summand is also a multiple of four, since \((r+2)(r+6)\) is divisible by four. Because \(S(k,2)=2^{k-1}-1\) is odd, reduction modulo four gives
\[
2^{-r}\kappa_0(N)\equiv(r+2)+(r+1)(r+4)(2^{k-1}-1)\equiv2\pmod4.
\]
For \(r\equiv0\pmod4\), the first term is 2 and the second is 0; for \(r\equiv2\pmod4\), the first is 0 and the second is 2. Thus the valuation is exactly \(r+1\), proving every case.

## Verification

A standalone Python verifier computes \(\kappa_0\) independently from its original proper-divisor recurrence on prime-exponent vectors, compares it with the exact Stirling expansion, and checks the stated valuations for each \(1\le r\le12\) and \(0\le k\le6\) (84 configurations). Execute `python3 verify.py` from the directory containing that file; it uses only the Python standard library and reports `VERIFY_OK` on success. These finite tests are corroboration; the coefficientwise argument proves the unrestricted result.

## Relationship to prior work

Fink introduced the recursive divisor count and studied its Dirichlet series and convolution identities. In *Properties of the recursive divisor function and the number of ordered factorizations* (2023), Theorem 1 establishes the Dirichlet series used above, and Theorems 2–3 express associated multiplicative convolutions. The 2023 companion paper *Number of ordered factorizations and recursive divisors* describes general closed-form expressions for these counts. The exact stability of their \(2\)-adic valuations across arbitrary numbers of distinct cofactor primes, including the exceptional one-prime transition, is not stated in the inspected 2023 primary full text. The latter companion paper could not be compared beyond available bibliographic text, a priority risk.

## Limitations

The theorem treats only prime-exponent vectors \((r,1,\ldots,1)\). It does not evaluate valuations for integers with two or more repeated-prime exponents or odd-prime-adic valuations. The published Dirichlet generating function is prior work; the contribution claimed here is its uniform sharp valuation classification for this natural infinite family, not the generating function itself. Independent scientific assessment remains outstanding.

## References

1. T. M. A. Fink, *Properties of the recursive divisor function and the number of ordered factorizations*, arXiv:2307.09140, first posted 2023-07-18. https://arxiv.org/abs/2307.09140
2. T. M. A. Fink, *Number of ordered factorizations and recursive divisors*, arXiv:2307.16691, first posted 2023-07-31. https://arxiv.org/abs/2307.16691
