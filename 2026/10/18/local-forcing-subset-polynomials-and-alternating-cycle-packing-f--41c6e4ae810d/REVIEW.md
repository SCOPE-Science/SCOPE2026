# Independent mathematical audit

## correctness

PASS

Independently enumerated all bijections from the eight even to the eight odd vertices, retaining only cube edges (272 matchings). For each matching, contract its eight matched pairs and direct an arc i→j for the unmatched edge from the even endpoint of i to the odd endpoint of j. Directed simple cycles correspond bijectively to alternating cycle edge sets, with rotation removed by starting at the least pair index. Vertex masks on matched pairs suffice for packing; different cyclic orders on the same mask are kept in the edge-set count. By switching a missed cycle, and conversely decomposing a symmetric difference, a subset is forcing iff it hits every such mask. Tested all 69,632 subsets and used recursive packing on the available pair set. The 384 bit-flip/coordinate permutations exhaust cube automorphisms: once origin and unit neighbors are fixed, every vertex is determined by its distances to these five vertices. Group action gives eight orbits, with all six table entries reproduced on each and the totals (2552,7040,6080,2176,272). The packing spectrum is 4:232, 3:32, 2:8; all forcing numbers are 4. The eight packing-two matchings therefore give the claimed sharp gap of two. The frozen scripts and certificate were inspected, not executed.

## originality

PASS

The justified distinct content is the degree-five and degree-six forcing-subset census and the edge-set alternating-cycle/vertex-packing profiles, including the sharp gap and its multiplicity. The total matching count and the uniform forcing number are established. Another indexed record has exactly the eight orbit sizes and all degree-four coefficients, so those alone cannot carry originality; its anti-forcing results are not the packing table. The distinct overlapping entry's later catalog date is not an inference about priority.

## value

PASS

The four-cube is a small test case for the gap between forcing and vertex-disjoint cycle packing outside the planar setting. The exact census shows that the common forcing number hides different numbers of certificates and different packing behavior: 40 matchings have a strict gap, with a sharp gap two in one orbit. Together with the higher-degree subset counts, this gives useful benchmarks for forcing and packing methods, beyond recomputing the uniform forcing number or the known c4 column.

The dated certificate retains the supplied scientific assessment, sources and limitations.
