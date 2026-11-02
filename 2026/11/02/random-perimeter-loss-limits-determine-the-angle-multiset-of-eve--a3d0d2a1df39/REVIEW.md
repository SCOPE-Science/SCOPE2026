# Scientific assessment

## Correctness — PASS
For every fixed convex polygon with genuine corners, the sampled-hull perimeter has an exact corner-chord decomposition whenever each side receives a sample. The probability of an empty side is exponentially small. Joint exponential endpoint-gap limits give the distributional and all-fixed-moment convergence. The individual corner MGF is an explicit one-dimensional gamma mixture, finite precisely to a critical positive value that increases strictly with its angle. A local quadratic maximum produces a \((1-z/z_\alpha)^{-3/2}\) singularity; the first singularity and its exponent identify the minimum angle and multiplicity, and finite cancellation proves uniqueness of the complete multiset. The supplemental Python checker completed 1787 checks, including exact geometric comparisons and numerical singularity asymptotics. The proof, not numerical extrapolation, supports the infinite-dimensional probability statement.

## Originality — PASS, subject to independent historical review
Closest inspected primary sources concern expected intrinsic-volume deficits for rolling-ball bodies (Böröczky–Fodor–Hug, 2011), boundary-sampled polytope expected volume/face data (Reitzner–Schütt–Werner, 2019), and Hausdorff approximation with the relevant vertex Poisson processes (Prochno–Schütt–Sonnleitner–Werner, 2024). The last paper provides a known ingredient for the forward asymptotic law, which is not claimed in isolation as original. Its inspected analysis does not give the singularity-based inverse identification of the full angle multiset from perimeter losses. An earlier equivalent perimeter law or angle-identification statement remains a real priority risk; no independent audit is represented.

## Mathematical value — PASS
The inverse statement classifies exactly which local geometric data a natural stochastic boundary-measurement limit retains: every angle, with multiplicities, but not side lengths. This distinction between full angular identifiability and failure of metric-shape reconstruction is not a normalization trick or an arbitrary parameter slice. The theorem holds for all fixed convex polygons, not only regular cases. No finite-data conditioning, numerical inversion stability, or polygonal side reconstruction is claimed.

## Closest literature and limitations
Böröczky–Fodor–Hug, arXiv:1103.4978v1 (2011); Reitzner–Schütt–Werner, arXiv:1911.05917v1 (2019); Prochno–Schütt–Sonnleitner–Werner, arXiv:2404.02870v1 (2024). The 2024 result directly supplies the local corner point processes and therefore is stronger than an unrelated citation; the retained result uses those ingredients toward a distinct inverse observable and theorem.

Self-review: passed. Independent audit: not yet performed.
