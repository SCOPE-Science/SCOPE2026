# Exact prime-support thresholds for generalized non-Wieferich integers

## Finding
Let \(b\ge2\) be an integer and let \(P\) be any nonempty finite set of odd primes not dividing \(b\). For each \(p\in P\) set
\[
d_p=\operatorname{ord}_p(b),\qquad h_p=\nu_p(b^{d_p}-1),\qquad t_p=h_p+\max_{q\in P}\nu_p(d_q).
\]
These are finite positive, effectively computable integers, except that the maximum may be zero. Given any exponents \(a_p\ge1\), set \(n=\prod_{p\in P}p^{a_p}\), \(L=\operatorname{ord}_n(b)\), and
\[
W_b(n)=\gcd\!\left(n,\frac{b^L-1}{n}\right).
\]
The quotient is integral. The following *exact prime-support valuation law* holds for every such \(b,P,(a_p)\):
\[
\boxed{\quad\nu_p\!\left(\frac{b^L-1}{n}\right)=\max(0,t_p-a_p)\quad(p\in P).\quad}
\]
In particular,
\[
\boxed{\quad W_b(n)=1\ \Longleftrightarrow\ a_p\ge t_p\ \text{for every }p\in P.\quad}
\]
Therefore the non-Wieferich integers with a fixed prime support \(P\) are exactly the exponent vectors in one upper orthant, with a *unique least integer* \(N_{b,P}=\prod_{p\in P}p^{t_p}\) under divisibility within that support. An equivalent exact power law is: for every odd \(n>1\) coprime to \(b\), writing \(a_p=\nu_p(n)\) and defining the above \(t_p\) on its prime support,
\[
\boxed{\quad W_b(n^k)=1\ \Longleftrightarrow\ k\ge K_b(n):=\max_{p\mid n}\left\lceil\frac{t_p}{a_p}\right\rceil\quad(k\ge1).\quad}
\]
Thus *every* odd integer coprime to \(b\) has all sufficiently large positive powers non-Wieferich in this order-based sense, with the exact first such power identified.

## Assumptions and scope
Here \(\operatorname{ord}_m(b)\) is the multiplicative order of \(b\) modulo \(m\) for \(\gcd(b,m)=1\); \(\nu_p\) is the usual prime valuation. We call \(n\) non-Wieferich to base \(b\) precisely when \(W_b(n)=1\). For \(b=2\), this is the same definition used in the recent study of non-Wieferich integers by Siegel and in the earlier work of Franco–Pomerance; it must not be confused with the alternative convention involving \(\varphi(n)\) rather than \(\operatorname{ord}_n(2)\). All moduli here are odd and greater than one. We assert nothing about even moduli or bases not coprime to the modulus.

## Proof
For each odd \(p\in P\), the order \(d_p\) divides \(p-1\), hence \(p\nmid d_p\). The elementary odd-prime lifting identity gives, for every integer \(u\ge1\),
\[
\nu_p(b^{d_p u}-1)=h_p+\nu_p(u).
\]
For completeness, if \(p\nmid u\) the binomial expansion of \((1+p^{h_p}c)^u-1\), with \(p\nmid c\), has valuation \(h_p\). Raising a unit congruent to one modulo \(p^{h_p}\) to the power \(p\) increases valuation by exactly one for odd \(p\); iterating and separating the prime-to-\(p\) part of \(u\) proves the identity.

Consequently the smallest exponent giving \(b^e\equiv1\pmod{p^{a_p}}\) is
\[
\operatorname{ord}_{p^{a_p}}(b)=d_p\,p^{\max(0,a_p-h_p)}.
\]
The Chinese remainder theorem implies
\[
L=\operatorname{lcm}_{q\in P}\bigl(d_q q^{\max(0,a_q-h_q)}\bigr).
\]
For a fixed \(p\in P\), only the \(q=p\) prime-power factor can contribute additional powers of \(p\), so
\[
\nu_p(L)=\max\!\left(\max_{q\in P}\nu_p(d_q),\ \max(0,a_p-h_p)\right).
\]
As \(d_p\mid L\) and \(p\nmid d_p\), another application of lifting yields
\[
\nu_p(b^L-1)=h_p+\nu_p(L)
=\max\!\left(h_p+\max_{q\in P}\nu_p(d_q),\ a_p\right)
=\max(t_p,a_p).
\]
Subtracting \(\nu_p(n)=a_p\) proves the exact quotient-valuation law. As the only prime factors of \(n\) are the members of \(P\), the gcd equals one precisely when all these valuations vanish. The threshold vector follows. Replacing each \(a_p\) by \(ka_p\) and solving the resulting inequalities proves the power law. Every step holds for arbitrarily large \(P\) and exponents; no numerical cutoff enters the proof.

For example, at base \(2\), \(P=\{3,7\}\), the two orders are \(d_3=2\), \(d_7=3\), and \(h_3=h_7=1\). Thus \(t_3=2\), \(t_7=1\). The integer \(21\) is Wieferich in the order-based sense, whereas \(63\) and all integers \(3^a7^c\) with \(a\ge2,c\ge1\) are non-Wieferich. In particular, \(K_2(21)=2\).

## Verification
The standalone file `verify.py` uses exact integer arithmetic without external packages. It compares the threshold criterion with a direct modular computation of \(\gcd(n,(b^{\operatorname{ord}_n(b)}-1)/n)\). It passed 3,422 direct checks for bases \(2,3,5,7\), 549 further prime-support/exponent combinations, and the exact power-threshold examples. The direct checks compute multiplicative orders by repeated modular multiplication and evaluate the quotient modulo \(n\) through modular exponentiation modulo \(n^2\). These finite computations test implementations and boundary cases; the unrestricted statement follows from the proof.

## Relationship to prior work
Franco–Pomerance (1995) introduced the order-based Wieferich-number definition and proved that the complementary set has density zero among odd integers. Their theorem supplies particular sufficient obstructions to non-Wieferich membership, not an exact exponent threshold for every fixed prime support. Siegel (2026) studies the counting function asymptotically and gives squarefree sufficient and necessary conditions and estimates for nonsquarefree numbers, but does not state this all-exponent, all-base prime-support classification or the exact first-power formula. The OEIS entries A182297 and A237292 give definitions, tabulated membership, and the identity expressing the gcd through the ratio of orders modulo \(n\) and \(n^2\); that identity does not itself determine the cross-prime threshold \(t_p\). The proof here uses classical order lifting and the Chinese remainder theorem, so priority remains sensitive to an implicit earlier derivation using these standard tools.

## Limitations
The theorem gives no asymptotic for the total count over varying prime supports and does not establish new results about the distribution of Wieferich primes. Base \(2\) is its direct application to the 1995/2026 convention; other bases are a natural definition extension. No independence or external verification is asserted. A previously unindexed explicit classification or an earlier result from which the complete threshold follows immediately would affect originality.

## References
1. C. Siegel, *An Asymptotic for Non-Wieferich Numbers*, arXiv:2610.28685v1, initially public 2026-10-19; https://arxiv.org/html/2610.28685v1.
2. Z. Franco and C. Pomerance, *On a Conjecture of Crandall Concerning the qx+1 Problem*, Math. Comp. 64 (1995), 1333–1336; https://math.dartmouth.edu/~carlp/PDF/paper101.pdf.
3. OEIS A182297, *Wieferich numbers (2)*; https://oeis.org/A182297.
4. OEIS A237292, multiplicative-order ratio sequence; https://oeis.org/A237292.
