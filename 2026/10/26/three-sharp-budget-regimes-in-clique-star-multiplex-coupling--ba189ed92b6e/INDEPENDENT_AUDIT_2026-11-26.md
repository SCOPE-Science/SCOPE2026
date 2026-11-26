# Independent mathematical audit

## correctness

PASS

For the unnormalized Laplacian, the Rayleigh minimum on the space orthogonal to constants is concave in the weights, so averaging the leaf permutations preserves the attainable maximum. The constant-leaf sector has the same within-layer quotient for clique and star and splits into the symmetric 0,n eigenvalues and the antisymmetric two-by-two block A. Zero-sum leaf contrasts give n−2 copies of C with lower eigenvalue ν<n. Along x=B−(n−1)y, the lower eigenvalue μ of A has derivative zero at y=B/n and strictly negative second derivative −8n²(n−1)/(δ²+4(n−1))^(3/2); ν is strictly increasing. At uniformity, ν≥2B/n exactly when B≤n²/(n+1), with the squaring sign valid at and below the threshold. Equality of the opposite-layer-constant Rayleigh test enforces equality of all weights. For B>B1, the optimum is the crossing to the right of uniformity, or the endpoint x=0 when no earlier crossing occurs. With t=ν, inversion gives y=(t−1)(n−t)/(n+1−2t); the determinant at x=0 has sign t−2 since the upper A eigenvalue is at least n−1>t. At t=2, y=(n−2)/(n−3) if n≥4, and t<2 at every finite y when n=3. The positive factor 1+2y−t=(t−1)(n−1)/(n+1−2t) yields the stated x(t) at the crossing. For unequal leaf weights, an orthonormal basis of leaf contrasts paired with a lower-eigenvalue vector (a,b) of C at the average leaf weight has mean Rayleigh quotient ν((B−x)/(n−1)). Attainment at and above B2 forces x=0; minimum equality on the whole test space then implies (y_i−ȳ)(a−b)θ_i=0 for every contrast θ, hence equal leaf weights as a≠b. This includes B=B2. In the n=3 crossing, x is bounded by its value at t=2n/(n+1) (the three positive factors in x(t) give strict decrease), so y→∞ and x→0. The large-budget limits follow. The frozen verify_multiplex.py uses finite rational checks and full-matrix Jacobi calculations (with symmetric neighboring designs); they are not needed for global or infinite claims and were not replayed.

## originality

PASS

The general one-to-one problem, uniform-optimum bound and first-transition criterion are established prior work. No inspected prior statement gives the exact post-uniform clique–star allocation, finite second threshold and high-budget optimizer rigidity, or the three-node exception. This is a bounded statement-level comparison, not a publication-priority claim.

## value

PASS

For a standard budgeted spectral design problem, the solution identifies exactly when increasing the budget makes one designated connection dispensable and proves that every optimizer deletes it thereafter. The sharp threshold, explicit intermediate allocation and absence of finite extinction on the three-node layers are natural, useful constraints, not consequences of the prior uniform bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
