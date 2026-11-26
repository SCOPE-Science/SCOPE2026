# Independent mathematical audit

## correctness

PASS

Reconstructed the finite proof: a candidate meets each closed neighborhood for domination and each pairwise symmetric difference for separation. These tests are necessary and sufficient. Every subset has one 18-bit mask; at fixed weight every legal adjacency is exactly a swap of one present and one absent bit, independent of their distance in Pappus. Read both frozen programs and their output; the C++ census generates all layers, while the LCF cross-check independently covers all code counts but only the k=9 and k=10 exchange graphs. A separately written program (not a run of the frozen code) checked the incidence/LCF isomorphism, exhausted 262144 subsets, found 52638 codes and none below size nine, and reproduced every code count, edge count and component size in the table. At k=9 it reproduced 1028 vertices, 3780 edges, two 514-vertex components with selected point counts 0–4 and 5–9, and the all-line and all-point centers. BFS from each code gave per-component eccentricities 4:1, 5:27, 6:81, 7:243, 8:162, hence radius four and diameter eight in each component. The incidence graph is self-dual via point (x,y) ↔ line (m=x,b=−y); this also explains the symmetry of the component profiles. Each k=10,…,18 was checked to have exactly one component. Replay: python3 /workspace/branches/26b49bef-4acf-427d-bec8-6353c7f4631b/independent_census.py; saved output is independent_census.out in that directory.

## originality

PASS

The supported distinct result is the exact one-extra-sensor threshold and census of the larger token-jump layers of Pappus. Two later indexed records contain substantial exact overlap at minimum size, including its geometry in one case; that subclaim is not exclusive to the frozen record. Neither comparison established coverage of the larger identifying-code layers. General graph/code bounds do not determine their component structure.

## value

PASS

An identifying sensor placement must preserve both domination and distinct signatures through each reconfiguration. The unweighted Pappus graph is a natural small symmetric test case in which optimal layouts separate into two geometrically structured regions. Computing the exact next layer and the remaining layers answers the operationally meaningful fixed-size question of how much spare capacity is needed to move between arbitrary valid placements; the answer is exactly one sensor. This conclusion is not just another count of minimum solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
