# Independent mathematical audit

## correctness

PASS

The empty leave-one-out sketch is zero, so Eq. (3.2) indeed reuses the single probe. Diagonalize A by real orthogonal invariance; write U=ω₁²,V=ω₂² and s²=a(a+ζ),t²=b(b+ζ). The sole nonzero Nyström eigenvalue is (a²U+b²V)/(aU+bV), yielding T=(aU+bV)²/(s²U+t²V). Subtracting T from the exactly unbiased probe of fζ(A) gives UV(at/s−bs/t)²/(s²U+t²V) pointwise. In polar coordinates the radial mean is 2. The angular identity E[cos²θ sin²θ/(s²cos²θ+t²sin²θ)]=1/[2(s+t)²] follows from E[1/(s²cos²θ+t²sin²θ)]=1/(st) and the linear identities for the cos² and sin² numerators; continuity covers s=t. This proves the bias and its equality case. The exact ratio to b/(b+ζ) is bounded by replacing (s+t)² by s² and tends to one when b,ζ→0 at fixed a. The expectation then tends to one because the weak contribution is bounded. For fixed b, the ζ↓0 bias is (a−b)²/(a+b)²; for fixed ζ the b↓0 bias is zero, establishing the stated noncommutation. An independently written 65,536-node quadrant midpoint quadrature matched the predicted expectation within 1.3×10⁻¹² in five cases, including (a,b,ζ)=(2,2,3) and (2,10⁻⁴,10⁻⁴). The frozen verify.py and VERIFICATION.md were inspected, not executed. Finite checks only corroborate the analytic result.

## originality

PASS

The estimator, effective-dimension function, and nonnegative-bias mechanism are established. The exact anisotropic two-eigenvalue bias, its sharp weak-mode comparison and nonuniform rank limit are the distinct contribution supported by the inspected evidence.

## value

PASS

The effective dimension and one-matvec estimator are defined independently by the motivating algorithm. The smallest nonflat spectrum already exposes a sharp failure of uniform weak-mode recovery: shrinking the tail at fixed regularization removes the bias, but shrinking regularization with the tail retains an order-one bias. That distinction is useful when choosing regularization and probe budgets; it is not a statement about variance, higher dimensions or multiple probes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
