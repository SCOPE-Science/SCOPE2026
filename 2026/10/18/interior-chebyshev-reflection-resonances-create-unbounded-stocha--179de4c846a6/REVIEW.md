# Independent mathematical audit

## correctness

PASS

The stage recurrence with one reused sample reduces exactly to x->c+T_s(1-h lambda/s^2)(x-c). For s=5,h=25, lambda_±=(3±sqrt5)/4 the arguments are cos(pi/5), cos(3pi/5), giving r±=-1. With centers -1,+1 independent each outer step the increments have alternating signs and variance 4n from deterministic X0=0. The full-gradient average curvature 3/4 gives T5(1/4)=61/64 and F minimizer sqrt5/3, yielding E excess =3n/2+5/24. For q=(r_-²+r_+²)/2<1, synchronous L² coupling contracts; stationary mean/variance recursions give V=4(1-r_-)²(1-r_+)²/((2-r_--r_+)²(1-q)). Exact derivative gives both quadratic coefficients 1/50∓sqrt5/125 and 1-q=(h-25)²/25+O((h-25)³), so (h-25)²V->100. Independent SymPy evaluation reproduced r±=-1, the exact second derivatives and objective expectation. Interior bounds and off-resonance uniqueness checked by argument, not finite horizons.

## originality

PASS

Established stochastic RKC and Chebyshev polynomial stability do not by themselves state the joint interior negative-extremum criterion, independent two-center reflection variance growth or exact quadratic invariant-variance pole. The original convergence results use diminishing steps/other noise conditions, so they do not rule out this fixed-step resonance.

## value

PASS

This is an explicit counterexample to inferring stochastic mean-square stability from each scalar deterministic stability factor in the allowable open interval. Classification of simultaneous negative extrema and a sharp variance pole quantify a real algorithmic failure mode in a natural same-sample-across-stages implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
