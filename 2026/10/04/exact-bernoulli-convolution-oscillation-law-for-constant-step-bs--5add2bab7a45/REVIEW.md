# Same-model review

## Correctness
PASS. The proximal subproblem is solved exactly, giving the affine recursion \(x_{k+1}=r x_k+(1-r)c\xi_k\) with \(r=(1+\alpha a)^{-1}\). Iterating the recursion gives the finite-time representation. A same-noise coupling contracts distances by the exact factor \(r\), proving uniqueness of the invariant law and geometric \(W_1\) convergence. Independence and centering of the Rademacher signs give the stated second moment and objective floor. The support trichotomy follows by comparing the two affine images of \([-c,c]\); the critical law is the centered fair binary expansion and is uniform. The checker replays the algebra and a finite Monte Carlo sanity check, but the proof does not rely on simulation.

## Originality
PASS, subject to the residual risk stated below. The primary BSPPA paper gives the vanilla proximal update and describes constant-step oscillation/non-interpolation qualitatively. The 2024 SPPA variance-reduction paper gives the variance motivation and convergence framework. The 2019 constant-step stochastic forward-backward paper gives general Feller-chain and invariant-measure machinery, including affine monotone examples. Full-text inspection of the relevant material and targeted published-record searches found no statement implying the exact Bernoulli-series invariant law, the exact optimization-error floor, or the sharp \(\alpha a=1\) support transition for the two-symmetric-quadratic BSPPA instance. The Bernoulli-convolution support argument is classical probability/IFS mathematics; originality is claimed only for the explicit BSPPA specialization and its optimization interpretation.

## Value
PASS. Constant-step oscillation is a stated motivation for variance reduction in the primary source. This minimal non-interpolating strongly convex example shows exactly what that oscillation can be: a unique stationary law with a closed-form error floor whose support undergoes a qualitative interval-to-fractal transition at a natural dimensionless stepsize. The threshold separates two genuinely different stationary geometries rather than an arbitrary parameter slice and gives a reusable diagnostic model for constant-step stochastic proximal behavior.

## Closest literature and limitations
The closest inspected sources are arXiv:2510.16655v1, doi:10.1007/s10957-024-02502-6, and arXiv:1702.04144v3. They cover BSPPA/SPPA variance behavior and general constant-step invariant-measure theory, but not the exact claim above. An older equivalent two-map specialization may exist under different terminology; this remains the principal originality risk. The result is restricted to the stated scalar symmetric model and makes no density claim in the overlapping Bernoulli-convolution regime.

Same-model review: passed. Independent audit: not yet performed.
