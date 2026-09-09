# Jones-span deficit and adequacy census for prime knots through 11 crossings, with unique maximal-deficit extremal K11n19 (D* = 7)

## Context

The Kauffman–Murasugi–Thistlethwaite theorem says the Jones-polynomial span
(breadth) equals the crossing number for reduced alternating diagrams.
Thistlethwaite proved the general bound span ≤ c and characterized connected
prime diagrams of breadth c−1. The Dasbach–Lin / Abe / Armond–Lowrance / Kim
program bounds Jones span via Turaev-genus and adequacy data. The pre-existing
question is quantitative: over a complete tabulated range, how far do
nonalternating diagrams fall short of maximal span, and how does the shortfall
(deficit) track adequacy and diagram Turaev genus? This record answers it at
the standard Hoste–Thistlethwaite range: all prime knots through 11 crossings.

## Definitions

- Committed diagrams: the KnotAtlas PD presentation per knot (801 knots:
  Rolfsen 3_1–10_165, K11a1–K11a367, K11n1–K11n185); DT codes committed
  alongside. `c(K)` = crossing number = DT length = PD crossing count.
- PD convention: `X_ijkl` positions (0,1,2,3) = (a,b,c,d), counterclockwise
  from the incoming lower edge (KnotTheory convention).
- Positional A/B smoothings (uniform at every crossing, sign-independent):
  A = P_ad P_bc = pairs (0,3)&(1,2); B = P_ab P_cd = pairs (0,1)&(2,3).
  `|s_A|`, `|s_B|` = circle counts of the uniform all-A / all-B states.
- Adequacy (positional): A-adequate iff every single A→B flip state has
  exactly `|s_A|−1` circles; B-adequate mirrored; adequate = both.
- Kauffman bracket: `⟨X⟩ = A^{−1}⟨A-smoothing⟩ + A⟨B-smoothing⟩`,
  `⟨unknot⟩ = 1`, `⟨L ⊔ O⟩ = (−A²−A^{−2})⟨L⟩`, full 2^c state sum
  (c ≤ 11, ≤ 2048 states), exact integer polynomial arithmetic.
  Jones: `V(q) = (−A³)^{−w}⟨K⟩` at `A = q^{−1/4}`, `w` = geometric writhe
  from straight-through tracing (under 0↔2, over 1↔3); bracket exponents
  minus 3w always divisible by 4.
- Span `s(K)` = maxdeg − mindeg of `V(K)`; deficit `d(K) = c(K) − s(K)`.
- Diagram Turaev genus `g_T(D) = (2 + c − |s_A| − |s_B|)/2` (integral,
  nonnegative on all rows).
