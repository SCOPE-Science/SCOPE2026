# Independent mathematical audit

## correctness

PASS

For the explicitly labeled 5-vertex 6-edge house (4-cycle sharing an edge with a triangle), 12 primitive vertex-edge incidences yield all acyclic partial functional orientations. Independent brute force across all 2^12 primitive subsets, discarding reused edge/tail and directed cycles, obtains exactly 208 nonempty simplices and face vector (12,51,90,55). Using actual package toggle order (7,5,4,11,3,9,10,1,6,8,2,0), reconstructed matching has exactly 101 valid pairs; complete acyclic topological sort of 592 Hasse covers leaves precisely one 0-cell and five 3-cells. No 1- or 2-dimensional CW cells remain; all attaching maps land at the single 0-cell, proving wedge of five S3 integrally, not just homology over primes. Original verifier independently checks exact Laplacian characteristic det(L+xI)=x^5+12x^4+51x^3+90x^2+55x and boundaries mod 2,3,5; tree/forest count checks are corroborative.

## originality

PASS

The finite directed-forest/Morse complex for a house (roof) graph is not determined by prior graph-family homotopy theorems that apply to complete graphs, paths, cycles, or by generic Morse-complex connectivity/rigidity theorems. The exact wedge multiplicity five is sourced from exhaustive computation rather than asserted from Euler characteristic alone.

## value

PASS

PASS, bounded: The house (roof) graph is a canonical minimal mixed-cycle motif with a triangle and four-cycle sharing an edge; its directed rooted-forest complex sits beyond the classical path/cycle/complete-graph examples. Its exact integral homotopy (five 3-spheres), certified by a full 208-face acyclic matching rather than rank-only outputs, supplies a natural small test case for graph-Morse connectivity and directed-forest topology. This is not claimed to settle a family or to be a major quantitative improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
