# Order-10 orthogonal pair with semiregular order-3 autotopism (3+3+3+1 on all four coordinates)

## Context
The smallest order at which Euler's conjecture on orthogonal Latin squares fails is 10: Parker, Bose, and Shrikhande showed pairs of orthogonal Latin squares of order 10 exist, but the landscape of such pairs — and in particular which symmetries a pair can carry — remains incompletely mapped. Egan–Wanless exhaustively classify sets of mutually orthogonal Latin squares (MOLS) only for orders n ≤ 9, with a closest near-triple at order 10. Gill–Wanless count ~18.5M species of order-10 pairs satisfying non-trivial relations without classifying joint cycle-profile autotopisms. The Sloane orthogonal-array library records that some OA(4,10) exists (oa.100.4.10.2) without any symmetry annotation. Whether order-3 symmetry survives joint orthogonality at order 10, and which cycle profiles occur, is therefore an open natural classification question and a source of symmetric seeds for triple-extension attempts.

## Definitions
- A Latin square of order 10 is a 10×10 array over symbols {0,…,9} with each symbol once per row and column.
- An orthogonal pair (A,B) has all 100 superimposed pairs (A[r][c],B[r][c]) distinct; equivalently the 100 rows (r,c,A[r][c],B[r][c]) form an OA(4,10) (strength 2, 4 columns over 10 symbols).
- An autotopism of a pair is a 4-tuple of permutations (rows, columns, symbols of A, symbols of B) mapping the OA row-set to itself. A diagonal autotopism applies the same permutation σ on all four coordinates.
- Let σ = (0 1 2)(3 4 5)(6 7 8)(9), i.e. SIG = [1,2,0,4,5,3,7,8,6,9]. It has order 3 and cycle profile 3+3+3+1 (three disjoint 3-cycles plus one fixed point), the minimal-fixed-point order-3 action on 10 points.
- A square G is σ-equivariant if G[σ(r)][σ(c)] = σ(G[r][c]) for all cells; a pair is jointly σ-equivariant if both squares are. Any autotopism whose four components each have profile 3+3+3+1 is isotopic (by independent conjugation on each coordinate) to the diagonal (σ,σ,σ,σ), so fixing this generator loses no generality.

## Result
There exists an orthogonal pair of Latin squares of order 10 admitting a joint autotopism of order 3 with cycle profile 3+3+3+1 on rows, on columns, and on each of the two symbol sets. Explicit witness squares A and B (rows 0..9, symbols 0..9):

A =
1 4 3 7 9 2 8 0 6 5
4 2 5 0 8 9 7 6 1 3
3 5 0 9 1 6 2 8 7 4
5 6 1 8 7 4 9 3 0 2
2 3 7 5 6 8 1 9 4 0
8 0 4 6 3 7 5 2 9 1
0 8 9 3 2 1 4 7 5 6
9 1 6 2 4 0 3 5 8 7
7 9 2 1 0 5 6 4 3 8
6 7 8 4 5 3 0 1 2 9

B =
8 1 6 0 7 9 2 3 5 4
7 6 2 9 1 8 3 0 4 5
0 8 7 6 9 2 5 4 1 3
9 7 3 8 5 4 0 2 6 1
4 9 8 5 6 3 7 1 0 2
6 5 9 4 3 7 1 8 2 0
1 0 4 7 2 5 6 9 3 8
5 2 1 3 8 0 4 7 9 6
2 3 0 1 4 6 9 5 8 7
3 4 5 2 0 1 8 6 7 9

Both squares are Latin, each satisfies the diagonal σ-equivariance at all 100 cells, σ has profile 3+3+3+1 and order 3, and the 100 superimposed pairs are pairwise distinct (orthogonality 100/100). The forced fixed cell is (9,9) with value 9 in both squares.

## Proof / Evidence
Verification is deterministic and machine-replayable, independent of the randomized search that found the witness:
1. Cycle profile: orbit decomposition of SIG gives sorted lengths [1,3,3,3]; SIG^3 = identity.
2. Latin property: every row and every column of A and of B sorts to [0,…,9].
3. Equivariance: direct check G[SIG[r]][SIG[c]] == SIG[G[r][c]] for all 100 cells and both G in {A,B}.
4. Orthogonality: the set {(A[r][c],B[r][c])} has cardinality 100.
The independent verifier output/artifacts/verifier.py performs all four checks on output/artifacts/witness.json and prints INDEPENDENT_VERIFY_OK (replayed in audit). The construction route (equivariant Latin found in 38 nodes, symmetric mate in 5076 nodes via orbit-backtracking search, seed 4) is documented but not needed for validity. Auxiliary data: transversal counts T(A)=808, T(B)=952.

## Limitations
- The headline claims existence of a pair with the prescribed joint profile, verified above. It does not claim a complete census of such pairs, the full autotopism group beyond the exhibited C3 subgroup (not enumerated), or an exhaustive count of equivariant Latin squares admitting symmetric mates (only sampled).
- Full isotopism comparison against every catalogued Parker pair was beyond this lane's offline budget; novelty rests on the prescribed-profile gap in the consulted classifications (Egan–Wanless to order 9, relation-pair counts, Sloane OA tables), not on a fresh whole-corpus diff.
- The search script uses randomized orbit backtracking; witness validity is deterministic regardless of search randomness.

## Reproducibility
- Data: output/artifacts/witness.json holds A and B (plus construction metadata seed/nodes).
- Code: output/artifacts/verifier.py (stdlib only) replays all checks: `python3 output/artifacts/verifier.py` → `INDEPENDENT_VERIFY_OK`.
- Inputs: generator SIG = [1,2,0,4,5,3,7,8,6,9] on every coordinate; grids as printed above.

## References
- J. Egan, I. M. Wanless, Enumeration of MOLS of small order, Math. Comp. 85 (2016), 799–824; arXiv:1406.3681. https://arxiv.org/abs/1406.3681
- I. M. Wanless, Data on MOLS (catalogues to order 9; order-10 samples and relation-pair files). https://users.monash.edu.au/~iwanless/data/MOLS/
- M. J. Gill, I. M. Wanless, Pairs of MOLS of order ten satisfying non-trivial relations, Des. Codes Cryptogr. (2023), doi:10.1007/s10623-022-01149-6.
- N. J. A. Sloane, Library of Orthogonal Arrays (oa.100.4.10.2). http://neilsloane.com/oadir/
- B. D. McKay, A. Meynert, W. Myrvold, Small Latin squares, quasigroups and loops (counts to order 10). https://users.cecs.anu.edu.au/~bdm/papers/ls_final.pdf
