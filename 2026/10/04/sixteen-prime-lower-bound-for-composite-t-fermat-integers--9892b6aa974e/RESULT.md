# Sixteen-prime lower bound for composite T-Fermat integers
## Finding
Every composite T-Fermat integer has at least \(16\) distinct prime divisors. Equivalently, if \(n\) is composite and T-Fermat, then \(\omega(n)\ge 16\).

## Assumptions and scope
For \(n>1\), write
\[
T_n(X)=\sum_{d\mid n}X^d-d(n)X,
\]
where \(d(n)\) is the divisor-counting function. A squarefree integer \(n\) is T-Fermat when \(n\mid T_n(x)\) for every integer \(x\). The statement concerns this notion as developed in Hakobyan's 2026 paper. It is only a lower bound on the number of prime factors of a hypothetical composite example; it does not assert that composite T-Fermat integers exist.

## Proof
Let \(n\) be composite T-Fermat and put \(M=\omega(n)\). Hakobyan proves that every composite T-Fermat integer is a Carmichael number, that it is odd, and that every prime divisor \(p\mid n\) satisfies \(p<d(n)\). Since \(n\) is squarefree, \(d(n)=2^M\), so every prime divisor satisfies
\[
p<2^M.
\]
Hakobyan also proves two pairwise restrictions on the prime divisors: the quantity \(\nu_2(p-1)\) is independent of \(p\mid n\), and for any prime divisors \(p,q\mid n\), the multiplicative order \(\operatorname{ord}_{p-1}(q)\) is odd.

For fixed \(M\) and integer \(a\ge1\), form a finite graph \(G_{M,a}\). Its vertices are the odd primes \(p<2^M\) with \(\nu_2(p-1)=a\). Distinct vertices \(p,q\) are adjacent exactly when both
\[
\operatorname{ord}_{p-1}(q)\quad\text{and}\quad \operatorname{ord}_{q-1}(p)
\]
are odd. The prime support of any composite T-Fermat integer with \(M\) prime factors must therefore be an \(M\)-clique in one of the graphs \(G_{M,a}\).

The standalone exact verifier exhaustively enumerates these finite graphs. For every \(3\le M\le14\), no \(M\)-clique exists. For \(M=15\), exactly one compatible \(15\)-clique exists:
\[
\{331,631,751,991,2311,4951,7351,11251,11551,14851,17011,25411,26251,28351,30871\}.
\]
Let \(N\) be the product of these fifteen primes. Korselt's criterion would require \(p-1\mid N-1\) for every \(p\mid N\) if \(N\) were Carmichael. At \(p=331\), however,
\[
N-1\equiv90\pmod{330},
\]
so \(N\) is not Carmichael. Therefore \(M=15\) is also impossible. Composite Carmichael numbers have at least three prime factors, so all cases \(M\le15\) are excluded and \(M\ge16\).

## Verification
The embedded program `verify_tfermat_bound.py` uses only exact integer arithmetic. It generates every prime below \(2^{15}\) by a sieve, computes \(\nu_2(p-1)\), factors Euler totients by trial division, computes multiplicative orders by exact modular exponentiation and divisor reduction, and recursively enumerates every target-size clique. It then applies Korselt's divisibility test to every surviving size-\(15\) support. Its certificate records the per-\(M\) vertex and edge counts, all surviving target-size cliques, and the Korselt remainders.

A successful replay prints:

`VERIFY_OK M=3..14_no_compatible_cliques M=15_unique_compatible_clique_not_Carmichael`

followed by the unique size-\(15\) clique and the witness `('331', 90)`. The enumeration is exhaustive over the finite domain forced by \(p<2^M\); it is not a sampling argument.

## Relationship to prior work
Hakobyan's paper supplies the structural ingredients used above: the Carmichael implication, the prime bound \(p<d(n)\), the common \(2\)-adic valuation of \(p-1\), and the odd multiplicative-order condition. The paper also proves finiteness for each fixed number of prime divisors, but the inspected full text does not give an explicit lower bound of \(16\) prime factors. The same divisor-polynomial condition appeared under the earlier term “almost prime” in a 2024 competition problem; that earlier formulation does not contain the 2026 pairwise order restrictions used in the finite exclusion here.

Targeted searches for the exact lower bound, its compatibility-graph formulation, the earlier “almost prime” terminology, and Carmichael/order aliases did not locate a statement implying this result. The closest located results about weak Carmichael, Lucas–Carmichael, and other pseudoprime predicates concern different defining conditions and do not imply the T-Fermat bound.

## Limitations
The argument proves only \(\omega(n)\ge16\). It neither constructs a composite T-Fermat integer nor proves that none exist. The computational part is finite and exact, but it depends on the cited structural lemmas from the motivating paper. The literature comparison cannot exclude an unindexed source using different terminology, and no independent audit has been performed.

## References
T. Hakobyan, *T-Fermat integers*, arXiv:2603.00679v2 (2026); earliest public arXiv version v1 dated 2026-02-28.

International Mathematics Competition for University Students, 2024, Problem 10 (“almost prime” formulation of the divisor-polynomial condition).
