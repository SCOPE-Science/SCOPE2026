# Independent mathematical audit

## correctness

PASS

At round 1 the signature distinguishes the marked origin, identifies b by degree d+b and detects adjacency to the mark. Coordinate permutations preserve all signatures, so each (b,c) type is indivisible. From round t to t+1, in any fixed-b unreached class at most one type can have distance t+1; it alone sees a reached colour. All types at distance >t+1 have exclusively unreached neighbours, with d−b in the b+1 tail and 2b in the b−1 tail (zero-count tails are irrelevant), independently of c. Old colours prevent merging. The final two b=0 types at distances 2d−2 and 2d are still tied at 2d−3, including d=2; at 2d−2 all tails contain at most one type. No earlier equality could precede a later split. Root distance and degree are rooted-automorphism invariants and determine (b,c); coordinate permutations give transitivity on each type. The multinomial size and triangular count follow. The stronger proof statement about the full stabilizer is also sound: degree distinguishes 2e_i among the distance-two neighbours of e_i, and the difference of distances to 2e_i and to the origin determines x_i.

## originality

PASS

The supported distinct contribution is the full time-dependent partition and sharp round 2d−2. Do not credit eventual rooted orbit recovery as distinct for d≥3: the inspected same-day rectangular-grid result covers it. Its stable-colour proof does not control intermediate colours or imply the sharp lower bound. The date alone does not establish priority.

## value

PASS

This is a natural controlled family for distinguishing propagation from convergence. The formula tells exactly which types remain indistinguishable after any fixed number of rounds, and shows that orbit separation can finish two rounds before the distance-to-mark signal could reach the far corner. Eventual orbit identification alone does not give either fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
