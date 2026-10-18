# Independent mathematical audit

## correctness

PASS

When tau(n) is a power of 2, each prime exponent is 2^s-1; sigma_k(p^{2^s-1})=product_{j=0}^{s-1}(p^{k2^j}+1). For even k with t=v2(k), any odd prime ell dividing a factor has v2(ord_ell(p))=t+j+1 and hence v2(ell-1)≥t+1. Therefore every protected odd q with v2(q-1)≤t avoids sigma_k(n) and has valuation k v_q(n) in the reduced denominator. For n,m in F_k, denominator equality recovers their entire odd parts. The remaining factor 2^a is uniquely recoverable since sum_{j=0}^a2^{-kj} strictly increases, including a=0. As 1≤R_k(n)<2 for k≥2, fractional-part injectivity follows. All n=1 and even n included. Read the frozen exact verifier and independently checked bounded cases for five k; finite checks are only corroborating.

## originality

PASS

Best-of-knowledge PASS for the explicit protected-prime valuation and restricted-domain injectivity for every even k. Defant 2015 covers density and gaps of a range, not one-to-one fibers; Sun OEIS A001157 records an unproved unrestricted distinct-fractional-part conjecture; OEIS A017667/A017668 contain reduced tables but do not establish this all-even-k family. The modular-order calculation is classical and receives no independent novelty credit.

## value

PASS

The result proves a meaningful infinite subclass of a named unresolved injectivity conjecture with no bound on prime support or Mersenne-type exponents, and a stronger exact denominator-reconstruction law. The chosen restriction is motivated precisely by disjoint numerator/denominator prime residue classes, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