- Orientation/components: straight-through arrival walk; each component
  contributes two directed cycles, so ncomp = (#cycles)/2 = 1 on all rows.

## Result

Over the 801 committed diagrams, recomputed from scratch in stdlib-only
Python with 801/801 exact Jones matches against the committed reference:

- Deficit distribution: d=0: 563; d=1: 18; d=2: 170; d=3: 40; d=4: 7;
  d=5: 1; d=6: 1; d=7: 1.
- By crossing number: c=8: {0:18, 2:2, 3:1}; c=9: {0:41, 2:6, 3:2};
  c=10: {0:123, 1:3, 2:32, 3:5, 4:1, 5:1};
  c=11: {0:367, 1:15, 2:130, 3:32, 4:6, 6:1, 7:1}.
- Maximal deficit is unique: **D* = 7, attained only by K11n19**.
  Runner-up K11n57 (d=6), then 10_132 (d=5).
- Deficit-1 stratum (18 knots): 10_152, 10_153, 10_154, K11n6, K11n9,
  K11n31, K11n34, K11n39, K11n42, K11n45, K11n67, K11n73, K11n74, K11n77,
  K11n80, K11n97, K11n151, K11n152 — all adequate with diagram Turaev
  genus exactly 1.
- Lockstep on this range: deficit ≤ 1 ⟺ adequate (563 deficit-0 + 18
  deficit-1 = all 581 adequate diagrams; every deficit ≥ 2 diagram is
  inadequate). Semi-adequacy: A-only 73, B-only 145, both-inadequate 2
  (K11n95, K11n118, both d=4).
- g_T distribution: 0: 563 (= deficit-0 set), 1: 204, 2: 33, 3: 1
  (K11n95: c=11, d=4, |s_A|=3, |s_B|=4). span ≤ c and deficit ≥ g_T on
  every row.
- Extremal witness K11n19: DT `4 8 10 -16 2 -18 -20 -22 -6 -12 -14`
  (c=11); signs [+1,−1,+1,+1,−1,−1,−1,−1,+1,−1,−1], writhe −3, ncomp 1;
  `V = q² − q + 1 − q^{−1} + q^{−2}` (span 4, deficit 7);
  `|s_A| = 4`, `|s_B| = 7`, `g_T = 1`; all-A single flips all 3
  (A-adequate); all-B single flips [6,6,8,6,6,6,6,6,6,6,6] vs 7 —
  B-inadequate with named failing crossing 2 (A-adequate-only).
- Runners-up: K11n57 (DT `4 8 -14 2 -16 -18 -20 -6 -10 -22 -12`,
  `V = −q⁶+q⁵−q⁴+2q³−q²+q`, span 5, d=6, |s_A|=7, |s_B|=4,
  B-adequate-only, g_T=1); 10_132 (DT `4 8 -12 2 -16 -6 -20 -18 -10 -14`,
  `V = −q^{−7}+q^{−6}−q^{−5}+q^{−4}+q^{−2}`, span 5, d=5,
  |s_A|=6, |s_B|=4, B-adequate-only, g_T=1).

## Proof / evidence

Exhaustive computational proof (certified enumeration), not an analytic
theorem. Pipeline (`knotlib.py`, stdlib only): parse PD →
straight-through trace (ncomp, signs/writhe + independent local
consecutive-edge-rule cross-check) → positional-A/B Kauffman-bracket
state sum → writhe-normalized Jones (exact) → positional all-A/all-B
circles + single-flip adequacy + g_T formula. Full rerun ≈ 20 s.

1. Jones replay: recomputed V(K) compared coefficient-for-coefficient
   against the committed reference — 801/801 exact matches (pins
   smoothing weights and writhe).
2. Diagram audit: DT length = PD crossing count = c on all rows;
   ncomp = 1 on all rows; traced signs = local rule on all rows;
   bracket-exponent divisibility asserted per knot.
3. Sorting the certified table gives maximum deficit 7 at the single
   row K11n19; runners-up order asserted and checked.
4. Tripwires: all 367 alternating K11a diagrams deficit-0/adequate/gT-0;
   deficit-0 set = adequate ∩ gT-0 exactly; span ≤ c everywhere.
5. Independent replay: `verify.py` reads only `knotlib.py`,
   `katlas_source.json`, `census_table.csv` (no network), redoes the
   whole computation and checks every column plus extremal uniqueness
   and deficit-1 certificates → `VERIFY_OK` (also from an isolated
   artifacts copy). Auditor re-execution confirmed `VERIFY_OK`.

## Limitations

- Adequacy, |s_A|, |s_B|, g_T are diagram invariants of the committed
  (KnotAtlas minimal) diagrams under the stated positional A/B
  convention, not knot invariants; deficit d = c − span uses the knot's
  crossing number and Jones polynomial, hence is a knot invariant. The
  extremal uniqueness is over this closed finite table.
- Reference Jones values/diagrams come from KnotAtlas (committed copy
  `katlas_source.json`); the contribution is the independent
  recomputation plus the joined adequacy/state-surface/extremal
  certificate with a byte-level replay path.
- General theorems (KMT sharpness, Thistlethwaite breadth bound and
  c−1 characterization, Dasbach–Lin/Abe/Armond–Lowrance span–genus
  relations) are consistency checks and attribution only; the
  deficit-1 discussion certifies adequacy + breadth c−1 per diagram,
  not a new proof of the general theorem nor almost-alternating
  classification of the 18.

## Reproducibility

Self-contained artifacts: `knotlib.py`, `katlas_source.json`,
`census_table.csv` (801 rows: knot, c, span, deficit, sA, sB, adequacy
flags, gT, writhe, ncomp, jones_match, Jones coefficients),
`dt_codes.txt`, `extremal_witnesses.json` (K11n19, K11n57, 10_132,
10_124 with PD, signs, writhe, ncomp, Jones, state data, convention,
full single-flip logs), `deficit1_stratum.json` (18 knots),
`verify.py`. Run `python3 verify.py` (or
`python3 verify.py --artifacts <dir>`) → `VERIFY_OK`.

## References

- Kauffman, Murasugi, Thistlethwaite — KMT span theorem.
- Thistlethwaite, "An upper bound for the breadth of the Jones
  polynomial", Math. Proc. Cambridge Philos. Soc. 1988.
- Dasbach–Futer–Kalfagianni–Lin–Stoltzfus, "The Jones polynomial and
  graphs on surfaces", J. Combin. Theory Ser. B 98/2 (2008).
- Armond–Lowrance, "Turaev genus and alternating decompositions",
  Algebr. Geom. Topol. 17 (2017); Kim, "Link diagrams with low Turaev
  genus", Proc. AMS (2018).
- KnotAtlas (katlas.org) — PD presentations, DT codes, Jones
  polynomials (diagram source / computation reference).
