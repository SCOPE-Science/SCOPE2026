# Independent mathematical audit

## correctness

PASS

Exact induction shows u_n=T^{floor(log2(n+1))}(x); v_j=T^j(x) repeats 2^j times. Piecewise affine Φ(y)=4/5-y/5 obeys y+Φ(y)<=2Φ(Ty) on [0,1], equality on right tent branch. Telescoping with 2^-j weights gives B_K<=Φ(v_K)-2^-K Φ(x), then interpolation inside each block yields sum_{n<N}u_n<=(4N+x)/5. Upper sharpness: legal right-branch backward orbit z_-j=(2/3)(1-(-1/2)^j) has discounted average sum 2^-j z_-j=4/5; a dense forward orbit shadows arbitrarily long finite reversed segments at arbitrarily late times. Lower sharpness: arbitrary late shadowing of fixed point 0. Cesaro increments <=1/(N+1) ensure all intermediate limit points, and full tent Lebesgue ergodic map yields almost sure density and ordinary mean1/2. Independently checked rational sample recurrence and upper bound and geometric inverse branch sums. Finite verify.py tests not proof for every real x.

## originality

PASS

Gade-Bhalekar exact plateau dynamics and explicit warning delayed averages may differ are established. Read their accessible long HTML article sections 2-4 plus appendix context, distinguishing their model and qualitative statements from exact dyadic 4/5 accumulation interval. Search of published mathematical records revealed no matching sharp Cesaro law, but historic exponentially weighted ergodic optimization literature is a priority risk.

## value

PASS

Shows a natural time-change of chaotic dynamics destroys physical-time ergodic averages: almost every ordinary orbit averages 1/2 but its delayed orbit has entire [0,4/5] Cesaro limit set. Exact upper bound and extremizing backward history give structural signature of dyadic proportional delay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
