# Exact normalized census of C5-equivariant Latin squares of order 10, with sampled equivariant pair obstruction

## Context

Existence of 3 mutually orthogonal Latin squares of order 10 (3-MOLS(10)),
equivalently an orthogonal array OA(5,10) of strength 2, is the century-old
frontier after Euler and the proof that no projective plane of order 10 exists.
Unrestricted search is infeasible, so design theory proceeds by
symmetry-restricted censuses: each ruled-out autotopism type provably shrinks
the viable space for a putative triple. The natural first prime-order family is
the fixed-point-free order-5 autotopism acting as two disjoint 5-cycles (5+5
profile) on each of the five coordinates (rows, columns, three symbol sets).
No decision on this five-coordinate C5 profile was recorded: Egan–Wanless
classify MOLS completely only to order 9 with only the closest triple at order
10, McKay–Meynert–Myrvold scope symmetry differently, Parker (1975) excludes
autotopism group order 25 (not a single diagonal C5), and the Sloane OA
directory lists OA(100,4,10,2) but no OA(5,10).

## Definitions

Let sigma = (0 1 2 3 4)(5 6 7 8 9) on Z_10 and
g = (sigma,sigma,sigma,sigma,sigma) on Z_10^5.
A Latin square of order 10 is g-equivariant if its 100-cell symbol assignment
is invariant under g. Since g has no fixed codeword, such an array is a union
of 20 orbits of size 5. On (row,col) coordinates the group <(sigma,sigma)> has
20 orbits indexed (er,ec,d) with er,ec in {0,1} and
d = (c mod 5 − r mod 5) mod 5. A 20-tuple X of orbit values with
v = 5*s+b encodes the square via the twisted symbol action
sym(v,r) = 5*s + (b + r mod 5) mod 5. Row groups (orbits with fixed er) must be
permutations of Z_10; every column must be Latin. The symbol centralizer acts
transitively on values, so we normalize X[fix] = 0 for fix = (0,0,0).
A g-equivariant second square is orthogonal to the first iff its 20 cell orbits
use 20 distinct symbol-pair classes
(a//5, b//5, (a%5 − b%5) mod 5), hence all of them.

## Result (headline claim)

Under the diagonal fixed-point-free C5 action g above, there are exactly
2,082,000 g-equivariant Latin squares of order 10 normalized by X[fix] = 0
(20,820,000 un-normalized). Furthermore, each of 65 diverse normalized
specimens (25 sequential plus 40 independently randomized) admits zero
g-equivariant orthogonal mate, proved by 650 exhaustive mate searches over all
10 second-square fix values. The full C5-symmetric triple (OA(5,10)) question
remains open: closing it requires extending the mate verdict to all 2,082,000
squares (~35 single-core CPU-days; canonical reduction gave no compression).

## Proof / evidence

Census: plain-stdlib depth-first backtracking over the 20 orbit variables with
row-group all-different plus column-Latin propagation. Primary run
(census.py): group-0-first ascending order, 2,082,000 solutions,
152,574,172 nodes, ~306 s single core. Independent replay (replay_census.py):
group-1-first reversed order, descending values, FNV-1a checksum folded over
all solutions, 2,082,000 solutions, 68,844,351 nodes, ~142 s, checksum
13354815127498168480. Two disjoint traversal orders agree exactly.
Mate tests (pair_layer.py): per-(L1,yfix) exhaustive search enforcing
row-group permutations, column-Latin, and 20-class pair-orbit injectivity,
~41.5k nodes / ~0.15 s per run, 650 runs total, zero mates on all 65 specimens.
Independent audit reran all 650 mate searches to completion with zero mates and
verified all 65 specimens Latin with the group-permutation property.
Relaxation anatomy (supporting only): column-Latin-only 80/80 survivors,
orthogonality-only 80/80 survivors, joint 0/80 — the kill is their interaction.

## Limitations

Normalized count only (X[fix]=0); un-normalized total is 10x larger;
isotopism classes not enumerated. Pair obstruction covers 65 of 2,082,000
squares with no statistical extrapolation. Certificates are
backtracking-certified (two agreeing runs plus checksum), not DRAT/SAT
proof-logged. No claim about non-equivariant squares, other C5 embeddings, or
3-MOLS(10) in general.

## Reproducibility

python3 output/artifacts/census.py (expect 2082000, ~5 min);
python3 output/artifacts/replay_census.py (expect 2082000 + checksum
13354815127498168480); python3 output/artifacts/verify.py (Latin sanity);
python3 output/artifacts/pair_layer.py (single-specimen mate UNSAT demo);
python3 output/artifacts/batch_mates.py (sweep driver).
Archived transcripts latin_census.log / latin_census_replay.log with DONE lines.

## References

Egan–Wanless, Enumeration of MOLS of small order, arXiv:1406.3681v2;
McKay–Meynert–Myrvold, Small latin squares, quasigroups, and loops;
Wanless, Diagonally cyclic latin squares; Parker 1975, Nonexistence of a triple
of OLS(10) with group of order 25; Sloane OA directory (neilsloane.com/oadir);
Wanless MOLS data pages.
