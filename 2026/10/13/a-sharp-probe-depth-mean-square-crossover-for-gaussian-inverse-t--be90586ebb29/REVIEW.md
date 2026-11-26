# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 39–119. Rotational invariance gives Q=R²/(a cos²θ+b sin²θ); the tangent substitution and a common spectral shift give angular moments 1/√(ab) and (a+b)/(2(ab)^{3/2}). The χ²₂ radial moments 2 and 8 give E Q=2/√(ab), Var Q=4(a+b)/(ab)^{3/2}−4/(ab). The squared bias is (u−1)^4/(b²u^4). Two-step nonbreakdown occurs almost surely and gives gᵀA⁻¹g, with variance 2(a⁻²+b⁻²). At the stated fixed budget the difference deep minus shallow is (u−1)^4(B*−B)/(B b²u^4). Writing z=1/(u−1) gives B*=4(1+3z+4z²+2z³+z⁴), strictly decreasing from infinity to 4 as u increases. The B=2 half-deep gap is 2(u−1)²/(b²u³), strictly positive. A separate scalar bisection gives κ₈=26.08108750465537. VERIFICATION.md and verify.py were read; the script was not run. The proof covers exactly the two allocations with independent unnormalized real Gaussian probes, distinct eigenvalues and exact arithmetic, not repeated-eigenvalue breakdown or other oracle algorithms.

## originality

PASS

The inspected sources establish the ingredients and analyze adjacent tradeoffs, but do not cover the exact biased-versus-unbiased equal-product Gaussian inverse-trace crossover or its uniform two-product inequality. Pass is limited to that benchmark, not to inverse-trace SLQ or the generic probe-depth tradeoff.

## value

PASS

The two-dimensional distinct-spectrum case is the first setting where increasing quadrature depth to two removes approximation bias exactly while halving the number of Gaussian probes. The exact curve distinguishes when that removes enough bias to justify the added sampling variance; exactness alone does not favor deep at B=4 even at arbitrarily large finite condition number. The result gives a useful analytic benchmark for depth/probe allocation and MSE analysis, not an optimal oracle-complexity claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
