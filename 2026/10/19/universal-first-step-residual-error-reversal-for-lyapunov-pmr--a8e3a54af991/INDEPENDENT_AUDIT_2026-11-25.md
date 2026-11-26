# Independent mathematical audit

## correctness

PASS

Lund–Palitta's scalar harmonic correction is −b²/a. Writing Hv=av+bw with w orthonormal to v gives residual square (1−2ay)²+2b²y², with minimum at the stated MR coefficient. PMR and Galerkin lie on opposite sides of MR and the ratio of their distances to MR is a²/(a²+b²)<1 for b>0. In an eigenbasis of H, let D,D′ be independent eigenvalue draws with masses equal to the squared components of v. The exact entry formula X_jk=v_j v_k/(H_jj+H_kk) gives ⟨X,vvᵀ⟩=E[1/(D+D′)]>1/(2a) by strict Jensen for b>0. Thus the Frobenius-error quadratic decreases throughout the interval of the three coefficients, yielding the displayed solution-error order. If b=0 all three recover the exact solution. In the exhibited family the leading Galerkin error is K⁻¹ times the matrix with entries (1/2,−1/2;−1/2,0), whereas PMR and MR errors tend to 1/4 and 1/6. Substitution of a→1 and b²→1 gives both stated residual ratios. The displayed inequalities are correct; 'opposite directions' is informal, since both comparisons to Galerkin reverse but MR still beats PMR on both metrics. The replay path is the supplied exact-rational verifier, inspected but not executed; it hard-codes extraction rules and is not a substitute for the analytic check.

## originality

PASS

Supported for the combined strict first-step rank-one Frobenius comparisons and the explicit unbounded error-ratio witness with lower residual. It is not a claim to the PMR method, MR principle, Galerkin's energy optimality, or the general distinction between residual and error.

## value

PASS

The theorem and witness answer a concrete diagnostic question for a practical class of solvers: in the simplest common Krylov trial space, even a fixed-factor better harmonic residual can coexist with an arbitrarily worse actual Frobenius error. Showing strict universal rank relations and unbounded distortion with only two eigenvalues is stronger and more useful than saying that ill-conditioning can make residuals misleading.

The dated certificate retains the supplied scientific assessment, sources and limitations.
