# Independent mathematical audit

## correctness

PASS

An intra-part jump on K_(a,b) leaves opposite-neighbor proportions and type occupancy counts unchanged. For a move of type t from B into vacant A, with A_t=x and B_t=y beforehand, the utility gain is x/(a-1)-(y-1)/(b-1), which exactly matches the two changes in normalized binomial within-type counts. The mirror orientation is symmetric; any fixed agents just remove permissible transitions. Phi lies in [0,(a+b-2)/2] on a grid of spacing 1/lcm(a-1,b-1), so every strict increase moves at least one grid unit and terminates within claimed steps. Independently checked 10394 legal moves across four small parameter triples including nonregular graphs.

## originality

PASS

Narayanan–Sabbagh–Voudouris 2025 full accessible article gives potentiality on regular graphs with one vacancy (Theorem 5.1) and spider graphs (Theorem 4.8), expressly proposing bipartite topologies in Section 7. The nonregular K_(a,b) with a != b and both sides >=2 is neither a regular graph nor a spider, so the paper does not imply this new exact pair-count potential and cubic bound; balanced complete bipartite and star boundary are correctly excluded as prior-covered special cases. Distinct variety-seeking and swap games use different utilities/moves.

## value

PASS

Exact potential for a natural nonregular cyclic bipartite network extends known potentiality classes and gives a uniform polynomial bound independent of types and immobile agents, resolving a motivated game-dynamics gap in a setting explicitly proposed by the prior article.

The dated certificate retains the supplied scientific assessment, sources and limitations.
