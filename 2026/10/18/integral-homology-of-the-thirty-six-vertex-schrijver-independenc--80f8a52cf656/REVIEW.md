# Independent mathematical audit

## correctness

PASS

Independent replay (python3 replays/3_schrijver.py; output replays/3_schrijver.txt) generates the 36 lexicographic five-subsets avoiding adjacency including the wrap from 11 to 0, enumerates cliques of their intersection graph, and checks the full directed augmented face poset. All 1,519,600 nodes and 12,264,696 covers were accounted for; 759,796 pairs leave exactly the eight frozen critical masks, with dimensions 6 six times and 8 twice. Removing the empty face and freeing its matched singleton gives an acyclic matching on the nonempty faces: the induced subgraph is unchanged except that the edge to the empty face has been deleted. Forman's theorem then supplies the claimed CW model including one 0-cell. With no positive-dimensional cells below dimension six it is five-connected; the cellular differential vanishes over Z because there are no consecutive occupied degrees. This establishes the full reduced integral homology but makes no determination of the attaching maps S^7 into the six-skeleton.

## originality

PASS

The nearest inspected results concern the same stable-disjointness family but other subset sizes, excesses or graph-complex functors. No inspected statement covers the exact integral homology or this sparse homotopy-equivalent CW model at the 36-vertex parameter. This is a bounded comparison, not a priority conclusion.

## value

PASS

The excess-two stable Kneser sequence is itself motivated by the unresolved topology of its independence complexes in the cited family work. The next parameter after the nearby 25-vertex case has a complete torsion-free two-degree computation and a CW model that isolates the remaining homotopy question to two attaching maps. Those precise data are useful for comparing the family and for a future attaching-map calculation; they are not a routine inference from either the neighborhood complex or the preceding size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
