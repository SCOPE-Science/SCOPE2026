# Arithmetic bitangent separation on the honeycomb tropical quartic

## Context
Smooth tropical plane quartics carry 7 bitangent classes, each lifting to 4
algebraic bitangents over an algebraic closure (Baker–Len–Morrison–Pflueger–Ren;
Len–Markwig genericity). Over a Henselian valued field, Markwig–Payne–Shaw
(2023) express rationality obstructions via edge twisting (depending on the
tropicalization plus initial coefficients mod squares) and compute
Grothendieck–Witt (A¹-enumerative) multiplicities from the same data, with 2H
(twice the hyperbolic plane) for most/compact classes and listed Appendix A.3
exceptions. Cueto–Markwig classify tropical bitangent deformation types (41
types) with 0-or-4 real-lift sign rules. No prior source logs a valuated
honeycomb quartic with initials, twist vector, or GW profile.

## Definitions
- `T_H`: the honeycomb unimodular triangulation of `4Δ₂` (16 unit triangles).
- `K = Q((t))`: Henselian discretely valued field, residue field `k = Q`
  (characteristic 0), value group `Z`. All twist radicands below have t-adic
  valuation 0, so nonsquare decisions reduce to residues.
- `Q*`: the valuated quartic `Q = Σ Aᵢⱼ xⁱyʲz⁴⁻ⁱ⁻ʲ` with
  `Aᵢⱼ = aᵢⱼ·t^(−Hh(i,j))`, `Hh(i,j) = −(i²+j²+k²)` (`k = 4−i−j`), initials
  `a*` with `a₁₁ = 2` and all other `aᵢⱼ = 1` (see `artifacts/qstar.json`).
- Generic weights `w` (see `artifacts/generic_pert.json`) keep the same regular
  cells `T_H` and resolve each `BM+(yz)` motif to shape `B` (dots 3/2, 5/2,
  −3/2, all nonzero).
- `B*_3`: the first `BM+(yz)` motif in polymake ordering, triangles
  `[[4,5,8],[4,7,8],[6,7,11]]`, sym 0 (GW-table row `B*_4`; label fixed
  throughout). Extension index map:
  `0:(0,0) 1:(1,0) 2:(0,1) 3:(2,0) 4:(1,1) 5:(0,2) 6:(3,0) 7:(2,1) 8:(1,2)
  9:(0,3) 10:(4,0) 11:(3,1) 12:(2,2) 13:(1,3) 14:(0,4)`.
- Focus edge `e* = ((1,2),(2,1))` (dual edge `(7,8)`), apexes `r = (1,1)`,
  `r′ = (2,2)`, `δ = 1`. MPS Def 3.5 radicand
  `R* = (−1)·a₁₁·a₂₂·a₁₂·a₂₁ = −2`.

## Result
For `Q*` as above, the 7 tropical bitangent classes have certified
Cueto–Markwig deformation types **3×A, 3×B, 1×C** (B resolved from `BM+(yz)`
at generic weights by the extension hyperplane rule), and the
Grothendieck–Witt multiplicity vector is `v_GW = (2H)×7 = 14H` of total
quadratic degree 28. The named class `B*_3` has **4 geometric lifts, 0 over
`Q((t))`**, obstructed by the twisted edge `e*` with certified nonsquare
radicand `R* = −2`.

## Proof / evidence
- `T_H`: 16 unit-area triangles (exact upper-hull check), regular under `w`,
  16 distinct dual vertices, compact genus `18−16+1 = 3` (smooth).
  Replay: `artifacts/honeycomb_cert.py`, `artifacts/replay_fallback.py`.
- Motifs: verbatim port of TropicalQuarticCurves-0.1 `check_*` rules (static
  tables parsed from the vendored 113-statement rules excerpt
  `artifacts/vendor/compute_motifs_declares.rules.txt`, origin+sha256 in
  `artifacts/vendor/SOURCES.json`). Validated against the vendored extension
  testsuite file `artifacts/vendor/10.poly` (all 7 stored motifs reproduced,
  FULL10 PASS). On `T_H` the port yields exactly 7 motifs `3×A/3×BM+(yz)/1×C`;
  hyperplane dots resolve `BM+(yz)→B`. A/BM subset additionally cross-checked
  inside the polymake 4.11 binary (S3 size 6, sets identical). The extension
  C++ motif rule is blocked in-env (logged); nothing polymake-dependent is
  faked.
- Incidence (`artifacts/check_incidence.py` → INCIDENCE_OK): `(7,8) = e*`;
  motif triangle `[4,7,8]` contains it; `T_H` triangles sharing `(7,8)` are
  `[4,8,7],[8,7,12]` with apexes `(1,1),(2,2)`, `δ = 1`. Shape-B overlap
  tangency plus the logged all-18-bounded-edges-twisted table
  (`artifacts/twist_gw.py`: twisted count 18) makes the overlap tangency
  twisted; `R* = −2` is the certified representative nonsquare ratio
  (negative in `Q`, `|R*| = 2` not a square; valuation 0 even).
- Obstruction: MPS Lemma 3.4 (line-coefficient lifts need `√R*` up to a
  monomial square) + Prop 3.8 (equation defined over `K` iff untwisted) +
  Thm 3.14 (all four lifts of a class share one obstruction) ⇒ 4 geometric,
  0 `K`-rational lifts.
- GW class-by-class (`artifacts/check_gw_table.py` → GW_TABLE_OK,
  `artifacts/gw_table.json`): every shape (A/B/C) lies in the MPS Thm A.2 2H
  list and outside the App. A.3 exception sets, and is compact (Thm 1.7
  cover); hence 2H per class, total 14H, degree 28. Trace/pairing mechanics
  replayed: matrix `[[0,−4s],[−4s,0]] = H` (TRACE_IS_H_OK), Lemma-4.18
  shape-B sign pairing (QTYPE_PAIR_OK).
- Master replay `artifacts/replay_fallback.py` prints FALLBACK_REPLAY_PASS
  (exit 0); clean-checkout rerun log confirms EXIT 0.

## Limitations
- Residue characteristic 0 (Q), tame Henselian `K = Q((t))` only; value group
  Z with all radicands at valuation 0 (unramified-part argument).
- Full 7-type enumeration via the testsuite-validated verbatim port (C++
  motif rule blocked in-env, logged); A/BM subset cross-checked in polymake.
- Only `B*_3`'s rationality verdict is proved 0; other classes' verdicts
  follow the logged twist table under MPS Thm 3.14.
- Cone-wide honeycomb census stays open; this is the atomic single-quartic
  fallback, not the target.

## Reproducibility
From `output/artifacts/`, run `python3 replay_fallback.py` (expects
FALLBACK_REPLAY_PASS, exit 0). Inputs read from the vendored copies
(`vendor/10.poly`, `vendor/compute_motifs_declares.rules.txt`);
no absolute `scratch/` paths remain in the replay path.

## References
- H. Markwig, S. Payne, K. Shaw, Bitangents to plane quartics via tropical
  geometry: rationality, A¹-enumeration, and real signed count,
  arXiv:2207.01305 (Res. Math. Sci. 10 (2023), no. 2, Paper No. 21).
- M. A. Cueto, H. Markwig, Combinatorics and real lifts of bitangents to
  tropical quartic curves.
- A. Geiger, M. Panizzut, A tropical count of real bitangents to plane
  quartic curves; TropicalQuarticCurves polymake extension + polyDB
  QuarticCurves collection (https://polymake.org/doku.php/extensions/tropicalquarticcurves).
- M. Baker et al., Bitangents of tropical plane quartic curves
  (arXiv:1710.10126).
