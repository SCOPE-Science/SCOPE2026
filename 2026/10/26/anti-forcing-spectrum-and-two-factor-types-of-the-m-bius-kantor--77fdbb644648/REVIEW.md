# Review of the Möbius–Kantor anti-forcing census

## Correctness
PASS. The adjacency specification is an eightfold rotation of the standard generalized Petersen presentation. Two independent perfect-matching enumerations return 33. The exact subset recurrence computes minimum feedback-arc sets for all 33 contracted digraphs. A second deletion-and-acyclicity search on the three proven symmetry-orbit representatives agrees. Explicit arc-disjoint directed-cycle packings of sizes 4, 5 and 5 match the upper bounds. Exhaustive adjacency-preserving bijections determine 96 graph automorphisms and orbit sizes 3, 6 and 24. `mk_antiforcing_verify.py` executes all tests and returns `VERIFY_OK`.

## Originality
PASS, with residual literature risk. The 2014 original anti-forcing article establishes the alternating-cycle criterion and a planar minimax theorem, not the nonplanar Möbius–Kantor census. The full HTML of the 2016 extremal article was inspected: its general bound \(\operatorname{Af}(G)\le r(G)\) and polygonal-chain spectra do not imply the exact values here. The 2025 matching-polynomial study reports 33 perfect matchings but the obtainable material does not exhibit anti-forcing values. Relevant research-record queries found matching-complex results on the same graph but not the asserted anti-forcing polynomial. The inaccessible sections of the 2025 article and unindexed earlier computations remain explicit risks.

## Value
PASS. The Möbius–Kantor graph is a canonical smallest cubic symmetric graph that is not distance-transitive; a complete matching-stability distribution on this graph is a natural finite benchmark. The exceptional three-element orbit has a structural characterization by complementary cycle type, and the exact cycle-packing equality tests a planar-source minimax phenomenon outside planar hypotheses. The classification concerns the full matching space, not a selected arbitrary slice.

## Remaining scope limitations
This result covers only the indicated 16-vertex graph; it does not prove a general nonplanar minimax principle. The completeness of the available literature comparison is limited by source access and indexing.

Self-review: passed. Independent audit: not yet performed.
