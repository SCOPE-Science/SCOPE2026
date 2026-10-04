# Review

## Correctness

PASS. For a pair of vertices at cyclic separation \(k\), the smallest possible maximal cyclic separation from a vertex center is exactly \(\lceil k/2\rceil\). Because chord length increases with cyclic separation up to a half-turn, this gives
\[
\operatorname{hd}=2d_{\lceil k/2\rceil}
\]
and hence an exact one-variable sequence of leipodistances.

Every even term is strictly smaller than the preceding odd term. The odd terms form a strictly increasing sequence because the continuous interpolation
\[
F(u)=4R\sin u-2R\sin(2u-t)
\]
has
\[
F'(u)=4R(\cos u-\cos(2u-t))\ge0
\]
throughout the admissible interval. The largest admissible odd separation therefore gives the global gap. Substitution yields the four residue-class expressions, and direct Taylor expansion yields the convergence profile.

The standalone checker exhausts all pairs and all candidate centers for every \(3\le n\le80\) and independently agrees with both formula forms. It is not used as evidence for the all-\(n\) step.

## Originality

PASS with residual terminology risk. The defining Geller–Misiurewicz paper was inspected at the definitions of hyperdistance, leipodistance, and gap, the exact Euclidean-sphere example, and the Hausdorff continuity lemma. Its accessible full text contains no occurrence of “polygon,” and it gives no finite regular sampling formula.

Targeted published-finding corpus searches and public web searches used the distinctive terms “leipodistance,” “hyperdistance,” and “convexity gap” together with regular polygon, cyclic metric, chord metric, and circle approximation. No equivalent statement or stronger result implying the exact modulo-\(4\) formula was located.

The closest indexed same-object result is a regular-hexagon minimal-filling theorem, which uses a different invariant. A prior own result computes Gromov four-point hyperbolicity for the same regular-polygon chord metric, but hyperbolicity optimizes four-point pair sums, whereas the present gap optimizes midpoint failure for pairs; neither statement implies the other.

## Value

PASS. The gap was introduced specifically as a quantitative measure of missing midpoints and nonconvexity, and the source computes the continuous circle as a model example while proving only a general Hausdorff stability estimate. Regular polygon vertices are the canonical finite samples of that circle. The theorem gives the exact discretization error, identifies the extremizing pair, and reveals a genuine arithmetic effect: one congruence class converges quadratically while the other three carry first-order signed errors.

Same-model review: passed. Independent audit: not yet performed.
