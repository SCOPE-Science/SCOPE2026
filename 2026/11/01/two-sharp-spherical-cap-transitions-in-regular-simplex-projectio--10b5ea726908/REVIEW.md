# Review of the two-transition regular-simplex width theorem

## Correctness — PASS

The claim is for every integer \(d\ge3\), Haar-uniform line directions, a unit-edge simplex, and thresholds \(b=\sqrt{2/3}\) and \(a=\sqrt3/2\). Centering and scaling the standard simplex gives exactly the directed type-\(A\) roots. Their discrete Gram inner products show that all cap intersections above \(b\) are either individual caps or pairs with inner product \(1/2\); every possible triple has a common-root endpoint and maximum simultaneous contact \(b\). There are \(d(d+1)(d-1)\) eligible unordered pairs. The one-dimensional lens integral follows from the exact conditional spherical coordinate distribution. The positive explicit asymptotic coefficient follows from a bounded local spherical-chart scaling and dominated convergence; no experiment substitutes for that proof. The standalone checker was executed with both root enumeration and numerical lens comparisons, and all tests passed.

## Originality — PASS, subject to historical priority

The closest directly relevant full texts were Har-Peled–Robson (arXiv:2301.02616, Jan. 6, 2023), which computes minimum widths; Finch (arXiv:1110.0671), which calculates tetrahedral first and second moments and explicitly reports unknown densities at the time; and Kabluchko–Litvak–Zaporozhets (arXiv:1511.08479), which provides all random-width moments implicitly determining the distribution. The latter has broader moment coverage, not the explicit two-regime edge-root cap-union formula or its first-overlap asymptotic. The published cube first-spherical-cap-transition result covers a different family and different normal configuration, while the regular-simplex-vertex cap-union result concerns caps centered at vertices rather than the simplex's directed edge differences. The assertion of originality is limited to the explicit high-tail classification and sharp transition, not the general cap or Gaussian moment methods. A previously unknown equivalent root-system cap formula remains possible.

## Mathematical value — PASS

The exact dimension-independent thresholds and their geometrically classified intersection multiplicities turn an implicit distribution into two explicitly computable regimes in every dimension. The onset exponent and coefficient quantify the first singularity in a canonical random-width law; the tetrahedral upper tail simplifies to a uniform conditional distribution. This is a natural all-dimensional geometric probability benchmark, not a parameter substitution or an arbitrary numerical slice. The work does not claim a full lower-tail distribution, a joint high-dimensional limit or finite-sample inference.

## Status and boundaries

No independent review is represented as completed. The upper-tail result rests on elementary exact geometric arguments, with finite machine checks supplementary. Novelty remains historical-priority provisional, especially in older spherical root-system literature.

Self-review: passed. Independent audit: not yet performed.
