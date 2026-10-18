# Independent mathematical audit

## correctness

PASS

The real unit ball of N(s,t)=max(|s|,|t|,(|s|+|t|)/sqrt2) has eight vertices ±(1,√2−1), ±(√2−1,1) with all sign rotations. The adjacent antipodal quadruple has zero centroid and two distances 2(√2−1), four distances2, yielding 40−16√2. For each of 8^4 ordered choices of sphere edges, the centroid equalities cut out a compact affine parameter polytope of rank1 or2; the objective ΣN(x_i−x_j)^2 is convex on each. Thus maxima lie at affine-polytope vertices, captured by fixing 3 (rank1) or 2 (rank2) parameters to endpoints and solving the rest. Exact Q(√2) source verifier fully inspected, including its exact comparison arithmetic and degenerate rank-one case, enumerates 4032 rank2 and64 rank1 cells and exactly 11136+576=11712 candidate occurrences. A separately coded independent floating-point full vertex-cell enumeration yielded the SAME counts and maximum 17.37258300203048=40−16√2. Independently evaluated 64 octagon-vertex pairs for C_NJprime=4−2√2. Since the exact source verifier uses rational-pair arithmetic, the finite certificate is exhaustive after convexity, not sampling.

## originality

PASS

The defining 2021 full text gives a lower bound J_in≥8+8C_NJprime and evaluates only square-type l1/l∞ planes, not regular octagon. A separate strictly convex planar equality theorem noted in the frozen scientific package excludes octagon because all eight boundary edges are flat; its hypothesis cannot be silently weakened. A known exact C_NJprime(X8)=4−2√2 would yield the lower bound, but not the missing four-point upper bound. No direct regular-octagon computation was verified in literature/indices, with Resultary outage retained as significant search limitation.

## value

PASS

The regular octagon is the standard flat, highly symmetric Banach plane lying outside strict convexity. Proving sharpness of the defining J_in–C_NJprime lower comparison on this boundary case is a mathematically motivated exact complete optimization, not an arbitrary slice; exhaustive algebraic certificate demonstrates that flatness does not force strict inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
