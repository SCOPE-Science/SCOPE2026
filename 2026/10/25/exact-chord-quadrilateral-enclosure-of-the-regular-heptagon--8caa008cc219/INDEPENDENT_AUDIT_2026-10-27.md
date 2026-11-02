# Independent mathematical audit

## correctness

PASS

Each unoriented heptagon chord has normal angle j*pi/7 mod pi, yielding precisely 14 directed support normals, alternately support heights 1 and cos(pi/7). Sliding any feasible side to support never increases area; fewer-than-four side enclosures can be tightened by an additional allowed supporting line. Four normals in cyclic order yield a bounded intersection exactly when all four positive circular index gaps are <7. Four supporting halfplanes touch the heptagon, so edge lengths are nonnegative (possibly zero) and the exact shoelace/support formula A=sum[h_i h_next-(h_i²+h_next²)cos(g*pi/7)/2]/sin(g*pi/7) applies. There are 511 bounded quartets. The source interval certificate tests all 511 with 65-digit outward enclosures, 7 odd-index winners with gaps (2,4,4,4) and 504 strict losers, lower gap >0.025947319986; independent full high-precision enumeration of all 511 and optimizer reconstruction agreed. Exact winner area cos²(pi/7)[tan(pi/7)+3tan(2pi/7)] and ratio 1.258803773547..., equality exactly seven rotations. The finite exhaustive certificate is valid because geometric reduction proves no omitted continuum cases; high precision independent check alone is corroborative, not a substitute for rigorous interval certification.

## originality

PASS

The 2026 Vígh paper already reports a numerical regular-heptagon ratio around 1.2588; therefore the approximate benchmark is unequivocally PREVIOUSLY KNOWN and is NOT claimed new. The assessed remainder is an exact closed expression, certified strict comparisons for all 511 chord normal quartets, and exact sevenfold complete optimizer classification. Related minimum enclosing parallelogram results impose opposite-side parallelism and do not determine arbitrary four-normal optimal patterns. Priority of an unpublished exact finite enumeration remains a qualified risk.

## value

PASS

The heptagon is the first odd regular polygon beyond the known pentagon case in the chord-quadrilateral enclosure program. A rigorous exact sharp value with all seven equality directions supplies a mathematically usable benchmark and non-parallelogram optimality, turning a prior numerical observation into a certified exact finite classification. No unrestricted Kuperberg conjecture is claimed, and this modest exact fact can be valuable on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
