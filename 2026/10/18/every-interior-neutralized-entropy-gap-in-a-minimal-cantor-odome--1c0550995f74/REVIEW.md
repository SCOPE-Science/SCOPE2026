# Review of the minimal Cantor-odometer realization

## Correctness

**PASS.** The real-coordinate embedding is injective because the first differing digit dominates the remaining tail by the explicitly positive factor \(1-2v\). The induced first-discrepancy metric is translation-invariant under the binary adding machine, so all iterates inherit one global bi-Lipschitz bound. Cylinder counts sandwich every neutralized separated-set count between powers of two with indices differing by a bounded amount. The level ratios oscillate to the prescribed values because each new superlong block dominates all predecessors. Unique ergodicity gives uniform empirical-measure convergence, making all eventually admissible PS sets equal to the entire phase space. The Haar measure of a neutralized Bowen ball is trapped between the same cylinder weights. These arguments cover every real \(0<L<U<1\) and every \(r>0\), rather than merely the checked finite instances.

## Originality

**PASS under the checked literature, with residual priority risk.** Chen–Xie–Zhou [1], Definitions 2.1/2.7 and Example 2.17, establish the definitions, the isometric entropy/box-dimension relation, and an upper/lower PS discrepancy in a nonminimal, non-uniquely-ergodic invariant set. Their Theorem 1.5 treats whole smooth manifolds. Rempe-Gillen–Urbański [2] establish nonautonomous fractal dimension machinery, not a minimal Euclidean Cantor adding machine's PS entropy. Dong–Qiao [3] study a hyperbolic-measure formula, not the claimed realization. Nothing here claims the isometry identity, classical Moran dimension estimates, or unique ergodicity of adding machines as original. The distinguishable combined statement is simultaneous **full interior-pair realization**, **minimality**, **unique ergodicity**, **uniform bi-Lipschitz control of every iterate in Euclidean distance**, and **equality of local/PS/topological neutralized profiles**. An unrecognized implicit specialization of classical odometer-fractal theory remains possible.

## Mathematical value

**PASS.** The first directly motivating PS-entropy gap example uses nonminimal components. The construction tests whether such oscillations disappear once there is only one dense orbit closure and one invariant measure: they do not, even when the map and all iterates have controlled metric distortion. More strongly, it realizes every interior profile \((rL,rU)\) with a single construction working for all neutralization rates, and identifies the exact geometric mechanism through small-scale cylinder dimensions. The object is the classical adding machine rather than an arbitrary unmotivated dynamical family; the precise two-parameter classification is the mathematical point of the result.

## Limitations and closest sources

The construction is confined to embedded Cantor sets and the strict interior \(0<L<U<1\). It does not extend to smooth ambient diffeomorphisms. Classical isometry identities and nonautonomous Moran calculations already provide substantial ingredients; any priority claim for their combination requires further independent review. The executable finite checker supports arithmetic and coding identities only and has no bearing on the infinite-asymptotic proof.

References: [1] Chen–Xie–Zhou, arXiv:2610.11639v1, especially §2 and Example 2.17; [2] Rempe-Gillen–Urbański, arXiv:1210.7469v4, especially §§1–2, 7; [3] Dong–Qiao, arXiv:2408.02397.

Self-review: passed. Independent audit: not yet performed.
