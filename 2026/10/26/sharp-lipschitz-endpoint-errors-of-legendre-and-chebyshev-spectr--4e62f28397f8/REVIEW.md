# Scientific review

## Correctness — PASS
Both finite-degree constants are exact operator dual norms on the real Lipschitz unit ball. The proof verifies normalizations of the two reproducing kernels, reduces the errors to integrals of arbitrary almost-everywhere derivatives with magnitude at most one, and gives explicit extremizers. Legendre telescoping yields the Jacobi absolute integral. The Jacobi bulk oscillation law with endpoint control gives the evaluated \(\sqrt{2/\pi}\) coefficient. The Chebyshev sine-tail Abel estimate, with a separately controlled small-angle region, gives \(8/\pi^2\). The standalone script independently evaluates both finite-degree integrals and checks the degree-two Legendre radical. Finite numerical experiments are not the proof of either infinite limit.

## Originality — PASS, with residual risk
The closest examined general result (Wang, arXiv:2001.01985) develops Peano kernels and rates for smoother, fixed functions; it does not calculate the sharp uniform Lipschitz-unit-ball endpoint norm, its extremizers, or the separate Chebyshev constant. The papers arXiv:math/0111252 and arXiv:1502.07191 supply Jacobi asymptotic theory, not the claimed endpoint-error comparison. Existing similar database entries involve different Fourier/projector spaces, unrelated endpoint norms, or affine detrending at one degree. An earlier specialized computation, if unindexed, remains possible; none was established by the actual comparisons. The general Peano-kernel theorem itself is known and not claimed as novel.

## Mathematical value — PASS
For a natural fixed regularity class, the theorem determines the exact worst possible endpoint output error for two standard orthogonal spectral truncations, at every degree, with attaining nonsmooth inputs. Its sharp limiting coefficients establish the structural fact that choosing the orthogonality weight changes the order of worst-case endpoint error, from a square-root rate to an inverse-degree rate. This is sharper than generic approximation estimates and directly informs the stability of endpoint recovery from truncated polynomial expansions.

## Limits and risk
Only endpoint evaluation is treated. Finite-degree comparison for arbitrary orders is not claimed. The asymptotic constants depend on standard fixed-parameter Jacobi endpoint estimates and elementary Fourier summation, not on external independent validation. Possible unindexed earlier exact constants remain a novelty risk.

Self-review: passed. Independent audit: not yet performed.
