# The complete first multiplicity layer of odd abundant numbers
## Finding
An odd positive integer \(n\) with \(\Omega(n)=5\) is abundant if and only if it belongs to the following disjoint families: \(945,1575,2205\); \(3^2\cdot5\cdot7\cdot q\) for prime \(11\le q\le103\); \(3^2\cdot5\cdot11\cdot q\) for \(q\in\{13,17\}\); \(3\cdot5^2\cdot7\cdot q\) for \(q\in\{11,13,17\}\); \(3\cdot5\cdot7^2\cdot q\) for \(q\in\{11,13\}\); \(3\cdot5\cdot7\cdot11^2\); \(3\cdot5\cdot7\cdot11\cdot q\) for prime \(13\le q\le383\); \(3\cdot5\cdot7\cdot13\cdot q\) for prime \(17\le q\le61\); \(3\cdot5\cdot7\cdot17\cdot q\) for \(q\in\{19,23,29\}\); and \(3\cdot5\cdot7\cdot19\cdot23\). There are exactly \(121\) such integers, with least member \(945\) and greatest member \(442365\). Consequently every odd abundant integer has \(\Omega(n)\ge5\), and this sharp boundary layer is completely classified.

Here \(\Omega(n)=\sum_p \nu_p(n)\) counts prime factors with multiplicity, and \(n\) is abundant when \(\sigma(n)>2n\).

## Assumptions and scope
The statement concerns positive odd integers and the ordinary divisor-sum function \(\sigma\). It classifies the complete boundary \(\Omega(n)=5\); it makes no claim about higher multiplicity layers.

## Proof
Put \(I(n)=\sigma(n)/n\). For a prime power,
\[
I(p^a)=1+p^{-1}+\cdots+p^{-a}.
\]
If \(p<q\) and \(a>b\), then
\[
I(p^a)I(q^b)-I(p^b)I(q^a)=\sum_{i=b+1}^a\sum_{j=0}^b\left(p^{-i}q^{-j}-p^{-j}q^{-i}\right)>0.
\]
Thus, for fixed distinct primes and a fixed exponent multiset, abundancy is maximized by assigning larger exponents to smaller primes. It also decreases when any prime is increased.

For \(\Omega(n)\le4\), it is enough to consider the five exponent partitions of \(4\). Their maximal odd abundancies occur at \(3^4\), \(3^3\cdot5\), \(3^2\cdot5^2\), \(3^2\cdot5\cdot7\), and \(3\cdot5\cdot7\cdot11\), respectively. The largest is
\[
\frac{4}{3}\frac{6}{5}\frac{8}{7}\frac{12}{11}=\frac{2304}{1155}<2.
\]
Hence every odd abundant integer has \(\Omega(n)\ge5\).

Now assume \(\Omega(n)=5\), and let \(q\) be the largest prime divisor. If \(q\ge389\), the same exchange argument reduces each possible number of distinct prime divisors \(r\in\{1,2,3,4,5\}\) to an exact extremal product. The respective maxima are
\[
\frac{364}{243},\qquad \frac{15730}{10503},\qquad \frac{10478}{5835},\qquad \frac{5408}{2723},\qquad \frac{59904}{29953},
\]
and each is strictly less than \(2\). Therefore every abundant candidate with \(\Omega(n)=5\) has largest prime divisor at most \(383\).

It remains a finite exact problem. For each ordered positive exponent composition \((a_1,\ldots,a_r)\) of \(5\), and increasing odd primes \(p_1<\cdots<p_r\le383\), the bundled verifier evaluates the rational product
\[
\prod_i I(p_i^{a_i}).
\]
Monotonic upper bounds using the next available primes prune only branches whose maximum possible product is already at most \(2\). The exact survivor set is then compared with the ten displayed families. The two sets agree and have cardinality \(121\). This completes the exhaustive proof.

## Verification
Run `python verify.py`. It uses exact rational arithmetic, proves the \(383\) largest-prime cutoff, exhaustively enumerates every exponent composition of \(5\), and compares the survivor set with the claimed families. The included `classification.json` stores the resulting \(121\) integers.

## Relationship to prior work
Ross introduced \(\{-1,1\}\)-perfect numbers and, while discussing odd nondeficient numbers, explicitly noted \(945\) as the least odd abundant number and proposed a broad signed-divisor conjecture for nonsquare odd nondeficient numbers. The focal paper does not classify the \(\Omega(n)=5\) abundant layer. The current OEIS entry A005231 records the standard lower bound that an odd abundant number has at least five prime factors counted with multiplicity, but its sequence table does not state the exact boundary classification above. A later paper by Campbell disproves Ross's signed-divisor conjecture; the accessible abstract and introductory material concern counterexample families, not this exact multiplicity-five classification. A current public computational window for the signed-divisor problem covers all admissible integers through \(10^6\); that result concerns signed presentations rather than an exhaustive classification of odd abundant integers with \(\Omega(n)=5\).

A previously checked classification of odd unitary Zumkeller numbers with five distinct prime factors has the same squarefree prime-support ranges appearing in the last four families. That prior statement is about a stronger divisor-partition property and five distinct prime factors; it neither states the complete odd-abundant \(\Omega(n)=5\) classification nor includes the \(34\) repeated-prime boundary members here.

## Limitations
The exhaustiveness step is finite but complete only because the symbolic abundancy argument first proves the global largest-prime cutoff \(q\le383\). The result does not classify \(\Omega(n)\ge6\). Searches did not locate a prior statement of this exact \(121\)-member classification; an obscure table or equivalent formulation could still have been missed.

## References
1. Tyler Ross, “A Perfect Number Generalization and Some Euclid-Euler Type Results,” *Journal of Integer Sequences* 27 (2024), Article 24.7.5, published 2024-09-08. Primary MSC2020 11A25.
2. OEIS Foundation Inc., A005231, “Odd abundant numbers,” current entry consulted 2026-10-05.
3. John M. Campbell, “Disproofs of two conjectures concerning nondeficient numbers,” arXiv:2607.11043 (2026), later published online in *Canadian Mathematical Bulletin* on 2026-09-25.
