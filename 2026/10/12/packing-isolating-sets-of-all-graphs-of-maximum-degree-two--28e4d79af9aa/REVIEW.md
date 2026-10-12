# Scientific review

## Correctness — PASS

The proof reduces simultaneous packing and edge isolation to an exact geometric restriction on consecutive selected vertices. Disjoint closed neighborhoods impose gaps at least \(3\); two consecutive vertices outside their union would form an undominated edge, forcing gaps at most \(4\). Endpoints of paths contribute independent slack from \(0\) to \(2\), and cycles are counted by marked cyclic compositions. The corresponding rational generating functions and component product follow bijectively. The full spectrum and unique \(C_5\) obstruction follow from elementary interval constraints, with all small boundary cases handled.

A standalone direct-neighborhood verifier checked \(221\) graphs and \(577328\) vertex subsets, including connected paths and cycles through \(17\) vertices and all disjoint-union component profiles through \(9\) vertices. These finite computations corroborate the general proof.

## Originality — PASS

The main June 2026 primary source treats exactly the same notion, proves existence for every tree, notes \(C_5\) as a counterexample, and establishes general NP-hardness. Its full text does not give the exact maximum-degree-two classification, all-solution generating functions or size distributions. The closest stronger-looking primary cycle theorem treats simultaneous distance-\(2\) domination and distance-\(2\) packing, which allows cyclic gaps \(3,4,5\). The present invariant excludes gap \(5\) and forbids \(C_5\), so that theorem does not imply this result. Database and both present/earlier-archive overlap searches did not locate a covering result. Alternate historical naming of vertex-edge packing remains a residual literature risk.

## Value — PASS

This supplies a complete first nonforest classification for the newly emphasized simultaneous packing-isolation property. Beyond the already-known \(C_5\) example, it proves that this is the *only* obstruction at degree at most two, describes all admissible sets, determines their contiguous cardinality spectra, and supplies exact bivariate generating functions and disconnected multiplicativity. The invariant is motivated by the recent comparative theory, rather than a parameter chosen after a calculation.

Self-review: passed. Independent audit: not yet performed.
