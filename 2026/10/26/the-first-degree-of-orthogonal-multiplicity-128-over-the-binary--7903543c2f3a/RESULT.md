# The first degree of orthogonal multiplicity 128 over the binary polynomial ring

## Finding
For monic \(f\in\mathbb F_2[T]\), write \(m(f)\) for the number of polynomials \(g\) of degree below \(\deg f\) coprime to \(f\) for which every partial quotient of the finite continued fraction for \(g/f\) has degree one. Then the least \(d\) for which some monic polynomial of degree \(d\) satisfies \(m(f)\ge128\) is \(d=26\). Exactly one monic degree-\(26\) polynomial attains this threshold:

\[
f_*(T)=(T^2+T+1)(T^3+T+1)(T^3+T^2+1)(T^4+T^3+1)(T^4+T^3+T^2+T+1)(T^5+T^2+1)(T^5+T^4+T^2+T+1).
\]

Its coefficient-bit integer is `123935485` (the coefficient of \(T^i\) is bit \(i\)), and \(m(f_*)=128\). There are precisely six monic degree-\(25\) polynomials with at least seven distinct nonlinear irreducible factors; none has positive orthogonal multiplicity.

## Assumptions and scope
All polynomials and polynomial divisions are over \(\mathbb F_2\). Degree refers to polynomial degree, and multiplicity is the standard orthogonal multiplicity above, not the number of irreducible factors with multiplicity. Blackburn's theorem, also recalled in the cited 2026 study, states that \(m(f)=0\) or \(m(f)=2^{\omega_0(f)}\), where \(\omega_0(f)\) is the number of distinct irreducible factors of \(f\) of degree greater than one. Thus the threshold \(m(f)\ge128\) forces \(\omega_0(f)\ge7\).

## Proof
There are exactly one monic irreducible quadratic, two irreducible cubics, three irreducible quartics, six irreducible quintics and nine irreducible sextics over \(\mathbb F_2\). The seven least-degree *distinct* nonlinear factors consequently have degrees \(2,3,3,4,4,4,5\), summing to \(25\). An eighth would require degree at least \(30\). Therefore a denominator of degree at most \(26\) and multiplicity at least \(128\) has exactly seven distinct nonlinear irreducible factors.

In degree \(25\), those seven factors must use both cubics, all three quartics and precisely one of the six quintics: six candidate polynomials. In degree \(26\), the complete candidates comprise twelve obtained by adjoining one of the linear factors \(T\) or \(T+1\) to a degree-\(25\) candidate, nine obtained by replacing its quintic with one of nine irreducible sextics, and forty-five from both cubics, two of three quartics and two of six quintics. The total is \(12+9+45=66\). No other factor-degree configuration fits degree \(26\).

It remains to determine exactly which of these 72 candidates have positive orthogonal multiplicity. Each degree-one partial quotient is either \(T\) or \(T+1\). Given a word \(a_1,\ldots,a_d\) with letters in this pair, define its continuant \(K_0=1\), \(K_1=a_1\), \(K_j=a_jK_{j-1}+K_{j-2}\) for \(2\le j\le d\). Distinct words of this form are precisely the reduced degree-one-quotient continued fractions, and each has denominator \(K_d\). Its leading coefficient is one and its degree is \(d\). Thus \(m(f)\) equals the number of these \(2^d\) words with \(K_d=f\).

The included `verify.c` performs an exhaustive finite computation: enumerates all monic irreducibles of degrees two through six by division by all monic polynomials of degree at most half the candidate degree; constructs exactly the six and 66 candidates; and enumerates all words of lengths 25 and 26 using the displayed continuant recurrence. The executable asserts all candidate totals, degree conditions, and multiplicity. The six degree-\(25\) candidates have zero occurrences. Of the 66 degree-\(26\) candidates, the unique occurrence-positive denominator has bit representation `123935485`, and its word count is exactly 128. The independent binary product of the seven displayed factors is that integer; their irreducibility follows from the same complete low-degree factor test. Therefore the displayed polynomial is the sole minimizer and has precisely the asserted multiplicity.

## Verification
Compile and run using a standard C11 compiler: `cc -O2 -std=c11 -Wall -Wextra verify.c -o verify && ./verify`. On the recorded run the output included `degree_25_candidates=6 positive=0`, `degree_26_candidates=66 positive=1`, `positive_degree_26: 123935485`, `witness_word_mask=52109888 witness_multiplicity=128` and `VERIFY_OK`. Every word of both lengths is enumerated; there is no sampling, probabilistic step, or extrapolation beyond those finite lengths. The factor-number lower bound is mathematical and applies to every lower degree.

## Relationship to prior work
Blackburn's 1998 theorem supplies the binary-zero-or-power-of-two multiplicity restriction, and his numerical table, as reported in the 2026 primary paper, extends through degree 21. The 2026 work counts polynomials of *positive* orthogonal multiplicity through degree 33 but does not state the least degree or unique polynomial realizing the first level \(128\). The result here is a different refinement: a sharp extremal-degree and uniqueness classification, not another aggregate count.

## Limitations
This is an exact finite-degree result, not an asymptotic or a classification of every higher multiplicity threshold. The full 1998 article was not available for direct inspection; an unindexed older extremal table remains a novelty risk. The proof uses the published multiplicity theorem as a cited mathematical input; the exhaustive program proves all new finite enumerations conditional on that standard result. The self-review is not independent verification.

## References
1. David Niedbala Giraudin, *The proportion of polynomials over \(\mathbb F_2\) with positive orthogonal multiplicity*, arXiv:2610.02352v1, first posted 2026-10-01, https://arxiv.org/abs/2610.02352.
2. S. R. Blackburn, work on orthogonal multiplicity, *Journal of Number Theory* (1998), DOI:10.1006/jnth.1997.2201. Full article not directly inspected.
