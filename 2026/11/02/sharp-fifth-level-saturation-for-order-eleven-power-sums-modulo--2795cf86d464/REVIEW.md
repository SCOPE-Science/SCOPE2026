# Independent mathematical audit

## correctness

PASS

Read RESULT.md and verifier source. For order-11 q, any ≤10-term vanishing sum corresponds to nonnegative degree≤10 polynomial g with total coefficient count ≤10. Since Φ11 irreducible, resultant R(Φ11,g) is nonzero integer |R|≤10^10 and p^k|R, reducing for k≥3 to p<2155, 29 primes ≡1 mod 11. Independently coded C++ sieve, Hensel root generator and complete stars-and-bars enumeration; scanned 31 full moduli ×352715 coefficient vectors=10,934,165, found only minimum 9 for p=23 at levels 3 and4, no ≤10 sum at 23^5 or all other p^3. Reduction from p^k to p^3/23^5 plus 11-term cyclotomic sum establishes every higher k, not extrapolation from finite range. The exact p23 sequence was prior; uniform all-prime assertion is assessed.

## originality

PASS

Jacob–Külshammer already define m(q,e), prove general tools, and tabulate p=23 order-11 sample m=3,5,9,9,11, so this exact sample and the generic resultant bound are NOT novel. The assessed all-prime order-eleven level≥3 exclusion and sharp uniform level-five classification require 31 exact modular searches not supplied by the inspected prior table. Breuer et al. and Resultary related cyclotomic results do not by cited statements imply this uniform cutoff; undiscovered exhaustive work remains a risk.

## value

PASS

Prime-power stabilization of shortest vanishing sums is a published arithmetic question. Proving a sharp all-prime exponent-five threshold at a fixed natural small order eleven, and identifying exactly the exceptional prime and levels, converts a generic resultant bound into a uniform sharp classification; independent exact arithmetic verifies finite remainder. It is specific to order 11 but not a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
