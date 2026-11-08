# Independent mathematical audit

## correctness

PASS

Reconstructed graph-burning timing: sources must be unburned at previous round end; legal iff d(v_i,v_j)>=j−i and radius-(k−i) balls cover the graph. Sum of ideal odd interval lengths is k²; k²−n=sum truncations+overlap excess, both nonnegative. Deficit 0 partitions arcs; deficit 1 forces a single clipped path end or one shared arc endpoint, with interior singleton overlaps forbidden by source legality. Permutations of distinct temporal labels yield k! square-path; cycle rotation yields n(k−1)!; at deficit 1 path overlap k!(k−1) plus 2(k−1)(k−1)! endpoint truncations, cycle overlap nk!; incident singleton junctions give redundant counts. Verified k=2 C3 and P3 boundary. Independent direct propagation enumeration checked k=2,3 and all 8 path/cycle-size combinations; finite checks are not the all-k proof.

## originality

PASS

Standard graph-burning radius characterization, path/cycle burning number, and square-order path nonredundancy are prior results. The complete labelled near-capacity count and final-source redundancy profile were not found in inspected 2026 primary article, survey, or published-finding semantic search. This is best-of-knowledge, not exhaustive historical priority.

## value

PASS

Natural exact enumeration of optimal contagion schedules at maximal and first submaximal coverage and an exact structural boundary between perfect tilings and one-defect configurations. The proportions quantify legally redundant interventions, not an arbitrary index or known table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
