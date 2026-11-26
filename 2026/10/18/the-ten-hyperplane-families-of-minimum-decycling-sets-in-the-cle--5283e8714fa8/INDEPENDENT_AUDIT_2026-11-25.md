# Independent mathematical audit

## correctness

PASS

The 16 characters on the even-parity group are represented without repetition by supports of sizes 0, 1 and 2. The generators flip all but one coordinate, so the respective eigenvalues are 5, −3 and 1. Parseval and the induced edge count give e(U)=m²/4−3m/2+Σbᵢⱼ²/8. At ten vertices this exceeds the forest bound; at nine each bᵢⱼ is odd, so eight edges are necessary and a forest forces all |bᵢⱼ|=1. The five odd coordinate sums then have squares summing to 53; the three listed patterns exhaust the possibilities. Two majority counts of seven would overlap in at least five points, impossible for two halfspaces; in the 7,6,6,6 majority-count case, the two points outside the 7-point majority agree on four coordinates and hence on all five. Thus only a full halfspace plus one point survives. The halfspace induces a matching; the outside point has one neighbor in each edge by triangle-freeness, giving the subdivided star. For the exchange rule, cross-index adjacency at cost three requires neither omitted point to lie in the intersection. The degree is 7+4·4. When both omissions block a cross-index move, they agree on a third coordinate by parity; opposite that bit, choose an omitted point with the opposite values on the two original coordinates, giving a common neighbor. States from complementary halfspaces cannot have a common neighbor because its omission would have to miss both; a third-clique route of length three exists using any coordinate on which the two original omissions agree. Token slides occur along just the four matching edges per halfspace. At threshold four the inactive induced graph is pruned at degree at most one, giving precisely three rounds on these trees.

## originality

PASS

The supported distinct result is the complete geometric description of the optima and their exact exchange and slide structure. The numerical extremum and count were checked separately; the threshold-four equivalence is a reduction, not a separate new general theorem.

## value

PASS

A standard symmetric graph supports a natural comparison between its exact extremal structure and mobility of optimal configurations. The ten-family description explains all optima and the sharp contrast between isolated slide pairs, ten exchange components, and eventual connectivity; this is more informative than tabulating the extremal value or the number of forest faces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
