# Independent mathematical audit

## correctness

PASS

A local round has multiplier (1-alpha*h_i)^E and center coefficient one minus that multiplier. The strict individual stability interval makes the mean round multiplier strictly contractive. Comparing normalized center coefficients at the limit for every center vector gives equality exactly when all F_E(alpha*h_i) agree. F_1 is constant. For even E>=2, F_E strictly decreases on (0,2): the geometric-sum derivative is positive in u=1-z both for u>=0 and, using even parity, for u<0. For odd E>=3 the branch z<1 has values above 1 and strictly decreases, whereas z=1+t, 0<t<1, has values below 1. Its derivative has the sign of E*t^(E-1)+(E-1)*t^E-1, strictly increasing from -1 to 2E-2. Hence three levels of curvature are impossible and distinct equal distortions require 1<alpha*a<alpha*b<2. For rho=b/a in (1,2), put x=alpha*b-1 and y=(x+1)/rho-1. The equality is x^E-rho*y^E=rho-1; the left side is strictly increasing (derivative E*(x^(E-1)-y^(E-1))) and its values at x=rho-1 and x=1 bracket rho-1 strictly. This rederives uniqueness and excludes the endpoint rho=2. Since 0<y<2/rho-1<1, the exact identity gives x^E -> rho-1, hence E*(1-x) -> -log(rho-1) and the synchronized multiplier tends to -q*(rho-1). The cubic rule follows by factoring the difference of 3-3z+z^2. The two witness fixed points and multipliers agree with independently iterated exact rational local steps.

## originality

PASS

The affine map and surrogate curvature distortion are already known, and comparing all center coefficients is a direct application of that surrogate formula. The distinct result is the full parity/level-set classification on the individually stable interval, including the sharp curvature-ratio obstruction, unique tuning and the asymptotic. The strongest inspected surrogate theorem and neighboring records give no covering theorem for these claims.

## value

PASS

The uniform-in-centers formulation isolates when an ordinary local update schedule does not distort the minimizer, rather than exploiting an accidental symmetric set of centers. The sharp obstruction at a curvature ratio of two, impossibility for three curvature levels, unique tunable exception and its precise stability-boundary approach answer a meaningful fixed-step question in an established scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
