# The least odd ample integer with three distinct prime factors

## Finding
Let the recursive divisor function be defined by
\[
a(1)=1,\qquad a(n)=1+\sum_{\substack{d\mid n\\d<n}}a(d)\quad(n>1).
\]
An integer \(n\) is **ample** if \(a(n)>n\). The least odd ample integer with exactly three distinct prime divisors is
\[
N_*=3^{20}5^9 7^6=801204488268064453125.
\]
More precisely,
\[
a(N_*)=841632661765951062016,
\qquad a(N_*)-N_*=40428173497886608891>0.
\]
Every smaller odd positive integer having at most three distinct prime divisors is non-ample. Consequently three is the minimum possible number of distinct prime factors of an odd ample integer, and \(N_*\) is the first example at that minimum support size.

## Assumptions and scope
All integers are positive, and \(\sigma(n)\) is the sum of positive divisors of \(n\). The inequality \(a(n)>n\) is strict. The result is a global minimum among odd numbers with **exactly three distinct prime factors**, not among all odd ample numbers (which can have more prime factors and be much smaller). The computation uses arbitrary-precision integer operations only; there is no numerical tolerance or unexamined search cutoff.

## Proof
**1. A divisor-sum exclusion.** Suppose \(\sigma(n)<2n\). Every divisor \(d\mid n\) also satisfies \(\sigma(d)/d\le\sigma(n)/n<2\): for fixed prime, \(\sigma(p^e)/p^e=1+p^{-1}+\cdots+p^{-e}\) increases with \(e\). Strong induction using the defining recurrence therefore gives \(a(d)\le d\) for every divisor \(d\mid n\). At the induction step,
\[
a(n)\le1+\sum_{\substack{d\mid n\\d<n}}d
=1+\sigma(n)-n\le n,
\]
where the last inequality uses integrality of \(\sigma(n)<2n\). Thus an ample integer cannot be deficient.

An odd positive integer with at most two distinct prime factors is deficient, since
\[
\frac{\sigma(n)}n<\frac32\frac54=\frac{15}{8}<2
\]
(with an obvious stronger bound when there is one or no prime factor). Now let an odd integer have exactly three distinct prime factors \(p<q<r\). It is deficient whenever
\[
\frac p{p-1}\frac q{q-1}\frac r{r-1}\le 2,
\]
since \(\sigma(n)/n\) is **strictly** smaller than this Euler product at finite positive exponents. If \(p\ge5\), the product is at most \((5/4)(7/6)(11/10)<2\). If \(p=3\) and \(q\ge7\), it is at most \((3/2)(7/6)(11/10)<2\). If \(p=3,q=5,r\ge17\), it is at most \((3/2)(5/4)(17/16)=255/128<2\). Therefore every candidate odd ample integer with exactly three prime factors is supported on exactly one of
\[
\{3,5,7\},\qquad \{3,5,11\},\qquad \{3,5,13\}.
\]

**2. An exact exponent-vector recurrence.** For any three distinct primes, define \(A(i,j,k)=a(p^i q^j r^k)\). This value is independent of the primes, since the divisor partial order is determined by the three exponents. Let \(A(i,j,k)=0\) when any coordinate is negative. The generating function of the defining divisor recurrence is
\[
\sum_{i,j,k\ge0}A(i,j,k)X^iY^jZ^k
=\frac1{2(1-X)(1-Y)(1-Z)-1}.
\]
Indeed, if \(S(i,j,k)\) denotes the sum of \(A(u,v,w)\) over \(0\le u\le i,0\le v\le j,0\le w\le k\), then \(2A=S+1\) at every exponent triple and the displayed rational identity follows by formal power series. Comparing coefficients gives \(A(0,0,0)=1\), and for every nonzero triple the seven-neighbor recurrence
\[
\begin{aligned}
A(i,j,k)=2\big(&A(i-1,j,k)+A(i,j-1,k)+A(i,j,k-1)\\
&-A(i-1,j-1,k)-A(i-1,j,k-1)\\
&-A(i,j-1,k-1)+A(i-1,j-1,k-1)\big).
\end{aligned}
\]
The stated generating function and recurrence are exact formal identities; they work on coordinate planes as well as in the interior. Their values use only lexicographically earlier exponent triples.

