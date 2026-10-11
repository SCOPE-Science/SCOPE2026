# Review of the circular-cone width law

## Correctness — PASS

For all positive cone radii and altitudes, the two support branches follow directly from the base disk and apex. Their monotone intervals and inverse Jacobians yield the full probability density, including overlapping image intervals. Exact comparisons of branch endpoints give the threshold \(h/r=\sqrt3\). The lower-support-edge density is zero on the broad branch and strictly positive on the slender branch; solving the endpoint equations then proves injection of the complete width law and the precise two-realization classification from endpoints. The proof covers \(h/r=1\) and \(h/r=\sqrt3\) explicitly. The extracted package's standard-library verifier passed 11140 supplementary numerical checks. Finite tests are not relied on for universal quantifiers.

## Originality — PASS, with residual literature risk

The inspected complete 2015 manuscript of Kim–Yaskin–Zvavitch concerns distribution functions of hyperplane-section and hyperplane-projection *areas*, not the one-dimensional random widths of finite cones. Pennell–Deignan's cone projection calculations concern planar projected area, while the abstract of Vickers–Brown concerns planar area and perimeter distributions; neither accessible statement entails this exact density and full inverse classification. Available research-record similarity searches against cone widths, line-projection distributions, exact aliases, and inverse geometric tomography disclosed no covering statement. Vickers–Brown was not accessible in full, so a prior equivalent width computation is an explicit residual risk. Absence of search hits is not treated as proof of historical novelty.

## Value — PASS

A complete natural two-parameter inverse classification under discarded orientation labels is substantively more informative than a routine expected-width integral. The exact two-to-one ambiguity for minimum/maximum width supplies a sharp failure-of-reconstruction boundary; the full density's lower-edge phase transition repairs the loss without supplying directional labels. The question connects directly to distributional geometric tomography of restricted convex-body families.

## Closest literature and limitations

See the three bibliographical sources in `RESULT.md` and the structured scientific comparisons in `AUDIT.json`. No claim is made for arbitrary convex bodies or noisy finite-sample inverse reconstruction. The potentially relevant 2001 planar-projection paper was seen only at abstract level; its complete statements have not been checked.

Same-model review: passed. Independent audit: not yet performed.
