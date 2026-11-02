# Independent mathematical audit

## correctness

PASS

Classify ordered solutions A_a to x²+y²+z²=b, B_a to 2x²+z²=b, and diagonal C_a to 3x²=b. The ternary and binary finite-field base counts follow from the standard quadratic Gauss sum, including p dividing b. For p odd, all nonsingular solutions lift with p² or p choices per modulus level; if p divides b the only singular residue tuple is all zero. Its branch is absent unless p² divides b and then contributes p³ A_(a-2)(b/p²) or p² B_(a-2)(b/p²), including a=2 boundary via A_0=B_0=1. For C_a use the standard odd-prime square-root valuation formula and handle p=3 separately by first dividing 3x²=b. Inclusion–exclusion removes triple-coordinate coincidences: N=(A-3B+2C)/6, since the remaining ordered triples have six free permutations. Unit targets for p>=5 yield the displayed exact quadratic-character bias. For support, p>=7 lower bounds and explicit p=5 base counts give a nonzero distinct triple for each mod-p b; lift a nonzero coordinate to every prescribed higher-power target. For p=3, q=3 has unique subset with b=2; nine explicit distinct triples cover every b mod9 and lift to arbitrary 3-powers. No claim for 2-powers or general composite moduli.

## originality

PASS

Classical quadratic representation counts and the distinct-coordinate inclusion–exclusion sieve are credited. The assessed addition is one exact depth-decreasing distribution formula for all target residues of every odd prime power, including singular targets and the complete support law; known general upper/lower bounds do not by themselves provide this full exact answer.

## value

PASS

The object—the pushforward of the uniform three-element subset distribution by the quadratic sum on a finite local ring—is natural in additive combinatorics and coding. The exact count at every singular and unit target, distinct-input corrections, and support classification are meaningful finite arithmetic invariants; singular prime-power behavior and the exceptional p=3 case are not recoverable by a trivial finite-field substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
