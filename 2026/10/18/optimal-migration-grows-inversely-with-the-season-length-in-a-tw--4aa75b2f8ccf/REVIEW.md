# Independent mathematical audit

## correctness

PASS

After removing the common scalar shift, each season matrix squares to (1+m²)I. The determinant-one period product has half-trace 1+2m² sinh²(T sqrt(1+m²))/(1+m²); its Perron root gives the displayed exponent with the full-period divisor 2T. At m=0 the shift alone remains, and for m>0 monotonicity of sinh x/x gives strictly positive gain, bounded above by sqrt(1+m²)-m and tending to zero at infinity. This ensures a finite positive maximizer. With z=mT and u=T², the difference of the regular analytic arcsinh expression from z is divisible by u. Its scaled limit is g=(z-tanh z)/(2z²) with g(0)=0; Taylor control is uniform on compact intervals, and twice differentiable locally at the positive maximizer. The bound by 1/(2z) keeps the global optimizer in a compact region, and g(0)=0 excludes the origin. For h=2tanh z-z(2-tanh² z), the sign of h' changes exactly once on z>0 as sinh(2z)/z rises through 4; h starts at 0, goes positive, then tends to -infinity. Thus g has a unique strict maximum with g''(z*)<0. All global optimizers converge there, and local strict concavity of the scaled objective gives uniqueness for small T. Stationarity and the O(T²) derivative error give z(T)=z*+O(T²), hence the displayed O(T) and O(T³) claims. Mortality is an exact additive shift, and no decision at scaled equality follows from the leading coefficient alone. Replay `cd /workspace && python audit_checks/check_frozen.py 5` uses independent 65-digit matrix exponentials and a stationary point for each of four finite T values, including sample competitors z=0 and z=200, and yields z*=1.60611529880276736408814145, G=0.132487539446827390709040742. Finite numbers are corroboration; global uniqueness follows analytically.

## originality

PASS

The exact Floquet formula for the opposite-season model and fixed-parameter asymptotics are verified prior coverage and explicitly credited. The distinct claim is the globally optimized singular fast-season regime, with uniqueness and first coefficient. No equivalent of that result was located in the inspected sources; targeted external search was unproductive and not a priority survey.

## value

PASS

The natural decision variable here is the magnitude of a constant symmetric dispersal rate. Optimizing before taking the period limit exposes the nonuniform rate scale and order-T gain that a fixed-rate limit misses, with a precise leading survival boundary for mortality on the same scale. The optimization is global within the stated class but does not claim optimality among time-varying controls or stochastic persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