**3. Complete finite exclusion and witness.** Set \(N_*=3^{20}5^9 7^6\). The independently reproducible `verify.py` computes \(A(i,j,k)\) for all triples in the box \(0\le i\le43\), \(0\le j\le29\), \(0\le k\le24\) using the formula of Step 2. These upper bounds include every triple for \(3^i5^j r^k\le N_*\), \(r\in\{7,11,13\}\), because all three prime bases are at least \(3,5,7\), respectively. For each of the three supports, the checker loops over all positive exponent triples in that box whose corresponding integer is \(\le N_*\) and tests the **exact** inequality \(A(i,j,k)>3^i5^j r^k\). It obtains:

| Prime support | Exact eligible exponent triples | Ample triples at or below \(N_*\) | Minimum \(n-a(n)\) among smaller candidates |
| --- | ---: | --- | ---: |
| \(\{3,5,7\}\) | 4,650 | \((20,9,6)\) only | 79 |
| \(\{3,5,11\}\) | 3,718 | none | 139 |
| \(\{3,5,13\}\) | 3,459 | none | 169 |

These 11,827 triples exhaust every positive-exponent candidate up to the proposed minimum. At the sole ample triple, the checker obtains precisely the integer \(a(N_*)\) displayed in the Finding. The prime-support exclusion rules out all other odd integers with three or fewer prime factors. This establishes both minimality and attainment.

## Verification
Run `python3 verify.py` from the directory containing this result and the verifier (standard Python 3 only). The program reconstructs the entire necessary exponent cube from the seven-term recurrence, enumerates all eligible exponent triples for each support with exact product cutoffs, checks the expected counts and the strict minimum gap, and asserts the unique surviving ample triple.

Two independent checks of the witness are included. First, on the witness's entire divisor box \(0\le i\le20\), \(0\le j\le9\), \(0\le k\le6\), it recomputes \(a\) directly by summing all proper-divisor values and checks every coefficient against the seven-term recurrence. Second, it evaluates the number of ordered factorizations of \(N_*\) into nonunit factors by inclusion-exclusion, and checks that twice this number equals \(a(N_*)\). The latter ordered-factorization identity is given in Fink's cited work. There are no heuristic or floating-point assumptions.

## Relationship to prior work
Fink introduced ample numbers and gave the smallest *unrestricted* odd ample number, which has five distinct prime factors [1]. His theorem that deficient numbers are non-ample is sharpened here to a complete three-prime-support reduction for the **different problem** of the least odd ample integer with minimal distinct-prime support. Fink's later paper identifies the ordered-factorization relation and the global Dirichlet series for \(a\) [2]; it does not compute this three-prime minimum.

A later finite-support theorem, “Finite abundant prime supports force ample numbers” [3], proves existence (and infinitude) for every finite prime support satisfying an Euler-product condition. It explicitly does **not** give an effective bound for the least ample number on such a support. Hence that existence theorem implies that suitable three-prime ample numbers exist, but it neither identifies nor implies the exact minimizer or the 11,827-triple certificate here. Nearby work on odd ample numbers gives a minimum total prime multiplicity, a different invariant; it does not identify the least integer with exactly three distinct primes. Published conference work [4] discusses progress on Fink's conjecture without this minimum. A search of the standard recursive-divisor sequence table [5] also does not contain the large witness.

## Limitations
This is an exact minimality result for the first odd-support layer, not a classification of all odd ample numbers. The finite certificate is exhaustive only **after** the proved prime-support sieve and the proved numerical upper bound; no infinite search or exclusion is inferred from finite sampling alone. Novelty comparisons with accessible primary papers, published research records, and searchable tables cannot rule out a previously unindexed exact minimizer.

## References
1. T. Fink, “Recursively abundant and recursively perfect numbers,” arXiv:2008.10398v1, first public 24 August 2020, especially Section 3.3 and Lemma 1. https://arxiv.org/pdf/2008.10398
2. T. M. A. Fink, “Properties of the recursive divisor function and the number of ordered factorizations,” arXiv:2307.09140v1, first public 18 July 2023. https://arxiv.org/pdf/2307.09140
3. “Finite abundant prime supports force ample numbers,” https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-abundant-prime-supports-force-ample-numbers--3a5bff12f682 (full `RESULT.md` examined).
4. M. P. Liyanage and P. G. R. S. Ranasinghe, “An Approach Towards Settling a Conjecture on Ample Numbers,” RISTCON 2022 conference abstract, 19 January 2022.
5. OEIS A067824, “Recursive divisor count,” https://oeis.org/A067824.
