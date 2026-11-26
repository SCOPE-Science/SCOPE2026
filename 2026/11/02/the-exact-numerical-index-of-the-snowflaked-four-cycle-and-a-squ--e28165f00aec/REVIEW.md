# Independent mathematical audit

## correctness

PASS

For 1<t<2 the primal extremes are the signed six molecules and the dual is the twelve-half-space polytope in the record. At a norming pair, convex decomposition into extreme points retains the equality pairing on every constituent with positive weight, so the numerical radius really is the maximum of the stated extreme-pair evaluations. Independently generated dual vertices from the signed incidence rows by Cramer's rule, checking whole feasible intervals from the affine slacks; there are 18 affine vertices and no extra isolated interior intersections. Affine slacks also give exactly 28 positive norming pairs up to simultaneous negation. Generating the signed functional orbits at the separating parameter 3/2 gives sizes 8,8,4,8,8,4,4,4,2,4 in the record's representative order, covering all 54 sign classes. This extends throughout the open interval by the continuous dihedral action on the distinct affine vertices. Each of the ten tensor identities was cross-checked using the independently generated vertex and pair lists: after multiplying by t^4 the entries have degree ≤5, and exact evaluations at 1,2,3,4,5,6 coincide. Thus the largest dual certificate cost is max(3−t, (−t³+2t²+8t−8)/t³). For both test operators independently checked their two attaining evaluations by clearing denominators and comparing at five integers, and all 112 inequalities 1±A_j(T) ≥ 0 on the required intervals. After multiplication by t² for T_A and t³ for T_B the latter numerators have degree ≤4, with cubics recovered and checked by exact interpolation at 0,1,2,3,4. Their cubic Bernstein coefficients are all nonnegative on [1,2] for T_A or [sqrt(2),2] for T_B, using integer arithmetic in Q(sqrt(2)); the cubic controls on [l,r] are f(l), f(l)+(r−l)f'(l)/3, f(r)−(r−l)f'(r)/3, f(r). The branch difference is (2−t)²(t²−2)/t³ and its derivative at sqrt(2) is (2−sqrt(2))²>0, so taking reciprocals leaves a genuine slope jump. For the endpoints, the dual balls are the convex hulls of the limiting vertex lists by compactness and the inclusions (s/t)K_t ⊂ K_s ⊂ K_t for s≤t. The limiting norm inequality holds since each limiting norming pair remains a norming pair, whether extreme or not. At t=2 C=1 and v≤||·||. At t=1, all dual extreme points are integer by unimodularity of the signed incidence rows; checking all integer feasible dual points in {-1,0,1}³ gives v(T_A)=1 while (0,−1,−1)(T_A m_0)=2. The endpoint formulas thus do not require an unproved general continuity assertion.

## originality

PASS

The distinct verified content is exact operator optimization over the symmetric interior four-point metrics, most notably the second branch and the switch at sqrt(2) without a change in the affine vertex combinatorics. The facet census, individual endpoint facts and a scalar formula coinciding after reparameterization for a different metric do not constitute the same invariant for this family.

## value

PASS

This is an exact operator invariant for a natural interpolation from an equilateral metric to a square graph. The change in which certificate gives the optimum, at a differentiable-metric parameter with constant dual vertex count, separates the operator optimization from the face census. The two sharp operator families and the nontrivial interior threshold are usable benchmarks for higher-dimensional Lipschitz-free numerical-index questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
