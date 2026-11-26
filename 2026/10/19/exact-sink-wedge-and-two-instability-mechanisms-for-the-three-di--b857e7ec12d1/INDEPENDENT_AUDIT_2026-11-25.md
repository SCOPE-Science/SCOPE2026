# Independent mathematical audit

## correctness

PASS

The shift forces the alternating coordinates. Subtracting the two recurrence equations gives (u-v)(u+v+Q)=0; the nonzero factor branch leaves h=(u-v)^2/4 and gives exactly one unordered orbit for h>0, with no exceptional division. Writing D=delta^2, the two-step derivative has trace 1+E-D-4h, principal-minor sum E and determinant D. Independent stability replay: map lambda=(1+s)/(1-s) and clear denominators. The ascending cubic coefficients are 4h, 2(1-E+2D+2h), 4(1-D-h), 2(1+E-2h); the Routh determinant (a2*a1-a3*a0)/8 is (1-D)(1-E+2D)-4Dh. The two upper bounds force h<1-D, because W_flip is at most 1-D for E<=1-2D and W_NS is at most 1-D for E>=1-2D. Positivity is therefore precisely the stated sink strip and width bounds. At the flip boundary division by lambda+1 gives lambda^2+(E+D)lambda-D, strictly Schur in the strict flip case (endpoint sums 1+E and 1-E-2D); at the other boundary the complementary factor to lambda-D is lambda^2-((E-1)/D)lambda+1, with strictly nonreal unit roots in the stated strip. At equality the pair coalesces at -1. The square completion E-1+2D=(sigma+delta)^2+(3delta-1)(1+delta) gives the exact dichotomy and puts both real interface roots inside the strip for 0<delta<1/3.

## originality

PASS

The inspected same-family work establishes the fixed-point period-doubling origin and observes both motivating losses numerically, but not the all-parameter primitive-two return-spectrum wedge and exact interface. Do not credit the map, the fixed-point flip locus, or the qualitative numerical observations as new.

## value

PASS

The natural family and two observed exit mechanisms predate the calculation. The result replaces single-orbit parameter surveys with an exhaustive existence and attraction criterion, locates an exact contraction cutoff between possible mechanism types, and identifies the exceptional double multiplier. A researcher studying higher-period origins or local boundaries needs the precise wedge rather than just the fixed-point flip locus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
