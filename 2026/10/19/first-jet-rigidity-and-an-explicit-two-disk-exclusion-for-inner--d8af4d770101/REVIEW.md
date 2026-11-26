# Independent mathematical audit

## correctness

PASS

For X=f(A+Bz), expansion of (1−X)^2(1−conj(X))^2 and inner boundary values cancel paired powers of f and conj(f). The only nonconstant Taylor coefficient of f that survives integration is f′(0), from the term f q² conj(q), whose only negative mode is −1; the f²q² term uses just its constant coefficient. Independent symbolic Laurent extraction gives the entire frozen quartic. The map q↦fq is injective and isometric on the boundary; coercivity follows from the reverse triangle inequality and equivalence of norms on the two-dimensional polynomial space. Strict convexity of the fourth power of the norm gives uniqueness. If f(0)=0 the mean-value lower bound is attained uniquely at q=0; if f is unimodular constant take q=1/f. Otherwise normalize to real u=f(0) in (0,1) and v=f′(0) in [0,1−u²] by phase and disk rotation. Conjugation invariance forces real minimizing coefficients a,b. When v=0 the phase symmetry in B gives b=0. When v>0, the odd b term favors b≥0; at a=0 the a derivative is negative, forcing a>0 by convexity on that slice, and then the b derivative at zero is negative, so b>0. At a=1 the derivative's verified decomposition is strictly positive for nonnegative b, because the (1−u)² term is positive and 1−u²−v≥0. Thus a<1. The other verified stationarity identity yields b[2(1−u²)+2(a−u)²+b²]=va², hence b<a²/2 strictly, also at the Schwarz–Pick endpoint. Therefore |a/b|>2/a>2. Zero and constant optimizers have no degree-one zero to which the assertion applies.

## originality

PASS

Uniform positive separation for degree-one inner-input OPA zeros is already established. The exact first-jet determination of the objective and the explicit strict separation beyond radius two were not found in the statements or implications examined. The new bound is not a claim of a new qualitative exclusion theorem or of a sharp constant.

## value

PASS

Quantifying the known uniform exclusion for the first non-Hilbert even exponent is a natural gap. The explicit bound places all the degree-one inner-input zeros strictly past the closed disk of radius two, rather than only keeping them away from zero. Separately, exact objective rigidity reduces the infinite inner-input family to two Taylor data and a constrained two-variable real optimization; that reduction can be used to investigate the optimal radius without choosing a concrete generator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
