# Certified weight spectra of a two-fold Golay shortening: an explicit [22,10,8] witness

## Context

The optimal distance D*(22,10) = 8 is closed background: Grassl BKLC records
Lb(22,10) = Ub(22,10) = 8 via shortening of the extended Golay [24,12,8] code at
{23..24}, with the upper bound by the Griesmer bound. Those tables publish no
weight enumerator, dual spectrum, or enumerator census for the shortened child.
Weight spectra of Golay-derived optimal codes fix the dual spectrum via
MacWilliams, determine undetected-error coefficients, and distinguish
inequivalent shortenings reused in code-based crypto and CSS/quantum-code
selections.

## Definitions

Binary linear [n,k,d] code C of length n, dimension k, minimum distance d.
W_C = (A_0,...,A_n): A_i = number of codewords of weight i.
Dual C^perp of dimension n-k with distribution (B_0,...,B_n).
Binary MacWilliams/Krawtchouk identities:
B_j = 2^{-k} sum_i A_i K_j(i;n), j = 0..n,
where K_j(i;n) = sum_t (-1)^t C(i,t) C(n-i,j-t).
Syndrome coset leaders: for parity-check H ((n-k) x n), each of the 2^{n-k}
syndromes has a minimum-weight error pattern (leader); the leader-weight
distribution proves distance: all weight-<=3 patterns are unique leaders and
the zero syndrome has no word of weight 1..7 iff d = 8.

## Result (proved witness)

There exists an explicit binary linear [22,10,8] code C, obtained as the
shortening of the extended Golay code G_24 = [24,12,8] at two coordinates,
with exactly tallied spectra:

- W_C: A_0 = 1, A_8 = 330, A_12 = 616, A_16 = 77 (all other A_i = 0; sum 1024).
- Dual C^perp (dim 12): B_0 = 1, B_6 = 77, B_7 = 352, B_8 = 330, B_10 = 616,
  B_11 = 1344, B_12 = 616, B_14 = 330, B_15 = 352, B_16 = 77, B_22 = 1
  (sum 4096).
- (W_C, W_{C^perp}) satisfies all 23 binary MacWilliams/Krawtchouk identities
  term-by-term over the integers.
- Coset-leader weight distribution over all 4096 syndromes:
  {0:1, 1:22, 2:231, 3:1540, 4:1771, 5:484, 6:45, 7:2};
  every error pattern of weight <= 3 is a unique coset leader (count
  1+22+231+1540 = 1794) and no nonzero codeword has weight below 8, so
  d(C) = 8 with covering radius 7.

Committed generator: 10x22 matrix in row-reduced systematic form (pivot
columns 0-9), rows as integer masks (bit c = column c):

G = [2422785, 1805314, 3610628, 3951624, 2810896, 504864, 1009728, 2019456,
     4038912, 2702848]

Row table (columns 0-21):

| row | columns 0-21 |
|-----|--------------|
| 0 | 1 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 1 0 0 1 |
| 1 | 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 1 1 0 |
| 2 | 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 1 1 1 0 1 1 |
| 3 | 0 0 0 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 1 1 1 1 |
| 4 | 0 0 0 0 1 0 0 0 0 0 1 0 0 1 1 1 0 1 0 1 0 1 |
| 5 | 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 0 0 0 |
| 6 | 0 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 0 0 |
| 7 | 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 0 |
| 8 | 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 1 1 0 1 1 1 1 |
| 9 | 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 1 0 0 1 0 1 |

## Proof / evidence

Exhaustive enumeration (proof, stdlib only), replayed by
output/artifacts/verify.py (prints VERIFY_OK):

1. Golay parent: cyclic [23,12,7] from g = x^11+x^10+x^6+x^5+x^4+x^2+1
   (g divides x^23+1 checked), 12 shifts x^i*g, extended by overall parity.
   Rank 12; 4096-word tally reproduces {0:1, 8:759, 12:2576, 16:759, 24:1}.
2. Shortening: kept codewords vanishing at coordinates 22 and 23, deleted
   those coordinates -> 1024-word subcode; Gaussian elimination gives the
   committed 10-row basis (auditor verified the projected set equals the
   committed row space exactly as sets).
3. Tallies: all 2^10 codewords and all 2^12 dual words (dual basis from RREF
   nullspace, G.H^T = 0 checked entrywise) give W_C and W_dual above.
4. MacWilliams replay: each of the 23 Krawtchouk sums divisible by 1024 with
   quotient equal to the tallied dual count.
5. Syndrome proof of distance: BFS on the 12-bit syndrome graph from the 22
   columns of H visits all 4096 syndromes; leaders of weight <= 3 count 1794.

## Limitations

Proves one attained enumerator only. Whether every binary [22,10,8] code has
this enumerator (uniqueness / exact-list census) is left open. Distance
optimality D*(22,10) = 8 is cited background, not proved here. Other
inequivalent two-fold shortenings may have different spectra; do not cite this
witness as a census.

## Reproducibility

python3 output/artifacts/verify.py (Python 3 stdlib only, seconds) replays all
four checks and prints VERIFY_OK.

## References

- Markus Grassl, Bounds on linear codes [22,10] over GF(2) (Lb=Ub=8).
  https://www.codetables.de/BKLC/BKLC.php?q=2&n=22&k=10
- Markus Grassl, Bounds on linear codes [24,12] over GF(2) (Golay parent).
  https://www.codetables.de/BKLC/BKLC.php?q=2&n=24&k=12
- F. J. MacWilliams, N. J. A. Sloane, MacWilliams identities / Theory of
  Error-Correcting Codes. https://doi.org/10.1002/j.1538-7305.1963.tb00040.x
- J. H. Griesmer, A bound for error-correcting codes (1960).
  https://doi.org/10.1147/rd.45.0532
