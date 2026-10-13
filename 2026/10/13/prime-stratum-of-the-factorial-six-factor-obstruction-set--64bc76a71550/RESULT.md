# Prime stratum of the factorial six-factor obstruction set
## Finding
Let \(s(m)\) be the squarefree part of a positive integer \(m\), meaning the product of the primes that occur to odd exponent in \(m\); put \(s(0!)=1\). Then
\[
s(c!)>c^2\qquad(c\ge12).
\]
For the set
\[
\mathcal R=\{a\ge1:\ a\text{ is squarefree and }s(a c!)\ge a\text{ for every integer }c\ge0\},
\]
which is used in the recent six-factor factorial-square construction, the prime elements are exactly
\[
\mathcal R\cap\mathbb P=\{p\in\mathbb P:p\ge13\}.
\]
The eventual quadratic threshold starts sharply at \(12\): \(s(11!)=77<121\), whereas \(s(12!)=231>144\).

## Assumptions and scope
All factorials are over nonnegative integers, with \(0!=1\). The classification concerns prime values of the squarefree parameter \(a\) in \(\mathcal R\); it does not classify composite elements of \(\mathcal R\). The prime-distribution input is Nagura's theorem that every real \(x\ge25\) has a prime in \([x,6x/5)\).

## Proof
First prove the quadratic tail. For \(12\le c\le49\), exact factorization of \(c!\) gives \(s(c!)>c^2\); the complete finite check is reproduced by `verify_prime_R.py`. In particular the endpoint values are \(s(11!)=77\) and \(s(12!)=231\).

Now let \(c\ge50\). Apply Nagura's theorem with \(x=(c+1)/2\), \(x=2c/3\), and \(x=5c/6\). This produces distinct primes
\[
q_1\in[(c+1)/2,3(c+1)/5),\qquad q_2\in[2c/3,4c/5),\qquad q_3\in[5c/6,c).
\]
The three intervals are disjoint because \(3(c+1)/5<2c/3\) for \(c\ge50\), and each \(q_i\) satisfies \(c/2<q_i\le c\), so \(v_{q_i}(c!)=1\). Hence all three divide \(s(c!)\), and therefore
\[
s(c!)\ge q_1q_2q_3\ge \frac{c+1}2\frac{2c}3\frac{5c}6>\frac5{18}c^3>c^2.
\]
This proves the tail bound for every \(c\ge12\).

Let \(p\ge13\) be prime and fix \(c\ge0\). If \(p\nmid s(c!)\), then squarefree parity gives \(s(pc!)=p\,s(c!)\ge p\). If \(p\mid s(c!)\), then necessarily \(c\ge p\ge13\), and toggling the odd \(p\)-valuation gives
\[
s(pc!)=\frac{s(c!)}p>\frac{c^2}p\ge p.
\]
Thus \(p\in\mathcal R\).

For the remaining primes, explicit witnesses violate the defining inequality: \(c=2\) for \(p=2\), \(c=3\) for \(p=3\), \(c=6\) for \(p=5\), \(c=7\) for \(p=7\), and \(c=11\) for \(p=11\). The corresponding values \(s(pc!)\) are respectively \(1,2,1,5,7\), each strictly below \(p\). Hence no prime below \(13\) belongs to \(\mathcal R\).

## Verification
`verify_prime_R.py` uses exact integer arithmetic. It factors every \(c!\) for \(12\le c\le49\), checks all five small-prime witnesses, verifies the endpoint values at \(11\) and \(12\), and stress-tests the prime classification for every prime \(p\le401\) and every \(0\le c\le500\). Its replay line is

`VERIFY_OK finite_tail=38 small_prime_witnesses=5 prime_stress=79 c_max=500 threshold_11_12=77,231`

The finite stress test is supplementary; the infinite statement follows from the proof above and Nagura's theorem.

## Relationship to prior work
Yudin's arXiv:2610.01899v1 defines the set \(\mathcal R\), proves that it has positive lower density, and uses subsets of it in the six-factor factorial-square construction. The paper does not classify the prime stratum of \(\mathcal R\). Broughan proved the asymptotic estimate \(\log s(n!)=n\log2+O(\sqrt n)\), which implies rapid growth but does not supply the exact all-\(n\) threshold \(s(c!)>c^2\) from \(c=12\) onward. OEIS A055204 tabulates the squarefree parts of factorials and is consistent with the finite boundary values but does not state the prime classification of \(\mathcal R\).

A previously recorded result classifies when \(s(c!)\) itself is prime. That statement is logically different: knowing that \(s(c!)\) has at least two prime divisors does not imply the quadratic lower bound required to decide whether a prime parameter lies in \(\mathcal R\).

## Limitations
The result does not determine the composite elements of \(\mathcal R\), their density, or finer distribution inside the squarefree integers. The proof uses the published Nagura prime-interval theorem rather than reproving it. The exact computation is needed only for \(12\le c\le49\); it is not evidence for the infinite tail.

## References
1. F. Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899v1, 2026.
2. K. A. Broughan, *Asymptotic Order of the Square-free Part of N!*, Integers 2 (2002), Article A10.
3. J. Nagura, *On The Interval Containing At Least One Prime Number*, Proceedings of the Japan Academy 28 (1952), 177–181, doi:10.3792/pja/1195570997.
4. OEIS Foundation, sequence A055204, *Squarefree part of n!*.
