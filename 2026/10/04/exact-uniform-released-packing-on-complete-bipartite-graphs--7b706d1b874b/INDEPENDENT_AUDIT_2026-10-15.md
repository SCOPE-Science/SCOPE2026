# Independent mathematical audit

## correctness

PASS

PASS: For K_{a,b}, a,b>=1, integer 0<=f(v)<=u, constrain closed neighborhood only when f(v)=u. Separating four exhaustive side-saturation patterns gives T0=(a+b)(u-1), TA=au+min(b(u-1),k-u) and TB=bu+min(a(u-1),k-u) if k>=u, and TAB=min(au,k-u)+min(bu,k-u) if k>=2u; the overall optimum is the maximum of available terms. In each pattern the upper bounds are exactly saturated-side sum constraints and attainable by distributing allowed integer mass, with at least one saturated vertex where required. For example a=3,b=1,k=u=2 achieves 6 by (2,2,2;0). Independently exhaustive direct feasibility tests covered 297 parameter combinations for 1<=a,b,u<=3, arbitrary bounded k. The proof, rather than those tests, establishes all positive sizes and capacities.

## originality

PASS

Best-of-knowledge PASS: initiating paper defines conditional-at-upper-bound packing and studies graph examples, ILP and complexity; an existing review already finds a counterexample to a flawed observation, so novelty is not assigned to that falsity. The contribution is the exact uniform K_{a,b} classification. No parameter-dominating released biclique theorem located.

## value

PASS

PASS: The newly introduced released packing invariant has a nontrivial saturation-dependent optimization unlike ordinary packing. Complete bipartite graphs are a fundamental infinite dense graph family, and the exact four-pattern phase diagram both organizes parameter behavior and produces robust counterexamples to an initial global optimality heuristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
