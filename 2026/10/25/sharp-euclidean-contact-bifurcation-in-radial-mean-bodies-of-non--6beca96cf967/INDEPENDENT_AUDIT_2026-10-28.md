# Independent mathematical audit

## correctness

PASS

Uniform-point rectangle covariogram gives exit-distance density (1+q-2qz) dz on z in [0,1], with moments T^p (p+2-pq)/((p+1)(p+2)) for all p>-1 and log moment log T-1-q/2 at p=0. Branch profiles Phi_(a,b,p) and Phi_(b,a,p) cover all unit directions and strict dominance Phi_(a,b)>Phi_(b,a) for q<1 reduces minimum to short-major profile, maximum to long-major. Log derivative has numerator t²[(p+2)q-(p+1)q²]-s² with positive denominator; the short-major profile has a unique strict interior min at q_min. For p<=2 the square endpoint comparison and a>b show global max only at ±long axis. For p>2 define w=1-pq/(p+2), B=w^(-2/p)-1, H=q²/B; its logarithmic elasticity E=qB'/B increases strictly from 1 to >2 by convexity of w^(-2/p), so H has one interior maximum and defines A_*. Comparing Phi(a,b,p)(q)/Phi(a,b,p)(0)=sqrt(1+q²/A²)w^(1/p) yields exact max regimes and six-way tie at equality; unique oblique maximum before transition is larger derivative root. SymPy exactly checked derivative and p=4 radical q_*, H(q_*) and numerical A_*=1.180800485353. Finite samples do not prove the all-parameter monotonicity; analytic convexity does.

## originality

PASS

The radial mean bodies, covariogram formula and general convexity are prior Gardner–Zhang and Langharst. Langharst–Manui–Zvavitch Proposition 34 gives pointwise cube profile; published Resultary square theorem gives square-only angular extrema. Since anisotropic affine deformations do not preserve Euclidean circles, these statements do not directly determine the nonsquare Euclidean contact bifurcation. The 1998 Gardner–Zhang full original could not be accessed; an old rectangle specialization remains a priority risk.

## value

PASS

Euclidean radii are genuinely non-affine observables of the radial mean body, so the rectangle family is a natural anisotropic deformation of the previously classified square. The unique aspect-ratio coexistence transition and contact multiplicities across the full real p>-1 interval resolve meaningful geometry rather than a coordinate renaming; the p=4 radical is an exact benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
