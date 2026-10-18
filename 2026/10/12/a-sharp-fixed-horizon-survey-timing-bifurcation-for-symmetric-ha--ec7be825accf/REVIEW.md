# Independent mathematical audit

## correctness

PASS

For stationary symmetric two-state CTMC with jump rate lambda/2, the independent same/different indicators across lengths u and H-u have Bernoulli success (1+e^(-lambda h))/2. Fisher information for log(lambda) is f(lambda u)+f(lambda(H-u)), f(x)=x^2/(e^(2x)-1), continuous at zero. The inspected P2 and P4 derivative recurrence was independently recomputed with exact symbolic arithmetic: P2 coefficients are negative for degrees3..7 and positive for all >=8 by the quadratic tail; P4 degrees6..25 are negative and all >=26 have positive summands. Thus f and f^(4) each cross once; the proven derivative ordering gives a single midpoint maximum for T<=2a and two unique asymmetric maxima for T>2a, with short gap converging to the unique maximizer c. Independent T=2,3,3.2,4,6,10 grid tests corroborate, but the infinite proof is coefficient-sign/monotonicity, not numerical.

## originality

PASS

Michel 2018 full mathematical preprint gives the same interval information in a freely chosen equal-interval/asymptotic design, not a compulsory fixed-first/fixed-last, exactly three-observation constrained problem. Mehtälä et al. 2011/2015 discuss binary transition-rate sampling intervals and are highly relevant; their full text could not be read (OA/arXiv failed; authorized Oxford service returned vpn_disconnected). The currently accessible abstracts concern repeated or freely spaced observations rather than the exact sharp 2a constrained bifurcation. Best-of-knowledge originality PASS, explicitly contingent on the uninspected full text not containing a stronger fixed-horizon result.

## value

PASS

Three exact surveys with compulsory endpoints is a natural budgeted field-monitoring design. A sharp phase transition from midpoint sampling to two distinct asymmetric globally optimal schedules has direct mathematical and design interpretability; the long-horizon short-gap constant is precise and is not an arbitrary tiny instance. Conditions of known stationary symmetry and perfect detection are essential; it is a local-in-parameter information optimum, not an adaptive unknown-rate protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
