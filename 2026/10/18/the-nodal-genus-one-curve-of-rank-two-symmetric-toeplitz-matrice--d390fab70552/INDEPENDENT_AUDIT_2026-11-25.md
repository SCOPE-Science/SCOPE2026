# Independent mathematical audit

## correctness

PASS

Reconstructed the arbitrary-size proof on the reduced projective rank locus (RESULT.md lines 24–55). The 3×3 principal determinant is (t0−t2)(t0(t0+t2)−2t1²). When the leading 2×2 block is invertible, the first two coordinates determine any column in its two-dimensional span; column 2 then equals column 0 in the periodic case or (2t1/t0)column 1−column 0 on the Chebyshev branch. The relation gives all later coefficients, not just the first three. If t0≠0 and t1=±t0, the principal minors on {0,1,j} are −t0(tj∓t_{j−1})² and force the rank-one sequences. If t0=0 and t1≠0, the leading determinant forces t2=0 and the invertible-block case applies. If t0=t1=0, a first nonzero coefficient at r≤n−3 gives an upper triangular rank-three minor; at r=n−2 the four indices 0,1,n−2,n−1 give a block off-diagonal matrix with invertible cross-block [[t_r,t_{r+1}],[0,t_r]], hence determinant t_r^4. Only the rank-two corner point at r=n−1 survives. Conversely the two-periodic matrices split into the constant and alternating outer products, the finite Chebyshev matrices split into reciprocal exponential products, and the corner has rank two. The homogenized Chebyshev polynomials give a basis of binary forms of degree n−1. The two components intersect only at u=±1, because their t0=0 representatives differ for n≥4 and the pulled-back equation t2=1 has simple zeros at ±1. Thus the local completed reduced union is the fiber product of two smooth one-dimensional complete local rings over k, an ordinary node. The standard union exact sequence subtracts 2 from the two rational Hilbert polynomials, giving degree n, polynomial nd and genus 1; the normalization is the disjoint union. No scheme-theoretic assertion about the minor ideal is needed. CHECK.py was inspected: its exact identities and six finite-field point checks would corroborate but are not the proof or a new execution.

## originality

PASS

The known n=3 conic-plus-line example, ordinary exponential/Chebyshev algebra, and rank-one Toeplitz families must be credited. The distinct finding supported by the inspected comparisons is the exact union for all n≥4 over an algebraically closed characteristic-zero field, including the periodic and corner cases and its global reduced nodal geometry. None of the available compared statements gives or mechanically implies that full result. This is a bounded judgment, not exhaustive priority.

## value

PASS

Rank two is a natural first nontrivial rank stratum in symmetric Toeplitz approximation and structured matrix geometry. The global classification identifies a separate periodic family and an exceptional projective corner that a generic finite recurrence alone misses; it quantifies the component intersections and arithmetic genus for every size. This is a complete description of a natural reduced feasible geometry, not a claim about radicality or an isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
