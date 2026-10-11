# Scientific review: difference-body distance beta bound

## Correctness — PASS

The claim quantifies over every full-dimensional compact convex body in dimension \(d\ge2\), every threshold \(t\in[0,1]\), and every positive moment exponent. The proof derives the exact law of a uniform random difference from the covariogram and proves, by Brunn–Minkowski, that its \(d\)-th root is concave. Normalizing every ray by the radial function of the difference body makes the ratio to \((1-t)^d\) nondecreasing. The resulting conditional monotone-likelihood-ratio inequality proves the full CDF comparison, not merely a mean bound. Its strict form and the sharp Rogers–Shephard equality case establish the simplex-only characterization. A direct barycentric overlap computation gives equality for every simplex. The beta moment constants, including mean and variance, have been checked exactly; the packaged program independently checks exact identities and finite diagnostics. The program alone is not an infinite-dimensional certificate.

## Originality — PASS, with explicit historical risk

Averkov–Bianchi (2007) studies covariogram reconstruction and makes the uniform-pair difference interpretation explicit, but its cited theorems concern geometric identification. Gardner–Zhang (1998) provides radial mean-body comparisons; Wang–Zhang (2014) reproduces its inclusion and Rogers–Shephard consequences. Langharst (2022) explicitly proves covariogram root-concavity (Proposition 2.5), simplex rigidity (Proposition 2.6) and radial-measure inequalities (Lemma 3.2 and Theorem 3.4). Those hypotheses and intermediate observations are acknowledged, but the inspected results do not formulate a first-order stochastic order for the random gauge \(\gamma_{K-K}(X-Y)\) against the fixed beta distribution, uniformly at every radius. This comparison is not a fixed directional moment inequality or the Rogers–Shephard bound alone. The full 1998 paper was not available to inspect, so equivalent older formulations remain a material priority risk and independent historical review is required.

## Value — PASS

The intrinsic difference-body gauge is affine invariant and directly measures the relative displacement of a randomly chosen pair inside a convex body. The theorem gives a sharp all-dimensional concentration benchmark **at every quantile**, not an arbitrarily selected finite parameter. It singles out simplices as the unique joint minimizers, yields every positive-moment inequality at once, and can distinguish canonical nonsimplices such as planar squares by an exact polynomial CDF gap. The result is motivated by covariogram and radial-mean-body geometry; its novelty is the sharp stochastic comparison and equality law, not the classical concavity or volume ingredients.

## Closest literature and limits

The sharp difference-body volume inequality of Rogers–Shephard, the radial mean-body family of Gardner–Zhang, and Langharst's covariogram equality criterion are the closest structural inputs. The conclusion assumes independent uniform points and the exact body-specific difference-body gauge. It does not address Euclidean separation, dependent points, nonconvex bodies, or stability rates. A historically equivalent beta comparison under another name may exist; available searches and identified results do not establish exhaustive priority.

Same-model review: passed. Independent audit: not yet performed.
