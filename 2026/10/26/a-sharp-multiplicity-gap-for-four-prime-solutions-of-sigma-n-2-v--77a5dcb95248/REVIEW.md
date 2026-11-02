# Independent mathematical audit

## correctness

PASS

The target exponent pattern is exactly (2,1,1,1). Write f(z)=(z+1)/(z-1), g(z)=(z²+z+1)/(z(z-1)); f,g and g/f decrease with prime z, so p=2 or 3 is too large, p>=11 too small, and p=5,7 lead to exactly five surviving (p,q) pairs. Squaring the largest prime s is impossible: reducing the full equation modulo s would force prime s to divide a product of three positive factors strictly smaller than s. For a square among the first three primes, monotone next-prime cutoffs leave exactly 21 third-prime triples, without bounding the last prime. Setting R=g(t)*f(u)*f(v) forces s=(2+R)/(2-R), and all six integral s>r are composite (559,249,63,63,32,39). The exact known witness has sigma=2822400 and phi=1411200. Independent rational arithmetic recovered five stop equalities, 21 triples and six composites. This is a global argument, not a finite search for n.

## originality

PASS

Broughan–Delbourgo (2013) classify sigma=2phi with at most three distinct primes and establish bounded-multiplicity finiteness; Broughan–Zhou (2014) treats related ratio equations. Those results do not imply emptiness of the first nonsquarefree omega=4 layer. OEIS A062699 already records 2011009, which is explicitly not asserted novel. Resultary semantic search found no same equation/exponent-shape theorem among returned records; this absence cannot prove novelty.

## value

PASS

The published solution is classified for at most three distinct prime factors; the next natural support frontier is four, and Omega=5 is exactly its first nonsquarefree layer. A global impossibility theorem together with the known sharp Omega=6 witness determines a motivated smallest multiplicity, not an arbitrary finite computational cutoff. The modular and rational-prime reductions give substantive structural elimination beyond table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
