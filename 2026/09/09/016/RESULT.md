# Demicap-fiber rigidity in AG(4,3): the pairwise-intersection spectrum over one demicap is the singleton {12}

## Context

Maximal caps in `AG(4,3)` have 20 points (Pellegrino) and are all affinely
equivalent (Hill). Follett et al. partition `AG(4,3)` into four disjoint
maximal caps plus a common anchor, classifying disjoint pairs as
1/2/6-completable (36/90/72). Awan et al. introduce 10-point demicaps
(five anchor-lines, no four cohyperplanar), prove all demicaps equivalent,
and count 101088 demicaps per anchor, 72 per maximal cap, and 6 maximal
caps per demicap. None of these sources states the intersection sizes of
two distinct maximal caps *sharing* one fixed demicap.

## Definitions

- `AG(4,3) = F_3^4`; point `(x1,x2,x3,x4)` is encoded as
  `x1*27+x2*9+x3*3+x4` in `0..80`. Three points are collinear iff their
  vectors sum to `(0,0,0,0)`.
- Anchor `a = 0 = (0,0,0,0)`.
- Committed demicap anchor
  `D0 = {1,2,3,6,9,18,27,40,54,80}`,
  the five `0`-lines through `+-(1,0,0,0)`, `+-(0,1,0,0)`,
  `+-(0,0,1,0)`, `+-(0,0,0,1)`, `+-(1,1,1,1)`.
- A demicap is a 10-point cap of five anchor-lines with no four
  cohyperplanar (every 4-subset of line directions spans `F_3^4`).
- Fiber: maximal 20-caps `C` with `D0 ⊆ C`.
- Spectrum `I(D0) = {|C1 ∩ C2| : C1 ≠ C2 maximal 20-caps, D0 ⊆ C1 ∩ C2}`.

## Result

**Theorem.** `D0` is a demicap with anchor `0`. Exactly six maximal 20-caps
contain `D0`:

- C0 = [1,2,3,6,9,14,18,25,27,34,40,44,47,48,54,59,64,69,76,80]
- C1 = [1,2,3,6,9,14,18,25,27,35,40,42,46,50,54,58,65,70,75,80]
- C2 = [1,2,3,6,9,16,18,23,27,32,40,44,46,51,54,61,65,66,76,80]
- C3 = [1,2,3,6,9,16,18,23,27,35,38,40,48,52,54,58,68,69,73,80]
- C4 = [1,2,3,6,9,17,18,22,27,32,40,42,47,52,54,61,64,68,75,80]
- C5 = [1,2,3,6,9,17,18,22,27,34,38,40,50,51,54,59,66,70,73,80]

For every unordered distinct pair, `|Ci ∩ Cj| = 12`: the five `0`-lines of
`D0` plus exactly one further shared `0`-line. Hence

```
I(D0) = {12},
```

with 12 attained by all 15 pairs and each of
`10,11,13,14,15,16,17,18,19` unattained.
Auxiliary data: `|Stab(D0)| = 240`; each `|Stab(Ci)| = 2880`;
`Stab(D0)` acts transitively on the six caps.

## Proof / evidence

Certified finite enumeration, replayable with stdlib only:

1. Demicap check: `D0` has no three collinear points; every 4-subset of
   its five line-directions has rank 4 (no four `0`-lines cohyperplanar).
2. Pool: 30 points complete no line with any pair from `D0`; the other 41
   points outside `D0` (including the anchor) each complete ≥ 1 line and
   can never extend `D0` to a cap.
3. Unbiased backtracking over `C(30,10)` with exact collinearity test
   `third(p,q) ∉ D0 ∪ chosen` on every addition, no symmetry pruning:
   returns exactly the six sets above, so the fiber is closed.
4. Each `Ci` verified: 20 points, cap (no line of the 1080 contained),
   maximal (every outside point lies on a secant), union of 10 lines
   through `0` (anchor `0`).
5. Linear-stabilizer enumeration: 240 for `D0`, 2880 per cap,
   transitivity on the fiber (orbit size 6).
6. Exact incidence intersections: all `C(6,2) = 15` pairs meet in 12
   points; each surplus beyond `D0` is one antipodal `0`-line pair.
   Exclusion of the other nine values in `[10,19]` is complete via the
   exhaustive pair table (no separate UNSAT search needed).

Replay: `python3 output/artifacts/verify.py` prints `VERIFY_OK` in seconds.

## Limitations

- Spectrum proved for the single committed anchor `D0`; extension to all
  demicaps uses the cited Awan et al. affine-equivalence theorem, not
  recomputed here.
- Fiber completeness rests on the sum-zero collinearity model of
  `AG(4,3)`, documented in the script.
- Stabilizer orders are linear (origin-fixing) stabilizers for the
  anchor-`0` setting.

## Reproducibility

- `output/artifacts/verify.py` (SHA256
  `7de4aab4449804cfd8576ced45a7764a38735e9363cb2c94618df1c9175d3341`),
  stdlib only, seconds-scale, prints `VERIFY_OK`.
- Independent audit re-ran the script, re-enumerated the fiber, the 1080
  lines, cap/maximality properties, stabilizers, transitivity, and the
  15-pair table, all matching.

## References

- M. Follett et al., Partitions of AG(4,3) into Maximal Caps,
  https://arxiv.org/abs/1302.4703
- J. Awan et al., Demicaps in AG(4,3) and Their Relation to Maximal Cap
  Partitions, https://arxiv.org/abs/2106.14141
- G. Pellegrino / R. Hill: maximal-cap size 20 in AG(4,3) and affine
  equivalence (background).
- Anbar et al., Small complete caps from nodal cubics,
  https://arxiv.org/abs/1305.3019 (infinite-family context only).
