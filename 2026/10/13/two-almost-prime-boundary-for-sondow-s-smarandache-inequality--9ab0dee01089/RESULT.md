# Two-almost-prime boundary for Sondow's Smarandache inequality

## Finding
Let \(S(n)\) denote the Smarandache (also called Kempner) function: \(S(n)\) is the least positive integer \(j\) for which \(n\mid j!\). Let \(\Omega(n)\) count prime factors with multiplicity.

For every integer \(n\ge2\) with \(\Omega(n)\le2\),
\[
n^2<S(n)!\quad\Longleftrightarrow\quad n\notin\{2,3,6,15\}.
\]
Thus the failures of Sondow's inequality on the complete two-almost-prime stratum are exactly \(2,3,6,15\). In particular, every further exceptional integer must have \(\Omega(n)\ge3\).

## Assumptions and scope
The domain is all integers \(n\ge2\) with \(\Omega(n)\le2\), with multiplicity counted. Such an \(n\) is exactly one of: a prime \(p\), a prime square \(p^2\), or a squarefree semiprime \(pq\) with primes \(p<q\). No assertion is made here about integers with \(\Omega(n)\ge3\), and the result does not claim a classification of all exceptions to Sondow's inequality.

## Proof
If \(n=p\) is prime, then \(S(p)=p\). Hence the required inequality is \(p^2<p!\). It fails for \(p=2,3\). For every prime \(p\ge5\),
\[
p!=p(p-1)!>p^2,
\]
because \((p-1)!\ge2\cdot3\cdot(p-1)>p\).

Now let \(n=p^2\). For \(p=2\), \(S(4)=4\). For odd \(p\), every factorial \(j!\) with \(j<2p\) contains only one multiple of \(p\), while \((2p)!\) contains both \(p\) and \(2p\); since \(p^2>2p\), these contribute exactly two factors of \(p\). Thus \(S(p^2)=2p\) for every prime \(p\). For \(p=2\), \(4^2=16<4!=24\). For \(p\ge3\),
\[
(2p)!\ge(2p)(2p-1)(2p-2)(2p-3)>p^4,
\]
since the first three displayed factors are strictly greater than \(p\) and the fourth is at least \(p\). Therefore every prime square satisfies Sondow's inequality.

Finally let \(n=pq\) with distinct primes \(p<q\). Then \(S(pq)=q\): the factorial \(q!\) contains both prime factors, whereas no smaller factorial is divisible by \(q\). The inequality is therefore
\[
p^2q^2<q!.
\]
For \(q=3\), necessarily \(p=2\), and \(36>3!=6\), so \(6\) is exceptional. For \(q=5\), the possibilities are \(p=2,3\): one has \(100<5!=120\), while \(225>120\), so \(10\) satisfies the inequality and \(15\) does not.

It remains to treat \(q\ge7\). Since \(p<q\) are primes, \(p\le q-2\). Put
\[
F(m)=rac{m!}{m^2(m-2)^2}\qquad(m\ge3).
\]
Directly,
\[
F(7)=rac{5040}{49\cdot25}>1.
\]
Moreover, for every integer \(m\ge7\),
\[
rac{F(m+1)}{F(m)}
=rac{m^2}{(m+1)(m-1)}\cdotrac{(m-2)^2}{m-1}>1,
\]
because \(m^2>(m+1)(m-1)\) and \((m-2)^2>m-1\). Hence \(F(q)>1\) for every \(q\ge7\), so
\[
q!>q^2(q-2)^2\ge q^2p^2.
\]
Thus all squarefree semiprimes with \(q\ge7\) satisfy the inequality. Combining the three forms proves the stated classification.

## Verification
The symbolic proof above is independent of a search cutoff. A bundled exact regression checker factors every \(2\le n\le200000\), selects those with \(\Omega(n)\le2\), computes \(S(n)\) from prime-power valuations of factorials, and compares \(n^2\) with a capped exact factorial table whose cap exceeds every tested \(n^2\). It checks \(63214\) two-almost-prime inputs and finds exactly the four failures \(2,3,6,15\).

## Relationship to prior work
Li and Sha define the same Smarandache function and prove the stronger asymptotic statement that for every fixed real \(k>1\), the inequality \(n^k<S(n)!\) holds for almost all positive integers \(n\). Their Theorem 1.2 is a counting bound for the exceptional set; it does not classify the two-almost-prime stratum. Their proof explicitly separates cases according to whether \(S(n)=P(n)\), where \(P(n)\) is the largest prime factor, rather than classifying exceptions by \(\Omega(n)\).

Earlier literature on the Smarandache function contains general pointwise inequalities and algorithms, including bounds for prime powers, but the inspected sources do not state the above exact four-element exception set on \(\Omega(n)\le2\). Searches under the alias “Kempner function,” the semiprime formulation, the prime-square formulation, and the exact exceptional set found no implication-equivalent statement. A similarly named literature on “\(\mu\)-Sondow numbers” concerns a different divisibility notion and does not imply this result.

## Limitations
This is a low-multiplicative-complexity classification, not a description of the full exceptional set. The proof shows only that any exception other than \(2,3,6,15\) must have at least three prime factors counted with multiplicity. The literature search cannot logically exclude every obscure or unindexed earlier observation; the main residual originality risk is an elementary equivalent statement under the older name “Kempner function.”

## References
1. X. Li and M. Sha, “A Proof of Sondow's Conjecture on the Smarandache Function,” arXiv:1907.00370; *American Mathematical Monthly* 127 (2020), 939–943, DOI 10.1080/00029890.2020.1820789.
2. J. Sándor, “On certain inequalities involving the Smarandache function,” an earlier collection of pointwise inequalities for \(S(n)\).
