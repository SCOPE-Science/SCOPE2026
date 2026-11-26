# Independent mathematical audit

## correctness

PASS

The classification and TAR table survive unchanged in /workspace/repairs/5/RESULT.md. A separate bounded computation constructed the lines as additive triples in F₂³, tried every subset, tested closed-neighborhood union and one-deletion minimality, and built all four geometric families independently of the minimality filter. Equality yielded 21,14,28,2 minimal sets and the full domination polynomial coefficients. BFS expanded exact frontiers as bitsets of configurations, with each permissible move a single bit flip. It verified the specific isolated families for k=4,…,7, the 21 stars at k=5, and reproduced the five rows (V,E,largest radius,largest diameter): (21,0,0,0), (245,210,1,2), (1176,2226,10,12), (3138,9674,11,14), (5532,23408,12,14); component sizes also matched. The all-source histogram at k=8 was 42 at eccentricity 12, 2156 at 13 and 3334 at 14. Replay: python3 /workspace/reproductions/heawood.py. Supplied checkers were inspected, not executed. Monotone addition up to the union of two minimal sets and containment for every single move prove the overlap-graph correspondence; every state in any larger budget can delete down to a minimal set of size at most seven, so connectedness at eight persists. No higher-budget metric claim is inferred. The repair also checks the contrary literature assertion directly: with ℓ={1,2,3} and p=4 in XOR coordinates, the three selected lines are {1,4,5},{2,4,6},{3,4,7}. Points 5,6,7 are private neighbors for those lines; for each selected point, its line other than ℓ and the line through 4 is a private neighbor. The six-set dominates and is minimal but not neat.

## originality

PASS

Pass for the surviving full minimal-set census, geometric six-set obstruction and metric/component portrait, with repaired attribution. The earlier projective-plane construction covers the minimum size and first-family construction, and Haas–Seyffarth accounts for the connectivity threshold conditional on the upper domination number. An earlier computer assertion on the same graph is actually false as stated; it does not provide a covering classification.

## value

PASS

The smallest projective-plane incidence graph makes the budget range canonical, from minimum size four through the first connected budget eight. The exact radii, diameters and geometric identities of isolates separate information that a generic connectivity threshold and a domination polynomial lose. The explicit non-neat six-sets also correct a specific published-preprint assertion by a short witness, independently of the computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
