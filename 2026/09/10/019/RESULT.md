# Engel width two on A_7: A_7 = e_2(A_7) e_2(A_7) with Frobenius class-algebra certificate

## Context

Engel word maps on finite simple groups are studied in the Shalev Engel-surjectivity
program and the Larsen–Shalev / Liebeck–O'Brien–Shalev / Guralnick word-map width
program. The commutator word (e_1) is surjective on finite simple groups (Ore
theorem). Even for the second Engel word e_2, no surjectivity or width-two theorem
on an alternating group past the exceptional isomorphisms
A_5 ≅ PSL_2(4), A_6 ≅ PSL_2(9) was recorded. The nearest results are
PSL(2,q)-only (Bandman–Garion–Grunewald) or large-group disjoint-variable
asymptotics with unspecified thresholds (Larsen–Shalev–Tiep).
A_7 (order 2520, 9 conjugacy classes) is the smallest alternating group free of
those exceptional isomorphisms, hence the canonical first generic case.

## Definitions

- Commutator: [a,b] = a^{-1} b^{-1} a b.
- Second Engel word: e_2(x,y) = [[x,y],y].
- G = A_7, |G| = 2520, with 9 conjugacy classes:
  identity; type (3,1^4) size 70; type (2^2,1^3) size 105;
  type (5,1^2) size 504; type (4,2,1) size 630; type (3^2,1) size 280;
  type (3,2^2,1) size 210; and the split pair 7A, 7B of type (7) size 360 each.
  Only type (7) (distinct odd parts) splits on restriction from S_7.
- E = e_2(G) = { e_2(x,y) : x,y in G }.
- N_1(g) = |{ (x,y) : e_2(x,y) = g }| (single-value preimage count).
- N(g) = |{ (u,v) in E × E : uv = g }| (width-two count).
- Frobenius class-algebra sum: for E a union of classes with
  S_chi = sum_{u in E} chi(u),
  N(g) = (1/|G|) sum_chi S_chi^2 chi(g)/chi(1).

## Result

Let e_2(x,y) = [[x,y],y] and G = A_7 (|G| = 2520).
Then every element of G is a product of two second-Engel values:

  G = e_2(G) e_2(G).

Precisely, for each of the 9 conjugacy-class representatives g,
N(g) = 2520 > 0 via the Frobenius sum over the logged A_7 character table
with S_chi = (2520, 0, …, 0).
In fact the certificate proves the sharp form N(g) = 2520 on all 9 classes
because E = G as sets (single-value surjectivity N_1 > 0 on every class).

Per-element single preimage counts N_1: identity 105840; 3-cycles 6768;
double-transpositions 4032; 5-cycles 2770; type (4,2,1) 1632;
type (3,3,1) 3510; type (3,2,2,1) 2232; 7A and 7B 2044 each.
Total pairs 2520^2 = 6350400.

## Proof / evidence

1. S_7 character table from scratch via the Murnaghan–Nakayama rim-hook rule
   over the 15 partitions of 7. Full 15×15 row orthogonality verified:
   sum_C |C| chi_lambda(C) chi_mu(C) = 5040 delta. Degrees
   [1,1,6,6,14,14,14,14,15,15,20,21,21,35,35], sum d^2 = 5040.
2. Restriction to A_7. The 8 even S_7 classes give A_7 classes; only (7)
   splits, yielding 9 classes with sizes above (sum 2520). Non-self-conjugate
   S_7 pairs restrict to one A_7 irrep each; the unique self-conjugate irrep
   (4,1^3) splits into two, differing on 7A/7B by ±sqrt(-7)/2.
   Full 9×9 complex row orthogonality verified. Degrees
   [1,6,10,10,14,14,15,21,35], sum d^2 = 2520.
3. Exhaustive enumeration over all 2520^2 = 6350400 pairs (numpy-vectorized
   loop, independently re-implemented with tuple arithmetic) gives the
   per-class N_1 table above. Every class has N_1 > 0, so E = G as sets.
   One explicit preimage witness per class (plus both 7A/7B halves) is filed
   and replayed; the two 7-cycle witnesses are proved to lie in distinct
   A_7-halves (A_7-orbit size 360; S_7-fusing element odd).
4. Frobenius convolution: since E = G, S_chi = (2520,0,…,0) by orthogonality,
   whence N(g) = 2520^2/2520 = 2520 > 0 for every class. Per-class constants
   table filed.
5. All checks replay: `verify.py` (independent recount + witness replay),
   `verify_frobenius.py` (class sizes, degrees, orthogonality, Frobenius sums),
   `char_table.py` (rebuild of both tables and certificate), `enumerate_e2.py`
   (census regeneration). The auditor independently re-ran the character-table
   build and Frobenius replay and performed a fresh full 6.35M-pair stdlib
   recount matching the census exactly.

## Limitations

Proves width-two (indeed single-value surjectivity) only for the single group
A_7. Uniform single-value surjectivity for all n ≥ 7 (the original target) is
NOT proved. Any supporting scaffolding toward larger n is conjectural and is
not part of the claimed theorem. The Frobenius width-two layer is degenerate
given E = G; the substantive content is the exhaustive census plus the verified
character table. Proof separates machine-verified computation from cited
standard formulas (rim-hook rule, A_n splitting criterion/values).

## Reproducibility

- `python3 output/artifacts/char_table.py` → ALL CERTIFICATE CHECKS PASSED
  (rebuilds S_7 and A_7 tables, Frobenius certificate).
- `python3 output/artifacts/verify.py` → VERIFY: OK
  (independent recount + witness replay).
- `python3 output/artifacts/verify_frobenius.py` → VERIFY_FROBENIUS: OK
  (class sizes, orthogonality, N(g) = 2520).
- `python3 output/artifacts/enumerate_e2.py` → regenerates `e2_census.json`.
- Convention: permutations compose as (pq)(i) = p(q(i)); [a,b] = a^{-1}b^{-1}ab.

## References

- T. Bandman, S. Garion, F. Grunewald, On the surjectivity of Engel words on
  PSL(2,q), arXiv:1008.1397 — PSL(2,q)/SL(2,q)-only Engel surjectivity via
  SL_2 trace dynamics; states nothing about A_n.
- M. Larsen, A. Shalev, P. H. Tiep, Probabilistic Waring problems for finite
  simple groups, arXiv:1808.05116 — disjoint-variable w_1 w_2 almost-uniformity
  and N-fold products for large groups with unspecified thresholds; no
  single-word e_2 statement, no fixed-group A_7 certificate.
- M. Larsen, A. Shalev, Word maps and Waring type problems, arXiv:math/0701334
  — asymptotic/large-group width; no uniform e_2 surjectivity from n = 7.
- S. Jambor, M. Liebeck, E. O'Brien, Some word maps that are non-surjective on
  infinitely many finite simple groups, arXiv:1205.1952 — ad-hoc words on
  PSL_2-type families, not e_2 on A_n.
