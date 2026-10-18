# Independent mathematical audit

## correctness

PASS

For shape alpha>0 and arbitrary scale beta>0, the density standardized about its mean has support z> -sqrt(alpha). At symmetric common-support points |z|<sqrt(alpha), r=z/sqrt(alpha), the log ratio equals 2[(alpha-1)atanh(r)-alpha*r]. When alpha<=1 it is strictly negative for z>0. If alpha>1, atanh(r)/r is strictly increasing from 1 to infinity, giving exactly one root. Series atanh(r)/r =1+sum_{m>=1}r^(2m)/(2m+1) and coefficient comparisons with 1/(alpha-1) give 1<kappa_alpha<sqrt(3), with upper boundary automatic for alpha<=3. Expanding in alpha^-1 yields kappa^2=3-12/(5alpha)+O(alpha^-2), equivalently kappa=sqrt(3)(1-2/(5alpha)+O(alpha^-2)); as alpha decreases to 1, r tends to 1 and kappa tends to 1. Independent bisection found kappa(1.1)=1.0488088476, kappa(2)=1.3541151769, kappa(7)=1.6305749459, kappa(50)=1.7181466725, kappa(500)=1.7306646916; these are checks, not infinite proofs.

## originality

PASS

Best-of-knowledge new sharp global pointwise reflection-density classification and scale-free 1-to-sqrt(3) interval. Sun–Hu–Sun 2023/2024 investigate cumulative Gamma probability within one standard deviation, shape-dependent central mass and normal comparison, a different functional; directly reading its relevant results shows no theorem asserting equality of g_alpha(z) and g_alpha(-z) or the exact artanh root. The raw density-ratio computation is elementary, and an older note on Gamma skewness could already encode the crossing; no exact earlier source found. The mathematically substantive package is the all-alpha uniqueness, universal bounds, and two endpoint limits.

## value

PASS

The location at which a skew Gamma law changes which equal-distance side of its mean has greater density is a natural dimensionless symmetry profile, relevant to central-variation/normal-comparison questions. Identifying a single crossing for every shape >1 and sharp 1-to-sqrt(3) standard-deviation bounds is a complete parameter classification rather than an arbitrary numerical threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
