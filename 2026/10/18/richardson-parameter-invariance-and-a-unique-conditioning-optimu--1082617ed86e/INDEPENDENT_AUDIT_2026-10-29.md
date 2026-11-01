# Independent mathematical audit

## correctness

PASS

Since P=[-omega r,-omega(r-omega Ar)] with omega>0, its range is exactly span{r,Ar}. x_pre-x=omega r lies in the same range, so the residual-minimizing correction solves the identical affine trial-space problem as GMRES(2), independent of the weight. Independence of r and Ar plus invertibility of A implies Ar,A²r independent and G positive definite. Direct Gram expansion gives entries omega²[u,u-omega v;u-omega v,u-2omega v+omega²w], determinant omega^6 Delta>0, trace omega²(2u-2omega v+omega²w). For eigenvalue ratio kappa≥1, T=trace/sqrt(det)=sqrt(kappa)+1/sqrt(kappa) is strictly increasing in kappa. Consequently T=(2u/omega-2v+w omega)/sqrt(Delta) and its completed-square difference from T_star is w(omega-omega_star)²/(omega sqrt(Delta)); this proves one strict global optimum over omega>0. T_star=2 precisely when v=sqrt(uw/2); can verify by squaring in |v|<sqrt(uw). As T tends to infinity at both ends, kappa~T², giving the two claimed sharp asymptotics. Each next cycle has same identity when the pair remains independent, and an eigenvector or zero residual is excluded/terminating. Independent exact Fraction implementation of a different two-column residual projection verified 1399 assertions for 45 nonsingular 3x3 systems with seven omega values, including nonsymmetric systems. A 2x2 explicit equality case gave G=I and the 3x3 SPD stability-interval example gave 2u/w=835/428. These finite tests are corroboration only.

## originality

PASS

Best-of-knowledge qualification: the exact two-grid prolongation is introduced by Adler et al. 2026, and GMRES residual minimization, Krylov equivalences and general conditioning methods are all prior. Independently checked the full source paper, He 2026, Pollock–Rebholz 2022, De Sterck–He–Krzysik 2021, and the closely related He 2025 aNGMRES theorem. The earlier aNGMRES(m,m+1) result itself yields GMRES(2) for m=1, but uses a different algorithm and does not analyze the later TGA Gram with scalar presmoother. No inspected source covers the combined TGA-specific all-positive-omega unique normal-conditioning optimum/equality/sharp endpoint asymptotics. This does not establish worldwide priority: the result is algebraically derivable from source definitions and an uninspected general basis-conditioning theorem might dominate.

## value

PASS

This specific two-grid accelerator has two physically meaningful choices that are often conflated: the scalar smoother weight and the arithmetic conditioning of the coarse solve. The theorem establishes an exact search-space invariance across all positive weights while isolating a unique best-conditioned coarse normal system, a strict penalty for deviation, a realizable perfect-conditioning equality case and sharp quadratic degeneration at the weight extremes. For a natural recently introduced numerical method, identifying a free algorithmic parameter with no exact iteration effect but a precisely quantifiable normal-matrix conditioning effect is independently useful for fair comparisons, benchmarking and parameter selection. The optimum can lie outside the conventional standalone Richardson stability interval, a substantive implementation caveat. No unsupported claim of faster finite-precision performance or general solver convergence is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
