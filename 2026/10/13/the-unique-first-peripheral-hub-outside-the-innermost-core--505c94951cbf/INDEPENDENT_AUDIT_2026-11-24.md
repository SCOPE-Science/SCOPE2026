# Independent mathematical audit

## correctness

PASS

For a failure, the top core C has k≥2, at least k+1 vertices, and an edge to its complement. The endpoint of that edge in C has total degree at least k+1, so the unique leader h has degree at least k+2. But h has at most k−1 neighbors in C (otherwise C together with h has minimum degree k), and at most |V\C|−1 outside. Hence deg(h)≤|V|−3. Together these force |V|≥7 and at equality k=2, deg(h)=4 and |C|=3. Thus C is a triangle and h hits exactly one triangle vertex and all three other outside vertices. Any additional edge would make a cycle through h, contradicting its absence from the 2-core. The displayed graph realizes this bound; its automorphisms are exactly permutations of the three leaves and a swap of the two unmarked triangle vertices. Its orbit has size 7!/12=420. Independently derived the connected denominator 1,866,256 by decomposing a labeled graph according to the size of the component of vertex 0. An independent simultaneous-pruning enumeration of all labeled edge subsets through order 7 also returned no failures below 7 and exactly the 420 relabelings at 7, with the stated representative vectors. The size-one connected graph causes no failure (its lone vertex has core number 0).

## originality

PASS

The same triangle–hub–three-leaf graph and its 420-member labeled orbit are indexed in work on the degree/eigenvector-leader split. That is real witness-level overlap, but the exact coreness threshold and the assertion that this is the only first-failure class are not established by that different criterion. The broad core literature inspected provides the structural terminology and peripheral-hub phenomenon, not the finite boundary.

## value

PASS

The threshold answers when a conspicuous local hub can first be excluded from the densest core in a simple connected example. The proof characterizes all minimum counterexamples by a triangle plus a uniquely attached hub with three leaves; the exact orbit verifies that there is no other mechanism at the first order. This value is structural, not a claim about influence or spreading performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
