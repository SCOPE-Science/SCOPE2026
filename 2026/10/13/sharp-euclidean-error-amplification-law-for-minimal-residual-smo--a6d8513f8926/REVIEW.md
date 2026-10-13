# Self-review

## Correctness
PASS. Minimal residual smoothing is reconstructed exactly as the projection
\[
P_d
=
I-
\frac{d\,d^{\mathsf T}A^2}
{d^{\mathsf T}A^2d}.
\]
Its Euclidean norm is the codimension-one oblique-projection factor
\[
\frac{\|d\|_2\|A^2d\|_2}{d^{\mathsf T}A^2d}.
\]
A sharp spectral secant inequality for \(A^2\) gives the global envelope
\[
\frac{\kappa^2+1}{2\kappa},
\]
and a two-eigenvalue construction attains equality. The explicit family also verifies strict residual decrease while Euclidean error grows. The packaged checker replays these identities exactly.

## Originality
PASS with explicit residual risk. Zhou and Walker's full paper already defines minimal residual smoothing and proves monotone residual norms; those facts are treated as prior work. Weiss's abstract already states the broader fact that residual decrease can accompany error increase.

The new claim is the exact local solution-error amplification law for minimal residual smoothing on SPD systems, its condition-number envelope, the equality family, and dimension-two minimality. Targeted published-record and web searches found no implication-equivalent statement. The strongest remaining risk is the inaccessible body of Weiss's closely related 1994 paper and older abstract projection literature.

## Value
PASS. Minimal residual smoothing deliberately improves the quantity commonly monitored for convergence. The theorem gives the exact conditioning-dependent price that can be paid in actual Euclidean solution error and shows that this price is attained in the smallest nontrivial dimension. For large \(\kappa\), the one-step mismatch is on the order of \(\kappa/2\), making the distinction practically meaningful.

## Closest literature and limitations
The closest full source is Zhou and Walker's residual-smoothing paper. The closest broader source is Weiss's error-minimizing Krylov paper, whose accessible abstract states the qualitative residual/error mismatch but whose full body was unavailable through the inspected route. The theorem is local and allows an unrestricted incoming direction; specific iterative methods, nonsymmetric systems, weighted smoothing, block smoothing, and finite precision are outside scope.

Self-review: passed. Independent audit: not yet performed.
