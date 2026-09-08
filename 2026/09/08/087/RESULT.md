# Exact Schrijver-sharpness census of D(7,3): minimum permanent 24, witness orbit, and full distribution

## Context

The minimum number of perfect matchings (permanents) of k-regular bipartite
graphs is a recognized program (Schrijver, Voorhoeve, with the Bregman–Minc
upper-bound counterpart). General lower bounds exist, but exact minima and
extremal structures are known only at small parameters. The adjacent class
D(6,3) has exact minimum 17 (internal precedent SCOPE040). This record settles
the next odd-order boundary D(7,3).

## Definitions

- Let D(7,3) be the set of all 7x7 binary (0,1)-matrices with every row sum
  and every column sum equal to 3.
- per(A) = sum over sigma in S_7 of prod_i A[i,sigma(i)] (number of perfect
  matchings of the corresponding 3-regular bipartite graph).
- m(7,3) = min_{A in D(7,3)} per(A).
- Schrijver(7,3) = ((3-1)^2/3)^7 = (4/3)^7 = 16384/2187 ≈ 7.4915, the general
  Schrijver k-regular lower bound evaluated at (n,k)=(7,3).

## Result

1. **Labeled count.** |D(7,3)| = 68,938,800 (agrees with OEIS A001501).
2. **Exact minimum.** m(7,3) = 24.
3. **Full permanent distribution** over labeled matrices:
   24: 14,439,600; 25: 6,350,400; 26: 25,401,600; 27: 16,934,400;
   30: 3,175,200; 31: 1,814,400; 32: 793,800; 54: 29,400.
   These sum to 68,938,800. Values 28, 29 and 33..53 do not occur;
   54 is an isolated value with mass 29,400.
4. **Schrijver ratio.** m(7,3)/Schrijver(7,3) = 24/(16384/2187)
   = 6561/2048 ≈ 3.2036 (exact fraction).
5. **Explicit minimizer.** With bit j = column j (LSB = column 0), row masks
   [7, 7, 25, 26, 100, 104, 112], i.e. the matrix
   ```
   1 1 1 0 0 0 0
   1 1 1 0 0 0 0
   1 0 0 1 1 0 0
   0 1 0 1 1 0 0
   0 0 1 0 0 1 1
   0 0 0 1 0 1 1
   0 0 0 0 1 1 1
   ```
   has all row and column sums 3 and permanent exactly 24.
   Its S7xS7 (row/column-permutation) stabilizer has order 16, so its orbit
   has size 5040^2/16 = 1,587,600 labeled matrices.

## Proof / evidence

- **Exhaustive enumeration** in C with OpenMP (`artifacts/enum.c`): fix row 0
  to canonical mask 7 (column symmetry gives factor 35 = C(7,3)); enumerate
  rows 1..6 over the 35 weight-3 masks with column-cap/capacity pruning
  (colsum+bit ≤ 3 and colsum+bit+remaining ≥ 3); evaluate each leaf by Ryser
  inclusion-exclusion (127 nonempty subsets x 7 rows). The auditor recompiled
  and re-ran this program and reproduced: subtotal with row 0 fixed
  1,969,680 = 68,938,800/35; minimum 24 in every one of the 35 row-1 classes;
  fixed-row-0 histogram 24:412560, 25:181440, 26:725760, 27:483840,
  30:90720, 31:51840, 32:22680, 54:840, which x35 equals the claimed
  full-class distribution.
- **Independent replay** (`python3 artifacts/verify.py` -> VERIFY_OK,
  re-executed by the auditor): witness margins all 3; brute-force
  5040-permutation permanent = 24; independent Ryser evaluation = 24;
  Schrijver fraction 16384/2187 and exact ratio 6561/2048; distribution sums
  to 68,938,800 with minimum 24.
- **Stabilizer cross-check** (auditor's independent C brute force over all
  5040 x 5040 = 25.4M S7xS7 pairs and all 5040 permutations): witness
  permanent 24, stabilizer order 16, orbit size 1,587,600.
- The column-symmetry reduction (factor 35) is justified by transitivity of
  the column-permutation action on weight-3 subsets; the pruning conditions
  are necessary conditions for completability, hence sound.

## Limitations

- Only one minimizer orbit (representative, stabilizer order 16, orbit size
  1,587,600) is exhibited. The total number of minimizer orbits under
  S7xS7 is not classified; no complete orbit census is claimed.
- The distribution (including gaps at 28, 29, 33..53 and the isolated mass
  at 54) is a computed exhaustive-census fact, replayed via the enumeration
  program, not a separately proved structural theorem.

## Reproducibility

- `gcc -O2 -fopenmp -o enum_audit artifacts/enum.c` then `./enum_audit`
  reproduces the subtotal, total, minimum, witness, and histogram.
- `python3 artifacts/verify.py` replays margins, both permanent evaluations,
  the Schrijver fraction/ratio, and the distribution sum (stdlib only).

## References

- OEIS A001501 — Number of n x n (0,1)-matrices with row/column sums 3
  (counts only): https://oeis.org/A001501
- OEIS A000166 — Derangements / permanent of J−I (structurally excluded by
  margin 3): https://oeis.org/A000166
- MathWorld, Permanent (Ryser formula reference):
  https://mathworld.wolfram.com/Permanent.html
- Schrijver (1998), Counting 1-Factors in Regular Bipartite Graphs, JCTB 72:
  https://doi.org/10.1006/jctb.1997.1798
