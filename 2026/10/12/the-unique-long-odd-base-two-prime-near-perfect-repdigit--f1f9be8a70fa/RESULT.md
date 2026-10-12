# The unique long odd-base two-prime near-perfect repdigit

## Finding
For each odd base \(g\in\{3,5,7,9\}\), digit \(1\le a<g\), and integer \(\ell\ge3\), put
\[
N=aU_\ell(g),\qquad U_\ell(g)=\frac{g^\ell-1}{g-1}=\sum_{j=0}^{\ell-1}g^j.
\]
Suppose that \(\omega(N)=2\), where \(\omega\) is the number of **distinct** prime divisors, and that \(N\) is near-perfect: for some proper positive divisor \(d\mid N\), \(\sigma(N)=2N+d\). Then
\[
\boxed{(g,a,\ell,N,d)=(3,1,4,40,10).}
\]
Conversely, this tuple works. Thus precisely one near-perfect integer with exactly two distinct prime factors is a repdigit of at least three digits in the four indicated odd bases. In particular, the published two-digit upper bound and stated emptiness for base \(3\) in Theorem 1.3(a) of [2] have this exception.

## Assumptions and scope
All variables are ordinary positive integers with \(g\in\{3,5,7,9\}\), \(1\le a\le g-1\), \(\ell\ge3\). A repdigit has exactly \(\ell\) equal nonzero digits \(a\) in base \(g\), so the leading digit is nonzero. No assumption is made about \(\Omega(N)\), the number of prime factors **with** multiplicity. We invoke the complete two-distinct-prime near-perfect classification of Ren and Chen [1], not any conjecture.

## Proof
**Structural bound.** Let \(e=\nu_2(N)\). Theorem 1.2 of [1] states that every near-perfect number with exactly two distinct prime divisors belongs to one of the following forms:
\[
\begin{aligned}
\mathrm{A}:&\quad 2^{p-1}(2^p-1)^2, \\
\mathrm{B}:&\quad 2^{2p-1}(2^p-1), \\
\mathrm{C}:&\quad 2^{t-1}(2^t-2^k-1),
\end{aligned}
\]
where the stated odd factors are prime, \(p\) is prime in the first two forms, \(1\le k<t\) in form C, or the exceptional integer \(40\). Each has \(e\ge1\) and satisfies
\[
N<2^{3e+2}. \tag{1}
\]
Indeed, in form A use \(e=p-1\), in B use \(e=2p-1\), in C use \(e=t-1\), and for \(40\) use \(e=3\). These substitutions yield (1) term by term.

**Length bound.** For odd \(g\), the lifting-the-exponent identity gives
\[
\nu_2(U_\ell(g))=
\begin{cases}
0,&\ell\text{ odd},\\
\nu_2(g+1)+\nu_2(\ell)-1,&\ell\text{ even}.
\end{cases}
\]
Because \(1\le a\le8\) and \(4\le g+1\le10\), we obtain \(e=\nu_2(a)+\nu_2(U_\ell(g))\le5+\log_2\ell\). On the other hand \(N\ge U_\ell(g)\ge3^{\ell-1}\). Consequently
\[
3^{\ell-1}\le N<2^{17}\ell^3.\tag{2}
\]
At \(\ell=20\), \(3^{19}>2^{17}\cdot20^3\). Moreover the ratio \(3^{\ell-1}/\ell^3\) strictly increases for \(\ell\ge20\), since \(3\ell^3>(\ell+1)^3\). Therefore (2) forces \(3\le\ell\le19\). In this range \(\nu_2(\ell)\le4\), hence \(1\le e\le9\).

**Finite, exhaustive parameter sieve.** For \(1\le e\le9\), Ren--Chen's forms have only the following possible parameters. Form A uses \(e\in\{1,2,4,6\}\); form B uses \(e\in\{3,5,9\}\). For form C the full set of \((e,k)\) is
\[
\begin{array}{c|l}
e&k\\\hline
2&1,2\\
3&1,2,3\\
4&1,3\\
5&1,2,4,5\\
7&2,4,5,6,7\\
8&1,3,5,7\\
9&1,2,5
\end{array}
\]
(the odd factor in every entry is checked prime by trial division). Including \(40\), this produces \(4+3+23+1=31\) **distinct** candidate integers. For each candidate and each of the four bases, test the necessary and sufficient equal-digit condition
\[
U_\ell(g)\mid N,\qquad 1\le N/U_\ell(g)<g,
\]
for every integer \(3\le\ell\le19\). The exact exhaustive division finds one match only: \((g,\ell,a,N)=(3,4,1,40)\). The complete standalone `verify.py` implements this finite sieve with integer arithmetic and trial-division primality; `verification_output.txt` gives the result. Unlike an unbounded empirical scan, the preceding proof establishes the finite bounds first.

Finally, \(40=2^3\cdot5=1+3+9+27\) and
\[
\sigma(40)=(1+2+4+8)(1+5)=90=2\cdot40+10.
\]
Here \(10\) is a proper divisor, and \(\omega(40)=2\), completing both directions. \(\square\)

## Verification
Run `python3 verify.py` using a standard Python 3 installation. Its deterministic primality test divides every trial integer by every possible divisor through its integer square root, and its candidate enumeration loops over every admissible \(e\), \(p\), \(t\), and \(k\). It checks all \(4\cdot17\cdot31\) candidate/base/length combinations, including every allowed digit through an exact quotient test. It also verifies near-perfectness and proper redundant-divisor conditions for every candidate. The final output records 31 distinct candidates and the sole tuple \((3,4,1,40)\). The general conclusion rests on the symbolic bounds and the exhaustive bounded sieve together; finite testing alone would not prove an infinite assertion.

## Relationship to prior work
Ren--Chen [1], Theorem 1.2, classifies all near-perfect integers with two distinct prime factors by three parameter families and the exceptional integer \(40\). That broad parametrization does **not** identify the intersection with odd-base repdigits; the new valuation bound makes its repdigit intersection finite and explicitly solvable. Hasanalizade [2], Theorem 1.3(a), asserts that in bases \(2\le g\le10\) every two-prime near-perfect repdigit has fewer than three digits and lists none for base \(3\). The counterexample \(40=(1111)_3\) refutes those particular assertions; our theorem replaces them with a complete statement for the four odd bases and lengths at least three. The displayed finite sieve also closes the type-C case for these bases. Related published work treats even bases, a mathematically disjoint parameter range.

## Limitations
The theorem neither classifies one- and two-digit repdigits nor addresses odd bases greater than \(9\), or near-perfect integers with three or more distinct prime divisors. It depends on the published Ren--Chen classification [1], whose theorem and proof were examined. The finite sieve is reproducible exact arithmetic, but the proof does not establish any claim beyond the stated range. No independent audit has been performed.

## References
[1] X.-Z. Ren and Y.-G. Chen, *On near-perfect numbers with two distinct prime factors*, Bull. Aust. Math. Soc. **88** (2013), 520--524, DOI: 10.1017/S0004972713000178, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/07195AD6B597AFD416F0AE1935286E3F/S0004972713000178a.pdf/on_nearperfect_numbers_with_two_distinct_prime_factors.pdf.

[2] E. Hasanalizade, *On near-perfect numbers of special forms*, arXiv:2206.10353v1 (first public 2022-06-14), later Bull. Aust. Math. Soc. **108** (2023), 366--372, DOI: 10.1017/S0004972723000072, https://arxiv.org/html/2206.10353v1.
