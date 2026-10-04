# Review of Quasiregularity restores Gabriel's convex-curve inequality at the endpoint

## Correctness

PASS. The proof reconstructs the endpoint estimate from first principles. For \(f=h+\overline g\), the singular values are \(|h'|\pm|g'|\), and \(K\)-quasiregularity gives the exact lower bound
\[
\frac{(|h'|-|g'|)^2}{|h'|^2+|g'|^2}\ge\frac2{K^2+1}.
\]
Regularizing both \(|f|\) and the Euclidean norm of \((h,g)\) yields smooth positive functions. Their Laplacians satisfy an explicit comparison with constant \(1/(\sqrt2(K^2+1))\). Green's radial-mean identity then gives uniform \(H^1\) control of both analytic components by the harmonic \(\mathbf h^1\) norm. The normalization \(g(0)=0\) is exactly what makes the two center terms agree in the limit. Analytic \(H^1\) boundary convergence and the sharp analytic Gabriel theorem complete the convex-curve estimate. The proof handles zeros by regularization and does not infer an infinite statement from finite computation.

## Originality

PASS. The full motivating preprint was inspected. It proves harmonic \(K\)-quasiregular convex-curve estimates for \(p>1\), with a special improved theorem at \(p=2\), and explicitly poses the restoration problem at \(p=1\) or below. It does not state the endpoint theorem proved here. Das's full harmonic Hardy-space paper proves that the unrestricted theorem fails at \(p\le1\), so it cannot imply the accepted positive result. The inspected harmonic-quasiregular Zygmund paper concerns component integrability under different hypotheses and does not state a convex-curve Gabriel theorem. General quasiregular Hardy-space maximal theorems require additional growth or multiplicity assumptions not present here.

Published-finding searches covered the source problem, the \(p=1\) endpoint, harmonic quasiregularity, convex curves, analytic-component formulations, and maximal-function aliases. No returned finding stated this theorem or a stronger theorem on the same class. A residual risk remains that an equivalent corollary may appear under older Hardy-space terminology not surfaced by the searches.

## Value

PASS. The motivating paper ends with the explicit question of which quasiregular assumptions restore Gabriel control at the excluded endpoint. The unrestricted harmonic theorem is known to fail at \(p=1\), while the accepted result shows that the central harmonic \(K\)-quasiregular subclass recovers a full boundary-norm convex-curve inequality with an explicit distortion dependence. The key structural content is that quasiregularity suppresses the endpoint cancellation obstruction strongly enough to force both analytic components into \(H^1\). This is a natural endpoint theorem tied directly to a published open problem, not an arbitrary parameter specialization.

Same-model review: passed. Independent audit: not yet performed.
