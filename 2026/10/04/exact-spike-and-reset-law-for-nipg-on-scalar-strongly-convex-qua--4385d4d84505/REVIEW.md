# Same-model review

## Correctness

PASS. On the scalar quadratic, the exact proximal step and both source curvature quantities are elementary and give a complete recurrence. The source's strict test is exactly equivalent to \(a t_k>c_0\), so a violation resets the next stepsize to \(c_1/a\). The objective ratio is exactly \((1-a t_k)^2\), making \(a t_k\le2\) the exact nonincrease condition. The boundary initialization \(a t_0=c_0\) therefore gives the stated expansion and arbitrary second-step spike when the admissible first expansion parameter is large.

The bundled exact-rational replay checks representative cases but is not used as an infinite proof.

## Originality

PASS. The 2026 primary paper was inspected at the curvature definitions, exact-proximal reduction, Algorithm 3.1, and both nonconvex and convex convergence theorems. It proves objective descent only from a finite iteration and does not state a finite-transient amplification law. The 2024 NPG1 predecessor was also inspected in full around its algorithm, eventual gamma control, sufficient-decrease result, and convergence theorem. It likewise gives eventual rather than all-iterate descent and does not state the spike-and-reset formula or sharp scalar safety cap.

Targeted database searches for the algorithm names, scalar quadratic specialization, objective overshoot, post-hoc curvature tests, and summable expansion sequences returned only different adaptive or accelerated methods. The main residual originality risk is an older normalized-gradient observation under different terminology.

## Value

PASS. The result identifies a structural distinction in the source algorithm: the curvature test repairs an oversized step only after that step has already affected the objective. The exact scalar law quantifies both the failure mode and the repair, while the sharp cap \(\gamma'_k\le2/c_0-1\) gives a concrete pre-step safeguard on the canonical strongly convex model. This directly explains the source's eventual-descent formulation and is not merely a numerical example.

Same-model review: passed. Independent audit: not yet performed.
