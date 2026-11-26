# Independent mathematical audit

## correctness

PASS

Let M₀=diag(M_U,M_W) and v=e_a+e_b. The signed coefficient matrix is M₀+t vvᵀ, positive definite since every anchor is positive. Since M₀·1=K·1 and vᵀ·1=2, direct substitution gives z=1−2tM₀⁻¹v/[1+t vᵀM₀⁻¹v]. The bridge split makes vᵀM₀⁻¹v=1/A+1/B, giving the frozen coordinate formulas. Each rooted Green column is positive by the diagonal-splitting series and connectedness, with strict maximum at the root by the killed averaging equation. The signs are therefore the signs of AB−t[2Bh_i−(A+B)] and the counterpart on W. The bracket can be positive only on the weak-anchor side, first and most strongly at its root. There the opinion is zero at t* and negative strictly above it; if A=B or an individual bracket vanishes, no finite negative opinion occurs at that vertex. The common t-factor increases strictly; every nonempty negative set is a strict superlevel set, and each nonroot vertex in it has a neighbor at strictly greater level. Strict ascent reaches the root and stays within the set. This works for singletons and cyclic components. In the unequal-anchor three-vertex example at t=3, multiplication of the proposed vector (−1,−2,6)/9 by the full signed system gives its exact anchored right-hand side. Replay: RESULT.md lines 38–98 and verify.py lines 11–76, 79–149. The frozen 4,550 rational instance-strength checks and six benchmarks were inspected as evidence, not rerun or treated as a universal proof. The result is about a static reversible-sign threshold in the specified one-bridge perturbation, not transient trajectories, directed edges, or arbitrary innate opinions.

## originality

PASS

Signed FJ equilibrium inversion, switching and positive-edge rank-one responses are established. The surviving claim is the exact effective-anchoring criterion together with the one-sided rooted connected sign filtration and sitewise thresholds on all allowed bridge graphs, not rank-one inversion or the equilibrium model alone.

## value

PASS

The smallest topological edit connecting two initially unanimous communities asks a concrete structural question: whether hostility can produce dissent and where it first appears. Effective anchoring separates topology from individual anchor magnitudes, including a reversal with uniform anchors; the exact t thresholds tell when each vertex joins a nested connected set without a sweep over signed systems. This is useful interpretation and an exact benchmark beyond the known inverse formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
