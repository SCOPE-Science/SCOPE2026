# One-landmark exchanges among the edge-metric bases of the Pappus graph

## Finding

In the Pappus graph, all 486 mixed edge-metric bases belong to one component under one-landmark exchanges. The component has 3,564 edges and every vertex has eccentricity five, so its radius and diameter are both five. The full exchange graph also has six components isomorphic to \(K_3\square K_3\), comprising the 54 pure bases, and has 3,672 edges in total. Restricting exchanges to replacements along edges of the Pappus graph leaves all bases isolated.

## Objects and prior basis classification

Use the eighteen-vertex incidence graph of points \(p_{x,y}\) and nonvertical lines \(\ell_{m,b}\) over \(\mathbb F_3\), with adjacency given by \(y=mx+b\). Label points by \(3x+y\) and lines by \(9+3m+b\) using the representatives \(0,1,2\). For a vertex \(s\) and an edge \(uv\), its distance to the edge is \(\min(d(s,u),d(s,v))\). An edge-metric basis is a smallest vertex set on which all edge-distance vectors are distinct. A token jump replaces exactly one landmark with an unoccupied vertex so that the resulting set is again a basis; a token slide requires the removed and added vertices to be adjacent in the incidence graph.

The edge metric dimension four, the census of 540 bases, and the following complete classification are prior results [1]. A point-only basis has two points from each of two distinct first-coordinate classes, and a line-only basis has two lines from each of two distinct slope classes; there are 27 of each type. A mixed basis consists of points \(p,q\) with distinct first coordinates and lines \(\ell,k\) of distinct slopes with \(\ell\cap k\) off the affine line through \(p,q\). The latter condition automatically rules out either selected line being the line through \(p,q\). There are 486 mixed bases. The earlier result also classifies the automorphism orbits of the bases, which is a different equivalence relation from connectivity by one-landmark exchanges.

## Proof

Every basis has zero, two, or four point landmarks. A token slide changes that number by one because every incidence edge joins a point and a line, so there are no token slides. For the same reason, a jump connecting two bases must keep the number of point landmarks fixed. In the point-only case, a jump cannot change the pair of occupied first-coordinate classes: each occupied class needs two points, and one exchange cannot remove both from a class. For a fixed pair of classes, each class has three possible two-element subsets and replacing one point changes precisely one of the two choices. Hence each pair of classes gives one \(K_3\square K_3\) component. The same argument for the line-only bases gives three more. These six components together have \(6\cdot 18=108\) edges and every vertex in them has eccentricity two.

For the mixed bases, the following finite enumeration determines all one-landmark paths, not merely the automorphism orbits. Generate the 27 unordered point pairs with different first coordinates. For each pair, choose one of the six affine points off its line and choose two of the three different line slopes there; take the two retained lines through the chosen point of those slopes. This generates every mixed basis exactly once, because a nonparallel line pair determines its intersection. Sort each resulting four-set by canonical label. Two states are adjacent exactly when they contain the same triple of labels. The exchange graph can therefore be reconstructed by listing all four triples of every state and joining all distinct states in each triple bucket. Distinct four-sets can have at most one shared triple, so a legal pair is counted once.

The mixed degree histogram from this enumeration is \(12:54,\;14:216,\;16:216\), giving \(\tfrac12(12\cdot54+14\cdot216+16\cdot216)=3564\) mixed edges. From every mixed state, take that state as layer zero and construct each subsequent layer as the neighbors of the preceding layer minus all states seen so far. The complete mixed layer histogram is:

| Successive layer sizes | Number of starting bases |
|---|---:|
| \((1,12,72,210,185,6)\) | 54 |
| \((1,14,83,203,183,2)\) | 216 |
| \((1,16,82,208,177,2)\) | 108 |
| \((1,16,90,196,180,3)\) | 108 |

Each row reaches all 486 states and has a nonempty fifth layer. This establishes mixed connectedness and eccentricity five for every mixed basis. Adding the pure components yields the full component and edge counts. The distance claim is a finite proof using the exhaustive state and path-layer calculation; no extension to larger incidence graphs is asserted.

## Verification

In the same directory, run `python3 verify_graph.py state_transition_certificate.json` and `python3 verify_geometry.py state_transition_certificate.json`. The first reconstructs the state family with graph breadth-first distances, enumerates all jumps, and obtains the layer histograms by breadth-first traversal. The second reconstructs the basis family with finite-field distance formulas and the geometric predicate, generates jumps by the shared-triple test, and computes all eccentricities via bitset frontiers. Both compare the complete state and jump lists with the certificate. Expected outputs are in `verification_graph.json` and `verification_geometry.json`. SHA-256 hashes of the state and jump lists with compact JSON serialization are `9c55045f90fe9a946ceec98c7caf4e7ce675c3c28bac63219649aabafb6ff74b` and `b4f09a77286c9916f88e733a5ddc10127e7109240af8774a1165f54ba92fd20d`, respectively.

## Relationship to prior work and limits

The classification and exact census of the bases are credited to [1]. In particular the pure component structure and absence of slides are direct consequences of that classification; they are stated here to give the full reconfiguration picture. The distinct claim concerns the mixed jump component and its exact distances. Neither the census nor the orbit partition alone gives the reachability or distances. The definition of vertex-to-edge resolution is standard [2]; ordinary vertex metric dimension for biaffine graphs [3] does not address the move graph studied here. These comparisons do not establish exhaustive bibliographic priority.

## References

1. *Geometric edge-metric bases and the complete edge-resolving polynomial of the Pappus graph*, Resultary record `2026/10/13/SCOPE-geometric-edge-metric-bases-and-the-complete-edge-resolving-poly--4aa71f8104c8`, [finding and classification](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-geometric-edge-metric-bases-and-the-complete-edge-resolving-poly--4aa71f8104c8/RESULT.md).
2. A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, [arXiv:1602.00291](https://arxiv.org/abs/1602.00291).
3. D. Bartoli, T. Héger, G. Kiss, M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, [arXiv:1706.06583](https://arxiv.org/abs/1706.06583).
