# Scientific review

## Correctness — PASS
The Euclidean parallelogram support-width formula is exact, and its Haar second moment is integrated without probabilistic approximation. Fixing perimeter and area reduces all shapes to one side-product interval. A derivative calculation gives a positive, strictly decreasing derivative on that interval, with the two exact endpoint slopes. This proves strict reconstruction, sharp rectangle/rhombus extrema, global two-sided inverse bounds, and equality classifications. The standalone `verify.py` successfully replayed 1,215 analytic-formula, quadrature, monotonicity, and reconstruction checks; these finite checks corroborate but do not prove the result.

## Originality — PASS, with residual risk
The closest accessible published parallelogram inverse theorem, *Three unlabeled width statistics reconstruct a parallelogram with sharp stability* (October 11, 2026), was read in full. It uses maximum width as its third statistic and supplies the mean-square formula credited here. No implication yields area-calibrated three-scalar uniqueness or the sharp fixed-area slope without the new monotonicity step. Kim–Yaskin–Zvavitch (2015) address broader full distribution questions; Martirosyan–Sargsyan (May 2026) recognize triangles from chord integrals. Those primary scopes and the available results do not establish the new assertion. Similar historical results could remain unindexed; two less decisive manuscripts were not fully accessible.

## Value — PASS
The theorem replaces optimizing the directional width by knowing ordinary area while retaining only two population width moments. It gives complete shape recovery for all genuine parallelograms, a sharp isoperimetric variance envelope at prescribed area/perimeter, and the optimal positive condition number for recovering the side product. These exact quantitative statements address a natural inverse integral-geometry question and are not mere recalculations of a known isolated table entry.

## Limitations
Only full-angle population measurements are considered; empirical finite-direction estimation and other quadrilaterals are outside scope. Conditioning degenerates for shapes tending to segments. The result has undergone self-review only, not independent validation. Broad historical priority is not certified.

Self-review: passed. Independent audit: not yet performed.
