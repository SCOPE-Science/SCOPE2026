# Independent mathematical audit

## correctness

PASS

Exact polynomial Lanczos identity yields y_m(t)=p_(m-1,t)(A)b, with interpolation at Ritz nodes. Strict Ritz upper bound follows because a Krylov polynomial of degree <m cannot isolate L when m<s. Hermite–Genocchi integral gives p_(m-1,t)(x)e^(tx)=1−(−1)^m H_m(t,x), where H_m=t^m prod(x−theta_j)∫_{Delta_m}exp[t Σu_j(x−theta_j)]du. For x>theta_m, H_m grows continuously and strictly from 0 to infinity as t rises; odd m then remains positive while even m crosses uniquely, and H_m grows with extrapolation x, yielding decreasing crossing times. Lagrange coefficients show top-mode relative error has sign (−1)^(m−1) and diverges exponentially at rate L−theta1. Independent interpolation sign tests covered 6 depths; the analytic simplex argument proves the arbitrary-depth result.

## originality

PASS

Published 2026 Resultary two-step positivity horizon covers exactly m=2 and even gives whole-coordinate positivity before its horizon. That special case is expressly excluded from the novel content. Chen–Greenbaum–Musco–Musco (2023) and Druskin (2008) treat Krylov approximation, norm errors, and reduced Jacobi-vector positivity, not the all-m physical top-eigenmode parity. General Hermite–Genocchi interpolation is classical; the structurally meaningful all-depth sign dichotomy requires its specialized Ritz evaluation. The older Druskin primary PDF could only be read through early pages after authorized access; later read was blocked, so its full section coverage remains a residual priority risk.

## value

PASS

The approximation targets a positivity-preserving semigroup but truncation can lose positivity. The theorem gives a complete all-depth parity classification at the stiffest physical eigenmode, a unique time threshold at every even depth, and demonstrates that odd-depth sign preservation is compatible with exponentially bad relative accuracy. This is a directly motivated structural warning for Lanczos exponentials, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
