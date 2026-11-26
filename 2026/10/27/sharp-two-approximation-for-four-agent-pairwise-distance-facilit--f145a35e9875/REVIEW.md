# Independent mathematical audit

## correctness

PASS

Summing the distances of the two unselected agents to the nearer selected site gives the six listed costs. Contiguous median clusters suffice for the optimum on a line, and the three cuts have costs b+c, a+c and a+b; a solution with an unused facility cannot improve on the best cut. After reflection to a≤c, direct expansion reduces the numerator to a²+5ab+5ac+4bc+(a+b)min(a,b)+(b+c)min(b,c)+(a+b+c)min(a+b,c). For a≤b≤c and c≥a+b the deficit 2Z·OPT−N is 3a²+6ab+6b²; for b≤a≤c and c≥a+b it is 4a²+6ab+5b². Within either ordering, taking c≤a+b instead adds (a+b)²−c² to the corresponding deficit. The remaining ordering a≤c≤b gives 4a²+2ab+6ac+2bc+4c². These cover positive gaps including case ties and are strictly positive. For a=b=1 and c=L≥2 the first deficit is 15 and Z·OPT=6L+14, giving the exact nonattained limit 2. The packaged verifier independently enumerates the six report pairs on a bounded rational test set; it was inspected, not executed, and the continuum bound rests on the certificates above.

## originality

PASS

The lottery and general factor 4 are known. The closest indexed exact factor 2 for n=4 has only three occupied sites and therefore does not supply a sharp strict bound on four distinct reports. No inspected primary or indexed stronger theorem supplies that upper bound or nonattainment in the assigned domain. The pass concerns that supported finite-profile refinement only.

## value

PASS

Four distinct agents form the first two-facility case beyond one omitted agent; two omitted agents can interact through the sampled pair. An exact finite-population benchmark for the standard unmixed lottery separates its true small-instance guarantee from the population-uniform factor 4 and from the guarantees of mixtures. Strictness and the distant fourth agent's limiting obstruction are informative. The useful new component is the sharp upper analysis on the full positive-gap domain, not the coincident-profile lower bound or strategyproofness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
