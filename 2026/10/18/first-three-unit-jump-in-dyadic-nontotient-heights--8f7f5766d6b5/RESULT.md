# First three-unit jump in dyadic Nontotient heights

## Finding

Let \(\varphi(n)\) be Euler's totient, \(g(n)=n-\varphi(n)\) for integers \(n\ge2\), and \(C(1)=0\), \(C(n)=1+C(g(n))\) for \(n\ge2\). Write
\[
M_k=\max_{2^{k-1}<n\le2^k} C(n),\qquad k\ge1.
\]
The **first index** \(k\ge2\) for which \(M_k-M_{k-1}\ge3\) is exactly \(k=19\). More precisely,
\[
M_{18}=30,\qquad M_{19}=33,
\]
and exactly one integer in \((2^{18},2^{19}]\) attains \(M_{19}\), namely \(n=462210\). For every \(2\le k\le18\), \(M_k-M_{k-1}\in\{1,2\}\). These claims are exact finite statements, not conjectures about larger intervals.

## Assumptions and scope

The domain consists of positive integers and all \(19\) dyadic intervals \((2^{k-1},2^k]\) for \(1\le k\le19\). The function \(g\) strictly decreases positive integers greater than one because \(1\le\varphi(n)<n\) when \(n\ge2\), so \(C\) is well defined. The statistic is a stopping-time maximum, not the Sprague–Grundy parity value. No assertion about \(M_k\) for \(k\ge20\) is made.

## Proof

The proof is an **exhaustive finite certificate**, with two separately implemented algorithms for Euler's totient and a recurrence verifying all integers through \(2^{19}=524288\). Its finite nature is essential: no sampled extrapolation is used.

**Totient algorithm A.** Initialize \(\varphi_A(n)=n\) for \(0\le n\le524288\). For every \(p\ge2\), if the current value at \(p\) is \(p\), then \(p\) is prime, and for every positive multiple \(m\) of \(p\) update \(\varphi_A(m)\gets\varphi_A(m)-\varphi_A(m)/p\). At the moment \(p\) is reached, all primes below \(p\) have already been processed, proving the primality test. Each distinct prime factor contributes exactly the multiplicative factor \((1-1/p)\). Thus this constructs the true totient for every \(n\) in the finite domain.

**Totient algorithm B.** Independently determine the smallest prime factor \(p\) of each composite integer by marking multiples from \(p^2\) in increasing prime order. For \(n\ge2\), put \(m=n/p\) and define
\[
\varphi_B(n)=
\begin{cases}
 p\varphi_B(m),&p\mid m,\\
 (p-1)\varphi_B(m),&p\nmid m.
\end{cases}
\]
Initialize \(\varphi_B(1)=1\). The prime-power totient formula and multiplicativity prove this recurrence. The two totient arrays were compared term by term.

**Height recurrence and exhaustive coverage.** With \(C(1)=0\), compute \(C(n)=1+C(n-\varphi(n))\) in increasing integer order. Since \(n-\varphi(n)\) is always between \(1\) and \(n-1\) for \(n\ge2\), every right-hand-side value is already established. Both totient implementations were used independently to construct and compare the full height arrays. Thus every \(C(n)\), not just a sample, was established for \(1\le n\le524288\).

Taking the maximum in each exactly enumerated dyadic interval gives the following certificate, where the last two columns record the number of maximizers and their least value:

| \(k\) | \(M_k\) | Maximizer count | Least maximizer |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 2 |
| 2 | 2 | 1 | 4 |
| 3 | 3 | 2 | 6 |
| 4 | 4 | 4 | 10 |
| 5 | 6 | 1 | 30 |
| 6 | 7 | 5 | 42 |
| 7 | 9 | 2 | 114 |
| 8 | 10 | 9 | 186 |
| 9 | 12 | 4 | 390 |
| 10 | 14 | 2 | 798 |
| 11 | 16 | 2 | 1950 |
| 12 | 18 | 1 | 4074 |
| 13 | 20 | 2 | 7770 |
| 14 | 22 | 3 | 15810 |
| 15 | 24 | 6 | 30702 |
| 16 | 26 | 15 | 53130 |
| 17 | 28 | 18 | 105090 |
| 18 | 30 | 44 | 206910 |
| 19 | 33 | 1 | 462210 |

The table proves \(M_{19}-M_{18}=3\), all earlier jumps are at most two, and there is exactly one maximizer at \(k=19\). The explicit orbit of the unique maximizer is

`462210, 361410, 278850, 216450, 164610, 122850, 96930, 71154, 48186, 32130, 25218, 16830, 12990, 9534, 6822, 4554, 3234, 2394, 1746, 1170, 882, 630, 486, 324, 216, 144, 96, 64, 32, 16, 8, 4, 2, 1`.

It has \(33\) transitions and independently witnesses \(C(462210)=33\).

## Verification

Run `python3 verify.py` with Python 3 and only its standard library. The script builds both complete totient arrays, checks their equality, independently computes and compares all heights, reproduces the whole \(19\)-interval table, asserts no earlier three-unit jump, checks the unique maximizer by another direct traversal, and verifies the full orbit. Successful completion prints `VERIFIED`. The code needs at most a few megabytes of numeric-array storage and terminates after finitely many simple loops; mathematical validity of the finite certificate follows from the recurrences proved above.

## Relationship to prior work

Ellis, Shi, Thanatipanonda, and Tu introduce the Nontotient iteration height \(C(n)\). Their Theorem 4.8 proves that the heights attained by even integers in each dyadic interval form a consecutive integer interval, without determining the maximal height \(M_k\) or the first occurrence of a jump by at least three. Their Lemma 4.4 is a structural identity for heights under doubling and their Lemma 4.6 a lower bound; neither gives the table or first-jump classification. The exact finite extremal computation here complements, rather than reproduces, those statements. The result may conceivably be subsumed by an unlocated general stopping-time census; no independent priority claim is made.

## Limitations

This is an exact finite first-crossing and unique-witness certificate, **not** an asymptotic theorem and not a proof of an eventual pattern. No assertion is made about the next jump, growth bounds beyond \(k=19\), or any generalized arithmetic iteration. Exhaustiveness relies on faithfully executing the included finite verifier and the standard arithmetic proofs of its two totient constructions. The motivating paper's parity-valued game outcomes are distinct from the heights analyzed here.

## References

P. Ellis, J. Shi, T. A. Thanatipanonda, A. Tu, *Two Games on Arithmetic Functions: SALIQUANT and NONTOTIENT*, 2023, arXiv:2309.01231, especially Section 4, Lemmas 4.4 and 4.6, and Theorem 4.8. https://arxiv.org/pdf/2309.01231. Published in *Discrete Mathematics Letters* 12 (2023), 209–216, DOI:10.47443/dml.2023.154.
