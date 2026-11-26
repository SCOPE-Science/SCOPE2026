# Independent mathematical audit

## correctness

PASS

For the reflecting mean-field ODE in Cao–Gong's time normalization, the only mean-feedback derivative is mₕ(eₖ−e₋ₖ)/[k(2k+1)]. The even mass-zero sector is strictly decaying. On the odd sector let A be minus the reflecting generator with a Dirichlet value at zero. Solving its endpoint forcing gives A⁻¹eₖ=2(1,…,k)ᵀ. Conjugation by A⁻¹/² makes the odd Jacobian a symmetric rank-one perturbation of −A; the inertia criterion is 4Σj²/[k(2k+1)]=2(k+1)/3>1, so there is one positive and no zero tangent eigenvalue. The positive eigenfunction is proportional to sinh(jt), where λ=cosh(t)−1; the reflecting endpoint equation gives precisely the displayed unique strictly positive root. The trivial t=0 of the unnormalized equation is not an eigenmode. At k=1 the direct odd Jacobian is −1/2+2/3=1/6. Multiplying the second difference of sinh(jt) by j and telescoping gives the stated finite-sum identity and λₖ=2(1−Rₖ)/(2k+1). The bound λₖ<2/(2k+1) gives tₖ→0. Bounded ktₖ along a subsequence would make the secular left side O(tₖ) and the right side at least 2(k+1)tₖ/3, a contradiction. Hence coth(ktₖ)→1, Rₖ∼1/(ktₖ), tₖ∼√(2/k), and √k(1−kλₖ)→1/√2, with the correct minus sign in λₖ. The sinh quotient at distance floor(x√k) from k tends to exp(−√2 x) for each fixed x≥0. A fresh bounded bisection/residual check for k=1,8,64 had maximum normalized odd eigenvector residuals below 9×10⁻¹⁶; at k=6400 the scaled eigenvalue correction was −0.710238689 and profile at x=1 was 0.244655614, compared with limits −0.707106781 and 0.243116734.

## originality

PASS

The one-dimensional instability itself is demonstrably covered in the same model; it gets no originality credit. The frozen result explicitly does not claim that index as new. The supported distinct assertion is the quantitative root and eigenfunction characterization, the explicit second term in k, and localization on the √k endpoint scale. The inspected overlapping statements do not establish those conclusions.

## value

PASS

For an existing opinion model, knowing that an instability exists does not tell how its linear timescale or the opinions carrying the mode change as the opinion scale grows. The growth law supplies a linear e-folding time of order k with a definite next correction, while the normalized eigenvector confines the growth mode to an endpoint distance of order √k instead of the full O(k) span. These are complementary and structurally useful quantitative answers to a gap left by the index and symmetric-mode results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
