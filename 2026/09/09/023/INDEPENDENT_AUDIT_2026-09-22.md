# Independent audit — 2026-09-22

Record: SCOPE-20260909-023. Examined 2026-09-26.

## Correctness — PASS
The committed verifier independently replayed all 801 planar diagrams, exact state sums and reference Jones comparisons: `VERIFY_OK` for 801/801. I separately parsed all diagrams and table polynomials and used a fresh disjoint-set smoothing calculation for both uniform states and every single-crossing flip. All 801 span, deficit, circle, A/B-adequacy and diagram Turaev-genus fields agree. Deficit counts are 563,18,170,40,7,1,1,1 for deficits 0–7. The sole deficit-seven entry is K11n19; the next are K11n57 (six) and 10_132 (five). An independently coded 2^11-term bracket sum for K11n19 yields `q²−q+1−q⁻¹+q⁻²`, span four at crossing number eleven. Knot Atlas directly confirms its diagram, DT code and Jones polynomial. The census concerns its committed minimal diagrams; adequacy and the computed Turaev genus here are diagram properties.

## Originality — PASS, narrowly
Knot Atlas already publishes the diagrams and individual Jones polynomials, including the K11n19 witness. Classical span and adequacy theorems and prior Turaev-genus work supply the conceptual setting. The checked sources do not give this exact joint 801-row deficit/adequacy/state-surface distribution or the finite-range uniqueness statement. The witness polynomial and the general theory themselves are not new.

## Scientific value — PASS, bounded
The joint table identifies the maximum deficit and its adequacy behavior across a standard closed prime-knot range and provides exact reproducible data. It is a finite database analysis, not a new general knot theorem; extending the crossing range could change the extremal.

Sources: [Knot Atlas K11n19](https://katlas.org/wiki/K11n19), [KnotInfo about its data](https://knotinfo.org/homelinks/about.html), [Kalfagianni–Lee, arXiv:2108.12391](https://arxiv.org/abs/2108.12391). Repository evidence: `artifacts/katlas_source.json`, `census_table.csv`, `knotlib.py`, `verify.py`.
