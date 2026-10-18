# Self-review

## Correctness — PASS
The full result is checked against Sun's normalized ground-state representation. Summing the kernel over distinct valuation shells gives the exact exponential Toeplitz form; its principal eigenpair is obtained from the explicit tridiagonal inverse and a uniquely solvable boundary equation. Crucially, the positive radial eigenvector solves the **pointwise** annular Dirichlet equation at every point of each shell. The ground-state factorization with this eigenvector then proves a positive remainder for arbitrary angular modes, not merely an averaged inequality. Positivity gives uniqueness of the radial extremizer. The proof covers complex test functions, all primes, dimensions, allowed orders and widths, and the one-shell boundary case. Numerical checks (858 diagnostics) are supportive rather than universal certificates.

## Originality — PASS, with priority risk
The closest primary paper is Sun, arXiv:2610.04463v1 (October 3, 2026): it establishes the global sharp Hardy inequality and remainder, but not the finite-annulus principal gap. The closest published scientific result (identifier `0555d4d60a6a`, October 11, 2026) establishes the exact radial shell energy and two nonexact spectral bounds; its stated scope excludes both exact width constants and nonradial optimality. Classical Kac--Murdock--Szegő matrix theory is appropriately acknowledged as an algebraic ingredient. No directly covering all-function p-adic annular theorem was found in the checked source set. General ground-state and principal-eigenvalue theory may contain equivalent applications, and older full texts remain a priority risk; independent review is necessary.

## Mathematical value — PASS
Exact positive stability improvements for compact annuli quantify how the global nonattained Hardy constant becomes coercive under scale confinement. The new result settles this natural sharp constant without any radiality restriction, classifies all equality cases, and gives an exact stability identity for nonradial deviations; the sharp width coefficient is useful for finite-scale limiting arguments. Neither a mere numerical value nor a routine parameter relabeling is the contribution.

## Scope and limitations
The result is restricted to the quadratic energy on a union of complete consecutive p-adic valuation shells and does not cover arbitrary shell masks, nonlinear exponent ranges or general ultrametric groups. The older hierarchical Schrödinger source was compared at abstract level only. Its possible uninspected overlap is a residual risk.

Self-review: passed. Independent audit: not yet performed.
