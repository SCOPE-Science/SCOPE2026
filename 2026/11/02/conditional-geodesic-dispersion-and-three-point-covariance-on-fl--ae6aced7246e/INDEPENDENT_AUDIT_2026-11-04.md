# Independent mathematical audit

## correctness

PASS

For deck generators (x,y)→(x,y+b),(x,y)→(x+a,−y), the intrinsic squared distance from anchor P=(0,v) to Y=(x,y) equals min[x²+A_y,(a−x)²+B_y], with A_y=dist(y−v,bZ)² and B_y=dist(y+v,bZ)². Since |A_y−B_y|<=b²/4<=a², integration over x uniform in [0,a] of the positive part gives a²/12+(A_y+B_y)/2−(A_y−B_y)²/(4a²). Writing h={2v/b}, the circular squared-distance correlation is exactly h²(1−h)²/3; I independently integrated the two polynomial branches symbolically. Consequently m(v)=(a²+b²)/12−b⁴ h²(1−h)²/(12a²). Conditional independence of D(P,Y)²,D(P,Z)² given P makes shared-endpoint covariance Var(m(P)). The exact quartic beta moments 1/30 and 1/630 yield Var(h²(1−h)²)=1/2100, so covariance=b⁸/(302400a⁴). Pair overlap counting yields the stated finite-n U-statistic variance, and the nondegenerate bounded Hoeffding projection yields sqrt(n) CLT with variance b⁸/(75600a⁴). Boundary a=b/2 included; no claim for a<b/2 or ambient distances.

## originality

PASS

Flat Klein quotient geodesic and spectral literature supplies deck transformations and global geometry, but not the anchor-dependent mean-square distance quartic, its nonzero three-point shared-anchor covariance or the aspect-ratio inversion. A one-pair marginal cannot determine shared-endpoint dependence. Resultary semantic search for this conditional covariance and Klein geometry returned only unrelated distance or triangulation results. Novelty remains qualified against unindexed specialized stochastic-geometry computations.

## value

PASS

The nonhomogeneous Klein bottle has a mathematically natural nonconstant conditional distance profile absent on a flat torus; the exact strictly positive shared-endpoint covariance is a metric-space statistic that recovers aspect ratio given area. It controls the leading sampling variance and CLT for the pair-distance statistic. This is a coherent analytical three-point invariant, not a made-up numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
