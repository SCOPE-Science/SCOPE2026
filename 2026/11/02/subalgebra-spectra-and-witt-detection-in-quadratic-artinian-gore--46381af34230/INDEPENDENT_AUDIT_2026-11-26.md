# Independent mathematical audit

## correctness

PASS

This verdict is for the repaired finding. The frozen final enumeration and asymptotic statements are true, but its proof as written gives the wrong nonsplit isotropic-line count in RESULT.md line 44: at q=3,d=4 it gives 8, rather than 10. The replacement derives the correct (q^r+1)[r−1]_q by counting quadratic zeros when adjoining a hyperbolic plane, starting in anisotropic dimensions 0,1,2. This restores the orthogonal-quotient incidence recurrence for all odd prime powers. A unital subalgebra decomposes as scalars plus a subspace of the maximal ideal; if it contains z, its projection is unrestricted, otherwise it is a graph over a totally isotropic subspace with q^k possible functionals. Uniform constant-factor bounds on the two counts give quadratic envelopes with centers d/2 and (d+1/2)/3. Nearest admissible integers and summable Gaussian upper tails yield base-q logarithms d²/4+O_q(1) and d²/6+d/6+O_q(1), their probability ratio, and concentration at two distinct dimension scales. The even and odd centered benchmarks follow from dominated convergence of the normalized Gaussian coefficients. Independent direct multiplication-closure enumeration over all 2,664 subspaces of the five-dimensional maximal ideal per form at q=3,d=4 gave split (1,49,112,130,40,1) and nonsplit (1,31,40,130,40,1), ruling out the erroneous line count. Replay: python3 /workspace/branches/5227000b-aad4-4e76-8b7f-773471c37a7d/bounded_q3_d4.py. The frozen script was inspected, not executed; no bounded test is used to establish the asymptotics.

## originality

PASS

The frozen combined originality claim fails for the complete enumerator and Witt detection, which have direct earlier coverage. The replacement expressly credits that coverage and retains the sharp fixed-q socle-avoidance exponent and conditional dimension shift as the distinct result. The ordinary subspace-centered limit is a benchmark, not an independent originality claim. The inspected stronger exact enumerator supplies the starting counts; the repaired conclusion additionally identifies and compares two different dominant dimension regimes with uniform error bounds. No equivalent statement or stronger asymptotic theorem was substantiated in the inspected sources.

## value

PASS

The repaired result quantifies how often a uniformly sampled subalgebra misses the canonical socle and shows that the conditioned measure changes its typical dimension by an amount proportional to d. It compares two intrinsically defined subalgebra classes of an entire natural family, gives a sharp exponent including its linear term, and holds across both Witt types. It does not rely on rebranding the already covered enumerator or claiming the standard Gaussian-binomial baseline as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
