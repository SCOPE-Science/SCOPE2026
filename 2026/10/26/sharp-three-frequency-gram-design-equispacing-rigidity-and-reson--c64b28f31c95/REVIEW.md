# Independent mathematical audit

## correctness

PASS

The dx/2 normalization gives a real sinc Gram matrix of trace 3. My symbolic replay /workspace/review-evidence/gram.py, independent of the frozen checker, confirms the elementary-symmetric coefficient expansions and the two symmetric eigenvalue coefficients. With z=ε² and λ=z²y, the characteristic equation divided by z³ is analytic at z=0, and the derivative in y there is 2(3+t²)/3, bounded away from zero on the closed interval. Local analytic branches glue on a compact neighborhood; this gives a uniform C² expansion in t. The largest root tends uniformly to 3 and the nontrivial middle root is 2(3+t²)z/9+O(z²), by the principal-minor sum, so the constructed root is the least even at t=±1. Its rescaled limit 2(1−t²)²/[45(3+t²)] has a strict isolated maximum with second derivative −28/405 at zero. Evenness, strict concavity near zero and the positive gap away from it imply exact uniqueness, not just convergence of optimizers. At zero the antisymmetric root is 1−sinc(2ε), and the remaining roots follow by splitting the symmetric 2×2 block. Independently, dividing the small block determinant 2z²/45−2z³/315+O(z⁴) by its large root 3−2z/3+O(z²) gives 2/135 and 2/1701. For any positive ε, compactness attains the maximum, and trace 3 forces equality at 1 exactly at identity. The two positive adjacent gaps must sum to 2ε and be nonzero integer multiples of π. This gives precisely the stated lattice, m≥2, the parity criterion and the m=3 strict loss at t=0. No intermediate-aperture classification is implied.

## originality

PASS

Credit prolate asymptotics, the fixed equispaced spectrum, and the elementary orthogonality criterion as background. The distinct supported content is exact global, unique placement for every sufficiently small positive aperture in the continuous fixed-span three-node problem. Resonance is a simple complementary result, not sufficient by itself for novelty or value.

## value

PASS

The free middle frequency at fixed bandwidth is a natural stability design variable. Exact small-aperture rigidity and the sharp optimum cost answer more than a scale bound or fixed-node computation. The lattice of perfect-conditioning designs provides a concrete contrast, with an entire resonant family excluding symmetry. No claim is made that the small-aperture interval is maximal or that the uncovered intermediate design problem is solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
