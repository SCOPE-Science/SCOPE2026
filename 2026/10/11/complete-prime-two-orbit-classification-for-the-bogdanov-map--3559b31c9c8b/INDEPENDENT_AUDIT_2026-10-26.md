# Independent mathematical audit

## correctness

PASS

Independently reconstructed the exact least-two equations from x_next=x+Y. For p0=(u,-d), p1=(v,d), d=v-u≠0, the two Y updates lead to E1=d(2+epsilon+mu*u)-k*u(u−1)=0, E2=−d(2+epsilon+mu*v)-k*v(v−1)=0. Their independent difference is d[(k+mu)S−k+4+2epsilon], and sum equals −1/2[(k+2mu)d²−kS(2−S)]. Because d≠0 and sum/difference are invertible, the two constraints are fully necessary and sufficient. Exhaustive case splits on k, k+mu and k+2mu yield generic R>0 one orbit, R≤0 none; at μ=−k/2 and k≠0, S=0 or S=2 produce exactly two reflection lines only at stated ε; at μ=−k and k≠0, required ε yields d²=S(S−2) and the Möbius-invariant smooth hyperbola; at k=0 the equations force μ=0, ε=−2 and a global involution. The two d signs encode the same 2-cycle. Excluded origin/(1,0) are exactly F-fixed points on special curves. All nonfixed points on special curves satisfy F²=id; differentiating along smooth invariant curves gives multiplier 1. Independent SymPy derives the sum/difference constraints, computes F on each curve and verifies pointwise F²=id plus the global involution, using exact arithmetic. Finite examples corroborate, not substitute for universal reversible derivation.

## originality

PASS

Best-of-knowledge new parameter-wide classification of all real least-period-two orbits of the exactly defined Bogdanov map. The primary 2004 full text analyzes a local flip curve and numerical bifurcations, not the complete global solution for all (k,mu,epsilon). The 2011 full text is a numerical basin study at one parameter point. A contemporary full HTML study treats a two-parameter homoclinic-tangency problem. Full mathematical text of the 1993 introducing paper was inaccessible and remains a concrete historical-priority risk, not affirmative coverage. The exact published Resultary mirror is the same assigned finding and therefore not independent prior work. A distinct Resultary finding on invariant-measure covariance proves equality rigidity onto period-two dynamics but does not classify locations or the parameter locus of all two-cycles. No inspected external result was found to imply the census; failed searches alone are not novelty proof.

## value

PASS

The full period-two orbit locus of the standard three-parameter quadratic Bogdanov map is a natural dynamical invariant with direct relevance to period-doubling continuation and singular bifurcation boundaries. Explicitly identifying exactly when the number changes from zero/one isolated orbit to uncountably many, and discovering the two reflection-line continua plus a Möbius-involution hyperbola, is a motivated complete parameter classification rather than a textbook generic flip threshold or arbitrary parameter experiment. The two algebraic constraints provide a concise exact description valid even at singular denominator parameter values. Identifying the common global involution and proving a unit tangent multiplier gives structural information useful when analyzing perturbations; no larger general theorem or paper-sized result is required for this exact natural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
