# Exact consecutive-prime residue-pair census to 5e7 with quantified Lemke Oliver-Soundararajan comparison

## Context

Consecutive primes show an unexpected erratic bias in their reduced residue
pairs, with diagonal pairs (a,a) suppressed relative to uniform, explained
conjecturally by Hardy-Littlewood k-tuple singular-series terms
(Lemke Oliver-Soundararajan 2016, arXiv:1603.03720 / PNAS).
That paper tabulates mod-3 pairs among the first 1e6 primes, mod-10 pairs
among the first 1e8 primes, and Section 5 tables at 1e9-1e12,
not an x <= 5e7 census.
Gap/pi databases (Oliveira e Silva to 4e18; Prime Gap List Project) record
bare gap sizes, occurrence counts, merits, and pi values with no
residue-labeled consecutive-pair matrices.
This record supplies a replayable exact T_10/T_3 benchmark at x = 5e7
(~3M pairs).

## Definitions

Let p_1 < p_2 < ... be the primes. Count consecutive pairs with
p_{n+1} <= 5e7.
T_10(a,b) for a,b in {1,3,7,9} counts pairs with p_n = a, p_{n+1} = b mod 10.
T_3(a,b) for a,b in {1,2} counts pairs with p_n = a, p_{n+1} = b mod 3
(pairs involving p = 2, 5 resp. p = 3 excluded).
Uniform expectation per cell: total pairs / 16 resp. / 4.
Chi-square vs uniform: sum (O-E)^2/E.
Hardy-Littlewood (HL) predictions: LOS Main Conjecture / Conjecture 1.1 and
Section 2 closed forms for r = 2 (diagonal (1.1)-type; symmetrised
off-diagonal (1.2)-type), evaluated with li(5e7) = 3001562.70.
Collapsed HL chi-square: 4 diagonal bins plus 6 symmetrised off-diagonal
sums (mod 10); 4 cells with halved symmetrised prediction (mod 3).

## Result

Marginals: pi(5e7) = 3001134.
Mod 10: 1: 750340; 3: 750395; 7: 750394; 9: 750003 (plus p = 2, 5).
Mod 3: 0: 1; 1: 1500480; 2: 1500653.

T_10 (rows/cols 1,3,7,9; 3001130 pairs):

|     | 1      | 3      | 7      | 9      |
|-----|--------|--------|--------|--------|
| 1   | 131565 | 229515 | 234815 | 154444 |
| 3   | 176570 | 123047 | 216105 | 234672 |
| 7   | 192045 | 205685 | 122881 | 229783 |
| 9   | 250160 | 192147 | 176592 | 131104 |

T_3 (rows/cols 1,2; 3001131 pairs):

|   | 1      | 2      |
|---|--------|--------|
| 1 | 655352 | 845128 |
| 2 | 845128 | 655523 |

Bias statistics (recomputed from the matrices):
uniform E_10 = 187570.625, chi2 = 155166.05 (df 15);
E_3 = 750282.75, chi2 = 47958.59 (df 3).
All four T_10 diagonal cells are the four smallest of the 16 entries
(diagonal share 0.1695 vs uniform 0.25).
Most suppressed (7,7) = 122881 (0.6551 x uniform);
most enhanced (9,1) = 250160 (1.3337 x uniform).
Mod 3 diagonal ratios 0.8735/0.8737, off-diagonal 1.1264/1.1264;
T_3[1,2] = T_3[2,1] = 845128 exactly.

HL comparison at this cutoff:
q = 10 diagonal prediction 138333.6 per class vs observed
[131565, 123047, 122881, 131104] (residuals -4.9%, -11.1%, -11.2%, -5.2%);
symmetrised off-diagonal prediction 408038.0 vs observed 404604-426860
(-0.8% to +4.6%).
Collapsed 10-bin HL chi2 = 6365.6 (df 9) vs uniform 10-bin chi2 = 105744.0
(~94% of uniform chi2 explained).
Mod 3: diagonal prediction 673893.9 vs 655352/655523;
symmetrised off-diagonal 1653775.0 vs 1690256 (+2.2%);
HL 4-cell chi2 = 1815.7 vs uniform 47958.6 (~96% explained).

## Proof / evidence

Finite census, not an asymptotic theorem.
Single Eratosthenes sieve to 5e7; ordered prime list archived
(12 MB uint32 LE binary, sha256 76f37eb58a4ca6daf73a49a8c174ed0c05772ef59b3c95caa4df88e16f8bb22d).
Two independent aggregation paths (modular % vs division-based residues)
agreed exactly.
verify.py re-reads the archive and re-derives pi, hash, both matrices,
both chi-squares, and extremal-pair identities from scratch, printing
VERIFY_OK.
Auditor independently reproduced pi = 3001134 with a separate odd-only
sieve giving a byte-exact hash match, and recomputed all sums, chi-squares,
and HL collapsed-bin statistics above.
HL formulae are prior work (LOS), applied and quantified here, not proved.

## Limitations

Single cutoff x = 5e7; no rate or sign-persistence claim beyond it.
HL comparison is a goodness-of-fit datum for a prior conjecture, not a proof
of that conjecture; collapsed-bin chi2 treats predictions as fixed (no
fitted parameters) and ignores dependence between cells.
Residual asymmetry (e.g. (3,3)/(7,7) fitting worse than (1,1)/(9,9); spread
among symmetrised off-diagonal sums) is reported as data, plausibly
zeros-of-L fluctuations and higher-order terms per LOS, unclaimed here.

## Reproducibility

output/artifacts/verify.py + output/artifacts/counts.json +
output/artifacts/stats.json replay all headline numbers (VERIFY_OK).
The 12 MB primes_5e7.bin (inputs/artifacts/) enables byte-level replay but
is not copied to output; its sha256 above pins it.
Independent sieve: odd-only bytearray Eratosthenes to 5e7 takes ~1 s in
Python and reproduces pi and the archived hash exactly.

## References

- R. J. Lemke Oliver, K. Soundararajan, Unexpected biases in the
  distribution of consecutive primes, arXiv:1603.03720 (PNAS 2016).
- T. Oliveira e Silva, Gaps between consecutive primes (to 4e18),
  http://sweet.ua.pt/tos/gaps.html
- Prime Gap List Project, https://primegap-list-project.github.io/about/
