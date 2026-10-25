# Review of sharp three-moment tomography of rectangular solids

## Correctness — PASS

The proof gives the exact sampling law \(D^2=\sum_i s_i W_i\), where \(W_i\) are independent squared differences of unit uniforms. Their third cumulant is nonzero (\(11/945\)), making the first three moments a triangular invertible map to the first three power sums of squared edges. Newton's identities reconstruct the cubic without excluding repeated roots. The exact feasible region is obtained from the discriminant and strict positivity of the roots, with the singular cube endpoint and vanishing-edge boundary explicitly distinguished. Exact two-moment nonuniqueness and the optimal cube-root stability estimate follow from constructed pairs and Rouché root matching. A standalone checker independently derives multinomial moments and tests 2,197 positive rational squared-edge triples, four ambiguity pairs, and seeded simulation. Finite checks corroborate but do not prove the analytic statements.

## Originality — PASS, with risk

The selected observation is the **interior-point Euclidean distance**, not random probe intercepts, area-uniform distances in planar rectangles, cube-only forward moments, sphere-uniform directional width or random projection volume. The published cube results are special symmetric cases that cannot imply identification across the three-parameter positive shape family merely by having the same sampling label. The 2026 width tomography paper derives a sharp three-cumulant theorem and feasible region for a *different* random variable; its proof exploits the intrinsic volumes of a box rather than the third cumulant of a squared uniform-coordinate difference. The generic positive-cubic discriminant is elementary and is not claimed as an original algebraic theorem. The originality assessment attaches to the specific distance-moment observation and optimal inverse stability. Risk: an undetected earlier specialist solution could contain an equivalent moment identification or stability theorem; the 1999 cube manuscript was not available in full.

## Mathematical value — PASS

Uniform interior point pairs are a natural geometric sampling law, and their unlabeled one-dimensional distance statistics discard orientation and coordinate information. Identifiability from only three exact moments, together with the **complete observed-moment feasibility boundary**, makes the inverse question substantive: it distinguishes realizable empirical targets from impossible triples and demonstrates where the inverse becomes singular near cubes. Two moments lose a continuum of geometric information; the sharp \(1/3\)-Hölder modulus locates the precise worst-case inverse instability at the maximally symmetric shape. This is a coherent finite-statistic inverse theorem, not a single special-case numerical evaluation or arbitrary parameter slice.

## Closest literature and limitations

Mathai, Moschopoulos and Pederzoli (1999) calculate forward moments within a cube; Marsaglia, Narasimhan and Zaman (1990), and Bäsel (2012) treat planar rectangle/triangle distances. Coleman (1981) investigates random probe intercepts. Abas (2026), Theorem 6.8, reconstructs a box from random **directional-width** cumulants rather than the moments of distances between volume-uniform independent points. Detailed inspection of its inverse theorem supports this material distinction, not a claim of mathematical independence from all related ideas. The full Mathai manuscript was inaccessible through the checked routes. The constants in the stability bound are not asserted optimal and no finite-sample estimation guarantee is supplied.

Self-review: passed. Independent audit: not yet performed.
