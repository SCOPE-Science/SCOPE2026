# Independent mathematical audit

## correctness

PASS

For equal-length primitive p,q with pq a proper power, Echi et al. Proposition 4.1 forces an odd exponent d>=3 dividing length ell and primitive period a=2ell/d. Two potential partners q1,q2 of a fixed p yield two periods a,b of p. For distinct odd d,e>=3, ell >= a+b-gcd(a,b) follows by 2/d+2/e-2/lcm(d,e)<=1; Fine–Wilf makes gcd(a,b) a period. Since the underlying primitive roots each have length a or b and occur in p, this would force both to equal the gcd, contradicting d!=e. Equal exponent gives identical prefix primitive root and therefore the same partner. Rotation conjugacy makes adjacency symmetric; Theorem 4.2 counts ordered pairs, hence edge count is half its sum. Independent enumeration produced ordered-edge counts 2,12,56 for binary lengths 3,6,9 and 6 for ternary length 3, all max degree 1. The infinite statement rests on Fine–Wilf, not finite enumeration.

## originality

PASS

PASS with caveat: Echi–Khalfallah–Kroumi Theorem 4.2 already counts all ordered pairs and bijectively parameterizes them by primitive roots. This claim does NOT assert that count as new. It proves a global at-most-one-partner property for each vertex via comparing two competing periods; no such fixed-vertex uniqueness is stated in the inspected full primary PDF. Related primitive-product surveys and Resultary matching records found no implication of degree<=1. Because the pair parametrization is precise, a folklore immediate partner uniqueness may exist; this is an explicitly retained risk.

## value

PASS

PASS: The natural relation among equal-length primitive words is structurally a disjoint union of isolated vertices and edges. This is a complete global-degree classification not entailed by the total edge count alone; it allows the existing pair-count formula to be interpreted as exact incident-vertex/edge counts and controls exceptional partners rather than only their abundance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
