# Kronecker-square fingerprints separate S_6-S_8 irreps up to sign

## Context

Whether a tensor square determines its factor is a recognized structural
question beside the Saxl tensor-square conjecture (which constituents appear
in staircase squares) and geometric-complexity / character-recognition tasks
(square-root uniqueness: recover chi from chi-squared data). Small-n exact
boundaries give checkable fingerprints and benchmarks for those methods.
The slice n = 6, 7, 8 (p(n) = 11, 15, 22 irreps) is the first consecutive
range with structurally nontrivial squares while staying fully exhaustive
and replayable in seconds.

## Definitions

- Partitions lambda of n index Irr(S_n) = {chi_lambda}.
- lambda^t = conjugate (transposed) partition; chi_{lambda^t} = sgn * chi_lambda.
- Write lambda ~ mu if mu = lambda or mu = lambda^t.
- Kronecker coefficient:
  g(lambda,mu,nu) = (1/n!) sum_C |C| chi_lambda(C) chi_mu(C) chi_nu(C),
  summed over conjugacy classes C with |C| = n!/z_mu.
- Kronecker-square vector: m(lambda) = (g(lambda,lambda,nu))_{nu |- n},
  coordinates in lexicographic partition order (ascending lists below).
- Lexicographic coordinate orders used:
  - n=6: (1^6),(2,1^4),(2^2,1^2),(2^3),(3,1^3),(3,2,1),(3,3),
    (4,1^2),(4,2),(5,1),(6).
  - n=7: (1^7),(2,1^5),(2^2,1^4),(2^3,1),(3,1^4),(3,2,1^2),(3,2^2),
    (3,3,1),(4,1^3),(4,2,1),(4,3),(5,1^2),(5,2),(6,1),(7).
  - n=8: (1^8),(2,1^6),(2^2,1^4),(2^3,1^2),(2^4),(3,1^5),(3,2,1^3),
    (3,2^2,1),(3^2,1^2),(3^2,2),(4,1^4),(4,2,1^2),(4,2^2),(4,3,1),
    (4,4),(5,1^3),(5,2,1),(5,3),(6,1^2),(6,2),(7,1),(8).

## Result

For each n = 6, 7, 8:

1. **Conjugate invariance.** m(lambda) = m(lambda^t) for every lambda.
2. **Separation, no exceptional collisions.**
   m(lambda) = m(mu) if and only if lambda ~ mu. Hence the p(n)
   square-vectors take exactly 6 (n=6), 8 (n=7), 12 (n=8) distinct values,
   indexed by conjugation pairs.
3. **Minimal separators.** For every pair of distinct conjugation classes
   {A, B} there is a lexicographically-first partition nu(A,B) with
   g(lambda,lambda,nu) != g(mu,mu,nu) for lambda in A, mu in B.
   Counts: 15 separators at n=6, 28 at n=7, 66 at n=8 (109 total).
   Every entry (nu, g1, g2) replays exactly from the class-sum formula.

Conjugation classes:

- n=6 (6): {(6),(1^6)}, {(5,1),(2,1^4)}, {(4,2),(2^2,1^2)},
  {(4,1^2),(3,1^3)}, {(3,3),(2^3)}, {(3,2,1)} (self-conjugate).
- n=7 (8): {(7),(1^7)}, {(6,1),(2,1^5)}, {(5,2),(2^2,1^3)},
  {(5,1^2),(3,1^4)}, {(4,3),(2^3,1)}, {(4,2,1),(3,2,1^2)},
  {(3,3,1),(3,2^2)}, {(4,1^3)} (self-conjugate).
- n=8 (12): {(8),(1^8)}, {(7,1),(2,1^6)}, {(6,2),(2^2,1^4)},
  {(6,1^2),(3,1^5)}, {(5,3),(2^3,1^2)}, {(5,2,1),(3,2,1^3)},
  {(5,1^3),(4,1^4)}, {(4,4),(2^4)}, {(4,3,1),(3,2^2,1)},
  {(4,2^2),(3^2,1^2)}, {(4,2,1^2)} (self-conj.), {(3^2,2)} (self-conj.).

n=6 separators (class A | class B | first nu | (g_A, g_B)),
lex order as above:

| class A | class B | first nu | (g_A, g_B) |
|---|---|---|---|
| {(6),(1^6)} | {(5,1),(2,1^4)} | (4,1,1) | (0,1) |
| {(6),(1^6)} | {(4,2),(2^2,1^2)} | (2,2,2) | (0,1) |
| {(6),(1^6)} | {(4,1^2),(3,1^3)} | (2,1^4) | (0,1) |
| {(6),(1^6)} | {(3,3),(2^3)} | (2,2,2) | (0,1) |
| {(6),(1^6)} | {(3,2,1)} | (1^6) | (0,1) |
| {(5,1),(2,1^4)} | {(4,2),(2^2,1^2)} | (2,2,2) | (0,1) |
| {(5,1),(2,1^4)} | {(4,1^2),(3,1^3)} | (2,1^4) | (0,1) |
| {(5,1),(2,1^4)} | {(3,3),(2^3)} | (2,2,2) | (0,1) |
| {(5,1),(2,1^4)} | {(3,2,1)} | (1^6) | (0,1) |
| {(4,2),(2^2,1^2)} | {(4,1^2),(3,1^3)} | (2,1^4) | (0,1) |
| {(4,2),(2^2,1^2)} | {(3,3),(2^3)} | (3,2,1) | (2,0) |
| {(4,2),(2^2,1^2)} | {(3,2,1)} | (1^6) | (0,1) |
| {(4,1^2),(3,1^3)} | {(3,3),(2^3)} | (2,1^4) | (1,0) |
| {(4,1^2),(3,1^3)} | {(3,2,1)} | (1^6) | (0,1) |
| {(3,3),(2^3)} | {(3,2,1)} | (1^6) | (0,1) |

