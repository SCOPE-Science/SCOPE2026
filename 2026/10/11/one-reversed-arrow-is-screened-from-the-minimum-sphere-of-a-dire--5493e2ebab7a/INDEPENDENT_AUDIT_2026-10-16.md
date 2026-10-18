# Independent mathematical audit

## correctness

PASS

At the assigned exact tree read RESULT.md and verify.py. Reconstructed the signed root-gram matrix G with diagonal 2, consecutive entries -s_i s_{i+1}, zero otherwise. For a one-arrow reversal the positive weights p_i=lambda i(L+1-i)/2 on the two surviving runs, p_j=0, sum to 1 by the cubic identity S/12, and satisfy (Gp)_i=lambda outside j, (Gp)_j=lambda(m-1)/2. Thus p^T Gp=lambda, every vertex has squared norm 2, and the weighted center c gives maximum squared distance 2-lambda. The weighted squared-distance averaging identity establishes minimum and uniqueness for every competing Euclidean center. The flipped vertex gap is lambda(m-3), hence contacts all m vertices at m=3 and exactly m-1 otherwise; position monotonicity follows from S=(m+1)(m(m-1)-3(j-1)(m-j)). Independently rebuilt rational incidence vertices and tested all 322 (m,j), m=3..25, with exact arithmetic; all center/weight/contact/gap identities held. The all-integer claim follows from algebra, not finite extrapolation.

## originality

PASS

Numata, Takahashi and Tamaki Example 5.2 states that any oriented Dynkin A path produces a simplex, but Section 5 gives combinatorial faces, not Euclidean Chebyshev radius or strict contact screening. General root-polytope dissection or canonical circumsphere statements do not solve the smaller active-set minimax sphere when its flipped vertex is screened. A related Resultary cycle-root screening result concerns different graph and two screened contacts, not this all-length one-reversal path formula.

## value

PASS

The metric effect of changing just one orientation in a directed-path root simplex is a natural structural perturbation: an otherwise extreme vertex ceases to support the unique minimum sphere for every m>=4. The complete exact contact transition, reversal-position dependence and center formula provide an explicit nontrivial family benchmark for finite-dimensional Chebyshev-ball and root-polytope geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
