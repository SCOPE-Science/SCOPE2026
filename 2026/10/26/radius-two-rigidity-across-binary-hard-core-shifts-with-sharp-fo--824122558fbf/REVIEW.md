# Independent mathematical audit

## correctness

PASS

A local rule preserves X_k exactly iff all admissible input blocks of length k+5 output legal length k+1 words. For k=2 and k=3, nine and seven admissible input neighborhoods give respectively 512 and 128 Boolean masks; complete preservation enumeration leaves 23 and 9. Build labeled directed graph on legal 4-block contexts, determinize reachable context subsets and add the k-zero legality state. BFS exhausts all reachable states and either finds the shortest absent legal output word or certifies equality of every finite image word, hence surjectivity for the compact subshift. Independently reimplemented this full automaton and reproduced all histograms, 5 onto maps in each range and masks 96,258 at k2. For k≥4, a one at one input coordinate has at most one possible output 1 within its radius-two window (otherwise distance≤4 forbidden), forcing exactly zero map or one of five shifts for all k.

## originality

PASS

Fixed-radius self-maps and sharp forbidden-word horizons are not contained in the inspected S-gap structural/entropy literature; general finite automaton procedures are prior methods, while this exact family-level classification appears separately motivated and original.

## value

PASS

A complete fixed-radius cellular-automaton classification across the full infinite hard-core exclusion hierarchy is a natural symbolic-dynamics question. The 23/9/6 map count and nine-symbol minimal obstruction are meaningful complete finite-state invariants; the infinite k≥4 branch is proved structurally, not extrapolated from samples. These data help understand detection limits for constrained factor maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
