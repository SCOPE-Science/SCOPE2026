# Independent mathematical audit

## correctness

PASS

Independently reconstructed the Pappus graph directly from the specified LCF list: 18 vertices, 27 edges, degree 3 throughout. Built reduced Świątkowski d3 columns from signed e_plus−e_reference boundaries in weight three, yielding 6528 degree-three columns and 16524 degree-two rows. Fetched the ACTUAL 68KB artifacts/kernel_basis.json and verified all seven integral vectors lie in the exact d3 kernel, with strictly increasing distinct highest nonzero columns 4641,5841,6217,6353,6360,6481,6512 giving integral/rational independence. Independently recomputed rank(d3 mod 3)=6521 by sparse Gaussian elimination on all 6528 columns (27970 pivot reductions, completed). Thus dim_Q ker(d3)=7 by simultaneous upper/lower rank bounds, C4=0, and ker d3⊂free Z^6528 is free; therefore H3(B3(P);Z)=Z^7. Unlike a claimed rank from logs, both certificates were checked from actual package data.

## originality

PASS

Best-of-knowledge: Maciążek–Sawicki gives the Świątkowski graph-configuration model and worked families including wheels, K_{3,3}, K_{2,p}, not the Pappus graph; PDF full search “Pappus” none. Resultary also returns three-particle homology for Heawood, theta and graph matching/independence complexes of Pappus, not a computation of H3 of unordered three points on Pappus. No explicit or stronger published result was found implying the precise rank-seven integral top homology.

## value

PASS

The Pappus graph is a canonical 18-vertex cubic incidence graph; its three-particle unordered configuration space is a natural graph-braid invariant. An exact integral top Betti number with a replayable independent rank/kernel sandwich supplies a useful datum for topology and quantum statistics on this graph, rather than an arbitrary graph-label computation. No claim is made to the complete homology ring or other particle weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
