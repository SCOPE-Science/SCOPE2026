# Independent mathematical audit

## correctness

PASS

For 0<p<2, each positive calibrated two-node rule has relative convex-body worst error exactly (1/2)||F−c_p||∞ by a thin-rectangle surface-area limiting argument. Testing normals perpendicular to either node yields min F≤min(w,1−w)|det(u,v)|^p≤1/2, while c_p=Gamma((p+1)/2)/(sqrt(pi)Gamma(1+p/2))>1/2. Thus error≥(c_p−1/2)/2 with equality forcing w=1/2 and orthogonality. For this rule F ranges [1/2,2^(−p/2)]; a=p/2 in (0,1), even-binomial sign expansion of ((1+t)^a+(1−t)^a)/2 and E|cos2θ|^(2k)≤1/2 show c_p is at least the midpoint of this range, hence the upper deviation is never dominant. The two sharp stability consequences |w−1/2|≤2ε and |u·v|≤sqrt(1−(1−4ε)^(2/p)) follow from the same test normals. Independently evaluated c_p and both angular deviations at seven exponents (.1,.4,.85,1,1.25,1.75,1.99); a finite sample does not establish the continuum result.

## originality

PASS

Congpei An arXiv:2609.05869 Theorem 3.2 already establishes the exact convex-body supremum as a potential sup norm, and Theorem 4.3 non-even-power nonexactness; these are expressly reused. Published Resultary 2026-10-11 all-N Cauchy quadrature proves the p=1 specialization; the present work explicitly claims novelty only for p≠1 in 0<p<2. The positive two-node all-exponent minimax optimizer, exact error and weights/angle rigidity are not entailed by nonexactness or the single p=1 case.

## value

PASS

Exact positive two-view minimax quadrature over the continuum of subquadratic cosine kernels is a natural budget-two geometric sampling benchmark. It determines optimal geometry, error, and quantitative near-optimal rigidity; differs mathematically from a routine substitution because the sign-controlled positive/negative discrepancy comparison varies with p.

The dated certificate retains the supplied scientific assessment, sources and limitations.
