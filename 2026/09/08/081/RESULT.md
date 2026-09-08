# Exact star-discrepancy values for the Fibonacci lattices F_5–F_12 with dual witnesses

## Context

Star discrepancy is the classical quantitative measure of uniform
distribution (Weyl) and controls quasi–Monte Carlo cubature error via the
Koksma–Hlawka inequality. The Fibonacci lattices are textbook rank-1
lattice rules in the unit square. Prior literature gives general bounds
(Erdos–Turan–Koksma inequality, optimal-order Fibonacci discrepancy) and
exact formulas for different invariants (extreme/periodic L_2, diaphony),
but no per-set exact L_infinity star-discrepancy table with extremal boxes
for these lattices.

## Definitions

Let F_1 = F_2 = 1, F_{m+1} = F_m + F_{m-1}. For m = 5..12 put N = F_m and
g = F_{m-1}. The Fibonacci lattice is

  P_m = { (k/N, {(k g mod N)/N}) : k = 0, ..., N-1 } ⊂ [0,1)^2.

For a finite set P with |P| = N, the anchored (L_infinity) star discrepancy is

  D*(P) = sup_{x,y ∈ [0,1]} | A([0,x]×[0,y]; P)/N − x·y |,

where A(B; P) counts points of P in B. The sup is over closed anchored
boxes; open and half-open variants are examined in the proof to capture
left-limit volumes.

The dual lattice is L^⊥ = { h ∈ Z² : h_1 + h_2·g ≡ 0 mod N }. The lattice
Weyl sum S(h) = N^{−1} Σ_{p ∈ P_m} e^{2πi h·p} satisfies |S(h)| = 1 if
h ∈ L^⊥ and 0 otherwise.

## Result (headline, proved)

For each m = 5..12, with N = F_m, the exact star discrepancy D*(P_m) equals
bestnum/N² with the extremal anchored box below (all extremal boxes are
closed, hence attained):

| m  | N   | D*(P_m) exact      | decimal      | extremal box (a/N, b/N, type, count) |
|----|-----|--------------------|--------------|--------------------------------------|
| 5  | 5   | 9/25               | 0.36         | 2/5, 3/5, closed, 3                  |
| 6  | 8   | 15/64              | 0.234375     | 5/8, 5/8, closed, 5                  |
| 7  | 13  | 28/169             | 0.1656804734 | 7/13, 9/13, closed, 7                |
| 8  | 21  | 16/147             | 0.1088435374 | 15/21, 15/21, closed, 13             |
| 9  | 34  | 41/578             | 0.0709342561 | 15/34, 24/34, closed, 13             |
| 10 | 55  | 136/3025           | 0.0449586777 | 36/55, 39/55, closed, 28             |
| 11 | 89  | 246/7921           | 0.0310566848 | 49/89, 64/89, closed, 38             |
| 12 | 144 | 13/648             | 0.0200617284 | 104/144, 104/144, closed, 78         |

Each row is an exact rational (degenerate width-0 interval).

Exact dual-lattice witnesses (shortest nonzero dual vector h*, squared
length, dual hits in ‖h‖_∞ ≤ 12, Q_H = Σ_hits 1/r(h) with
r(h) = max(1,|h_1|)·max(1,|h_2|)):

| N   | h*      | ‖h*‖² | dual hits (H=12) | Q_H      |
|-----|---------|-------|-------------------|----------|
| 5   | (−2,−1) | 5     | 24                | 5.126667 |
| 8   | (−2,2)  | 8     | 36                | 4.139484 |
| 13  | (−3,2)  | 13    | 48                | 2.879666 |
| 21  | (−3,−3) | 18    | 30                | 1.485120 |
| 34  | (−5,−3) | 34    | 16                | 0.635281 |
| 55  | (−5,5)  | 50    | 10                | 0.283196 |
| 89  | (−8,5)  | 89    | 4                 | 0.100000 |
| 144 | (−8,−8) | 128   | 2                 | 0.031250 |

## Proof / evidence

Both coordinates of P_m lie on (1/N)Z. Between consecutive grid lines the
box census A is constant while the volume varies continuously, so the
deviation |A/N − xy| on each cell attains its supremum at a cell corner
(closed boxes at corners; open/mixed types capture left limits). Hence the
sup over all anchored boxes equals the max over the (N+1)² grid corners
(a/N, b/N) with all four edge-inclusion types (closed, open, two mixed
half-open), i.e. deviation |C·N − a·b|/N² with integer census C.

The verifier `output/artifacts/verify_discrepancy.py` (stdlib only) computes
this max twice, independently: (i) 2D prefix sums over the occupancy grid,
(ii) O(N³) brute-force counting of points in every point-defined box. Both
engines agree digit-for-digit (integer equality of bestnum) on all 8
lattices; the script exits nonzero on any mismatch and prints VERIFY_OK
otherwise. The audit independently recomputed all 8 rows from scratch with
exact rational arithmetic and confirmed every fraction and every extremal
(a, b, count), plus all dual witnesses. Full cross-check at N ≤ 144 runs in
seconds.

## Limitations

1. No Erdos–Turan–Koksma Weyl-sum upper/lower enclosure is computed; the
   original target's "interval contains both exact and ETK enclosure"
   criterion is not met and no certified ETK bounds are claimed.
2. The accompanying three-distance gap census (golden-ratio rotation at
   N = F_m: 2 distinct gaps, N·mingap ≈ 0.7236) and Kronecker rows for one
   bounded-quotient vector (α = (√5−1)/2, β = √2−1) are replayable float
   computations (1e-9 clustering tolerance; coordinate-separation margins
   logged), not interval-certified proofs, and no separate
   Ostrowski-decomposition log is given.
3. The proved part is the exact Fibonacci table plus the exact dual
   witnesses above; the gap/Kronecker rows are computed evidence only.

## Reproducibility

`python3 output/artifacts/verify_discrepancy.py` (stdlib only) recomputes
everything from the committed generators (N = F_m, g = F_{m-1}), runs both
exact engines, performs the gap-census and Kronecker computations, writes
`run_log.txt` and `table.json`, and terminates with VERIFY_OK. Runtime is
seconds at N ≤ 144.

## References

- Kuipers and Niederreiter — Uniform Distribution of Sequences
  (foundational ETK inequality and general bounds; no per-set table).
  https://onlinelibrary.wiley.com/doi/book/10.1002/9781118032426
- Drmota and Tichy — Sequences, Discrepancies and Applications
  (general discrepancy theory; no finite two-sided Fibonacci table).
  https://link.springer.com/book/10.1007/BFb0093402
- Weiß — Hammersley Point Sets and Inverse of Star-Discrepancy
  (Hammersley upper bound only, different object).
  https://arxiv.org/abs/2411.10363
- Clement, Doerr, Klamroth, Paquete — Constructing Optimal L_infinity Star
  Discrepancy Sets (optima known only n ≤ 6 in d=2; confirms hardness).
  https://arxiv.org/abs/2311.17463
- Hinrichs, Kritzinger, Pillichshammer — Extreme and periodic L_2
  discrepancy of plane point sets (L_2/diaphony formulas, not L_inf star).
  https://arxiv.org/abs/2005.09933
