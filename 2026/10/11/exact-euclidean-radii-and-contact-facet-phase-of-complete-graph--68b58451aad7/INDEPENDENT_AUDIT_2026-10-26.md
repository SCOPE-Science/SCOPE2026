# Independent mathematical audit

## correctness

PASS

For n≥3, K_n acts orthogonally transitively on all N=binom(n,2) edge coordinates. Average any feasible inball center over the group; convexity retains the same radius and makes the center q·1. The complete irredundant facet description has coordinate distance q, vertex-degree distance [1-(n-1)q]/sqrt(n-1) when n≥4, and odd-set size-s distance sqrt[(s-1)/(2s)](1-sq), s odd≥3. Balancing each decreasing upper-facet distance against increasing coordinate distance gives q_deg=1/[n-1+sqrt(n-1)] and q_s=1/[s+sqrt(2s/(s-1))]. The latter denominator strictly increases for s≥3; comparing the largest odd set with degree facets gives odd control at 3,5,7, tie at 4, and degree control at 6 and all n≥8. Active shrunken degree or global odd facet together with all coordinates≥r forces every center coordinate to equal r, proving uniqueness. The edge-incidence vertices are exactly matchings. At q·1 their squared distance is j(1-2q)+Nq². Its maximum over j=0..floor(n/2) is the upper envelope of j=0 and j=k; the branch q≥1/2 has minimum N/4, strictly larger than k-k²/N, so q=k/N is globally optimal. Strict convexity of max_j ||vertex-c||² implies unique circumcenter and, since q<1/2, exactly maximum matchings touch. n=2 is the unit segment. Independent LP optimized all ambient center coordinates and radius for n=2..9 using 626 facet inequalities; direct enumeration tested 3,734 matching incidence vertices and active facet lists; exact symbolic checks corroborated the denominators and circumradius simplifications. Finite checks are not used as the proof for all n.

## originality

PASS

Best-of-knowledge original sharp Euclidean metric classification for the full integral matching polytope of K_n in canonical edge coordinates. The complete published facet description, a general fractional matching circumball reduction, and adjacent John/spectral results were compared at statement-and-implication level; none establishes the inball competition, exact radical phase, both unique centers, and all outer contacts.

## value

PASS

The full matching polytope of a complete graph is a canonical high-dimensional combinatorial polytope, and the standard edge-coordinate Euclidean inradius and circumball are natural sharp metric invariants. The theorem gives both centers, both radii, all tangencies, and a finite exception/transition in which global blossom inequalities win only for n=3,5,7. This quantifies how odd-set facets, though plentiful, cease controlling the inball after a sharp threshold. The outer sphere also links exactly to maximum matchings. The special family is motivated by its universal role in matching-polytope theory; this is more than a restatement of the facet inequalities or a single tiny numerical test, even though the proof reduces to a short optimization once symmetry and all genuine facets are known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