n=7: all 28 pairs separate; rows against {(7),(1^7)} use
nu = (5,1,1),(3,2,2),(3,1^4),(2^3,1),(2,1^5),(1^7),(2,1^5), all (0,1);
the same ladder repeats for the {(6,1),...} and {(5,2),...} rows;
{(5,1^2),(3,1^4)} row: (2^3,1),(2,1^5),(1^7),(2,1^5), all (0,1);
{(4,3),(2^3,1)} row: (2,1^5),(1^7),(2,1^5), all (0,1);
{(4,2,1),(3,2,1^2)} vs {(3,3,1),(3,2^2)}: (2^2,1^3) (3,1);
{(4,2,1),(3,2,1^2)} vs {(4,1^3)}: (1^7) (0,1);
{(4,1^3)} vs {(3,3,1),(3,2^2)}: (1^7) (1,0).
Full 28-row machine list in artifacts/square_vectors.json.

n=8: all 66 pairs separate. Early lex coordinates vanish for small squares,
so most separators are (0,1)/(0,2) at the first supported coordinate;
large-on-both-sides cases include
{(3,2,2,1),(4,3,1)} vs {(3,3,1,1),(4,2,2)}: (2^3,1^2)=(2,2,2,1,1) (3,1);
{(3,2,1^3),(5,2,1)} vs {(2^4),(4,4)}: (2,2,2,1,1) (1,0);
{(4,2,1^2)} vs {(3^2,2)}: (2,1^6) (2,1).
Full 66-row machine list in artifacts/square_vectors.json.

Example certificate: n=6, {(4,2),(2^2,1^2)} vs {(3,3),(2^3)} at nu=(3,2,1),
values (2,0): sum_C |C| chi_(4,2)(C)^2 chi_(3,2,1)(C) = 2*720 while the same
sum for (3,3) is 0; all earlier lex nu agree.

## Proof / evidence

From-scratch exact integer computation (certified computation, not a
closed-form proof):

1. Enumerate partitions (11/15/22). Recompute all irreducible characters by
   Murnaghan-Nakayama recursion from the empty partition with rim-hook signs
   (no library tables).
2. Class sizes |C| = n!/z_mu per cycle type; verified sum |C| = n!.
3. Character orthogonality sum_C |C| chi_a chi_b = n! delta_{ab} verified.
4. Cross-checks: hook-length formula for degrees; n-cycle values +-1 on
   hooks, 0 elsewhere.
5. Every g(lambda,lambda,nu) by the exact class-sum formula; integer
   division certified (numerator divisible by n!).
6. Pairwise comparison of square-vectors; grouping equals conjugation pairs;
   lex-first separators extracted.
7. Independent replay (verify.py) rechecks every coefficient, every
   separator entry plus earlier-coordinate agreement, and S3 symmetry
   g(a,b,c) permutations.

The auditor additionally recomputed everything through an independent
beta-set (Maya-diagram) Murnaghan-Nakayama code path and matched all 48
square-vectors and all 109 separator nu/values exactly.

## Limitations

- Scope is exactly n = 6, 7, 8; no claim for n >= 9 or general n.
- Proof is computational (exact integer arithmetic, hand-replayable in
  principle); no closed-form human proof.
- Separator minimality is relative to the fixed lexicographic orders above.
- Character tables are classical; the new content is the
  separation/collision boundary with certificates.

## Reproducibility

Stdlib-only Python, seconds of runtime (n=8 dominates, well under a minute):

```
python3 artifacts/mn_check.py      # MN tables + orthogonality
python3 artifacts/squares.py       # square vectors + separators
python3 artifacts/dump_tables.py   # char tables + hook/n-cycle checks
python3 artifacts/verify.py        # independent replay of all
                                   # coefficients, separators, S3
```

Artifacts: mn_check.py, squares.py, square_vectors.json (all 48 square
vectors and all 109 separators with (nu,g1,g2)), char_tables.json,
dump_tables.py, verify.py.

## References

- C. Bessenrodt, C. Bowman, Multiplicity-free Kronecker products of
  characters of the symmetric groups, arXiv:1609.03596 (2016).
- I. Pak, G. Panova, E. Vallejo, Kronecker products, characters, partitions,
  and the tensor square conjectures, arXiv:1304.0738 (2013).
- C. Zhao, On the Kronecker product of Schur functions of square shapes,
  arXiv:2309.00764 (2023).
- C. Lecouvey, Stabilized plethysms for the classical Lie groups,
  arXiv:math/0703514 (2007/2008).
- GAP Character Table Library (CTblLib),
  https://www.gap-system.org/Packages/ctbllib.html
