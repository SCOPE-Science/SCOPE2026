# Prime squarefree kernels of factorials
## Finding
For every integer \(c\ge 1\), let \(s(c!)\) denote the squarefree kernel of \(c!\): the unique squarefree integer such that \(c!/s(c!)\) is a square. Then \(s(c!)\) is prime exactly for
\[
c\in\{2,6,10\},
\]
with corresponding values \(2,5,7\). Equivalently, the prime elements of the set \(\mathcal{S}=\{s(c!):c\ge1\}\) are exactly \(\{2,5,7\}\).

## Assumptions and scope
The statement is over positive integers \(c\). Primality has its usual meaning, so \(1\) is not prime. The notation \(s(v)\) agrees with the squarefree-part convention used in the motivating work: if \(v=a b^2\) with \(a\) squarefree, then \(s(v)=a\).

## Proof
If a prime \(q\) lies in \((c/2,c]\) and \(c\ge5\), then Legendre's formula gives \(v_q(c!)=1\): there is exactly one multiple of \(q\) among \(1,\ldots,c\), and \(q^2>c\). Hence every prime in \((c/2,c]\) divides \(s(c!)\).

For \(11\le c\le50\), direct prime enumeration shows that \((c/2,c]\) contains at least two primes. For \(c\ge51\), apply Nagura's theorem, which states that for every real \(x\ge25\) there is a prime strictly between \(x\) and \(6x/5\). With \(x=c/2\), obtain a prime
\[
q_1\in(c/2,3c/5).
\]
With \(x=5c/6\), obtain a second prime
\[
q_2\in(5c/6,c).
\]
The two intervals are disjoint. Thus for every \(c\ge11\), at least two distinct primes divide \(s(c!)\), so \(s(c!)\) cannot be prime.

It remains to inspect \(1\le c\le10\). Exact valuation parity gives
\[
\bigl(s(1!),s(2!),\ldots,s(10!)\bigr)
=(1,2,6,6,30,5,35,70,70,7).
\]
The prime entries occur exactly at \(c=2,6,10\), completing the proof.

## Verification
The accompanying `verify.py` independently computes prime exponents in factorials, reconstructs \(s(c!)\) for \(1\le c\le50\), checks the ten displayed initial values, checks that the only prime kernels in this finite range occur at \(2,6,10\), and verifies that every integer \(11\le c\le50\) has at least two primes in \((c/2,c]\). The infinite tail uses Nagura's published prime-interval theorem, not finite computation.

## Relationship to prior work
Yudin's 2026 preprint makes \(\mathcal{S}=\{s(c!):c\ge1\}\) a central parameter set for the main term in the three-factorial square-product problem, and notes that every prime in \((c/2,c]\) divides \(s(c!)\). The result here determines the entire prime stratum of that parameter set.

OEIS A055204 tabulates \(s(c!)\), and OEIS A055460 tabulates the number of prime divisors of \(s(c!)\); their published finite tables display the three small prime cases but do not state an all-\(c\) classification. Broughan proves the asymptotic estimate \(\log s(c!)=(\log 2)c+O(\sqrt c)\), which implies eventual growth but does not identify the exact exceptional indices. Jakimczuk studies more general power-free parts asymptotically. The present classification instead combines a short finite boundary check with Nagura's explicit prime-gap theorem.

## Limitations
This result classifies only the one-prime-support layer of \(\mathcal{S}\). It does not classify kernels having exactly two or more prime factors, nor does it sharpen the asymptotic order of \(s(c!)\). The finite verification is supplementary; the proof of the infinite tail depends on Nagura's theorem.

## References
1. F. Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899v1, 2026. https://arxiv.org/abs/2610.01899
2. OEIS Foundation, A055204, *Squarefree part of n!: n! divided by its largest square divisor*. https://oeis.org/A055204
3. OEIS Foundation, A055460, *Number of primes with odd exponents in the prime power factorization of n!*. https://oeis.org/A055460
4. K. A. Broughan, *Asymptotic Order of the Square-free Part of N!*, Integers 2 (2002), Paper A10.
5. R. Jakimczuk, *On the h-th free part of the factorial*, International Mathematical Forum 12 (2017), 629--634. https://doi.org/10.12988/imf.2017.7542
6. J. Nagura, *On The Interval Containing At Least One Prime Number*, Proceedings of the Japan Academy 28 (1952), 177--181. https://doi.org/10.3792/pja/1195570997
