# Conditioned pair-crosscorrelation minimum at N=21: exact census, gap, and classification

## Context

Single-sequence low-autocorrelation optima (Bernasconi / LABS energies) are
closed to N <= 66 (Packebusch–Mertens), but no exhaustive pair-crosscorrelation
table exists at N = 21. For CDMA, radar, and Rudin–Shapiro-like family design,
the recognized benchmark is the Pursley–Sarwate autocorrelation versus
crosscorrelation tradeoff (Katz–Lee–Trunov). This record supplies the first
proved conditioned pair floor at the natural N = 21 window where single-sided
2^21 enumeration is exactly closable.

## Definitions

- Littlewood sequence: `P, Q in {+1,-1}^21` (N = 21).
- Aperiodic autocorrelation: `C_k(Q) = sum_{j=0}^{20-k} q_j q_{j+k}`, k = 1..20.
- Autocorrelation energy: `E(Q) = sum_{k=1}^{20} C_k(Q)^2`.
- Aperiodic crosscorrelation: `D_k(P,Q)`, k = -20..20, with
  `D_k = sum_j P_j Q_{j+k}` (k >= 0) and the transposed sum for k < 0.
- Cross energy: `X(P,Q) = sum_{k=-20}^{20} D_k^2`.
- Combined demerit: `S(Q) = E(Q) + X(P*,Q)`.
- Fixed anchor: `P* = --+++++++--++-+-+-++-`, with
  `C(P*) = [0,1,0,1,0,-3,0,1,0,1,0,1,0,1,0,1,0,-3,0,1]`, `E(P*) = 26`
  (published OEIS A102780 / Packebusch–Mertens optimum at N = 21).
- Golay deficiency: `G(Q) = sum_{k>=1} (C^P_k + C^Q_k)^2 >= 0`.
- Exact identity (all integer, no rounding):
  `X(P*,Q) = N^2 + 2<C^P, C^Q>`, hence
  `S(Q) = N^2 - E(P*) + G(Q) = 415 + G(Q)`.
  Minimizing S is exactly minimizing G.
- Global-sign quotient: `q0 = +1` fixes `Q ~ -Q`; lossless for S since both
  E and X are invariant under `Q -> -Q`. Quotient size 2^20 = 1048576.
- Merit: `F(Q) = N^2/(2E(Q))`.
  Pursley–Sarwate diagnostic: `PSC = (X + 2*sqrt(E(P*)E(Q)))/N^2`.

## Result

Conditioned on the fixed anchor P* above, over all Littlewood Q of length 21:

- Minimum: `min_Q S(Q) = 455`, equivalently `G_min = 40` via `S = 415 + G`.
- Attainment: exactly 44 quotient representatives (`q0=+1`;
  88 full sequences counting `Q ~ -Q`).
- No exact complementary Q (`G = 0`) exists for this anchor; all minimizers
  are almost-complementary with deficiency 40.
- Gap: next occupied level `S = 471` (multiplicity 684 in quotient),
  so minimality gap is `471 - 455 = 16`.
- Minimizer landscape in 5 classes by `(E(Q), X)`:

| rep Q* | E | X | S | G | F(Q*) | PSC | quotient mult |
|---|---|---|---|---|---|---|---|
| `+--+-++++---+-----+--` | 66 | 389 | 455 | 40 | 3.3409 | 1.06995 | 12 |
| `+--++--++++--+-+-----` | 58 | 397 | 455 | 40 | 3.8017 | 1.07634 | 20 |
| `+--++--++++-----+-+--` | 50 | 405 | 455 | 40 | 4.4100 | 1.08188 | 4 |
| `+-++++--++++-+---+--+` | 46 | 409 | 455 | 40 | 4.7935 | 1.08428 | 4 |
| `+++++--++++--+--+-+-+` | 42 | 413 | 455 | 40 | 5.2500 | 1.08637 | 4 |

Full integer auto profiles C_k, cross profiles D_k, canonical-sign
certificates, reversal orbits, and FFT cross-spectrum logs are in
`output/artifacts/catalog.json`.

## Proof / evidence

Proof by exhaustive enumeration with exact integer arithmetic
(distinguished from heuristic or statistical evidence):

1. Anchor: E(P*) recomputed as exactly 26 from the string.
2. Key identity X = N^2 + 2<C^P,C^Q> verified on samples; S = 415 + G holds
   for every evaluated Q.
3. Exhaustion: all 2^20 quotient patterns evaluated by exact integer
   autocorrelation/crosscorrelation (vectorized, seconds-scale).
   Independent recount with separately written code confirms
   total = 1048576, global min S = 455, count 44,
   bottom histogram {455: 44, 471: 684}.
4. Classification: every minimizer has G = 40; the five (E,X) classes above
   partition the 44 (12/20/4/4/4), each profile re-derived from its string.
5. FFT spectra are auxiliary logs only; minimality rests on exact integers.

## Limitations

- Conditioned on the single pinned anchor P*; no claim about unconditioned
  pair minima over both P and Q, other lengths, or asymptotic bounds.
- P* is one published-optimal (E = 26) representative; the conditioned
  minimum is relative to this fixed representative.
- Almost-complementary is used in the finite Golay-deficiency sense
  (G = 40), not as a claim about RS-like infinite families.
- Published-optimality E = 26 at N = 21 is taken from OEIS A102780 and
  Packebusch–Mertens scope, not re-derived here.
- Multiplicities 44/684 are in the q0=+1 quotient (full-sequence counts double).

## Reproducibility

```
python3 output/artifacts/run_census.py     # full 2^20 exact census (~seconds), writes census_top.json
python3 output/artifacts/build_catalog.py  # builds catalog.json (5 class reps + profiles)
python3 output/artifacts/verify.py         # independent audit incl. full recount; ALL CHECKS PASSED
```

Exact-integer recomputation of E, D_k, X, S, G, F, PSC from the P*/Q* strings
suffices to verify every number; numpy + stdlib only.

## References

- T. Packebusch and S. Mertens, Low Autocorrelation Binary Sequences,
  arXiv:1512.02475. Exhaustive single-sequence optima to N <= 66;
  used only as anchor source.
- D. J. Katz, S. Lee, and S. A. Trunov, Crosscorrelation of
  Rudin-Shapiro-Like Polynomials, arXiv:1702.07697. Crosscorrelation merit
  formula and RS-like pairs approaching the Pursley–Sarwate bound.
- D. J. Katz, S. Lee, and S. A. Trunov, Rudin-Shapiro-Like Sequences with
  Maximum Asymptotic Merit Factor, arXiv:1711.02233. Asymptotic merit 3 iff
  seed is length 1 or Golay-pair interleaving; almost-complementary lens.
- OEIS A102780, Ground states of the Bernasconi model. a(21) = 26 anchor.
