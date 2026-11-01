# Scientific assessment: exact rectangular-box mean-projection-body deficit

## Correctness — PASS
The definition uses probability-normalized integration over two-planes containing each support direction. Projected rectangular-box area gives the displayed disk-support decomposition with coefficient \(8/\pi\). The zonoid determinant formula computes every repeated-index mixed-volume coefficient as \(2\pi\); the distinct-index coefficient cancels for equal box volumes. Direct algebra gives the exact normalized deficit, and the elementary hyperbolic-cosine inequality gives globally sharp logarithmic stability. The analytic proof covers all strictly positive half-side lengths. Finite rational and numerical checks are supplemental, not certificates of the infinite statements.

## Originality — PASS, provisional historical priority
The 2026 source establishes general log-concavity of intrinsic volumes of mean-projection bodies, not the exact three-dimensional orthotope volume deficit. The two inspected primary sources on discotopes describe the three-disk body, including its algebraic boundary/fiber-body structure, but do not state the sharp fixed-volume expression and its log-aspect stability. A previously indexed exact orthotope result determines the **support and Euclidean radii** of this image, not its three-dimensional volume. A search result on the volume of the **convex hull** of three orthogonal disks is not interchangeable with the present **Minkowski sum**. Residual risk: an older mixed-volume table or zonoid calculation might contain the same polynomial and make the stability statement an immediate corollary. The exact source comparison has not been independently audited.

## Mathematical value — PASS
Mean-projection-body volume is a natural intrinsic-volume statistic newly featured in the motivating literature. Rectangular boxes provide the fundamental fully anisotropic test family; their image is a genuinely curved three-disk discotope. The result gives a complete sharp, globally quantified, scale-invariant stability law for its volume (and an optimal logarithmic modulus), rather than a routine special-case numerical evaluation or an unmotivated parameter slice. It does not claim all-convex-body extremality.

## Reproducibility and limitations
The standalone program `verify.py` performs 125 exact-rational tests, quadrature convergence checks, and independent inscribed-hull comparisons. Independent mathematical audit and final historical priority remain outstanding.

Self-review: passed. Independent audit: not yet performed.
