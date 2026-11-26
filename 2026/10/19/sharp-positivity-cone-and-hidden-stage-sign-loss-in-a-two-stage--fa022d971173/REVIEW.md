# Independent mathematical audit

## correctness

PASS

In the stipulated unshifted ansatz with r=η²<1, consistency gives 2α=1+r, the first-order equation gives (α−r)β=1−r hence β=2, and the second-order equation gives (7+5r)/4=2, hence r=1/5 and α=3/5. This fixes the parameters in the cited stage realization, not all possible nonlinear implementations of the same stability polynomial. With exact past data v₀=y+(h/2)y′−(h²/4)y″+O(h³), v₁=y+hy′+O(h²), and v₂=v₀+h f₀+h f₁ has the needed second-order Taylor expansion after output mixing. At h=0 the roots 1,1/5 give zero stability. For decay, v₂=t v₀, so the characteristic polynomial is ξ²−(3/5)(1+t)ξ+t/5. For −1≤t<1 the strict Schur inequalities hold; for t≤0 the recurrence is nonnegative with at least one positive coefficient. For 0<t<1 both roots are positive and the dominant coefficient has the sign of q−ℓ₋. After division by ℓ₊^n the solution is a convex interpolation between that coefficient and the normalized initial value 1, with positive weight on 1 at each finite index. This proves the stated cone, including the smaller-root equality mode. The polynomial at ξ=1/5 is (2/25)(t−1)<0. Implicit differentiation then makes ℓ₋ strictly increasing in t, with nonzero slope on the upper z-branch, while e^(−z) decreases, giving one crossing there and none on the lower branch. Beyond the crossing, strict negativity occurs for n strictly greater than the log quotient in the original; an integral quotient gives a zero at equality, so floor plus one is essential. Its numerator is log(z−z_*)+O(1), and its denominator has a nonzero smooth limit; this yields the claimed delay. Independent double-precision bisection gives z_*≈3.480888475257458 and coefficient ≈0.331753556229006. The first v₀ is exactly (3e^(−z)−1)y₀/2, proving the claimed overlap of negative stage and positive endpoints.

## originality

PASS

The polynomial ansatz and stage realization are prior, as are general two-step recurrence formulas and SSP criteria. The supported distinct claim is the full positive-start boundary for the specified nondegenerate unshifted branch, with its exact-exponential-starter threshold and all-iteration sign-loss delay, and the separate first-stage obstruction within its endpoint-positive regime. The inspected method papers and closely overlapping indexed claims do not give these results for this recurrence and starter.

## value

PASS

A stable decay test can return positive endpoints while evaluating f at an inadmissible state; the proof identifies a whole interval with this behavior for exact positive data. Separately, the logarithmic delay explains why finite tests can miss endpoint failure near the boundary. The precisely defined unshifted branch, sharp complete starting cone and two distinct practical obstructions make this more than a stability-polynomial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
