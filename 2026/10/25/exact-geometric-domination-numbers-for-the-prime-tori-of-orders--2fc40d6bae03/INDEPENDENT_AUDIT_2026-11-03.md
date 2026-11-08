# Independent mathematical audit

## correctness

PASS

The exact statement is D_5=5 and D_7=6 for the affine F_p^2 torus under pair-line covering. For s<=4, at most s+C(s,2)(p-2) points are covered, giving 22<25 and 34<49. For a five-point set in F_7^2, a collinear triple leaves at most 4+7*5=39 external points covered (<44). For a five-point arc, the 10 secants each contribute 5 external incidences (50 total); among their 15 endpoint-disjoint line pairs at most eight are parallel because there are eight directions and each has at most two arc-secants. At least seven nonparallel intersections lie outside S and are at distinct points (at most two secants through any external point), so at most 50-7=43 external points are covered, whereas 44 are needed. The two displayed explicit witnesses were independently re-evaluated with exact modular bitmasks; their pair-lines cover all 25 or 49 points. A separately implemented complete enumeration of C(49,5)=1,906,884 five-subsets found no dominator; this checks the finite classification but is not the basis for the structural lower-bound proof.

## originality

PASS

Best-of-knowledge originality for two exact values in the same affine-torus geometric domination invariant as Aichholzer–Eppstein–Hainzl. That paper states general lower and upper bounds, plus four-point constructions for other orders, and asks for exact torus values; its inspected statements do not yield D_5=5 or D_7=6. No-three-in-line studies maximum point counts under a prohibition on collinearity, rather than minimum pair-secant domination. Projective 1-saturating-set surveys and tables concern PG(2,q), including the line at infinity; their tabulated parameters are not the affine covering number, and do not directly imply either exact affine value. Three Resultary semantic searches found no statement-equivalent or dominating published record. This is a bounded priority assessment, not proof of global novelty.

## value

PASS

The discrete-torus geometric domination number is the natural minimum size of a point set whose pair-secants cover the finite affine plane, and its exact evaluation is explicitly motivated as an open direction in the primary definition paper. The two first odd prime cases outside the composite four-point family have distinct sharp answers, D_5=5 and D_7=6, and p=7 requires a nontrivial forced secant-intersection obstruction. The exact pair supplies motivated finite calibration instances for incidence bounds, secant-cover algorithms and further classification; no general-prime breakthrough is claimed or required for these exact natural values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
