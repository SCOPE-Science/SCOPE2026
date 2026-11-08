# Independent mathematical audit

## correctness

PASS

For real alpha,b>0 and t>=0, direct diagonalization of [[-b,t],[t,b t^alpha]] yields F=b+u for t<=1 with u[b(1+t^alpha)+u]=t^2, and the positive eigenvalue branch increases for t>=1. Implicit differentiation fixes the sign reversal at b^2=4/(alpha t^(alpha-2)((alpha-2)t^alpha-2)); the threshold is decreasing in t and terminates at alpha>4, b_c=2/sqrt(alpha(alpha-4)). The exact F(t)>F(1) comparison confines all positive backward overshoot to b>=const epsilon^(-1/2), 1-t=O(epsilon). The uniform square-root expansion there yields L(beta,s)=s(beta^2-1)/(4 beta^3)-s^2/beta. Its unique global maximum is 1/(100sqrt5) at beta=sqrt5,s=1/10; compactness and the vanishing beta->infinity envelope establish global limit and every maximizing-pair scale. Exact symbolic checks independently confirmed stationary and expansion identities; finite checker samples do not prove universality.

## originality

PASS

The previous universal exponent-four boundary and alpha=5,b=2 witness are explicitly credited. They do not imply the coefficient-dependent threshold or optimized critical 5/2 law. Search of alternate spectral-norm and moving-diagonal formulations plus the constant-diagonal quadratic-operator sources found no comparison proving that law; priority is best knowledge, not a certification.

## value

PASS

The failure mechanism at the sharp universal exponent-four monotonicity threshold is a natural quantitative follow-up; both the optimal overshoot coefficient and coupled divergent/vanishing optimizer scales define an intrinsic sharp onset in a canonical spectral-norm family. It is not a repackaging of the known single fifth-power example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
