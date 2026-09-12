# 1458 symmetric 2-(36,15,6) designs spanning self-dual ternary [36,18,6] codes

## Statement of result

There exist at least 1458 pairwise-distinct symmetric 2-(36,15,6) designs whose
36x36 (0,1)-incidence matrices have GF(3)-rank exactly 18, and the GF(3)-row
space of every one of these 1458 designs is a self-dual ternary code of length
36, dimension 18, and minimum Hamming distance exactly 6, i.e. a [36,18,6]
code. The full set of incidence matrices is archived as
`artifacts/gs_designs/` (1458 files `gsdes18_*.txt`); the representative is
`artifacts/gs_designs/gsdes18_1000.txt`. The per-design rank and distance
certificates are logged in `artifacts/sweep_results.txt` (1458 lines, every
line `RANK 18 MINWEIGHT 6`).

## Context and motivation

The admitted target asked whether some symmetric 2-(36,15,6) design spans an
extremal ternary self-dual code of length 36 (dimension 18, minimum distance
12) inequivalent to the Pless symmetry code C(17) under monomial equivalence.
Four routes were tried: Williamson Hadamards (96 unique designs), Menon
difference-set designs in groups of order 36 (about 5900 unique designs),
Goethals-Seidel arrays with symmetric first block (2106 candidates), and a
search for designs inside C(17) itself (700128 weight-15 supports). No route
produced an extremal-spanning design, so the target is reported BLOCKED. The
Goethals-Seidel sweep instead produced this finding: 1458 of its designs reach
full rank 18, and every one of them has row-space distance exactly 6. This
converts the open target into a quantified extremality barrier: rank-18
spanning is plentiful, yet extremality fails uniformly across all examined
families (ranks 12/14/16 elsewhere; distance 6 in all 1458 rank-18 cases).

## Definitions

A symmetric 2-(36,15,6) design is a 36x36 (0,1)-matrix N with every row sum 15,
every column sum 15, and N N^T = N^T N = 9I + 6J, where J is the all-ones
matrix. Equivalently N = (J - H)/2 for a regular Hadamard matrix H of order 36
with row and column sums 6. The ternary row space (code) of N is the linear
span of its rows over GF(3). A ternary code of length 36 is self-dual if it
equals its orthogonal complement (hence has dimension 18); it is extremal if
its minimum nonzero Hamming weight is 12, the largest possible at this length.

## Result (precise headline)

At least 1458 pairwise-distinct symmetric 2-(36,15,6) designs have incidence
matrices of GF(3)-rank exactly 18, and each spans a self-dual ternary
[36,18,6] code: dimension 18 and minimum Hamming distance exactly 6.

## Proof and verification evidence

Design validity: every one of the 1458 archived matrices was re-verified with
exact integer arithmetic to be 36x36 (0,1) with all row and column sums 15 and
N N^T = N^T N = 9I + 6J. Rank: independent exact GF(3) row reduction gives rank
exactly 18 for all 1458 matrices (rank set {18} over the full set).
Self-duality: every row has weight 15 = 0 mod 3 and every two distinct rows
meet in 6 = 0 mod 3, so the row space is self-orthogonal (Gram matrix 0 mod 3,
checked directly); dimension 18 at half the length forces self-duality.
Distance: the rank-aware meet-in-the-middle verifier `artifacts/minweight36.c`
reduces each design to an 18x36 basis, systematizes it, and splits information
words 9+9 (19683 x 19683 packed pairs covering all 3^18 codewords) with
bit-exact GF(3) addition, excluding the zero word. Its core was calibrated by
reproducing the literature Pless-code values on `artifacts/C17_gen.txt` (rank
18, distance 12, weight distribution with A12 = 42840 summing to 3^18), so the
tool discriminates extremal from non-extremal codes. The verifier was rebuilt
from source and rerun on the representative and 13 further samples, all giving
`RANK 18 / MINWEIGHT 6`; the sweep log covers all 1458 files one-to-one with
`RANK 18 MINWEIGHT 6`. An independent Python meet-in-the-middle check on the
representative exhibits an explicit weight-6 codeword and exhaustively excludes
all codewords of weights 1, 2, 3, 4 and all 12063744 weight-5 words, proving
distance exactly 6 there. Distinctness: all 1458 file byte-strings have
distinct SHA-256 hashes and are distinct as matrices. No monomial-equivalence
or design-isomorphism classification is claimed.

## Limitations

Monomial (in)equivalence among the 1458 row spaces (and against C(17)) was not
tested; all share parameters [36,18,6] and self-duality, nothing finer.
Isomorphism classification of the designs was not done; distinctness is at
matrix/file-bytes level. Explicit weight-6 codewords are certified per design
by the distance log but listed explicitly only for the representative. The
broader suggestion that Goethals-Seidel/Menon/Williamson (36,15,6) designs
never span extremal ternary codes is a conjecture, not a theorem; only the
stated 1458-case classification at distance 6 is claimed as proved fact.

## Reproducibility

Compile `artifacts/minweight36.c` with `gcc -O2 -fopenmp -o minweight36
artifacts/minweight36.c` and run `./minweight36
artifacts/gs_designs/<file>.txt` for any archived design; expected output is
`RANK 18` followed by `MINWEIGHT 6`. Design equations and GF(3)-rank can be
rechecked with plain exact integer/numpy arithmetic: row/column sums 15 and
products against 9I + 6J, then row reduction mod 3. The sweep log
`artifacts/sweep_results.txt` records the per-file outcome for all 1458 cases.

## References

V. Pless, Symmetry codes over GF(3) and new five-designs, J. Combin. Theory
Ser. A 12 (1972), 119-142. S. Rukavina and V. D. Tonchev, Extremal ternary
self-dual codes of length 36 and symmetric 2-(36,15,6) designs with an
automorphism of order 2, arXiv:2209.13468 (2022). V. D. Tonchev, On Pless
symmetry codes, ternary QR codes, and related Hadamard matrices and designs,
Des. Codes Cryptogr. 90 (2022), 2753-2762. M. Harada and K. Ishizuka, Hadamard
matrices of order 36 formed by codewords in some ternary self-dual codes,
arXiv:2303.05056 (2023).
