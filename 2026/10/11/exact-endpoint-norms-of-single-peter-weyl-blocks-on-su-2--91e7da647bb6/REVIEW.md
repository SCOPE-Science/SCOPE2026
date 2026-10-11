# Same-model review

## Correctness
**PASS.** The projection kernel is the standard central Peter--Weyl idempotent \(m\chi_r\). Both endpoint convolution norms equal its \(L^1\) mass. Weyl integration reduces that mass exactly to \(\frac{2m}\pi\int_0^\pi|\sin(m\theta)|\sin\theta\,d\theta\), and splitting at all \(m-1\) interior zeros gives the cotangent sum without approximation. The trivial case \(m=1\) is handled separately. The standalone verifier checks the signed-integral identity through \(m=500\) and direct quadrature at representative dimensions, but the universal theorem rests on the analytic derivation.

## Originality
**PASS, with stated residual risk.** Hare's full paper uses exactly the same \(SU(2)\) isotypic spaces and Peter--Weyl block decomposition, but its Section 2(4) concerns Littlewood--Paley estimates and does not state an endpoint norm or an exact character-mass evaluation. Giulini--Travaglini and Meaney concern Lebesgue constants of partial-sum schemes on compact groups, not the exact norm of one irreducible block. published-finding corpus and web searches under projection, character-norm, Peter--Weyl, Lebesgue-constant, and explicit-cotangent aliases returned no covering statement. The remaining risk is that the elementary character integral has appeared elsewhere without the operator formulation.

## Value
**PASS.** A single irreducible Peter--Weyl block is the atomic spectral projection for nonabelian compact Fourier analysis. The formula gives its exact endpoint stability constant in every dimension and shows linear growth \((8/\pi^2)m\), in sharp contrast with norm-one single-character projections on compact abelian groups. This supplies a natural quantitative baseline for endpoint instability before any multi-block partial summation is introduced.

Same-model review: passed. Independent audit: not yet performed.
