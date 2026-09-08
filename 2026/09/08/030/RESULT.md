# Certified Sprague-Grundy and Outcome Periodicity with Cold Census for Subtract-a-Cube to Heap 200 (Ultimate Period 7 from 263/264)

## Context

Finite subtraction games and the structure/density of their P-position sets are a
recognized program: subtract-a-square P-positions as maximal square-difference-free
sets (Rouse Ball/Coxeter, Guy E26, Furstenberg–Sarkozy), with Eppstein (2018)
giving density/modular-structure benchmarks and a fast subtraction-game solver.
The cube analogue — the subtraction game with all applicable cube moves — had no
recorded Sprague-Grundy / P-position table (OEIS queries for subtract-a-cube
Grundy/losing positions return no results; the squares positive control A014586
and Eppstein's squares-only analysis confirm the gap).

## Definitions

Fix the subtraction set

S = {1, 8, 27, 64, 125} = {k^3 : k^3 <= 200},

the complete set of cube moves applicable to heaps 0 <= n <= 200.
From heap n, move to n − s for any s in S with s <= n. Heap 0 has no moves and loses.

- Outcome W(n) in {win, lose}: W(0) = lose; for n >= 1, W(n) = win iff some legal
  move reaches a losing heap.
- Sprague-Grundy value G(n) = mex{G(n−s) : s in S, s <= n}.
- A cold (P-) position is n with G(n) = 0, equivalently W(n) = lose.
- Let M = max S = 125.

## Result

For subtract-a-cube with S = {1, 8, 27, 64, 125}:

(a) Outcome. Least outcome-period pW = 7 with least preperiod qW = 263.
Cycle W[263..269] = [win, win, lose, win, lose, win, lose].
For all n >= 263, n is losing iff n mod 7 in {1, 3, 6}.

(b) Sprague-Grundy. Least SG-period pG = 7 with least preperiod qG = 264.
Cycle G[264..270] = [2, 0, 1, 0, 1, 0, 1].
For all n >= 264 with r = n mod 7: G(n) = 2 if r = 5; 0 if r in {1, 3, 6};
1 otherwise.

(c) Leastness. qW = 263, qG = 264, periods 7 are each least:
W(262) = win != lose (tail value at 262, since 262 mod 7 = 3);
G(263) = 4 != 1 (tail value at 263, since 263 mod 7 = 4);
every p in {1,..,6} fails in the tail, and the tail 7-cycles force any
preserving period to be a multiple of 7, all of which fail at the same
witness indices.

(d) Cold census on [0,200] (exact). Complete P-position list:

0, 2, 4, 6, 9, 11, 13, 15, 18, 20, 22, 24, 34, 37, 39, 41, 43, 46, 48, 50,
52, 55, 57, 59, 62, 69, 71, 74, 76, 78, 80, 83, 85, 87, 90, 92, 94, 97, 99,
104, 106, 108, 111, 113, 115, 118, 120, 122, 132, 137, 139, 141, 146, 148,
150, 152, 155, 157, 167, 169, 174, 176, 178, 181, 183, 185, 188, 190, 192,
195, 197

71 positions, density 71/201 ≈ 0.3532.
SG distribution on [0,200]: 0: 71; 1: 71; 2: 34; 3: 19; 4: 6.
G(n) = 0 coincides with losing on the whole computed range.

(e) Max nimber (exact). max_{0<=n<=200} G(n) = 4, attained exactly at
{128, 144, 160, 165, 172, 200}. Globally, the last 4 is G(263) = 4
(the only 4 beyond 200), the last 3 is at n = 216, and max_{n>=264} G(n) = 2.
Complete 4-positions: 128, 144, 160, 165, 172, 200, 263.
Complete 3-positions: 27, 29, 31, 33, 36, 65, 67, 96, 102, 125, 127, 130,
134, 136, 143, 162, 164, 171, 199, 216.

(f) Negative certificate (exact). No outcome period and no SG period is
certifiable with an agreement window of length >= 125 inside [0,200]
(exhaustive check over all (q, p) pairs). Hence ultimate periodicity is
genuinely not closable at the 200 cutoff; the preperiods 263/264 are the
true onsets.

## Proof / Evidence

Lemma (max-move induction step). If for some q >= 0, p >= 1,
W(n) = W(n+p) for all q <= n < q+M (and likewise G), then the equality holds
for all n >= q: for n >= q+M every predecessor n−s lies at >= q and the
predecessor sets of n and n+p shift identically, so the win-recurrence and
the mex sets agree. Hence a consecutive agreement window of length M = 125
proves ultimate periodicity for all n.

Standard subtraction DP from the rules alone computes W and G to 5000.
Direct integer comparison verifies: the 125-length base windows
W[n] = W[n+7] on 263 <= n < 388 and G[n] = G[n+7] on 264 <= n < 389;
the cycles; the last-mismatch indices (262 for W, 263 for G); failure of
every p < 7 in the tail (extended to all p by the gcd/multiple argument:
a non-multiple of 7 cannot preserve a non-constant 7-cycle, and every
multiple of 7 fails at the witness index); the cold list, SG distribution,
and max-nimber positions. The Lemma converts each 125-window into a proof
for all larger n; the 5000-extension (independently re-extended to 8000 in
audit) is confirmation. Claim (f) is an exhaustive finite check over [0,200].
Status is proof (finite certificate plus induction), not extrapolation.

## Limitations

- Period onsets (263/264) lie beyond the original [0,200] cutoff, so the
  200-range contribution is a certified census plus a proved negative
  certificate rather than a closed period; the closed ultimate periods are
  proved with data beyond 200 via the Lemma.
- Literature-absence rests on targeted OEIS/arXiv/octal queries with squares-only
  and octal-only positive controls, not an exhaustive full-text sweep.

## Reproducibility

Stdlib-only verifier recomputes everything from S alone:

```
python3 output/artifacts/verify_cubes.py   # prints VERIFY_OK
```

## References

- OEIS A014586 — Nim-Grundy for subtract-a-square (squares-only positive control).
- D. Eppstein, Faster Evaluation of Subtraction Games, FUN 2018, arXiv:1804.06515
  (squares only; density/modular-structure/fast-solver benchmarks).
- A. Flammenkamp, Sprague-Grundy Values of Octal-Games
  (https://wwwhomes.uni-bielefeld.de/achim/octal.html) — octal take-and-break only.
- Live OEIS nulls: "subtract a cube grundy", "subtract cubes losing" (no results);
  "subtract a cube" returns only unrelated entries (taxicab, reversal cubes, squares).
