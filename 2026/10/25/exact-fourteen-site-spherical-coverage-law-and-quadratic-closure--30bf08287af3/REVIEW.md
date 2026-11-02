# Independent mathematical audit

## correctness

PASS

PASS. Signed coordinate permutations give 48 congruent spherical chambers with x>=y>=z>=0. In coordinates (x,sqrt(1-x²)cosφ,sqrt(1-x²)sinφ), area element is dx dφ; ordering requires φ>=L(x), and diagonal-support threshold requires φ<=H_c(x). Multiplication by 48/(4pi)=12/pi yields the exact distribution integral with appropriate endpoint handling. Minimizing C uses b_i=|u_i|/c∈[0,1] with Σb_i<=sqrt3 and Σb_i²=1/c²; convexity and vertex classification give max Σb_i²=1+(sqrt3-1)² at the 24 signed permutations of q(1,r,0), where r=sqrt3-1. A Taylor expansion at each isolated minimizer yields the coercive piecewise-linear local function max(-A t,B t+E|z|); the exact sublevel triangle/trapezoid area is (1+B/A)^2/(BE)=1/[q^5 r²(1-r)], producing the 24/(4pi) prefactor. Distinct caps have disjoint interiors for angular radius <=half arccos(1/sqrt3), giving F(c)=1-14(1-c)/2=7c-6 for c>=c0. Differentiation cos(rho*-delta) gives angular coefficient 6/[pi q³(1-r)]. Independently coded 1D quadrature at c=.82,.85,.88,.9,.95 matched 120000 direct random sphere directions within 0.0031; onset at eps=1e-4 gave coefficient 38.9368 versus 38.8842 predicted. Finite numerical comparisons support, but do not prove, the uniform local asymptotic or exact integral.

## originality

PASS

PASS with best-of-knowledge qualification. Fowler–Tarnai–Gáspár (2002) already identifies the identical equal-radius cube–octahedron 14-site configuration, antipodal coverage transition, approximate covering radius 36.2060°, and intermediate numerical coverage, all excluded from novelty. Its public full text was inspected; the inspected paper derives and tabulates covering configurations/numerical values rather than the complete exact fixed-site uncovered-area CDF and local quadratic coefficient. General random-center sphere-coverage laws by Bürgisser–Cucker–Lotz do not directly describe these deterministic sites. General Voronoi algorithms could reconstruct the same distribution, but a computational method without an explicit demonstrated implication is not automatically the claimed exact formula.

## value

PASS

PASS. The specific 14-point compound is a published canonical antipodally constrained covering configuration, not an arbitrary set of directions. Its exact all-threshold uncovered-area law and gap-closure exponent/coefficient give meaningful accuracy beyond the known covering radius and numerical near-covering values, and can calibrate geometric covering algorithms and local perturbations. The linear disjoint-cap regime and quadratic local gap regime provide complete sharp asymptotic benchmarks; no global optimality among other 14-site configurations is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
