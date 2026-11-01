# Independent mathematical audit

## correctness

PASS

PASS: With rank 1/2 for neighbors and 3 for unmatched, a matched endpoint can improve by at most one; a two-blocking edge therefore has both endpoints unmatched and favoring each other first. Encoding cycle-edge occupancy e_i and local order o_i makes the only forbidden window (e_{i-1},e_i,e_{i+1};o_i,o_{i+1})=(0,0,0;1,0), in addition to adjacent occupied edges forbidden. The explicit six-state de Bruijn-style transfer matrix tracks (e_{i-1},e_i,o_i), assigning z to newly occupied e_{i+1}. Its trace T(z)^n counts every labeled profile/matching pair once, without quotienting rotations. The independent exact symbolic determinant equals lambda^4((lambda-1)^2-4z), hence trace T^n=(1+2sqrt z)^n+(1-2sqrt z)^n. Binomial expansion and division by 2^n yield each size coefficient and total expectation. Independent direct rank-difference brute force for all profiles and matchings for n=3..8 agreed, but the universal theorem comes from transfer bijection and characteristic polynomial, not these finite cases.

## originality

PASS

PASS: Fanelli and Moscardelli introduce rank-k blocking and study existence and convergence, including cycle-related dynamics but no annealed full matching-size law. Random stable-roommates and cyclic multi-sided matching literature uses different graphs or preference distributions. The exact polynomial at fixed two-neighbor cyclic acceptability is not in the inspected primary results.

## value

PASS

PASS: The simplest non-bipartite acceptability graph has a canonical binary preference law, but 2-stability creates local forbidden configurations whose number varies by matching size. The complete all-n exact annealed polynomial separates cardinalities and gives a precise exponential total expectation, refining mere existence/dynamics results. The six-state transfer reduction is a motivated reproducible structural argument, not a relabeling of the classical ordinary matching polynomial or a disconnected tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
