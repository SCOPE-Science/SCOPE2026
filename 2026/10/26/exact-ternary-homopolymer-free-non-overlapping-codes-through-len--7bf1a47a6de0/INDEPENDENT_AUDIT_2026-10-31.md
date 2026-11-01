# Independent mathematical audit

## correctness

PASS

Reconstructed all finite candidate words, tested both ordered prefix/suffix directions and self-overlap, and independently enumerated every inclusion-maximal clique with Bron-Kerbosch and all maximum cliques with an ordered complete branch-and-bound. For n=9, 342 valid candidate words, 121728 maximal cliques and exactly 12 cliques of size 24; direct word-level overlap and 12-element alphabet/reversal symmetry actions verify two six-element orbits. All eight n match pinned table. Branch exhaustiveness follows each clique has a unique strictly increasing vertex order and both algorithms prune only bounds incapable of reaching the current maximum. Finite complete classification; no n>9 assertion.

## originality

PASS

Existing work characterizes general maximal non-overlapping code constructions and considers bounded run lengths; the inspected 2025 primary paper gives construction families and bounds, but does not evaluate the exact size-and-all-optima and symmetry census for ternary no-repeat lengths 2..9. Earlier general maximal-code framework implicitly contains enumerability but not these computed values. Unrestricted length-five/six Resultary findings do not cover the distinct constrained objective. Best-of-knowledge originality is qualified, not an absolute claim.

## value

PASS

Ternary Smirnov/no-homopolymer constraints are natural in synchronization and sequence-storage codes. A complete small-length optimum plus number and symmetry classification of every maximizer is independently useful for testing constructions and distinguishing constrained from unconstrained maxima, not a mere normalized rewrite of published unconstrained table entries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
